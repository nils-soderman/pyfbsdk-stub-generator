"""
Stub file generated for MotionBuilder 2024 using:
https://github.com/nils-soderman/pyfbsdk-stub-generator

This module improves pyfbsdk UI building.

It provides Layout classes similar to classes found in Qt/GTK/Tcl/Tk that
helps to manage region handling and UI control positioning.

It also gives functions to create/destroy and manage Tools created in Python.
"""
from __future__ import annotations

import pyfbsdk

# Typing not included in the actual module:
import typing
from typing_extensions import Unpack

__ToolList_T = dict[str, pyfbsdk.FBTool]


class __BoxLayoutCustomParams(typing.TypedDict, total=False):
    space: int
    width: int
    height: int

# pyfbsdk_additions Stub:


# Tool Management
FBToolList: __ToolList_T = {}
FBToolListeners: list[typing.Callable[[__ToolList_T], typing.Any]] = []
FBToolManager = None


def FBCreateUniqueTool(name: str) -> pyfbsdk.FBTool:
    """
    Create a Tool with a unique name. Will destroy 
    any other similarly named tool.
    """
    ...


def FBGetTools() -> dict[str, pyfbsdk.FBTool]:
    """Get the list of Python Tools instantiated in MotionBuilder"""
    ...


def FBCreateTool(name: str) -> pyfbsdk.FBTool:
    """Create a tool given a tool name. Notify all Tool listeners about it."""
    ...


def FBDestroyTool(tool: pyfbsdk.FBTool) -> None:
    """Destroy a Tool."""
    ...


def FBDestroyToolByName(name: str) -> None:
    """Destroy a tool given its name. Notify all Tool listeners about it"""
    ...


def FBAddTool(tool: pyfbsdk.FBTool) -> pyfbsdk.FBTool:
    """Method that can be used for custom tool deriving from FBTool to add themselves to the too list"""
    ...


def FBRemoveTool(tool: pyfbsdk.FBTool) -> None:
    """Remove a given tool from the tool list. It won't be managed anymore by the Tool Manager"""
    ...


def FBAddToolListener(toollistener: typing.Callable[[__ToolList_T], typing.Any]) -> None:
    """Add a tool listener that will be notified on new tool creation/destruction."""
    ...


def FBRemoveToolListener(toollistener: typing.Callable[[__ToolList_T], typing.Any]) -> None:
    """Remove a tool listener."""
    ...


def _FBNotityToolListener() -> None:
    ...


class FBButtonGroup:
    """
    Button group class used to manage multiple radio buttons. 
    This class ensure that only one radio button is enabled (it does all the ClickState management)

    - Use the Add method to Add new radio button to the group.        
    - Use AddCallback method to register a UNIQUE callback that will be called when ANY
      of the registered radio buttons is clicked.
    """

    def __init__(self):
        self.buttons: list[pyfbsdk.FBButton] = []
        self.callback: typing.Callable[[pyfbsdk.FBButton, pyfbsdk.FBEventActivate], typing.Any] | typing.Literal[False] = False

    def Add(self, btn: pyfbsdk.FBButton) -> None:
        """Add a radio button to group."""
        ...

    def AddCallback(self, callback: typing.Callable[[pyfbsdk.FBButton, pyfbsdk.FBEventActivate], typing.Any] | typing.Literal[False]) -> None:
        """Add a callback that will be call when a radiobutton in the group is clicked."""
        ...

    def _MultiCallback(self, control: pyfbsdk.FBButton, event: pyfbsdk.FBEventActivate) -> None:
        ...


class FBTabControl(pyfbsdk.FBLayout):
    """
    A real FBTabControl that improve the behavior of the FBTabPanel.

    This class manage the Tabs and the 'middle region' used to display. It manages
    all the region 'swapping' necessary to implement a Tab behavior.

    - Use Add method to Add a Control to the FBTabControl. This will create a tab
      and ensure that when that tab is clicked the Control is shown.
    - Use SetContent with a tab index To specify which tab should be displayed.
    """

    def __init__(self):
        self.TabPanel: pyfbsdk.FBTabPanel = pyfbsdk.FBTabPanel()
        self.TabContents: list[pyfbsdk.FBVisualComponent] = []

    def Add(self, name: str, content: pyfbsdk.FBVisualComponent) -> None:
        """Create a tab with <name> that will display <content> when clicked."""
        ...

    def SetContent(self, index: int) -> None:
        """Show <content> associated with tab at <index>"""
        ...

    def _ChangeCallback(self, control: pyfbsdk.FBTabPanel, event: pyfbsdk.FBEvent) -> None:
        ...


class FBBoxLayout(pyfbsdk.FBLayout):
    """
    Base class for a line layout (either vertical or horizontal)

    This class is made to ease the creation of Tool in Python. It manages
    all the 'FBLayout' region stuff (no need to use FBAddRegionParam anymore!).

    Generally you just Add a Control to the layout specifying some parameters.

    There are 2 kinds of Add: Add with fixed size and AddRelative which ensure
    the control Added will occupy a 'percentage' of the available space AFTER the 
    fixed space has been assigned.        
    """

    def __init__(self, floworientation: pyfbsdk.FBAttachType):
        self.controls: list[FBBoxLayout.ControlDesc] = []
        self.ratio: float = 0.0
        self.allocatedsize: int = 0
        self.floworientation = floworientation
        self.default_space = 5

    def Add(self, control: pyfbsdk.FBVisualComponent, size: int, **customparams: Unpack[__BoxLayoutCustomParams]) -> None:
        """
        Add a control to layout specifying its FIXED size.

        customparams:
        space: space between previous control
        width: fixed width if layout is vertical based
        height: fixed height if layout is horizontal based.
        """
        ...

    def AddRelative(self, control: pyfbsdk.FBVisualComponent, ratio: float = 1.0, **customparams: __BoxLayoutCustomParams) -> None:
        """ 
        Add a control to layout specifying its RATIO. This means
        the control will be assigned a size based on the space left when all FIXED
        size have been allocated.

        customparams:
        space: space between prev control
        width: fixed width if layout is vertical based
        height: fixed height if layout is horizontal based.
        """
        ...

    def Remove(self, control: pyfbsdk.FBVisualComponent) -> None:
        """ Remove a control from the layout. """
        ...

    def RemoveAll(self) -> None:
        """ Remove all controls from layout """
        ...

    class ControlDesc:
        def __init__(self, regionName: str, control: pyfbsdk.FBVisualComponent, size: int, ratio: float, customparams: __BoxLayoutCustomParams):
            self.regionName: str = regionName
            self.size: int = size
            self.control = control
            self.ratio: float = ratio
            self.customparams = customparams

        def getSpace(self) -> int:
            ...

        def setSpace(self, space: int) -> None:
            ...

        space = property(getSpace, setSpace)

    def _Resize(self, control: pyfbsdk.FBLayout, event: pyfbsdk.FBEventResize) -> None:
        ...

    def _GetDesc(self, control: pyfbsdk.FBVisualComponent) -> ControlDesc | None:
        ...

    def _Add(self, control: pyfbsdk.FBVisualComponent, size: int, ratio: float, customparams: __BoxLayoutCustomParams) -> None:
        ...

    def _Restructure(self) -> None:
        ...

    def _computeregion(self) -> None:
        raise RuntimeError("Must be reimplemented!")


class FBHBoxLayout(FBBoxLayout):
    """
    This class manages a FBBoxLayout Horizontal (see FBBoxLayout for documentation on how to Add/Remove control).
    Add method specify the fixed width of a control.
    """

    def __init__(self, floworientation = pyfbsdk.FBAttachType.kFBAttachLeft):
        """ 
        floworientation: 
        FBAttachType.kFBAttachLeft : all controls added from left to right ->
        FBAttachType.kFBAttachRight: all controls added from right to left <-
        """
        ...

    def _computeregion(self) -> None:
        ...


class FBVBoxLayout(FBBoxLayout):
    """ 
    This class manages a FBBoxLayout Vertical (see FBBoxLayout for documentation on how to Add/Remove control).
    Add method specify the fixed height of a control.
    """

    def __init__(self, floworientation = pyfbsdk.FBAttachType.kFBAttachTop):
        """
        floworientation: 
        FBAttachType.kFBAttachTop : all controls added from top to bottom 
        FBAttachType.kFBAttachBottom: all controls added from bottom to top
        """

    def _computeregion(self) -> None:
        ...


class FBGridLayout(pyfbsdk.FBLayout):
    """
    More advance layout that allow organisation of control in a grid. 
    User can place a control at specific coordinates. 
    User can also setup parameters that affect whole row or column.
    """

    def __init__(self, spacing: int = 5):
        self.defaultspacing = spacing
        self.controls: list[FBGridLayout.ControlDesc] = []
        self.rows: list[FBGridLayout.RowDesc] = []
        self.cols: list[FBGridLayout.ColDesc] = []

    def Add(self, control: pyfbsdk.FBVisualComponent, r: int, c: int, attachX = pyfbsdk.FBAttachType.kFBAttachLeft, attachY = pyfbsdk.FBAttachType.kFBAttachTop, width: int | None = None, height: int | None = None) -> None:
        """
        Add control in row r and column c.
        attachX: specifies a control horizontal attachment in a column (kFBAttachLeft, kFBAttachRight)
        attachY: specifies a control veritcal attachment in a row (kFBAttachTop, kFBAttachBottom)
        width: fixed width of a control
        height: fixed height of a control
        """
        ...

    def AddRange(self, control: pyfbsdk.FBVisualComponent, r1: int, r2: int, c1: int, c2: int, attachX = pyfbsdk.FBAttachType.kFBAttachLeft, attachY = pyfbsdk.FBAttachType.kFBAttachTop) -> None:
        """
        Add control in a range of coordinates. Control will span from row1 to row2 and from col1 to col2        
        attachX: specifies a control horizontal attachment in a column (kFBAttachLeft, kFBAttachRight)
        attachY: specifies a control veritcal attachment in a row (kFBAttachTop, kFBAttachBottom)
        """
        ...

    def Remove(self, control: pyfbsdk.FBVisualComponent) -> None:
        ...

    def RemoveAll(self) -> None:
        """Remove all controls from the grid"""
        ...

    def SetRowHeight(self, r: int, h: int) -> None:
        """ Set row r fixed height"""
        ...

    def SetRowRatio(self, r: int, ratio: float) -> None:
        """ 
        Set row r ratio. this row will be allocated height according to this ratio
        when all fixed height has been allocated.
        """
        ...

    def SetRowSpacing(self, r: int, spacing: int) -> None:
        """ Set row r spacing between previous row. """
        ...

    def SetColWidth(self, c: int, w: int) -> None:
        """ Set col c fixed width. """
        ...

    def SetColRatio(self, c: int, ratio: float) -> None:
        """
        Set col c ratio. this col will be allocated width according to this ratio
        when all fixed width has been allocated.
        """
        ...

    def SetColSpacing(self, c: int, spacing: int) -> None:
        """ Set col c spacing between previous col. """
        ...

    def _GetDesc(self, control: pyfbsdk.FBVisualComponent) -> ControlDesc | None:
        ...

    class ColDesc:
        def __init__(self):
            self.width: int | None = None
            self.ratio = 1.0
            self.spacing: int | None = None
            self.x = 0
            self.w = 0

        def Right(self) -> int: ...

    class RowDesc:
        def __init__(self):
            self.height: int | None = None
            self.ratio = 1.0
            self.spacing: int | None = None
            self.y = 0
            self.h = 0

        def Bottom(self) -> int: ...

    class ControlDesc:
        def __init__(self, control: pyfbsdk.FBVisualComponent, regionName: str, r1: int, r2: int, c1: int, c2: int, attachX: pyfbsdk.FBAttachType, attachY: pyfbsdk.FBAttachType, w: int | None, h: int | None):
            self.control = control
            self.regionName = regionName
            self.ratio = 1.0
            self.r1 = r1
            self.r2 = r2
            self.c1 = c1
            self.c2 = c2
            self.attachX = attachX
            self.attachY = attachY
            self.w = w
            self.h = h

    def _Resize(self, control: pyfbsdk.FBLayout, event: pyfbsdk.FBEventResize) -> None:
        ...

    def _Add(self, control: pyfbsdk.FBVisualComponent, r1: int, r2: int, c1: int, c2: int, attachX: pyfbsdk.FBAttachType, attachY: pyfbsdk.FBAttachType, width: int | None, height: int | None) -> None:
        ...

    def _Updaterows(self, r: int) -> None:
        ...

    def _Updatecols(self, c: int) -> None:
        ...

    def _GetSpace(self, element: ColDesc | RowDesc) -> int:
        ...

    def _Restructure(self) -> None:
        ...
