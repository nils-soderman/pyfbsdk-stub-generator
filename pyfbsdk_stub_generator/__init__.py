import os


def Generate(Directory: str, FileExtension = "pyi") -> str:
    """ 
    Generate a stub file for the pyfbsdk module. \\
    This may take a while since the online MoBu sdk documentation will have to be parsed.

    ## Parameters:
        - directory: The absolute path to the directory where the pyfbsdk stub file should be created
        - fileExtension: The file extension

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

    return GeneratePyfbsdkStubFile(Filepath)
