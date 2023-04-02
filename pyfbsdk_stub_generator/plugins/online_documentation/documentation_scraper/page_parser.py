from __future__ import annotations

from dataclasses import dataclass
from importlib   import reload

from bs4 import BeautifulSoup

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


@dataclass
class Parameter:
    Name: str
    Type: str
    DefaultValue: str = None


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

    def GetMemberByName(self, Name: str) -> MemberItem:
        for Member in self.Members:
            if Member.Name == Name:
                return Member

        return None


def ParsePage(PageName: str, PageHtmlContent: str, ) -> DocumentationParsedPage:
    Parser = BeautifulSoup(PageHtmlContent, "html.parser")

    DescriptionHtml = Parser.find("div", class_ = ClassNames.TextBlockDescription)
    Description = DescriptionHtml.get_text() if DescriptionHtml else ""

    MemberItems = []
    for Item in Parser.find_all("div", class_ = ClassNames.Items):
        ItemName = ""
        ItemType = ""
        ItemDocumentation = ""

        DocumentationHtml = Item.find("div", class_ = ClassNames.Doc)
        if DocumentationHtml:
            ItemDocumentation: str = DocumentationHtml.get_text().strip()

        NameTable = Item.find("table", class_ = ClassNames.ItemName)
        if NameTable:
            NameHtml = NameTable.find("td", class_ = ClassNames.ItemName)
            if NameHtml:
                ItemName: str = NameHtml.get_text().strip()
                if " " in ItemName:
                    ItemType, _, ItemName = ItemName.partition(" ")
                    ItemName = ItemName.strip()
                    ItemType = ItemType.strip()

            # Find all parameters
            Parameters = []
            for Row in NameTable.find_all("tr"):
                ParameterNameHtml = Row.find("td", class_ = ClassNames.ParameterName)
                ParameterTypeHtml = Row.find("td", class_ = ClassNames.ParameterType)
                if ParameterNameHtml and ParameterTypeHtml:
                    ParameterName: str = ParameterNameHtml.get_text()
                    ParameterType: str = ParameterTypeHtml.get_text()

                    ParamDefaultValue = None
                    if "=" in ParameterName:
                        ParameterName, _, ParamDefaultValue = ParameterName.partition("=")
                        ParamDefaultValue = ParamDefaultValue.strip()

                    Parameters.append(Parameter(ParameterName.strip(), ParameterType.strip(), ParamDefaultValue))

        MemberItems.append(MemberItem(ItemName, ItemType, ItemDocumentation, Parameters))

    return DocumentationParsedPage(PageName, Description.strip(), MemberItems)
