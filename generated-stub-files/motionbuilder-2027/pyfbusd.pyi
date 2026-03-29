"""
Stub file generated for MotionBuilder 2027 using:
https://github.com/nils-soderman/pyfbsdk-stub-generator
"""
from __future__ import annotations
import pyfbsdk

class FBUsdStageProxy(pyfbsdk.FBModel):
	FilePath:str
	"""The file path of the USD stage."""
	FrameOffset:pyfbsdk.FBPropertyAnimatableInt
	"""The frame offset applied to the USD stage."""
	def __init__(self,Name:str,/):...
	def Reload(self)->None:...
def CreateUsdStageProxy(Name:str,/)->FBUsdStageProxy:...
def ORUsdStageProxy_TypeInfo()->int:...

