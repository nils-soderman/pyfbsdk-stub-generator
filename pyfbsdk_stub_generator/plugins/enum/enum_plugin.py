""" 
Set the default value of the Enum properties to the correct value,
And remove the type of the Enum properties, to make them act like a `Literal[enum]`
"""
from __future__ import annotations

from ..plugin import PluginBaseClass
from ...module_types import StubClass


class PluginEnum(PluginBaseClass):
    Threading = False
    Priority = 100

    def PatchEnum(self, Enum: StubClass):
        for Property in Enum.GetStubProperties():
            Property.Type = None
            Property.Value = int(Property.Ref)
