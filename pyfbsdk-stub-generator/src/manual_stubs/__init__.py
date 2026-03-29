import pyfbsdk

import os


def get_motionbuilder_version() -> int:
    """ Get the current version of MotionBuilder """
    return int(2000 + pyfbsdk.FBSystem().Version / 1000)


def copy_manual_stubs(out_directory: str):
    """
    Copy the additional stubs to the output directory.
    This includes e.g. callbackframework.pyi, pyfbsdk_additions.pyi, etc.

    These stubs have been manually created and are not automatically generated, and may therefore be outdated.

    ## Parameters:
        - out_directory: The directory where the additional stubs should be copied    
    """
    os.makedirs(out_directory, exist_ok=True)

    for filename in os.listdir(os.path.dirname(__file__)):
        if filename.endswith(".pyi"):
            src_file = os.path.join(os.path.dirname(__file__), filename)
            dst_file = os.path.join(out_directory, filename)

            with open(src_file, "r") as f:
                content = f.read()
                content = content.replace("{MOTIONBUILDER_VERSION}", str(get_motionbuilder_version()))

                with open(dst_file, "w") as f:
                    f.write(content)
