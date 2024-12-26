"""
Stub file generated for MotionBuilder 2025 using:
https://github.com/nils-soderman/pyfbsdk-stub-generator
"""
from __future__ import annotations

import pyfbsdk


# TypeVar and Protocol(s) not actually in the source code
import typing

__FBPlugType_T = typing.TypeVar('__FBPlugType_T', bound=pyfbsdk.FBPythonWrapper)
__FBEvent_T = typing.TypeVar('__FBEvent_T', bound=pyfbsdk.FBEvent)

class __HasType(typing.Protocol):
    @property
    def Type(self) -> typing.Any:
        ...

# Stub for callbackframework.py

def GetFBEventSource(source: pyfbsdk.FBPlug, eventtype: pyfbsdk.FBEventName) -> FBEventSource:
   ...

def RemoveAllEvents(source: typing.Any) -> None:
   ...

def GetEventSource(source: typing.Any, eventtype: typing.Any) -> EventSource:
   ...

def NotifyEventSource(source: typing.Any, event: __HasType) -> None:
   ...

class EventSource:
    callbacks: list[typing.Callable] = []
    control: typing.Any
    eventtype: typing.Any

    def __init__(self, control: typing.Any, eventtype: typing.Any):
        ...

    def Add(self, toCall: typing.Callable[[typing.Any, typing.Any], typing.Any]) -> None:
        ...

    def Remove(self, toRemove: typing.Callable[[typing.Any, typing.Any], typing.Any]) -> None:
        ...

    def RemoveAll(self) -> None:
        ...

    def Notify(self, event: __HasType) -> None:
        ...

class FBEventSource(typing.Generic[__FBPlugType_T, __FBEvent_T], EventSource):
    callbacks: list[pyfbsdk.FBCallback] = []
    control: __FBPlugType_T
    eventtype: pyfbsdk.FBEventName

    def __init__(self, control: __FBPlugType_T, eventtype: pyfbsdk.FBEventName):
        ...

    def Add(self, toCall: typing.Callable[[__FBPlugType_T, __FBEvent_T], typing.Any]) -> None:
        ...

    def Remove(self, toRemove: typing.Callable[[__FBPlugType_T, __FBEvent_T], typing.Any]) -> None:
        ...

    def Notify(self, event: __FBEvent_T) -> None:
        ...
