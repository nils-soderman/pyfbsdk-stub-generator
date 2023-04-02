import threading
import os

from types import ModuleType

from ..module_types import StubClass, StubFunction, StubParameter, StubProperty


class PluginBaseClass():
    Threading = True

    def __init__(self, Version: int, Module: ModuleType) -> None:
        self.Version = Version
        # self.Module = Module
        self.ModuleName = Module.__name__

        self.bDevMode = os.environ.get("PYFBSDK_DEVMODE") == "True"

    def PatchClass(self, Class: StubClass):
        ...

    def PatchFunction(self, Function: StubFunction):
        ...

    def PatchEnum(self, Enum: StubClass):
        ...

    def PatchEnums(self, ClassList: list[StubClass]):
        if self.Threading:
            Threads = []
            for x in ClassList:
                Thread = threading.Thread(target=self.PatchEnum, args=(x,))
                Threads.append(Thread)
                Thread.start()
            for Thread in Threads:
                Thread.join()
        else:
            for x in ClassList:
                self.PatchEnum(x)

    def PatchClasses(self, ClassList: list[StubClass]):
        if self.Threading:
            Threads = []
            for x in ClassList:
                Thread = threading.Thread(target=self.PatchClass, args=(x,))
                Threads.append(Thread)
                Thread.start()
            for Thread in Threads:
                Thread.join()
        else:
            for x in ClassList:
                self.PatchClass(x)

    def PatchFunctions(self, FunctionList: list[StubFunction]):
        if self.Threading:
            Threads = []
            for x in FunctionList:
                Thread = threading.Thread(target=self.PatchFunction, args=(x,))
                Threads.append(Thread)
                Thread.start()
            for Thread in Threads:
                Thread.join()
        else:
            for x in FunctionList:
                self.PatchFunction(x)
