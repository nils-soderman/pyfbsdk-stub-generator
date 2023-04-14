from __future__ import annotations

from dataclasses import dataclass

@dataclass
class Argument:
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
    
class Function:
    Arguments: tuple[Argument] = ()
    ReturnType: str | None | type = None
    
    def GetReturnTypeString(self) -> str | None:
        if self.ReturnType is None:
            return None

        if isinstance(self.ReturnType, str):
            return self.ReturnType

        return self.ReturnType.__name__