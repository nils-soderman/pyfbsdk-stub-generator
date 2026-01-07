"""
Mark properties as read-only if docstring hints at it.
"""

from __future__ import annotations

from ..plugin_base import PluginBaseClass


class PluginReadOnly(PluginBaseClass):
    Priority = 100

    def PatchProperty(self, Class, Property):
        if Property.DocString.lower().startswith("read only property"):
            Property.ReadOnly = True
