import sys
import os

from importlib import reload

# Append to directory
sys.path.append(os.path.dirname(__file__))

import mobu_stub_generator.stub_generator as StubGenerator
reload(StubGenerator)

# Make sure code is running inside of MotionBuilder
try:
    import pyfbsdk_additions
    import pythonidelib
    import pyfbsdk
except:
    raise Exception("Code running outside of MotionBuilder. Please run this inside of the MotionBuilder version you want to generate a stub file for.")


OUTPUT_DIRECTORY = os.path.join(os.path.dirname(__file__), "generated-stub-files")


def GetMotionBuilderVersion():
    """ Get the current version of MotionBuilder """
    return int(2000 + pyfbsdk.FBSystem().Version / 1000)


def GenerateDefaultPackages(OutputDir = ""):
    Version = GetMotionBuilderVersion()
    if not OutputDir:
        OutputDir = os.path.join(OUTPUT_DIRECTORY, "motionbuilder-%s" % Version)

    StubsToGenerate = [
        (pyfbsdk, "pyfbsdk_gen_doc"),
        (pythonidelib, ""),
        (pyfbsdk_additions, "pyfbsdk_additions")
    ]

    for Module, GeneratedDocFile in StubsToGenerate:
        OutFilepath = os.path.join(OutputDir, "%s.py" % Module.__name__)
        StubGenerator.GenerateStub(Module,
                                   Filepath = OutFilepath,
                                   SourcePyFile = GeneratedDocFile,
                                   DocumentationVersion = Version
                                   )


if "builtin" in __name__:
    GenerateDefaultPackages()
