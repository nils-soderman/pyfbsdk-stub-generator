import os

from types import ModuleType

import pyfbsdk

from .flags import GeneratorFlag


def generate(directory: str, modules: list[ModuleType] | None = None, copy_additional_stubs = True, flags = GeneratorFlag.NONE) -> list[str]:
    """
    Generate a stub file for the pyfbsdk module. \\
    This may take a while since the online MoBu sdk documentation will have to be parsed.

    ## Parameters:
        - directory: The absolute path to the directory where the pyfbsdk stub file should be created
        - file_extension: The file extension
        - copy_additional_stubs: If True, additional manually typed stubs will be copied to the output directory. These include e.g. callbackframework.pyi, pyfbsdk_additions.pyi, etc.

    ## Returns:
    The filepath to the generated file 
    """
    from . import stub_generator, manual_stubs

    if modules is None:
        import pyfbusd
        modules = [pyfbsdk, pyfbusd]

    out_files: list[str] = []
    for module in modules:
        out_files.append(stub_generator.generate_stub_file(module, directory, flags))

    if copy_additional_stubs:
        manual_stubs.copy_manual_stubs(directory)

    return out_files
