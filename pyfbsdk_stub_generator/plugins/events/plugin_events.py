"""
Patch callbackframework.FBEventSource properties have correct parameter types
"""

from __future__ import annotations

import pyfbsdk as fb

from ..plugin_base import PluginBaseClass
from ...module_types import StubClass


EVENTS = {
    fb.FBApplication: {
        "FBEventOverrideFileOpen": fb.FBEventOverrideFileOpen,
    },
    fb.FBEvaluateManager: {
        "OnSynchronizationEvent": fb.FBEventEvalGlobalCallback,
        "OnRenderingPipelineEvent": fb.FBEventEvalGlobalCallback 
    },
    fb.FBFCurveEventManager: {
        "OnFCurveEvent": fb.FBFCurveEvent ,
        "OnPropertyEvent": fb.FBPropertyStateEvent,
    },
    fb.FBFileMonitoringManager: {
        "OnFileChangeAnimationClip": fb.FBEventFileChange,
        "OnFileChangeFileReference": fb.FBEventFileChange,
        "OnFileChangeMainScene": fb.FBEventFileChange,
        "OnFileChangePythonEditorScript": fb.FBEventFileChange,
    },
    fb.FBGenericMenu: {
        "OnMenuActivate": fb.FBEventMenu,
    },
    fb.FBPlayerControl: {
        "OnChange": fb.FBEventPlayerControlChange,
    },
    fb.FBScene: {
        "OnChange": fb.FBEventSceneChange,
        "OnTakeChange": fb.FBEventTakeChange,
    },
    fb.FBStoryClip: {
        "OnChange": fb.FBEventClipChange,
    },
    fb.FBSystem: {
        "OnConnectionDataNotify": fb.FBEventConnectionDataNotify,
        "OnConnectionKeyingNotify": fb.FBEventConnectionKeyingNotify,
        "OnConnectionNotify": fb.FBEventConnectionNotify,
        "OnConnectionStateNotify": fb.FBEventConnectionStateNotify,
        "OnVideoFrameRendering": fb.FBEventVideoFrameRendering,
    },
    fb.FBVisualContainer: {
        "OnDblClick": fb.FBEventDblClick,
        "OnDragAndDrop": fb.FBEventDragAndDrop,
    },
    fb.FBButton: {
        "OnClick": fb.FBEventActivate,
    },
    fb.FBTree: {
        "OnSelect": fb.FBEventTreeSelect,
        "OnClickCheck": fb.FBEventTreeSelect,
        "OnCollapsed": fb.FBEventTree,
        "OnCollapsing": fb.FBEventTree,
        "OnDblClick": fb.FBEventTreeSelect,
        "OnDragAndDrop": fb.FBEventDragAndDrop,
        "OnExpanded": fb.FBEventTree,
        "OnExpanding": fb.FBEventTree,
    },
    fb.FBSpreadCell: {
        "OnCellChange": fb.FBEventSpread,
        "OnColumnClick": fb.FBEventSpread,
        "OnRowClick": fb.FBEventSpread,
        "OnDragAndDrop": fb.FBEventDragAndDrop,
    },
    fb.FBSlider: {
        "OnTransaction": fb.FBEventTransaction,
    },
    fb.FBList: {
        "OnDragAndDrop": fb.FBEventDragAndDrop,
    },
    fb.FBLayout: {
        "OnResize": fb.FBEventResize,
        "OnShow": fb.FBEventShow,
        "OnInput": fb.FBEventInput,
        "OnPaint": fb.FBEventExpose,
    }
}


class PluginEvents(PluginBaseClass):
    Threading = False
    Priority = 100

    def PatchClass(self, Class: StubClass):
        for Property in Class.StubProperties:
            if Property.Type == 'callbackframework.FBEventSource' or Property.Name == "OnUnbind":
                Event = fb.FBEvent
                if Class.Ref in EVENTS:
                    for EventName, EventType in EVENTS[Class.Ref].items():
                        if Property.Name == EventName:
                            Event = EventType
                            break

                Property.Type = f'callbackframework.FBEventSource[{Class.Name}, {Event.__name__}]'

        # FBEventTree.Why has a event that's not exposed to the Python API
        if Class.Ref is fb.FBEventTree:
            WhyProperty = Class.GetPropertyByName('Why')
            if WhyProperty:
                WhyProperty.Type = None
