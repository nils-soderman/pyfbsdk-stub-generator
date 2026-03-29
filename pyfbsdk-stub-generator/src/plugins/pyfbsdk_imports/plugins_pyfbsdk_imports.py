""" 
Plugin meant for patching modules that import pyfbsdk and reference its classes.
Those will need the pyfbsdk. prefix added for them to link to the correct class.
"""
from __future__ import annotations

import pyfbsdk

from ..plugin_base import PluginBaseClass
from ...module_types import StubClass


class PluginPyfbsdkImports(PluginBaseClass):
    Priority = 200

    def ShouldPatch(self) -> bool:
        return self.module is not pyfbsdk

    def PatchClass(self, stub_class: StubClass):
        for parent_index, parent in enumerate(stub_class.Parents):
            if parent.startswith("FB") and hasattr(pyfbsdk, parent):
                stub_class.Parents[parent_index] = f"pyfbsdk.{parent}"

            for stub_property in stub_class.StubProperties:
                if stub_property.Type.startswith("FB") and hasattr(pyfbsdk, stub_property.Type):
                    stub_property.Type = f"pyfbsdk.{stub_property.Type}"
