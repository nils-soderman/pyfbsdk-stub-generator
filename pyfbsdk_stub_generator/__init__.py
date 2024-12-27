import os

# Make sure code is running in a motionbuilder python interpreter with access to the pyfbsdk module
try:
    import pyfbsdk
except ModuleNotFoundError as e:
    raise ImportError(f"pyfbsdk_stub_generator can only be called upon from within MotionBuilder.") from e

from . import stub_generator

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
            
            with open(SrcFile, "r") as f:
                content = f.read()
                content = stub_generator.ReplaceVariables(content)
                
                with open(DstFile, "w") as f:
                    f.write(content)


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
    

    Filepath = os.path.join(Directory, f"pyfbsdk.{FileExtension}")

    Outfilepath = stub_generator.GeneratePyfbsdkStubFile(Filepath)

    if bCopyAdditionalStubs:
        CopyAdditionalStubs(Directory)

    return Outfilepath
