""" 
Set the default value of the Enum properties to the correct value,
And remove the type of the Enum properties, to make them act like a `Literal[enum]`
"""
from __future__ import annotations

from ..plugin_base import PluginBaseClass
from ...module_types import StubClass


class PluginEnum(PluginBaseClass):
    PRIORITY = 100

    def patch_enum(self, stub_enum: StubClass):
        for stub_property in stub_enum.get_stub_properties():
            stub_property.Type = None
            stub_property.value = int(stub_property.ref)  # type: ignore
