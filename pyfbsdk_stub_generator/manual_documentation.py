from __future__ import annotations

import pyfbsdk

"""
This module containts manually written documentation.
If a class / function is missing from the official pyfbsdk documentation it can be documented here.

To add a doc string to a property, add a second property with the same name except with the suffix "__doc__".
Example:
    HelloWorld = "Hello"
    HelloWorld__doc__ = "This is the DocString for HelloWorld property!"
    
Function overloading:
To overload a function
"""


class FBAnimationNode():
    ConnectorType: pyfbsdk.FBAnimationNodeConnectorType
    DefaultInterpolation: pyfbsdk.FBInterpolation
    DefaultInterpolation__doc__ = "Read Write Property: Default type of interpolation."
    FCurve: pyfbsdk.FBFCurve
    FCurve__doc__ = "Read Write Property: FCurve for animation. See sample: StartKeysAtCurrentTime.py."
    KeyCount: int
    KeyCount__doc__ = "Read Only Property: Number of keys."
    Label: str
    Label__doc__ = "Read Write Property: Label (UI Name)."
    Live: bool
    Live__doc__ = "Read Write Property: Is animation live?"
    Nodes: pyfbsdk.FBPropertyListAnimationNode
    Nodes__doc__ = "List of animation nodes."
    RecordMode: bool
    RecordMode__doc__ = "Read Write Property: Is the node in recording mode (device connectors)?"
    UserName: str
    UserName__doc__ = "Read Only Property: Name of animation node."

    def __init__(self, Name):
        """
        ### Parameters:
            - Name: name of animation node (default is NULL).
        """
        ...

    def ConvertGlobalToNodeTime(self, KeyTime):
        """
        Convert global time to node time.
        (NOTE: Only used in the context of a story clip)
        ### Parameters:
            - pKeyTime:	Time of the key to convert.
        """
        ...

    def ConvertNodeToGlobalTime(self, KeyTime):
        """
        Convert node time to global time.
        (NOTE: Only used in the context of a story clip)
        ### Parameters:
            - pKeyTime:	Time of the key to convert.
        """
        ...

    def GetAnimationToPlay(self) -> pyfbsdk.FBAnimationNode:
        """
        Get animation node to play from.
        ### Returns:
        Animation node to be played.
        """
        ...

    def GetAnimationToRecord(self) -> pyfbsdk.FBAnimationNode:
        """
        Get animation node to record to.
        ### Returns:
        Animation node to record to.
        """
        ...

    def GetDataDoubleArrayCount(self) -> int:
        """
        If the DataPtr is of numeric value type .

        .. get the size of the array ex: Light Intensity:1, Translation 3

        ### Returns:
        Size of DataPtr array.
        """
        ...

    def GetSizeOfData(self) -> int:
        """ Get sizeof void Data Ptr. """
        ...

    def IsKey(self) -> bool:
        """
        Verifies if there is a key at the current time.
        ### Returns:
        true if there is a key at the current time.
        """
        ...

    def KeyAdd_1(self, Time: pyfbsdk.FBTime, Data: float, Interpolation: pyfbsdk.FBInterpolation = pyfbsdk.FBInterpolation.kFBInterpolationCubic, TangentMode: pyfbsdk.FBTangentMode = pyfbsdk.FBTangentMode.kFBTangentModeAuto): ...
    def KeyAdd_2(self, Data: float, Interpolation: pyfbsdk.FBInterpolation = pyfbsdk.FBInterpolation.kFBInterpolationCubic, TangentMode: pyfbsdk.FBTangentMode = pyfbsdk.FBTangentMode.kFBTangentModeAuto): ...
    def KeyAdd_3(self, Time: pyfbsdk.FBTime, Data: list, Interpolation: pyfbsdk.FBInterpolation = pyfbsdk.FBInterpolation.kFBInterpolationCubic, TangentMode: pyfbsdk.FBTangentMode = pyfbsdk.FBTangentMode.kFBTangentModeAuto): ...
    def KeyAdd_4(self, Data: list, Interpolation: pyfbsdk.FBInterpolation = pyfbsdk.FBInterpolation.kFBInterpolationCubic, TangentMode: pyfbsdk.FBTangentMode = pyfbsdk.FBTangentMode.kFBTangentModeAuto): ...
    def KeyCandidate(self, Time: pyfbsdk.FBTime = None): ...

    def KeyRemove(self):
        """ Remove key at current time. """
        ...

    def KeyRemoveAt(self, Time: pyfbsdk.FBTime):
        """ Remove key at a given time. """
        ...

    def ReadData_1(self, EvaluateInfo: pyfbsdk.FBEvaluateInfo = None, bConvertGlobalToLocal: bool = False) -> list: ...
    def ReadData_2(self, Time: pyfbsdk.FBTime, bConvertGlobalToLocal = None) -> list: ...
    def ReadLastEvalData(self) -> list: ...

    def SetBufferType(self, bGlobal: bool):
        """ Set buffer type for ANIMATIONNODE_TYPE_LOCAL_TRANSLATION, ANIMATIONNODE_TYPE_LOCAL_ROTATION and ANIMATIONNODE_TYPE_LOCAL_SCALE.
        ### Parameters:
            - bGlobal: Is buffer local or global.
        """
        ...

    def SetCandidate(self, Data: list, bCheckLocked: bool = False) -> bool: ...

    def WriteData(self, Data: list, EvaluateInfo: pyfbsdk.FBEvaluateInfo = None) -> int:
        """ Write data to animation node.
        ### Parameters:
            - Data: Data to write to animation node.
            - EvaluateInfo: Node evaluation information (access to system and local time).
        ### Returns:
        true if successful. 
        """
        ...
