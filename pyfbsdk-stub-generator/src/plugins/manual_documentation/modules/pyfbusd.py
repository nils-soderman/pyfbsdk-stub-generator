""" 
This files contains manually typed documentation for pyfbusd.
Here we we can manually patch types, docstrings, etc. for any entries that are missing or have incorrect information in the offical documentation.

Dict entries should be in alphabetical order
"""
from __future__ import annotations

import pyfbusd as usd

from ..base import ParamDoc, FunctionDoc, PropertyDoc, ClassDoc


# ---------------------------------------------------------------------
#                          Classes
# ---------------------------------------------------------------------

CLASSES: dict[type, ClassDoc] = {
    usd.FBUsdStageProxy: ClassDoc(
        properties=[
            PropertyDoc("FilePath", "str", "The file path of the USD stage."),
            PropertyDoc("FrameOffset", "FBPropertyAnimatableInt", "The frame offset applied to the USD stage."),
        ],
        functions=[
            FunctionDoc(
                ref="__init__",
                parameters=[
                    ParamDoc("Name", "str"),
                ]
            )
        ]
    )
}


# ---------------------------------------------------------------------
#                          FUNCTIONS
# ---------------------------------------------------------------------

FUNCTIONS: dict[object, FunctionDoc] = {
    usd.CreateUsdStageProxy: FunctionDoc(
        parameters=[
            ParamDoc("Name", "str"),
        ],
        return_type=usd.FBUsdStageProxy
    ),
}
