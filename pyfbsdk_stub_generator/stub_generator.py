from __future__ import annotations

import typing
import time
import sys
import os

from importlib import reload
from types import FunctionType, ModuleType

import pyfbsdk

bTest = "builtin" in __name__
if bTest:
    # Reload all stub generator modules
    for ImportedModule in list(sys.modules.values()):
        if isinstance(ImportedModule, ModuleType) and "pyfbsdk_stub_generator" in ImportedModule.__name__:
            reload(ImportedModule)

    for Path in (
        os.path.dirname(os.path.dirname(__file__)),
        f"C:/Python{sys.version_info.major}{sys.version_info.minor}/lib/site-packages",
        f"{os.getenv('APPDATA')}/Python/Python{sys.version_info.major}{sys.version_info.minor}/site-packages"
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


def SortClasses(Classes: list[StubClass]):
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
    def __init__(self, Module: ModuleType, Plugins: typing.Iterable[type[plugins.PluginBaseClass]] | None = DEFAULT_PLUGINS):
        self.Module = Module
        self.Version = GetMotionBuilderVersion()

        self._AllClassNames = []

        self.Plugins: list[type[plugins.PluginBaseClass]] = list(Plugins) if Plugins else []
        self.Plugins.sort(key=lambda x: x.Priority)

    # ---------------------------------------------------
    #                      Internal
    # ---------------------------------------------------

    def GetAllClassNames(self):
        """ Get the names of all classes avaliable in the pyfbsdk module """
        if not self._AllClassNames:
            Functions, Classes, Enums = native_generator.GetModuleContent(self.Module)
            self._AllClassNames = [x.__name__ for x in Classes + Enums]
        return self._AllClassNames

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


def GenerateModuleStub(Module: ModuleType, Filepath: str) -> str:
    StartTime = time.time()

    Generator = StubGenerator(Module)
    FileContent = Generator.GenerateString()

    # Make sure directory exists
    if not os.path.isdir(os.path.dirname(Filepath)):
        os.makedirs(os.path.dirname(Filepath))

    with open(Filepath, "w+", encoding="utf-8") as File:
        File.write(FileContent)

    GenerationTime = time.time() - StartTime
    print(f"Generating pyfbsdk stub file took: {round(GenerationTime, 2)}s.")

    return Filepath


def GeneratePyfbsdkStubFile(Filepath: str):
    return GenerateModuleStub(pyfbsdk, Filepath)


if bTest:
    ModuleToGenerate = pyfbsdk
    DEFAULT_OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "generated-stub-files")
    OutFilepath = os.path.join(DEFAULT_OUTPUT_DIR, f"motionbuilder-{GetMotionBuilderVersion()}", f"{ModuleToGenerate.__name__}.pyi")
    GenerateModuleStub(ModuleToGenerate, OutFilepath)
