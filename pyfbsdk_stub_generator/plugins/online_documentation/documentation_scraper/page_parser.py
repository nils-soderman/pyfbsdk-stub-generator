from __future__ import annotations

import string
import re

from dataclasses import dataclass
from importlib   import reload

import markdownify
from bs4 import BeautifulSoup, Tag, NavigableString

from . import documentation_urls as urls
from . import documentation_cache as cache

reload(cache)
reload(urls)


class ClassNames:
    Items = "memitem"
    Doc = "memdoc"
    ItemName = "memname"
    ParameterName = "paramname"
    ParameterType = "paramtype"
    TextBlockDescription = "textblock"
    ParameterTalble = "params"


@dataclass
class Parameter:
    Name: str | None
    Type: str | None
    DefaultValue: str | None = None


@dataclass
class MemberItem:
    Name: str
    Type: str
    DocString: str
    Parameters: list[Parameter]


class DocumentationParsedPage():
    def __init__(self, Name: str, DocString: str, Members: list[MemberItem]):
        self.Name = Name
        self.DocString = DocString
        self.Members = Members

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}<{self.Name}>"

    def GetFirstMemberByName(self, Name: str) -> MemberItem:
        for Member in self.Members:
            if Member.Name == Name:
                return Member

        return None

    def GetMembersByName(self, Name: str):
        return [x for x in self.Members if x.Name == Name]


def ParsePage(PageName: str, PageHtmlContent: str, BaseURL: str) -> DocumentationParsedPage:
    """
    Parse the HTML content of a page and return a DocumentationParsedPage object.

    ### Parameters:
        - `PageName`: The name of the page.
        - `PageHtmlContent`: The HTML content of the page.
        - `BaseURL`: The base URL to be used to resolve relative URLs.
    """
    DocStringParser = DocstringParser(BaseURL)
    Parser = BeautifulSoup(PageHtmlContent, "html.parser")

    DescriptionHtml = Parser.find("div", class_ = ClassNames.TextBlockDescription)
    Description = DocStringParser.ParseDocString(DescriptionHtml) if DescriptionHtml else ""

    MemberItems = []
    Item: Tag | NavigableString
    for Item in Parser.find_all("div", class_ = ClassNames.Items):
        ItemName = ""
        ItemType = ""
        ItemDocumentation = ""

        DocumentationHtml = Item.find("div", class_ = ClassNames.Doc)
        if DocumentationHtml:
            ItemDocumentation: str = DocStringParser.ParseDocString(DocumentationHtml)

        NameTable = Item.find("table", class_ = ClassNames.ItemName)
        if NameTable:
            NameHtml = NameTable.find("td", class_ = ClassNames.ItemName)
            if NameHtml:
                ItemName: str = GetSafeText(NameHtml.get_text())
                if " " in ItemName:
                    ItemType, _, ItemName = ItemName.partition(" ")
                    ItemName = ItemName.strip()
                    ItemType = ItemType.strip()

            if ItemName == "PlotToCameraSwitcher":
                print(DocumentationHtml.prettify())

            # Find all parameters
            Parameters = []
            for Row in NameTable.find_all("tr"):
                ParameterNameHtml = Row.find("td", class_ = ClassNames.ParameterName)
                ParameterTypeHtml = Row.find("td", class_ = ClassNames.ParameterType)
                if ParameterNameHtml and ParameterTypeHtml:
                    ParameterName: str = GetSafeText(ParameterNameHtml.get_text())
                    ParameterType: str = GetSafeText(ParameterTypeHtml.get_text())

                    ParamDefaultValue = None
                    if "=" in ParameterName:
                        ParameterName, _, ParamDefaultValue = ParameterName.partition("=")
                        ParamDefaultValue = ParamDefaultValue.strip()

                    ParameterName = ParameterName.strip()
                    if not ParameterName:
                        if ParameterType.startswith("p"):
                            ParameterName = ParameterType
                            ParameterType = ""
                        else:
                            ParameterName = None

                    Parameters.append(Parameter(ParameterName, ParameterType, ParamDefaultValue))

        MemberItems.append(MemberItem(ItemName, ItemType, ItemDocumentation, Parameters))

    return DocumentationParsedPage(PageName, Description.strip(), MemberItems)


def GetSafeText(Text: str):
    # Remove any non-breaking spaces and strip the text of whitespace and commas
    return Text.replace('\xa0', ' ').strip(string.whitespace + ",")


class DocstringParser(markdownify.MarkdownConverter):
    def __init__(self, UrlBase: str, **options):
        super().__init__(**options)

        self.UrlBase = UrlBase  # Base for any relative url's found

    def ParseDocString(self, DescriptionHtml: Tag | NavigableString):
        return self.convert(str(DescriptionHtml))

    def convert_a(self, el: Tag, text, convert_as_inline):
        """ Make sure all <a> tags have a full URL. """
        Href = el.get("href")

        # Example URLs are broken in the 2024 docs. Resolve them manually.
        SampleUrlPrefix = "ms-its:MotionBuilder_SDK_Samples.chm::"
        if Href.startswith(SampleUrlPrefix):
            # From: ms-its:MotionBuilder_SDK_Samples.chm::/Scripts/BasicOperations/FBSystemEvents.html
            # To: _basic_operations_0c_f_b_system_events_8py-example.html
            Suffix = "_8py-example.html"
            ScriptsFolder = "Scripts/"
            if ScriptsFolder in Href:
                RelativeUrl = Href.partition(ScriptsFolder)[2]
                ConvertedString: str = re.sub(r'(?<!^)(?=[A-Z])', '_', RelativeUrl).lower()  # Convert from PascalCase to snake_case
                ConvertedString = ConvertedString.replace("/", "_0c")  # Replace the slashes with _0c
                ConvertedString = ConvertedString.partition(".")[0]  # Remove the extension (.html)
                Href = f"_{ConvertedString}{Suffix}"

        if Href and not Href.startswith("http"):
            el["href"] = f"{self.UrlBase}{Href}"

        return markdownify.markdownify(str(el))

    # -------------------------
    #      Parameter Lists
    # -------------------------

    def convert_dt(self, el: Tag, text, convert_as_inline):
        """ Convert all <dt> tags to a headers. """
        HeaderText = markdownify.markdownify(str(el))
        return f"### {HeaderText}:\n"

    def convert_table(self, el: Tag, text, convert_as_inline):
        # Check if element has the class name for a parameter list
        ElementClassNames = el.get("class")
        if ElementClassNames and ClassNames.ParameterTalble in ElementClassNames:
            ParameterLines = []
            Row: Tag
            for Row in el.find_all("tr"):
                Text = ""

                Cell: Tag
                for Index, Cell in enumerate(Row.find_all("td")):
                    if Index == 0 and ClassNames.ParameterName in Cell.get("class"):
                        Text = f"    - {GetSafeText(Cell.get_text())}: "
                    else:
                        # TODO: Might not ned to run mardkdownify on the cell text, just use the text instead
                        Text += markdownify.markdownify(str(Cell)).strip(string.whitespace + "|")

                ParameterLines.append(Text)
            return "\n".join(ParameterLines)

        return super().convert_table(el, text, convert_as_inline)
