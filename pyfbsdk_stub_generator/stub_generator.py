from __future__ import annotations

import inspect
import typing
import time
import sys
import re
import os

from importlib import reload
from types import FunctionType

import pyfbsdk

bTest = "builtin" in __name__
if bTest:
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    __name__ = "pyfbsdk_stub_generator.stub_generator"  # pylint: disable=redefined-builtin

from . import motionbuilder_documentation_parser as docParser
from . import manual_documentation as manualDoc


reload(docParser)
reload(manualDoc)

IS_PYTHON_39 = sys.version_info.major == 3 and sys.version_info.minor == 9
ADDITIONS_FILEPATH = os.path.join(os.path.dirname(__file__), "additions_pyfbsdk.py")
TAB_CHARACTER = "    "


# TODO: Broken stuff:
# FBModel.GetHierarchyWorldMatrices() - First param in the docs doesn't exists in the python version
# FBInterpolateRotation() - Both of them use the same documentation :/
# Support URLs in the doc strings
# FBStoryClip -> GetAffectedAnimationNodes & FBModel::GetHierarchyWorldMatrices()
# GetCommandLineArgs - Turn blockquotes into: ```

# -------------------------------------------------------------
#                         Translations
# -------------------------------------------------------------

# In the online C++ MotionBuilder documentation these classes/functions have following aliases:
TranslationDocumentationClassNames = {
    "FBVector3d": "FBVector3",
    "FBVector4d": "FBVector4"
}


TranslationDocumentationMethodNames = {
    "__sub__": "operator-",
    "__getitem__": "operator[]",
}


PropertyTypeTranslation = {
    "FBPropertyString": "str",
    "FBPropertyInt": "int",
    "FBPropertyFloat": "float",
    "FBPropertyDouble": "float",
    "FBPropertyBool": "bool",
}


VariableTypeTranslations = {
    "FBColorF": "FBColor",
    "tType": "float"  # This is probably incorrect, but gives the desired results for 2022 at least :)
}


# List of known enum values that doesn't start with a 'k' (should only be FBEffectorSetID)
KnownEnumValuesNotStartingWithK = [
    "FBEffectorSetDefault"
]


# -------------------------------------------------------------
#                       Structs & Enums
# -------------------------------------------------------------

class FObjectType:
    Function = 'function'
    Class = 'class'
    Property = 'property'
    Enum = 'type'


# -------------------------------------------------------------
#                       Helper Functios
# -------------------------------------------------------------


def GetMotionBuilderVersion():
    """ Get the current version of MotionBuilder """
    return int(2000 + pyfbsdk.FBSystem().Version / 1000)


def GetObjectName(Object):
    return Object.__name__


def GetObjectType(Object) -> FObjectType:
    """ Get object type as a string """
    return GetObjectName(type(Object))


def IsPrivate(Object):
    """ Check if the name of an object begins with a underscore """
    return GetObjectName(Object).startswith("_")


def Indent(Text: str):
    return TAB_CHARACTER + f"\n{TAB_CHARACTER}".join(Text.split("\n"))


def IsMethodStatic(Class, MethodName: str):
    """ 
    Check if a method is static
    Args:
        - Class: reference to the class
        - Method: Name of the method
    """
    return isinstance(inspect.getattr_static(Class, MethodName), staticmethod)


# -------------------------------------------------------------
#                       Functions
# -------------------------------------------------------------

def GetCustomAdditions():
    Content = ""
    if os.path.isfile(ADDITIONS_FILEPATH):
        with open(ADDITIONS_FILEPATH, 'r', encoding="utf-8") as File:
            Content = File.read().strip() + "\n"
    Content = Content.replace("{MOTIONBUILDER_VERSION}", str(GetMotionBuilderVersion()))
    return Content


def GetPyfbsdkContent():
    """ 
    Get all members in the pyfbsdk module
    returns: a tuple with (Functions, Classes, Enums)
    """
    Functions = [x[1] for x in inspect.getmembers(pyfbsdk) if GetObjectType(x[1]) == FObjectType.Function and not IsPrivate(x[1])]
    Classes = [x[1] for x in inspect.getmembers(pyfbsdk) if GetObjectType(x[1]) == FObjectType.Class]
    Enums = [x[1] for x in inspect.getmembers(pyfbsdk) if GetObjectType(x[1]) == FObjectType.Enum]

    return (Functions, Classes, Enums)


def GetClassParents(Class):
    return Class.__bases__


def GetUniqueClassMembers(Class, Ignore = (), AllowedOverrides = ()):
    """ 
    Args:
        - Class {object}: reference to the class
        - Ignore {List[str]}: 
        - AlwaysAllow {List[str]}: Always allowed members named x, even if they exists in the parent class

    Returns: tuple("Name", Reference)
    """
    Members = inspect.getmembers(Class)
    ParentClass = GetClassParents(Class)[0]
    UniqueMemebers = [x for x in Members if (not hasattr(ParentClass, x[0]) and x[0] not in Ignore) or x[0] in AllowedOverrides]  # and not x[0].startswith("__")

    return UniqueMemebers


def GetClassParentNames(Class):
    ParentClassNames = []
    for Parent in GetClassParents(Class):
        ParentClassName = Parent.__name__
        if ParentClassName == "instance":
            ParentClassName = ""

        elif ParentClassName == "enum":
            ParentClassName = "_Enum"

        ParentClassNames.append(ParentClassName)

    return ParentClassNames


def GetFunctionInfoFromDocString(Function):
    """
    Get Parameters & Return type from the docstring, can return multiple results if overload functions exists.

    Returns: a list of tuple([Parameters], ReturnType)
    """
    def _GenerateParams(ParamsString, DefaultValue = None):
        """ 
        Parse a param string that looks something like this:
        "(FBVector4d)arg1, (FBVector4d)arg2, (FBVector4d)arg3"
        and generate StubParameter instances from it
        """
        Params = []
        for Param in ParamsString.split(","):
            # Param will now look something like this: '(str)arg1'
            ParamType, _, ParamName = Param.strip().partition(")")
            ParameterInstance = StubParameter(ParamName, ParamType[1:], DefaultValue = DefaultValue)
            Params.append(ParameterInstance)
        return Params

    FunctionParamters = []
    # Read the docstring and split it up if there are multiple function overrides
    FunctionsDocs = [x for x in Function.__doc__.split("\n") if x]
    for Doc in FunctionsDocs:
        # 'Doc' will now look something like this:
        # ShowToolByName( (str)arg1 [, (object)arg2]) -> object
        Doc = Doc.partition("(")[2]  # Remove function name
        Params, _, ReturnType = Doc.rpartition("->")

        # Split params into required & optional
        Params = Params.rpartition(")")[0]
        RequiredParams, _, OptionalParams = Params.partition("[")
        OptionalParams = OptionalParams.replace("[", "").replace("]", "").lstrip(',')

        Params = []
        if RequiredParams.strip():
            Params += _GenerateParams(RequiredParams)
        if OptionalParams.strip():
            Params += _GenerateParams(OptionalParams, DefaultValue = "None")

        FunctionParamters.append(
            (Params, ReturnType.strip())
        )

    return FunctionParamters


def SortClasses(Classes: list):
    """ 
    Sort classes based on their parent class
    If a class has another class as their parent class, it'll be placed later in the list
    """
    ClassNames = [x.Name for x in Classes]

    i = 0
    while i < len(Classes):
        # Check if class has any required classes that needs to be defined before it (aka. parent classes)
        Requirements = Classes[i].GetRequirements()
        if Requirements:
            # Get the required class that has the highest index in the list
            RequiredIndices = [ClassNames.index(x) for x in Requirements if x in ClassNames]
            RequiredMaxIndex = max(RequiredIndices) if RequiredIndices else -1

            # If current index is lower than the highest required index, move current index to be just below the required one.
            if RequiredMaxIndex > i:
                Classes.insert(RequiredMaxIndex + 1, Classes.pop(i))
                ClassNames.insert(RequiredMaxIndex + 1, ClassNames.pop(i))
                i -= 1  # Because we moved current index away, re-itterate over the same index once more.

        i += 1

    return Classes


def GetDataTypeFromPropertyClassName(ClassName: str, AllClassNames: list[str]):
    """
    Get the `Data` property type for a class that inherits from `FBProperty`
    This is done by removing e.g. `FBProperty` from the class name. Example: `FBPropertyVector3d` -> `Vector3d`
    """
    # Value to return use if a valid class could not be found for the given ClassName
    DefaultValue = "property"

    ConvertTypeDict = {
        "Bool": "bool",
        "String": "str",
        "Int": "int",
        "Int64": "int",
        "UInt64": "int",
        "Float": "float",
        "Double": "float"
    }

    DataType = ClassName
    for x in ("FBProperty", "Animatable", "List"):
        DataType = DataType.replace(x, "")

    if DataType in ConvertTypeDict:
        return ConvertTypeDict[DataType]

    # For the base classes e.g. FBProperty
    if not DataType:
        return DefaultValue

    # TODO: Validate that the class actually exists
    DataType = f"FB{DataType}"
    if DataType not in AllClassNames:
        return DefaultValue

    return DataType

# -------------------------------------------------------------
#                       Classes
# -------------------------------------------------------------


class StubBaseClass():
    def __init__(self, Name = "") -> None:
        self.Name: str = Name
        self.DocString = ""

    def GetAsString(self) -> str:
        """
        Get instance as python code (in string format)
        """
        raise NotImplementedError("GetAsString() has not yet been implemented")

    def GetDocString(self):
        if self.DocString:
            return f'""\"{self.DocString.strip()}"""'
        return ""

    def GetRequirements(self) -> list:
        """
        Get a list of variable/class names that needs to be declared before the current object
        """
        raise NotImplementedError("GetRequirements() has not yet been implemented")


class StubFunction(StubBaseClass):
    def __init__(self, Name = "", Parameters = None, ReturnType = None):
        super().__init__(Name = Name)
        self._Params: list[StubParameter] = Parameters if Parameters else []
        self.ReturnType = ReturnType
        self.bIsMethod = False
        self.bIsStatic = False
        self.bIsOverload = False

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.Name}>"

    def AddParameter(self, Parameter):
        self._Params.append(Parameter)

    def GetParameters(self) -> list[StubParameter]:
        return self._Params

    def SetParameter(self, Index, Paramter):
        if Index > len(self._Params) - 1:
            raise IndexError("given parameter index is larger than the size of the paramter array")
        self._Params[Index] = Paramter

    def GetRequirements(self) -> list:
        ReturnValue = []
        for Parameter in self._Params:
            ReturnValue += Parameter.GetRequirements()
        return ReturnValue

    def GetParamsAsString(self):
        ParametersAsStrings = []
        for i, Param in enumerate(self._Params):
            if self.bIsMethod and i == 0:
                Param.Name = "self"
                Param.Type = None
            ParametersAsStrings.append(Param.GetAsString())

        return ",".join(ParametersAsStrings)

    def GetAsString(self):
        FunctionAsString = ""
        if self.bIsOverload:
            FunctionAsString += "@overload\n"
        elif self.bIsStatic:
            FunctionAsString += "@staticmethod\n"

        FunctionAsString += f'def {self.Name}({self.GetParamsAsString()})'

        if self.ReturnType and self.ReturnType != "None":
            FunctionAsString += f'->{self.ReturnType}'

        FunctionAsString += ":"

        DocString = self.GetDocString()
        if DocString:
            FunctionAsString += f"\n{Indent(DocString)}\n{Indent('...')}"
        else:
            FunctionAsString += "..."

        return FunctionAsString


class StubClass(StubBaseClass):
    def __init__(self, Name = ""):
        super().__init__(Name = Name)
        self.Parents = []
        self.StubProperties: list[StubProperty] = []
        self.StubFunctions: list[StubFunction] = []

    def GetFunctionsByName(self, Name: str):
        return [x for x in self.StubFunctions if x.Name == Name]

    def GetPropertyByName(self, Name: str):
        for x in self.StubProperties:
            if x.Name == Name:
                return x

    def AddFunction(self, Function: StubFunction):
        Function.bIsMethod = True  # Make function a method
        self.StubFunctions.append(Function)

    def AddProperty(self, Property: StubProperty):
        self.StubProperties.append(Property)

    def AddParent(self, Parent: str):
        self.Parents.append(Parent)

    def GetStubProperties(self) -> list[StubProperty]:
        return self.StubProperties

    def GetRequirements(self) -> list:
        # The class parent's needs to be declared before the class
        FunctionRequirements = []
        for Function in self.StubFunctions:
            FunctionRequirements += Function.GetRequirements()
        return self.Parents + FunctionRequirements

    def GetAsString(self):
        ParentClassesAsString = ','.join(self.Parents)

        ClassAsString = f"class {self.Name}({ParentClassesAsString}):\n"

        if self.GetDocString():
            ClassAsString += f"{Indent(self.GetDocString())}\n"

        ClassMembers = self.StubProperties + self.StubFunctions
        for StubObject in ClassMembers:
            ClassAsString += f"{Indent(StubObject.GetAsString())}\n"

        # If class doesn't have any members, add a '...'

        if not ClassMembers:
            ClassAsString += Indent("...")

        return ClassAsString.strip()


class StubProperty(StubBaseClass):
    def __init__(self, Name = ""):
        super().__init__(Name = Name)
        self._Type = None

    @property
    def Type(self):
        if self._Type:
            return self._Type
        return "property"

    @Type.setter
    def Type(self, Value):
        self._Type = Value

    def GetAsString(self):
        PropertyAsString = f"{self.Name}:{self.Type}"

        # Add docstring
        if self.GetDocString():
            PropertyAsString += "\n"
            PropertyAsString += self.GetDocString()

        return PropertyAsString


class StubParameter(StubBaseClass):
    def __init__(self, Name = "", Type = "", DefaultValue = None):
        super().__init__(Name = Name)
        self.Type = Type
        self.DefaultValue = DefaultValue

    def GetRequirements(self):
        if self.DefaultValue and self.DefaultValue.startswith("FB"):
            RequirementClass: str = self.DefaultValue
            if "." in RequirementClass:
                RequirementClass = RequirementClass.partition(".")[0]
            return [RequirementClass]
        return []

    def GetNiceName(self):
        ReturnValue = self.Name
        if ReturnValue.startswith("p") and not ReturnValue[1].isnumeric():
            ReturnValue = ReturnValue.lstrip("p")
        if self.Type == "bool" and not ReturnValue.startswith("b"):
            ReturnValue = f"b{ReturnValue}"
        return ReturnValue

    def GetAsString(self):
        ParamString = self.GetNiceName()  # PatchParameterName(self.Name)
        if self.Type and self.Type != "object":
            ParamString += f":{self.Type}"

        if self.DefaultValue is not None:
            ParamString += f"={self.DefaultValue}"

        return ParamString


# ---------------------------------------------------------------------------------
#                                  GENERATOR
# ---------------------------------------------------------------------------------


class PyfbsdkStubGenerator():
    def __init__(self, bCacheDocumentation = False):
        self.Functions: list[StubFunction] = []
        self.Classes: list[StubClass] = []
        self.Enums: list[StubClass] = []
        self.Version = GetMotionBuilderVersion()
        self.DocumentationParser = docParser.MotionBuilderDocumentation(self.Version, bCache = bCacheDocumentation)

        self._AllClassNames = []

        self._DebugPropertiesConvertedToDefault = []

    # ---------------------------------------------------
    #                      Internal
    # --------------------------------------------------
    def GetAllClassNames(self):
        """ Get the names of all classes avaliable in the pyfbsdk module """
        if not self._AllClassNames:
            Functions, Classes, Enums = GetPyfbsdkContent()
            self._AllClassNames = [x.__name__ for x in Classes + Enums]
        return self._AllClassNames

    def _GenerateEnumInstance(self, Class):
        """
        Generate a StubClass instance from a class (enum) reference

        Args:
            - Class {class}: reference to the class
        """
        # Create the stub instance
        ClassName = GetObjectName(Class)
        EnumClassInstance = StubClass(ClassName)

        # Get all members and generate stub properties of them
        ClassMemebers = GetUniqueClassMembers(Class, Ignore = ["__init__", "__slots__", "names", "values"])
        for PropertyName, PropertyReference in ClassMemebers:
            PropertyInstance = StubProperty(PropertyName)
            PropertyInstance.Type = ClassName
            EnumClassInstance.AddProperty(PropertyInstance)

        EnumClassInstance.AddParent("_Enum")

        return EnumClassInstance

    def _GenerateClassInstance(self, Class) -> StubClass:
        """
        Generate a StubClass instance from a class reference

        Args:
            - Class {class}: reference to the class
        """
        # Create the stub instance
        ClassName = GetObjectName(Class)
        ClassInstance = StubClass(ClassName)

        # Get all members and generate stub properties of them
        ClassMemebers = GetUniqueClassMembers(Class, Ignore = ["__instance_size__"], AllowedOverrides = ["__init__", "__getitem__", "Data"])
        for MemberName, MemberReference in ClassMemebers:
            Type = GetObjectType(MemberReference)
            if Type == FObjectType.Function:
                for StubMethod in self._GenerateFunctionInstances(MemberReference):
                    StubMethod.bIsStatic = IsMethodStatic(Class, MemberName)
                    ClassInstance.AddFunction(StubMethod)
            elif MemberName not in ["__init__"]:
                Property = StubProperty(MemberName)
                Property.Type = GetObjectType(MemberReference)
                if MemberName == "Data" and "FBProperty" in ClassName and Property.Type == FObjectType.Property:
                    Property.Type = GetDataTypeFromPropertyClassName(ClassName, self.GetAllClassNames())
                ClassInstance.AddProperty(Property)

        # Set the parent classes
        for ParentClassName in GetClassParentNames(Class):
            ClassInstance.AddParent(ParentClassName)

        return ClassInstance

    def _GenerateFunctionInstances(self, Function) -> list[StubFunction]:
        """
        Generate StubFunction instances from a function reference.

        Args:
            - Function {function}: reference to the function

        Returns: A list of function instances, can be multiple if it has overload versions
        """
        FunctionName = GetObjectName(Function)

        StubFunctions = []

        # Get param & returntype info from the docstring
        FunctionInfo = GetFunctionInfoFromDocString(Function)
        for Parameters, ReturnType in FunctionInfo:
            StubFunctionInstance = StubFunction(FunctionName, Parameters, ReturnType)

            # If multiple versions of this function exists, set the functions to be overloads
            StubFunctionInstance.bIsOverload = len(FunctionInfo) > 1

            StubFunctions.append(StubFunctionInstance)

        return StubFunctions

    # ---------------------------------------------------
    #           Online Documentation Functions
    # --------------------------------------------------

    def _EnsurePropertyTypeIsValid(self, PropertyType: str):
        """
        Patch a class property type, e.g. turning 'FBPropertyCamera' -> 'FBCamera'
        """
        # Default property types to always accept as valid
        if PropertyType in ["str", "float", "bool", "int"]:
            return PropertyType

        # Check if PropertyType exists as a known type to be translated into something else
        if PropertyType in PropertyTypeTranslation:
            return PropertyTypeTranslation[PropertyType]

        # Remove FBProperty, only do this for properties that are not list's or animatable
        if PropertyType.startswith("FBProperty") and not any(x for x in PropertyType if x in ["List", "Animatable"]):
            NewPropertyType = PropertyType.replace("Property", "", 1)
            if NewPropertyType in self.GetAllClassNames():
                return NewPropertyType

        if PropertyType in self.GetAllClassNames():
            return PropertyType

        self._DebugPropertiesConvertedToDefault.append(PropertyType)
        return "property"

    def _PatchFunctionDocstring(self, DocString: str, Function: StubFunction = None):
        Translations = {
            " Null ": " `None` ",
            " null ": " `None` ",
            " NULL ": " `None` "
        }

        # Titles where all of the contents under it should be in list form
        TitlesWithLists = ["parameters", "return values"]

        # Prevent some functions from having a docstring.
        # These functions doesn't need a docstring and will only increase filesize
        if Function.Name in ["__getitem__"]:
            return ""

        NewDocString = ""
        UnderTitle = None
        NumberOfParameters = 0
        bParsingCode = False
        for i, Line in enumerate(self._PatchDocStringGeneric(DocString).split("\n")):

            if Line.startswith(">>>"):
                bParsingCode = True
            elif bParsingCode and not Line:
                bParsingCode = False

            elif not bParsingCode:
                if i == 0 and (Line.strip(". \\") == Function.Name or Line.strip("\\ ").lower().endswith("constructor.")):
                    continue

                bIsLineATitle = Line.startswith("#")
                if bIsLineATitle:
                    bAddExtraLine = bool(UnderTitle)
                    UnderTitle = Line.strip("# :").lower()
                    if bAddExtraLine:
                        Line = f"\n{Line}"

                if UnderTitle and not bIsLineATitle:
                    if UnderTitle in TitlesWithLists:
                        ParameterName, _, Description = Line.partition(" ")
                        NumberOfParameters += 1
                        Line = f"- {ParameterName}: {Description}"

                # Null -> None translation
                for Key, Item in Translations.items():
                    if Key in Line:
                        if Key.lower().strip() == "null" and "null pointer" in Line.lower():
                            continue
                        Line = Line.replace(Key, Item)

            NewDocString += f"{Line}\n"

        # Replace parameter names with their Nice Names. 'pMyParam' -> 'MyParam'
        for Parameter in Function.GetParameters():
            NewDocString = NewDocString.replace(Parameter.Name, Parameter.GetNiceName())

        # Remove parameters that doesn't exists in the Python version (but is included in the SDK docs)
        NumberOfFunctionParams = len(Function.GetParameters()) - 1 if Function.bIsMethod else len(Function.GetParameters())
        if NumberOfParameters > NumberOfFunctionParams:
            ParameterNiceNames = [x.GetNiceName() for x in Function.GetParameters()]
            NewDocStringAfterParamFix = ""
            bInParamsList = False
            for Line in NewDocString.split("\n"):
                if Line.startswith("###"):
                    bInParamsList = Line.partition(" ")[2] in ["Parameters:", "ReturnValues:"]
                    if bInParamsList and NumberOfFunctionParams == 0:
                        continue

                elif bInParamsList:
                    if Line.strip() and Line.lstrip("- ").partition(":")[0] not in ParameterNiceNames:
                        continue

                NewDocStringAfterParamFix += f"{Line}\n"
            NewDocString = NewDocStringAfterParamFix

        NewDocString = NewDocString.replace("  ", " ")

        return NewDocString.strip()

    def _PatchDocStringGeneric(self, Docstring: str):
        # TODO: This is now defined in 2 locations
        TitlesWithLists = ["parameters", "return values"]

        NewDocString = ""
        CodeLines = 0
        UnderTitle = None
        bParsingCode = False

        PreviousLine = ""

        for i, Line in enumerate(Docstring.split("\n")):
            if not Line.strip():
                continue

            NumberOfNewLines = 1
            PreviousLineSuffix = ""

            if not bParsingCode:
                Line = Line.strip()

            # Remove all 'Definition at line x' lines.
            if Line.startswith("Definition at line"):
                continue

            # Check if we're entering a codeblock
            if Line == "@CODE":
                bParsingCode = True
                CodeLines = 0
                continue

            # Check if we're exiting a code block
            elif bParsingCode and Line == "@ENDCODE":
                bParsingCode = False
                Line = ""

            if bParsingCode:
                Line = Line.replace("\\n", "\\\\n")
                Line = Line.replace("//", "# //")
                if CodeLines == 0:
                    Line = f"\n>>> {Line}"
                else:
                    # Switch to 4 spaces as tabs, instead of 2 spaces.
                    NumberOfTabs = int((len(Line) - len(Line.lstrip())) / 2)
                    Line = (TAB_CHARACTER * NumberOfTabs) + Line.lstrip()
                CodeLines += 1

            else:
                # Check if line is a title
                bIsLineATitle = Line.startswith("#")
                if bIsLineATitle:
                    Line = Line.partition(" ")[2]
                    UnderTitle = Line.lower()
                    Line = f"### {Line}:"

                if Line in ["C++ sample code:", "Python sample code:"]:
                    Line = f"### {Line}"
                    bIsLineATitle = True

                # Add a 'LineBreak'
                if UnderTitle not in TitlesWithLists and not PreviousLine.startswith("#") and i > 0 and not bIsLineATitle and Line.strip():
                    PreviousLineSuffix = r" \\"

                Line = Line.replace("  ", " ")

            PreviousLine = Line
            NewDocString += PreviousLineSuffix + ("\n" * NumberOfNewLines) + Line

        # Remove double spaces
        NewDocString = NewDocString.replace("\"", "'")

        return NewDocString.strip(" \n\\")

    def _PatchParameter(self, StubParameterInstance: StubParameter):
        # Patch type
        if StubParameterInstance.Type in VariableTypeTranslations:
            StubParameterInstance.Type = VariableTypeTranslations[StubParameterInstance.Type]
        elif StubParameterInstance.Type.startswith("FB") and StubParameterInstance.Type not in self.GetAllClassNames():
            StubParameterInstance.Type = None
        elif StubParameterInstance.Type.startswith("list["):
            ClassType = StubParameterInstance.Type.replace("list[", "", 1)[:-1]
            ClassType = VariableTypeTranslations.get(ClassType, ClassType)
            StubParameterInstance.Type = f"list[{ClassType}]"

        # Patch default value
        if StubParameterInstance.DefaultValue:
            if StubParameterInstance.DefaultValue.startswith("k") or StubParameterInstance.DefaultValue in KnownEnumValuesNotStartingWithK:
                StubParameterInstance.DefaultValue = f"{StubParameterInstance.Type}.{StubParameterInstance.DefaultValue}"

            elif StubParameterInstance.DefaultValue.startswith("FB") and StubParameterInstance.DefaultValue not in self.GetAllClassNames():
                if "." not in StubParameterInstance.DefaultValue:
                    # TODO: We should split on '.' & ensure the first classname actually exists
                    StubParameterInstance.DefaultValue = "None"

    def _EnsureReturnValueIsValid(self, ReturnValue):
        if ReturnValue.startswith("FB") and ReturnValue not in self.GetAllClassNames():
            return "object"
        return ReturnValue

    def _PatchFunctionsFromDocumentation(self, Functions: list[StubFunction], DocumentationMembers = None):
        UsedDocumentations = []
        for StubFunctionInstance in Functions:
            Documentations = []
            if DocumentationMembers:
                Documentations = DocumentationMembers
            else:
                Documentations = self.DocumentationParser.GetSDKFunctionByName(StubFunctionInstance.Name)
                if not Documentations:
                    # Try adding FB
                    Documentations = self.DocumentationParser.GetSDKFunctionByName(f"FB{StubFunctionInstance.Name}")
                    if not Documentations:
                        continue

            # If it's a method
            StubParameterInstances = StubFunctionInstance.GetParameters()[1:] if StubFunctionInstance.bIsMethod else StubFunctionInstance.GetParameters()

            Documentation = None
            if StubFunctionInstance.bIsOverload:
                HighestScore = -1
                BestMatch = None
                for Doc in Documentations:
                    if Doc in UsedDocumentations:
                        continue

                    # Check if number of parameters match
                    if len(Doc.Params) != len(StubParameterInstances):
                        continue

                    # Find the one with highest matching parameter score
                    Score = 0
                    for Parameter, DocumentationParam in zip(StubParameterInstances, Doc.Params):
                        ParamType = DocumentationParam.GetType(bConvertToPython = True)
                        if Parameter.Type == ParamType:
                            Score += 1

                    if Score > HighestScore:
                        BestMatch = Doc

                if BestMatch:
                    Documentation = BestMatch
                    UsedDocumentations.append(Documentation)

            else:
                Documentation = Documentations[0]

            if not Documentation:
                continue

            # Patch the return type
            if StubFunctionInstance.ReturnType is None or StubFunctionInstance.ReturnType in ["object", "tuple"]:
                NewReturnType = Documentation.GetType(bConvertToPython = True)
                if NewReturnType and NewReturnType != "None":
                    StubFunctionInstance.ReturnType = self._EnsureReturnValueIsValid(NewReturnType)

            # Patch the parameters
            DocumentationParam: docParser.DocMemberParameter
            for Parameter, DocumentationParam in zip(StubParameterInstances, Documentation.Params):
                Parameter.Name = DocumentationParam.Name
                if Parameter.DefaultValue is not None:
                    NewDefaultValue = DocumentationParam.GetDefaultValue(bConvertToPython = True)
                    if NewDefaultValue:
                        Parameter.DefaultValue = NewDefaultValue

                if not Parameter.Type or Parameter.Type == "object":
                    Parameter.Type = DocumentationParam.GetType(bConvertToPython = True)
                self._PatchParameter(Parameter)

            StubFunctionInstance.DocString = self._PatchFunctionDocstring(Documentation.DocString, StubFunctionInstance)

    def _PatchTableDocString(self, Class: StubClass, DocString: str):
        bParsingEnum = False
        NewDocString = ""
        for Line in DocString.split("\n"):
            Line = Line.strip()

            if Line == "@TABLE":
                bParsingEnum = True
                continue
            elif Line == "@ENDTABLE":
                bParsingEnum = False
                continue

            if bParsingEnum:
                if Line.startswith("#"):
                    continue

                PropertyName, _, PropertyDesc = Line.partition(":")
                MatchingProperties = [x for x in Class.GetStubProperties() if x.Name == PropertyName]
                if MatchingProperties:
                    MatchingProperty = MatchingProperties[0]
                    if "Definition at line" in PropertyDesc:
                        PropertyDesc = PropertyDesc.partition("Definition at line")[0]
                    MatchingProperty.DocString = self._PatchDocStringGeneric(PropertyDesc)
                continue

            NewDocString += f"{Line}\n"

        return self._PatchDocStringGeneric(NewDocString)

    def _PatchEnumFromDocumentation(self, Enum: StubClass):
        Documentation = self.DocumentationParser.GetSDKClassPagesByName(Enum.Name)
        if not Documentation:
            return
        DocumentationMembers = Documentation.GetMembersByName(Enum.Name)
        if not DocumentationMembers:
            return

        # Doc String
        DocumentationMember = DocumentationMembers[0]
        DocString = DocumentationMember.DocString

        Enum.DocString = self._PatchTableDocString(Enum, DocString)

    def _PatchClassFromDocumentation(self, Classes: list[StubClass]):
        for StubClassInstance in Classes:
            DocumentationClassName = TranslationDocumentationClassNames.get(StubClassInstance.Name, StubClassInstance.Name)
            Documentation = self.DocumentationParser.GetSDKClassPagesByName(DocumentationClassName)
            if not Documentation:
                continue

            # Patch functions
            # First collect all functions with the same name, so we itterate over them at the same time
            StubFunctionsInstancesDict = {}
            for StubFunctionInstance in StubClassInstance.StubFunctions:
                Value = StubFunctionsInstancesDict.get(StubFunctionInstance.Name, [])
                Value.append(StubFunctionInstance)
                StubFunctionsInstancesDict[StubFunctionInstance.Name] = Value

            for StubFunctionName, StubFunctionInstances in StubFunctionsInstancesDict.items():
                DocumentationFunctionName = TranslationDocumentationMethodNames.get(StubFunctionName, StubFunctionName)
                if DocumentationFunctionName == "__init__":
                    DocumentationFunctionName = DocumentationClassName
                FunctionDocumentations = Documentation.GetMembersByName(DocumentationFunctionName)
                self._PatchFunctionsFromDocumentation(StubFunctionInstances, FunctionDocumentations)

            # Patch properties
            for StubPropertyInstance in StubClassInstance.GetStubProperties():
                DocumentationMembers = Documentation.GetMembersByName(StubPropertyInstance.Name)
                if not DocumentationMembers:
                    # Check if the property is a GetX function in C++
                    DocumentationMembers = Documentation.GetMembersByName(f"Get{StubPropertyInstance.Name}")
                    if not DocumentationMembers:
                        continue

                # Properties doesn't have overloads, so we can get the first result
                PropertyDocumentation = DocumentationMembers[0]

                if StubPropertyInstance.Type == "property":
                    NewType = PropertyDocumentation.GetType(bConvertToPython = True)
                    NewType = self._EnsurePropertyTypeIsValid(NewType)
                    StubPropertyInstance.Type = NewType

                StubPropertyInstance.DocString = self._PatchDocStringGeneric(PropertyDocumentation.DocString)
                if "@TABLE" in StubPropertyInstance.DocString:
                    StubPropertyInstance.DocString = self._PatchTableDocString(StubClassInstance, StubPropertyInstance.DocString)

            # TODO: Add Class Docstring

    def GetClassByName(self, Name: str):
        for x in self.Classes:
            if x.Name == Name:
                return x
        for x in self.Enums:
            if x.Name == Name:
                return x

    def GetFunctionsByName(self, Name: str):
        return [x for x in self.Functions if x.Name == Name]

    def _PatchFromManualDocumentation(self):
        """
        Patch the StubClasses & StubFunctions based on the 'manual_documentation.py' file.
        """
        def _ParseManualDocumentation(Doc: str):
            # Remove tabs
            if "\n" in Doc:
                Doc = Doc.replace("\t", TAB_CHARACTER)
                Doc = Doc.replace("    ", TAB_CHARACTER)
                Lines = Doc.split("\n")
                Num = min(x.count(TAB_CHARACTER, 0, len(x) - len(x.lstrip())) for x in Lines[1:] if x)
                NewDoc = ""
                for Line in Lines:
                    if Num and Line.startswith(TAB_CHARACTER * Num):
                        Line = Line.partition(TAB_CHARACTER * Num)[2]
                    NewDoc += f"{Line}\n"
                Doc = NewDoc

            return Doc

        def _GetTypeHintString(TypeHint):
            if IS_PYTHON_39 and isinstance(TypeHint, typing._UnionGenericAlias):  # pylint: disable=protected-access
                return typing.get_args(TypeHint)[0].__name__
            if inspect.isclass(TypeHint):
                return TypeHint.__name__
            return str(TypeHint)

        def _PatchFunction(Function: StubFunction, DocumentedFunction: FunctionType):
            if DocumentedFunction.__doc__:
                Function.DocString = _ParseManualDocumentation(DocumentedFunction.__doc__)
            TypeHints = typing.get_type_hints(DocumentedFunction)
            StubParameters = Function.GetParameters()
            DocumentedSignature = inspect.signature(DocumentedFunction)

            for i, ParameterName in enumerate(DocumentedSignature.parameters):
                StubParam = StubParameters[i]
                Parameter = DocumentedSignature.parameters[ParameterName]
                StubParam.Name = ParameterName

                TypeHint = TypeHints.get(ParameterName)
                if TypeHint:
                    StubParam.Type = _GetTypeHintString(TypeHint)

                # Default values
                if Parameter.default is not inspect._empty:  # pylint: disable=protected-access
                    if "pyfbsdk" in str(type(Parameter.default)):
                        StubParam.DefaultValue = f"{type(Parameter.default).__name__}.{Parameter.default}"
                    else:
                        StubParam.DefaultValue = str(Parameter.default)

            if "return" in TypeHints:
                Function.ReturnType = _GetTypeHintString(TypeHints["return"])

        # Patch classes
        for Name, Object in inspect.getmembers(manualDoc, inspect.isclass):
            TypeHints = typing.get_type_hints(Object, localns = locals())
            StubClassRef = self.GetClassByName(Name)
            ClassMembers = dict(inspect.getmembers(Object))
            if StubClassRef:
                if Object.__doc__:
                    StubClassRef.DocString = _ParseManualDocumentation(Object.__doc__)

                # Patch properties
                for ClassMemberName, TypeHint in TypeHints.items():
                    StubPropertyRef = StubClassRef.GetPropertyByName(ClassMemberName)
                    if StubPropertyRef:
                        # Set type hint & doc string
                        StubPropertyRef.Type = _GetTypeHintString(TypeHint)
                        DocString = ClassMembers.get(f"{ClassMemberName}__doc__")
                        if DocString:
                            StubPropertyRef.DocString = _ParseManualDocumentation(DocString)

                PatchedStubFunctions = []
                for FunctionName, Function in inspect.getmembers(Object, inspect.isfunction):
                    bOverloadedFunction = re.search(r"_\d+$", Function.__name__)
                    if bOverloadedFunction:
                        FunctionName = FunctionName.rpartition("_")[0]
                    StubFunctionReferences = StubClassRef.GetFunctionsByName(FunctionName)
                    if StubFunctionReferences:
                        StubFunc = StubFunctionReferences[0]
                        if len(StubFunctionReferences) > 1:
                            Matches = [x for x in StubFunctionReferences if x not in PatchedStubFunctions and len(x.GetParameters()) == len(inspect.signature(Function).parameters)]
                            if not Matches:
                                continue
                            StubFunc = Matches[0]
                        _PatchFunction(StubFunc, Function)

                        PatchedStubFunctions.append(StubFunc)

        # Patch functions
        for Name, Object in inspect.getmembers(manualDoc, inspect.isfunction):
            StubFunctionRef = self.GetFunctionsByName(Name)
            if StubFunctionRef:
                _PatchFunction(StubFunctionRef[0], Object)

    def GenerateString(self, bUseOnlineDocumentation = True):
        """
        Returns: The stub file as a string
        """
        # Get the content
        Functions, Classes, Enums = GetPyfbsdkContent()

        # Generate the initial classes & functions
        self.Enums = [self._GenerateEnumInstance(Enum) for Enum in Enums]
        self.Classes = [self._GenerateClassInstance(Class) for Class in Classes]
        # Sort classes so that if there is if a class has a parent class, that parent comes before the child
        for Function in Functions:
            self.Functions.extend(self._GenerateFunctionInstances(Function))

        for Enum in self.Enums:
            self._PatchEnumFromDocumentation(Enum)

        # Use the online documentation to try and create better param names, values etc.
        if bUseOnlineDocumentation:
            self._PatchFunctionsFromDocumentation(self.Functions)
            self._PatchClassFromDocumentation(self.Classes)

        # Patch from the manual documentation
        self._PatchFromManualDocumentation()

        # Sort classes after all patches are done and we know their requirements
        self.Classes = SortClasses(self.Classes)

        # Generate a string
        StubString = GetCustomAdditions()  # Read the custom additions file first
        StubString += "\n".join([x.GetAsString() for x in self.Enums])
        StubString += "\n"
        StubString += "\n".join([x.GetAsString() for x in self.Classes])
        StubString += "\n"
        StubString += "\n".join([x.GetAsString() for x in self.Functions])

        return StubString


def GeneratePYFBSDKStub(Filepath, bCacheDocumentation = False) -> str:
    StartTime = time.time()

    Generator = PyfbsdkStubGenerator(bCacheDocumentation)

    FileContent = Generator.GenerateString()

    # Make sure directory exists
    if not os.path.isdir(os.path.dirname(Filepath)):
        os.makedirs(os.path.dirname(Filepath))

    with open(Filepath, "w+", encoding="utf-8") as File:
        File.write(FileContent)

    GenerationTime = time.time() - StartTime
    print(f"Generating pyfbsdk stub file took: {round(GenerationTime, 2)}s.")

    return Filepath


if bTest:
    DEFAULT_OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "generated-stub-files")
    OutFilepath = os.path.join(DEFAULT_OUTPUT_DIR, f"motionbuilder-{GetMotionBuilderVersion()}", "pyfbsdk.pyi")
    GeneratePYFBSDKStub(OutFilepath, bCacheDocumentation = True)
