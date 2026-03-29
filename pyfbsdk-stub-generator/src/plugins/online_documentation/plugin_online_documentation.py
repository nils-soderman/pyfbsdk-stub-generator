from __future__ import annotations

from types import ModuleType
from typing import TypeGuard

from ..plugin_base import PluginBaseClass
from ...module_types import StubClass, StubFunction, StubParameter, StubProperty
from ...flags import GeneratorFlag

from .documentation_scraper import Documentation, MemberItem, get_parameter_nice_name


EVENT_SOURCE_TYPE = "callbackframework.FBEventSource"

TYPE_IGNORE_PREFIXES = (
    "unsigned",
    "K_DEPRECATED"
)

TRANSLATION_TYPE = {
    "double": "float",
    "long": "int",
    "kInt64": "int",
    "kULong": "int",
    "char": "str",

    "kReference": "int",
    "FBkReference": "int",

    "FBAudioFmt": "int",
    "FBBool": "bool",

    "FBArrayDouble": "list[float]",
    "FBArrayUInt": "list[int]",

    "FBVector4[float]": "FBVector4d",
    "FBTVector": "FBVector4d",
    "FBQuaternion": "FBVector4d",
    "FBRVector": "FBVector3d",
    "FBColorF": "FBColor",

    # These are a bit more spesific, and may need to be changed in the future
    "AreaLightShapes": "FBLight.EAreaLightShapes",
    "KeyBehavior": "FBModelPath3D.EKeyPropertyBehavior",
    "UnitType": "FBModelPath3D.ELengthUnitType",
    "Element": "object",

    # These are unknown, revert them back to properties
    "FBEventTreeWhy": "property",
}

TRANSLATION_DEFAULT_VALUES = {
    "nullptr": "None",
    "true": "True",
    "false": "False",
}


class PluginOnlineDocumentation(PluginBaseClass):
    THREADING = True
    PRIORITY = 10  # We preferably want this to run directly after the native generator

    def __init__(self,
                 version: int,
                 module: ModuleType,
                 stub_enums: list[StubClass],
                 stub_classes: list[StubClass],
                 stub_functions: list[list[StubFunction]],
                 flags: GeneratorFlag):
        super().__init__(version, module, stub_enums, stub_classes, stub_functions, flags)

        # Initialize the documentation
        self.documentation = Documentation(module.__name__, version, self.flags & GeneratorFlag.CACHE != 0)
        if not self.documentation:
            return

        # Parse the first documentation page to get the list of all pages
        for function_group in stub_functions:
            Function = function_group[0]
            self.function_page = self.documentation.parse_page(Function.name)
            if self.function_page:
                break

        # Make a map of all class names and their class object that can be used for patching types etc.
        self.all_classes_map = {x.name: x for x in stub_classes + stub_enums}

    def should_patch(self) -> bool:
        return bool(self.documentation)

    # ---------------------------------------------------------------------------------------------
    #                                 Patch Entry Methods
    # ---------------------------------------------------------------------------------------------

    def patch_enum(self, stub_enum: StubClass):
        parsed_page = self.documentation.parse_page(stub_enum.name)
        if not parsed_page:
            return

        stub_enum.docstring = parsed_page.description

        for stub_property in stub_enum.stub_properties:
            if member := parsed_page.find_member_by_name(stub_property.name):
                stub_property.docstring = member.doc_string

    def patch_class(self, stub_class: StubClass):
        parsed_page = self.documentation.parse_page(stub_class.name)
        if not parsed_page:
            return

        stub_class.docstring = parsed_page.description

        # Properties
        for stub_property in stub_class.stub_properties:
            if member := parsed_page.find_member_by_name(stub_property.name):
                stub_property.docstring = member.doc_string
                stub_property.Type = self.ensure_valid_type_property(stub_property, member.type_str)

        # Methods
        for stub_functions in stub_class.stub_functions:
            function_name = stub_functions[0].name

            # In the documentation, the constructor is called the same as the stub_class
            if function_name == "__init__":
                function_name = stub_class.name

            if members := parsed_page.find_members_by_name(function_name):
                self._patch_function_groups_from_doc(stub_functions, members, stub_class)

    def patch_function_group(self, function_group: list[StubFunction]):
        if not function_group:
            return  # TODO: This should never happen, look into it

        if self.function_page:
            name = function_group[0].name
            if members := self.function_page.find_members_by_name(name):
                self._patch_function_groups_from_doc(function_group, members)

    # ---------------------------------------------------------------------------------------------
    #                                    Patch Functions
    # ---------------------------------------------------------------------------------------------

    def _patch_function_groups_from_doc(self,
                                        stub_functions: list[StubFunction],
                                        doc_member: list[MemberItem],
                                        parent_stub_class: StubClass | None = None):
        # If we only have one function and one member, we don't need to do any matching, we can just patch them directly
        if len(stub_functions) == 1 and len(doc_member) == 1:
            self.patch_function_from_doc(stub_functions[0], doc_member[0], parent_stub_class)
            return

        # If we have multiple functions and multiple members, we need to figure out which ones to match
        # This happens when functions are overloaded

        # Make copies of the lists so we can modify them without affecting the original lists
        FunctionsCopy = stub_functions.copy()
        MembersCopy = doc_member.copy()

        # Find all of the functions that has a perfect match with a member, by the parameter types
        perfect_matches: list[tuple[StubFunction, MemberItem]] = []
        matched_functions: list[StubFunction] = []
        matched_members: list[MemberItem] = []
        for stub_function in FunctionsCopy:
            stub_parameters = stub_function.get_parameters(exclude_self = True)

            for member in MembersCopy:
                if len(stub_parameters) != len(member.parameters):
                    continue

                for stub_param, doc_param in zip(stub_parameters, member.parameters):
                    if stub_param.Type != doc_param.type_str:
                        break
                else:
                    # Make sure neither the function or the member has already been matched with another function or member
                    if stub_function in matched_functions or member in matched_members:
                        continue

                    perfect_matches.append((stub_function, member))

                    matched_functions.append(stub_function)
                    matched_members.append(member)

        for stub_function, member in perfect_matches:
            self.patch_function_from_doc(stub_function, member, parent_stub_class)

            # Remove them from the lists so we don't try to match them again
            FunctionsCopy.remove(stub_function)
            MembersCopy.remove(member)

        # TODO: Match based on most similar parameter types
        Scores: list[tuple[StubFunction, MemberItem, int]] = []
        for stub_function in FunctionsCopy:
            stub_parameters = stub_function.get_parameters(exclude_self = True)
            for member in MembersCopy:
                Score = 0
                if len(stub_parameters) == len(member.parameters):
                    Score += 1

                for stub_param, doc_param in zip(stub_parameters, member.parameters):
                    MemberParameterType = self.ensure_valid_type(doc_param.type_str)
                    if not MemberParameterType or not stub_param.Type:
                        continue
                    if stub_param.Type == MemberParameterType:
                        Score += 1
                    elif MemberParameterType.startswith("list") and stub_param.Type == "list":
                        Score += 1
                    elif is_type_defined(stub_param.Type):
                        # Member description is not compatible with current function
                        Score = -1
                        break

                if Score > 0:
                    Scores.append((stub_function, member, Score))

        # Sort the scores from highest to lowest
        Scores.sort(key = lambda Score: Score[2], reverse = True)
        while Scores:
            stub_function, member, Score = Scores.pop(0)
            if stub_function in matched_functions or member in matched_members:
                continue

            self.patch_function_from_doc(stub_function, member, parent_stub_class)

            matched_members.append(member)
            matched_functions.append(stub_function)

            # Remove them from the lists so we don't try to match them again
            FunctionsCopy.remove(stub_function)
            MembersCopy.remove(member)

    def patch_function_from_doc(self, stub_function: StubFunction, doc_function: MemberItem, parent_stub_class: StubClass | None = None):
        stub_function.docstring = doc_function.doc_string
        if stub_function.name == "__init__":
            if stub_function.docstring.startswith("Constructor."):
                stub_function.docstring = stub_function.docstring.replace("Constructor.", "", 1)

        if self.should_patch_type(stub_function.return_type, doc_function.type_str):
            if new_type := self.ensure_valid_type(doc_function.type_str):
                stub_function.return_type = new_type

        FunctionParameters = stub_function.get_parameters(exclude_self = True)
        DocumentationParameters = doc_function.parameters

        # The documentation includes an additional empty parameter for functions directly in the module
        if not stub_function.is_method and len(DocumentationParameters) - 1 == len(FunctionParameters):
            DocumentationParameters = DocumentationParameters[:-1]

        if not FunctionParameters:
            return  # If there are no parameters, we don't need to do anything else

        # Function that has different number of parameters than the documentation requires a more careful patch to avoid patching the wrong parameter
        # It's better to not patch the parameters than patching it incorrectly, which could cause a lot of confusion
        safe_to_patch = len(FunctionParameters) != len(DocumentationParameters)

        for stub_parameters, doc_parameters in zip(FunctionParameters, DocumentationParameters):
            if safe_to_patch:
                # Variable Types must match when doing a safe patch, otherwise we might be patching the wrong parameter
                if stub_parameters.Type != doc_parameters.type_str:
                    continue

            # Name
            if doc_parameters.name and stub_parameters.name.startswith("arg"):
                stub_parameters.name = get_parameter_nice_name(doc_parameters.name)

            # Type
            self.patch_stub_parameter(stub_parameters, doc_parameters.type_str, parent_stub_class)

            # Default value
            self.patch_default_value(stub_parameters, doc_parameters.default_value)

    # ---------------------------------------------------------------------------------------------
    #                                    Validate Types
    # ---------------------------------------------------------------------------------------------

    def patch_stub_parameter(self, stub_parameter: StubParameter, new_type: str | None, parent_class: StubClass | None = None):
        if new_type is None or not self.should_patch_type(stub_parameter.Type, new_type):
            return

        stub_parameter.Type = self.ensure_valid_type(new_type)

    def ensure_valid_type_property(self, stub_property: StubProperty, new_type: str) -> str | None:
        """
        Make sure the type is valid for the given property
        """
        # If it's a class, make sure it's a valid class
        is_valid_fb_class = new_type in self.all_classes_map
        if not is_valid_fb_class:
            if new_type.startswith("FB"):
                # In the documentation the "Property" part might be missing from the class name
                fixed_type = f"FBProperty{new_type[2:]}"
                if fixed_type in self.all_classes_map:
                    new_type = fixed_type

        # Convert all Events to EventSource
        # The documentation says otherwise, but is wrong.
        if (
            new_type.startswith("FBEvent")
            or
            (
                stub_property.name.startswith("On") and
                stub_property.name.endswith("Event")
            )
            or
            (not is_valid_fb_class and new_type.startswith("FBEvent"))
        ):
            if new_type != "FBEventName":
                new_type = EVENT_SOURCE_TYPE

        return self.ensure_valid_type(new_type)

    def patch_default_value(self, stub_parameter: StubParameter, default_value: str | None):
        if stub_parameter.default_value is None or default_value is None:
            return

        # Replace namespace C++ syntax with Python
        if "::" in default_value:
            default_value = default_value.replace("::", ".")

        default_value = TRANSLATION_DEFAULT_VALUES.get(default_value, default_value)

        # Remove the "f" suffix from float literals, e.g. '1.0f' -> '1.0'
        if default_value.endswith("f") and default_value[:-1].replace(".", "").isnumeric():
            default_value = default_value[:-1]

        if default_value.startswith("FBArrayTemplate"):
            default_value = "[]"
        elif default_value == "FBString()":
            default_value = '""'

        if default_value.startswith(("FB", "k")) and default_value not in self.all_classes_map:
            if stub_parameter.Type:
                stub_enums = self.all_classes_map.get(stub_parameter.Type)
                if stub_enums:
                    if any(x.name for x in stub_enums.stub_properties if x.name == default_value):
                        default_value = f"{stub_enums.name}.{default_value}"

        stub_parameter.default_value = default_value

    def should_patch_type(self, current_type: str | None, new_type: str | None) -> bool:
        """
        Check if we want to patch the current type with the new type from the documentation.

        If type has alredy been defined from the native parsing, we should trust that over the documentation.
        """
        if not is_type_defined(current_type):
            return True  # If the current type is not defined, we should use the type from documentation

        validated_type = self.ensure_valid_type(new_type)
        if not validated_type:
            return False

        if current_type == "list" and validated_type.startswith("list"):
            return True
        if current_type == "tuple" and validated_type.startswith("tuple"):
            return True

        if current_type.startswith(("E", "FB")) and current_type not in self.all_classes_map:
            return True

        return False

    def ensure_valid_type(self, _type: str | None) -> str | None:
        """
        Make sure type is a valid Python type that can be used in the stubs, and translate it if necessary.
        """
        if not _type:
            return None

        if "<" in _type:
            _type = _type.replace("<", "[").replace(">", "]").replace(" ", "")
            _type = _type.replace("FBArrayTemplate", "list")

            # Get content between brackets
            list_types_str = _type[_type.find("[") + 1:_type.find("]")]
            if list_types_str:
                validated_types: list[str] = []
                list_types = list_types_str.split(",")
                for list_type in list_types:
                    list_type = self.ensure_valid_type(list_type)
                    if list_type:
                        validated_types.append(list_type)

                if len(list_types) != len(validated_types):
                    return None

                _type = _type.replace(list_types_str, ",".join(validated_types))
                if _type.endswith("[]"):
                    _type = _type[:-2]

        if " " in _type:
            for prefix in TYPE_IGNORE_PREFIXES:
                if _type.startswith(prefix):
                    _type = _type.rpartition(" ")[2]

        _type = TRANSLATION_TYPE.get(_type, _type)

        # Replace namespace C++ syntax with Python
        if "::" in _type:
            _type = _type.replace("::", ".")

        if _type.startswith("FB"):
            class_name = _type
            if "." in _type:
                class_name = _type.partition(".")[0]
            if class_name not in self.all_classes_map:
                # print(f"Type not found: {Type}")
                return None

        return _type


def is_type_defined(_type: str | None) -> TypeGuard[str]:
    if not _type:
        return False

    return _type != "object" and _type != "Any"
