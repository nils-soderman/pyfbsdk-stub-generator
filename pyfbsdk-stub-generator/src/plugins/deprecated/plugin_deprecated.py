""" 
Plugin for marking classes, functions, and properties as deprecated
"""
from __future__ import annotations

from ..plugin_base import PluginBaseClass


def is_deprecated(docstring: str) -> bool:
    return "deprecated" in docstring.lower()


def extract_deprecation_message(docstring: str) -> str:
    deprecated_msg_index = -1

    lines = docstring.splitlines()
    for index, line in enumerate(lines):
        if "deprecated" in line.lower():
            deprecated_msg_index = index + 1

    if 0 <= deprecated_msg_index < len(lines):
        return lines[deprecated_msg_index].strip()

    return ""


class PluginDeprecated(PluginBaseClass):
    def patch_class(self, stub_class):
        super().patch_class(stub_class)

        if is_deprecated(stub_class.docstring):
            stub_class.deprecation_message = extract_deprecation_message(stub_class.docstring)

    def patch_function_group(self, stub_functions):
        for stub_function in stub_functions:
            if is_deprecated(stub_function.docstring):
                stub_function.deprecation_message = extract_deprecation_message(stub_function.docstring)

    def patch_property(self, stub_class, stub_property):
        if is_deprecated(stub_property.docstring):
            stub_property.deprecation_message = extract_deprecation_message(stub_property.docstring)
