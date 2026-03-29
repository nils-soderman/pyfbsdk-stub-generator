"""
Stub file generated for MotionBuilder {MOTIONBUILDER_VERSION} using:
https://github.com/nils-soderman/pyfbsdk-stub-generator
"""
from __future__ import annotations
from enum import EnumMeta as __EnumMeta
from typing import overload, Any, Iterator, Literal, Self
from warnings import deprecated
import callbackframework
class Enumeration(int, metaclass=__EnumMeta):
	__slots__:tuple
	names:dict[str, Self]
	values:dict[int, Self]
	@overload
	def __init__(self,value:str|int=0,/):...
	@overload
	def __init__(self,value:str|bytes|bytearray,/,base:int): ...
