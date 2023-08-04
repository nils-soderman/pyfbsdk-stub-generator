from __future__ import annotations

import importlib
import inspect

from typing import TypeVar, Generator

from .doc_bases import FunctionBase, ClassBase
from ..plugin import PluginBaseClass
from ...module_types import StubClass, StubFunction, StubParameter, StubProperty

T = TypeVar('T')


class PluginManualDocumentation(PluginBaseClass):
    Threading = False
    Priority = 150

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # try to import the module
        try:
            self.ContentModule = importlib.import_module(f".modules.{self.ModuleName}", package=__package__)
            importlib.reload(self.ContentModule)
        except ModuleNotFoundError:
            self.ContentModule = None

        self.ManualFunctionMap = {x.__name__: x for x in self.GetContent(FunctionBase)}
        self.ManualClassMap = {x.__name__: x for x in self.GetContent(ClassBase)}

    def GetContent(self, Type: type[T]) -> list[T]:
        Content = []
        for Name, Obj in inspect.getmembers(self.ContentModule):
            if inspect.isclass(Obj) and issubclass(Obj, Type) and Obj != Type:
                Content.append(Obj)
        return Content

    def ShouldPatch(self) -> bool:
        return self.ContentModule is not None

    def PatchEnum(self, Enum: StubClass):
        ...

    def PatchClass(self, Class: StubClass):
        if Class.Name not in self.ManualClassMap:
            return

        # Get functions from class
        ManualClass = self.ManualClassMap[Class.Name]

        for ManualFunctionGroup in ManualClass.GetFunctionGroups():
            FunctionName = ManualFunctionGroup[0].__name__
            StubFunctionGroup = Class.GetFunctionsByName(FunctionName)
            if len(ManualFunctionGroup) > 1 or len(StubFunctionGroup) > 1:
                raise RuntimeError(f"FunctionGroup with more than one function is not yet supported. {ManualFunctionGroup}")

            self._PatchFunctionGroup(StubFunctionGroup[0], ManualFunctionGroup[0])

    def _PatchFunctionGroup(self, Function: StubFunction, ManualFunction: FunctionBase):
        if ManualFunction.__doc__:
            Function.DocString = PatchDocString(ManualFunction.__doc__)

        ReturnType = ManualFunction.GetReturnTypeString()
        if ReturnType:
            Function.ReturnType = ReturnType

        for Parameter, ManualDocParameter in zip(Function.GetParameters(True), ManualFunction.Parameters):
            if not ManualDocParameter:
                continue

            if ManualDocParameter.Name:
                Parameter.Name = ManualDocParameter.Name

            Type = ManualDocParameter.GetTypeString()
            if Type:
                Parameter.Type = Type

            DefaultValue = ManualDocParameter.GetDefaultValueString()
            if DefaultValue is not None:
                Parameter.DefaultValue = DefaultValue

    def PatchFunctionGroup(self, FunctionGroup: list[StubFunction]):
        if not FunctionGroup:
            return

        Function = FunctionGroup[0]
        if Function.Name not in self.ManualFunctionMap:
            return

        if len(FunctionGroup) > 1:
            raise RuntimeError(f"FunctionGroup with more than one function is not yet supported. {FunctionGroup}")

        ManualFunctionDoc = self.ManualFunctionMap[Function.Name]
        self._PatchFunctionGroup(Function, ManualFunctionDoc)


def PatchDocString(DocString: str):
    Lines = []

    for Line in DocString.splitlines():

        # Remove one indent from each line since the docstring is indented one level
        if Line.startswith("    "):
            Line = Line[4:]

        Lines.append(Line)

    return "\n".join(Lines)
