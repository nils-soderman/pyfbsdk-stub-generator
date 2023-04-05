from __future__ import annotations

import string

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


def ParsePage(PageName: str, PageHtmlContent: str, ) -> DocumentationParsedPage:
    Parser = BeautifulSoup(PageHtmlContent, "html.parser")

    DescriptionHtml = Parser.find("div", class_ = ClassNames.TextBlockDescription)
    Description = GetSafeText(DescriptionHtml.get_text()) if DescriptionHtml else ""

    MemberItems = []
    for Item in Parser.find_all("div", class_ = ClassNames.Items):
        ItemName = ""
        ItemType = ""
        ItemDocumentation = ""

        DocumentationHtml = Item.find("div", class_ = ClassNames.Doc)
        if DocumentationHtml:
            ItemDocumentation: str = GetSafeText(DocumentationHtml.get_text())

        NameTable = Item.find("table", class_ = ClassNames.ItemName)
        if NameTable:
            NameHtml = NameTable.find("td", class_ = ClassNames.ItemName)
            if NameHtml:
                ItemName: str = GetSafeText(NameHtml.get_text())
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
                    ParameterName: str = GetSafeText(ParameterNameHtml.get_text())
                    ParameterType: str = GetSafeText(ParameterTypeHtml.get_text())

                    ParamDefaultValue = None
                    if "=" in ParameterName:
                        ParameterName, _, ParamDefaultValue = ParameterName.partition("=")
                        ParamDefaultValue = ParamDefaultValue.strip()

                    Parameters.append(Parameter(ParameterName.strip(), ParameterType, ParamDefaultValue))

        MemberItems.append(MemberItem(ItemName, ItemType, ItemDocumentation, Parameters))

    return DocumentationParsedPage(PageName, Description.strip(), MemberItems)


def GetSafeText(Text: str):
    # Remove any non-breaking spaces and strip the text of whitespace and commas
    return Text.replace('\xa0', ' ').strip(string.whitespace + ",")
