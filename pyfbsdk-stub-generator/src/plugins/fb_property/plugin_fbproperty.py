""" 
This plugin patches the FBProperty classes to make sure properties and functions are correctly typed.
"""
from __future__ import annotations

import copy

import pyfbsdk

from ..plugin_base import PluginBaseClass
from ...module_types import StubClass, StubFunction

NAME_INDEX = "Index"
NAME_OBJECT = "Object"

TYPE_CONVERSION_MAP = {
    "Bool": "bool",
    "String": "str",
    "Int": "int",
    "Int64": "int",
    "UInt64": "int",
    "Float": "float",
    "Double": "float"
}

PROPERTY_TYPE_MAP = {
    pyfbsdk.FBPropertyType.kFBPT_Action: (pyfbsdk.FBPropertyAction, pyfbsdk.FBPropertyAnimatableAction),
    pyfbsdk.FBPropertyType.kFBPT_bool: (pyfbsdk.FBPropertyBool, pyfbsdk.FBPropertyAnimatableBool),
    pyfbsdk.FBPropertyType.kFBPT_charptr: (pyfbsdk.FBPropertyString, pyfbsdk.FBPropertyString),
    pyfbsdk.FBPropertyType.kFBPT_ColorRGB: (pyfbsdk.FBPropertyColor, pyfbsdk.FBPropertyAnimatableColor),
    pyfbsdk.FBPropertyType.kFBPT_ColorRGBA: (pyfbsdk.FBPropertyColorAndAlpha, pyfbsdk.FBPropertyAnimatableColorAndAlpha),
    pyfbsdk.FBPropertyType.kFBPT_double: (pyfbsdk.FBPropertyDouble, pyfbsdk.FBPropertyAnimatableDouble),
    pyfbsdk.FBPropertyType.kFBPT_enum: (pyfbsdk.FBPropertyEnum, pyfbsdk.FBPropertyAnimatableEnum),
    pyfbsdk.FBPropertyType.kFBPT_event: (pyfbsdk.FBProperty, None),
    pyfbsdk.FBPropertyType.kFBPT_float: (pyfbsdk.FBPropertyFloat, None),
    pyfbsdk.FBPropertyType.kFBPT_int: (pyfbsdk.FBPropertyInt, pyfbsdk.FBPropertyAnimatableInt),
    pyfbsdk.FBPropertyType.kFBPT_kReference: (None, None),
    pyfbsdk.FBPropertyType.kFBPT_object: (pyfbsdk.FBPropertyListObject, None),
    pyfbsdk.FBPropertyType.kFBPT_stringlist: (pyfbsdk.FBPropertyStringList, None),
    pyfbsdk.FBPropertyType.kFBPT_Reference: (None, None),
    pyfbsdk.FBPropertyType.kFBPT_Time: (pyfbsdk.FBPropertyTime, pyfbsdk.FBPropertyAnimatableTime),
    pyfbsdk.FBPropertyType.kFBPT_TimeCode: (pyfbsdk.FBPropertyTimeCode, pyfbsdk.FBPropertyAnimatableTimeCode),
    pyfbsdk.FBPropertyType.kFBPT_TimeSpan: (None, None),
    pyfbsdk.FBPropertyType.kFBPT_unknown: (None, None),
    pyfbsdk.FBPropertyType.kFBPT_Vector2D: (pyfbsdk.FBPropertyVector2d, pyfbsdk.FBPropertyAnimatableVector2d),
    pyfbsdk.FBPropertyType.kFBPT_Vector3D: (pyfbsdk.FBPropertyVector3d, pyfbsdk.FBPropertyAnimatableVector3d),
    pyfbsdk.FBPropertyType.kFBPT_Vector4D: (pyfbsdk.FBPropertyVector4d, pyfbsdk.FBPropertyAnimatableVector4d),
}


class PluginFbProperty(PluginBaseClass):
    PRIORITY = 200

    def get_data_type(self, stub_class: StubClass):
        """
        Find the correct data type for the given class based on its name.
        """
        type_str = stub_class.name
        for x in ("FBProperty", "Animatable", "List"):
            type_str = type_str.replace(x, "")

        # Base classes e.g. 'FBProperty'
        if not type_str:
            return "Any"

        if type_str in TYPE_CONVERSION_MAP:
            return TYPE_CONVERSION_MAP[type_str]

        type_str = f"FB{type_str}"
        if type_str in self.map_classes:
            return type_str

        # If the type can't be found and it's a FBPropertyListComponent, Use the base class 'FBComponent'
        if "FBPropertyListComponent" in stub_class.parents:
            return "FBComponent"

    def patch_class(self, stub_class: StubClass):
        self.patch_class_properties(stub_class)

        # FBProperty classes
        if stub_class.name.startswith("FBProperty"):
            self._patch_property_class(stub_class)

        elif stub_class.name == "FBComponent":
            self._patch_component(stub_class)

    def _patch_property_class(self, stub_class: StubClass):
        _type = self.get_data_type(stub_class)
        if _type is None:
            return

        is_list = "List" in stub_class.name

        if data_property := stub_class.get_property_by_name("Data"):
            data_property.Type = f"list[{_type}]" if is_list else _type

        if is_list:
            self._patch_property_list_class(stub_class, _type)

    def patch_class_properties(self, stub_class: StubClass):
        """ 
        Patch FBProperties used as class properties.
        * Add setter functions for animatable properties, that takes the native type as argument too.
        For example, `FBPropertyAnimatableDouble` can accept `float` as argument.
        """
        for stub_property in stub_class.get_stub_properties():
            # Animatable properties
            if stub_property.Type.startswith("FBPropertyAnimatable"):
                # Make setter functions that accept the correct type
                _type = self.map_classes.get(stub_property.Type)
                if _type:
                    if type_setter := self.get_data_type(_type):
                        stub_property.setter_type = f"{stub_property.Type}|{type_setter}"

    def _patch_property_list_class(self, stub_class: StubClass, Type: str):
        """ 
        Patch the FBPropertyList classes
        """
        for stub_function in stub_class.get_functions_by_name("__getitem__"):
            stub_function.return_type = Type
            stub_param = stub_function.get_parameters()[1]
            stub_param.Type = "int|slice"
            stub_param.name = NAME_INDEX

        # __setitem__ is not allowed for FBPropertyList
        stub_setitem = stub_class.get_functions_by_name("__setitem__")
        if stub_setitem in stub_class.stub_functions:
            stub_class.stub_functions.remove(stub_setitem)

        # Patch the first parameter of the following functions
        for name in ("append", "remove", "insert", "__contains__", "count"):
            for stub_function in stub_class.get_functions_by_name(name):
                stub_param = stub_function.get_parameters()[1]
                stub_param.Type = Type
                if stub_param.name.startswith(("arg", NAME_INDEX)):
                    stub_param.name = NAME_OBJECT

        for stub_function in stub_class.get_functions_by_name("pop"):
            stub_function.return_type = Type
            stub_param = stub_function.get_parameters()
            if len(stub_param) > 1:
                stub_param[1].Type = "int"
                stub_param[1].name = NAME_INDEX

        for stub_function in stub_class.get_functions_by_name("insert"):
            stub_parameters = stub_function.get_parameters()
            stub_parameters[1].Type = "int"
            stub_parameters[1].name = NAME_INDEX
            stub_parameters[2].Type = Type
            if stub_parameters[2].name.startswith("arg"):
                stub_parameters[2].name = NAME_OBJECT

    def _patch_component(self, stub_class: StubClass):
        """ 
        Patch the 'FBComponent.PropertyCreate' function
        Create @overload functions for each property type, that returns the correct FBProperty class.
        """
        stub_functions = stub_class.get_functions_by_name("PropertyCreate")
        assert len(stub_functions) == 1, f"Expected 1 PropertyCreate function, got {len(stub_functions)}"

        Function = stub_functions[0]

        # Make a new copy of the function list
        new_stub_functions: list[StubFunction] = []

        for property_type in pyfbsdk.FBPropertyType.values.values():
            if property_type not in PROPERTY_TYPE_MAP:
                print(f"{self.__class__.__name__}: PropertyType {property_type} not found in PROPERTY_TYPE_MAP")
                continue

            type_class, animatable_type_class = PROPERTY_TYPE_MAP[property_type]

            PropertyTypeName = f"Literal[{pyfbsdk.FBPropertyType.__name__}.{str(property_type)}]"

            if type_class is not None and type_class == animatable_type_class:
                variant = copy.copy(Function)
                variant.get_parameters()[2].Type = PropertyTypeName
                variant.return_type = type_class.__name__
                new_stub_functions.append(variant)

            else:
                if type_class:
                    variant = copy.copy(Function)
                    variant.get_parameters()[2].Type = PropertyTypeName
                    variant.get_parameters()[4].Type = "Literal[False]"

                    variant.return_type = type_class.__name__

                    new_stub_functions.append(variant)

                if animatable_type_class:
                    variant = copy.copy(Function)
                    variant.get_parameters()[2].Type = PropertyTypeName
                    variant.get_parameters()[4].Type = "Literal[True]"

                    variant.return_type = animatable_type_class.__name__

                    new_stub_functions.append(variant)

        stub_class.stub_functions.remove(stub_functions)

        new_stub_functions.extend(stub_functions)  # Re-add the generic PropertyCreate last
        stub_class.add_functions(new_stub_functions)
