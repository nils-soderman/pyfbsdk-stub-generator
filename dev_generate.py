""" 
Script used to generate the stub files under: ./generated-stub-files/

This script is also used during development to test the generator, therefore it 
reloads all of the modules and caches the online documentation on disk.
"""

import sys
import os

from types import ModuleType
from importlib import reload

import pyfbsdk

CURRENT_DIR = os.path.dirname(__file__)
REQUIRED_PACKAGES_DIR = os.path.join(CURRENT_DIR, "env")

# Reload all stub generator modules
for ImportedModule in list(sys.modules.values()):
    if isinstance(ImportedModule, ModuleType) and "pyfbsdk_stub_generator" in ImportedModule.__name__:
        reload(ImportedModule)

for Path in (
    CURRENT_DIR,
    REQUIRED_PACKAGES_DIR,
):
    if Path not in sys.path:
        sys.path.append(Path)


try:
    import pyfbsdk_stub_generator
    from pyfbsdk_stub_generator.stub_generator import GetMotionBuilderVersion
except ModuleNotFoundError:
    # Install the required packages
    import subprocess
    MoBuPyExe = os.path.join(os.path.dirname(sys.executable), "mobupy.exe")
    Requirements = os.path.join(CURRENT_DIR, "requirements.txt")
    subprocess.run([MoBuPyExe, "-m", "pip", "install", "-r", Requirements, "--target", REQUIRED_PACKAGES_DIR], check=True)

    pyfbsdk.FBMessageBox("Restart MotionBuilder", "Please restart MotionBuilder to reload the modules.", "Restart")
    exit()

# This will cache the online documentation
os.environ["PYFBSDK_DEVMODE"] = "True"


def main():
    OutDir = os.path.join(CURRENT_DIR,
                          "generated-stub-files",
                          f"motionbuilder-{GetMotionBuilderVersion()}")
    pyfbsdk_stub_generator.Generate(OutDir)


if "builtin" in __name__:
    main()
