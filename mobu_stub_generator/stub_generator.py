#
#   Code to generate a stub files
#
from __future__ import annotations

import importlib
import inspect
import typing
import pydoc
import time
import sys
import os
import re

from importlib import reload

from . import motionbuilder_documentation_parser as docParser

reload(docParser)

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "generated-stub-files")


# ---------------------------
#     Enums And Structs
# ---------------------------


class FObjectType:
    Function = 'function'
    Class = 'class'
    Property = 'property'
    Enum = 'type'

# --------------------------------------------------------
#                    Patch Functions
# --------------------------------------------------------


def PatchGeneratedDocString(Text):
    # Replace content
    if not Text:
        return ""

    for TagName, ReplaceWith in [("<b>", ""), ("</b>", ""), ("b>", ""), ("\\", "\\\\")]:
        Text = Text.replace(TagName, ReplaceWith)

    # Patch @code, example:
    #   @code
    #   print("Hello World")
    #   @endcode
    if "@code" in Text:
        NewText = ""
        bInCodeBlock = False
        bFirstCodeLine = False
        for Line in Text.split("\n"):
            Line += "\n"
            if bInCodeBlock:
                if Line.startswith("@endcode"):
                    bInCodeBlock = False
                    Line = "\n"
                elif not Line.strip():
                    continue
                else:
                    if Line.strip().startswith("//"):
                        Line = Line.replace("//", "#")
                    if not bFirstCodeLine:
                        Line = "    %s" % Line
                bFirstCodeLine = False
            elif Line.startswith("@code"):
                bFirstCodeLine = True
                bInCodeBlock = True
                Line = "\n>>> "

            NewText += Line
        Text = NewText

    # Remove p prefix from parameters, example: pVector -> Vector
    Text = re.sub(r"\s(p)([A-Z])", r"\2", Text)

    return Text.strip()


def PatchParameterName(Param: str):
    # Remove the 'p' prefix
    if Param.startswith("p"):
        if not (len(Param) == 2 and Param[1].isdigit()):
            Param = Param[1:]

    if Param == "True":
        Param = "bState"

    return Param


def PatchVariableType(VariableType: str, ExistingClassNames, ClassMembers = [], Default = None, bAlwaysTryToRemoveProperty = True):
    """
    Patch property types to match what's avaliable for Python.
    """

    if VariableType == "enum":
        return "_Enum"

    if not VariableType.startswith("FB"):
        if VariableType.startswith("Property"):
            NewVariableType = VariableType.replace("Property", "", 1)
            if NewVariableType in ExistingClassNames or NewVariableType in ClassMembers:
                return NewVariableType
            return Default

        if VariableType[0].isupper() and not VariableType.startswith("List["):
            if VariableType in ExistingClassNames or VariableType in ClassMembers:
                return VariableType
            return Default

        return VariableType

    FBEventName = "FBEvent"
    if VariableType.startswith(FBEventName) and not (VariableType in ExistingClassNames or VariableType in ClassMembers):
        if FBEventName in ExistingClassNames or FBEventName in ClassMembers:
            return FBEventName

    if bAlwaysTryToRemoveProperty or VariableType not in ExistingClassNames:
        for Key, Value in docParser.CToPythonVariableTranslation.items():
            if "fbproperty%s" % Key.lower() == VariableType.lower() or "fbpropertyanimatable%s" % Key.lower() == VariableType.lower():
                return Value

        if VariableType.startswith("FBPropertyAnimatable"):
            NewVariableType = VariableType.replace("PropertyAnimatable", "", 1)
        else:
            NewVariableType = VariableType.replace("Property", "", 1)

        if NewVariableType in ExistingClassNames or NewVariableType in ClassMembers:
            return NewVariableType

    if VariableType in ExistingClassNames or VariableType in ClassMembers:
        return VariableType

    return Default


def PatchDefaultValue(Value:str, ExistingClassNames, ClassMembers = [], Default = None):
    
    if Value.startswith("FB"):
        return Value
        if Value not in ExistingClassNames or Value not in ClassMembers:
            if Value.lower().startswith("fbstring"):
                return ""
            
            return Default
        
        return Value
    
    return Value

# --------------------------------------------------------
#                       Classes
# --------------------------------------------------------

class StubSettings():
    TabCharacter = "    "


class StubBaseClass():
    def __init__(self, Name = "", Indentation = 0, Settings = None) -> None:
        self.Name = Name
        self._DocString = ""
        self.SetIndentationLevel(Indentation)
        self.Settings = Settings if Settings else StubSettings()

    def SetIndentationLevel(self, Level: int):
        self._Indentation = Level

    def GetAsString(self) -> str:
        """
        Get instance as python code (in string format)
        """
        raise NotImplementedError("GetAsString() has not yet been implemented")

    def SetDocString(self, Text):
        """ Will patch the docstring before setting it """
        self._DocString = PatchGeneratedDocString(Text)

    def GetDocString(self):
        if self._DocString:
            return '"""%s"""' % self._DocString
        return ""

    def Indent(self, Text, bCurrent = False):
        Level = self._Indentation if bCurrent else self._Indentation + 1
        return "\n".join([(self.Settings.TabCharacter * Level) + Line.strip() for Line in Text.split("\n")])

    def GetRequirements(self) -> list:
        """
        Get a list of variable/class names that needs to be declared before the current object
        """
        raise NotImplementedError("GetRequirements() has not yet been implemented")


class StubClass(StubBaseClass):
    def __init__(self, Name = "", Indentation = 0, Settings = None):
        super().__init__(Name = Name, Indentation = Indentation, Settings = Settings)
        self.Parents = []
        self.StubProperties = []
        self.StubFunctions = []

    def GetRequirements(self) -> list:
        # The class parent's needs to be declared before the class
        FunctionRequirements = []
        for Function in self.StubFunctions:
            FunctionRequirements += Function.GetRequirements()
        return self.Parents + FunctionRequirements

    def AddProperty(self, Property: StubProperty):
        self.StubProperties.append(Property)

    def AddFunction(self, Function: StubFunction):
        self.StubFunctions.append(Function)

    def GetAsString(self):
        ParentClassesAsString = ','.join(self.Parents)
        ClassAsString = "class %s(%s):\n" % (self.Name, ParentClassesAsString)

        if self.GetDocString():
            ClassAsString += "%s\n" % self.Indent(self.GetDocString())

        ClassMembers = self.StubProperties + self.StubFunctions
        for StubObject in ClassMembers:
            StubObject.SetIndentationLevel(1)
            ClassAsString += "%s\n" % StubObject.GetAsString()

        # If class doesn't have any members, add a ...
        if not len(ClassMembers):
            ClassAsString += self.Indent("...")

        return ClassAsString.strip()


class StubFunction(StubBaseClass):
    def __init__(self, Name = "", Indentation = 0, Settings = None):
        super().__init__(Name = Name, Indentation = Indentation, Settings = Settings)
        self._Params = []
        self.ReturnType = None
        self.bIsClassFunction = False

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
        if self.bIsClassFunction:
            if len(self._Params) < 1:
                return "self"
            self._Params[0].bIsClassSelfParam = True
        ParametersAsStrings = [x.GetAsString() for x in self._Params]
        return ",".join(ParametersAsStrings)

    def GetAsString(self):
        FunctionAsString = self.Indent(
            'def %s(%s)' % (self.Name, self.GetParamsAsString()),
            bCurrent = True
        )

        if self.ReturnType and self.ReturnType != "None":
            FunctionAsString += '->%s' % self.ReturnType

        FunctionAsString += ":"

        DocString = self.GetDocString()
        if DocString:
            FunctionAsString += "\n%s\n%s" % (self.Indent(DocString), self.Indent("..."))
        else:
            FunctionAsString += "..."

        return FunctionAsString


class StubParameter():
    def __init__(self, Name, Type = None, DefaultValue = None):
        self.Name = Name
        self.Type = Type
        self.DefaultValue = DefaultValue
        self.bIsClassSelfParam = False

    def GetRequirements(self):
        if self.DefaultValue and self.DefaultValue.startswith("FB"):
            RequirementClass: str = self.DefaultValue
            if "." in RequirementClass:
                RequirementClass = RequirementClass.partition(".")[0]
            return [RequirementClass]
        return []

    def GetAsString(self):
        if self.bIsClassSelfParam:
            return "self"

        ParamString = PatchParameterName(self.Name)

        if self.Type:
            ParamString += ":%s" % self.Type

        if self.DefaultValue != docParser.FMoBoDocsParameterNames.NoDefaultValue:
            if self.DefaultValue and self.DefaultValue.startswith("k"):
                ParamString += "=%s.%s" % (self.Type, self.DefaultValue)
            else:
                ParamString += "=%s" % self.DefaultValue

        return ParamString


class StubProperty(StubBaseClass):
    def __init__(self, Name="", Indentation = 0, Settings = None):
        super().__init__(Name = Name, Indentation = Indentation, Settings = Settings)
        self._Type = None

    def GetType(self):
        if self._Type:
            return self._Type
        return "property"

    def SetType(self, Type):
        self._Type = Type

    def GetAsString(self):
        PropertyAsString = self.Indent("%s:%s" % (self.Name, self.GetType()), bCurrent = True)
        if self.GetDocString():
            PropertyAsString += "\n"
            PropertyAsString += self.Indent(self.GetDocString(), bCurrent = True)

        return PropertyAsString


class GeneratedPythonDocumentation():
    """ pyfbsdk comes with a pyfbsdk_gen_doc.py, containing some doc strings etc. """

    def __init__(self, ModuleName):
        if os.path.isabs(ModuleName):
            # TODO: Load module from abs path instead (using importlib)
            raise Exception("Absolute path to module is currently not supported!\nWhen trying to load: %s" % ModuleName)

        ImportedModule = importlib.import_module(ModuleName)
        self.Members = dict(inspect.getmembers(ImportedModule))

    def GetMemberByName(self, Name):
        return self.Members.get(Name)

    def GetDocString(self, Name):
        Member = self.GetMemberByName(Name)
        return Member.__doc__ if Member else ""


# --------------------------------------------------------
#                Helper functions
# --------------------------------------------------------

def GetObjectType(Object):
    """ Get object type as a string """
    return type(Object).__name__


def IsPrivate(Object):
    """ Check if the name of an object begins with a underscore """
    return Object.__name__.startswith("_")


def GetClassParents(Class):
    return Class.__bases__


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


def GetClassMembers(Class):
    IgnoreMembers = ["names", "values", "__slots__", "__instance_size__"]
    Members = inspect.getmembers(Class)
    ParentClass = GetClassParents(Class)[0]
    UniqueMemebers = [x for x in Members if not hasattr(ParentClass, x[0]) and x[0] not in IgnoreMembers and not x[0].startswith("__")]
    return UniqueMemebers


def SortClasses(Classes: list):
    """ 
    Sort classes based on their parent class
    If a class has another class as their parent class, it'll be placed later in the list
    """
    ClassNames = [x.Name for x in Classes]

    i = 0
    while (i < len(Classes)):
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


def GetParametersFromFunction(Function):
    """
    Try to get the return value from a function's docstring
    (The docstring in pyfbsdk looks something like: "def MyFunc() -> bool")
    """
    try:
        return [StubParameter(x) for x in inspect.getargspec(Function).args]
    except:
        pass

    DocString: str = Function.__doc__
    if not DocString or "->" not in DocString:
        return []

    HelpFunction = DocString.partition("->")[0]
    if "(" not in HelpFunction:
        return []

    HelpParameterString = HelpFunction.split("(", 1)[1].strip()[:-1]
    HelpParameterString = HelpParameterString.replace("]", "").replace("[", "")
    HelpParameters = HelpParameterString.split(",")
    ReturnValue = []

    for Parameter in HelpParameters:
        if not Parameter or ")" not in Parameter:
            continue
        Type, ParamName = Parameter.strip().split(")")
        ReturnValue.append(
            StubParameter(ParamName.strip(), Type[1:].strip())
        )

    return ReturnValue


def GetReturnTypeFromDocString(Function):
    if not Function.__doc__ or "->" not in Function.__doc__:
        return None

    ReturnType = Function.__doc__.split("->", 1)[1].strip()
    if "\n" in ReturnType:
        ReturnType = ReturnType.split("\n")[0].strip()
    if ReturnType.endswith(":"):
        ReturnType = ReturnType[:-1].strip()

    return ReturnType

# --------------------------------------------------------
#                   Generate Functions
# --------------------------------------------------------


def GenerateStubClassFunction(Function, DocMembers, ExistingClassNames, ClassMemberNames, DocPage: docParser.DocumentationPage = None):
    StubFunctionInstance = GenerateStubFunction(Function, DocMembers)
    StubFunctionInstance.bIsClassFunction = True

    if DocPage:
        Member = DocPage.GetMember(Function.__name__)
        if Member:
            # Return Type
            if not StubFunctionInstance.ReturnType.startswith("FB"):
                Type = Member.GetType(bConvertToPython = True)
                if Type:
                    Type = PatchVariableType(Type, ExistingClassNames, ClassMemberNames)
                    if Type and not Type.startswith("k"):
                        StubFunctionInstance.ReturnType = Type

            for CurrentParam, DocParam in zip(StubFunctionInstance.GetParameters()[1:], Member.Params):
                if DocParam.Name:
                    CurrentParam.Name = DocParam.Name

                NewParamType = DocParam.GetType(bConvertToPython = True)
                if NewParamType:
                    CurrentParam.Type = PatchVariableType(NewParamType, ExistingClassNames, ClassMemberNames, bAlwaysTryToRemoveProperty = False)

                DefaultValue = DocParam.GetDefaultValue(bConvertToPython = True)
                if DefaultValue:
                    CurrentParam.DefaultValue = DefaultValue # PatchDefaultValue(DefaultValue, ExistingClassNames, ClassMemberNames)

    return StubFunctionInstance


def GenerateStubFunction(Function, DocMembers, MoBuDocumentation: docParser.MotionBuilderDocumentation = None):
    FunctionName: str = Function.__name__

    StubFunctionInstance = StubFunction(FunctionName)

    # Parameters
    Parameters = GetParametersFromFunction(Function)

    DocRef = DocMembers.get(FunctionName) if DocMembers else None
    if DocRef:
        StubFunctionInstance.SetDocString(DocRef.__doc__)
        DocArgumentNames = inspect.getargspec(DocRef).args
        for Parameter, DocArgName in zip(Parameters, DocArgumentNames):
            Parameter.Name = DocArgName

    for Parameter in Parameters:
        StubFunctionInstance.AddParameter(Parameter)

    # Return Type
    StubFunctionInstance.ReturnType = GetReturnTypeFromDocString(Function)

    return StubFunctionInstance


def GenerateStubClass(Module, Class, GeneratedPyDoc, AllClassNames, MoBuDocumentation: docParser.MotionBuilderDocumentation = None, bIsEnum = False):
    ClassName: str = Class.__name__
    DocClasses = [x for x in GeneratedPyDoc if GetObjectType(x) in ["class", "type"]]
    DocMemberNames = [x.__name__ for x in DocClasses]

    StubClassInstance = StubClass(ClassName)
    StubClassInstance.Parents = GetClassParentNames(Class)

    Page = MoBuDocumentation.GetSDKClassByName(ClassName) if MoBuDocumentation else None

    # TODO: DocMembers/DocGenRef etc. could be a class
    DocGenRef = GeneratedPyDoc.get(ClassName)
    DocGenMembers = {}
    if DocGenRef:
        StubClassInstance.SetDocString(DocGenRef.__doc__)
        DocGenMembers = dict(GetClassMembers(DocGenRef))

    ClassMembers = GetClassMembers(Class)
    ClassMemberNames = [x[0] for x in ClassMembers]
    for Name, Reference in ClassMembers:
        MemberType = GetObjectType(Reference)
        WebDocMember = Page.GetMember(Name) if Page else None
        if MemberType == FObjectType.Function:
            try:
                StubClassInstance.AddFunction(
                    GenerateStubClassFunction(Reference, DocGenMembers, AllClassNames, ClassMemberNames, Page)
                )
            except Exception as e:
                print(e)
        else:
            Property = StubProperty(Name)

            # Enums should have their 'self' as type
            if bIsEnum:
                Property.SetType(ClassName)

            # Class Member
            else:
                # Try to get the property type from the documentation
                Type = WebDocMember.GetType(bConvertToPython = True) if WebDocMember else None
                if not Type:
                    # Attempt to get the type by evaluating some code
                    try:
                        exec("import %s" % Module.__name__)
                        Type = eval("type(%s.%s().%s).__name__" % (Module.__name__, ClassName, Name))
                    except Exception as e:
                        # pyfbsdk FBModel types must be inialized with a name
                        if Module.__name__ == "pyfbsdk":
                            try:
                                if eval("issubclass(%s.%s, %s.FBModel)" % (Module.__name__, ClassName, Module.__name__)):
                                    Type = eval("type(%s.%s('stub-generator-temp').%s).__name__" % (Module.__name__, ClassName, Name))
                            except Exception as e:
                                pass

                    if Type == "NoneType":
                        Type = None

                if Type:
                    Type = PatchVariableType(Type, AllClassNames, ClassMemberNames)
                    Property.SetType(Type)

            # Get property doc string
            PropertyDocGenRef = DocGenMembers.get(Name)
            if PropertyDocGenRef:
                Property.SetDocString(PropertyDocGenRef.__doc__)

            # Add property to the class
            StubClassInstance.AddProperty(Property)

    return StubClassInstance


# --------------------------------------------------------
#                   Main generate function
# --------------------------------------------------------

def GenerateStub(Module, Filepath: str, SourcePyFile = "", DocumentationVersion: int = None):
    """
    Generate a stubfile

    * Module: Reference to a module to generate a stubfile
    * Filepath: The output abs filepath
    * SourcePyFile: If there exists a source .py file with doc comments (like pyfbsdk_gen_doc.py)
    """
    StartTime = time.time()

    # Create a documentation instance
    MoBuDocumentation = None
    if DocumentationVersion:
        SupportedDocumentationVersion = docParser.GetClosestSupportedMotionBuilderVersion(DocumentationVersion)
        MoBuDocumentation = docParser.MotionBuilderDocumentation(SupportedDocumentationVersion, bCache = True)

    # Get all members from the pre-generated doc/stub file
    GeneratedPyDoc = GeneratedPythonDocumentation(SourcePyFile) if SourcePyFile else None
    if SourcePyFile:
        ImportedModule = importlib.import_module(SourcePyFile)
        GeneratedPyDoc = dict(inspect.getmembers(ImportedModule))

    # Get all Functions, Classes etc. inside of the module
    Functions = [x[1] for x in inspect.getmembers(Module) if GetObjectType(x[1]) == FObjectType.Function and not IsPrivate(x[1])]
    Classes = [x[1] for x in inspect.getmembers(Module) if GetObjectType(x[1]) == FObjectType.Class]
    Enums = [x[1] for x in inspect.getmembers(Module) if GetObjectType(x[1]) == FObjectType.Enum]
    Misc = [x for x in inspect.getmembers(Module) if GetObjectType(x[1]) not in [FObjectType.Function, FObjectType.Class, FObjectType.Enum]]
    AllClassNames = [x.__name__ for x in Classes + Enums]

    # Construct stub class instances based on all functions & classes found in the module
    StubFunctions = [GenerateStubFunction(x, GeneratedPyDoc, MoBuDocumentation) for x in Functions]
    StubClasses = [GenerateStubClass(Module, x, GeneratedPyDoc, AllClassNames, MoBuDocumentation) for x in Classes]
    StubEnums = [GenerateStubClass(Module, x, GeneratedPyDoc, AllClassNames, bIsEnum = True) for x in Enums]

    Classes = SortClasses(StubClasses)

    #
    # Generate the stub file content as a string
    #

    StubFileContent = ""

    # Extra custom additions
    AdditionsFilepath = os.path.join(os.path.dirname(__file__), "additions_%s.py" % Module.__name__)
    if os.path.isfile(AdditionsFilepath):
        with open(AdditionsFilepath, 'r') as File:
            StubFileContent += "%s\n" % File.read()

    # Add Enums, Classes & Functions to the string
    StubFileContent += "%s\n" % "\n".join([x.GetAsString() for x in StubEnums + StubClasses + StubFunctions])

    # Write content into the file
    with open(Filepath, "w+") as File:
        File.write(StubFileContent)

    # Print how long it took to generate the stub file
    ElapsedTime = time.time() - StartTime
    print("Generating stub for module '%s' took %ss" % (Module.__name__, ElapsedTime))

    return True
