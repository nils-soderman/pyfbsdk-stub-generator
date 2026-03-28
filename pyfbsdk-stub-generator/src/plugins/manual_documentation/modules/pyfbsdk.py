""" 
This files contains manually typed documentation for pyfbsdk.
Here we we can manually patch types, docstrings, etc. for any entries that are missing or have incorrect information in the offical documentation.

Dict entries should be in alphabetical order
"""
from __future__ import annotations

import pyfbsdk as fb

from ..base import ParamDoc, FunctionDoc, PropertyDoc, ClassDoc


# ---------------------------------------------------------------------
#                          Classes
# ---------------------------------------------------------------------

CLASSES: dict[type, ClassDoc] = {
    fb.FBActionManager: ClassDoc(
        properties=[
            PropertyDoc("CurrentInteractionMode", str),
        ],
    ),

    fb.FBCamera: ClassDoc(
        properties=[
            PropertyDoc("AnimatableFarPlane", fb.FBPropertyAnimatableDouble),
            PropertyDoc("AnimatableNearPlane", fb.FBPropertyAnimatableDouble),
        ],
    ),

    fb.FBComponent: ClassDoc(
        properties=[
            PropertyDoc("FullName", str),
            PropertyDoc("OwnerNamespace", fb.FBNamespace | None),
        ],
        functions=[
            FunctionDoc("PropertyCreate", parameters=[None, None, None, None, None, ParamDoc(parameter_type=fb.FBProperty | None)], return_type="FBProperty|None"),
        ],
    ),

    fb.FBEditProperty: ClassDoc(
        properties=[
            PropertyDoc("Property", fb.FBProperty),
        ],
    ),

    fb.FBEditPropertyModern: ClassDoc(
        properties=[
            PropertyDoc("Property", fb.FBProperty),
        ],
    ),

    fb.FBEventConnectionKeyingNotify: ClassDoc(
        properties=[
            PropertyDoc("Action", fb.FBConnectionAction),
            PropertyDoc("Plug", fb.FBPlug),
            PropertyDoc("Property", fb.FBPropertyAnimatable),
            PropertyDoc("StartTime", fb.FBTime),
            PropertyDoc("StopTime", fb.FBTime),
        ],
    ),

    fb.FBEventEvalGlobalCallback: ClassDoc(
        properties=[
            PropertyDoc("Timing", fb.FBGlobalEvalCallbackTiming),
        ],
    ),

    fb.FBEventVideoFrameRendering: ClassDoc(
        properties=[
            PropertyDoc("FrameCount", int),
            PropertyDoc("FrameNumber", int),
            PropertyDoc("State", fb.FBEventVideoFrameRendering.EState),
        ],
    ),

    fb.FBFCurveEvent: ClassDoc(
        properties=[
            PropertyDoc("ParentAnimationNode", fb.FBAnimationNode),
            PropertyDoc("ParentComponent", fb.FBComponent),
            PropertyDoc("ParentProperty", fb.FBPropertyAnimatable),
        ],
    ),

    fb.FBHUDElement: ClassDoc(
        properties=[
            PropertyDoc("Visibility", bool),
        ],
    ),

    fb.FBLight: ClassDoc(
        properties=[
            PropertyDoc("ConeAngle", float),
        ],
    ),

    fb.FBMenuManager: ClassDoc(
        functions=[
            FunctionDoc("InsertBefore", parameters=[ParamDoc("MenuPath", str | None)]),
            FunctionDoc("InsertAfter", parameters=[ParamDoc("MenuPath", str | None)]),
            FunctionDoc("InsertFirst", parameters=[ParamDoc("MenuPath", str | None)]),
            FunctionDoc("InsertLast", parameters=[ParamDoc("MenuPath", str | None)]),
        ],
    ),

    fb.FBModel: ClassDoc(
        properties=[
            PropertyDoc("Parent", fb.FBModel | None),
            PropertyDoc("CullingMode", fb.FBModelCullingMode),
        ],
    ),

    fb.FBModelPath3D: ClassDoc(
        properties=[
            PropertyDoc("PathEndCapStyle", fb.FBModelPath3D.EPathEndCapStyle),
        ],
    ),

    fb.FBNamespace: ClassDoc(
        properties=[
            PropertyDoc("ContentCount", int),
        ],
        functions=[
            FunctionDoc("__init__", parameters=[None, ParamDoc(parameter_type=fb.FBNamespace | None)]),
        ],
    ),

    fb.FBPlug: ClassDoc(
        functions=[
            FunctionDoc("GetDst", parameters=[ParamDoc("Index", int)], return_type=fb.FBPlug),
            FunctionDoc("GetSrc", parameters=[ParamDoc("Index", int)], return_type=fb.FBPlug),
            FunctionDoc("GetOwned", parameters=[ParamDoc("Index", int)], return_type=fb.FBPlug),
            FunctionDoc("GetOwner", return_type=fb.FBPlug),
        ],
    ),

    fb.FBPropertyConnectionEditor: ClassDoc(
        properties=[
            PropertyDoc("Property", fb.FBProperty),
        ],
    ),

    fb.FBPropertyManager: ClassDoc(
        functions=[
            FunctionDoc("__getitem__", parameters=[ParamDoc("Index", int)], return_type=fb.FBProperty),
        ],
    ),

    fb.FBPropertyStateEvent: ClassDoc(
        properties=[
            PropertyDoc("ParentComponent", fb.FBComponent),
            PropertyDoc("Property", fb.FBProperty),  # TODO: This could potentially be limited to FBPropertyAnimatable
        ],
    ),

    fb.FBTimeCode: ClassDoc(
        properties=[
            PropertyDoc("Frame", float),
            PropertyDoc("FrameRate", float),
        ],
    ),

    fb.FBVideoGrabOptions: ClassDoc(
        properties=[
            PropertyDoc("RendererCallbackIndex", int),
            PropertyDoc("RendererCallbackPrefIndex", int),
            PropertyDoc("StereoDisplayMode", fb.FBStereoDisplayMode),
        ],
    ),
}


# ---------------------------------------------------------------------
#                          Functions
# ---------------------------------------------------------------------

FUNCTIONS: dict[object, FunctionDoc] = {
    fb.GetToolPosition: FunctionDoc(
        doc="""This function will get the position of a specific tool.
### Parameters:
- Tool: A pointer to the tool.""",
        parameters=[ParamDoc("Tool", fb.FBTool)],
        return_type=tuple,
    ),

    fb.GetToolPositionByName: FunctionDoc(
        doc="""This function will get the position of a specific tool.
### Parameters:
- ToolName: The name of the tool as shown in the Open Reality menu.""",
        parameters=[ParamDoc("ToolName", str)],
        return_type=tuple,
    ),

    fb.GetToolSize: FunctionDoc(
        doc="""This function will get the size of a specific tool in the GUI.
### Parameters:
- Tool: A pointer to the tool.""",
        parameters=[ParamDoc("Tool", fb.FBTool)],
        return_type=tuple,
    ),

    fb.GetToolSizeByName: FunctionDoc(
        doc="""This function will get the size of a specific tool in the GUI.
### Parameters:
- ToolName: The name of the tool as shown in the Open Reality menu.""",
        parameters=[ParamDoc("ToolName", str)],
        return_type=tuple,
    ),

    fb.SetToolPosition: FunctionDoc(
        doc="""This function will set the position of a specific tool.
### Parameters:
- Tool: A pointer to the tool.
- PosX: New position in X for the tool.
- PosY: New position in Y for the tool.""",
        parameters=[ParamDoc("Tool", fb.FBTool), ParamDoc("PosX", int), ParamDoc("PosY", int)],
    ),

    fb.SetToolPositionByName: FunctionDoc(
        doc="""This function will set the position of a specific tool.
### Parameters:
- ToolName: The name of the tool as shown in the Open Reality menu.
- PosX: New position in X for the tool.
- PosY: New position in Y for the tool.""",
        parameters=[ParamDoc("ToolName", str), ParamDoc("PosX", int), ParamDoc("PosY", int)],
    ),

    fb.SetToolSize: FunctionDoc(
        doc="""This function will set the size of a specific tool in the GUI.
### Parameters:
- Tool: A pointer to the tool.
- Width: New width of the tool.
- Height: New height of the tool.""",
        parameters=[ParamDoc("Tool", fb.FBTool), ParamDoc("Width", int), ParamDoc("Height", int)],
    ),

    fb.SetToolSizeByName: FunctionDoc(
        doc="""This function will set the size of a specific tool in the GUI.
### Parameters:
- ToolName: The name of the tool as shown in the Open Reality menu.
- Width: New width of the tool.
- Height: New height of the tool.""",
        parameters=[ParamDoc("ToolName", str), ParamDoc("Width", int), ParamDoc("Height", int)],
    ),

    fb.ShowTool: FunctionDoc(
        doc="""This function will show a specific tool in the GUI.
### Parameters:
- Tool: A pointer to the tool to show.
- bResizeWnd: Adjust the size of the tool window if needed (if started too close to the end of the screen for example).

### Returns:
A pointer to the FBTool object, `None` otherwise.""",
        parameters=[ParamDoc("Tool", fb.FBTool), ParamDoc("ResizeWnd", bool, True)],
        return_type=fb.FBTool,
    ),

    fb.ShowToolByName: FunctionDoc(
        doc="""This function will show a specific tool in the GUI.
### Parameters:
- ToolName: The name of the tool as shown in the Open Reality menu.
- bResizeWnd: Adjust the size of the tool window if needed (if started too close to the end of the screen for example).

### Returns:
A pointer to the FBTool object, `None` otherwise.""",
        parameters=[ParamDoc("ToolName", str), ParamDoc("ResizeWnd", bool, True)],
        return_type=fb.FBTool,
    ),
}
