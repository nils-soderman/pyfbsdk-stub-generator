from __future__ import annotations

import inspect
import typing

from dataclasses import dataclass


@dataclass
class Parameter:
    Name: str | None = ""
    Type: str | type | typing.Iterable[type | str] | None = None
    DefaultValue: typing.Any | str | None = None

    def GetTypeString(self) -> str | None:
        if self.Type is None:
            return None

        if isinstance(self.Type, typing.Iterable):
            return "|".join(x if isinstance(x, str) else x.__name__ for x in self.Type)

        if isinstance(self.Type, str):
            return self.Type

        return self.Type.__name__

    def GetDefaultValueString(self) -> str | None:
        if self.DefaultValue is None:
            return None

        if isinstance(self.DefaultValue, str):
            return self.DefaultValue

        return str(self.DefaultValue)


class FunctionBase:
    Parameters: typing.Iterable[Parameter | None] = ()
    ReturnType: str | None | type = None

    @classmethod
    def GetReturnTypeString(cls) -> str | None:
        if cls.ReturnType is None:
            return None

        if isinstance(cls.ReturnType, str):
            return cls.ReturnType

        return cls.ReturnType.__name__


class ClassBase:
    @classmethod
    def GetFunctionGroups(cls) -> list[list[type[FunctionBase]]]:
        Functions = []
        for Name, Obj in inspect.getmembers(cls):
            if isinstance(Obj, type) and issubclass(Obj, FunctionBase) and Obj != FunctionBase:
                Functions.append(Obj)
        return [Functions]

    @classmethod
    def GetProperties(cls) -> list[type[PropertyBase]]:
        Properties = []
        for Name, Obj in inspect.getmembers(cls):
            if isinstance(Obj, type) and issubclass(Obj, PropertyBase) and Obj != PropertyBase:
                Properties.append(Obj)
        return Properties


class PropertyBase:
    Types: type | str | typing.Iterable[type | str] | None = None
    SetType: typing.Iterable[type | str] | None = None

    @classmethod
    def GetTypesString(cls) -> str | None:
        if cls.Types is None:
            return None

        if isinstance(cls.Types, typing.Iterable):
            StrList = []
            for Type in cls.Types:
                if isinstance(Type, str):
                    StrList.append(Type)
                elif isinstance(Type, type):
                    StrList.append(Type.__name__)
                else:
                    raise RuntimeError(f"Unexpected type as Property Type in the manual docs: {cls} -> {Type}")
            return "|".join(StrList)

        if isinstance(cls.Types, str):
            return cls.Types

        return cls.Types.__name__
