from types import ModuleType
from pathlib import Path

import pyfbsdk

# -------------------------------------------------------------
#                       Helper Functions
# -------------------------------------------------------------

def get_motionbuilder_version() -> int:
    """ Get the current version of MotionBuilder """
    return int(2000 + pyfbsdk.FBSystem().Version / 1000)


# -------------------------------------------------------------
#                       Functions
# -------------------------------------------------------------

def replace_docstring_variables(string: str) -> str:
    """
    Insert variables into the string, e.g. {MOTIONBUILDER_VERSION}
    """
    string = string.replace("{MOTIONBUILDER_VERSION}", str(get_motionbuilder_version()))

    return string


def get_base_content(module: ModuleType) -> str:
    filepath = Path(__file__).parent / f"{module.__name__}.pyi"

    if not filepath.is_file():
        return ""

    content = filepath.read_text(encoding="utf-8").strip() + "\n"
    content = replace_docstring_variables(content)

    return content