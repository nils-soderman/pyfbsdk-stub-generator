from __future__ import annotations

import typing
import copy

ALWAYS_CREATE_ELLIPSIS = True
TAB_CHARACTER = "\t"


def indent(text: str) -> str:
    lines: list[str] = []
    for line in text.splitlines():
        if line.strip():
            lines.append(TAB_CHARACTER + line)
        else:
            lines.append("")

    return "\n".join(lines)


class StubBase:
    def __init__(self, ref: object, name: str = "") -> None:
        self.ref = ref
        self.name: str = name
        self.docstring = ""
        self.deprecation_message: str | None = None

    def __copy__(self):
        new_instance = self.__class__(self.ref, name=self.name)
        new_instance.docstring = self.docstring
        return new_instance

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.name}>"

    def as_string(self) -> str:
        """
        Get instance as python code (in string format)
        """
        raise NotImplementedError("as_string() has not yet been implemented")

    def get_doc_string(self) -> str:
        if self.docstring:
            # Strip each line of unnecessary whitespace
            lines = self.docstring.split("\n")
            lines = [x.rstrip() for x in lines]
            docstring = "\n".join(lines)

            return f'\"""{docstring.strip()}"""'
        return ""

    def get_requirements(self) -> list:
        """
        Get a list of variable/class names that needs to be declared before the current object
        """
        raise NotImplementedError("get_requirements() has not yet been implemented")

    def get_deprecation_decorator(self):
        msg = self.deprecation_message or ""
        return f'@deprecated("{msg}")\n'


class StubFunction(StubBase):
    def __init__(self, ref: typing.Callable, name: str = "", parameters: list[StubParameter] | None = None, ReturnType: str | None = None):
        super().__init__(ref, name=name)
        self._params: list[StubParameter] = parameters if parameters else []
        self._return_type = ReturnType
        self.is_method = False
        self.is_static = False

    def __copy__(self):
        new_instance = super().__copy__()
        new_instance._params = [copy.copy(x) for x in self._params]
        new_instance._return_type = self._return_type
        new_instance.is_method = self.is_method
        new_instance.is_static = self.is_static
        return new_instance

    @property
    def return_type(self):
        if self._return_type == "object":
            return "Any"
        return self._return_type

    @return_type.setter
    def return_type(self, Value: str | None):
        self._return_type = Value

    def add_parameter(self, stub_parameter: StubParameter):
        self._params.append(stub_parameter)

    def get_parameters(self, exclude_self=False) -> list[StubParameter]:
        """
        Get a list of the parameters

        ### Parameters:
            - exclude_self: If the function is a method, exclude the first parameter (self)
        """
        if exclude_self and self.is_method:
            return self._params[1:]
        return self._params

    def set_parameter(self, Index: int, Parameter: StubParameter):
        if Index > len(self._params) - 1:
            raise IndexError("given parameter index is larger than the size of the parameter array")
        self._params[Index] = Parameter

    def get_requirements(self) -> list:
        return_value = []
        for stub_parameter in self._params:
            return_value += stub_parameter.get_requirements()
        return return_value

    def get_parameters_as_string(self):
        parameters_as_strings: list[str] = []
        for i, stub_parameter in enumerate(self._params):
            if self.is_method and i == 0:
                stub_parameter.name = "self"
                stub_parameter.Type = None
            parameters_as_strings.append(stub_parameter.as_string())

        # Insert a / to indicate that the function only accepts positional parameters
        # Only the function takes more than 1 parameter (excluding self)
        if (not self.is_method and len(self._params) > 0) or len(self._params) > 1:
            parameters_as_strings.append("/")

        return ",".join(parameters_as_strings)

    def as_string(self, is_overload=False):
        function_as_string = ""
        if is_overload:
            function_as_string += "@overload\n"
        if self.is_static:
            function_as_string += "@staticmethod\n"
        if self.deprecation_message is not None:
            function_as_string += self.get_deprecation_decorator()

        function_as_string += f'def {self.name}({self.get_parameters_as_string()})'

        if not (self.name.startswith("__") and self.return_type == "None"):
            function_as_string += f'->{self.return_type}'

        function_as_string += ":"

        docstring = self.get_doc_string()
        if docstring:
            function_as_string += f"\n{indent(docstring)}"
            if ALWAYS_CREATE_ELLIPSIS:
                function_as_string += f"\n{indent('...')}"
        else:
            function_as_string += "..."

        return function_as_string


class StubClass(StubBase):
    def __init__(self, ref: type, name=""):
        super().__init__(ref, name=name)
        self.parents: list[str] = []
        self.stub_properties: list[StubProperty] = []
        self.stub_enums: list[StubClass] = []
        self.stub_functions: list[list[StubFunction]] = []

    def get_functions_by_name(self, name: str) -> list[StubFunction]:
        for function_group in self.stub_functions:
            if function_group[0].name == name:
                return function_group
        return []

    def get_property_by_name(self, name: str):
        for x in self.stub_properties:
            if x.name == name:
                return x

    def add_enum(self, stub_enum: StubClass):
        self.stub_enums.append(stub_enum)

    def add_functions(self, stub_functions: list[StubFunction]):
        for function in stub_functions:
            function.is_method = True  # Make function a method
        self.stub_functions.append(stub_functions)

    def add_property(self, Property: StubProperty):
        self.stub_properties.append(Property)

    def add_parent(self, Parent: str):
        self.parents.append(Parent)

    def get_stub_properties(self) -> list[StubProperty]:
        return self.stub_properties

    def get_requirements(self) -> list:
        # The class parent's needs to be declared before the class
        requirements: list[str] = []
        flat_stub_function_list = [x for FunctionGroup in self.stub_functions for x in FunctionGroup]
        for stub_function in flat_stub_function_list:
            requirements += stub_function.get_requirements()

        return self.parents + requirements

    def as_string(self):
        parent_classes_as_str = ','.join(self.parents)
        if parent_classes_as_str:
            parent_classes_as_str = f"({parent_classes_as_str})"

        class_as_str = f"class {self.name}{parent_classes_as_str}:\n"

        if self.deprecation_message is not None:
            class_as_str = f"{self.get_deprecation_decorator()}{class_as_str}"

        if self.get_doc_string():
            class_as_str += f"{indent(self.get_doc_string())}\n"

        for stub_object in self.stub_enums + self.stub_properties:
            class_as_str += f"{indent(stub_object.as_string())}\n"

        # Always place __init__ at the top, then sort the rest of the functions alphabetically
        sorted_functions = sorted(self.stub_functions, key=lambda x: (x[0].name != '__init__', x[0].name))
        for stub_functions in sorted_functions:
            overload = len(stub_functions) > 1  # If there are multiple functions with the same name, add @overload
            for stub_func in stub_functions:
                class_as_str += f"{indent(stub_func.as_string(overload))}\n"

        # If class doesn't have any members, add a '...'
        if not any((self.stub_properties, self.stub_enums, self.stub_functions)):
            class_as_str += indent("...")

        return class_as_str.strip()


class StubProperty(StubBase):
    def __init__(self, ref: object, name=""):
        super().__init__(ref, name=name)
        self._type = None
        self.setter_type: str | None = None
        self.value: typing.Any = None
        self.read_only: bool = False

    @property
    def Type(self) -> str:
        if self._type == "object":
            return "Any"
        if self._type:
            return self._type
        return "property"

    @Type.setter
    def Type(self, Value):
        self._type = Value

    def as_string(self):
        create_setter = bool(self.setter_type) and self.setter_type != self.Type
        create_getter = self.read_only or create_setter

        is_deprecated = self.deprecation_message is not None
        if is_deprecated:
            create_getter = True
            create_setter = not self.read_only

        if create_getter:
            # If it has a custom setter type, create seperate getter and setter functions
            lines: list[str] = ["@property"]
            if is_deprecated:
                lines.append(self.get_deprecation_decorator().rstrip())
            
            lines.append(f"def {self.name}(self)->{self.Type}:")
            
            if self.get_doc_string():
                lines.append(f"{indent(self.get_doc_string())}")
                lines.append(f"{indent('...')}")
            else:
                lines[-1] += "..."

            if create_setter:
                setter_type = self.setter_type or self.Type
                lines.append(f"@{self.name}.setter")
                if is_deprecated:
                    lines.append(self.get_deprecation_decorator().rstrip())
                lines.append(f"def {self.name}(self, Value: {setter_type}):...")

            property_as_string = "\n".join(lines)
        else:
            property_as_string = self.name

            if self._type or self.value is None:
                property_as_string += f":{self.Type}"

            if self.value is not None:
                property_as_string += f"={self.value}"

            # Add docstring
            if self.get_doc_string():
                property_as_string += "\n"
                property_as_string += self.get_doc_string()

        return property_as_string


class StubParameter(StubBase):
    def __init__(self, ref: object, name="", _type: str | None = "", default_value=None):
        super().__init__(ref, name=name)
        self.default_value = default_value
        self._type = _type

    def __copy__(self):
        new_instance = super().__copy__()
        new_instance.default_value = self.default_value
        new_instance._type = self._type
        new_instance.docstring = self.docstring
        return new_instance

    @property
    def Type(self) -> str | None:
        if self._type == "object":
            return None
        return self._type

    @Type.setter
    def Type(self, Value: str | None):
        self._type = Value

    def get_requirements(self):
        if self.default_value and self.default_value.startswith("FB"):
            requirement_cls: str = self.default_value
            for char in ".(":
                if char in requirement_cls:
                    requirement_cls = requirement_cls.partition(char)[0]

            return [requirement_cls]
        return []

    def as_string(self):
        parameter_as_string = self.name  # PatchParameterName(self.Name)
        # Some parameters have a 0 instead of 'None'
        if self.default_value == "0" and self.Type not in (None, "float", "int"):
            self.default_value = "None"

        if self.Type:
            type_str = self.Type
            if self.default_value == "None":
                type_str = f"{type_str}|None"
            parameter_as_string += f":{type_str}"

        if self.default_value is not None:
            parameter_as_string += f"={self.default_value}"

        return parameter_as_string
