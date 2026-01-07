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
    Priority = 200

    def GetDataType(self, Class: StubClass):
        """
        Find the correct data type for the given class based on its name.
        """
        Type = Class.Name
        for x in ("FBProperty", "Animatable", "List"):
            Type = Type.replace(x, "")

        # Base classes e.g. 'FBProperty'
        if not Type:
            return "Any"

        if Type in TYPE_CONVERSION_MAP:
            return TYPE_CONVERSION_MAP[Type]

        Type = f"FB{Type}"
        if Type in self.ClassMap:
            return Type

        # If the type can't be found and it's a FBPropertyListComponent, Use the base class 'FBComponent'
        if "FBPropertyListComponent" in Class.Parents:
            return "FBComponent"

    def PatchClass(self, Class: StubClass):
        self.PatchClassProperties(Class)

        # FBProperty classes
        if Class.Name.startswith("FBProperty"):
            self.PatchPropertyClass(Class)

        elif Class.Name == "FBComponent":
            self.PatchFBComponent(Class)

    def PatchPropertyClass(self, Class: StubClass):
        Type = self.GetDataType(Class)
        if Type is None:
            return

        bIsList = "List" in Class.Name

        DataProperty = Class.GetPropertyByName("Data")
        if DataProperty:
            DataProperty.Type = f"list[{Type}]" if bIsList else Type

        if bIsList:
            self.PatchListPropertyClass(Class, Type)

    def PatchClassProperties(self, Class: StubClass):
        """ 
        Patch FBProperties used as class properties.
        * Add setter functions for animatable properties, that takes the native type as argument too.
        For example, `FBPropertyAnimatableDouble` can accept `float` as argument.
        """
        for Property in Class.GetStubProperties():
            # Animatable properties
            if Property.Type.startswith("FBPropertyAnimatable"):
                # Make setter functions that accept the correct type
                TypeClass = self.ClassMap.get(Property.Type)
                if TypeClass:
                    SetterType = self.GetDataType(TypeClass)
                    if SetterType:
                        Property.SetterType = f"{Property.Type}|{SetterType}"

    def PatchListPropertyClass(self, Class: StubClass, Type: str):
        """ 
        Patch the FBPropertyList classes
        """
        for Function in Class.GetFunctionsByName("__getitem__"):
            Function.ReturnType = Type
            Param = Function.GetParameters()[1]
            Param.Type = "int"
            Param.Name = NAME_INDEX

        # __setitem__ is not allowed for FBPropertyList
        SetItem = Class.GetFunctionsByName("__setitem__")
        if SetItem in Class.StubFunctions:
            Class.StubFunctions.remove(SetItem)

        # Patch the first parameter of the following functions
        for FunctionName in ("append", "remove", "insert", "__contains__", "count"):
            for Function in Class.GetFunctionsByName(FunctionName):
                Param = Function.GetParameters()[1]
                Param.Type = Type
                if Param.Name.startswith(("arg", NAME_INDEX)):
                    Param.Name = NAME_OBJECT

        for Function in Class.GetFunctionsByName("pop"):
            Function.ReturnType = Type
            Param = Function.GetParameters()
            if len(Param) > 1:
                Param[1].Type = "int"
                Param[1].Name = NAME_INDEX

        for Function in Class.GetFunctionsByName("insert"):
            Params = Function.GetParameters()
            Params[1].Type = "int"
            Params[1].Name = NAME_INDEX
            Params[2].Type = Type
            if Params[2].Name.startswith("arg"):
                Params[2].Name = NAME_OBJECT

    def PatchFBComponent(self, Class: StubClass):
        """ 
        Patch the 'FBComponent.PropertyCreate' function
        Create @overload functions for each property type, that returns the correct FBProperty class.
        """
        Functions = Class.GetFunctionsByName("PropertyCreate")
        assert len(Functions) == 1, f"Expected 1 PropertyCreate function, got {len(Functions)}"

        Function = Functions[0]

        # Make a new copy of the function list
        NewFunctionList: list[StubFunction] = []

        for PropertyType in pyfbsdk.FBPropertyType.values.values():
            if PropertyType not in PROPERTY_TYPE_MAP:
                print(f"{self.__class__.__name__}: PropertyType {PropertyType} not found in PROPERTY_TYPE_MAP")
                continue

            TypeClass, AnimatableTypeClass = PROPERTY_TYPE_MAP[PropertyType]

            PropertyTypeName = f"Literal[{pyfbsdk.FBPropertyType.__name__}.{str(PropertyType)}]"

            if TypeClass is not None and TypeClass == AnimatableTypeClass:
                Variant = copy.copy(Function)
                Variant.GetParameters()[2].Type = PropertyTypeName
                Variant.ReturnType = TypeClass.__name__
                NewFunctionList.append(Variant)

            else:
                if TypeClass:
                    Variant = copy.copy(Function)
                    Variant.GetParameters()[2].Type = PropertyTypeName
                    Variant.GetParameters()[4].Type = "Literal[False]"

                    Variant.ReturnType = TypeClass.__name__

                    NewFunctionList.append(Variant)

                if AnimatableTypeClass:
                    Variant = copy.copy(Function)
                    Variant.GetParameters()[2].Type = PropertyTypeName
                    Variant.GetParameters()[4].Type = "Literal[True]"

                    Variant.ReturnType = AnimatableTypeClass.__name__

                    NewFunctionList.append(Variant)

        Class.StubFunctions.remove(Functions)

        NewFunctionList.extend(Functions)  # Re-add the generic PropertyCreate last
        Class.AddFunctions(NewFunctionList)
