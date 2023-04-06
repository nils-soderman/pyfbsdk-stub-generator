from __future__ import annotations

import time
import sys
import os

from importlib import reload
from types import FunctionType, ModuleType

import pyfbsdk

bTest = "builtin" in __name__
if bTest:
    for Path in (
        os.path.dirname(os.path.dirname(__file__)),
        f"C:/Python{sys.version_info.major}{sys.version_info.minor}/lib/site-packages"
    ):
        if Path not in sys.path:
            sys.path.append(Path)
    __name__ = "pyfbsdk_stub_generator.stub_generator"  # pylint: disable=redefined-builtin
    os.environ["PYFBSDK_DEVMODE"] = "True"

from . import plugins
from .module_types import StubClass, StubFunction, StubParameter, StubProperty
from . import native_generator

reload(plugins)
reload(native_generator)

DEFAULT_PLUGINS = plugins.GetDefaultPlugins()

# TODO: Broken stuff:
# FBModel.GetHierarchyWorldMatrices() - First param in the docs doesn't exists in the python version
# FBInterpolateRotation() - Both of them use the same documentation :/
# Support URLs in the doc strings
# FBStoryClip -> GetAffectedAnimationNodes & FBModel::GetHierarchyWorldMatrices()
# GetCommandLineArgs - Turn blockquotes into: ```


TranslationDefaultValues = {
    "FRAMES_30": "FBTimeCode.FRAMES_30"
}

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


# -------------------------------------------------------------
#                       Functions
# -------------------------------------------------------------

def GetBaseContent(Module: ModuleType):
    ModuleName = Module.__name__
    Filepath = os.path.join(os.path.dirname(__file__), "base_content", f"{ModuleName}.pyi")

    Content = ""
    if os.path.isfile(Filepath):
        with open(Filepath, 'r', encoding="utf-8") as File:
            Content = File.read().strip() + "\n"

    Content = Content.replace("{MOTIONBUILDER_VERSION}", str(GetMotionBuilderVersion()))

    return Content


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


# ---------------------------------------------------------------------------------
#                                  GENERATOR
# ---------------------------------------------------------------------------------


class StubGenerator():
    def __init__(self, Module: ModuleType, Plugins: list[type[plugins.PluginBaseClass]] | None = DEFAULT_PLUGINS):
        self.Module = Module
        self.Version = GetMotionBuilderVersion()

        self._AllClassNames = []
        
        self.Plugins: list[type[plugins.PluginBaseClass]] = Plugins if Plugins else []

    # ---------------------------------------------------
    #                      Internal
    # ---------------------------------------------------

    def GetAllClassNames(self):
        """ Get the names of all classes avaliable in the pyfbsdk module """
        if not self._AllClassNames:
            Functions, Classes, Enums = native_generator.GetModuleContent(self.Module)
            self._AllClassNames = [x.__name__ for x in Classes + Enums]
        return self._AllClassNames

    # ---------------------------------------------------
    #                   Final Patch
    # ---------------------------------------------------

    def FinalPatchClass(self, Class: StubClass, Classes: list[StubClass]):
        for Function in Class.StubFunctions:
            self.FinalPatchFunction(Function, Classes)

    def FinalPatchFunction(self, Function: StubFunction, Classes: list[StubClass]):
        for Parameter in Function.GetParameters():
            self.FinalPatchParameter(Parameter, Classes)

    def FinalPatchParameter(self, Parameter: StubParameter, Classes: list[StubClass]):
        # Patch the type if it's an enum that lives as a subclass
        if Parameter.Type and Parameter.Type.startswith("E"):
            if Parameter.Type not in self.GetAllClassNames():
                # Find the class that the enum is a part of
                for Class in Classes:
                    if hasattr(Class.Ref, Parameter.Type):
                        Parameter.Type = f"{Class.Name}.{Parameter.Type}"
                        if Parameter.DefaultValue and "." not in Parameter.DefaultValue:
                            Parameter.DefaultValue = f"{Parameter.Type}.{Parameter.DefaultValue}"
                        break

        if Parameter.DefaultValue in TranslationDefaultValues:
            Parameter.DefaultValue = TranslationDefaultValues[Parameter.DefaultValue]

    def GenerateString(self) -> str:
        """
        Returns: The stub file as a string
        """
        # Get the content
        Enums, Classes, FunctionGroupList = native_generator.GenerateModuleSubs(self.Module)

        # Run all of the plugins
        for PluginType in self.Plugins:
            Plugin = PluginType(self.Version, self.Module, Enums, Classes, FunctionGroupList)
            Plugin.Run()

        # Do a final patch before generating the docstring
        # for StubClassInstance in Classes:
        #     self.FinalPatchClass(StubClassInstance, Classes)
        # for StubFunctionInstance in Functions:
        #     self.FinalPatchFunction(StubFunctionInstance, Classes)

        # Sort classes after all patches are done and we know their requirements
        Classes = SortClasses(Classes)
        
        # Flatten the functions list
        FlatFunctionList = [x for y in FunctionGroupList for x in y]

        # Generate a string
        StubString = GetBaseContent(self.Module)  # Read the custom additions file first
        StubString += "\n".join([x.GetAsString() for x in Enums])
        StubString += "\n"
        StubString += "\n".join([x.GetAsString() for x in Classes])
        StubString += "\n"
        StubString += "\n".join([x.GetAsString() for x in FlatFunctionList])
        StubString += "\n"

        return StubString


def GeneratePYFBSDKStub(Filepath: str) -> str:
    StartTime = time.time()

    Generator = StubGenerator(pyfbsdk)
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
    GeneratePYFBSDKStub(OutFilepath)
