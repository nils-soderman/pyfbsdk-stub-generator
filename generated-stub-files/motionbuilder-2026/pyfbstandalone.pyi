"""
Stub file generated for MotionBuilder 2026 using:
https://github.com/nils-soderman/pyfbsdk-stub-generator

This module provides functionality to initialize MotionBuilder's Python API (pyfbsdk) after launching
the mobupy Python interpreter.
"""


def initialize() -> None:
    """ 
    Initialize MotionBuilder for standalone Python usage.

    Must be called before using any `pyfbsdk` functionality when running the mobupy Python interpreter.

    Raises:
        RuntimeError: If called from within MotionBuilder. This function can only be called in mobupy.
    """
