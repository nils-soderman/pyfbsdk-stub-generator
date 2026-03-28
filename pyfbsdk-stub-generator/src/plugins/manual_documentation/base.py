from __future__ import annotations

import types
import typing

from dataclasses import dataclass, field


def _arg_to_string(t: type | str) -> str:
    if t is type(None):
        return "None"

    if isinstance(t, str):
        return t

    return t.__name__


def _type_to_string(_type: str | type | types.UnionType | typing.Iterable[type | str] | None) -> str | None:
    if _type is None:
        return None

    if isinstance(_type, str):
        return _type

    if isinstance(_type, types.UnionType) or typing.get_origin(_type) is typing.Union:
        return "|".join(_arg_to_string(t) for t in typing.get_args(_type))

    if isinstance(_type, typing.Iterable):
        return "|".join(_arg_to_string(x) for x in _type)

    return _type.__name__


@dataclass
class ParamDoc:
    name: str | None = ""
    parameter_type: str | type | types.UnionType | typing.Iterable[type | str] | None = None
    default_value: typing.Any | None = None

    def get_type_as_string(self) -> str | None:
        return _type_to_string(self.parameter_type)

    def get_default_value_as_string(self) -> str | None:
        if self.default_value is None:
            return None

        if isinstance(self.default_value, str):
            return self.default_value

        return str(self.default_value)


@dataclass
class FunctionDoc:
    ref: str | typing.Callable | None = None
    parameters: list[ParamDoc | None] = field(default_factory=list)
    return_type: str | type | types.UnionType | typing.Iterable[type | str] | None = None
    doc: str | None = None

    @property
    def name(self) -> str:
        assert self.ref is not None, "FunctionDoc.ref must be set for inline use"
        return self.ref if isinstance(self.ref, str) else self.ref.__name__

    def get_return_type_as_string(self) -> str | None:
        return _type_to_string(self.return_type)


@dataclass
class PropertyDoc:
    name: str
    property_type: str | type | types.UnionType | typing.Iterable[type | str] | None = None
    doc: str | None = None

    def get_type_as_string(self) -> str | None:
        return _type_to_string(self.property_type)


@dataclass
class ClassDoc:
    properties: list[PropertyDoc] = field(default_factory=list)
    functions: list[FunctionDoc] = field(default_factory=list)
