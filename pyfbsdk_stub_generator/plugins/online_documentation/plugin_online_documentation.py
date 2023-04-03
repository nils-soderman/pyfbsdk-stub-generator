import os

from types import ModuleType
from importlib import reload

from .documentation_scraper import table_of_contents

from .documentation_scraper.page_parser import MemberItem
from ..plugin import PluginBaseClass
from ...module_types import StubClass, StubFunction, StubParameter, StubProperty

reload(table_of_contents)


class PluginOnlineDocumentation(PluginBaseClass):
    Threading = False
    
    def __init__(self, Version: str, Module: ModuleType):
        super().__init__(Version, Module)

        # Initialize the documentation
        self.Documentation = table_of_contents.Documentation(self.ModuleName, Version, self.bDevMode)

    def PatchClass(self, Class: StubClass):
        ParsedPage = self.Documentation.GetParsedPage(Class.Name)
        if not ParsedPage:
            return

        Class.DocString = ParsedPage.DocString

        for FunctionGroup in Class.StubFunctions:
            FirstFunction = FunctionGroup[0]
            FunctionName = FirstFunction.Name
            Members = ParsedPage.GetMembersByName(FunctionName)
            if Members:
                PatchFunction(FunctionGroup, Members)

        for Property in Class.StubProperties:
            Members = ParsedPage.GetFirstMemberByName(Property.Name)
            if Members:
                Property.DocString = Members.DocString
                Property.Type = Members.Type


def PatchFunction(Function: list[StubFunction], Members: list[MemberItem]):
    if len(Members) > 1:
        print(f"Found multiple members for {Function[0].Name}")
    # for Function in Function.Functions:
    #     Function.DocString = Member.DocString
