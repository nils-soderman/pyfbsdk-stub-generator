""" 
Script used to generate the stub files under: ./generated-stub-files/

This script is also used during development to test the generator, therefore it 
reloads all of the modules and caches the online documentation on disk.
"""

import sys
import os

from types import ModuleType
from importlib import reload


# Reload all stub generator modules
for ImportedModule in list(sys.modules.values()):
    if isinstance(ImportedModule, ModuleType) and "pyfbsdk_stub_generator" in ImportedModule.__name__:
        reload(ImportedModule)

for Path in (
    os.path.dirname(__file__),
    f"C:/Python{sys.version_info.major}{sys.version_info.minor}/lib/site-packages",
    f"{os.getenv('APPDATA')}/Python/Python{sys.version_info.major}{sys.version_info.minor}/site-packages"
):
    if Path not in sys.path:
        sys.path.append(Path)

import pyfbsdk_stub_generator
from pyfbsdk_stub_generator.stub_generator import GetMotionBuilderVersion

# This will cache the online documentation
os.environ["PYFBSDK_DEVMODE"] = "True"


def main():
    OutDir = os.path.join(os.path.dirname(__file__),
                          "generated-stub-files",
                          f"motionbuilder-{GetMotionBuilderVersion()}")
    pyfbsdk_stub_generator.Generate(OutDir)


if "builtin" in __name__:
    main()
