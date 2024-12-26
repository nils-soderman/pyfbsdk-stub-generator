import shutil
import os


def CopyAdditionalStubs(OutDirectory: str):
    """
    Copy the additional stubs to the output directory.
    This includes e.g. callbackframework.pyi, pyfbsdk_additions.pyi, etc.
    
    These stubs have been manually created and are not automatically generated, and may therefore be outdated.
    
    ## Parameters:
        - OutDirectory: The directory where the additional stubs should be copied    
    """
    ManualStubsDirectory = os.path.join(os.path.dirname(__file__), "manual_stubs")
    for File in os.listdir(ManualStubsDirectory):
        if File.endswith(".pyi"):
            SrcFile = os.path.join(ManualStubsDirectory, File)
            DstFile = os.path.join(OutDirectory, File)
            shutil.copy(SrcFile, DstFile)


def Generate(Directory: str, FileExtension = "pyi", bCopyAdditionalStubs = True):
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
    # Make sure code is running in a motionbuilder python interpreter with access to the pyfbsdk module
    try:
        import pyfbsdk
    except ModuleNotFoundError as e:
        raise ImportError(f"{Generate.__name__} can only be called upon from within MotionBuilder.") from e

    from .stub_generator import GeneratePyfbsdkStubFile

    Filepath = os.path.join(Directory, f"pyfbsdk.{FileExtension}")

    Outfilepath = GeneratePyfbsdkStubFile(Filepath)

    if bCopyAdditionalStubs:
        CopyAdditionalStubs(Directory)

    return Outfilepath
