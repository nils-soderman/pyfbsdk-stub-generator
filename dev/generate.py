""" 
Script used to generate the stub files under: ./generated-stub-files/

This script is also used during development to test the generator, therefore it 
reloads all of the modules and caches the online documentation on disk.
"""
from __future__ import annotations

import subprocess
import sys
import os

# from types import ModuleType
from importlib import reload

ROOT_DIR = os.path.join(os.path.dirname(__file__), "..")
REQUIRED_PACKAGES_DIR = os.path.join(ROOT_DIR, "env")

# This will cache the online documentation
os.environ["PYFBSDK_DEVMODE"] = "True"


def GetPyprojectData(PythonExecutable: str) -> dict:
    """ 
    Read the pyproject.toml file and return the data as a dictionary.
    """
    try:
        import toml
    except ImportError:
        subprocess.run([PythonExecutable, "-m", "pip", "install", "toml", "--target", REQUIRED_PACKAGES_DIR], check=True)
        sys.path.append(REQUIRED_PACKAGES_DIR)
        import toml

    PyProject = os.path.join(ROOT_DIR, "pyproject.toml")
    with open(PyProject, 'r', encoding="utf8") as File:
        return toml.load(File)


def GetPyProjectDependencies(PythonExecutable: str) -> list[str]:
    """ 
    Read the pyproject.toml file and return the dependencies as a dictionary.
    """
    return GetPyprojectData(PythonExecutable).get('project', {}).get('dependencies', [])


def SetupEnvironment():
    # Install required packages
    if not os.path.exists(REQUIRED_PACKAGES_DIR):
        MoBuPyExe = os.path.join(os.path.dirname(sys.executable), "mobupy.exe")
        Dependencies = GetPyProjectDependencies(MoBuPyExe)

        subprocess.run([MoBuPyExe, "-m", "pip", "install", *Dependencies, "--target", REQUIRED_PACKAGES_DIR], check=True)

    # Add the required packages to the path
    for Path in (ROOT_DIR, REQUIRED_PACKAGES_DIR):
        if Path not in sys.path:
            sys.path.append(Path)


def ReloadPyfbsdkStubGenerator():
    """ Reload all of the modules that are part of the pyfbsdk_stub_generator package """
    for ImportedModule in list(sys.modules.values()):
        if "pyfbsdk_stub_generator" in ImportedModule.__name__:
            reload(ImportedModule)


def main():
    SetupEnvironment()
    ReloadPyfbsdkStubGenerator()

    import pyfbsdk_stub_generator
    from pyfbsdk_stub_generator.stub_generator import GetMotionBuilderVersion

    OutDir = os.path.join(ROOT_DIR,
                          "generated-stub-files",
                          f"motionbuilder-{GetMotionBuilderVersion()}")

    pyfbsdk_stub_generator.Generate(OutDir)


if "builtin" in __name__:
    # Script is running from within MotionBuilder
    main()

if __name__ == "__main__":
    # Script is running from MobuPy
    try:
        # In versions 2025 and above, the mobupy needs to be initialized before pyfbsdk can be used
        import pyfbstandalone # type: ignore
        pyfbstandalone.initialize()
    except ModuleNotFoundError:
        pass

    main()
