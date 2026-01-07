"""
This module patches the callbackframework.FBEventSource properties to have the correct parameter types for various events in the pyfbsdk library.
"""

from __future__ import annotations

import pyfbsdk as fb

from ..plugin_base import PluginBaseClass
from ...module_types import StubClass


EVENTS = {
    fb.FBApplication.OnOverrideFileOpen: fb.FBEventOverrideFileOpen,

    fb.FBEvaluateManager.OnSynchronizationEvent: fb.FBEventEvalGlobalCallback,
    fb.FBEvaluateManager.OnRenderingPipelineEvent: fb.FBEventEvalGlobalCallback,

    fb.FBFCurveEventManager.OnFCurveEvent: fb.FBFCurveEvent,
    fb.FBFCurveEventManager.OnPropertyEvent: fb.FBPropertyStateEvent,

    fb.FBFileMonitoringManager.OnFileChangeAnimationClip: fb.FBEventFileChange,
    fb.FBFileMonitoringManager.OnFileChangeFileReference: fb.FBEventFileChange,
    fb.FBFileMonitoringManager.OnFileChangeMainScene: fb.FBEventFileChange,
    fb.FBFileMonitoringManager.OnFileChangePythonEditorScript: fb.FBEventFileChange,

    fb.FBGenericMenu.OnMenuActivate: fb.FBEventMenu,

    fb.FBPlayerControl.OnChange: fb.FBEventPlayerControlChange,

    fb.FBScene.OnChange: fb.FBEventSceneChange,
    fb.FBScene.OnTakeChange: fb.FBEventTakeChange,

    fb.FBStoryClip.OnChange: fb.FBEventClipChange,

    fb.FBSystem.OnConnectionDataNotify: fb.FBEventConnectionDataNotify,
    fb.FBSystem.OnConnectionKeyingNotify: fb.FBEventConnectionKeyingNotify,
    fb.FBSystem.OnConnectionNotify: fb.FBEventConnectionNotify,
    fb.FBSystem.OnConnectionStateNotify: fb.FBEventConnectionStateNotify,
    fb.FBSystem.OnVideoFrameRendering: fb.FBEventVideoFrameRendering,

    fb.FBVisualContainer.OnDblClick: fb.FBEventDblClick,
    fb.FBVisualContainer.OnDragAndDrop: fb.FBEventDragAndDrop,

    fb.FBButton.OnClick: fb.FBEventActivate,

    fb.FBTree.OnSelect: fb.FBEventTreeSelect,
    fb.FBTree.OnClickCheck: fb.FBEventTreeSelect,
    fb.FBTree.OnCollapsed: fb.FBEventTree,
    fb.FBTree.OnCollapsing: fb.FBEventTree,
    fb.FBTree.OnDblClick: fb.FBEventTreeSelect,
    fb.FBTree.OnDragAndDrop: fb.FBEventDragAndDrop,
    fb.FBTree.OnExpanded: fb.FBEventTree,
    fb.FBTree.OnExpanding: fb.FBEventTree,

    fb.FBSpread.OnCellChange: fb.FBEventSpread,
    fb.FBSpread.OnColumnClick: fb.FBEventSpread,
    fb.FBSpread.OnRowClick: fb.FBEventSpread,
    fb.FBSpread.OnDragAndDrop: fb.FBEventDragAndDrop,

    fb.FBSlider.OnTransaction: fb.FBEventTransaction,

    fb.FBList.OnDragAndDrop: fb.FBEventDragAndDrop,

    fb.FBLayout.OnResize: fb.FBEventResize,
    fb.FBLayout.OnShow: fb.FBEventShow,
    fb.FBLayout.OnInput: fb.FBEventInput,
    fb.FBLayout.OnPaint: fb.FBEventExpose,
}


class PluginEvents(PluginBaseClass):
    Priority = 100

    def PatchClass(self, Class: StubClass):
        for Property in Class.StubProperties:
            if Property.Type == 'callbackframework.FBEventSource':
                Event = fb.FBEvent
                if Property.Ref in EVENTS:
                    Event = EVENTS[Property.Ref]

                Property.Type = f'callbackframework.FBEventSource[Self, {Event.__name__}]'

        # If FBEvent.Type doesn't have a defined type, remove it.
        # It's already defined in the base class as a int.
        if fb.FBEvent.__name__ in Class.Parents:
            TypeProperty = Class.GetPropertyByName('Type')
            if TypeProperty and TypeProperty.Type == property.__name__:
                Class.StubProperties.remove(TypeProperty)

            # FBEventTree.Why has a event that's not exposed to the Python API
            if Class.Ref is fb.FBEventTree:
                WhyProperty = Class.GetPropertyByName('Why')
                if WhyProperty:
                    WhyProperty.Type = None
