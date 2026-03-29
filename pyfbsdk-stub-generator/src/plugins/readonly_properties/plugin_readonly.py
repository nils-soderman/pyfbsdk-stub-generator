"""
Mark properties as read-only if docstring hints at it.
"""

from __future__ import annotations

from ..plugin_base import PluginBaseClass


class PluginReadOnly(PluginBaseClass):
    PRIORITY = 100

    def patch_property(self, stub_class, stub_property):
        if stub_property.docstring:
            first_line = stub_property.docstring.partition("\n")[0]
            if "read only property" in first_line.lower():
                stub_property.read_only = True
