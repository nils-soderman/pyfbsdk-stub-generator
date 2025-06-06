""" 
Script to generate pyfbsdk stub files for all MotionBuilder versions installed on the system.
"""
from __future__ import annotations

import subprocess
import winreg
import os

MOTIONBUILDER_KEY = r"SOFTWARE\Autodesk\MotionBuilder"

def GetInstalledMotionBuilderVersions():
    """ 
    Get all of the MotionBuilder versions installed on the system.
    """

    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, MOTIONBUILDER_KEY) as Key:
        Index = 0
        while True:
            try:
                yield int(winreg.EnumKey(Key, Index))
                Index += 1
            except OSError:
                break


def GetMotionBuilderInstallDirectory(Version: int) -> str:
    """ 
    Get the path to the MotionBuilder version.
    """

    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, MOTIONBUILDER_KEY) as Key:
        with winreg.OpenKey(Key, str(Version)) as VersionKey:
            return winreg.QueryValueEx(VersionKey, "InstallPath")[0]


def main():
    for Version in GetInstalledMotionBuilderVersions():
        if Version < 2022:
            print(f"Skipping MotionBuilder {Version} as it's not supported.")
            continue

        print(f"Generating stub file for MotionBuilder {Version}...")

        InstallDir = GetMotionBuilderInstallDirectory(Version)
        MotionBuilderPython = os.path.join(InstallDir, "bin", "x64", "mobupy.exe")

        # Run the generator
        GenerateScript = os.path.join(os.path.dirname(__file__), "generate.py")
        Result = subprocess.run([MotionBuilderPython, GenerateScript], check=False, capture_output=True, text=True)
        if Result.stdout:
            print(Result.stdout)
        if Result.stderr:
            print(Result.stderr)


if __name__ == "__main__":
    main()
