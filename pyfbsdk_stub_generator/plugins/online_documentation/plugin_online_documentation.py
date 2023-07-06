from __future__ import annotations

import os

from types import ModuleType
from importlib import reload

from .documentation_scraper import table_of_contents

from .documentation_scraper.page_parser import MemberItem, GetParameterNiceName
from ..plugin import PluginBaseClass
from ...module_types import StubClass, StubFunction, StubParameter, StubProperty

reload(table_of_contents)

EVENT_SOURCE_TYPE = "callbackframework.FBEventSource"

TYPE_IGNORE_PREFIXES = (
    "unsigned",
    "K_DEPRECATED"
)

TRANSLATION_TYPE = {
    "double": "float",
    "long": "int",
    "kInt64": "int",
    "kULong": "int",
    "char": "str",

    "kReference": "int",
    "FBkReference": "int",

    "FBAudioFmt": "int",
    "FBBool": "bool",

    "FBArrayDouble": "list[float]",
    "FBArrayUInt": "list[int]",

    "FBVector4[float]": "FBVector4d",
    "FBTVector": "FBVector4d",
    "FBQuaternion": "FBVector4d",
    "FBRVector": "FBVector3d",
    "FBColorF": "FBColor",

    # These are a bit more spesific, and may need to be changed in the future
    "AreaLightShapes": "FBLight.EAreaLightShapes",
    "KeyBehavior": "FBModelPath3D.EKeyPropertyBehavior",
    "UnitType": "FBModelPath3D.ELengthUnitType",
    "Element": "object",

    # These are unknown, revert them back to properties
    "FBEventTreeWhy": "property",
}

TRANSLATION_VALUES = {
    "nullptr": "None",
}


class PluginOnlineDocumentation(PluginBaseClass):
    Threading = False
    Priority = 10  # We preferably want this to run directly after the native generator

    def __init__(self, Version: int, Module: ModuleType, EnumList: list[StubClass], ClassList: list[StubClass], FunctionGroupList: list[list[StubFunction]]):
        super().__init__(Version, Module, EnumList, ClassList, FunctionGroupList)

        # Initialize the documentation
        self.DocNamespace = table_of_contents.GetNameSpaceFromModule(self.ModuleName)
        if self.DocNamespace is None:
            return
        self.Documentation = table_of_contents.Documentation(self.DocNamespace, Version, self.bDevMode)

        # Parse the first documentation page to get the list of all pages
        for FunctionGroup in FunctionGroupList:
            Function = FunctionGroup[0]
            self.FunctionPage = self.Documentation.GetParsedPage(Function.Name)
            if self.FunctionPage:
                break

        # Make a map of all class names and their class object that can be used for patching types etc.
        self.AllClassesMap = {Class.Name: Class for Class in ClassList + EnumList}

    def ShouldPatch(self) -> bool:
        return self.DocNamespace is not None

    # ---------------------------------------------------------------------------------------------
    #                                 Patch Entry Methods
    # ---------------------------------------------------------------------------------------------

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
            Member = ParsedPage.GetFirstMemberByName(Property.Name)
            if Member:
                Property.DocString = Member.DocString
                Property.Type = self.EnsureValidPropertyType(Property, Member.Type)

        # Methods
        for FunctionGroup in Class.StubFunctions:
            FirstFunction = FunctionGroup[0]
            FunctionName = FirstFunction.Name

            # In the documentation, the constructor is called the same as the class
            if FunctionName == "__init__":
                FunctionName = Class.Name

            Members = ParsedPage.GetMembersByName(FunctionName)
            if Members:
                self._PatchFunctionGroupsWithDocumentation(FunctionGroup, Members, Class)

    def PatchFunctionGroup(self, FunctionGroup: list[StubFunction]):
        if not FunctionGroup:
            return  # TODO: This should never happen, look into it

        if self.FunctionPage:
            Members = self.FunctionPage.GetMembersByName(FunctionGroup[0].Name)
            if Members:
                self._PatchFunctionGroupsWithDocumentation(FunctionGroup, Members)

    # ---------------------------------------------------------------------------------------------
    #                                    Patch Functions
    # ---------------------------------------------------------------------------------------------

    def _PatchFunctionGroupsWithDocumentation(self, Functions: list[StubFunction], Members: list[MemberItem], ParentClass: StubClass | None = None):
        # If we only have one function and one member, we don't need to figure out which one is the correct one
        if len(Functions) == 1 and len(Members) == 1:
            self.PatchFunctionWithDocumentation(Functions[0], Members[0], ParentClass)
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
            self.PatchFunctionWithDocumentation(Function, Member, ParentClass)

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
                    MemberParameterType = self.EnsureValidType(MemberParameter.Type)
                    if not MemberParameterType or not FunctionParameter.Type:
                        continue
                    if FunctionParameter.Type == MemberParameterType:
                        Score += 1
                    elif MemberParameterType.startswith("list") and FunctionParameter.Type == "list":
                        Score += 1
                    elif IsTypeDefined(FunctionParameter.Type):
                        # Member description is not compatible with current function
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

            self.PatchFunctionWithDocumentation(Function, Member, ParentClass)

            MatchedDocMembers.append(Member)
            MatchedFunctions.append(Function)

            # Remove them from the lists so we don't try to match them again
            FunctionsCopy.remove(Function)
            MembersCopy.remove(Member)

    def PatchFunctionWithDocumentation(self, Function: StubFunction, DocMember: MemberItem, ParentClass: StubClass | None = None):
        Function.DocString = DocMember.DocString
        if Function.Name == "__init__":
            if Function.DocString.startswith("Constructor."):
                Function.DocString = Function.DocString.replace("Constructor.", "", 1)

        if self.ShouldPatchType(Function.ReturnType, DocMember.Type):
            NewType = self.EnsureValidType(DocMember.Type)
            if NewType:
                Function.ReturnType = NewType

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
                FunctionParameter.Name = GetParameterNiceName(DocParameter.Name)

            # Type
            self.PatchParameterType(FunctionParameter, DocParameter.Type, ParentClass)

            # Default value
            self.PatchPropertyDefaultValue(FunctionParameter, DocParameter.DefaultValue)

    # ---------------------------------------------------------------------------------------------
    #                                    Validate Types
    # ---------------------------------------------------------------------------------------------

    def PatchParameterType(self, Parameter: StubParameter, Type: str, ParentClass: StubClass | None = None) -> str:
        # If the enum is a subclass of the current class, patch the type to include the class name
        # This is not really needed, though MyPy might want it
        # if ParentClass and IsTypeDefined(Parameter.Type):
        #     if Parameter.Type.startswith("E") and Type not in self.AllClassesMap:
        #         # Check if enum is a subclass of the parent class
        #         for Enum in ParentClass.StubEnums:
        #             if Parameter.Type == Enum.Name:
        #                 Parameter.Type = f"{ParentClass.Name}.{Enum.Name}"
        #                 print(f"Patched parameter type: {Parameter.Type}")
        #                 return
        if not self.ShouldPatchType(Parameter.Type, Type):
            return

        Parameter.Type = self.EnsureValidType(Type)

    def EnsureValidPropertyType(self, Property: StubProperty, Type: str) -> str:

        # If it's a class, make sure it's a valid class
        bIsValidFBClass = Type in self.AllClassesMap
        if not bIsValidFBClass:
            if Type.startswith("FB"):
                # In the documentation the "Property" part is missing from the class name
                PropertyType = f"FBProperty{Type[2:]}"
                if PropertyType in self.AllClassesMap:
                    Type = PropertyType

        # Convert all Events to EventSource
        # The documentation says otherwise, but is wrong.
        if ((Type.startswith("FBEvent") or Property.Name.endswith("Event")) and Property.Name.startswith("On") and Property.DocString.startswith("Event")) or \
                (not bIsValidFBClass and Type.startswith("FBEvent")):
            Type = EVENT_SOURCE_TYPE

        return self.EnsureValidType(Type)

    def PatchPropertyDefaultValue(self, Parameter: StubParameter, DefaultValue: str | None):
        if Parameter.DefaultValue is None or DefaultValue is None:
            return

        # Replace namespace C++ syntax with Python
        if "::" in DefaultValue:
            DefaultValue = DefaultValue.replace("::", ".")

        DefaultValue = TRANSLATION_VALUES.get(DefaultValue, DefaultValue)

        # Remove the "f" suffix from float literals, e.g. '1.0f' -> '1.0'
        if DefaultValue.endswith("f") and DefaultValue[:-1].replace(".", "").isnumeric():
            DefaultValue = DefaultValue[:-1]

        if DefaultValue.startswith("FBArrayTemplate"):
            DefaultValue = "[]"
        elif DefaultValue == "FBString()":
            DefaultValue = '""'

        if DefaultValue.startswith(("FB", "k")) and DefaultValue not in self.AllClassesMap:
            EnumClass = self.AllClassesMap.get(Parameter.Type)
            if EnumClass:
                if any(x.Name for x in EnumClass.StubProperties if x.Name == DefaultValue):
                    DefaultValue = f"{EnumClass.Name}.{DefaultValue}"

        Parameter.DefaultValue = DefaultValue

    def ShouldPatchType(self, CurrentType: str, NewType: str) -> bool:
        if not IsTypeDefined(CurrentType):
            return True

        ValidatedType = self.EnsureValidType(NewType)
        if not ValidatedType:
            return False

        if CurrentType == "list" and ValidatedType.startswith("list"):
            return True
        if CurrentType == "tuple" and ValidatedType.startswith("tuple"):
            return True

        # TODO: Must check if type is valid as well
        if CurrentType.startswith(("E", "FB")) and CurrentType not in self.AllClassesMap:
            return True

        return False

    def EnsureValidType(self, Type: str) -> str | None:
        if "<" in Type:
            Type = Type.replace("<", "[").replace(">", "]").replace(" ", "")
            Type = Type.replace("FBArrayTemplate", "list")

            # Get content between brackets
            ListTypesStr = Type[Type.find("[") + 1:Type.find("]")]
            if ListTypesStr:
                ValidatedTypes = []
                ListTypes = ListTypesStr.split(",")
                for ListType in ListTypes:
                    ListType = self.EnsureValidType(ListType)
                    if ListType:
                        ValidatedTypes.append(ListType)
                
                if len(ListTypes) != len(ValidatedTypes):
                    return None
                
                Type = Type.replace(ListTypesStr, ",".join(ValidatedTypes))
                if Type.endswith("[]"):
                    Type = Type[:-2]

        if " " in Type:
            for Prefix in TYPE_IGNORE_PREFIXES:
                if Type.startswith(Prefix):
                    Type = Type.rpartition(" ")[2]
        
        Type = TRANSLATION_TYPE.get(Type, Type)

        # Replace namespace C++ syntax with Python
        if "::" in Type:
            Type = Type.replace("::", ".")

        if Type.startswith("FB"):
            ClassName = Type
            if "." in Type:
                ClassName = Type.partition(".")[0]
            if ClassName not in self.AllClassesMap:
                # print(f"Type not found: {Type}")
                return None

        return Type


def IsTypeDefined(Type: str | None) -> bool:
    if not Type:
        return False
    return Type != "object" and Type != "Any"
