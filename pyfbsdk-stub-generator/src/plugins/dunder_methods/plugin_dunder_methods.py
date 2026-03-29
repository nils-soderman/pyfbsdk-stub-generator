from __future__ import annotations

from ..plugin_base import PluginBaseClass
from ...module_types import StubClass, StubFunction, StubParameter, StubProperty


# Dunder methods that we want to assume they return self
METHODS_RETURNING_SELF = {"__add__", "__sub__", "__mul__", "__truediv__", "__floordiv__", "__mod__", "__divmod__", "__pow__", "__neg__",
                          "__isub__", "__iadd__", "__imul__", "__itruediv__", "__ifloordiv__", "__imod__", "__ipow__", "__idiv__",
                          "__radd__", "__rsub__", "__rmul__", "__rtruediv__", "__rfloordiv__", "__rmod__", "__rdivmod__", "__rpow__", "__rneg__",
                          "__copy__", "__deepcopy__"}

# Some dunder methods have a different return type than the class they are defined in
CONVERT_DUNDER_RETURN_TYPE = {
    "FBPropertyAnimatableDouble": "float",
}

KNOWN_RETURN_TYPES: dict[str, type] = {
    "__float__": float,
    "__gt__": bool,
    "__lt__": bool,
    "__ge__": bool,
    "__le__": bool
}


class PluginDunderMethods(PluginBaseClass):
    PRIORITY = 200

    def patch_class(self, stub_class: StubClass):
        for stub_functions in stub_class.stub_functions:
            if not stub_functions:
                continue

            for stub_function in stub_functions:
                if stub_function.return_type != "Any":
                    continue

                if stub_function.name in METHODS_RETURNING_SELF:
                    stub_function.return_type = stub_class.name

                    if stub_function.return_type in CONVERT_DUNDER_RETURN_TYPE:
                        stub_function.return_type = CONVERT_DUNDER_RETURN_TYPE[stub_function.return_type]
                    elif stub_function.name.startswith("FBProperty"):
                        print(f"Warning: {stub_class.name}.{stub_function.name} has a return type of self. This is probably wrong. Might need a new entry in `plugins.dunder_methods.CONVERT_DUNDER_RETURN_TYPE`.")

                elif stub_function.name in KNOWN_RETURN_TYPES:
                    stub_function.return_type = KNOWN_RETURN_TYPES[stub_function.name].__name__

            # If the class has __getitem__ implemented, we should also add the __iter__ method.
            # Technically, this is not correct. But otherwise typecheckers like PyRight & MyPy will complain that the
            # class is not iterable & not compatible with the typing.Iterable protocol.
            if stub_functions[0].name == "__getitem__":
                # Make sure we don't add __iter__ twice:
                if not any(x[0].name == "__iter__" for x in stub_class.stub_functions if x):
                    return_type = f"Iterator[{stub_functions[0].return_type}]"
                    stub_function = StubFunction(None, "__iter__", [StubParameter(None, "self")], return_type)
                    stub_class.add_functions([stub_function])
