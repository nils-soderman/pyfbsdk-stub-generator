from .flags import GeneratorFlag

import os


def Generate(Directory: str, FileExtension = "pyi", bCopyAdditionalStubs = True, flags = GeneratorFlag.NONE) -> str:
    """ 
    Generate a stub file for the pyfbsdk module. \\
    This may take a while since the online MoBu sdk documentation will have to be parsed.

    ## Parameters:
        - Directory: The absolute path to the directory where the pyfbsdk stub file should be created
        - FileExtension: The file extension
        - bCopyAdditionalStubs: If True, additional manually typed stubs will be copied to the output directory. These include e.g. callbackframework.pyi, pyfbsdk_additions.pyi, etc.

    ## Returns:
    The filepath to the generated file 
    """
    from . import stub_generator, manual_stubs

    Filepath = os.path.join(Directory, f"pyfbsdk.{FileExtension}")

    Outfilepath = stub_generator.GeneratePyfbsdkStubFile(Filepath, flags)

    if bCopyAdditionalStubs:
        manual_stubs.CopyManualStubs(Directory)

    return Outfilepath
