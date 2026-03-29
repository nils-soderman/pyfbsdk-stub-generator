from __future__ import annotations

import threading

from types import ModuleType
import typing

from ..module_types import StubClass, StubFunction, StubProperty
from ..flags import GeneratorFlag


class PluginBaseClass:
    THREADING = False
    PRIORITY = 100

    def __init__(self, 
                 version: int, 
                 module: ModuleType, 
                 stub_enums: list[StubClass], 
                 stub_classes: list[StubClass], 
                 stub_functions: list[list[StubFunction]], 
                 flags: GeneratorFlag) -> None:
        self.flags = flags
        self.version = version
        self.module = module

        self.stub_enums = stub_enums
        self.stub_classes = stub_classes
        self.stub_functions = stub_functions

        self.map_classes = {x.name: x for x in stub_classes}
        self.map_enums = {x.name: x for x in stub_enums}
        self.map_functions = {x[0].name: x for x in stub_functions if x}

        self.exceptions = []

    def should_patch(self) -> bool:
        return True

    def patch_class(self, stub_class: StubClass):
        for stub_property in stub_class.stub_properties:
            self.patch_property(stub_class, stub_property)

        for stub_method in stub_class.stub_functions:
            self.patch_method(stub_class, stub_method)

    def patch_method(self, stub_class: StubClass, stub_methods: list[StubFunction]):
        pass

    def patch_property(self, stub_class: StubClass, stub_property: StubProperty):
        pass

    def patch_function_group(self, stub_functions: list[StubFunction]):
        pass

    def patch_enum(self, Enum: StubClass):
        pass

    def run(self):
        if not self.should_patch():
            return
        
        print(f"  [{self.PRIORITY}] Running plugin: {self.__class__.__name__}")

        self._patch_enums(self.stub_enums)
        self._patch_classes(self.stub_classes)
        self._patch_functions(self.stub_functions)

    def _patch_enums(self, stub_enums: list[StubClass]):
        self._run_patcher(self.patch_enum, stub_enums)

    def _patch_classes(self, stub_classes: list[StubClass]):
        self._run_patcher(self.patch_class, stub_classes)

    def _patch_functions(self, stub_functions: list[list[StubFunction]]):
        self._run_patcher(self.patch_function_group, stub_functions)

    def _run_patcher(self, patch_function: typing.Callable, stub_list: list[StubClass] | list[list[StubFunction]]):
        event_stop = threading.Event()

        def _threaded_patcher(self, stub_item: StubClass | list[StubFunction]):
            try:
                patch_function(stub_item)
            except Exception as e:
                self.exceptions.append(e)
                event_stop.set()

        if self.THREADING:
            threads: list[threading.Thread] = []
            for x in stub_list:
                thread = threading.Thread(target=_threaded_patcher, args=(self, x,))
                threads.append(thread)
                thread.start()
            for thread in threads:
                thread.join()

            if self.exceptions:
                raise self.exceptions[0]

            if event_stop.is_set():
                for thread in threads:
                    thread.join()
        else:
            for x in stub_list:
                patch_function(x)
