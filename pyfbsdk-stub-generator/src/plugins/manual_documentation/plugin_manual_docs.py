from __future__ import annotations

import importlib

from .base import ClassDoc, FunctionDoc, PropertyDoc
from ..plugin_base import PluginBaseClass
from ...module_types import StubClass, StubFunction, StubProperty


class PluginManualDocumentation(PluginBaseClass):
    PRIORITY = 150

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # try to import the module
        try:
            self.content_module = importlib.import_module(f".modules.{self.module.__name__}", package=__package__)
        except ModuleNotFoundError:
            self.content_module = None

        self.manual_function_map: dict[str, FunctionDoc] = {}
        self.manual_class_map: dict[str, ClassDoc] = {}
        if self.content_module:
            self.manual_function_map: dict[str, FunctionDoc] = {k.__name__: v for k, v in getattr(self.content_module, 'FUNCTIONS', {}).items()}
            self.manual_class_map: dict[str, ClassDoc] = {k.__name__: v for k, v in getattr(self.content_module, 'CLASSES', {}).items()}

    def should_patch(self) -> bool:
        return self.content_module is not None

    def patch_class(self, stub_class: StubClass):
        if stub_class.name not in self.manual_class_map:
            return

        manual_cls = self.manual_class_map[stub_class.name]

        for manual_fn in manual_cls.functions:
            stub_functions = stub_class.get_functions_by_name(manual_fn.name)
            if len(stub_functions) > 1:
                raise RuntimeError(f"FunctionGroup with more than one function is not yet supported. {manual_fn.name}")

            if stub_functions:
                self._patch_function_group(stub_functions[0], manual_fn)

        for manual_property in manual_cls.properties:
            stub_property = stub_class.get_property_by_name(manual_property.name)
            if not stub_property:
                raise Warning(f"Property {manual_property.name} not found in {stub_class.name}")

            self._patch_property(stub_property, manual_property)

    def patch_function_group(self, stub_functions: list[StubFunction]):
        if not stub_functions:
            return

        stub_function = stub_functions[0]
        if stub_function.name not in self.manual_function_map:
            return

        if len(stub_functions) > 1:
            raise RuntimeError(f"FunctionGroup with more than one function is not yet supported. {stub_functions}")

        function_doc = self.manual_function_map[stub_function.name]
        self._patch_function_group(stub_function, function_doc)

    def _patch_property(self, prop: StubProperty, manual_prop_doc: PropertyDoc):
        if manual_prop_doc.doc:
            prop.docstring = manual_prop_doc.doc

        if type_str := manual_prop_doc.get_type_as_string():
            prop.Type = type_str

    def _patch_function_group(self, stub_function: StubFunction, manual_function_doc: FunctionDoc):
        if manual_function_doc.doc:
            stub_function.docstring = manual_function_doc.doc

        if return_type := manual_function_doc.get_return_type_as_string():
            stub_function.return_type = return_type

        for stub_parameter, manual_paramter_doc in zip(stub_function.get_parameters(True), manual_function_doc.parameters):
            if not manual_paramter_doc:
                continue

            if manual_paramter_doc.name:
                stub_parameter.name = manual_paramter_doc.name

            if type_str := manual_paramter_doc.get_type_as_string():
                stub_parameter.Type = type_str

            default_value = manual_paramter_doc.get_default_value_as_string()
            if default_value is not None:
                stub_parameter.default_value = default_value
    