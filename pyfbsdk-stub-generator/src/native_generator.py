from __future__ import annotations

import inspect
import typing
import types
import enum

from types import ModuleType

from .module_types import StubClass, StubFunction, StubParameter, StubProperty

import pyfbsdk as fb


ENUMERATION_NAME = "Enumeration"
ALLOWED_BUILTIN_OVERRIDES = {"__gt__", "__lt__", "__ge__", "__le__"}
ALLOWED_CLASS_OVERRIDES = [
    fb.FBEvent.Type,
]


class EObjectType(enum.StrEnum):
    FUNCTION = 'function'
    CLASS = 'class'
    PROPERTY = 'property'
    ENUM = 'type'


# -------------------------------------------------------------
#                       Helper Functions
# -------------------------------------------------------------

def get_object_name(obj: type) -> str:
    return obj.__name__


def get_object_type(obj: type) -> str:
    """ Get object type as a string """
    return get_object_name(type(obj))


def is_private(obj: type) -> bool:
    """ Check if the name of an object begins with a underscore """
    return get_object_name(obj).startswith("_")


def is_method_static(cls: type, method_name: str) -> bool:
    """ 
    Check if a method is static
    Args:
        - cls: reference to the class
        - method_name: Name of the method
    """
    return isinstance(inspect.getattr_static(cls, method_name), staticmethod)


def get_class_parents(cls: type):
    return cls.__bases__


def get_unique_class_members(cls: type, ignore: tuple[str, ...] = (), allowed_overrides: tuple[str, ...] = ()):
    members = inspect.getmembers(cls)
    parent_cls = get_class_parents(cls)[0]

    unique_members = []
    for name, ref in members:
        if name in ignore:
            continue

        if hasattr(parent_cls, name):
            if parent_cls.__name__ == "instance":
                if isinstance(ref, (types.BuiltinFunctionType, types.BuiltinMethodType)) and name in ALLOWED_BUILTIN_OVERRIDES:
                    unique_members.append((name, ref))
                    continue

            if name not in allowed_overrides and getattr(parent_cls, name) not in ALLOWED_CLASS_OVERRIDES:
                continue

        unique_members.append((name, ref))

    return unique_members


def get_class_parent_names(cls: type) -> list[str]:
    parent_names: list[str] = []

    for parent_cls in get_class_parents(cls):
        parent_name = parent_cls.__name__
        if parent_name == "instance":
            continue

        elif parent_name == "enum":
            parent_name = ENUMERATION_NAME

        parent_names.append(parent_name)

    return parent_names


def get_function_info_from_doc_string(function: typing.Callable) -> list[tuple[list[StubParameter], str]]:
    """
    Get Parameters & Return type from the docstring, can return multiple results if overload functions exists.

    Returns: a list of tuple([Parameters], ReturnType)
    """
    if not function.__doc__:  # Return an empty list if the function has no docstring
        return []

    def _generate_parameters(param_str: str, default_value = None) -> list[StubParameter]:
        """ 
        Parse a param string that looks something like this:
        "(FBVector4d)arg1, (FBVector4d)arg2, (FBVector4d)arg3"
        and generate StubParameter instances from it
        """
        params: list[StubParameter] = []
        for param in param_str.split(","):
            # Param will now look something like this: '(str)arg1'
            param_type, _, param_name = param.strip().partition(")")
            parameter_instance = StubParameter(function, param_name, param_type[1:], default_value = default_value)
            params.append(parameter_instance)

        return params

    parameters = []

    # Read the docstring and split it up if there are multiple function overrides
    function_docs = [x for x in function.__doc__.split("\n") if x]
    for docstring in function_docs:
        # Make sure `docstring` now follows this format: "FunctionName( (str)arg1 [, (object)arg2]) -> object"
        if not docstring.strip().startswith(function.__name__) or not all(x in docstring for x in ["->", "(", ")"]):
            continue

        # 'docstring' will now look something like this:
        # ShowToolByName( (str)arg1 [, (object)arg2]) -> object
        docstring = docstring.partition("(")[2]  # Remove function name
        params, _, return_type = docstring.rpartition("->")

        return_type = return_type.strip(" :")

        # Split params into required & optional
        params = params.rpartition(")")[0]
        required_params, _, optional_params = params.partition("[")
        optional_params = optional_params.replace("[", "").replace("]", "").lstrip(',')

        params = []
        if required_params.strip():
            params += _generate_parameters(required_params)
        if optional_params.strip():
            params += _generate_parameters(optional_params, default_value = "None")

        parameters.append(
            (params, return_type.strip())
        )

    return parameters


# -------------------------------------------------------------
#                     Generator Functions
# -------------------------------------------------------------


def generate_enum_instance(cls: type, parent_cls = None):
    """
    Generate a StubClass instance from a class (enum) reference

    Args:
        - Class: reference to the class
        - ParentClass: If this class is a subclass, the parent class should be passed along
    """
    # Create the stub instance
    cls_name = get_object_name(cls)
    stub_enum = StubClass(cls, cls_name)

    # Get all members and generate stub properties of them
    cls_members = get_unique_class_members(cls, ignore = ("__init__", "__slots__", "names", "values"))

    for name, ref in cls_members:
        stub_property = StubProperty(ref, name)
        if parent_cls:
            stub_property.Type = f"{get_object_name(parent_cls)}.{cls_name}"
        else:
            stub_property.Type = cls_name

        stub_enum.add_property(stub_property)

    stub_enum.add_parent(ENUMERATION_NAME)

    return stub_enum


def generate_class_instance(cls: type) -> StubClass:
    """
    Generate a StubClass instance from a class reference

    Args:
        - Class {class}: reference to the class
    """
    # Create the stub instance
    cls_name = get_object_name(cls)
    stub_class = StubClass(cls, cls_name)

    # Get all members and generate stub properties of them
    cls_members = get_unique_class_members(cls,
                                           ignore = ("__instance_size__",),
                                           allowed_overrides = ("__init__",
                                                                "__getitem__",
                                                                "__contains__",
                                                                "Data",
                                                                "remove",
                                                                "pop",
                                                                "insert",
                                                                "append",
                                                                "count")
                                           )

    cls_member_names = [x for x, y in cls_members]

    for member_name, member_reference in cls_members:
        type_str = get_object_type(member_reference)

        if type_str == EObjectType.FUNCTION:
            methods: list[StubFunction] = []
            for stub_methods in generate_function_instances(member_reference):
                stub_methods.is_static = is_method_static(cls, member_name)
                methods.append(stub_methods)
            
            stub_class.add_functions(methods)

        elif type_str == EObjectType.ENUM:
            stub_enum = generate_enum_instance(member_reference, parent_cls = cls)
            stub_class.add_enum(stub_enum)

        elif member_name not in ["__init__"]:
            stub_property = StubProperty(member_reference, member_name)
            if type_str in cls_member_names:
                stub_property.Type = f"{cls_name}.{type_str}"
            else:
                stub_property.Type = type_str

            stub_class.add_property(stub_property)

    # Set the parent classes
    for parent_name in get_class_parent_names(cls):
        stub_class.add_parent(parent_name)

    return stub_class


def generate_function_instances(function: type) -> list[StubFunction]:
    """
    Generate StubFunction instances from a function reference.

    Args:
        - function: reference to the function

    Returns: A list of function instances, can be multiple if it has overload versions
    """
    name = get_object_name(function)

    stub_functions: list[StubFunction] = []

    # Get param & returntype info from the docstring
    function_info = get_function_info_from_doc_string(function)
    for stub_parameter, return_type in function_info:
        stub_functions.append(StubFunction(function, name, stub_parameter, return_type))

    return stub_functions


# -------------------------------------------------------------
#                     Main Generator Class
# -------------------------------------------------------------

class RawModuleContent(typing.NamedTuple):
    enums: list[type]
    classes: list[type]
    functions: list[type]


class ModuleStubs(typing.NamedTuple):
    enums: list[StubClass]
    classes: list[StubClass]
    function_groups: list[list[StubFunction]]


def get_module_content(module: ModuleType) -> RawModuleContent:
    """
    Get all members in the given module
    returns: a ModuleContent named tuple with (functions, classes, enums)
    """
    members = inspect.getmembers(module)
    functions = [x[1] for x in members if get_object_type(x[1]) == EObjectType.FUNCTION and not is_private(x[1])]
    classes = [x[1] for x in members if get_object_type(x[1]) == EObjectType.CLASS]
    enums = [x[1] for x in members if get_object_type(x[1]) == EObjectType.ENUM]

    return RawModuleContent(enums=enums, classes=classes, functions=functions)


def generate_module_stubs(module: ModuleType) -> ModuleStubs:
    content = get_module_content(module)

    enum_stubs = [generate_enum_instance(x) for x in content.enums]
    class_stubs = [generate_class_instance(x) for x in content.classes]
    function_stubs = [generate_function_instances(x) for x in content.functions]

    return ModuleStubs(enums=enum_stubs, classes=class_stubs, function_groups=function_stubs)
