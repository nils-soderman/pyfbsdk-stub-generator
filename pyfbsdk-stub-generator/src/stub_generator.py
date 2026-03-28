from __future__ import annotations

import time

from types import ModuleType
from pathlib import Path

import pyfbsdk

from . import plugins, base_content, native_generator
from .module_types import StubClass
from .flags import GeneratorFlag


DEFAULT_PLUGINS = plugins.GetDefaultPlugins()


# -------------------------------------------------------------
#                       Helper Functions
# -------------------------------------------------------------

def get_motionbuilder_version() -> int:
    """ Get the current version of MotionBuilder """
    return int(2000 + pyfbsdk.FBSystem().Version / 1000)


# -------------------------------------------------------------
#                       Functions
# -------------------------------------------------------------


def sort_classes(classes: list[StubClass]) -> list[StubClass]:
    """ 
    Sort classes based on their parent class
    If a class has another class as their parent class, it'll be placed later in the list
    """
    class_names = [x.Name for x in classes]

    i = 0
    while i < len(classes):
        # Check if class has any required classes that needs to be defined before it (aka. parent classes)
        requirements = classes[i].GetRequirements()
        if requirements:
            # Get the required class that has the highest index in the list
            required_indices = [class_names.index(x) for x in requirements if x in class_names]
            required_max_index = max(required_indices) if required_indices else -1

            # If current index is lower than the highest required index, move current index to be just below the required one.
            if required_max_index > i:
                classes.insert(required_max_index + 1, classes.pop(i))
                class_names.insert(required_max_index + 1, class_names.pop(i))
                i -= 1  # Because we moved current index away, re-iterate over the same index once more.

        i += 1

    return classes


# ---------------------------------------------------------------------------------
#                                  GENERATOR
# ---------------------------------------------------------------------------------


class StubGenerator:
    def __init__(
        self,
        module: ModuleType,
        flags: GeneratorFlag,
        plugins: list[type[plugins.PluginBaseClass]] | None = DEFAULT_PLUGINS
    ):
        self.flags = flags
        self.module = module
        self.version = get_motionbuilder_version()

        self.plugins = plugins or []
        self.plugins.sort(key=lambda x: x.Priority)

    # ---------------------------------------------------
    #                      Internal
    # ---------------------------------------------------

    def generate_string(self) -> str:
        """
        Returns: The stub file as a string
        """
        # Get the content
        enums, classes, function_groups = native_generator.generate_module_stubs(self.module)

        # Run all of the plugins
        for plugin_cls in self.plugins:
            plugin = plugin_cls(self.version, self.module, enums, classes, function_groups, self.flags)
            plugin.Run()

        # Sort classes after all patches are done and we know their requirements
        classes = sort_classes(classes)

        # Generate a string
        stub_content = base_content.get_base_content(self.module)  # Read the custom additions file first
        stub_content += "\n".join([x.GetAsString() for x in enums])
        stub_content += "\n"
        stub_content += "\n".join([x.GetAsString() for x in classes])
        stub_content += "\n"

        for function_group in function_groups:
            overload = len(function_group) > 1  # If there are multiple functions with the same name, add @overload
            stub_content += "\n".join([x.GetAsString(overload) for x in function_group])
            stub_content += "\n"

        stub_content = stub_content.replace("    ", "\t")  # Make sure tabs are used

        stub_content += "\n"

        return stub_content


def generate_stub_file(module: ModuleType, directory_str: str, flags: GeneratorFlag) -> str:
    start_time = time.time()

    generator = StubGenerator(module, flags)
    file_content = generator.generate_string()

    directory = Path(directory_str)

    directory.mkdir(parents=True, exist_ok=True)
    filepath = directory / f"{module.__name__}.pyi"
    filepath.write_text(file_content)

    elapsed_time = time.time() - start_time

    print(f"Generating {module.__name__} stub file took: {round(elapsed_time, 2)}s.")

    return str(filepath)
