"""
Stub file generated for MotionBuilder {MOTIONBUILDER_VERSION} using:
https://github.com/nils-soderman/pyfbsdk-stub-generator
"""
# pylint: disable=all
from __future__ import annotations
from typing import overload, Any, Iterator, Literal, Self
import callbackframework
from enum import EnumMeta as __EnumMeta
class Enumeration(int, metaclass=__EnumMeta):
	__slots__:tuple
	names:dict
	values:dict
	@overload
	def __init__(self,value:str|int=0,/):...
	@overload
	def __init__(self,value:str|bytes|bytearray,/,base:int): ...
