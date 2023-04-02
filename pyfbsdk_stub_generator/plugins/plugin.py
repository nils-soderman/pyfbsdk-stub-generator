from types import ModuleType

from ..module_types import StubClass, StubFunction, StubParameter, StubProperty


class PluginBaseClass():
    def __init__(self, Version: int, Module: ModuleType) -> None:
        self.Version = Version
        self.Module = Module

    def PatchClass(self, Class: StubClass):
        ...

    def PatchFunction(self, Function: StubFunction):
        ...
        
    def PatchEnum(self, Enum: StubClass):
        ...

    def PatchEnums(self, ClassList: list[StubClass]):
        for x in ClassList:
            self.PatchEnum(x)
            
    def PatchClasses(self, ClassList: list[StubClass]):
        for x in ClassList:
            self.PatchClass(x)

    def PatchFunctions(self, FunctionList: list[StubFunction]):
        for x in FunctionList:
            self.PatchFunction(x)
