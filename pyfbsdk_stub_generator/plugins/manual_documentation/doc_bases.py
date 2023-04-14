from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ParameterBase:
    Name: str
    Type: str | type
    DefaultValue: str | None = None

    def GetTypeString(self) -> str:
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
    Parameters: tuple[ParameterBase] = ()
    ReturnType: str | None | type = None

    @classmethod
    def GetReturnTypeString(cls) -> str | None:
        if cls.ReturnType is None:
            return None

        if isinstance(cls.ReturnType, str):
            return cls.ReturnType

        return cls.ReturnType.__name__


class ClassBase:
    Functions: tuple[FunctionBase] = ()
    Properties: tuple = ()
