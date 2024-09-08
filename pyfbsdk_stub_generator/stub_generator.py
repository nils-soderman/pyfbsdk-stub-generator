from __future__ import annotations

import typing
import time
import os

from types import ModuleType

import pyfbsdk

from . import plugins
from .module_types import StubClass
from . import native_generator


DEFAULT_PLUGINS = plugins.GetDefaultPlugins()


# -------------------------------------------------------------
#                       Helper Functios
# -------------------------------------------------------------

def GetMotionBuilderVersion() -> int:
    """ Get the current version of MotionBuilder """
    return int(2000 + pyfbsdk.FBSystem().Version / 1000)


# -------------------------------------------------------------
#                       Functions
# -------------------------------------------------------------

def GetBaseContent(Module: ModuleType) -> str:
    ModuleName = Module.__name__
    Filepath = os.path.join(os.path.dirname(__file__), "base_content", f"{ModuleName}.pyi")

    Content = ""
    if os.path.isfile(Filepath):
        with open(Filepath, 'r', encoding="utf-8") as File:
            Content = File.read().strip() + "\n"

    Content = Content.replace("{MOTIONBUILDER_VERSION}", str(GetMotionBuilderVersion()))

    return Content


def SortClasses(Classes: list[StubClass]) -> list[StubClass]:
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


class StubGenerator:
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

        # Generate a string
        StubString = GetBaseContent(self.Module)  # Read the custom additions file first
        StubString += "\n".join([x.GetAsString() for x in Enums])
        StubString += "\n"
        StubString += "\n".join([x.GetAsString() for x in Classes])
        StubString += "\n"

        for FunctionGroup in FunctionGroupList:
            bOverload = len(FunctionGroup) > 1  # If there are multiple functions with the same name, add @overload
            StubString += "\n".join([x.GetAsString(bOverload) for x in FunctionGroup])
            StubString += "\n"

        StubString = StubString.replace("    ", "\t") # Make sure tabs are used

        StubString += "\n"

        return StubString


def GeneratePyfbsdkStubFile(Filepath: str) -> str:
    StartTime = time.time()

    # Make sure directory exists
    Directory = os.path.dirname(Filepath)
    if not os.path.isdir(Directory):
        os.makedirs(Directory)

    Generator = StubGenerator(pyfbsdk)
    FileContent = Generator.GenerateString()

    with open(Filepath, "w+", encoding="utf-8") as File:
        File.write(FileContent)

    GenerationTime = time.time() - StartTime
    print(f"Generating pyfbsdk stub file took: {round(GenerationTime, 2)}s.")

    return Filepath
