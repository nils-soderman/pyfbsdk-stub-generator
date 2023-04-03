import threading
import logging
import os

from types import ModuleType, FunctionType

from ..module_types import StubClass, StubFunction, StubParameter, StubProperty


class PluginBaseClass():
    Threading = True

    def __init__(self, Version: int, Module: ModuleType) -> None:
        self.Version = Version
        # self.Module = Module
        self.ModuleName = Module.__name__

        self.bDevMode = os.environ.get("PYFBSDK_DEVMODE") == "True"
        self.Exceptions = []

    def PatchClass(self, Class: StubClass):
        ...

    def PatchFunction(self, Function: StubFunction):
        ...

    def PatchEnum(self, Enum: StubClass):
        ...

    def PatchEnums(self, ClassList: list[StubClass]):
        self._RunPatcher(self.PatchEnum, ClassList)

    def PatchClasses(self, ClassList: list[StubClass]):
        self._RunPatcher(self.PatchClass, ClassList)

    def PatchFunctions(self, FunctionGroupList: list[list[StubFunction]]):
        self._RunPatcher(self.PatchFunction, FunctionGroupList)

    def _RunPatcher(self, PatchFunction: FunctionType, StubList: list):
        StopEvent = threading.Event()
        
        def _ThreadedPatcher(self, StubItem):
            try:
                PatchFunction(StubItem)
            except Exception as e:
                self.Exceptions.append(e)
                StopEvent.set()

        if self.Threading:
            Threads = []
            for x in StubList:
                Thread = threading.Thread(target=_ThreadedPatcher, args=(x,))
                Threads.append(Thread)
                Thread.start()
            for Thread in Threads:
                Thread.join()

            if self.Exceptions:
                raise self.Exceptions[0]
            
            if StopEvent.is_set():
                for Thread in Threads:
                    Thread.join()
        else:
            for x in StubList:
                PatchFunction(x)
