import pyfbsdk

import os


def GetMotionBuilderVersion() -> int:
    """ Get the current version of MotionBuilder """
    return int(2000 + pyfbsdk.FBSystem().Version / 1000)


def CopyManualStubs(OutDirectory: str):
    """
    Copy the additional stubs to the output directory.
    This includes e.g. callbackframework.pyi, pyfbsdk_additions.pyi, etc.

    These stubs have been manually created and are not automatically generated, and may therefore be outdated.

    ## Parameters:
        - OutDirectory: The directory where the additional stubs should be copied    
    """
    os.makedirs(OutDirectory, exist_ok=True)

    for File in os.listdir(os.path.dirname(__file__)):
        if File.endswith(".pyi"):
            SrcFile = os.path.join(os.path.dirname(__file__), File)
            DstFile = os.path.join(OutDirectory, File)

            with open(SrcFile, "r") as f:
                content = f.read()
                content = content.replace("{MOTIONBUILDER_VERSION}", str(GetMotionBuilderVersion()))

                with open(DstFile, "w") as f:
                    f.write(content)
