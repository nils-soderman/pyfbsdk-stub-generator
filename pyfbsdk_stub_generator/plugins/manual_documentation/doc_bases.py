from __future__ import annotations

import inspect
import typing

from dataclasses import dataclass


@dataclass
class Parameter:
    Name: str | None = ""
    Type: str | type | typing.Iterable[type | str] | None = None
    DefaultValue: str | None = None

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
    Properties: tuple = ()
    
    @classmethod
    def GetFunctionGroups(cls) -> list[list[FunctionBase]]:
        Functions = []
        for Name, Obj in inspect.getmembers(cls):
            if isinstance(Obj, type) and issubclass(Obj, FunctionBase) and Obj != FunctionBase:
                Functions.append(Obj)
        return [Functions]
