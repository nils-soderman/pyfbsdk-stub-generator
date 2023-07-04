
from __future__ import annotations

from pyfbsdk_stub_generator.module_types import StubClass, StubFunction

from ..plugin import PluginBaseClass
from ...module_types import StubClass, StubFunction, StubParameter, StubProperty

# Dunder methods that we want to assume they return self
DUNDER_METHODS_RETURNING_SELF = {"__add__", "__sub__", "__mul__", "__truediv__", "__floordiv__", "__mod__", "__divmod__", "__pow__", "__neg__",
                                 "__isub__", "__iadd__", "__imul__", "__itruediv__", "__ifloordiv__", "__imod__", "__ipow__", "__idiv__",
                                 "__radd__", "__rsub__", "__rmul__", "__rtruediv__", "__rfloordiv__", "__rmod__", "__rdivmod__", "__rpow__", "__rneg__"}

# Some dunder methods have a different return type than the class they are defined in
CONVERT_DUNDER_RETURN_TYPE = {
    "FBPropertyAnimatableDouble": "float",
}

KNOWN_RETURN_TYPES = {
    "__float__": "float",
}


class PluginDunderMethods(PluginBaseClass):
    Threading = False
    Priority = 200

    def PatchClass(self, Class: StubClass):
        for FunctionGroup in Class.StubFunctions:
            for Function in FunctionGroup:
                if Function.ReturnType != "object":
                    continue

                if Function.Name in DUNDER_METHODS_RETURNING_SELF:
                    Function.ReturnType = Class.Name

                    if Function.ReturnType in CONVERT_DUNDER_RETURN_TYPE:
                        Function.ReturnType = CONVERT_DUNDER_RETURN_TYPE[Function.ReturnType]
                    elif Function.Name.startswith("FBProperty"):
                        print(f"Warning: {Class.Name}.{Function.Name} has a return type of self. This is probably wrong. Might need a new entry in `plugins.dunder_methods.CONVERT_DUNDER_RETURN_TYPE`.")

                elif Function.Name in KNOWN_RETURN_TYPES:
                    Function.ReturnType = KNOWN_RETURN_TYPES[Function.Name]
