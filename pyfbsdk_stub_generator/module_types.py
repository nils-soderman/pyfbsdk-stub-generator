from __future__ import annotations

import typing
import copy

ALWAYS_CREATE_ELLIPSIS = True
TAB_CHARACTER = "    "


def Indent(Text: str):
    return TAB_CHARACTER + f"\n{TAB_CHARACTER}".join(Text.split("\n"))


class StubBase():
    def __init__(self, Ref, Name="") -> None:
        self.Ref = Ref
        self.Name: str = Name
        self.DocString = ""

    def __copy__(self):
        NewInstance = self.__class__(self.Ref, Name=self.Name)
        NewInstance.DocString = self.DocString
        return NewInstance

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.Name}>"

    def GetAsString(self) -> str:
        """
        Get instance as python code (in string format)
        """
        raise NotImplementedError("GetAsString() has not yet been implemented")

    def GetDocString(self):
        if self.DocString:
            return f'""\"{self.DocString.strip()}"""'
        return ""

    def GetRequirements(self) -> list:
        """
        Get a list of variable/class names that needs to be declared before the current object
        """
        raise NotImplementedError("GetRequirements() has not yet been implemented")


class StubFunction(StubBase):
    def __init__(self, Ref, Name="", Parameters: list[StubParameter] | None = None, ReturnType: str | None = None):
        super().__init__(Ref, Name=Name)
        self._Params: list[StubParameter] = Parameters if Parameters else []
        self._ReturnType = ReturnType
        self.bIsMethod = False
        self.bIsStatic = False

    def __copy__(self):
        NewInstance = super().__copy__()
        NewInstance._Params = [copy.copy(x) for x in self._Params]
        NewInstance._ReturnType = self._ReturnType
        NewInstance.bIsMethod = self.bIsMethod
        NewInstance.bIsStatic = self.bIsStatic
        return NewInstance

    @property
    def ReturnType(self):
        if self._ReturnType == "object":
            return "Any"
        return self._ReturnType

    @ReturnType.setter
    def ReturnType(self, Value: str | None):
        self._ReturnType = Value

    def AddParameter(self, Parameter):
        self._Params.append(Parameter)

    def GetParameters(self, bExcludeSelf=False) -> list[StubParameter]:
        """
        Get a list of the parameters

        ### Parameters:
            - bExcludeSelf: If the function is a method, exclude the first parameter (self)
        """
        if bExcludeSelf and self.bIsMethod:
            return self._Params[1:]
        return self._Params

    def SetParameter(self, Index, Paramter):
        if Index > len(self._Params) - 1:
            raise IndexError("given parameter index is larger than the size of the paramter array")
        self._Params[Index] = Paramter

    def GetRequirements(self) -> list:
        ReturnValue = []
        for Parameter in self._Params:
            ReturnValue += Parameter.GetRequirements()
        return ReturnValue

    def GetParamsAsString(self):
        ParametersAsStrings = []
        for i, Param in enumerate(self._Params):
            if self.bIsMethod and i == 0:
                Param.Name = "self"
                Param.Type = None
            ParametersAsStrings.append(Param.GetAsString())

        # Insert a / to indicate that the function only accepts positional parameters
        # Only the function takes more than 1 parameter (excluding self)
        if (not self.bIsMethod and len(self._Params) > 0) or len(self._Params) > 1:
            ParametersAsStrings.append("/")

        return ",".join(ParametersAsStrings)

    def GetAsString(self, bIsOverload=False):
        FunctionAsString = ""
        if bIsOverload:
            FunctionAsString += "@overload\n"
        elif self.bIsStatic:
            FunctionAsString += "@staticmethod\n"

        FunctionAsString += f'def {self.Name}({self.GetParamsAsString()})'

        if self.ReturnType and self.ReturnType != "None":
            FunctionAsString += f'->{self.ReturnType}'

        FunctionAsString += ":"

        DocString = self.GetDocString()
        if DocString:
            FunctionAsString += f"\n{Indent(DocString)}"
            if ALWAYS_CREATE_ELLIPSIS:
                FunctionAsString += f"\n{Indent('...')}"
        else:
            FunctionAsString += "..."

        return FunctionAsString


class StubClass(StubBase):
    def __init__(self, Ref, Name=""):
        super().__init__(Ref, Name=Name)
        self.Parents: list[str] = []
        self.StubProperties: list[StubProperty] = []
        self.StubEnums: list[StubClass] = []
        self.StubFunctions: list[list[StubFunction]] = []

    def GetFunctionsByName(self, Name: str) -> list[StubFunction]:
        for FunctionGroup in self.StubFunctions:
            if FunctionGroup[0].Name == Name:
                return FunctionGroup
        return []

    def GetPropertyByName(self, Name: str):
        for x in self.StubProperties:
            if x.Name == Name:
                return x

    def AddEnum(self, Enum: StubClass):
        self.StubEnums.append(Enum)

    def AddFunctions(self, Functions: list[StubFunction]):
        for Function in Functions:
            Function.bIsMethod = True  # Make function a method
        self.StubFunctions.append(Functions)

    def AddProperty(self, Property: StubProperty):
        self.StubProperties.append(Property)

    def AddParent(self, Parent: str):
        self.Parents.append(Parent)

    def GetStubProperties(self) -> list[StubProperty]:
        return self.StubProperties

    def GetRequirements(self) -> list:
        # The class parent's needs to be declared before the class
        FunctionRequirements = []
        FlatFunctionList = [x for FunctionGroup in self.StubFunctions for x in FunctionGroup]
        for Function in FlatFunctionList:
            FunctionRequirements += Function.GetRequirements()
        return self.Parents + FunctionRequirements

    def GetAsString(self):
        ParentClassesAsString = ','.join(self.Parents)

        ClassAsString = f"class {self.Name}({ParentClassesAsString}):\n"

        if self.GetDocString():
            ClassAsString += f"{Indent(self.GetDocString())}\n"

        for StubObject in self.StubEnums + self.StubProperties:
            ClassAsString += f"{Indent(StubObject.GetAsString())}\n"

        for StubFunctions in self.StubFunctions:
            bOverload = len(StubFunctions) > 1  # If there are multiple functions with the same name, add @overload
            for StubFunc in StubFunctions:
                ClassAsString += f"{Indent(StubFunc.GetAsString(bOverload))}\n"

        # If class doesn't have any members, add a '...'
        if not any((self.StubProperties, self.StubEnums, self.StubFunctions)):
            ClassAsString += Indent("...")

        return ClassAsString.strip()


class StubProperty(StubBase):
    def __init__(self, Ref, Name=""):
        super().__init__(Ref, Name=Name)
        self._Type = None
        self.SetterType: str | None = None
        self.Value: typing.Any = None

    @property
    def Type(self) -> str:
        if self._Type == "object":
            return "Any"
        if self._Type:
            return self._Type
        return "property"

    @Type.setter
    def Type(self, Value):
        self._Type = Value

    def GetAsString(self):
        if self.SetterType and self.SetterType != self.Type:
            # If it has a custom setter type, create seperate getter and setter functions
            Lines = ["@property"]
            Lines.append(f"def {self.Name}(self)->{self.Type}:")
            if self.GetDocString():
                Lines.append(f"{Indent(self.GetDocString())}")
                Lines.append(f"{Indent('...')}")
            else:
                Lines[-1] += "..."
            Lines.append(f"@{self.Name}.setter")
            Lines.append(f"def {self.Name}(self, Value: {self.SetterType}):...")

            PropertyAsString = "\n".join(Lines)
        else:
            PropertyAsString = self.Name

            if self._Type or self.Value is None:
                PropertyAsString += f":{self.Type}"

            if self.Value is not None:
                PropertyAsString += f"={self.Value}"

            # Add docstring
            if self.GetDocString():
                PropertyAsString += "\n"
                PropertyAsString += self.GetDocString()

        return PropertyAsString


class StubParameter(StubBase):
    def __init__(self, Ref, Name="", Type: str | None = "", DefaultValue=None):
        super().__init__(Ref, Name=Name)
        self.DefaultValue = DefaultValue
        self._Type = Type

    def __copy__(self):
        NewInstance = super().__copy__()
        NewInstance.DefaultValue = self.DefaultValue
        NewInstance._Type = self._Type
        NewInstance.DocString = self.DocString
        return NewInstance

    @property
    def Type(self) -> str | None:
        if self._Type == "object":
            return None
        return self._Type

    @Type.setter
    def Type(self, Value: str | None):
        self._Type = Value

    def GetRequirements(self):
        if self.DefaultValue and self.DefaultValue.startswith("FB"):
            RequirementClass: str = self.DefaultValue
            for Char in ".(":
                if Char in RequirementClass:
                    RequirementClass = RequirementClass.partition(Char)[0]

            return [RequirementClass]
        return []

    def GetAsString(self):
        ParamString = self.Name  # PatchParameterName(self.Name)
        # Some parameters have a 0 instead of 'None'
        if self.DefaultValue == "0" and self.Type not in (None, "float", "int"):
            self.DefaultValue = "None"

        if self.Type:
            TypeStr = self.Type
            if self.DefaultValue == "None":
                TypeStr = f"{TypeStr}|None"
            ParamString += f":{TypeStr}"

        if self.DefaultValue is not None:
            ParamString += f"={self.DefaultValue}"

        return ParamString
