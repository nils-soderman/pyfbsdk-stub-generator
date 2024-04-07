from __future__ import annotations

from typing import Any

import pyfbsdk

from ..doc_bases import Parameter, FunctionBase, ClassBase, PropertyBase


# ---------------------------------------------------------------------
#                          Classes
# ---------------------------------------------------------------------

class FBComponent(ClassBase):
    class PropertyCreate(FunctionBase):
        Parameters = (None, None, None, None, None, Parameter(Type = (pyfbsdk.FBProperty, "None")))
        ReturnType = Any
        
class FBModel(ClassBase):
    class Parent(PropertyBase):
        Types = (pyfbsdk.FBModel, "None")


class FBModelPath3D(ClassBase):
    class PathEndCapStyle(PropertyBase):
        Types = pyfbsdk.FBModelPath3D.EPathEndCapStyle

# ---------------------------------------------------------------------
#                          Functions
# ---------------------------------------------------------------------

class GetToolPosition(FunctionBase):
    """This function will get the position of a specific tool.
    ### Parameters:
    - Tool: A pointer to the tool."""
    Parameters = (Parameter("Tool", pyfbsdk.FBTool),)
    ReturnType = tuple


class GetToolPositionByName(FunctionBase):
    """This function will get the position of a specific tool.
    ### Parameters:
    - ToolName: The name of the tool as shown in the Open Reality menu."""
    Parameters = (Parameter("ToolName", str),)
    ReturnType = tuple


class GetToolSize(FunctionBase):
    """This function will get the size of a specific tool in the GUI.
    ### Parameters:
    - Tool: A pointer to the tool."""
    Parameters = (Parameter("Tool", pyfbsdk.FBTool),)
    ReturnType = tuple


class GetToolSizeByName(FunctionBase):
    """This function will get the size of a specific tool in the GUI.
    ### Parameters:
    - ToolName: The name of the tool as shown in the Open Reality menu."""
    Parameters = (Parameter("ToolName", str),)
    ReturnType = tuple


class SetToolPosition(FunctionBase):
    """This function will set the position of a specific tool.
    ### Parameters:
    - Tool: A pointer to the tool.
    - PosX: New position in X for the tool.
    - PosY: New position in Y for the tool."""
    Parameters = (Parameter("Tool", pyfbsdk.FBTool), Parameter("PosX", int), Parameter("PosY", int))


class SetToolPositionByName(FunctionBase):
    """This function will set the position of a specific tool.
    ### Parameters:
    - ToolName: The name of the tool as shown in the Open Reality menu.
    - PosX: New position in X for the tool.
    - PosY: New position in Y for the tool."""
    Parameters = (Parameter("ToolName", str), Parameter("PosX", int), Parameter("PosY", int))

# Convert all functions above into classes that inherit from FunctionBase:


class SetToolSize(FunctionBase):
    """This function will set the size of a specific tool in the GUI.
    ### Parameters:
    - Tool: A pointer to the tool.
    - Width: New width of the tool.
    - Height: New height of the tool."""
    Parameters = (Parameter("Tool", pyfbsdk.FBTool), Parameter("Width", int), Parameter("Height", int))


class SetToolSizeByName(FunctionBase):
    """This function will set the size of a specific tool in the GUI.
    ### Parameters:
    - ToolName: The name of the tool as shown in the Open Reality menu.
    - Width: New width of the tool.
    - Height: New height of the tool."""
    Parameters = (Parameter("ToolName", str), Parameter("Width", int), Parameter("Height", int))


class ShowTool(FunctionBase):
    """This function will show a specific tool in the GUI.
    ### Parameters:
    - Tool: A pointer to the tool to show.
    - bResizeWnd: Adjust the size of the tool window if needed (if started too close to the end of the screen for example).

    ### Returns:
    A pointer to the FBTool object, `None` otherwise."""
    Parameters = (Parameter("Tool", pyfbsdk.FBTool), Parameter("ResizeWnd", bool, True))
    ReturnType = pyfbsdk.FBTool


class ShowToolByName(FunctionBase):
    """This function will show a specific tool in the GUI.
    ### Parameters:
        - ToolName: The name of the tool as shown in the Open Reality menu.
        - bResizeWnd: Adjust the size of the tool window if needed (if started too close to the end of the screen for example).

    ### Returns:
    A pointer to the FBTool object, `None` otherwise."""

    Parameters = (
        Parameter("ToolName", str),
        Parameter("ResizeWnd", bool, True),
    )

    ReturnType = pyfbsdk.FBTool
