""" 
This plugin patches the FBProperty classes to make sure they have the correct types for e.g. Data & __getitem__
"""
from __future__ import annotations

from ..plugin import PluginBaseClass
from ...module_types import StubClass, StubFunction, StubParameter, StubProperty


class PluginFbProperty(PluginBaseClass):
    Threading = False
    Priority = 200

    ConvertTypeDict = {
        "Bool": "bool",
        "String": "str",
        "Int": "int",
        "Int64": "int",
        "UInt64": "int",
        "Float": "float",
        "Double": "float"
    }

    def GetDataType(self, Class: StubClass):
        # Figure out the data type based on the class name
        Type = Class.Name
        for x in ("FBProperty", "Animatable", "List"):
            Type = Type.replace(x, "")

        # For the base classes e.g. FBProperty
        if not Type:
            return None

        if Type in self.ConvertTypeDict:
            return self.ConvertTypeDict[Type]

        Type = f"FB{Type}"
        if Type in self.ClassMap:
            return Type

    def PatchClass(self, Class: StubClass):
        # Only patch FBProperty classes
        if not Class.Name.startswith("FBProperty"):
            return

        Type = self.GetDataType(Class)
        if Type is None:
            return

        bIsList = "List" in Class.Name

        DataProperty = Class.GetPropertyByName("Data")
        if DataProperty:
            DataProperty.Type = f"list[{Type}]" if bIsList else Type

        if bIsList:
            GetItemFunction = Class.GetFunctionsByName("__getitem__")
            for Function in GetItemFunction:
                Function.ReturnType = Type
                Param = Function.GetParameters()[1]
                Param.Type = "int"
                Param.Name = "Index"