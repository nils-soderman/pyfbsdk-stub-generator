from __future__ import annotations

import pyfbsdk

import importlib
import inspect
import typing
import pydoc
import time
import sys
import os
import re

from importlib import reload

sys.path.append(os.path.dirname(__file__))

import motionbuilder_documentation_parser as docParser


reload(docParser)

DEFAULT_OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "generated-stub-files")
ADDITIONS_FILEPATH = os.path.join(os.path.dirname(__file__), "additions_pyfbsdk.py")
TAB_CHARACTER = "    "


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
    return TAB_CHARACTER + ("\n%s" % TAB_CHARACTER).join(Text.split("\n"))


# -------------------------------------------------------------
#                       Functions
# -------------------------------------------------------------


def GetCustomAdditions():
    with open(ADDITIONS_FILEPATH, 'r') as File:
        return File.read().strip() + "\n"


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


def GetUniqueClassMembers(Class, Ignore = [], AllowedOverrides = []):
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

# -------------------------------------------------------------
#                       Classes
# -------------------------------------------------------------


class StubBaseClass():
    def __init__(self, Name = "") -> None:
        self.Name = Name
        self.DocString = ""

    def GetAsString(self) -> str:
        """
        Get instance as python code (in string format)
        """
        raise NotImplementedError("GetAsString() has not yet been implemented")

    def GetDocString(self):
        if self.DocString:
            return '"""%s"""' % self.DocString
        return ""

    def GetRequirements(self) -> list:
        """
        Get a list of variable/class names that needs to be declared before the current object
        """
        raise NotImplementedError("GetRequirements() has not yet been implemented")


class StubFunction(StubBaseClass):
    def __init__(self, Name = "", Parameters = [], ReturnType = None):
        super().__init__(Name = Name)
        self._Params = Parameters
        self.ReturnType = ReturnType
        self.bIsMethod = False
        self.bIsOverload = False

    def AddParameter(self, Parameter):
        self._Params.append(Parameter)

    def GetParameters(self):
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

        FunctionAsString += 'def %s(%s)' % (self.Name, self.GetParamsAsString())

        if self.ReturnType and self.ReturnType != "None":
            FunctionAsString += '->%s' % self.ReturnType

        FunctionAsString += ":"

        DocString = self.GetDocString()
        if DocString:
            FunctionAsString += "\n%s\n%s" % (Indent(DocString), Indent("..."))
        else:
            FunctionAsString += "..."

        return FunctionAsString


class StubClass(StubBaseClass):
    def __init__(self, Name = ""):
        super().__init__(Name = Name)
        self.Parents = []
        self.StubProperties = []
        self.StubFunctions = []

    def AddFunction(self, Function: StubFunction):
        Function.bIsMethod = True  # Make function a method
        self.StubFunctions.append(Function)

    def AddProperty(self, Property: StubProperty):
        self.StubProperties.append(Property)

    def AddParent(self, Parent: str):
        self.Parents.append(Parent)

    def GetRequirements(self) -> list:
        # The class parent's needs to be declared before the class
        FunctionRequirements = []
        for Function in self.StubFunctions:
            FunctionRequirements += Function.GetRequirements()
        return self.Parents + FunctionRequirements

    def GetAsString(self):
        ParentClassesAsString = ','.join(self.Parents)

        ClassAsString = "class %s(%s):\n" % (self.Name, ParentClassesAsString)

        if self.GetDocString():
            ClassAsString += "%s\n" % Indent(self.GetDocString())

        ClassMembers = self.StubProperties + self.StubFunctions
        for StubObject in ClassMembers:
            ClassAsString += "%s\n" % Indent(StubObject.GetAsString())

        # If class doesn't have any members, add a ...
        if not len(ClassMembers):
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
        PropertyAsString = "%s:%s" % (self.Name, self.Type)

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

    def GetAsString(self):
        ParamString = self.Name  # PatchParameterName(self.Name)
        if self.Type:
            ParamString += ":%s" % self.Type

        if self.DefaultValue is not None:
            ParamString += "=%s" % self.DefaultValue

        return ParamString


# ---------------------------------------------------------------------------------
#                                  GENERATOR
# ---------------------------------------------------------------------------------


class PyfbsdkStubGenerator():
    def __init__(self):
        self.Functions = []
        self.Classes = []
        self.Enums = []

    def _GenerateEnumInstance(self, Class):
        """ 
        Generate enum instances based on the loaded pyfbsdk module
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

    def _GenerateClassInstance(self, Class):
        """ 
        Generate enum instances based on the loaded pyfbsdk module
        """
        # Create the stub instance
        ClassName = GetObjectName(Class)
        ClassInstance = StubClass(ClassName)

        # Get all members and generate stub properties of them
        ClassMemebers = GetUniqueClassMembers(Class, Ignore = ["__instance_size__"], AllowedOverrides = ["__init__"])
        for MemberName, MemberReference in ClassMemebers:
            Type = GetObjectType(MemberReference)
            if Type == FObjectType.Function:
                for StubMethod in self._GenerateFunctionInstances(MemberReference):
                    ClassInstance.AddFunction(StubMethod)
            elif MemberName not in ["__init__"]:
                Property = StubProperty(MemberName)
                Property.Type = GetObjectType(MemberReference)
                ClassInstance.AddProperty(Property)

        # Set the parent classes
        for ParentClassName in GetClassParentNames(Class):
            ClassInstance.AddParent(ParentClassName)

        return ClassInstance

    def _GenerateFunctionInstances(self, Function):
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

    def GenerateString(self):
        """ 
        Returns: The stub file as a string 
        """
        # Get the content
        Functions, Classes, Enums = GetPyfbsdkContent()

        # Generate a string
        self.Enums = [self._GenerateEnumInstance(Enum) for Enum in Enums]
        self.Classes = [self._GenerateClassInstance(Class) for Class in Classes]
        for Function in Functions:
            self.Functions.extend(self._GenerateFunctionInstances(Function))

        StubString = GetCustomAdditions()
        StubString += "\n".join([x.GetAsString() for x in self.Enums])
        StubString += "\n"
        StubString += "\n".join([x.GetAsString() for x in self.Classes])
        StubString += "\n"
        StubString += "\n".join([x.GetAsString() for x in self.Functions])

        return StubString


def GeneratePYFBSDKStub(Filepath):
    Generator = PyfbsdkStubGenerator()

    FileContent = Generator.GenerateString()

    with open(Filepath, "w+") as File:
        File.write(FileContent)


def main():
    StartTime = time.time()

    MotionBuilderVersion = GetMotionBuilderVersion()
    Filepath = os.path.join(DEFAULT_OUTPUT_DIR, "motionbuilder-%s" % MotionBuilderVersion, "pyfbsdk.py")
    GeneratePYFBSDKStub(Filepath)

    GenerationTime = time.time() - StartTime
    print("Generating pyfbsdk stub file took: %ss." % GenerationTime)


main()
