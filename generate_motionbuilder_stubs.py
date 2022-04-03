from pyfbsdk import *

import sys
import os

from importlib import reload

# Append to directory
sys.path.append(os.path.dirname(__file__))

import pyfbsdk_stub_generator as StubGenerator

reload(StubGenerator)


OUTPUT_DIRECTORY = os.path.join(os.path.dirname(__file__), "generated-stub-files")


def GetMotionBuilderVersion():
    """ Get the current version of MotionBuilder """
    return int(2000 + FBSystem().Version / 1000)


def GeneratePyfbsdkStub(OutputDir = ""):
    if not OutputDir:
        OutputDir = os.path.join(OUTPUT_DIRECTORY, "motionbuilder-%s" % GetMotionBuilderVersion())
    
    StubGenerator.Generate(OutputDir)


if "builtin" in __name__:
    GeneratePyfbsdkStub()
