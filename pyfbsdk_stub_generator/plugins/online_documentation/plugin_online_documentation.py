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
    "kULong": "int",
    
    "kReference": "int",
    "FBkReference": "int",
    
    "FBAudioFmt": "int",
    
    "FBTVector": "FBVector4d",
    "FBQuaternion": "FBVector4d",
    "FBRVector": "FBVector3d",
    "FBColorF": "FBColor"
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

    def PatchEnum(self, Enum: StubClass):
        ParsedPage = self.Documentation.GetParsedPage(Enum.Name)
        if not ParsedPage:
            return

        Enum.DocString = ParsedPage.DocString

        for Property in Enum.StubProperties:
            Members = ParsedPage.GetFirstMemberByName(Property.Name)
            if Members:
                Property.DocString = Members.DocString

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
                Property.Type = EnsureValidType(Members.Type)

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

    # If we have multiple functions and multiple members, we need to figure out which ones to match

    # Make copies of the lists so we can modify them without affecting the original lists
    FunctionsCopy = Functions.copy()
    MembersCopy = Members.copy()

    # Find all of the functions that has a perfect match with a member, by the parameter types
    PerfectMatches: list[tuple[StubFunction, MemberItem]] = []
    MatchedFunctions: list[StubFunction] = []
    MatchedDocMembers: list[MemberItem] = []
    for Function in FunctionsCopy:
        FunctionParameters = Function.GetParameters(bExcludeSelf = True)

        for Member in MembersCopy:
            if len(FunctionParameters) != len(Member.Parameters):
                continue

            for FunctionParameter, MemberParameter in zip(FunctionParameters, Member.Parameters):
                if FunctionParameter.Type != MemberParameter.Type:
                    break
            else:
                # Make sure neither the function or the member has already been matched with another function or member
                if Function in MatchedFunctions or Member in MatchedDocMembers:
                    continue
                PerfectMatches.append((Function, Member))

                MatchedFunctions.append(Function)
                MatchedDocMembers.append(Member)

    for Function, Member in PerfectMatches:
        PatchFunction(Function, Member)

        # Remove them from the lists so we don't try to match them again
        FunctionsCopy.remove(Function)
        MembersCopy.remove(Member)

    # TODO: Match based on most similar parameter types
    Scores: list[tuple[StubFunction, MemberItem, int]] = []
    for Function in FunctionsCopy:
        FunctionParameters = Function.GetParameters(bExcludeSelf = True)
        for Member in MembersCopy:
            Score = 0
            if len(FunctionParameters) == len(Member.Parameters):
                Score += 1

            for FunctionParameter, MemberParameter in zip(FunctionParameters, Member.Parameters):
                MemberParameterType = EnsureValidType(MemberParameter.Type)
                if FunctionParameter.Type == MemberParameterType:
                    Score += 1
                elif MemberParameterType.startswith("list") and FunctionParameter.Type == "list":
                    Score += 1
                elif IsTypeDefined(FunctionParameter.Type):
                    # Member description is not compatible with current function
                    print(f"Member {Member.Name} is not compatible because of parameter {FunctionParameter.Type} != {MemberParameterType}")
                    Score = -1
                    break

            if Score > 0:
                Scores.append((Function, Member, Score))

    # Sort the scores from highest to lowest
    Scores.sort(key = lambda Score: Score[2], reverse = True)
    while Scores:
        Function, Member, Score = Scores.pop(0)
        if Function in MatchedFunctions or Member in MatchedDocMembers:
            continue

        PatchFunction(Function, Member)

        MatchedDocMembers.append(Member)
        MatchedFunctions.append(Function)

        # Remove them from the lists so we don't try to match them again
        FunctionsCopy.remove(Function)
        MembersCopy.remove(Member)


def PatchFunction(Function: StubFunction, DocMember: MemberItem):
    Function.DocString = DocMember.DocString

    if ShouldPatchType(Function.ReturnType, DocMember.Type):
        Function.ReturnType = DocMember.Type

    FunctionParameters = Function.GetParameters(bExcludeSelf = True)
    DocumentationParameters = DocMember.Parameters

    # The documentation includes an additional empty parameter for functions directly in the module
    if not Function.bIsMethod and len(DocumentationParameters) - 1 == len(FunctionParameters):
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
        if DocParameter.Name and FunctionParameter.Name.startswith("arg"):
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
    if not ShouldPatchType(Parameter.Type, Type):
        return

    Parameter.Type = EnsureValidType(Type)


def PatchPropertyDefaultValue(Parameter: StubParameter, DefaultValue: str | None):
    if Parameter.DefaultValue is None or DefaultValue is None:
        return

    # Replace namespace C++ syntax with Python
    if "::" in DefaultValue:
        DefaultValue = DefaultValue.replace("::", ".")

    DefaultValue = TRANSLATION_VALUES.get(DefaultValue, DefaultValue)

    # Remove the "f" suffix from float literals, e.g. '1.0f' -> '1.0'
    if DefaultValue.endswith("f") and DefaultValue[:-1].replace(".", "").isnumeric():
        DefaultValue = DefaultValue[:-1]

    Parameter.DefaultValue = DefaultValue


def EnsureValidType(Type: str) -> str:
    Type = TRANSLATION_TYPE.get(Type, Type)
    
    if "<" in Type:
        Type = Type.replace("<", "[").replace(">", "]").replace(" ", "")
        Type = Type.replace("FBArrayTemplate", "list")
    
    return Type


def ShouldPatchType(CurrentType: str, NewType: str) -> bool:
    if not IsTypeDefined(CurrentType):
        return True

    if CurrentType == "list" and EnsureValidType(NewType).startswith("list"):
        return True

    return False

def IsTypeDefined(Type: str | None) -> bool:
    if not Type:  # TODO: Hmmm ?
        return True
    return Type != "object"
