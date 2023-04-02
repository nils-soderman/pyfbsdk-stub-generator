import os

from types import ModuleType
from importlib import reload

from .documentation_scraper import table_of_contents

from .documentation_scraper.page_parser import MemberItem
from ..plugin import PluginBaseClass
from ...module_types import StubClass, StubFunction, StubParameter, StubProperty

reload(table_of_contents)

class PluginOnlineDocumentation(PluginBaseClass):
    def __init__(self, Version: str, Module: ModuleType):
        super().__init__(Version, Module)

        # Initialize the documentation
        self.Documentation = table_of_contents.Documentation(self.ModuleName, Version, self.bDevMode)

    def PatchClass(self, Class: StubClass):
        ParsedPage = self.Documentation.GetParsedPage(Class.Name)
        if not ParsedPage:
            return

        Class.DocString = ParsedPage.DocString

        for Function in Class.StubFunctions:
            Member = ParsedPage.GetMemberByName(Function.Name)
            if Member:
                PatchFunction(Function, Member)
                
        for Property in Class.StubProperties:
            Member = ParsedPage.GetMemberByName(Property.Name)
            if Member:
                Property.DocString = Member.DocString
                Property.Type = Member.Type


def PatchFunction(Function: StubFunction, Member: MemberItem):
    Function.DocString = Member.DocString
