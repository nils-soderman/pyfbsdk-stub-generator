"""
This module containts manually written documentation.
If a class / function is missing from the official pyfbsdk documentation it can be documented here.

To add a doc string to a property, add a second property with the same name except with the suffix "__doc__".
Example:
    HelloWorld = "Hello"
    HelloWorld__doc__ = "This is the DocString for HelloWorld property!"
    
Function overloading:
To overload a function add a "_1" suffix, increasing the number for each overloaded function. 
Example: 
def HelloWorld_1(arg1: int): ...
def HelloWorld_2(arg1: str): ...
"""

from __future__ import annotations

import pyfbsdk


class FBAnimationNode:
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


class FBVideoClip:
    CurrentFrame: int
    CurrentFrame__doc__ = "Read Write Property: Current frame."
    CurrentFrameTime: pyfbsdk.FBTime
    CurrentFrameTime__doc__ = "Read Write Property: Current time in clip."
    CurrentFrameTimeCode: property
    Filename: str
    Filename__doc__ = "Read Write Property: Filename of media."
    Format: pyfbsdk.FBVideoFormat
    Format__doc__ = "Read Only Property: Video format."
    FrameTime: pyfbsdk.FBTime
    FrameTime = "Read Only Property: Inverse of FPS, time per frame"
    FreeRunning: bool
    FreeRunning__doc__ = "Read Write Property: Is free Running on?"
    Height: int
    Height__doc__ = "Read Only Property: Height of image."
    InterlaceMode: pyfbsdk.FBVideoInterlaceMode
    InterlaceMode__doc__ = "Read Write Property: Interlace mode."
    LastFrame: int
    LastFrame__doc__ = "Read Only Property: Last frame in clip."
    LastFrameTime: pyfbsdk.FBTime
    LastFrameTime__doc__ = "Read Only Property: Time of last frame"
    Loop: bool
    Loop__doc__ = "Read Write Property: Loop video clip?"
    PlaySpeed: float
    PlaySpeed__doc__ = "Read Write Property: Playback speed."
    PowerOfTwoHeight: int
    PowerOfTwoHeight__doc__ = "Read Only Property: Closest power of two value superior to height of image."
    PowerOfTwoWidth: int
    PowerOfTwoWidth__doc__ = "Read Only Property: Closest power of two value superior to width of image."
    ProxyMode: pyfbsdk.FBVideoProxyMode
    ProxyMode__doc__ = "Read Write Property: Proxy mode."
    RelativePath: str
    RelativePath__doc__ = "Read Only Property: Relative path of media."
    StartFrame: int
    StartFrame__doc__ = "Read Write Property: Frame to begin video playback from."
    StopFrame: int
    StopFrame__doc__ = "Read Write Property: Frame to end video playback at."
    StorageMode: pyfbsdk.FBVideoStorageMode
    StorageMode__doc__ = "Read Write Property: Storage mode."
    TimeOffset: pyfbsdk.FBTime
    TimeOffset__doc__ = "Read Write Property: Temporal offset for beginning of video."
    Width: int
    Width__doc__ = "Read Only Property: Width of image."

    def DrawImage(self, X=0, Y=0, W=-1, H=-1, Frame=-1):
        """
        Draw a frame of the image to the current view.
        ### Parameters:
            - X: X position of image (default=0).
            - Y: Y position of image (default=0).
            - W: Width of image (default=-1).
            - H: Height of image (default=-1).
            - Frame: Frame to draw (default=-1).
        """
        ...

    def IsValid(self) -> bool:
        """
        Verifies the validity of the FBVideo object.
        ### Returns:
        true if data is valid.
        """
        ...

    def __init__(self, Name: str):
        """
        ### Parameters:
            - pName: Name of video media.

        ### Warning:
        The Name parameter must point to a valid media file, otherwise the object will not be valid. Use the method `IsValid()` to confirm the object status.
        """
        ...


class FBVideoGrabOptions:
    AntiAliasing: bool
    AntiAliasing__doc__ = "Read Write Property: If true, video frames will be anti-aliased."
    AudioRenderFormat: property
    AudioRenderFormat__doc__ = "Read Write roperty: Audio render format."
    AudioUseCustomStandaloneFileName: property
    BitsPerPixel: pyfbsdk.FBVideoRenderDepth
    BitsPerPixel__doc__ = "Read Write Property: Video grab color depth."
    CameraResolution: pyfbsdk.FBCameraResolutionMode
    CameraResolution__doc__ = "Read Write Property: Camera Resolution."
    FieldMode: pyfbsdk.FBVideoRenderFieldMode
    FieldMode__doc__ = "Read Write Property: Video grab field mode."
    OutputFileName: str
    OutputFileName__doc__ = "Read Write Property: Grabbing destination file."
    RenderAudio: bool
    RenderAudio__doc__ = "Read Write Property: If true and there's audio in the scene, add audio to the output file."
    ShowCameraLabel: bool
    ShowCameraLabel__doc__ = "Read Write Property: If true, display camera label information."
    ShowSafeArea: bool
    ShowSafeArea__doc__ = "Read Write Property: If true, display safe area."
    ShowTimeCode: bool
    ShowTimeCode__doc__ = "Read Write Property: If true, display time code information."
    StillImageCompression: int
    StillImageCompression__doc__ = "Property: Compression ratio for image(jpg) 0-100 where 0=Greatest compression, 100=Least Compression."
    TimeSpan: pyfbsdk.FBTimeSpan
    TimeSpan__doc__ = "Read Write Property: Start and stop selection time to grab."
    TimeSteps: pyfbsdk.FBTime
    TimeSteps__doc__ = "Read Write Property: Time step length between each grab."
    ViewingMode: pyfbsdk.FBVideoRenderViewingMode
    ViewingMode__doc__ = "Read Write Property: Video grab viewing mode."


class FBPlotOptions:
    ConstantKeyReducerKeepOneKey: bool
    ConstantKeyReducerKeepOneKey__doc__ = "Read Write Property: Should the constant key reducer keep at least one key?"
    EvaluateDeformation: bool
    PlotAllTakes: bool
    PlotAllTakes__doc__ = "Read Write Property: Should we plot all takes?"
    PlotAuxEffectors: property
    PlotLockedProperties: bool
    PlotOnFrame: bool
    PlotOnFrame__doc__ = "Read Write Property: Should we plot on frame?"
    PlotPeriod: pyfbsdk.FBTime
    PlotPeriod__doc__ = "Read Write Property: The plot period (1/fps)."
    PlotTangentMode: pyfbsdk.FBPlotTangentMode
    PlotTranslationOnRootOnly: bool
    PlotTranslationOnRootOnly__doc__ = "Read Write Property: Should we plot the translation on root only?"
    PreciseTimeDiscontinuities: bool
    PreciseTimeDiscontinuities__doc__ = "Read Write Property: Should we plot the translation on root only?"
    RotationFilterToApply: pyfbsdk.FBRotationFilter
    RotationFilterToApply__doc__ = "Read Write Property: The rotation filter to apply."
    UseConstantKeyReducer: bool
    UseConstantKeyReducer__doc__ = "Read Write Property: Should we use a constant key reducer with the filter?"


class FBEvaluateManager:
    DeviceCount: int
    DualQuaternionSkinning: bool
    FrameSkipOptimization: bool
    NodeCount: int
    OnRenderingPipelineEvent: object
    OnSynchronizationEvent: object
    ParallelDeformation: bool
    ParallelEvaluation: bool
    ParallelPipeline: bool
    ParallelScheduleType: pyfbsdk.FBParallelScheduleType
    UseGPUDeformation: bool


class FBTexture:
    Alpha: float
    BlendMode: pyfbsdk.FBTextureBlendMode
    Height: int
    Mapping: pyfbsdk.FBTextureMapping
    Rotation: pyfbsdk.FBPropertyAnimatableVector3d
    Scaling: pyfbsdk.FBPropertyAnimatableVector3d
    SwapUV: bool
    TextureOGLId: int
    Translation: pyfbsdk.FBPropertyAnimatableVector3d
    UseType: pyfbsdk.FBTextureUseType
    Video: pyfbsdk.FBVideo
    Width: int
    def Clone(self) -> FBTexture: ...
