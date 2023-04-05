from __future__ import annotations

import os

from types import ModuleType
from importlib import reload

from .documentation_scraper import table_of_contents

from .documentation_scraper.page_parser import MemberItem
from ..plugin import PluginBaseClass
from ...module_types import StubClass, StubFunction, StubParameter, StubProperty

reload(table_of_contents)


TRANSLATION_TYPE = {
    "long": "float",
    "double": "float",
    "kInt64": "int",
}

TRANSLATION_VALUES = {
    "nullptr": "None",
}


class PluginOnlineDocumentation(PluginBaseClass):
    Threading = False

    def __init__(self, Version: int, Module: ModuleType, EnumList: list[StubClass], ClassList: list[StubClass], FunctionGroupList: list[list[StubFunction]]):
        super().__init__(Version, Module, EnumList, ClassList, FunctionGroupList)

        # Initialize the documentation
        self.Documentation = table_of_contents.Documentation(self.ModuleName, Version, self.bDevMode)

        # Parse the first documentation page to get the list of all pages
        for FunctionGroup in FunctionGroupList:
            Function = FunctionGroup[0]
            self.FunctionPage = self.Documentation.GetParsedPage(Function.Name)
            if self.FunctionPage:
                break

    def PatchClass(self, Class: StubClass):
        ParsedPage = self.Documentation.GetParsedPage(Class.Name)
        if not ParsedPage:
            return

        Class.DocString = ParsedPage.DocString

        # Properties
        for Property in Class.StubProperties:
            Members = ParsedPage.GetFirstMemberByName(Property.Name)
            if Members:
                Property.DocString = Members.DocString
                Property.Type = Members.Type

        # Methods
        for FunctionGroup in Class.StubFunctions:
            FirstFunction = FunctionGroup[0]
            FunctionName = FirstFunction.Name

            # In the documentation, the constructor is called the same as the class
            if FunctionName == "__init__":
                FunctionName = Class.Name

            Members = ParsedPage.GetMembersByName(FunctionName)
            if Members:
                _PatchFunctions(FunctionGroup, Members)

    def PatchFunctionGroup(self, FunctionGroup: list[StubFunction]):
        if not FunctionGroup:
            return  # TODO: This should never happen, look into it

        if self.FunctionPage:
            Members = self.FunctionPage.GetMembersByName(FunctionGroup[0].Name)
            if Members:
                _PatchFunctions(FunctionGroup, Members)


def _PatchFunctions(Functions: list[StubFunction], Members: list[MemberItem]):
    # If we only have one function and one member, we don't need to figure out which one is the correct one
    if len(Functions) == 1 and len(Members) == 1:
        PatchFunction(Functions[0], Members[0])
        return


def PatchFunction(Function: StubFunction, DocMember: MemberItem):
    Function.DocString = DocMember.DocString

    if not IsTypeDefined(Function.ReturnType):
        Function.ReturnType = DocMember.Type

    FunctionParameters = Function.GetParameters()
    DocumentationParameters = DocMember.Parameters
    # Documentation does not include the self parameter for methods
    if Function.bIsMethod:
        FunctionParameters = FunctionParameters[1:]

    # The documentation includes an additional empty parameter for functions directly in the module
    elif len(DocumentationParameters) - 1 == len(FunctionParameters):
        DocumentationParameters = DocumentationParameters[:-1]

    if not FunctionParameters:
        return  # If there are no parameters, we don't need to do anything else

    # Function that has different number of parameters than the documentation requires a more careful patch to avoid patching the wrong parameter
    # It's better to not patch the parameters than patching it incorrectly, which could cause a lot of confusion
    bSafePatch = len(FunctionParameters) != len(DocumentationParameters)

    for FunctionParameter, DocParameter in zip(FunctionParameters, DocumentationParameters):
        if bSafePatch:
            # Variable Types must match when doing a safe patch, otherwise we might be patching the wrong parameter
            if FunctionParameter.Type != DocParameter.Type:
                continue

        # Name
        if FunctionParameter.Name.startswith("arg"):
            NewName = DocParameter.Name

            # Remove the "p" prefix from the parameter name, since arguments cannot be referenced as keywords
            if NewName.startswith("p") and not NewName[1].isnumeric():
                NewName = NewName.lstrip("p")

            FunctionParameter.Name = NewName

        # Type
        PatchParameterType(FunctionParameter, DocParameter.Type)

        # Default value
        PatchPropertyDefaultValue(FunctionParameter, DocParameter.DefaultValue)


def PatchParameterType(Parameter: StubParameter, Type: str) -> str:
    if IsTypeDefined(Parameter.Type):
        return

    if Type in TRANSLATION_TYPE:
        Type = TRANSLATION_TYPE[Type]

    Parameter.Type = Type


def PatchPropertyDefaultValue(Parameter: StubParameter, DefaultValue: str | None):
    if Parameter.DefaultValue is None or DefaultValue is None:
        return

    # Replace namespace C++ syntax with Python
    if "::" in DefaultValue:
        DefaultValue = DefaultValue.replace("::", ".")

    if DefaultValue in TRANSLATION_VALUES:
        DefaultValue = TRANSLATION_VALUES[DefaultValue]

    Parameter.DefaultValue = DefaultValue


def IsTypeDefined(Type: str | None) -> bool:
    if not Type:  # TODO: Hmmm ?
        return True
    return Type != "object"
