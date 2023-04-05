import threading
import logging
import os

from types import ModuleType, FunctionType

from ..module_types import StubClass, StubFunction, StubParameter, StubProperty


class PluginBaseClass():
    Threading = True

    def __init__(self, Version: int, Module: ModuleType, EnumList: list[StubClass], ClassList: list[StubClass], FunctionGroupList: list[list[StubFunction]]) -> None:
        self.Version = Version
        self.ModuleName = Module.__name__

        self.EnumList = EnumList
        self.ClassList = ClassList
        self.FunctionGroupList = FunctionGroupList

        self.bDevMode = os.environ.get("PYFBSDK_DEVMODE") == "True"
        self.Exceptions = []

    def PatchClass(self, Class: StubClass):
        ...

    def PatchFunctionGroup(self, FunctionGroup: list[StubFunction]):
        ...

    def PatchEnum(self, Enum: StubClass):
        ...

    def Run(self):
        self._PatchEnums(self.EnumList)
        self._PatchClasses(self.ClassList)
        self._PatchFunctions(self.FunctionGroupList)

    def _PatchEnums(self, ClassList: list[StubClass]):
        self._RunPatcher(self.PatchEnum, ClassList)

    def _PatchClasses(self, ClassList: list[StubClass]):
        self._RunPatcher(self.PatchClass, ClassList)

    def _PatchFunctions(self, FunctionGroupList: list[list[StubFunction]]):
        self._RunPatcher(self.PatchFunctionGroup, FunctionGroupList)

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
