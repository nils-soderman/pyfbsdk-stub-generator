from __future__ import annotations

import importlib

from .base import ClassDoc, FunctionDoc, PropertyDoc
from ..plugin_base import PluginBaseClass
from ...module_types import StubClass, StubFunction, StubProperty


class PluginManualDocumentation(PluginBaseClass):
    Priority = 150

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # try to import the module
        try:
            self.content_module = importlib.import_module(f".modules.{self.ModuleName}", package=__package__)
        except ModuleNotFoundError:
            self.content_module = None

        self.manual_function_map: dict[str, FunctionDoc] = {}
        self.manual_class_map: dict[str, ClassDoc] = {}
        if self.content_module:
            self.manual_function_map: dict[str, FunctionDoc] = {k.__name__: v for k, v in getattr(self.content_module, 'FUNCTIONS', {}).items()}
            self.manual_class_map: dict[str, ClassDoc] = {k.__name__: v for k, v in getattr(self.content_module, 'CLASSES', {}).items()}

    def ShouldPatch(self) -> bool:
        return self.content_module is not None

    def PatchClass(self, Class: StubClass):
        if Class.Name not in self.manual_class_map:
            return

        manual_cls = self.manual_class_map[Class.Name]

        for manual_fn in manual_cls.functions:
            StubFunctionGroup = Class.GetFunctionsByName(manual_fn.name)
            if len(StubFunctionGroup) > 1:
                raise RuntimeError(f"FunctionGroup with more than one function is not yet supported. {manual_fn.name}")

            if StubFunctionGroup:
                self._patch_function_group(StubFunctionGroup[0], manual_fn)

        for manual_property in manual_cls.properties:
            StubPropertyInstance = Class.GetPropertyByName(manual_property.name)
            if not StubPropertyInstance:
                raise Warning(f"Property {manual_property.name} not found in {Class.Name}")

            self._patch_property(StubPropertyInstance, manual_property)

    def PatchFunctionGroup(self, FunctionGroup: list[StubFunction]):
        if not FunctionGroup:
            return

        Function = FunctionGroup[0]
        if Function.Name not in self.manual_function_map:
            return

        if len(FunctionGroup) > 1:
            raise RuntimeError(f"FunctionGroup with more than one function is not yet supported. {FunctionGroup}")

        ManualFunctionDoc = self.manual_function_map[Function.Name]
        self._patch_function_group(Function, ManualFunctionDoc)

    def _patch_property(self, prop: StubProperty, manual_prop_doc: PropertyDoc):
        if manual_prop_doc.doc:
            prop.DocString = manual_prop_doc.doc

        if type_str := manual_prop_doc.get_type_as_string():
            prop.Type = type_str

    def _patch_function_group(self, stub_function: StubFunction, manual_function_doc: FunctionDoc):
        if manual_function_doc.doc:
            stub_function.DocString = manual_function_doc.doc

        if return_type := manual_function_doc.get_return_type_as_string():
            stub_function.ReturnType = return_type

        for stub_parameter, manual_paramter_doc in zip(stub_function.GetParameters(True), manual_function_doc.parameters):
            if not manual_paramter_doc:
                continue

            if manual_paramter_doc.name:
                stub_parameter.Name = manual_paramter_doc.name

            if type_str := manual_paramter_doc.get_type_as_string():
                stub_parameter.Type = type_str

            default_value = manual_paramter_doc.get_default_value_as_string()
            if default_value is not None:
                stub_parameter.DefaultValue = default_value
    