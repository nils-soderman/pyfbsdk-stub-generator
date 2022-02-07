from __future__ import annotations
from typing import List, overload
class _Enum:
    __slots__:tuple
    names:dict
    values:dict
class ETimeFormats:...
class FBAccessMode(_Enum):
    kFBAccessModeDisk:FBAccessMode
    kFBAccessModeMemory:FBAccessMode
class FBAlphaSource(_Enum):
    kFBAlphaSource2DTransparency:FBAlphaSource
    kFBAlphaSourceAccurateAlpha:FBAlphaSource
    kFBAlphaSourceAdditiveAlpha:FBAlphaSource
    kFBAlphaSourceMatteAlpha:FBAlphaSource
    kFBAlphaSourceNoAlpha:FBAlphaSource
    kFBAlphaSourceTransluscentAlpha:FBAlphaSource
    kFBAlphaSourceTransluscentZSortAlpha:FBAlphaSource
class FBAnimationLayerMergeOptions(_Enum):
    kFBAnimLayerMerge_AllLayers_AllProperties:FBAnimationLayerMergeOptions
    kFBAnimLayerMerge_AllLayers_CompleteScene:FBAnimationLayerMergeOptions
    kFBAnimLayerMerge_AllLayers_SelectedProperties:FBAnimationLayerMergeOptions
    kFBAnimLayerMerge_SelectedLayers_AllProperties:FBAnimationLayerMergeOptions
    kFBAnimLayerMerge_SelectedLayers_CompleteScene:FBAnimationLayerMergeOptions
    kFBAnimLayerMerge_SelectedLayers_SelectedProperties:FBAnimationLayerMergeOptions
class FBAnimationNodeConnectorType(_Enum):
    kFBAnimationNodeConnectorTypeConnectedIn:FBAnimationNodeConnectorType
    kFBAnimationNodeConnectorTypeConnectedOut:FBAnimationNodeConnectorType
    kFBAnimationNodeConnectorTypeConstantIn:FBAnimationNodeConnectorType
    kFBAnimationNodeConnectorTypeNone:FBAnimationNodeConnectorType
class FBArrangeMode(_Enum):
    kHorizontalMode:FBArrangeMode
    kVerticalMode:FBArrangeMode
class FBAssetMngFileOptions(_Enum):
    kFileAddOnNewSave:FBAssetMngFileOptions
    kFileAddOnNewSave_Ask:FBAssetMngFileOptions
    kFileCheckInOnClose:FBAssetMngFileOptions
    kFileCheckInOnClose_Ask:FBAssetMngFileOptions
    kFileCheckOutOnLoad:FBAssetMngFileOptions
    kFileCheckOutOnLoad_Ask:FBAssetMngFileOptions
    kFileOptionsAll:FBAssetMngFileOptions
    kFileUploadOnSave:FBAssetMngFileOptions
    kFileUploadOnSave_Ask:FBAssetMngFileOptions
class FBAssetMngMenuOptions(_Enum):
    kMenuAddToDatabase:FBAssetMngMenuOptions
    kMenuAll:FBAssetMngMenuOptions
    kMenuCheckIn:FBAssetMngMenuOptions
    kMenuCheckOut:FBAssetMngMenuOptions
    kMenuEnable:FBAssetMngMenuOptions
    kMenuFileAll:FBAssetMngMenuOptions
    kMenuGetLatest:FBAssetMngMenuOptions
    kMenuOpenFromDatabase:FBAssetMngMenuOptions
    kMenuShowExplorer:FBAssetMngMenuOptions
    kMenuShowHistory:FBAssetMngMenuOptions
    kMenuShowProperties:FBAssetMngMenuOptions
    kMenuShowReferenceMng:FBAssetMngMenuOptions
    kMenuShowSettings:FBAssetMngMenuOptions
    kMenuSourceControlAll:FBAssetMngMenuOptions
    kMenuSourceControlMin:FBAssetMngMenuOptions
    kMenuUndoCheckOut:FBAssetMngMenuOptions
    kMenuUploadToDatabase:FBAssetMngMenuOptions
class FBAttachType(_Enum):
    kFBAttachBottom:FBAttachType
    kFBAttachCenter:FBAttachType
    kFBAttachHeight:FBAttachType
    kFBAttachLeft:FBAttachType
    kFBAttachNone:FBAttachType
    kFBAttachRight:FBAttachType
    kFBAttachTop:FBAttachType
    kFBAttachWidth:FBAttachType
class FBAttenuationType(_Enum):
    kFBAttenuationCubic:FBAttenuationType
    kFBAttenuationLinear:FBAttenuationType
    kFBAttenuationNone:FBAttenuationType
    kFBAttenuationQuadratic:FBAttenuationType
class FBAudioBitDepthMode(_Enum):
    kFBAudioBitDepthMode_16:FBAudioBitDepthMode
    kFBAudioBitDepthMode_24:FBAudioBitDepthMode
    kFBAudioBitDepthMode_8:FBAudioBitDepthMode
    kFBAudioBitDepthMode_FP:FBAudioBitDepthMode
class FBAudioChannelMode(_Enum):
    kFBAudioChannelModeMono:FBAudioChannelMode
    kFBAudioChannelModeStereo:FBAudioChannelMode
    kFBAudioChannelMode_4:FBAudioChannelMode
    kFBAudioChannelMode_8:FBAudioChannelMode
class FBAudioOutputLocation(_Enum):
    FBAudioOutputLocationCount:FBAudioOutputLocation
    FBAudioOutputLocationEmbedded:FBAudioOutputLocation
    FBAudioOutputLocationEmbeddedAndStandalone:FBAudioOutputLocation
    FBAudioOutputLocationStandalone:FBAudioOutputLocation
class FBAudioRateMode(_Enum):
    kFBAudioRateMode_100000:FBAudioRateMode
    kFBAudioRateMode_12000:FBAudioRateMode
    kFBAudioRateMode_12500:FBAudioRateMode
    kFBAudioRateMode_16000:FBAudioRateMode
    kFBAudioRateMode_22050:FBAudioRateMode
    kFBAudioRateMode_24000:FBAudioRateMode
    kFBAudioRateMode_25000:FBAudioRateMode
    kFBAudioRateMode_32000:FBAudioRateMode
    kFBAudioRateMode_44100:FBAudioRateMode
    kFBAudioRateMode_48000:FBAudioRateMode
    kFBAudioRateMode_50000:FBAudioRateMode
    kFBAudioRateMode_64000:FBAudioRateMode
    kFBAudioRateMode_8000:FBAudioRateMode
    kFBAudioRateMode_88200:FBAudioRateMode
    kFBAudioRateMode_96000:FBAudioRateMode
    kFBRAudioateMode_11025:FBAudioRateMode
class FBBatchFileFormat(_Enum):
    kFBBatchFileFormatAMC:FBBatchFileFormat
    kFBBatchFileFormatBVH:FBBatchFileFormat
    kFBBatchFileFormatC3D:FBBatchFileFormat
    kFBBatchFileFormatFBX:FBBatchFileFormat
    kFBBatchFileFormatHTR:FBBatchFileFormat
    kFBBatchFileFormatTRC:FBBatchFileFormat
class FBBatchOnContainsBatchTakes(_Enum):
    kFBBatchOnContainsBatchTakesSaveAllTakes:FBBatchOnContainsBatchTakes
    kFBBatchOnContainsBatchTakesSaveBatchTakesOnly:FBBatchOnContainsBatchTakes
class FBBatchOnTakeExist(_Enum):
    kFBBatchOnTakeExistOverwrite:FBBatchOnTakeExist
    kFBBatchOnTakeExistSkip:FBBatchOnTakeExist
class FBBatchProcessType(_Enum):
    kFBBatchProcessTypeConvert:FBBatchProcessType
    kFBBatchProcessTypeLoad:FBBatchProcessType
    kFBBatchProcessTypeSave:FBBatchProcessType
class FBBatchStatus(_Enum):
    kFBBatchStatusActorInputMarkersetHasNoReferenceModel:FBBatchStatus
    kFBBatchStatusActorInputMarkersetNotCorrectlyAssociated:FBBatchStatus
    kFBBatchStatusActorInputMarkersetNotSpecified:FBBatchStatus
    kFBBatchStatusAsfSkeletonFileNotSpecified:FBBatchStatus
    kFBBatchStatusCantOpenAsfSkeletonFile:FBBatchStatus
    kFBBatchStatusCharacterHasNoReference:FBBatchStatus
    kFBBatchStatusCharacterNotCharacterized:FBBatchStatus
    kFBBatchStatusCharacterNotSpecified:FBBatchStatus
    kFBBatchStatusError:FBBatchStatus
    kFBBatchStatusInputActorNotSpecified:FBBatchStatus
    kFBBatchStatusInputCharacterHasNoReference:FBBatchStatus
    kFBBatchStatusInputCharacterNotCharacterized:FBBatchStatus
    kFBBatchStatusInputDirectoryNotValid:FBBatchStatus
    kFBBatchStatusOutputDirectoryNotValid:FBBatchStatus
    kFBBatchStatusSuccess:FBBatchStatus
class FBBodyNodeId(_Enum):
    kFBChestNodeId:FBBodyNodeId
    kFBHeadNodeId:FBBodyNodeId
    kFBHipsNodeId:FBBodyNodeId
    kFBHipsTranslationNodeId:FBBodyNodeId
    kFBInvalidNodeId:FBBodyNodeId
    kFBLastNodeId:FBBodyNodeId
    kFBLastNodeId_Old:FBBodyNodeId
    kFBLeftAnkleNodeId:FBBodyNodeId
    kFBLeftCollarNodeId:FBBodyNodeId
    kFBLeftElbowNodeId:FBBodyNodeId
    kFBLeftElbowRollNode1Id:FBBodyNodeId
    kFBLeftElbowRollNode2Id:FBBodyNodeId
    kFBLeftElbowRollNode3Id:FBBodyNodeId
    kFBLeftElbowRollNode4Id:FBBodyNodeId
    kFBLeftElbowRollNode5Id:FBBodyNodeId
    kFBLeftElbowRollNodeId:FBBodyNodeId
    kFBLeftExtraFingerANodeId:FBBodyNodeId
    kFBLeftExtraFingerBNodeId:FBBodyNodeId
    kFBLeftExtraFingerCNodeId:FBBodyNodeId
    kFBLeftExtraFingerDNodeId:FBBodyNodeId
    kFBLeftExtraFingerInNodeId:FBBodyNodeId
    kFBLeftExtraFootFingerANodeId:FBBodyNodeId
    kFBLeftExtraFootFingerBNodeId:FBBodyNodeId
    kFBLeftExtraFootFingerCNodeId:FBBodyNodeId
    kFBLeftExtraFootFingerDNodeId:FBBodyNodeId
    kFBLeftExtraFootFingerInNodeId:FBBodyNodeId
    kFBLeftFootIndexANodeId:FBBodyNodeId
    kFBLeftFootIndexBNodeId:FBBodyNodeId
    kFBLeftFootIndexCNodeId:FBBodyNodeId
    kFBLeftFootIndexDNodeId:FBBodyNodeId
    kFBLeftFootIndexInNodeId:FBBodyNodeId
    kFBLeftFootMiddleANodeId:FBBodyNodeId
    kFBLeftFootMiddleBNodeId:FBBodyNodeId
    kFBLeftFootMiddleCNodeId:FBBodyNodeId
    kFBLeftFootMiddleDNodeId:FBBodyNodeId
    kFBLeftFootMiddleInNodeId:FBBodyNodeId
    kFBLeftFootNodeId:FBBodyNodeId
    kFBLeftFootPinkyANodeId:FBBodyNodeId
    kFBLeftFootPinkyBNodeId:FBBodyNodeId
    kFBLeftFootPinkyCNodeId:FBBodyNodeId
    kFBLeftFootPinkyDNodeId:FBBodyNodeId
    kFBLeftFootPinkyInNodeId:FBBodyNodeId
    kFBLeftFootRingANodeId:FBBodyNodeId
    kFBLeftFootRingBNodeId:FBBodyNodeId
    kFBLeftFootRingCNodeId:FBBodyNodeId
    kFBLeftFootRingDNodeId:FBBodyNodeId
    kFBLeftFootRingInNodeId:FBBodyNodeId
    kFBLeftFootThumbANodeId:FBBodyNodeId
    kFBLeftFootThumbBNodeId:FBBodyNodeId
    kFBLeftFootThumbCNodeId:FBBodyNodeId
    kFBLeftFootThumbDNodeId:FBBodyNodeId
    kFBLeftFootThumbInNodeId:FBBodyNodeId
    kFBLeftHandNodeId:FBBodyNodeId
    kFBLeftHipNodeId:FBBodyNodeId
    kFBLeftHipRollNode1Id:FBBodyNodeId
    kFBLeftHipRollNode2Id:FBBodyNodeId
    kFBLeftHipRollNode3Id:FBBodyNodeId
    kFBLeftHipRollNode4Id:FBBodyNodeId
    kFBLeftHipRollNode5Id:FBBodyNodeId
    kFBLeftHipRollNodeId:FBBodyNodeId
    kFBLeftIndexANodeId:FBBodyNodeId
    kFBLeftIndexBNodeId:FBBodyNodeId
    kFBLeftIndexCNodeId:FBBodyNodeId
    kFBLeftIndexDNodeId:FBBodyNodeId
    kFBLeftIndexInNodeId:FBBodyNodeId
    kFBLeftKneeNodeId:FBBodyNodeId
    kFBLeftKneeRollNode1Id:FBBodyNodeId
    kFBLeftKneeRollNode2Id:FBBodyNodeId
    kFBLeftKneeRollNode3Id:FBBodyNodeId
    kFBLeftKneeRollNode4Id:FBBodyNodeId
    kFBLeftKneeRollNode5Id:FBBodyNodeId
    kFBLeftKneeRollNodeId:FBBodyNodeId
    kFBLeftMiddleANodeId:FBBodyNodeId
    kFBLeftMiddleBNodeId:FBBodyNodeId
    kFBLeftMiddleCNodeId:FBBodyNodeId
    kFBLeftMiddleDNodeId:FBBodyNodeId
    kFBLeftMiddleInNodeId:FBBodyNodeId
    kFBLeftPinkyANodeId:FBBodyNodeId
    kFBLeftPinkyBNodeId:FBBodyNodeId
    kFBLeftPinkyCNodeId:FBBodyNodeId
    kFBLeftPinkyDNodeId:FBBodyNodeId
    kFBLeftPinkyInNodeId:FBBodyNodeId
    kFBLeftRingANodeId:FBBodyNodeId
    kFBLeftRingBNodeId:FBBodyNodeId
    kFBLeftRingCNodeId:FBBodyNodeId
    kFBLeftRingDNodeId:FBBodyNodeId
    kFBLeftRingInNodeId:FBBodyNodeId
    kFBLeftShoulderNodeId:FBBodyNodeId
    kFBLeftShoulderRollNode1Id:FBBodyNodeId
    kFBLeftShoulderRollNode2Id:FBBodyNodeId
    kFBLeftShoulderRollNode3Id:FBBodyNodeId
    kFBLeftShoulderRollNode4Id:FBBodyNodeId
    kFBLeftShoulderRollNode5Id:FBBodyNodeId
    kFBLeftShoulderRollNodeId:FBBodyNodeId
    kFBLeftThumbANodeId:FBBodyNodeId
    kFBLeftThumbBNodeId:FBBodyNodeId
    kFBLeftThumbCNodeId:FBBodyNodeId
    kFBLeftThumbDNodeId:FBBodyNodeId
    kFBLeftThumbInNodeId:FBBodyNodeId
    kFBLeftWristNodeId:FBBodyNodeId
    kFBNeck1NodeId:FBBodyNodeId
    kFBNeck2NodeId:FBBodyNodeId
    kFBNeck3NodeId:FBBodyNodeId
    kFBNeck4NodeId:FBBodyNodeId
    kFBNeck5NodeId:FBBodyNodeId
    kFBNeck6NodeId:FBBodyNodeId
    kFBNeck7NodeId:FBBodyNodeId
    kFBNeck8NodeId:FBBodyNodeId
    kFBNeck9NodeId:FBBodyNodeId
    kFBNeckNodeId:FBBodyNodeId
    kFBReferenceNodeId:FBBodyNodeId
    kFBRightAnkleNodeId:FBBodyNodeId
    kFBRightCollarNodeId:FBBodyNodeId
    kFBRightElbowNodeId:FBBodyNodeId
    kFBRightElbowRollNode1Id:FBBodyNodeId
    kFBRightElbowRollNode2Id:FBBodyNodeId
    kFBRightElbowRollNode3Id:FBBodyNodeId
    kFBRightElbowRollNode4Id:FBBodyNodeId
    kFBRightElbowRollNode5Id:FBBodyNodeId
    kFBRightElbowRollNodeId:FBBodyNodeId
    kFBRightExtraFingerANodeId:FBBodyNodeId
    kFBRightExtraFingerBNodeId:FBBodyNodeId
    kFBRightExtraFingerCNodeId:FBBodyNodeId
    kFBRightExtraFingerDNodeId:FBBodyNodeId
    kFBRightExtraFingerInNodeId:FBBodyNodeId
    kFBRightExtraFootFingerANodeId:FBBodyNodeId
    kFBRightExtraFootFingerBNodeId:FBBodyNodeId
    kFBRightExtraFootFingerCNodeId:FBBodyNodeId
    kFBRightExtraFootFingerDNodeId:FBBodyNodeId
    kFBRightExtraFootFingerInNodeId:FBBodyNodeId
    kFBRightFootIndexANodeId:FBBodyNodeId
    kFBRightFootIndexBNodeId:FBBodyNodeId
    kFBRightFootIndexCNodeId:FBBodyNodeId
    kFBRightFootIndexDNodeId:FBBodyNodeId
    kFBRightFootIndexInNodeId:FBBodyNodeId
    kFBRightFootMiddleANodeId:FBBodyNodeId
    kFBRightFootMiddleBNodeId:FBBodyNodeId
    kFBRightFootMiddleCNodeId:FBBodyNodeId
    kFBRightFootMiddleDNodeId:FBBodyNodeId
    kFBRightFootMiddleInNodeId:FBBodyNodeId
    kFBRightFootNodeId:FBBodyNodeId
    kFBRightFootPinkyANodeId:FBBodyNodeId
    kFBRightFootPinkyBNodeId:FBBodyNodeId
    kFBRightFootPinkyCNodeId:FBBodyNodeId
    kFBRightFootPinkyDNodeId:FBBodyNodeId
    kFBRightFootPinkyInNodeId:FBBodyNodeId
    kFBRightFootRingANodeId:FBBodyNodeId
    kFBRightFootRingBNodeId:FBBodyNodeId
    kFBRightFootRingCNodeId:FBBodyNodeId
    kFBRightFootRingDNodeId:FBBodyNodeId
    kFBRightFootRingInNodeId:FBBodyNodeId
    kFBRightFootThumbANodeId:FBBodyNodeId
    kFBRightFootThumbBNodeId:FBBodyNodeId
    kFBRightFootThumbCNodeId:FBBodyNodeId
    kFBRightFootThumbDNodeId:FBBodyNodeId
    kFBRightFootThumbInNodeId:FBBodyNodeId
    kFBRightHandNodeId:FBBodyNodeId
    kFBRightHipNodeId:FBBodyNodeId
    kFBRightHipRollNode1Id:FBBodyNodeId
    kFBRightHipRollNode2Id:FBBodyNodeId
    kFBRightHipRollNode3Id:FBBodyNodeId
    kFBRightHipRollNode4Id:FBBodyNodeId
    kFBRightHipRollNode5Id:FBBodyNodeId
    kFBRightHipRollNodeId:FBBodyNodeId
    kFBRightIndexANodeId:FBBodyNodeId
    kFBRightIndexBNodeId:FBBodyNodeId
    kFBRightIndexCNodeId:FBBodyNodeId
    kFBRightIndexDNodeId:FBBodyNodeId
    kFBRightIndexInNodeId:FBBodyNodeId
    kFBRightKneeNodeId:FBBodyNodeId
    kFBRightKneeRollNode1Id:FBBodyNodeId
    kFBRightKneeRollNode2Id:FBBodyNodeId
    kFBRightKneeRollNode3Id:FBBodyNodeId
    kFBRightKneeRollNode4Id:FBBodyNodeId
    kFBRightKneeRollNode5Id:FBBodyNodeId
    kFBRightKneeRollNodeId:FBBodyNodeId
    kFBRightMiddleANodeId:FBBodyNodeId
    kFBRightMiddleBNodeId:FBBodyNodeId
    kFBRightMiddleCNodeId:FBBodyNodeId
    kFBRightMiddleDNodeId:FBBodyNodeId
    kFBRightMiddleInNodeId:FBBodyNodeId
    kFBRightPinkyANodeId:FBBodyNodeId
    kFBRightPinkyBNodeId:FBBodyNodeId
    kFBRightPinkyCNodeId:FBBodyNodeId
    kFBRightPinkyDNodeId:FBBodyNodeId
    kFBRightPinkyInNodeId:FBBodyNodeId
    kFBRightRingANodeId:FBBodyNodeId
    kFBRightRingBNodeId:FBBodyNodeId
    kFBRightRingCNodeId:FBBodyNodeId
    kFBRightRingDNodeId:FBBodyNodeId
    kFBRightRingInNodeId:FBBodyNodeId
    kFBRightShoulderNodeId:FBBodyNodeId
    kFBRightShoulderRollNode1Id:FBBodyNodeId
    kFBRightShoulderRollNode2Id:FBBodyNodeId
    kFBRightShoulderRollNode3Id:FBBodyNodeId
    kFBRightShoulderRollNode4Id:FBBodyNodeId
    kFBRightShoulderRollNode5Id:FBBodyNodeId
    kFBRightShoulderRollNodeId:FBBodyNodeId
    kFBRightThumbANodeId:FBBodyNodeId
    kFBRightThumbBNodeId:FBBodyNodeId
    kFBRightThumbCNodeId:FBBodyNodeId
    kFBRightThumbDNodeId:FBBodyNodeId
    kFBRightThumbInNodeId:FBBodyNodeId
    kFBRightWristNodeId:FBBodyNodeId
    kFBSpine2NodeId:FBBodyNodeId
    kFBSpine3NodeId:FBBodyNodeId
    kFBSpine4NodeId:FBBodyNodeId
    kFBSpine5NodeId:FBBodyNodeId
    kFBSpine6NodeId:FBBodyNodeId
    kFBSpine7NodeId:FBBodyNodeId
    kFBSpine8NodeId:FBBodyNodeId
    kFBSpine9NodeId:FBBodyNodeId
    kFBWaistNodeId:FBBodyNodeId
class FBBodyPartId(_Enum):
    kFBCtrlSetPartChest:FBBodyPartId
    kFBCtrlSetPartHead:FBBodyPartId
    kFBCtrlSetPartHips:FBBodyPartId
    kFBCtrlSetPartLeftArm:FBBodyPartId
    kFBCtrlSetPartLeftFoot:FBBodyPartId
    kFBCtrlSetPartLeftHand:FBBodyPartId
    kFBCtrlSetPartLeftLeg:FBBodyPartId
    kFBCtrlSetPartNone:FBBodyPartId
    kFBCtrlSetPartRightArm:FBBodyPartId
    kFBCtrlSetPartRightFoot:FBBodyPartId
    kFBCtrlSetPartRightHand:FBBodyPartId
    kFBCtrlSetPartRightLeg:FBBodyPartId
    kFBLastCtrlSetPartIndex:FBBodyPartId
class FBBorderStyle(_Enum):
    kFBEmbossBorder:FBBorderStyle
    kFBEmbossEdgeSmoothBorder:FBBorderStyle
    kFBEmbossSmoothBorder:FBBorderStyle
    kFBEmbossSmoothEdgeBorder:FBBorderStyle
    kFBHighlightBorder:FBBorderStyle
    kFBNoBorder:FBBorderStyle
    kFBPickingBorder:FBBorderStyle
    kFBStandardBorder:FBBorderStyle
    kFBStandardEdgeSmoothBorder:FBBorderStyle
    kFBStandardSmoothBorder:FBBorderStyle
    kFBStandardSmoothEdgeBorder:FBBorderStyle
class FBButtonLook(_Enum):
    kFBLookAlphaBackground:FBButtonLook
    kFBLookColorChange:FBButtonLook
    kFBLookFlat:FBButtonLook
    kFBLookNormal:FBButtonLook
    kFBLookPush:FBButtonLook
class FBButtonState(_Enum):
    kFBButtonState0:FBButtonState
    kFBButtonState1:FBButtonState
class FBButtonStyle(_Enum):
    kFB2States:FBButtonStyle
    kFBBitmap2States:FBButtonStyle
    kFBBitmapButton:FBButtonStyle
    kFBCheckbox:FBButtonStyle
    kFBPushButton:FBButtonStyle
    kFBRadioButton:FBButtonStyle
class FBCameraAntiAliasingMethod(_Enum):
    kFBAntiAliasingSoftware:FBCameraAntiAliasingMethod
    kFBAntialiasingMultiSamplingOnyx:FBCameraAntiAliasingMethod
class FBCameraApertureMode(_Enum):
    kFBApertureFocalLength:FBCameraApertureMode
    kFBApertureHorizontal:FBCameraApertureMode
    kFBApertureVertHoriz:FBCameraApertureMode
    kFBApertureVertical:FBCameraApertureMode
class FBCameraDistanceMode(_Enum):
    kFBDistModeAbsoluteFromCamera:FBCameraDistanceMode
    kFBDistModeRelativeToInterest:FBCameraDistanceMode
class FBCameraFilmBackType(_Enum):
    kFBFilmBack16mmTheatrical:FBCameraFilmBackType
    kFBFilmBack35mm185Projection:FBCameraFilmBackType
    kFBFilmBack35mmAcademy:FBCameraFilmBackType
    kFBFilmBack35mmAnamorphic:FBCameraFilmBackType
    kFBFilmBack35mmFullAperture:FBCameraFilmBackType
    kFBFilmBack35mmTVProjection:FBCameraFilmBackType
    kFBFilmBack70mmProjection:FBCameraFilmBackType
    kFBFilmBackCustom:FBCameraFilmBackType
    kFBFilmBackDynavision:FBCameraFilmBackType
    kFBFilmBackIMAX:FBCameraFilmBackType
    kFBFilmBackSuper16mm:FBCameraFilmBackType
    kFBFilmBackVistaVision:FBCameraFilmBackType
class FBCameraFocusDistanceSource(_Enum):
    kFBFocusDistanceCameraInterest:FBCameraFocusDistanceSource
    kFBFocusDistanceModel:FBCameraFocusDistanceSource
    kFBFocusDistanceSpecificDistance:FBCameraFocusDistanceSource
class FBCameraFrameSizeMode(_Enum):
    kFBFrameSizeFixedHeightResolution:FBCameraFrameSizeMode
    kFBFrameSizeFixedRatio:FBCameraFrameSizeMode
    kFBFrameSizeFixedResolution:FBCameraFrameSizeMode
    kFBFrameSizeFixedWidthResolution:FBCameraFrameSizeMode
    kFBFrameSizeWindow:FBCameraFrameSizeMode
class FBCameraMatrixType(_Enum):
    kFBModelView:FBCameraMatrixType
    kFBModelViewProj:FBCameraMatrixType
    kFBProjInverse:FBCameraMatrixType
    kFBProjection:FBCameraMatrixType
class FBCameraResolutionMode(_Enum):
    kFBResolution128x128:FBCameraResolutionMode
    kFBResolution320x200:FBCameraResolutionMode
    kFBResolution320x240:FBCameraResolutionMode
    kFBResolution640x480:FBCameraResolutionMode
    kFBResolutionCustom:FBCameraResolutionMode
    kFBResolutionD1NTSC:FBCameraResolutionMode
    kFBResolutionD1PAL:FBCameraResolutionMode
    kFBResolutionFullScreen:FBCameraResolutionMode
    kFBResolutionHD:FBCameraResolutionMode
    kFBResolutionNTSC:FBCameraResolutionMode
    kFBResolutionPAL:FBCameraResolutionMode
class FBCameraSafeAreaMode(_Enum):
    kFBSafeAreaRound:FBCameraSafeAreaMode
    kFBSafeAreaSquare:FBCameraSafeAreaMode
class FBCameraSamplingType(_Enum):
    kFBSamplingStochastic:FBCameraSamplingType
    kFBSamplingUniform:FBCameraSamplingType
class FBCameraStereoType(_Enum):
    kFBCameraStereoConverged:FBCameraStereoType
    kFBCameraStereoNone:FBCameraStereoType
    kFBCameraStereoOff_Axis:FBCameraStereoType
    kFBCameraStereoParallel:FBCameraStereoType
class FBCameraType(_Enum):
    kFBCameraTypeOrthogonal:FBCameraType
    kFBCameraTypePerspective:FBCameraType
class FBCameraViewPlaneMode(_Enum):
    kFBViewPlaneAlways:FBCameraViewPlaneMode
    kFBViewPlaneDisabled:FBCameraViewPlaneMode
    kFBViewPlaneWhenMedia:FBCameraViewPlaneMode
class FBCellStyle(_Enum):
    kFBCellStyle2StatesButton:FBCellStyle
    kFBCellStyle3StatesButton:FBCellStyle
    kFBCellStyleButton:FBCellStyle
    kFBCellStyleDefault:FBCellStyle
    kFBCellStyleDouble:FBCellStyle
    kFBCellStyleInteger:FBCellStyle
    kFBCellStyleMenu:FBCellStyle
    kFBCellStyleString:FBCellStyle
    kFBCellStyleTime:FBCellStyle
    kFBCellStyleView:FBCellStyle
    kFBCellStyleVoid:FBCellStyle
class FBCharacterContactBehaviour(_Enum):
    kFBLastContactBehaviour:FBCharacterContactBehaviour
    kFBParamContactAlwaysSync:FBCharacterContactBehaviour
    kFBParamContactNeverSync:FBCharacterContactBehaviour
    kFBParamContactSyncOnKey:FBCharacterContactBehaviour
class FBCharacterExtensionRetargetMode(_Enum):
    kFBRetargetModeAuto:FBCharacterExtensionRetargetMode
    kFBRetargetModeManual:FBCharacterExtensionRetargetMode
    kFBRetargetModeOff:FBCharacterExtensionRetargetMode
class FBCharacterExtensionStancePoseMode(_Enum):
    kFBStancePose_Always:FBCharacterExtensionStancePoseMode
    kFBStancePose_Never:FBCharacterExtensionStancePoseMode
    kFBStancePose_Reference_Selected:FBCharacterExtensionStancePoseMode
    kFBStancePose_Selected:FBCharacterExtensionStancePoseMode
    kFBStancePose_Self_Or_Reference_Selected:FBCharacterExtensionStancePoseMode
class FBCharacterHipsTranslationMode(_Enum):
    kFBLastHipsTranslationMode:FBCharacterHipsTranslationMode
    kFBParamHipsTranslationBodyRigid:FBCharacterHipsTranslationMode
    kFBParamHipsTranslationWorldRigid:FBCharacterHipsTranslationMode
class FBCharacterInputType(_Enum):
    kFBCharacterInputActor:FBCharacterInputType
    kFBCharacterInputCharacter:FBCharacterInputType
    kFBCharacterInputMarkerSet:FBCharacterInputType
    kFBCharacterInputMoCap:FBCharacterInputType
    kFBCharacterInputStance:FBCharacterInputType
    kFBCharacterOutputMarkerSet:FBCharacterInputType
class FBCharacterKeyingMode(_Enum):
    kFBCharacterKeyingBodyPart:FBCharacterKeyingMode
    kFBCharacterKeyingFullBody:FBCharacterKeyingMode
    kFBCharacterKeyingFullBodyNoPull:FBCharacterKeyingMode
    kFBCharacterKeyingSelection:FBCharacterKeyingMode
class FBCharacterLoadAnimationMethod(_Enum):
    kFBCharacterLoadConnect:FBCharacterLoadAnimationMethod
    kFBCharacterLoadCopy:FBCharacterLoadAnimationMethod
    kFBCharacterLoadPlot:FBCharacterLoadAnimationMethod
    kFBCharacterLoadPlotIfSampled:FBCharacterLoadAnimationMethod
    kFBCharacterLoadRetarget:FBCharacterLoadAnimationMethod
class FBCharacterPlotWhere(_Enum):
    kFBCharacterPlotOnControlRig:FBCharacterPlotWhere
    kFBCharacterPlotOnSkeleton:FBCharacterPlotWhere
class FBCharacterPoseFlag(_Enum):
    kFBCharacterPoseGravity:FBCharacterPoseFlag
    kFBCharacterPoseMatchFKTranslation:FBCharacterPoseFlag
    kFBCharacterPoseMatchPivot:FBCharacterPoseFlag
    kFBCharacterPoseMatchR:FBCharacterPoseFlag
    kFBCharacterPoseMatchTX:FBCharacterPoseFlag
    kFBCharacterPoseMatchTY:FBCharacterPoseFlag
    kFBCharacterPoseMatchTZ:FBCharacterPoseFlag
    kFBCharacterPoseMirror:FBCharacterPoseFlag
    kFBCharacterPoseNoFlag:FBCharacterPoseFlag
    kFBCharacterPoseUseKeyingGroup:FBCharacterPoseFlag
class FBCharacterPoseKeyingMode(_Enum):
    kFBCharacterPoseKeyingModeBodyPart:FBCharacterPoseKeyingMode
    kFBCharacterPoseKeyingModeCount:FBCharacterPoseKeyingMode
    kFBCharacterPoseKeyingModeFullBody:FBCharacterPoseKeyingMode
    kFBCharacterPoseKeyingModeInvalid:FBCharacterPoseKeyingMode
class FBCharacterResetProperties(_Enum):
    kFBCharacterResetPropertiesAll:FBCharacterResetProperties
    kFBCharacterResetPropertiesDefinition:FBCharacterResetProperties
    kFBCharacterResetPropertiesSolving:FBCharacterResetProperties
class FBCharacterRollSolver(_Enum):
    kFBLastRollSolver:FBCharacterRollSolver
    kFBParamRollSolver70:FBCharacterRollSolver
    kFBParamRollSolver75:FBCharacterRollSolver
class FBClipEnd(_Enum):
    kFBClipEndEnd:FBClipEnd
    kFBClipEndLoop:FBClipEnd
class FBClusterMode(_Enum):
    kFBClusterAdditive:FBClusterMode
    kFBClusterNormalize:FBClusterMode
    kFBClusterTotal100:FBClusterMode
class FBCommPortType(_Enum):
    kFBInternal:FBCommPortType
    kFBPhysical:FBCommPortType
    kFBVirtual:FBCommPortType
class FBCommType(_Enum):
    kFBCommTypeNetworkTCP:FBCommType
    kFBCommTypeNetworkUDP:FBCommType
    kFBCommTypeNone:FBCommType
    kFBCommTypeOther:FBCommType
    kFBCommTypeSerial:FBCommType
    kFBCommTypeSharedMemory:FBCommType
    kFBCommTypeSimulator:FBCommType
class FBCommandState(_Enum):
    kFBCommandStateMute:FBCommandState
    kFBCommandStateMuteBecauseSolo:FBCommandState
    kFBCommandStateSolo:FBCommandState
    kFBCommandStateStandard:FBCommandState
class FBConnectionAction(_Enum):
    kFBBeginChange:FBConnectionAction
    kFBBeginReplaceDst:FBConnectionAction
    kFBBeginReplaceSrc:FBConnectionAction
    kFBCandidate:FBConnectionAction
    kFBCandidateGlobal:FBConnectionAction
    kFBCandidated:FBConnectionAction
    kFBConnect:FBConnectionAction
    kFBConnectDst:FBConnectionAction
    kFBConnectSrc:FBConnectionAction
    kFBConnected:FBConnectionAction
    kFBConnectedDst:FBConnectionAction
    kFBConnectedOwner:FBConnectionAction
    kFBConnectedSrc:FBConnectionAction
    kFBDescription:FBConnectionAction
    kFBDestroy:FBConnectionAction
    kFBDetached:FBConnectionAction
    kFBDisconnect:FBConnectionAction
    kFBDisconnectDst:FBConnectionAction
    kFBDisconnectOwner:FBConnectionAction
    kFBDisconnectSrc:FBConnectionAction
    kFBDisconnected:FBConnectionAction
    kFBDisconnectedDst:FBConnectionAction
    kFBDisconnectedSrc:FBConnectionAction
    kFBEndChange:FBConnectionAction
    kFBEndReplaceDst:FBConnectionAction
    kFBEndReplaceSrc:FBConnectionAction
    kFBKeyingCandidate:FBConnectionAction
    kFBKeyingCurveChange:FBConnectionAction
    kFBKeyingCurveEndChange:FBConnectionAction
    kFBKeyingDeleteKey:FBConnectionAction
    kFBKeyingKey:FBConnectionAction
    kFBPrefixRename:FBConnectionAction
    kFBPrefixRenamed:FBConnectionAction
    kFBRename:FBConnectionAction
    kFBRenamed:FBConnectionAction
    kFBReorderSrc:FBConnectionAction
    kFBReorderedSrc:FBConnectionAction
    kFBRequestConnectDst:FBConnectionAction
    kFBRequestConnectSrc:FBConnectionAction
    kFBRequestDisconnectDst:FBConnectionAction
    kFBRequestDisconnectSrc:FBConnectionAction
    kFBRequestPrefixRename:FBConnectionAction
    kFBRequestRename:FBConnectionAction
    kFBReselect:FBConnectionAction
    kFBSelect:FBConnectionAction
    kFBUnselect:FBConnectionAction
class FBConnectionType(_Enum):
    kFBConnectionTypeNone:FBConnectionType
    kFBConnectionTypeSystem:FBConnectionType
class FBConsoleChannelType(_Enum):
    kFBConsoleButton:FBConsoleChannelType
    kFBConsoleDisplay:FBConsoleChannelType
    kFBConsoleEncoder:FBConsoleChannelType
    kFBConsoleJoystick:FBConsoleChannelType
    kFBConsoleKey:FBConsoleChannelType
    kFBConsoleNull:FBConsoleChannelType
    kFBConsoleSlider:FBConsoleChannelType
    kFBConsoleTransport:FBConsoleChannelType
class FBConstantKeyReducerThresholdType(_Enum):
    kFBDefaultThreshold:FBConstantKeyReducerThresholdType
    kFBRotationThreshold:FBConstantKeyReducerThresholdType
    kFBScalingThreshold:FBConstantKeyReducerThresholdType
    kFBTranslationThreshold:FBConstantKeyReducerThresholdType
class FBConstructionHistoryState(_Enum):
    kFBConstructionHistory_Listening:FBConstructionHistoryState
    kFBConstructionHistory_Replaying:FBConstructionHistoryState
class FBControlSetType(_Enum):
    kFBControlSetTypeFKIK:FBControlSetType
    kFBControlSetTypeIKOnly:FBControlSetType
    kFBControlSetTypeNone:FBControlSetType
class FBControllerMode(_Enum):
    kFBControllerLabelling:FBControllerMode
    kFBControllerNone:FBControllerMode
    kFBControllerRigidBody:FBControllerMode
    kFBControllerSegment:FBControllerMode
class FBDataAsStringFlag(_Enum):
    kFBDataAsStringPersistence:FBDataAsStringFlag
    kFBDataAsStringUI:FBDataAsStringFlag
class FBDeckTransportMode(_Enum):
    kFBDeckTransportMain:FBDeckTransportMode
    kFBDeckTransportMaster:FBDeckTransportMode
    kFBDeckTransportNone:FBDeckTransportMode
    kFBDeckTransportSlave:FBDeckTransportMode
    kFBDeckTransportSync:FBDeckTransportMode
class FBDeformerType(_Enum):
    kFBDeformerPointCache:FBDeformerType
    kFBDeformerSkeleton:FBDeformerType
    kFBDeformerUnkown:FBDeformerType
class FBDeviceKeyboardKey(_Enum):
    kFBDKey0:FBDeviceKeyboardKey
    kFBDKey1:FBDeviceKeyboardKey
    kFBDKey2:FBDeviceKeyboardKey
    kFBDKey3:FBDeviceKeyboardKey
    kFBDKey4:FBDeviceKeyboardKey
    kFBDKey5:FBDeviceKeyboardKey
    kFBDKey6:FBDeviceKeyboardKey
    kFBDKey7:FBDeviceKeyboardKey
    kFBDKey8:FBDeviceKeyboardKey
    kFBDKey9:FBDeviceKeyboardKey
    kFBDKeyArrowDown:FBDeviceKeyboardKey
    kFBDKeyArrowLeft:FBDeviceKeyboardKey
    kFBDKeyArrowRight:FBDeviceKeyboardKey
    kFBDKeyArrowUp:FBDeviceKeyboardKey
    kFBDKeyEnd:FBDeviceKeyboardKey
    kFBDKeyEscape:FBDeviceKeyboardKey
    kFBDKeyF1:FBDeviceKeyboardKey
    kFBDKeyF10:FBDeviceKeyboardKey
    kFBDKeyF11:FBDeviceKeyboardKey
    kFBDKeyF12:FBDeviceKeyboardKey
    kFBDKeyF2:FBDeviceKeyboardKey
    kFBDKeyF3:FBDeviceKeyboardKey
    kFBDKeyF4:FBDeviceKeyboardKey
    kFBDKeyF5:FBDeviceKeyboardKey
    kFBDKeyF6:FBDeviceKeyboardKey
    kFBDKeyF7:FBDeviceKeyboardKey
    kFBDKeyF8:FBDeviceKeyboardKey
    kFBDKeyF9:FBDeviceKeyboardKey
    kFBDKeyHome:FBDeviceKeyboardKey
    kFBDKeyPageDown:FBDeviceKeyboardKey
    kFBDKeyPageUp:FBDeviceKeyboardKey
    kFBDKeyReturn:FBDeviceKeyboardKey
    kFBDKeySpace:FBDeviceKeyboardKey
class FBDeviceSamplingMode(_Enum):
    kFBAutoFrequency:FBDeviceSamplingMode
    kFBHardwareFrequency:FBDeviceSamplingMode
    kFBHardwareTimestamp:FBDeviceSamplingMode
    kFBSoftwareTimestamp:FBDeviceSamplingMode
class FBDisplayMode(_Enum):
    kFBDisplayModeCount:FBDisplayMode
    kFBDisplayModeDefault:FBDisplayMode
    kFBDisplayModeFlatShade:FBDisplayMode
    kFBDisplayModeHardShade:FBDisplayMode
    kFBDisplayModeTexture:FBDisplayMode
    kFBDisplayModeWireFrame:FBDisplayMode
class FBDisplayWhat(_Enum):
    kFBDisplay3dIcon:FBDisplayWhat
    kFBDisplayAll:FBDisplayWhat
    kFBDisplayCamera:FBDisplayWhat
    kFBDisplayCenter:FBDisplayWhat
    kFBDisplayLight:FBDisplayWhat
    kFBDisplayMarker:FBDisplayWhat
    kFBDisplayNone:FBDisplayWhat
    kFBDisplayNull:FBDisplayWhat
    kFBDisplaySkeleton:FBDisplayWhat
class FBDragAndDropState(_Enum):
    kFBDragAndDropBegin:FBDragAndDropState
    kFBDragAndDropDrag:FBDragAndDropState
    kFBDragAndDropDrop:FBDragAndDropState
    kFBDragAndDropEnd:FBDragAndDropState
    kFBDragOnEmpty:FBDragAndDropState
    kFBDragOnEmptyDrop:FBDragAndDropState
class FBEffectorId(_Enum):
    kFBChestEndEffectorId:FBEffectorId
    kFBChestOriginEffectorId:FBEffectorId
    kFBHeadEffectorId:FBEffectorId
    kFBHipsEffectorId:FBEffectorId
    kFBInvalidEffectorId:FBEffectorId
    kFBLastEffectorId:FBEffectorId
    kFBLeftAnkleEffectorId:FBEffectorId
    kFBLeftElbowEffectorId:FBEffectorId
    kFBLeftFootEffectorId:FBEffectorId
    kFBLeftFootExtraFingerEffectorId:FBEffectorId
    kFBLeftFootIndexEffectorId:FBEffectorId
    kFBLeftFootMiddleEffectorId:FBEffectorId
    kFBLeftFootPinkyEffectorId:FBEffectorId
    kFBLeftFootRingEffectorId:FBEffectorId
    kFBLeftFootThumbEffectorId:FBEffectorId
    kFBLeftHandEffectorId:FBEffectorId
    kFBLeftHandExtraFingerEffectorId:FBEffectorId
    kFBLeftHandIndexEffectorId:FBEffectorId
    kFBLeftHandMiddleEffectorId:FBEffectorId
    kFBLeftHandPinkyEffectorId:FBEffectorId
    kFBLeftHandRingEffectorId:FBEffectorId
    kFBLeftHandThumbEffectorId:FBEffectorId
    kFBLeftHipEffectorId:FBEffectorId
    kFBLeftKneeEffectorId:FBEffectorId
    kFBLeftShoulderEffectorId:FBEffectorId
    kFBLeftWristEffectorId:FBEffectorId
    kFBRightAnkleEffectorId:FBEffectorId
    kFBRightElbowEffectorId:FBEffectorId
    kFBRightFootEffectorId:FBEffectorId
    kFBRightFootExtraFingerEffectorId:FBEffectorId
    kFBRightFootIndexEffectorId:FBEffectorId
    kFBRightFootMiddleEffectorId:FBEffectorId
    kFBRightFootPinkyEffectorId:FBEffectorId
    kFBRightFootRingEffectorId:FBEffectorId
    kFBRightFootThumbEffectorId:FBEffectorId
    kFBRightHandEffectorId:FBEffectorId
    kFBRightHandExtraFingerEffectorId:FBEffectorId
    kFBRightHandIndexEffectorId:FBEffectorId
    kFBRightHandMiddleEffectorId:FBEffectorId
    kFBRightHandPinkyEffectorId:FBEffectorId
    kFBRightHandRingEffectorId:FBEffectorId
    kFBRightHandThumbEffectorId:FBEffectorId
    kFBRightHipEffectorId:FBEffectorId
    kFBRightKneeEffectorId:FBEffectorId
    kFBRightShoulderEffectorId:FBEffectorId
    kFBRightWristEffectorId:FBEffectorId
class FBEffectorSetID(_Enum):
    EFBffectorSetAux7:FBEffectorSetID
    FBEffectorSetAux1:FBEffectorSetID
    FBEffectorSetAux10:FBEffectorSetID
    FBEffectorSetAux11:FBEffectorSetID
    FBEffectorSetAux12:FBEffectorSetID
    FBEffectorSetAux13:FBEffectorSetID
    FBEffectorSetAux14:FBEffectorSetID
    FBEffectorSetAux2:FBEffectorSetID
    FBEffectorSetAux3:FBEffectorSetID
    FBEffectorSetAux4:FBEffectorSetID
    FBEffectorSetAux5:FBEffectorSetID
    FBEffectorSetAux6:FBEffectorSetID
    FBEffectorSetAux8:FBEffectorSetID
    FBEffectorSetAux9:FBEffectorSetID
    FBEffectorSetDefault:FBEffectorSetID
    FBLastEffectorSetIndex:FBEffectorSetID
class FBElementAction(_Enum):
    kFBElementActionAppend:FBElementAction
    kFBElementActionDiscard:FBElementAction
    kFBElementActionMerge:FBElementAction
    kFBElementActionSave:FBElementAction
class FBEventAnimationNodeType(_Enum):
    kFBEventAnimationNodeConstraintChange:FBEventAnimationNodeType
    kFBEventAnimationNodeDataChange:FBEventAnimationNodeType
    kFBEventAnimationNodeNone:FBEventAnimationNodeType
class FBEventName(_Enum):
    kFBEventActivate:FBEventName
    kFBEventCellChange:FBEventName
    kFBEventChange:FBEventName
    kFBEventColumnClick:FBEventName
    kFBEventDoubleClick:FBEventName
    kFBEventDragAndDrop:FBEventName
    kFBEventEnter:FBEventName
    kFBEventExit:FBEventName
    kFBEventExpose:FBEventName
    kFBEventFileExit:FBEventName
    kFBEventFileMerge:FBEventName
    kFBEventFileNew:FBEventName
    kFBEventFileNewCompleted:FBEventName
    kFBEventFileOpen:FBEventName
    kFBEventFileOpenCompleted:FBEventName
    kFBEventFileSave:FBEventName
    kFBEventFileSaveCompleted:FBEventName
    kFBEventIdle:FBEventName
    kFBEventInput:FBEventName
    kFBEventMenu:FBEventName
    kFBEventOnClick:FBEventName
    kFBEventOnClickCheck:FBEventName
    kFBEventResize:FBEventName
    kFBEventRowClick:FBEventName
    kFBEventShow:FBEventName
    kFBEventTransaction:FBEventName
    kFBEventTreeCollapsed:FBEventName
    kFBEventTreeCollapsing:FBEventName
    kFBEventTreeExpanded:FBEventName
    kFBEventTreeExpanding:FBEventName
    kFBEventTreeSelect:FBEventName
    kFBEventUnbindSDK:FBEventName
class FBExistingClipAction(_Enum):
    kFBExistingClipAbortOperation:FBExistingClipAction
    kFBExistingClipAskUser:FBExistingClipAction
    kFBExistingClipRemove:FBExistingClipAction
class FBExistingFileAction(_Enum):
    kFBExistingFileAbortOperation:FBExistingFileAction
    kFBExistingFileAppend:FBExistingFileAction
    kFBExistingFileAskUser:FBExistingFileAction
    kFBExistingFileOverwrite:FBExistingFileAction
class FBExtrapolationMode(_Enum):
    kFCurveExtrapolationConst:FBExtrapolationMode
    kFCurveExtrapolationKeepSlope:FBExtrapolationMode
    kFCurveExtrapolationMirrorRepetition:FBExtrapolationMode
    kFCurveExtrapolationRelativeRepetition:FBExtrapolationMode
    kFCurveExtrapolationRepetition:FBExtrapolationMode
class FBFCurveEventType(_Enum):
    kFBFCurveEventTypeDerivativedChanged:FBFCurveEventType
    kFBFCurveEventTypeKeyAdded:FBFCurveEventType
    kFBFCurveEventTypeKeyBiasChanged:FBFCurveEventType
    kFBFCurveEventTypeKeyContinuityChanged:FBFCurveEventType
    kFBFCurveEventTypeKeyInterpolationChanged:FBFCurveEventType
    kFBFCurveEventTypeKeyMassOperation:FBFCurveEventType
    kFBFCurveEventTypeKeyPostExtrapolationChanged:FBFCurveEventType
    kFBFCurveEventTypeKeyPreExtrapolationChanged:FBFCurveEventType
    kFBFCurveEventTypeKeyRemoved:FBFCurveEventType
    kFBFCurveEventTypeKeyTangentBreakChanged:FBFCurveEventType
    kFBFCurveEventTypeKeyTangentChanged:FBFCurveEventType
    kFBFCurveEventTypeKeyTangentClampModeChanged:FBFCurveEventType
    kFBFCurveEventTypeKeyTangentConstantChanged:FBFCurveEventType
    kFBFCurveEventTypeKeyTensionChanged:FBFCurveEventType
    kFBFCurveEventTypeKeyTimeChanged:FBFCurveEventType
    kFBFCurveEventTypeKeyValueChanged:FBFCurveEventType
    kFBFCurveEventTypeKeyVelocityChanged:FBFCurveEventType
    kFBFCurveEventTypeKeyWeightChanged:FBFCurveEventType
    kFBFCurveEventTypeUnknownOperation:FBFCurveEventType
class FBFileFormatAndVersion(_Enum):
    kFBDefaultFormatAndVersion:FBFileFormatAndVersion
    kFBFBX2010:FBFileFormatAndVersion
    kFBFBX2011:FBFileFormatAndVersion
    kFBFBX2012:FBFileFormatAndVersion
    kFBFBX2013:FBFileFormatAndVersion
    kFBFBX2014_2015:FBFileFormatAndVersion
    kFBFBX2016:FBFileFormatAndVersion
    kFBFBX2018:FBFileFormatAndVersion
    kFBFBX2019:FBFileFormatAndVersion
    kFBFBX2020:FBFileFormatAndVersion
class FBFileMonitoringType(_Enum):
    kFBFileMonitoring_ANIMATIONCLIP:FBFileMonitoringType
    kFBFileMonitoring_FILEREFERENCE:FBFileMonitoringType
    kFBFileMonitoring_InvalidIndex:FBFileMonitoringType
    kFBFileMonitoring_MAINSCENE:FBFileMonitoringType
    kFBFileMonitoring_PYTHONEDITORSCRIPT:FBFileMonitoringType
class FBFilePopupStyle(_Enum):
    kFBFilePopupOpen:FBFilePopupStyle
    kFBFilePopupSave:FBFilePopupStyle
class FBFilterType(_Enum):
    kFBFilterNumber:FBFilterType
    kFBFilterVector:FBFilterType
class FBFloorContactID(_Enum):
    FBLastCharacterMember:FBFloorContactID
    FBLeftFootMemberIndex:FBFloorContactID
    FBLeftHandMemberIndex:FBFloorContactID
    FBRightFootMemberIndex:FBFloorContactID
    FBRightHandMemberIndex:FBFloorContactID
class FBFogMode(_Enum):
    kFBFogModeExponential:FBFogMode
    kFBFogModeLinear:FBFogMode
    kFBFogModeSquareExponential:FBFogMode
class FBGapMode(_Enum):
    kFBGapBezier:FBGapMode
    kFBGapConstant:FBGapMode
    kFBGapCurve:FBGapMode
    kFBGapLinear:FBGapMode
    kFBGapRigidBody:FBGapMode
    kFBGapSample:FBGapMode
class FBGenerationMode(_Enum):
    kFBGenerationFast:FBGenerationMode
    kFBGenerationNone:FBGenerationMode
class FBGeometryArrayElementType(_Enum):
    kFBGeometryArrayElementType_Float:FBGeometryArrayElementType
    kFBGeometryArrayElementType_Float2:FBGeometryArrayElementType
    kFBGeometryArrayElementType_Float3:FBGeometryArrayElementType
    kFBGeometryArrayElementType_Float4:FBGeometryArrayElementType
    kFBGeometryArrayElementType_FloatMatrix4x4:FBGeometryArrayElementType
    kFBGeometryArrayElementType_Integer:FBGeometryArrayElementType
    kFBGeometryArrayElementType_IntegerArrayPointer:FBGeometryArrayElementType
    kFBGeometryArrayElementType_Unknown:FBGeometryArrayElementType
class FBGeometryArrayID(_Enum):
    kFBGeometryArrayID_Binormal:FBGeometryArrayID
    kFBGeometryArrayID_Color:FBGeometryArrayID
    kFBGeometryArrayID_Normal:FBGeometryArrayID
    kFBGeometryArrayID_Point:FBGeometryArrayID
    kFBGeometryArrayID_Tangent:FBGeometryArrayID
class FBGeometryMappingMode(_Enum):
    kFBGeometryMapping_ALL_SAME:FBGeometryMappingMode
    kFBGeometryMapping_BY_CONTROL_POINT:FBGeometryMappingMode
    kFBGeometryMapping_BY_EDGE:FBGeometryMappingMode
    kFBGeometryMapping_BY_POLYGON:FBGeometryMappingMode
    kFBGeometryMapping_BY_POLYGON_VERTEX:FBGeometryMappingMode
    kFBGeometryMapping_NONE:FBGeometryMappingMode
class FBGeometryPrimitiveType(_Enum):
    kFBGeometry_LINES:FBGeometryPrimitiveType
    kFBGeometry_LINE_LOOP:FBGeometryPrimitiveType
    kFBGeometry_LINE_STRIP:FBGeometryPrimitiveType
    kFBGeometry_POINTS:FBGeometryPrimitiveType
    kFBGeometry_POLYGON:FBGeometryPrimitiveType
    kFBGeometry_QUADS:FBGeometryPrimitiveType
    kFBGeometry_QUADS_STRIP:FBGeometryPrimitiveType
    kFBGeometry_TRIANGLES:FBGeometryPrimitiveType
    kFBGeometry_TRIANGLE_FAN:FBGeometryPrimitiveType
    kFBGeometry_TRIANGLE_STRIP:FBGeometryPrimitiveType
class FBGeometryReferenceMode(_Enum):
    kFBGeometryReference_DIRECT:FBGeometryReferenceMode
    kFBGeometryReference_INDEX:FBGeometryReferenceMode
    kFBGeometryReference_INDEX_TO_DIRECT:FBGeometryReferenceMode
class FBGlobalEvalCallbackTiming(_Enum):
    kFBGlobalEvalCallbackAfterDAG:FBGlobalEvalCallbackTiming
    kFBGlobalEvalCallbackAfterDeform:FBGlobalEvalCallbackTiming
    kFBGlobalEvalCallbackAfterPlottingFrame:FBGlobalEvalCallbackTiming
    kFBGlobalEvalCallbackAfterRender:FBGlobalEvalCallbackTiming
    kFBGlobalEvalCallbackBeforeDAG:FBGlobalEvalCallbackTiming
    kFBGlobalEvalCallbackBeforePlottingFrame:FBGlobalEvalCallbackTiming
    kFBGlobalEvalCallbackBeforeRender:FBGlobalEvalCallbackTiming
    kFBGlobalEvalCallbackSyn:FBGlobalEvalCallbackTiming
class FBHUDElementHAlignment(_Enum):
    kFBHUDCenter:FBHUDElementHAlignment
    kFBHUDLeft:FBHUDElementHAlignment
    kFBHUDRight:FBHUDElementHAlignment
class FBHUDElementVAlignment(_Enum):
    kFBHUDBottom:FBHUDElementVAlignment
    kFBHUDTop:FBHUDElementVAlignment
    kFBHUDVCenter:FBHUDElementVAlignment
class FBIconPosition(_Enum):
    kFBIconLeft:FBIconPosition
    kFBIconTop:FBIconPosition
class FBImageFormat(_Enum):
    kFBImageFormatABGR32:FBImageFormat
    kFBImageFormatARGB32:FBImageFormat
    kFBImageFormatBGR16:FBImageFormat
    kFBImageFormatBGR24:FBImageFormat
    kFBImageFormatBGRA32:FBImageFormat
    kFBImageFormatRGB24:FBImageFormat
    kFBImageFormatRGBA32:FBImageFormat
    kFBImageFormatUnknown:FBImageFormat
class FBImageInterleaveType(_Enum):
    kFBImageInterleaveTypeAverage:FBImageInterleaveType
    kFBImageInterleaveTypeEven:FBImageInterleaveType
    kFBImageInterleaveTypeFullFrame:FBImageInterleaveType
    kFBImageInterleaveTypeOdd:FBImageInterleaveType
class FBImageInterpolationType(_Enum):
    kFBImageInterpolationTypeDuplicate:FBImageInterpolationType
    kFBImageInterpolationTypeLinear:FBImageInterpolationType
    kFBImageInterpolationTypeNone:FBImageInterpolationType
class FBImageType(_Enum):
    kFBImageTypeField:FBImageType
    kFBImageTypeFrame:FBImageType
class FBInputKey(_Enum):
    kFBKeyBackSpace:FBInputKey
    kFBKeyDel:FBInputKey
    kFBKeyDown:FBInputKey
    kFBKeyEnd:FBInputKey
    kFBKeyEscape:FBInputKey
    kFBKeyF1:FBInputKey
    kFBKeyF10:FBInputKey
    kFBKeyF11:FBInputKey
    kFBKeyF12:FBInputKey
    kFBKeyF2:FBInputKey
    kFBKeyF3:FBInputKey
    kFBKeyF4:FBInputKey
    kFBKeyF5:FBInputKey
    kFBKeyF6:FBInputKey
    kFBKeyF7:FBInputKey
    kFBKeyF8:FBInputKey
    kFBKeyF9:FBInputKey
    kFBKeyHome:FBInputKey
    kFBKeyIns:FBInputKey
    kFBKeyLeft:FBInputKey
    kFBKeyPageDown:FBInputKey
    kFBKeyPageUp:FBInputKey
    kFBKeyReturn:FBInputKey
    kFBKeyRight:FBInputKey
    kFBKeyTab:FBInputKey
    kFBKeyUp:FBInputKey
class FBInputModifier(_Enum):
    kFBKeyAlt:FBInputModifier
    kFBKeyCtrl:FBInputModifier
    kFBKeyNone:FBInputModifier
    kFBKeyShift:FBInputModifier
class FBInputType(_Enum):
    kFBButtonDoubleClick:FBInputType
    kFBButtonPress:FBInputType
    kFBButtonRelease:FBInputType
    kFBDragging:FBInputType
    kFBDropping:FBInputType
    kFBKeyPress:FBInputType
    kFBKeyPressRaw:FBInputType
    kFBKeyRelease:FBInputType
    kFBKeyReleaseRaw:FBInputType
    kFBMotionNotify:FBInputType
    kFBMouseEnter:FBInputType
    kFBMouseLeave:FBInputType
    kFBMouseWheelNotify:FBInputType
    kFBUnknownInput:FBInputType
class FBInsertSegmentMode(_Enum):
    kFBInsertSegmentFromStart:FBInsertSegmentMode
    kFBInsertSegmentToEnd:FBInsertSegmentMode
    kFBInsertSegmentWhole:FBInsertSegmentMode
class FBInterpolation(_Enum):
    kFBInterpolationConstant:FBInterpolation
    kFBInterpolationCubic:FBInterpolation
    kFBInterpolationCustom:FBInterpolation
    kFBInterpolationLinear:FBInterpolation
class FBInterpolatorCurveType(_Enum):
    kFBInterpolatorCurveFastIn:FBInterpolatorCurveType
    kFBInterpolatorCurveFastOut:FBInterpolatorCurveType
    kFBInterpolatorCurveLast:FBInterpolatorCurveType
    kFBInterpolatorCurveLinearIn:FBInterpolatorCurveType
    kFBInterpolatorCurveLinearOut:FBInterpolatorCurveType
    kFBInterpolatorCurveSlowIn:FBInterpolatorCurveType
    kFBInterpolatorCurveSlowOut:FBInterpolatorCurveType
    kFBInterpolatorCurveSmoothIn:FBInterpolatorCurveType
    kFBInterpolatorCurveSmoothOut:FBInterpolatorCurveType
class FBKeyingGroupType(_Enum):
    kFBKeyingGroupGlobal:FBKeyingGroupType
    kFBKeyingGroupLocal:FBKeyingGroupType
    kFBKeyingGroupObjectType:FBKeyingGroupType
class FBLayerMode(_Enum):
    kFBLayerModeAdditive:FBLayerMode
    kFBLayerModeInvalidIndex:FBLayerMode
    kFBLayerModeOverride:FBLayerMode
    kFBLayerModeOverridePassthrough:FBLayerMode
class FBLayerRotationMode(_Enum):
    kFBLayerRotationModeEulerRotation:FBLayerRotationMode
    kFBLayerRotationModeInvalidIndex:FBLayerRotationMode
    kFBLayerRotationModeQuaternionRotation:FBLayerRotationMode
class FBLightType(_Enum):
    kFBLightTypeArea:FBLightType
    kFBLightTypeInfinite:FBLightType
    kFBLightTypePoint:FBLightType
    kFBLightTypeSpot:FBLightType
class FBListStyle(_Enum):
    kFBDropDownList:FBListStyle
    kFBVerticalList:FBListStyle
class FBManipulatorPickType(_Enum):
    FBPickObjects:FBManipulatorPickType
    FBPickPoints:FBManipulatorPickType
    FBPickSurfaces:FBManipulatorPickType
class FBManipulatorTransformType(_Enum):
    kFBManipulatorTransformNone:FBManipulatorTransformType
    kFBManipulatorTransformRotation:FBManipulatorTransformType
    kFBManipulatorTransformScaling:FBManipulatorTransformType
    kFBManipulatorTransformTranslation:FBManipulatorTransformType
class FBMarkerLook(_Enum):
    kFBMarkerLookAimRollGoal:FBMarkerLook
    kFBMarkerLookBone:FBMarkerLook
    kFBMarkerLookBox:FBMarkerLook
    kFBMarkerLookCapsule:FBMarkerLook
    kFBMarkerLookCircle:FBMarkerLook
    kFBMarkerLookCube:FBMarkerLook
    kFBMarkerLookHardCross:FBMarkerLook
    kFBMarkerLookLightCross:FBMarkerLook
    kFBMarkerLookNone:FBMarkerLook
    kFBMarkerLookRigidGoal:FBMarkerLook
    kFBMarkerLookRotationGoal:FBMarkerLook
    kFBMarkerLookSphere:FBMarkerLook
    kFBMarkerLookSquare:FBMarkerLook
    kFBMarkerLookStick:FBMarkerLook
class FBMarkerResolutionLevel(_Enum):
    kFBMarkerHighResolution:FBMarkerResolutionLevel
    kFBMarkerLowResolution:FBMarkerResolutionLevel
    kFBMarkerMediumResolution:FBMarkerResolutionLevel
class FBMarkerType(_Enum):
    kFBMarkerTypeFKEffector:FBMarkerType
    kFBMarkerTypeIKEffector:FBMarkerType
    kFBMarkerTypeOptical:FBMarkerType
    kFBMarkerTypeStandard:FBMarkerType
class FBMaterialTextureType(_Enum):
    kFBMaterialTextureAmbient:FBMaterialTextureType
    kFBMaterialTextureAmbientFactor:FBMaterialTextureType
    kFBMaterialTextureBump:FBMaterialTextureType
    kFBMaterialTextureDiffuse:FBMaterialTextureType
    kFBMaterialTextureDiffuseFactor:FBMaterialTextureType
    kFBMaterialTextureEmissive:FBMaterialTextureType
    kFBMaterialTextureEmissiveFactor:FBMaterialTextureType
    kFBMaterialTextureNormalMap:FBMaterialTextureType
    kFBMaterialTextureReflection:FBMaterialTextureType
    kFBMaterialTextureReflectionFactor:FBMaterialTextureType
    kFBMaterialTextureShiness:FBMaterialTextureType
    kFBMaterialTextureSpecular:FBMaterialTextureType
    kFBMaterialTextureSpecularFactor:FBMaterialTextureType
    kFBMaterialTextureTransparent:FBMaterialTextureType
    kFBMaterialTextureTransparentFactor:FBMaterialTextureType
class FBMenuItemType(_Enum):
    kFBMenuItemMotionExport:FBMenuItemType
    kFBMenuItemMotionImport:FBMenuItemType
    kFBMenuItemSceneExport:FBMenuItemType
    kFBMenuItemSceneImport:FBMenuItemType
class FBMergeLayerMode(_Enum):
    kFBMergeLayerModeAdditive:FBMergeLayerMode
    kFBMergeLayerModeAutomatic:FBMergeLayerMode
    kFBMergeLayerModeOverride:FBMergeLayerMode
class FBMirrorPlaneType(_Enum):
    kFBMirrorPlaneTypeAuto:FBMirrorPlaneType
    kFBMirrorPlaneTypeCount:FBMirrorPlaneType
    kFBMirrorPlaneTypeEquation:FBMirrorPlaneType
    kFBMirrorPlaneTypeInvalid:FBMirrorPlaneType
    kFBMirrorPlaneTypeUser:FBMirrorPlaneType
    kFBMirrorPlaneTypeXY:FBMirrorPlaneType
    kFBMirrorPlaneTypeXZ:FBMirrorPlaneType
    kFBMirrorPlaneTypeZY:FBMirrorPlaneType
class FBModelCullingMode(_Enum):
    kFBCullingOff:FBModelCullingMode
    kFBCullingOnCCW:FBModelCullingMode
    kFBCullingOnCW:FBModelCullingMode
class FBModelEvaluationTaskType(_Enum):
    kFBModelEvaluationBBox:FBModelEvaluationTaskType
    kFBModelEvaluationDeform:FBModelEvaluationTaskType
    kFBModelEvaluationTransform:FBModelEvaluationTaskType
class FBModelHiercharyTraverserType(_Enum):
    kModelTraverserBreadthFirst:FBModelHiercharyTraverserType
    kModelTraverserDepthFirst:FBModelHiercharyTraverserType
class FBModelRotationOrder(_Enum):
    kFBEulerXYZ:FBModelRotationOrder
    kFBEulerXZY:FBModelRotationOrder
    kFBEulerYXZ:FBModelRotationOrder
    kFBEulerYZX:FBModelRotationOrder
    kFBEulerZXY:FBModelRotationOrder
    kFBEulerZYX:FBModelRotationOrder
    kFBSphericXYZ:FBModelRotationOrder
class FBModelSelection(_Enum):
    kFBAllModels:FBModelSelection
    kFBCreateModels:FBModelSelection
    kFBInHierarchy:FBModelSelection
    kFBNone:FBModelSelection
    kFBPrefixGroupContainingModel:FBModelSelection
    kFBSelectedModelAndChildren:FBModelSelection
    kFBSelectedModels:FBModelSelection
class FBModelShadingMode(_Enum):
    kFBModelShadingAll:FBModelShadingMode
    kFBModelShadingDefault:FBModelShadingMode
    kFBModelShadingFlat:FBModelShadingMode
    kFBModelShadingHard:FBModelShadingMode
    kFBModelShadingLight:FBModelShadingMode
    kFBModelShadingTexture:FBModelShadingMode
    kFBModelShadingWire:FBModelShadingMode
class FBModelTemplateStyle(_Enum):
    kFBModelTemplateCamera:FBModelTemplateStyle
    kFBModelTemplateCameraInterest:FBModelTemplateStyle
    kFBModelTemplateGeometry:FBModelTemplateStyle
    kFBModelTemplateLight:FBModelTemplateStyle
    kFBModelTemplateMarker:FBModelTemplateStyle
    kFBModelTemplateNone:FBModelTemplateStyle
    kFBModelTemplateNull:FBModelTemplateStyle
    kFBModelTemplateOptical:FBModelTemplateStyle
    kFBModelTemplateRoot:FBModelTemplateStyle
    kFBModelTemplateSensor:FBModelTemplateStyle
    kFBModelTemplateSkeleton:FBModelTemplateStyle
class FBModelTransformationType(_Enum):
    kModelInverse_Rotation:FBModelTransformationType
    kModelInverse_Scaling:FBModelTransformationType
    kModelInverse_Transformation:FBModelTransformationType
    kModelInverse_Transformation_Geometry:FBModelTransformationType
    kModelInverse_Translation:FBModelTransformationType
    kModelRotation:FBModelTransformationType
    kModelScaling:FBModelTransformationType
    kModelTransformation:FBModelTransformationType
    kModelTransformation_Geometry:FBModelTransformationType
    kModelTranslation:FBModelTransformationType
class FBNamespaceAction(_Enum):
    kFBConcatNamespace:FBNamespaceAction
    kFBRemoveAllNamespace:FBNamespaceAction
    kFBReplaceNamespace:FBNamespaceAction
class FBNewKeyInterpolationType(_Enum):
    kFBNewKeyInterpolation_Auto:FBNewKeyInterpolationType
    kFBNewKeyInterpolation_Custom0:FBNewKeyInterpolationType
    kFBNewKeyInterpolation_Custom1:FBNewKeyInterpolationType
    kFBNewKeyInterpolation_Custom2:FBNewKeyInterpolationType
    kFBNewKeyInterpolation_Fixed:FBNewKeyInterpolationType
    kFBNewKeyInterpolation_Linear:FBNewKeyInterpolationType
    kFBNewKeyInterpolation_None:FBNewKeyInterpolationType
    kFBNewKeyInterpolation_Smooth:FBNewKeyInterpolationType
    kFBNewKeyInterpolation_SmoothClamp:FBNewKeyInterpolationType
    kFBNewKeyInterpolation_Spline:FBNewKeyInterpolationType
    kFBNewKeyInterpolation_SplineClamp:FBNewKeyInterpolationType
    kFBNewKeyInterpolation_Step:FBNewKeyInterpolationType
    kFBNewKeyInterpolation_TCB:FBNewKeyInterpolationType
class FBNurbType(_Enum):
    kFBNurbTypeClosed:FBNurbType
    kFBNurbTypeOpen:FBNurbType
    kFBNurbTypePeriodic:FBNurbType
class FBObjectFlag(_Enum):
    kFBFlagAllocated:FBObjectFlag
    kFBFlagBrowsable:FBObjectFlag
    kFBFlagClonable:FBObjectFlag
    kFBFlagDeletable:FBObjectFlag
    kFBFlagDetachable:FBObjectFlag
    kFBFlagKeyable:FBObjectFlag
    kFBFlagMergeable:FBObjectFlag
    kFBFlagNamespaceEditable:FBObjectFlag
    kFBFlagNewable:FBObjectFlag
    kFBFlagParentable:FBObjectFlag
    kFBFlagRenamable:FBObjectFlag
    kFBFlagSavable:FBObjectFlag
    kFBFlagSelectable:FBObjectFlag
    kFBFlagStorable6:FBObjectFlag
    kFBFlagStorableData6:FBObjectFlag
    kFBFlagStory:FBObjectFlag
    kFBFlagSystem:FBObjectFlag
    kFBFlagUndoable:FBObjectFlag
    kFBFlagUndoableSeparately:FBObjectFlag
    kFBFlagUniqueName:FBObjectFlag
    kFBFlagVisible:FBObjectFlag
class FBObjectPoseMirrorOptionsFlag(_Enum):
    kFBObjectPoseMirrorOptionsNoFlag:FBObjectPoseMirrorOptionsFlag
    kFBObjectPoseMirrorOptionsUpdateLocal:FBObjectPoseMirrorOptionsFlag
    kFBObjectPoseMirrorOptionsUpdateLocalMirrorParent:FBObjectPoseMirrorOptionsFlag
    kFBObjectPoseMirrorOptionsUpdateLocalRef:FBObjectPoseMirrorOptionsFlag
    kFBObjectPoseMirrorOptionsUpdateLocalRefMirrorRef:FBObjectPoseMirrorOptionsFlag
class FBObjectPoseOptionsFlag(_Enum):
    kFBObjectPoseOptionsNoFlag:FBObjectPoseOptionsFlag
    kFBObjectPoseOptionsRotation:FBObjectPoseOptionsFlag
    kFBObjectPoseOptionsScaling:FBObjectPoseOptionsFlag
    kFBObjectPoseOptionsTranslationX:FBObjectPoseOptionsFlag
    kFBObjectPoseOptionsTranslationY:FBObjectPoseOptionsFlag
    kFBObjectPoseOptionsTranslationZ:FBObjectPoseOptionsFlag
class FBObjectStatus(_Enum):
    kFBStatusClearing:FBObjectStatus
    kFBStatusCreating:FBObjectStatus
    kFBStatusDestroying:FBObjectStatus
    kFBStatusMerging:FBObjectStatus
    kFBStatusRetrieving:FBObjectStatus
    kFBStatusStoring:FBObjectStatus
class FBOneClickApplication(_Enum):
    kFBOneClick3dsMax:FBOneClickApplication
    kFBOneClickMaya:FBOneClickApplication
    kFBOneClickNone:FBOneClickApplication
    kFBOneClickSoftimage:FBOneClickApplication
class FBOrientation(_Enum):
    kFBHorizontal:FBOrientation
    kFBVertical:FBOrientation
class FBParallelScheduleType(_Enum):
    kFBParallelScheduleAdvanced:FBParallelScheduleType
    kFBParallelScheduleSerial:FBParallelScheduleType
    kFBParallelScheduleSimple:FBParallelScheduleType
class FBParity(_Enum):
    kFBParityEven:FBParity
    kFBParityNone:FBParity
    kFBParityOdd:FBParity
class FBPickingMode(_Enum):
    kFBPickingModeCount:FBPickingMode
    kFBPickingModeModelsOnly:FBPickingMode
    kFBPickingModeStandard:FBPickingMode
    kFBPickingModeXRay:FBPickingMode
class FBPlayMode(_Enum):
    kFBPlayModeLoop:FBPlayMode
    kFBPlayModeNoPlay:FBPlayMode
    kFBPlayModePlay:FBPlayMode
    kFBPlayModePlayToEnd:FBPlayMode
    kFBPlayModePreviewToEnd:FBPlayMode
class FBPlayerControlChangeType(_Enum):
    kFBPlayerControlGoto:FBPlayerControlChangeType
    kFBPlayerControlNone:FBPlayerControlChangeType
    kFBPlayerControlPlay:FBPlayerControlChangeType
    kFBPlayerControlPlayReverse:FBPlayerControlChangeType
    kFBPlayerControlRecordModeOff:FBPlayerControlChangeType
    kFBPlayerControlRecordModeOn:FBPlayerControlChangeType
    kFBPlayerControlStepBackward:FBPlayerControlChangeType
    kFBPlayerControlStepForward:FBPlayerControlChangeType
    kFBPlayerControlStop:FBPlayerControlChangeType
class FBPlotAllowed(_Enum):
    kFBPlotAllowed_Both:FBPlotAllowed
    kFBPlotAllowed_ControlRig:FBPlotAllowed
    kFBPlotAllowed_None:FBPlotAllowed
    kFBPlotAllowed_Skeleton:FBPlotAllowed
class FBPlotTangentMode(_Enum):
    kFBPlotTangentModeAuto:FBPlotTangentMode
    kFBPlotTangentModeSmooth:FBPlotTangentMode
    kFBPlotTangentModeSmoothClamp:FBPlotTangentMode
    kFBPlotTangentModeSpline:FBPlotTangentMode
    kFBPlotTangentModeSplineClamp:FBPlotTangentMode
class FBPlugModificationFlag(_Enum):
    kFBAllConnectionModified:FBPlugModificationFlag
    kFBAllCustomPropertyModified:FBPlugModificationFlag
    kFBAllDataModified:FBPlugModificationFlag
    kFBAllKeyingModified:FBPlugModificationFlag
    kFBAllModifiedMask:FBPlugModificationFlag
    kFBAllStateModified:FBPlugModificationFlag
    kFBContentAllModifiedMask:FBPlugModificationFlag
    kFBContentConnectionModified:FBPlugModificationFlag
    kFBContentCustomPropertyModified:FBPlugModificationFlag
    kFBContentDataModified:FBPlugModificationFlag
    kFBContentKeyingModified:FBPlugModificationFlag
    kFBContentStateModified:FBPlugModificationFlag
    kFBPlugAllContent:FBPlugModificationFlag
    kFBSelfAllModifiedMask:FBPlugModificationFlag
    kFBSelfConnectionDstObjectModified:FBPlugModificationFlag
    kFBSelfConnectionDstPropertyModified:FBPlugModificationFlag
    kFBSelfConnectionModifiedMask:FBPlugModificationFlag
    kFBSelfConnectionSrcObjectModified:FBPlugModificationFlag
    kFBSelfConnectionSrcPropertyModified:FBPlugModificationFlag
    kFBSelfCustomPropertyModified:FBPlugModificationFlag
    kFBSelfDataModified:FBPlugModificationFlag
    kFBSelfKeyingModified:FBPlugModificationFlag
    kFBSelfStateModified:FBPlugModificationFlag
class FBPlugStatusFlag(_Enum):
    kFBOwnedByUndo:FBPlugStatusFlag
    kFBPlugStatusFlagNone:FBPlugStatusFlag
    kFBStatusMask:FBPlugStatusFlag
class FBPopupInputType(_Enum):
    kFBPopupBool:FBPopupInputType
    kFBPopupChar:FBPopupInputType
    kFBPopupDouble:FBPopupInputType
    kFBPopupFloat:FBPopupInputType
    kFBPopupInt:FBPopupInputType
    kFBPopupPassword:FBPopupInputType
    kFBPopupString:FBPopupInputType
class FBPoseTransformType(_Enum):
    kFBPoseTransformGlobal:FBPoseTransformType
    kFBPoseTransformInvalid:FBPoseTransformType
    kFBPoseTransformLocal:FBPoseTransformType
    kFBPoseTransformLocalRef:FBPoseTransformType
    kFBPoseTransformTypeCount:FBPoseTransformType
class FBPoseType(_Enum):
    kFBBindPose:FBPoseType
    kFBRestPose:FBPoseType
class FBProfilingMode(_Enum):
    kFBProfilingModeAllHi:FBProfilingMode
    kFBProfilingModeAllLow:FBProfilingMode
    kFBProfilingModeDevices:FBProfilingMode
    kFBProfilingModeDisabled:FBProfilingMode
    kFBProfilingModeEvaluation:FBProfilingMode
    kFBProfilingModeRendering:FBProfilingMode
    kFBProfilingModeSDK:FBProfilingMode
class FBPropertyComponents(_Enum):
    kFBPropertyComponent0:FBPropertyComponents
    kFBPropertyComponent1:FBPropertyComponents
    kFBPropertyComponent2:FBPropertyComponents
    kFBPropertyComponent3:FBPropertyComponents
    kFBPropertyComponentAll:FBPropertyComponents
class FBPropertyFlag(_Enum):
    kFBDrivenSetByMain:FBPropertyFlag
    kFBDynamicHidden:FBPropertyFlag
    kFBLoadedUserProperty:FBPropertyFlag
    kFBPropertyFlagAnimated:FBPropertyFlag
    kFBPropertyFlagDisableProperty:FBPropertyFlag
    kFBPropertyFlagDrivenProperty:FBPropertyFlag
    kFBPropertyFlagForceStaticProperty:FBPropertyFlag
    kFBPropertyFlagHideProperty:FBPropertyFlag
    kFBPropertyFlagNotSavable:FBPropertyFlag
    kFBPropertyFlagNotSet:FBPropertyFlag
    kFBPropertyFlagNotUserDeletable:FBPropertyFlag
    kFBPropertyFlagReadOnly:FBPropertyFlag
    kFBSlaveSetByMaster:FBPropertyFlag
    kFBValueAllocated:FBPropertyFlag
class FBPropertyStateEventType(_Enum):
    kFBPropertyStateEventTypeAttached:FBPropertyStateEventType
    kFBPropertyStateEventTypeDestroyed:FBPropertyStateEventType
    kFBPropertyStateEventTypeDetached:FBPropertyStateEventType
    kFBPropertyStateEventTypeMassOperation:FBPropertyStateEventType
    kFBPropertyStateEventTypeUnknownOperation:FBPropertyStateEventType
class FBPropertyType(_Enum):
    kFBPT_Action:FBPropertyType
    kFBPT_ColorRGB:FBPropertyType
    kFBPT_ColorRGBA:FBPropertyType
    kFBPT_Reference:FBPropertyType
    kFBPT_Time:FBPropertyType
    kFBPT_TimeCode:FBPropertyType
    kFBPT_TimeSpan:FBPropertyType
    kFBPT_Vector2D:FBPropertyType
    kFBPT_Vector3D:FBPropertyType
    kFBPT_Vector4D:FBPropertyType
    kFBPT_bool:FBPropertyType
    kFBPT_charptr:FBPropertyType
    kFBPT_double:FBPropertyType
    kFBPT_enum:FBPropertyType
    kFBPT_event:FBPropertyType
    kFBPT_float:FBPropertyType
    kFBPT_int:FBPropertyType
    kFBPT_kReference:FBPropertyType
    kFBPT_object:FBPropertyType
    kFBPT_stringlist:FBPropertyType
    kFBPT_unknown:FBPropertyType
class FBPropertyViewType(_Enum):
    kFBViewByObject:FBPropertyViewType
    kFBViewByObjectType:FBPropertyViewType
    kFBViewGlobal:FBPropertyViewType
class FBRSType(_Enum):
    kFBRS232:FBRSType
    kFBRS422:FBRSType
class FBRecalcMarkerSetOffset(_Enum):
    kFBRecalcMarkerSetOffsetROnly:FBRecalcMarkerSetOffset
    kFBRecalcMarkerSetOffsetTR:FBRecalcMarkerSetOffset
class FBRenderingPass(_Enum):
    kFBPassAddColor:FBRenderingPass
    kFBPassFlat:FBRenderingPass
    kFBPassInvalid:FBRenderingPass
    kFBPassLighted:FBRenderingPass
    kFBPassMatte:FBRenderingPass
    kFBPassPostRender:FBRenderingPass
    kFBPassPreRender:FBRenderingPass
    kFBPassTranslucent:FBRenderingPass
    kFBPassTranslucentZSort:FBRenderingPass
    kFBPassZTranslucent:FBRenderingPass
    kFBPassZTranslucentAlphaTest:FBRenderingPass
class FBRigidBodyMode(_Enum):
    kFBRigidBodyBest:FBRigidBodyMode
    kFBRigidBodyFast:FBRigidBodyMode
class FBRootHMode(_Enum):
    kFBRootHAbsoluteDifference:FBRootHMode
    kFBRootHRelativeDifference:FBRootHMode
class FBRootRMode(_Enum):
    kFBRootRAbsoluteDifference:FBRootRMode
    kFBRootRRelativeDifference:FBRootRMode
class FBRootSpeedMode(_Enum):
    kFBRootSpeedAbsoluteDifference:FBRootSpeedMode
    kFBRootSpeedRelativeDifference:FBRootSpeedMode
class FBRootXZMode(_Enum):
    kFBRootXZAbsoluteDifference:FBRootXZMode
    kFBRootXZRelativeDifference:FBRootXZMode
class FBRotationFilter(_Enum):
    kFBRotationFilterGimbleKiller:FBRotationFilter
    kFBRotationFilterNone:FBRotationFilter
    kFBRotationFilterUnroll:FBRotationFilter
class FBRotationOrder(_Enum):
    kFBXYZ:FBRotationOrder
    kFBXZY:FBRotationOrder
    kFBYXZ:FBRotationOrder
    kFBYZX:FBRotationOrder
    kFBZXY:FBRotationOrder
    kFBZYX:FBRotationOrder
class FBSceneChangeType(_Enum):
    kFBSceneChangeActivate:FBSceneChangeType
    kFBSceneChangeAddChild:FBSceneChangeType
    kFBSceneChangeAttach:FBSceneChangeType
    kFBSceneChangeChangeName:FBSceneChangeType
    kFBSceneChangeChangedName:FBSceneChangeType
    kFBSceneChangeChangedParent:FBSceneChangeType
    kFBSceneChangeClearBegin:FBSceneChangeType
    kFBSceneChangeClearEnd:FBSceneChangeType
    kFBSceneChangeDeactivate:FBSceneChangeType
    kFBSceneChangeDestroy:FBSceneChangeType
    kFBSceneChangeDetach:FBSceneChangeType
    kFBSceneChangeFocus:FBSceneChangeType
    kFBSceneChangeHardSelect:FBSceneChangeType
    kFBSceneChangeLoadBegin:FBSceneChangeType
    kFBSceneChangeLoadEnd:FBSceneChangeType
    kFBSceneChangeMergeTransactionBegin:FBSceneChangeType
    kFBSceneChangeMergeTransactionEnd:FBSceneChangeType
    kFBSceneChangeNone:FBSceneChangeType
    kFBSceneChangePreParent:FBSceneChangeType
    kFBSceneChangePreUnparent:FBSceneChangeType
    kFBSceneChangeReSelect:FBSceneChangeType
    kFBSceneChangeRemoveChild:FBSceneChangeType
    kFBSceneChangeRename:FBSceneChangeType
    kFBSceneChangeRenamePrefix:FBSceneChangeType
    kFBSceneChangeRenameUnique:FBSceneChangeType
    kFBSceneChangeRenameUniquePrefix:FBSceneChangeType
    kFBSceneChangeRenamed:FBSceneChangeType
    kFBSceneChangeRenamedPrefix:FBSceneChangeType
    kFBSceneChangeRenamedUnique:FBSceneChangeType
    kFBSceneChangeRenamedUniquePrefix:FBSceneChangeType
    kFBSceneChangeReorder:FBSceneChangeType
    kFBSceneChangeReordered:FBSceneChangeType
    kFBSceneChangeSelect:FBSceneChangeType
    kFBSceneChangeSoftSelect:FBSceneChangeType
    kFBSceneChangeSoftUnselect:FBSceneChangeType
    kFBSceneChangeTransactionBegin:FBSceneChangeType
    kFBSceneChangeTransactionEnd:FBSceneChangeType
    kFBSceneChangeUnselect:FBSceneChangeType
class FBSegmentMode(_Enum):
    kFBSegmentAll:FBSegmentMode
    kFBSegmentMarker:FBSegmentMode
    kFBSegmentRigidBody:FBSegmentMode
class FBShadowFrameType(_Enum):
    kFBShadowFrameTypeShadowCaster:FBShadowFrameType
    kFBShadowFrameTypeShadowCubeMap:FBShadowFrameType
    kFBShadowFrameTypeShadowReceiver:FBShadowFrameType
class FBShadowType(_Enum):
    kFBShadowTypeLightMapProjectiveTexture:FBShadowType
    kFBShadowTypeShadowOpaquePlanar:FBShadowType
    kFBShadowTypeShadowProjectiveTexture:FBShadowType
    kFBShadowTypeShadowTranslucentPlanar:FBShadowType
    kFBShadowTypeZLightMapProjectiveTexture:FBShadowType
    kFBShadowTypeZShadowProjectiveTexture:FBShadowType
class FBSkeletonLook(_Enum):
    kFBSkeletonLookBone:FBSkeletonLook
    kFBSkeletonLookBox:FBSkeletonLook
    kFBSkeletonLookCapsule:FBSkeletonLook
    kFBSkeletonLookCircle:FBSkeletonLook
    kFBSkeletonLookCube:FBSkeletonLook
    kFBSkeletonLookHardCross:FBSkeletonLook
    kFBSkeletonLookLightCross:FBSkeletonLook
    kFBSkeletonLookSphere:FBSkeletonLook
    kFBSkeletonLookSquare:FBSkeletonLook
    kFBSkeletonLookStick:FBSkeletonLook
class FBSkeletonNodeId(_Enum):
    kFBSkeletonChestIndex:FBSkeletonNodeId
    kFBSkeletonHeadIndex:FBSkeletonNodeId
    kFBSkeletonHipsIndex:FBSkeletonNodeId
    kFBSkeletonInvalidIndex:FBSkeletonNodeId
    kFBSkeletonLastIndex:FBSkeletonNodeId
    kFBSkeletonLeftAnkleIndex:FBSkeletonNodeId
    kFBSkeletonLeftCollarIndex:FBSkeletonNodeId
    kFBSkeletonLeftElbowIndex:FBSkeletonNodeId
    kFBSkeletonLeftFootIndex:FBSkeletonNodeId
    kFBSkeletonLeftHipIndex:FBSkeletonNodeId
    kFBSkeletonLeftIndexAIndex:FBSkeletonNodeId
    kFBSkeletonLeftIndexBIndex:FBSkeletonNodeId
    kFBSkeletonLeftIndexCIndex:FBSkeletonNodeId
    kFBSkeletonLeftKneeIndex:FBSkeletonNodeId
    kFBSkeletonLeftMiddleAIndex:FBSkeletonNodeId
    kFBSkeletonLeftMiddleBIndex:FBSkeletonNodeId
    kFBSkeletonLeftMiddleCIndex:FBSkeletonNodeId
    kFBSkeletonLeftPinkyAIndex:FBSkeletonNodeId
    kFBSkeletonLeftPinkyBIndex:FBSkeletonNodeId
    kFBSkeletonLeftPinkyCIndex:FBSkeletonNodeId
    kFBSkeletonLeftRingAIndex:FBSkeletonNodeId
    kFBSkeletonLeftRingBIndex:FBSkeletonNodeId
    kFBSkeletonLeftRingCIndex:FBSkeletonNodeId
    kFBSkeletonLeftShoulderIndex:FBSkeletonNodeId
    kFBSkeletonLeftThumbAIndex:FBSkeletonNodeId
    kFBSkeletonLeftThumbBIndex:FBSkeletonNodeId
    kFBSkeletonLeftThumbCIndex:FBSkeletonNodeId
    kFBSkeletonLeftWristIndex:FBSkeletonNodeId
    kFBSkeletonNeckIndex:FBSkeletonNodeId
    kFBSkeletonReferenceIndex:FBSkeletonNodeId
    kFBSkeletonRightAnkleIndex:FBSkeletonNodeId
    kFBSkeletonRightCollarIndex:FBSkeletonNodeId
    kFBSkeletonRightElbowIndex:FBSkeletonNodeId
    kFBSkeletonRightFootIndex:FBSkeletonNodeId
    kFBSkeletonRightHipIndex:FBSkeletonNodeId
    kFBSkeletonRightIndexAIndex:FBSkeletonNodeId
    kFBSkeletonRightIndexBIndex:FBSkeletonNodeId
    kFBSkeletonRightIndexCIndex:FBSkeletonNodeId
    kFBSkeletonRightKneeIndex:FBSkeletonNodeId
    kFBSkeletonRightMiddleAIndex:FBSkeletonNodeId
    kFBSkeletonRightMiddleBIndex:FBSkeletonNodeId
    kFBSkeletonRightMiddleCIndex:FBSkeletonNodeId
    kFBSkeletonRightPinkyAIndex:FBSkeletonNodeId
    kFBSkeletonRightPinkyBIndex:FBSkeletonNodeId
    kFBSkeletonRightPinkyCIndex:FBSkeletonNodeId
    kFBSkeletonRightRingAIndex:FBSkeletonNodeId
    kFBSkeletonRightRingBIndex:FBSkeletonNodeId
    kFBSkeletonRightRingCIndex:FBSkeletonNodeId
    kFBSkeletonRightShoulderIndex:FBSkeletonNodeId
    kFBSkeletonRightThumbAIndex:FBSkeletonNodeId
    kFBSkeletonRightThumbBIndex:FBSkeletonNodeId
    kFBSkeletonRightThumbCIndex:FBSkeletonNodeId
    kFBSkeletonRightWristIndex:FBSkeletonNodeId
    kFBSkeletonWaistIndex:FBSkeletonNodeId
class FBSkeletonResolutionLevel(_Enum):
    kFBSkeletonHighResolution:FBSkeletonResolutionLevel
    kFBSkeletonLowResolution:FBSkeletonResolutionLevel
    kFBSkeletonMediumResolution:FBSkeletonResolutionLevel
class FBSplitStyle(_Enum):
    kFBHSplit:FBSplitStyle
    kFBHVSplit:FBSplitStyle
    kFBNoSplit:FBSplitStyle
    kFBVSplit:FBSplitStyle
class FBStereoDisplayMode(_Enum):
    kFBStereoDisplayActive:FBStereoDisplayMode
    kFBStereoDisplayAnaglyph:FBStereoDisplayMode
    kFBStereoDisplayAnaglyphLuminance:FBStereoDisplayMode
    kFBStereoDisplayCenterEye:FBStereoDisplayMode
    kFBStereoDisplayCheckerboard:FBStereoDisplayMode
    kFBStereoDisplayFreeviewCrossed:FBStereoDisplayMode
    kFBStereoDisplayFreeviewParallel:FBStereoDisplayMode
    kFBStereoDisplayHorizontalInterlace:FBStereoDisplayMode
    kFBStereoDisplayLeftEye:FBStereoDisplayMode
    kFBStereoDisplayModeCount:FBStereoDisplayMode
    kFBStereoDisplayRightEye:FBStereoDisplayMode
class FBStoryClipAlignmentType(_Enum):
    kFBStoryClipAlignmentBeginningNext:FBStoryClipAlignmentType
    kFBStoryClipAlignmentBeginningNextAllAligned:FBStoryClipAlignmentType
    kFBStoryClipAlignmentBeginningNextWithOffset:FBStoryClipAlignmentType
    kFBStoryClipAlignmentCurrentTimeline:FBStoryClipAlignmentType
    kFBStoryClipAlignmentCurrentTimelineWithOffset:FBStoryClipAlignmentType
    kFBStoryClipAlignmentEndPrevious:FBStoryClipAlignmentType
    kFBStoryClipAlignmentEndPreviousAllAligned:FBStoryClipAlignmentType
    kFBStoryClipAlignmentEndPreviousWithOffset:FBStoryClipAlignmentType
class FBStoryClipChangeType(_Enum):
    kFBStoryClipMoveBlend:FBStoryClipChangeType
    kFBStoryClipMoveClip:FBStoryClipChangeType
    kFBStoryClipMoveData:FBStoryClipChangeType
    kFBStoryClipNotSet:FBStoryClipChangeType
    kFBStoryClipRemoved:FBStoryClipChangeType
    kFBStoryClipUpdateUI:FBStoryClipChangeType
class FBStoryClipCompMode(_Enum):
    kFBStoryClipAuto:FBStoryClipCompMode
    kFBStoryClipOff:FBStoryClipCompMode
    kFBStoryClipUser:FBStoryClipCompMode
class FBStoryClipGhostTimeMode(_Enum):
    kFBStoryClipGhostCurrent:FBStoryClipGhostTimeMode
    kFBStoryClipGhostCustom:FBStoryClipGhostTimeMode
    kFBStoryClipGhostStart:FBStoryClipGhostTimeMode
    kFBStoryClipGhostStop:FBStoryClipGhostTimeMode
class FBStoryClipMatchingRotationType(_Enum):
    kFBStoryClipMatchingRotationDefault:FBStoryClipMatchingRotationType
    kFBStoryClipMatchingRotationGravityXZ:FBStoryClipMatchingRotationType
    kFBStoryClipMatchingRotationNone:FBStoryClipMatchingRotationType
    kFBStoryClipMatchingRotationXYZ:FBStoryClipMatchingRotationType
class FBStoryClipMatchingTimeType(_Enum):
    kFBStoryClipMatchingTimeBetweenPreviousAndSelectedClip:FBStoryClipMatchingTimeType
    kFBStoryClipMatchingTimeBetweenSelectedAndNextClip:FBStoryClipMatchingTimeType
    kFBStoryClipMatchingTimeCurrentTime:FBStoryClipMatchingTimeType
    kFBStoryClipMatchingTimeDefault:FBStoryClipMatchingTimeType
    kFBStoryClipMatchingTimeEndOfPreviousClip:FBStoryClipMatchingTimeType
    kFBStoryClipMatchingTimeEndOfSelectedClip:FBStoryClipMatchingTimeType
    kFBStoryClipMatchingTimeStartOfNextClip:FBStoryClipMatchingTimeType
    kFBStoryClipMatchingTimeStartOfSelectedClip:FBStoryClipMatchingTimeType
class FBStoryClipMatchingTranslationType(_Enum):
    kFBStoryClipMatchingTranslationDefault:FBStoryClipMatchingTranslationType
    kFBStoryClipMatchingTranslationGravityXZ:FBStoryClipMatchingTranslationType
    kFBStoryClipMatchingTranslationNone:FBStoryClipMatchingTranslationType
    kFBStoryClipMatchingTranslationXYZ:FBStoryClipMatchingTranslationType
class FBStoryClipMirrorPlane(_Enum):
    kFBStoryClipMirrorPlaneXY:FBStoryClipMirrorPlane
    kFBStoryClipMirrorPlaneXZ:FBStoryClipMirrorPlane
    kFBStoryClipMirrorPlaneZY:FBStoryClipMirrorPlane
class FBStoryClipNodeFunction(_Enum):
    kFBStoryClipNodeAverage:FBStoryClipNodeFunction
    kFBStoryClipNodeFloorProjection:FBStoryClipNodeFunction
    kFBStoryClipNodeNone:FBStoryClipNodeFunction
class FBStoryClipShowGhostMode(_Enum):
    kFBStoryClipAlways:FBStoryClipShowGhostMode
    kFBStoryClipTimeCursor:FBStoryClipShowGhostMode
    kFBStoryClipTimeCustom:FBStoryClipShowGhostMode
class FBStoryClipSolveMode(_Enum):
    kFBStoryClipAnimFkIk:FBStoryClipSolveMode
    kFBStoryClipAnimSkeleton:FBStoryClipSolveMode
    kFBStoryClipAnimSkeletonIk:FBStoryClipSolveMode
    kFBStoryClipRetargetSkeleton:FBStoryClipSolveMode
class FBStoryClipTimeWarpInterpolatorType(_Enum):
    kFBStoryClipTimeWarpInterpolatorCustom:FBStoryClipTimeWarpInterpolatorType
    kFBStoryClipTimeWarpInterpolatorGoingFaster:FBStoryClipTimeWarpInterpolatorType
    kFBStoryClipTimeWarpInterpolatorGoingFasterReversed:FBStoryClipTimeWarpInterpolatorType
    kFBStoryClipTimeWarpInterpolatorLinear:FBStoryClipTimeWarpInterpolatorType
    kFBStoryClipTimeWarpInterpolatorLinearReversed:FBStoryClipTimeWarpInterpolatorType
    kFBStoryClipTimeWarpInterpolatorSlowingDown:FBStoryClipTimeWarpInterpolatorType
    kFBStoryClipTimeWarpInterpolatorSlowingDownReversed:FBStoryClipTimeWarpInterpolatorType
    kFBStoryClipTimeWarpInterpolatorSmoothedEnds:FBStoryClipTimeWarpInterpolatorType
    kFBStoryClipTimeWarpInterpolatorSmoothedEndsReversed:FBStoryClipTimeWarpInterpolatorType
class FBStoryGroupClipAlignmentType(_Enum):
    kFBStoryGroupClipAlignmentBeginningNextWithOffset:FBStoryGroupClipAlignmentType
    kFBStoryGroupClipAlignmentCurrentTimeline:FBStoryGroupClipAlignmentType
    kFBStoryGroupClipAlignmentEndPreviousWithOffset:FBStoryGroupClipAlignmentType
class FBStoryTrackBodyPart(_Enum):
    kFBStoryTrackBodyPartAll:FBStoryTrackBodyPart
    kFBStoryTrackBodyPartExtensions:FBStoryTrackBodyPart
    kFBStoryTrackBodyPartHead:FBStoryTrackBodyPart
    kFBStoryTrackBodyPartLeftArm:FBStoryTrackBodyPart
    kFBStoryTrackBodyPartLeftFoot:FBStoryTrackBodyPart
    kFBStoryTrackBodyPartLeftHand:FBStoryTrackBodyPart
    kFBStoryTrackBodyPartLeftLeg:FBStoryTrackBodyPart
    kFBStoryTrackBodyPartLeftShoulder:FBStoryTrackBodyPart
    kFBStoryTrackBodyPartLowerBody:FBStoryTrackBodyPart
    kFBStoryTrackBodyPartNone:FBStoryTrackBodyPart
    kFBStoryTrackBodyPartProps:FBStoryTrackBodyPart
    kFBStoryTrackBodyPartRightArm:FBStoryTrackBodyPart
    kFBStoryTrackBodyPartRightFoot:FBStoryTrackBodyPart
    kFBStoryTrackBodyPartRightHand:FBStoryTrackBodyPart
    kFBStoryTrackBodyPartRightLeg:FBStoryTrackBodyPart
    kFBStoryTrackBodyPartRightShoulder:FBStoryTrackBodyPart
    kFBStoryTrackBodyPartSpine:FBStoryTrackBodyPart
    kFBStoryTrackBodyPartUpperBody:FBStoryTrackBodyPart
class FBStoryTrackGhostShowMode(_Enum):
    kFBStoryTrackShowAllClips:FBStoryTrackGhostShowMode
    kFBStoryTrackShowCurrentTimeAdjacentClips:FBStoryTrackGhostShowMode
class FBStoryTrackRefMode(_Enum):
    kFBStoryTrackAdditive:FBStoryTrackRefMode
    kFBStoryTrackOverride:FBStoryTrackRefMode
class FBStoryTrackType(_Enum):
    kFBStoryTrackAnimation:FBStoryTrackType
    kFBStoryTrackAudio:FBStoryTrackType
    kFBStoryTrackCamera:FBStoryTrackType
    kFBStoryTrackCharacter:FBStoryTrackType
    kFBStoryTrackCommand:FBStoryTrackType
    kFBStoryTrackConstraint:FBStoryTrackType
    kFBStoryTrackShot:FBStoryTrackType
    kFBStoryTrackVideo:FBStoryTrackType
class FBSurfaceMode(_Enum):
    kFBSurfaceModeHigh:FBSurfaceMode
    kFBSurfaceModeHighNoNormals:FBSurfaceMode
    kFBSurfaceModeLow:FBSurfaceMode
    kFBSurfaceModeLowNoNormals:FBSurfaceMode
    kFBSurfaceModeRaw:FBSurfaceMode
class FBSurfaceType(_Enum):
    kFBSurfaceTypeBezier:FBSurfaceType
    kFBSurfaceTypeBezierQuadric:FBSurfaceType
    kFBSurfaceTypeBspline:FBSurfaceType
    kFBSurfaceTypeCardinal:FBSurfaceType
    kFBSurfaceTypeLinear:FBSurfaceType
class FBSyncActivationAndVisibilityMode(_Enum):
    kFBSyncMode_None:FBSyncActivationAndVisibilityMode
    kFBSyncMode_WithContolRig:FBSyncActivationAndVisibilityMode
    kFBSyncMode_WithOthersThanControlRig:FBSyncActivationAndVisibilityMode
class FBTCPIPSocketType(_Enum):
    kFBTCPIP_DGRAM:FBTCPIPSocketType
    kFBTCPIP_RAW:FBTCPIPSocketType
    kFBTCPIP_Stream:FBTCPIPSocketType
class FBTakeChangeType(_Enum):
    kFBTakeChangeAdded:FBTakeChangeType
    kFBTakeChangeClosed:FBTakeChangeType
    kFBTakeChangeMoved:FBTakeChangeType
    kFBTakeChangeNone:FBTakeChangeType
    kFBTakeChangeOpened:FBTakeChangeType
    kFBTakeChangeRemoved:FBTakeChangeType
    kFBTakeChangeRenamed:FBTakeChangeType
    kFBTakeChangeUpdated:FBTakeChangeType
class FBTakeSpanOnLoad(_Enum):
    kFBFrameAnimation:FBTakeSpanOnLoad
    kFBImportFromFile:FBTakeSpanOnLoad
    kFBLeaveAsIs:FBTakeSpanOnLoad
class FBTangentClampMode(_Enum):
    kFBTangentClampModeClamped:FBTangentClampMode
    kFBTangentClampModeNone:FBTangentClampMode
class FBTangentConstantMode(_Enum):
    kFBTangentConstantModeNext:FBTangentConstantMode
    kFBTangentConstantModeNormal:FBTangentConstantMode
class FBTangentCustomIndex(_Enum):
    kFBTangentCustomIndex0:FBTangentCustomIndex
    kFBTangentCustomIndex1:FBTangentCustomIndex
    kFBTangentCustomIndex2:FBTangentCustomIndex
class FBTangentMode(_Enum):
    kFBTangentModeAuto:FBTangentMode
    kFBTangentModeBreak:FBTangentMode
    kFBTangentModeClampProgressive:FBTangentMode
    kFBTangentModeTCB:FBTangentMode
    kFBTangentModeTimeIndependent:FBTangentMode
    kFBTangentModeUser:FBTangentMode
class FBTangentWeightMode(_Enum):
    kFBTangentWeightModeBoth:FBTangentWeightMode
    kFBTangentWeightModeNextLeft:FBTangentWeightMode
    kFBTangentWeightModeNone:FBTangentWeightMode
    kFBTangentWeightModeRight:FBTangentWeightMode
class FBTextJustify(_Enum):
    kFBTextJustifyCenter:FBTextJustify
    kFBTextJustifyLeft:FBTextJustify
    kFBTextJustifyRight:FBTextJustify
class FBTextStyle(_Enum):
    kFBTextStyleBold:FBTextStyle
    kFBTextStyleItalic:FBTextStyle
    kFBTextStyleNone:FBTextStyle
    kFBTextStyleUnderlined:FBTextStyle
class FBTextureBlendMode(_Enum):
    kFBTextureBlendAdditive:FBTextureBlendMode
    kFBTextureBlendModulate:FBTextureBlendMode
    kFBTextureBlendModulate2:FBTextureBlendMode
    kFBTextureBlendTranslucent:FBTextureBlendMode
class FBTextureMapping(_Enum):
    kFBTextureMappingCylindrical:FBTextureMapping
    kFBTextureMappingEnvironment:FBTextureMapping
    kFBTextureMappingProjection:FBTextureMapping
    kFBTextureMappingSpherical:FBTextureMapping
    kFBTextureMappingUV:FBTextureMapping
    kFBTextureMappingXY:FBTextureMapping
    kFBTextureMappingXZ:FBTextureMapping
    kFBTextureMappingYZ:FBTextureMapping
    kFBTextureNoMapping:FBTextureMapping
class FBTextureUseType(_Enum):
    kFBTextureUseAll:FBTextureUseType
    kFBTextureUseBumpNormalMap:FBTextureUseType
    kFBTextureUseColor:FBTextureUseType
    kFBTextureUseLightMap:FBTextureUseType
    kFBTextureUseShadowMap:FBTextureUseType
    kFBTextureUseSphereReflexionMap:FBTextureUseType
    kFBTextureUseSphericalReflexionMap:FBTextureUseType
class FBTimeMarkAction(_Enum):
    kFBTimeMarkAction_Loop:FBTimeMarkAction
    kFBTimeMarkAction_None:FBTimeMarkAction
    kFBTimeMarkAction_Stop:FBTimeMarkAction
class FBTimeMode(_Enum):
    kFBTimeMode1000Frames:FBTimeMode
    kFBTimeMode100Frames:FBTimeMode
    kFBTimeMode11988Frames:FBTimeMode
    kFBTimeMode120Frames:FBTimeMode
    kFBTimeMode23976Frames:FBTimeMode
    kFBTimeMode24Frames:FBTimeMode
    kFBTimeMode25Frames:FBTimeMode
    kFBTimeMode2997Frames:FBTimeMode
    kFBTimeMode2997Frames_Drop:FBTimeMode
    kFBTimeMode30Frames:FBTimeMode
    kFBTimeMode48Frames:FBTimeMode
    kFBTimeMode50Frames:FBTimeMode
    kFBTimeMode5994Frames:FBTimeMode
    kFBTimeMode60Frames:FBTimeMode
    kFBTimeMode72Frames:FBTimeMode
    kFBTimeMode96Frames:FBTimeMode
    kFBTimeModeCustom:FBTimeMode
    kFBTimeModeDefault:FBTimeMode
class FBTimeReferential(_Enum):
    kFBTimeReferentialAction:FBTimeReferential
    kFBTimeReferentialEdit:FBTimeReferential
    kFBTimeReferentialShot:FBTimeReferential
class FBToolPossibleDockPosition(_Enum):
    kFBToolPossibleDockPosBottom:FBToolPossibleDockPosition
    kFBToolPossibleDockPosLeft:FBToolPossibleDockPosition
    kFBToolPossibleDockPosNone:FBToolPossibleDockPosition
    kFBToolPossibleDockPosRight:FBToolPossibleDockPosition
    kFBToolPossibleDockPosTop:FBToolPossibleDockPosition
class FBTransportLoopMode(_Enum):
    kFBTransportLoopCurrentTake:FBTransportLoopMode
    kFBTransportLoopThroughAllTakes:FBTransportLoopMode
    kFBTransportNoLoop:FBTransportLoopMode
class FBTransportMode(_Enum):
    kFBTransportGoto:FBTransportMode
    kFBTransportGotoPrepare:FBTransportMode
    kFBTransportGotoReady:FBTransportMode
    kFBTransportJog:FBTransportMode
    kFBTransportJogPrepare:FBTransportMode
    kFBTransportJogReady:FBTransportMode
    kFBTransportPlay:FBTransportMode
    kFBTransportPlayPrepare:FBTransportMode
    kFBTransportPlayReady:FBTransportMode
    kFBTransportPlayReverse:FBTransportMode
    kFBTransportPlayReversePrepare:FBTransportMode
    kFBTransportPlayReverseReady:FBTransportMode
    kFBTransportShuttle:FBTransportMode
    kFBTransportShuttlePrepare:FBTransportMode
    kFBTransportShuttleReady:FBTransportMode
    kFBTransportStepBackward:FBTransportMode
    kFBTransportStepBackwardPrepare:FBTransportMode
    kFBTransportStepBackwardReady:FBTransportMode
    kFBTransportStepForward:FBTransportMode
    kFBTransportStepForwardPrepare:FBTransportMode
    kFBTransportStepForwardReady:FBTransportMode
    kFBTransportStop:FBTransportMode
    kFBTransportStopPost:FBTransportMode
    kFBTransportStopReady:FBTransportMode
class FBTransportPlaySpeed(_Enum):
    kFBSpeed_10x:FBTransportPlaySpeed
    kFBSpeed_1_10x:FBTransportPlaySpeed
    kFBSpeed_1_2x:FBTransportPlaySpeed
    kFBSpeed_1_3x:FBTransportPlaySpeed
    kFBSpeed_1_4x:FBTransportPlaySpeed
    kFBSpeed_1_5x:FBTransportPlaySpeed
    kFBSpeed_1x:FBTransportPlaySpeed
    kFBSpeed_2x:FBTransportPlaySpeed
    kFBSpeed_3x:FBTransportPlaySpeed
    kFBSpeed_4x:FBTransportPlaySpeed
    kFBSpeed_5x:FBTransportPlaySpeed
    kFBSpeed_ALL_FR:FBTransportPlaySpeed
    kFBSpeed_Custom:FBTransportPlaySpeed
class FBTransportSnapMode(_Enum):
    kFBTransportSnapModeNoSnap:FBTransportSnapMode
    kFBTransportSnapModePlayOnFrames:FBTransportSnapMode
    kFBTransportSnapModeSnapAndPlayOnFrames:FBTransportSnapMode
    kFBTransportSnapModeSnapOnFrames:FBTransportSnapMode
class FBTransportTimeFormat(_Enum):
    kFBTimeFormatFrame:FBTransportTimeFormat
    kFBTimeFormatTimecode:FBTransportTimeFormat
class FBTriggerStyle(_Enum):
    kFBTriggerStyleContinue:FBTriggerStyle
    kFBTriggerStyleCut:FBTriggerStyle
    kFBTriggerStyleToggle:FBTriggerStyle
class FBUpAxis(_Enum):
    kFBUpAxisY:FBUpAxis
    kFBUpAxisZ:FBUpAxis
class FBUseChnMode(_Enum):
    kFBUseChannelBoth:FBUseChnMode
    kFBUseChannelLeftOnly:FBUseChnMode
    kFBUseChannelRightOnly:FBUseChnMode
class FBVideoCodecMode(_Enum):
    FBVideoCodecAsk:FBVideoCodecMode
    FBVideoCodecStored:FBVideoCodecMode
    FBVideoCodecUncompressed:FBVideoCodecMode
class FBVideoFormat(_Enum):
    kFBVideoFormat_422:FBVideoFormat
    kFBVideoFormat_ABGR_32:FBVideoFormat
    kFBVideoFormat_ARGB_32:FBVideoFormat
    kFBVideoFormat_Any:FBVideoFormat
    kFBVideoFormat_BGRA_32:FBVideoFormat
    kFBVideoFormat_BGR_16:FBVideoFormat
    kFBVideoFormat_BGR_24:FBVideoFormat
    kFBVideoFormat_Other:FBVideoFormat
    kFBVideoFormat_RGBA_32:FBVideoFormat
    kFBVideoFormat_RGB_24:FBVideoFormat
class FBVideoInterlaceMode(_Enum):
    kFBVideoInterlaceFullFrameEven:FBVideoInterlaceMode
    kFBVideoInterlaceFullFrameOdd:FBVideoInterlaceMode
    kFBVideoInterlaceHalfFrameEven:FBVideoInterlaceMode
    kFBVideoInterlaceHalfFrameOdd:FBVideoInterlaceMode
    kFBVideoInterlaceNone:FBVideoInterlaceMode
class FBVideoLiveType(_Enum):
    kFBVideoLiveBasic:FBVideoLiveType
    kFBVideoLiveDefault:FBVideoLiveType
class FBVideoProxyMode(_Enum):
    kFBVideoProxyAlways:FBVideoProxyMode
    kFBVideoProxyNone:FBVideoProxyMode
    kFBVideoProxyOnPlay:FBVideoProxyMode
class FBVideoRenderDepth(_Enum):
    FBVideoRender24Bits:FBVideoRenderDepth
    FBVideoRender32Bits:FBVideoRenderDepth
    FBVideoRenderDepthCount:FBVideoRenderDepth
class FBVideoRenderFieldMode(_Enum):
    FBFieldModeCount:FBVideoRenderFieldMode
    FBFieldModeField0:FBVideoRenderFieldMode
    FBFieldModeField1:FBVideoRenderFieldMode
    FBFieldModeHalfField0:FBVideoRenderFieldMode
    FBFieldModeHalfField1:FBVideoRenderFieldMode
    FBFieldModeNoField:FBVideoRenderFieldMode
class FBVideoRenderViewingMode(_Enum):
    FBViewingModeCount:FBVideoRenderViewingMode
    FBViewingModeCurrent:FBVideoRenderViewingMode
    FBViewingModeModelsOnly:FBVideoRenderViewingMode
    FBViewingModeStandard:FBVideoRenderViewingMode
    FBViewingModeXRay:FBVideoRenderViewingMode
class FBVideoResolution(_Enum):
    kFBVideo_RES_1:FBVideoResolution
    kFBVideo_RES_128:FBVideoResolution
    kFBVideo_RES_16:FBVideoResolution
    kFBVideo_RES_1K:FBVideoResolution
    kFBVideo_RES_2:FBVideoResolution
    kFBVideo_RES_256:FBVideoResolution
    kFBVideo_RES_2K:FBVideoResolution
    kFBVideo_RES_32:FBVideoResolution
    kFBVideo_RES_4:FBVideoResolution
    kFBVideo_RES_4K:FBVideoResolution
    kFBVideo_RES_512:FBVideoResolution
    kFBVideo_RES_64:FBVideoResolution
    kFBVideo_RES_8:FBVideoResolution
    kFBVideo_RES_8K:FBVideoResolution
    kFBVideo_RES_FULL:FBVideoResolution
class FBVideoStorageMode(_Enum):
    kFBVideoStorageDisk:FBVideoStorageMode
    kFBVideoStorageDiskAsync:FBVideoStorageMode
    kFBVideoStorageMemory:FBVideoStorageMode
class FBViewerMode(_Enum):
    kFBViewerModeFourWindow:FBViewerMode
    kFBViewerModeOneWindow:FBViewerMode
    kFBViewerModeSchematic:FBViewerMode
    kFBViewerModeThreeWindow:FBViewerMode
    kFBViewerModeTwoWindow:FBViewerMode
class FBVisibilityState(_Enum):
    kFBVisibilityAll:FBVisibilityState
    kFBVisibilityAny:FBVisibilityState
    kFBVisibilityInvalid:FBVisibilityState
    kFBVisibilitySome:FBVisibilityState
class kDeviceIOs(_Enum):
    kIOPlayModeRead:kDeviceIOs
    kIOPlayModeWrite:kDeviceIOs
    kIOStopModeRead:kDeviceIOs
    kIOStopModeWrite:kDeviceIOs
class kDeviceOperations(_Enum):
    kOpAutoDetect:kDeviceOperations
    kOpDone:kDeviceOperations
    kOpInit:kDeviceOperations
    kOpReset:kDeviceOperations
    kOpStart:kDeviceOperations
    kOpStop:kDeviceOperations
class FBAddRegionParam():
    mMult:property
    mPos:property
    mRelative:property
    mType:property
    def __init__(self,arg2,arg3:FBAttachType,arg4:str,arg5:float=None):...
class FBAudioRenderOptions():
    BitDepthMode:FBAudioBitDepthMode
    ChannelMode:FBAudioChannelMode
    OutputFileName:str
    RateMode:FBAudioRateMode
    TimeSpan:FBTimeSpan
    def __init__(self):...
class FBBatchOptions():
    Character:property
    FrameAnimation:property
    InputDirectory:property
    InputFileFormat:property
    KeepCharacterConstraint:property
    KeepDummyBones:property
    OnContainsBatchTakesAction:property
    OnTakeExistAction:property
    OutputDirectory:property
    OutputFileFormat:property
    OverwriteScaling:property
    PlotToCharacter:property
    PlotToControlSet:property
    ProcessType:property
    SkeletonFile:property
    StartAnimationAtZero:property
    UseBatchSuffix:property
    UseSingleTake:property
    WriteRate:property
    WriteTranslation:property
    def __init__(self):...
class FBCallback():
    Callback:property
    EventType:property
    Wrapper:property
    def __init__(self,arg2,arg3:FBEventName,arg4):...
class FBCharacterPoseOptions():
    mCharacterPoseKeyingMode:FBCharacterPoseKeyingMode
    mMirrorPlaneEquation:FBVector4d
    mMirrorPlanePanAngle:float
    mMirrorPlaneTiltAngle:float
    mMirrorPlaneType:FBMirrorPlaneType
    mModelToMatch:FBModel
    def ClearFlag(self):
        """Clear all flags."""
        ...
    def GetFlag(self,Flag:FBCharacterPoseFlag)->bool:
        """Get a flag value.
        ### Parameters:
        - Flag: Flag to get.
        
        ### Returns:
        Value of the flag."""
        ...
    def SetFlag(self,Flag:FBCharacterPoseFlag,bValue:bool):
        """Set a flag value.
        ### Parameters:
        - Flag: Flag to set.
        - bValue: Value to set."""
        ...
    def __init__(self):...
class FBColor():
    @overload
    def CopyFrom(self,arg2:FBColor)->FBColor:...
    @overload
    def CopyFrom(self,arg2:list)->FBColor:...
    def GetBufferAddress(self)->int:...
    def GetList(self)->list:...
    def IsEqual(self,arg2:FBColor)->bool:...
    def NotEqual(self,arg2:FBColor)->bool:...
    @overload
    def __add__(self,arg2:FBColor)->object:...
    @overload
    def __add__(self,arg2)->object:...
    def __getitem__(self,Index:int)->float:...
    @overload
    def __iadd__(self,arg2:FBColor)->object:...
    @overload
    def __iadd__(self,arg2)->object:...
    @overload
    def __idiv__(self,arg2:FBColor)->object:...
    @overload
    def __idiv__(self,arg2)->object:...
    @overload
    def __imul__(self,arg2:FBColor)->object:...
    @overload
    def __imul__(self,arg2)->object:...
    @overload
    def __init__(self):...
    @overload
    def __init__(self,Vector:FBColor):...
    @overload
    def __init__(self,Red:float,Green:float,Blue:float):
        """### Parameters:
        - Red: Red component.
        - Green: Green component.
        - Blue: Blue component."""
        ...
    @overload
    def __init__(self,Value:float):
        """Constructor from array.
        ### Parameters:
        - Value: Array to take values from."""
        ...
    @overload
    def __init__(self,arg2:list):...
    @overload
    def __isub__(self,arg2:FBColor)->object:...
    @overload
    def __isub__(self,arg2)->object:...
    def __len__(self)->int:...
    @overload
    def __mul__(self,arg2:FBColor)->object:...
    @overload
    def __mul__(self,arg2)->object:...
    def __neg__(self)->object:...
    def __setitem__(self,arg2,arg3):...
    @overload
    def __sub__(self,arg2:FBColor)->object:...
    @overload
    def __sub__(self,arg2)->object:...
    @overload
    def __truediv__(self,arg2:FBColor)->object:...
    @overload
    def __truediv__(self,arg2)->object:...
class FBColorAndAlpha():
    @overload
    def CopyFrom(self,arg2:FBColorAndAlpha)->FBColorAndAlpha:...
    @overload
    def CopyFrom(self,arg2:list)->FBColorAndAlpha:...
    def GetBufferAddress(self)->int:...
    def GetList(self)->list:...
    def IsEqual(self,arg2:FBColorAndAlpha)->bool:...
    def NotEqual(self,arg2:FBColorAndAlpha)->bool:...
    @overload
    def __add__(self,arg2:FBColorAndAlpha)->object:...
    @overload
    def __add__(self,arg2)->object:...
    def __getitem__(self,Index:int)->float:...
    @overload
    def __iadd__(self,arg2:FBColorAndAlpha)->object:...
    @overload
    def __iadd__(self,arg2)->object:...
    @overload
    def __idiv__(self,arg2:FBColorAndAlpha)->object:...
    @overload
    def __idiv__(self,arg2)->object:...
    @overload
    def __imul__(self,arg2:FBColorAndAlpha)->object:...
    @overload
    def __imul__(self,arg2)->object:...
    @overload
    def __init__(self):...
    @overload
    def __init__(self,Vector:FBColorAndAlpha):...
    @overload
    def __init__(self,Red:float,Green:float,Blue:float,Alpha:float=1.0):
        """### Parameters:
        - Red: Red component.
        - Green: Green component.
        - Blue: Blue component.
        - Alpha: Alpha component(default=1.0)."""
        ...
    @overload
    def __init__(self,Value:FBColor):
        """Constructor from FBColorF.
        ### Parameters:
        - Value: FBColorF to take values from."""
        ...
    @overload
    def __init__(self,Value:list):
        """Constructor from FBColor .
        ### Parameters:
        - Value: FBColor to take values from."""
        ...
    @overload
    def __isub__(self,arg2:FBColorAndAlpha)->object:...
    @overload
    def __isub__(self,arg2)->object:...
    def __len__(self)->int:...
    @overload
    def __mul__(self,arg2:FBColorAndAlpha)->object:...
    @overload
    def __mul__(self,arg2)->object:...
    def __neg__(self)->object:...
    def __setitem__(self,arg2,arg3):...
    @overload
    def __sub__(self,arg2:FBColorAndAlpha)->object:...
    @overload
    def __sub__(self,arg2)->object:...
    @overload
    def __truediv__(self,arg2:FBColorAndAlpha)->object:...
    @overload
    def __truediv__(self,arg2)->object:...
class FBComponentList():
    def Add(self,Result:FBComponent):
        """Add two vectors together ( Result = pV1 + pV2 )
        ### Return values:
        - Result: Resulting vector.
        
        ### Parameters:"""
        ...
    def Clear(self):...
    def GetCount(self)->int:...
    def __getitem__(self,arg2)->object:...
    def __init__(self):
        """typedef FBArrayTemplate<FBComponent*> FBComponentList;
        Definition at line 284 of file fbcomponent.h ."""
        ...
    def __len__(self)->int:...
    def append(self,arg2:FBComponent):...
    def count(self)->int:...
    def removeAll(self):...
class FBConfigFile():
    def ClearFile(self):
        """Remove all content from the config file."""
        ...
    def Get(self,SectionName:str,ItemName:str,DefaultValue:str=0)->str:
        """Get an item's value.
        Get an item's value by looking inside a specific section of the config file.
        ### Parameters:
        - SectionName: Name of the section.
        - ItemName: Name of the item.
        - DefaultValue: Default value that will be returned if the item is not found.
        
        ### Returns:
        The value assigned to the item in the specified section of the config file, or the default value if not found."""
        ...
    def GetOrSet(self,SectionName:str,ItemName:str,Value:str,Comment:str=0)->bool:
        """Get a value from the config file and set it if it was not found.
        ### Parameters:
        - SectionName: Name of the section.
        - ItemName: Name of the item.
        - Value: Reference the the string that will contain the value of the item. If the item is not found in the file, it will be added with the initial value in this string.
        - Comment: Optional parameter that can be used to add a comment.
        
        ### Returns:
        true if the value was found or added, or false if the item was not found and could not be added to the file."""
        ...
    def Set(self,SectionName:str,ItemName:str,Value:str,Comment:str=0)->bool:
        """Set an item's value.
        Assign a value to an item in the config file. If the item does not exist, it will be created.
        ### Parameters:
        - SectionName: Name of the section.
        - ItemName: Name of the item.
        - Value: Value assigned to the item.
        - Comment: Optional parameter that can be used to add a comment.
        
        ### Returns:
        true if the item was written to the config file, false otherwise."""
        ...
    @overload
    def __init__(self,ConfigFileName:str,bVirtualMode:bool=False,bClearFile:bool=False):
        """This will open the desired config file from the [APPLICATION]/bin/config folder. The file will be created if it does not exists. By prefixing the character '@' to the file name, this will automatically prepend the current machine name to the config file, the way it is done for the other config files of the application.
        ### Parameters:
        - ConfigFileName: Name the config file to use.
        - bVirtualMode: Enable this to limit disk access, file will only be read at construction and written at destruction.
        - bClearFile: Remove all existing content from the config file."""
        ...
    @overload
    def __init__(self,ConfigFileName:str,ConfigFilePath:str,bVirtualMode:bool=False,bClearFile:bool=False):
        """This will open the desired config file in the designed folder. The file will be created if it does not exists. By prefixing the character '@' to the file name, this will automatically prepend the current machine name to the config file, the way it is done for the other config files of the application.
        ### Parameters:
        - ConfigFileName: Name the config file to use.
        - ConfigFilePath: Location where the file should reside. Missing directories will not be created.
        - bVirtualMode: Enable this to limit disk access, file will only be read at construction and written at destruction.
        - bClearFile: Remove all existing content from the config file."""
        ...
class FBConstraintInfo():
    def GetSnapRequested(self)->bool:
        """Was a 'snap' requested?
        ### Returns:
        true if 'snap' was requeststed."""
        ...
    def GetZeroRequested(self)->bool:
        """Was a 'zero' requested?
        ### Returns:
        true if 'zero' was requeststed."""
        ...
class FBConstructionOperation():
    def GetCommandId(self)->int:...
    def GetExecuteAsLocalOperation(self)->bool:...
    def GetLanguage(self)->str:...
    def GetLanguageVersion(self)->int:...
    def GetOrigin(self)->str:...
    def GetScript(self)->str:...
    def SetCommandId(self,commandId:int):
        """SetCommandId Set the operation's Id so that operation transactions can be resolved properly (eg: command 1 should go before command 2).
        Set this to -1 for new operations.
        ### Parameters:
        - commandId: Command Id. Defaults to -1."""
        ...
    def SetExecuteAsLocalOperation(self,bbIsLocal:bool):
        """SetExecuteAsLocalOperation Whether to execute this operation as local or remote.
        If this is set to false (remote) and an operation is sent to the construction history, it will also execute locally on this motionbuilder.
        ### Parameters:
        - bbIsLocal: Defaults to true (local)."""
        ...
    def SetLanguage(self,language:str):
        """SetLanguage Set the script language for this operation.
        Currently only "python" is supported.
        ### Parameters:
        - language: Langugage string. Default to construction history's code generator's language (Currently "python")."""
        ...
    def SetLanguageVersion(self,version:int):
        """SetLanguageVersion Set the script language interpreter's version that this operation should be interpreted with.
        ### Parameters:
        - version: Version number. Defaults to construction history's code generator's version (Currently 1)."""
        ...
    def SetOrigin(self,origin:str):
        """SetOrigin Set operation's original creator.
        For instance "localhost" or http://192.0.0.1:9000 . Should mostly be "localhost" for new operations.
        ### Parameters:
        - origin: Operation's Origin. Defaults to "localhost"."""
        ...
    def SetScript(self,script:str):
        """SetScript Set the script content for this operation.
        ### Parameters:
        - script: Script content as a string. Defaults to empty."""
        ...
    def __init__(self,arg2:str=None):...
class FBDeviceNotifyInfo():
    def GetLocalTime(self)->FBTime:
        """Get local time.
        ### Returns:
        Current local time."""
        ...
    def GetSyncCount(self)->int:
        """Return the wanted timer sync count (internal or external)
        ### Returns:
        sync count or -1 if no sync is present"""
        ...
    def GetSystemTime(self)->FBTime:
        """Get system time.
        ### Returns:
        Current system time."""
        ...
class FBDirMap():
    def Add(self,arg2:str,arg3:str):...
    def Clear(self):...
    def GetCount(self)->int:...
    def GetSource(self,arg2)->str:...
    def GetTarget(self,arg2)->str:...
    def Map(self,arg2:str)->str:...
    def __init__(self):...
class FBEvaluateInfo():
    def GetEvaluationID(self)->int:
        """Return the wanted timer sync count (internal or external).
        ### Returns:
        sync count or -1 if no sync is present"""
        ...
    def GetLocalTime(self)->FBTime:
        """Return local (scene) time.
        ### Returns:
        Local time."""
        ...
    def GetSyncCount(self)->int:
        """Return the wanted timer sync count (internal or external).
        ### Returns:
        sync count or -1 if no sync is present"""
        ...
    def GetSystemTime(self)->FBTime:
        """Return system time.
        ### Returns:
        System time."""
        ...
    def IsStop(self)->bool:
        """Is local time stopped? (ie: no animation).
        ### Returns:
        true if local time is stopped."""
        ...
class FBEvent():
    Type:int
class FBEventActivate(FBEvent):
    Data:property
class FBEventClipChange(FBEvent):
    def __init__(self):...
class FBEventConnectionDataNotify(FBEvent):
    Action:FBConnectionAction
    Plug:FBPlug
    def __init__(self):...
class FBEventConnectionKeyingNotify(FBEvent):
    Action:property
    Plug:property
    Property:property
    StartTime:property
    StopTime:property
    def __init__(self):...
class FBEventConnectionNotify(FBEvent):
    Action:FBConnectionAction
    ConnectionType:FBConnectionType
    DstPlug:FBPlug
    NewPlug:FBPlug
    SrcIndex:int
    SrcPlug:FBPlug
    def __init__(self):...
class FBEventConnectionStateNotify(FBEvent):
    Action:FBConnectionAction
    Plug:FBPlug
    def __init__(self):...
class FBEventDblClick(FBEvent):
    Selection:int
    def __init__(self):...
class FBEventDragAndDrop(FBEvent):
    Components:property
    Data:property
    PosX:int
    PosY:int
    State:FBDragAndDropState
    def Accept(self):
        """Accept a drag and drop sequence.
        This will cause the region in question to accept a drag and drop action when this event occurs."""
        ...
    def Add(self,Component:FBComponent,Id:int=0):
        """Add an item to the drag and drop list.
        ### Parameters:
        - Component: Item to add to the list.
        - Id: User-defined reference for the item (default = 0 )."""
        ...
    def Clear(self):
        """Clear drag and drop list."""
        ...
    def Get(self,Index:int)->FBComponent:
        """Get the FBComponent specified by Index from the Drag and Drop list.
        ### Parameters:
        - Index: Index in list where to get FBComponent .
        
        ### Returns:
        Handle to FBComponent in list at Index ."""
        ...
    def GetCount(self)->int:
        """Get the number of items in the DragAndDrop list.
        ### Returns:
        Number of items in DragAndDrop list."""
        ...
class FBEventEvalGlobalCallback(FBEvent):
    Timing:property
class FBEventExpose(FBEvent):
    ...
class FBEventFileChange(FBEvent):
    Path:str
class FBEventInput(FBEvent):
    InputType:FBInputType
    Key:int
    KeyState:int
    MouseButton:int
    X:int
    Y:int
class FBEventMenu(FBEvent):
    Id:int
    Name:str
class FBEventOverrideFileOpen(FBEvent):
    FilePath:str
    WillOverride:bool
    def __init__(self):...
class FBEventPlayerControlChange(FBEvent):
    def __init__(self):...
class FBEventResize(FBEvent):
    Height:int
    Width:int
    def __init__(self):...
class FBEventSceneChange(FBEvent):
    ChildComponent:FBComponent
    Component:FBComponent
    def __init__(self):...
class FBEventShow(FBEvent):
    Shown:bool
class FBEventSpread(FBEvent):
    Action:int
    Column:int
    Row:int
class FBEventTakeChange(FBEvent):
    Take:FBTake
    def __init__(self):...
class FBEventTransaction(FBEvent):
    IsBeginTransaction:bool
class FBEventTree(FBEvent):
    TreeNode:FBTreeNode
    Why:property
class FBEventTreeSelect(FBEvent):
    TreeNode:FBTreeNode
    def __init__(self):...
class FBEventVideoFrameRendering(FBEvent):
    EState:type
    FrameCount:property
    FrameNumber:property
    State:property
    eBeginRendering:EState
    eEndRendering:EState
    eRendering:EState
    def __init__(self):...
class FBFCurveEvent(FBEvent):
    Curve:FBFCurve
    CurveIndex:int
    CurveName:str
    EventType:FBFCurveEventType
    KeyIndexStart:int
    KeyIndexStop:int
    ParentAnimationNode:property
    ParentComponent:property
    ParentProperty:property
    def __init__(self):...
class FBFCurveKey():
    Bias:float
    Continuity:float
    ExtrapolationMode:FBExtrapolationMode
    Interpolation:FBInterpolation
    LeftBezierTangent:float
    LeftDerivative:float
    LeftTangentWeight:float
    MarkedForManipulation:bool
    RightBezierTangent:float
    RightDerivative:float
    RightTangentWeight:float
    Selected:bool
    TangentBreak:bool
    TangentClampMode:FBTangentClampMode
    TangentConstantMode:FBTangentConstantMode
    TangentCustomIndex:FBTangentCustomIndex
    TangentMode:FBTangentMode
    TangentWeightMode:FBTangentWeightMode
    Tension:float
    Time:FBTime
    Value:float
    def __init__(self):...
class FBFilePopup():
    Caption:str
    FileName:str
    Filter:str
    FullFilename:str
    Path:str
    Style:FBFilePopupStyle
    def Execute(self)->bool:
        """Execute file popup.
        ### Returns:
        true if OK is clicked by user."""
        ...
    def __init__(self):...
class FBFilterManager():
    FilterTypeNames:FBStringList
    def CreateFilter(self,FilterTypeName:str)->FBFilter:
        """Create a filter instance according to the filter type requested.
        ### Parameters:
        - FilterTypeName: String describing the type of the desired filter, as obtained from list FilterTypeNames.
        
        ### Returns:
        A pointer to a filter instance, or a `None` if the type name was invalid."""
        ...
    def __init__(self):...
class FBFolderPopup():
    Caption:str
    Path:str
    def Execute(self)->bool:
        """Execute folder popup.
        ### Returns:
        true if OK is clicked by user."""
        ...
    def __init__(self):...
class FBMatrix():
    def CopyFrom(self,arg2:FBMatrix)->FBMatrix:...
    def GetBufferAddress(self)->int:...
    def Identity(self):
        """Load identity matrix."""
        ...
    def Inverse(self):
        """Get Inversed matrix.
        ### Returns:
        the matrix Inversed."""
        ...
    def InverseProduct(self,Matrix:FBMatrix):
        """InverseProduct Matrix.
        ### Parameters:
        - Matrix: Matrix to Product.
        
        ### Returns:
        result matrix."""
        ...
    def IsEqual(self,arg2:FBMatrix)->bool:...
    def NotEqual(self,arg2:FBMatrix)->bool:...
    def Set(self,Value:list):
        """Set matrix from an array.
        ### Parameters:
        - Value: Array to intialize matrix from."""
        ...
    def Transpose(self):
        """Get Transposed matrix.
        ### Returns:
        the matrix Transposed."""
        ...
    def Validate(self)->bool:
        """Validated matrix.
        ### Returns:
        true if matrix Validated."""
        ...
    def __add__(self,arg2:FBMatrix)->object:...
    def __getitem__(self,arg2)->float:...
    def __iadd__(self,arg2:FBMatrix)->object:...
    @overload
    def __imul__(self,arg2:FBMatrix)->object:...
    @overload
    def __imul__(self,arg2)->object:...
    @overload
    def __init__(self):
        """Constructor Initializes matrix to identity."""
        ...
    @overload
    def __init__(self,Matrix:list):
        """### Parameters:
        - Matrix: Matrix to copy."""
        ...
    @overload
    def __init__(self,Value:FBMatrix):
        """### Parameters:
        - Value: Array to intialize matrix from."""
        ...
    def __isub__(self,arg2:FBMatrix)->object:...
    def __len__(self)->int:...
    @overload
    def __mul__(self,arg2:FBMatrix)->object:...
    @overload
    def __mul__(self,arg2)->object:...
    def __neg__(self)->object:...
    def __setitem__(self,arg2,arg3):...
    def __sub__(self,arg2:FBMatrix)->FBMatrix:
        """unary minus operator.
        ### Returns:
        this matrix as a const."""
        ...
class FBModelList():
    def Add(self,Result:FBModel):
        """Add two vectors together ( Result = pV1 + pV2 )
        ### Return values:
        - Result: Resulting vector.
        
        ### Parameters:"""
        ...
    def Clear(self):...
    def GetCount(self)->int:...
    def GetModel(self,arg2)->object:...
    def __getitem__(self,arg2)->object:...
    def __init__(self):
        """typedef class FBSDK_DLL
        Definition at line 241 of file fbmodel.h ."""
        ...
    def __len__(self)->int:...
    def append(self,arg2:FBModel):...
    def count(self)->int:...
    def removeAll(self):...
class FBMultiLangManager():
    Languages:FBStringList
    def GetCurrentLanguage(self)->str:
        """Obtain the current language.
        Query the current language used for the GUI.
        ### Returns:
        Will return the string associated with the current language used."""
        ...
    def SetCurrentLanguage(self,Language:str)->bool:
        """Set the current language.
        Change the current language to another available language.
        ### Parameters:
        - Language: The string corresponding to the desired language, as defined in property Languages.
        
        ### Returns:
        Indicate if the change of language was successful.
        
        ### Warning:
        Setting the current language will affect the lookup done with the functions FBGetMultiLangText, but will not have any effect on the GUI."""
        ...
    def __init__(self):...
class FBNormal():
    @overload
    def CopyFrom(self,arg2:FBNormal)->FBNormal:...
    @overload
    def CopyFrom(self,arg2:list)->FBNormal:...
    def CrossProduct(self,arg2:FBNormal)->FBNormal:...
    def DotProduct(self,arg2:FBNormal)->float:...
    def GetBufferAddress(self)->int:...
    def GetList(self)->list:...
    def IsEqual(self,arg2:FBNormal)->bool:...
    def Length(self)->float:
        """Get the length of a vector.
        ### Returns:
        Length of vector pV ."""
        ...
    def Normalize(self)->FBNormal:...
    def NotEqual(self,arg2:FBNormal)->bool:...
    def SquareLength(self)->float:...
    @overload
    def __add__(self,arg2:FBNormal)->object:...
    @overload
    def __add__(self,arg2)->object:...
    def __getitem__(self,arg2)->float:...
    @overload
    def __iadd__(self,arg2:FBNormal)->object:...
    @overload
    def __iadd__(self,arg2)->object:...
    @overload
    def __idiv__(self,arg2:FBNormal)->object:...
    @overload
    def __idiv__(self,arg2)->object:...
    @overload
    def __imul__(self,arg2:FBNormal)->object:...
    @overload
    def __imul__(self,arg2)->object:...
    @overload
    def __init__(self):
        """Normal.
        Definition at line 556 of file fbtypes.h ."""
        ...
    @overload
    def __init__(self,arg2:FBNormal):...
    @overload
    def __init__(self,arg2:float,arg3:float,arg4:float):...
    @overload
    def __init__(self,arg2):...
    @overload
    def __init__(self,arg2:list):...
    @overload
    def __isub__(self,arg2:FBNormal)->object:...
    @overload
    def __isub__(self,arg2)->object:...
    def __len__(self)->int:...
    @overload
    def __mul__(self,arg2:FBNormal)->object:...
    @overload
    def __mul__(self,arg2)->object:...
    def __neg__(self)->object:...
    def __setitem__(self,arg2,arg3:float):...
    @overload
    def __sub__(self,arg2:FBNormal)->object:...
    @overload
    def __sub__(self,arg2)->object:...
    @overload
    def __truediv__(self,arg2:FBNormal)->object:...
    @overload
    def __truediv__(self,arg2)->object:...
class FBObjectPoseMirrorOptions():
    mMirrorPlaneEquation:FBVector4d
    def ClearFlag(self):
        """Clear all flags."""
        ...
    def GetFlag(self,Flag:FBObjectPoseMirrorOptionsFlag)->bool:
        """Get a flag value.
        ### Parameters:
        - Flag: Flag to get.
        
        ### Returns:
        Value of the flag."""
        ...
    def SetFlag(self,Flag:FBObjectPoseMirrorOptionsFlag,bValue:bool):
        """Set a flag value.
        ### Parameters:
        - Flag: Flag to set.
        - bValue: Value to set."""
        ...
    def __init__(self):...
class FBObjectPoseOptions():
    mPoseTransformType:FBPoseTransformType
    mReferenceGRM:FBMatrix
    mReferenceGSM:FBMatrix
    mReferenceGT:FBVector4d
    def ClearFlag(self):
        """Clear all flags."""
        ...
    def GetFlag(self,Flag:FBObjectPoseOptionsFlag)->bool:
        """Get a flag value.
        ### Parameters:
        - Flag: Flag to get.
        
        ### Returns:
        Value of the flag."""
        ...
    def SetFlag(self,Flag:FBObjectPoseOptionsFlag,bValue:bool):
        """Set a flag value.
        ### Parameters:
        - Flag: Flag to set.
        - bValue: Value to set."""
        ...
    def __init__(self):...
class FBPickInfosList():
    def GetCount(self)->int:...
    def GetPickedModel(self,arg2)->object:...
    def __getitem__(self,arg2)->tuple:...
    def __init__(self):
        """typedef class FBSDK_DLL FBArrayTemplate<FBPickInfos> FBPickInfosList
        Definition at line 287 of file fbrenderer.h ."""
        ...
    def __len__(self)->int:...
    def count(self)->int:...
class FBPlotOptions():
    ConstantKeyReducerKeepOneKey:property
    EvaluateDeformation:property
    PlotAllTakes:property
    PlotAuxEffectors:property
    PlotLockedProperties:property
    PlotOnFrame:property
    PlotPeriod:property
    PlotTangentMode:property
    PlotTranslationOnRootOnly:property
    PreciseTimeDiscontinuities:property
    RotationFilterToApply:property
    UseConstantKeyReducer:property
    def __init__(self):...
class FBPlugList():
    def GetCount(self)->int:...
    def __getitem__(self,arg2)->object:...
    def __init__(self):
        """typedef FBArrayTemplate<FBPlug*> FBPlugList;
        Definition at line 193 of file fbplug.h ."""
        ...
    def __len__(self)->int:...
class FBProfileTaskCycle():
    def GetAvgMinMaxUsage(self)->tuple:
        """Get the task cycle's average, minimum and maximum usage.
        Results will vary on buffer size. When profiling is disabled all values are set to 1.
        ### Return values:
        - pAvg: Average time spend for computation of task (in micro seconds).
        - pMin: Minimum time spend for computation of task (in micro seconds).
        - pMax: Maximum time spend for computation of task (in micro seconds)."""
        ...
    def GetChild(self,Index:int)->FBProfileTaskCycle:
        """Get child task based on specific index.
        Can return `None` if child index is not used.
        ### Parameters:
        - Index: Child index.
        
        ### Returns:
        Child at given index."""
        ...
    def GetChildCount(self)->int:
        """Get number of child tasks.
        Task cycles are organized in a hierarchy which is dependent on the scene. Samples can be cumulative in the parent task cycle, or independent. For example, all character evaluation samples will be cumulated in one evaluation cycle.
        ### Returns:
        Number of child tasks."""
        ...
    def GetColor(self)->FBColor:
        """Get the color of the task cycle. Used in profiling Center for drawing."""
        ...
    def GetIndex(self)->int:
        """Get the unique registration index for each cycle."""
        ...
    def GetName(self)->str:
        """Get the name of task cycle."""
        ...
    def IsStarted(self)->bool:
        """Test to see if sampling has started."""
        ...
class FBProfileTimeEvent():
    def GetColor(self)->FBColor:
        """Get the color assigned to the event."""
        ...
    def GetComment(self)->str:
        """Get the comment for the event. Comments are not editable."""
        ...
    def GetThreadID(self)->int:
        """Get the thread ID used in the event execution."""
        ...
    def GetTime(self)->FBTime:
        """Get the time when the event occurred."""
        ...
    def GetTypeName(self)->str:
        """Get the event registered type name."""
        ...
    def IsSingleEvent(self)->bool:
        """Three types of events exits: single, start and end. Some actions that takes more time to execute or when other events can occur inbetween are collected with start time event at begin and end time event at finish."""
        ...
class FBPropertyListAnimationNode():
    def FindByLabel(self,NodeLabel:str)->FBAnimationNode:
        """Find an animation node by label name.
        ### Parameters:
        - NodeLabel: UI name of animation node to find.
        
        ### Returns:
        Handle to the animation node by the label of pNodeName ."""
        ...
    def __getitem__(self,Index:int)->FBAnimationNode:...
    def __len__(self)->int:...
class FBPropertyListDeviceInstrument():
    def __getitem__(self,Index:int)->FBDeviceInstrument:...
    def __len__(self)->int:...
class FBPropertyListDeviceOpticalMarker():
    def __getitem__(self,Index:int)->FBDeviceOpticalMarker:...
    def __len__(self)->int:...
class FBPropertyListFCurveKey():
    def __getitem__(self,Index:int)->FBFCurveKey:...
    def __len__(self)->int:...
class FBPropertyListManipulator():
    def __getitem__(self,Index:int)->FBManipulator:...
    def __len__(self)->int:...
class FBPropertyListMarkerSegment():
    def __getitem__(self,Index:int)->FBOpticalSegment:...
    def __len__(self)->int:...
class FBPropertyListModelMarkerOptical():
    def __getitem__(self,Index:int)->FBModelMarkerOptical:...
    def __len__(self)->int:...
class FBPropertyListModelTemplate():
    def __getitem__(self,Index:int)->FBModelTemplate:...
    def __len__(self)->int:...
class FBPropertyListModelTemplateBinding():
    def __getitem__(self,Index:int)->FBAnimationNode:...
    def __len__(self)->int:...
class FBPropertyListOpticalGap():
    def __getitem__(self,Index:int)->FBOpticalGap:...
    def __len__(self)->int:...
class FBPropertyListOpticalSegment():
    def __getitem__(self,Index:int)->FBOpticalSegment:...
    def __len__(self)->int:...
class FBPropertyListRigidBody():
    def __getitem__(self,Index:int)->FBRigidBody:...
    def __len__(self)->int:...
class FBPropertyListRigidBodyMarkers():
    def __getitem__(self,Index:int)->FBModelMarkerOptical:...
    def __len__(self)->int:...
class FBPropertyManager():
    def Find(self,PropertyName:str,bMultilangLookup:bool=True)->FBProperty:
        """Find a property, based on its name.
        ### Parameters:
        - PropertyName: Name of property to look for.
        - bMultilangLookup: When searching, indicate if the name lookup should also be done on the property name as shown in the GUI. (default = true)
        
        ### Returns:
        Handle to property found."""
        ...
    def FindPropertiesByName(self,PropertyNamePattern:str,PropList:list,bMultilangLookup:bool=True):
        """This function will query the property list for properties fulfilling a particular name pattern.
        ### Parameters:
        - PropertyNamePattern: Indicate the name pattern to search. This pattern can contain any amount of *. (ex: *tr*mod*scene )
        - PropList: List that contains the resulting properties matching the pattern
        - bMultilangLookup: When searching, indicate if the name lookup should also be done on the property name as shown in the GUI. (default = true)
        
        ### Note:
        The script FindPropertiesWithWildcard.py shows how to use this function."""
        ...
    def __getitem__(self,Index:int)->FBProperty:...
    def __len__(self)->int:...
class FBPropertyStateEvent(FBEvent):
    EventType:FBPropertyStateEventType
    ParentComponent:property
    Property:property
    def __init__(self):...
class FBPropertyViewDefinition():
    def IsFolder(self)->bool:
        """Is view a folder."""
        ...
    def IsOpen(self)->bool:
        """Is property view open at run time."""
        ...
    def IsSaved(self)->bool:
        """Is property view saved on view manager store."""
        ...
    def SetOpen(self,bTrue:bool,bApplyUpHierarchy:bool):
        """Set view open/closed at run time."""
        ...
    def SetSaved(self,bTrue:bool,bApplyUpHierarchy:bool):
        """Set view to be saved on view manager store."""
        ...
class FBPropertyViewList():
    def AddPropertyView(self,Property:FBProperty,Hierarchy:str)->FBPropertyViewDefinition:
        """Add property view.
        ### Parameters:
        - Property: Property to add.
        - Hierarchy: Hierarchy under which property view should be created, each level name is separated by dot (for example "Degrees of Freedom.Translation").
        
        ### Returns:
        created object (should not be called on non editable view list)."""
        ...
    def FindPropertyView(self,PropertyName:str)->FBPropertyViewDefinition:
        """Find property view for PropertyName in this list."""
        ...
    def IsEditable(self)->bool:
        """Is property view list editable."""
        ...
    def RemovePropertyView(self,PropertyViewDefinition:FBPropertyViewDefinition)->bool:
        """Remove property view from view list.
        ### Parameters:
        - PropertyViewDefinition: Property view definition to destroy.
        
        ### Returns:
        true when PropertyViewDefinition got removed and free (should not be called on non editable view list)."""
        ...
class FBPythonWrapper():
    OnUnbind:property
class FBPlug(FBPythonWrapper):
    ClassGroupName:str
    TypeInfo:int
    def BeginChange(self)->bool:
        """Begins a change on multiple plugs.
        ### Returns:
        A boolean indicating success (True) or failure (False)."""
        ...
    def ClassName(self)->str:
        """internal System vars.
        Reimplemented in FBCustomManager , and FBComponent ."""
        ...
    def ConnectDst(self,Dst:FBPlug,ConnectionType:FBConnectionType=FBConnectionType.kFBConnectionTypeNone)->bool:
        """Add a destination connection.
        ### Parameters:
        - Dst: Destination plug.
        - ConnectionType: Type of connection, taken from FBConnectionType. Default value should work in all cases.
        
        ### Returns:
        A boolean indicating success (True) or failure (False)"""
        ...
    def ConnectDstAt(self,Src_DstIndex:int,Dst:FBPlug,ConnectionType:FBConnectionType=FBConnectionType.kFBConnectionTypeNone)->bool:
        """Add a destination connection.
        ### Parameters:
        - Src_DstIndex: Index that tells where to add this destination connection in the source's connection list. if index is out of bound, and this destination connection will be appended at the end.
        - Dst: Destination plug.
        - ConnectionType: Type of connection, taken from FBConnectionType. Default value should work in all cases.
        
        ### Returns:
        A boolean indicating success (True) or failure (False)."""
        ...
    def ConnectSrc(self,Src:FBPlug,ConnectionType:FBConnectionType=FBConnectionType.kFBConnectionTypeNone)->bool:
        """Add a source connection.
        ### Parameters:
        - Src: Source plug.
        - ConnectionType: Type of connection, taken from FBConnectionType. Default value should work in all cases.
        
        ### Returns:
        A boolean indicating success (True) or failure (False)."""
        ...
    def ConnectSrcAt(self,Dst_SrcIndex:int,Src:FBPlug,ConnectionType:FBConnectionType=FBConnectionType.kFBConnectionTypeNone)->bool:
        """Add a source connection.
        ### Parameters:
        - Dst_SrcIndex: Index that tells where to add this source connection in the destination's connection list. if index is out of bound, and this source connection will be appended at the end.
        - Src: Source plug.
        - ConnectionType: Type of connection, taken from FBConnectionType. Default value should work in all cases.
        
        ### Returns:
        A boolean indicating success (True) or failure (False)."""
        ...
    def DisconnectAllDst(self):
        """Remove all destination connections."""
        ...
    def DisconnectAllSrc(self):
        """Remove all source connections."""
        ...
    def DisconnectDst(self,Dst:FBPlug)->bool:
        """Remove a destination connection.
        ### Parameters:
        - Dst: Destination plug.
        
        ### Returns:
        A boolean indicating success (True) or failure (False)."""
        ...
    def DisconnectDstAt(self,Index:int)->bool:
        """Remove a destination connection at a specified index.
        ### Parameters:
        - Index: Destination plug index.
        
        ### Returns:
        A boolean indicating success (True) or failure (False)."""
        ...
    def DisconnectSrc(self,Src:FBPlug)->bool:
        """Remove a source connection.
        ### Parameters:
        - Src: Source plug.
        
        ### Returns:
        A boolean indicating success (True) or failure (False)."""
        ...
    def DisconnectSrcAt(self,Index:int)->bool:
        """Remove a source connection at a specified index.
        ### Parameters:
        - Index: Source plug index.
        
        ### Returns:
        A boolean indicating success (True) or failure (False)."""
        ...
    def EndChange(self):
        """Ends a change on multiple plugs."""
        ...
    def GetContentModified(self,Flag:FBPlugModificationFlag)->bool:
        """Tell if the plug's content has changed.
        ### Parameters:
        - Flag: bitwise AND of content modification flags.
        
        ### Returns:
        true if content connection changed."""
        ...
    def GetDst(self,Index:int)->FBPlug:
        """Get a destination connection's plug at specified index.
        ### Parameters:
        - Index: Index of the destination connection's plug.
        
        ### Returns:
        Destination plug at specified index."""
        ...
    def GetDstCount(self)->int:
        """Get destination connection count.
        ### Returns:
        Total destinations connections count."""
        ...
    def GetDstType(self,Index:int)->FBConnectionType:
        """Get a destination connection's type at specified index.
        ### Parameters:
        - Index: Index of the destination connection's type.
        
        ### Returns:
        Destination connection's type at specified index."""
        ...
    def GetOwned(self,Index:int)->FBPlug:
        """Get the owned plug at specified index.
        ### Parameters:
        - Index: Index of the owned plug to get.
        
        ### Returns:
        The owned plug at specified index."""
        ...
    def GetOwnedCount(self)->int:
        """Get the owned plug count.
        ### Returns:
        The owned plug count."""
        ...
    def GetOwner(self)->FBPlug:
        """Get the owner of this plug.
        Very useful for properties since they are plugs too.
        ### Returns:
        The owner of this plug."""
        ...
    def GetPlugConnectionModifiedList(self,PlugList:FBPlugList,ConnectionModificatonFlag:FBPlugModificationFlag,bAddRemove:bool)->int:
        """Get plug's modified src/dst property/object connection added/removed List.
        ### Parameters:
        - PlugList: plug list to fill up.
        - ConnectionModificatonFlag: Src/Dst Property/Object connection modification flag.
        - bAddRemove: Ask for the added list if true, removed list if false.
        
        ### Returns:
        count of list;"""
        ...
    def GetSelfModified(self,Flag:FBPlugModificationFlag)->bool:
        """Tell if the plug's self has changed.
        ### Parameters:
        - Flag: bitwise AND of self modification flags.
        
        ### Returns:
        true if self changed"""
        ...
    def GetSrc(self,Index:int)->FBPlug:
        """Get a source connection's plug at specified index.
        ### Parameters:
        - Index: Index of the source connection's plug.
        
        ### Returns:
        Source plug at specified index."""
        ...
    def GetSrcCount(self)->int:
        """Get source connection count.
        ### Returns:
        Total sources connections count."""
        ...
    def GetSrcType(self,Index:int)->FBConnectionType:
        """Get a source connection's type at specified index.
        ### Parameters:
        - Index: Index of the source connection's type.
        
        ### Returns:
        Source connection's type at specified index."""
        ...
    def GetStatusFlag(self,Status:FBPlugStatusFlag)->bool:
        """Tell if the plug's status has changed.
        ### Parameters:
        - Status: bitwise AND of self modification flags.
        
        ### Returns:
        true if self changed"""
        ...
    def Is(self,TypeId:int)->bool:
        """Is( int TypeId )
        ### Parameters:
        - TypeId: Type Identification.
        
        ### Returns:
        True if Plug is a Instance of TypeId.
        Reimplemented in FBCustomManager , and FBComponent ."""
        ...
    def IsSDKComponent(self)->bool:
        """Return whether or not item is an SDK component."""
        ...
    @overload
    def MoveSrcAt(self,Index:int,AtIndex:int)->bool:
        """Move source connection at Index to AtIndex.
        ### Parameters:
        - Index: Plug current index.
        - AtIndex: Plug new index.
        
        ### Returns:
        A boolean indicating success (True) or failure (False).
        
        ### Remarks:
        This is not like the swap function since the connection at AtIndex is untouched."""
        ...
    @overload
    def MoveSrcAt(self,Src:FBPlug,AtSrc:FBPlug)->bool:
        """Move source connection Src to the position of AtSrc.
        ### Parameters:
        - Src: Plug.
        - AtSrc: Plug that mark where we want to insert (will insert before this one).
        
        ### Returns:
        A boolean indicating success (True) or failure (False).
        
        ### Remarks:
        This is not like the swap function since the connection at AtSrc is untouched."""
        ...
    @staticmethod
    def PrintClassDefinitions():
        """Print out internal Class (ID) Definition table.
        For internal debug purpose only."""
        ...
    def ReplaceDstAt(self,Index:int,Dst:FBPlug)->bool:
        """Replace a destination connection at a specified index.
        ### Parameters:
        - Index: Destination plug index.
        - Dst: Plug that will replace the other at index.
        
        ### Returns:
        A boolean indicating success (True) or failure (False)."""
        ...
    def ReplaceSrcAt(self,Index:int,Src:FBPlug)->bool:
        """Replace a source connection at a specified index.
        ### Parameters:
        - Index: Source plug index.
        - Src: Plug that will replace the other at index.
        
        ### Returns:
        A boolean indicating success (True) or failure (False)."""
        ...
    def RevertModification(self,Flag:FBPlugModificationFlag=FBPlugModificationFlag.kFBAllModifiedMask)->bool:
        """Revert the plug's modification to original status.
        ### Parameters:
        - Flag: the type of modification to be reverted.
        
        ### Returns:
        true if revert successfully."""
        ...
    def SetContentModified(self,Flag:FBPlugModificationFlag,bBool:bool):
        """Set the plug's owned property/object's modification flag.
        ### Parameters:
        - Flag: bitwise AND of content modification flags.
        - bBool: true if content has modification."""
        ...
    def SetSelfModified(self,Flag:FBPlugModificationFlag,bBool:bool):
        """Set the plug's self modification flag.
        ### Parameters:
        - Flag: bitwise AND of self modification flags.
        - bBool: true if self changed."""
        ...
    def SetStatusFlag(self,Status:FBPlugStatusFlag,bValue:bool):
        """Set the plug's status flag.
        ### Parameters:
        - Status: bitwise AND of status flags.
        - bValue: true if status has modification."""
        ...
    def SwapSrc(self,IndexA:int,IndexB:int)->bool:
        """Swap source connection at index A with source connection at index B.
        ### Parameters:
        - IndexA: Plug index.
        - IndexB: Other plug index.
        
        ### Returns:
        A boolean indicating success (True) or failure (False)."""
        ...
class FBRenderOptions():
    def GetIDBufferPickingAlphaThreshold(self)->float:...
    def GetRenderFrameId(self)->int:...
    def GetRenderingCamera(self)->object:...
    def GetViewerOptions(self)->FBViewingOptions:...
    def IsIDBufferPicking(self)->bool:...
    def IsIDBufferRendering(self)->bool:...
    def IsOfflineRendering(self)->bool:...
class FBProperty(FBPlug):
    Data:property
    Name:property
    def AllowsLocking(self)->bool:
        """### Returns:
        true if property can be locked"""
        ...
    def AsString(self,Flag:FBDataAsStringFlag=FBDataAsStringFlag.kFBDataAsStringUI)->str:
        """Get the property value as a string.
        ### Parameters:
        - Flag: Indicates the returned string to be used for UI or storage. It defaults to kFBDataAsStringUI.
        
        ### Returns:
        The string version of the property.
        Reimplemented in FBPropertyStringList ."""
        ...
    def EnumList(self,Index:int)->str:
        """Return the string of an enum value.
        ### Parameters:
        - Index: Enum value to get string for.
        
        ### Returns:
        String value of enum specified by Index ."""
        ...
    def GetEnumStringList(self,bCreateIt:bool=False)->FBStringList:
        """String list for enum properties.
        ### Parameters:
        - bCreateIt: Create a new list if necessary.
        
        ### Returns:
        the pointer to the string list.."""
        ...
    def GetMax(self)->float:
        """### Returns:
        Maximum value for the property."""
        ...
    def GetMin(self)->float:
        """### Returns:
        Minimum value for the property."""
        ...
    def GetName(self)->str:
        """Get the property's name.
        ### Returns:
        The property's name."""
        ...
    def GetPropertyFlag(self,Flag:FBPropertyFlag)->bool:
        """### Parameters:
        - Flag: Flag to test if it is True or False.
        
        ### Returns:
        If the flag is True, the function returns True and vice-versa.
        
        ### Warning:
        Flags are not saved into or read from a FBX file."""
        ...
    def GetPropertyFlags(self)->int:
        """### Returns:
        Return all flags at once."""
        ...
    def GetPropertyType(self)->FBPropertyType:
        """Get the property's type.
        ### Returns:
        The property's type.
        Reimplemented in FBPropertyStringList , FBPropertyEvent , and FBPropertyListComponentBase ."""
        ...
    def GetPropertyTypeName(self)->str:
        """Get the property's type name.
        ### Returns:
        The property's type name."""
        ...
    def GetReferencedProperty(self)->FBProperty:
        """Get the referenced property, in the case of this property is a reference property (see the IsReferenceProperty() method).
        ### Returns:
        The referenced property, or a null pointer if this property is not a reference property."""
        ...
    def GetSubMemberCount(self)->int:
        """### Returns:
        Number of sub-members."""
        ...
    def HasSomethingLocked(self)->bool:
        """### Returns:
        true if property or any of its members is locked"""
        ...
    def IsAnimatable(self)->bool:...
    def IsInternal(self)->bool:...
    def IsList(self)->bool:
        """Verify if property is of this type.
        ### Returns:
        true if property is of type.
        Reimplemented in FBPropertyStringList ."""
        ...
    def IsLocked(self)->bool:
        """### Returns:
        true if property is locked"""
        ...
    def IsMaxClamp(self)->bool:
        """Indicate if maximum value clamping will be applied on user input value.
        ### Returns:
        true if property the value will be clamped to a maximum value."""
        ...
    def IsMemberLocked(self,Index:int)->bool:
        """### Parameters:
        - Index: Index of the sub-member of the property to check.
        
        ### Returns:
        true if property sub-member is locked"""
        ...
    def IsMinClamp(self)->bool:
        """Indicate if minimum value clamping will be applied on user input value.
        ### Returns:
        true if property the value will be clamped to a minimum value."""
        ...
    def IsObjectList(self)->bool:
        """Indicate if is an instance of FBPropertyListObject .
        ### Warning:
        A FBPropertyListObject will also return true on a call to ' IsList() '."""
        ...
    def IsReadOnly(self)->bool:
        """Is property read-only?
        ### Returns:
        true if property is read-only."""
        ...
    def IsReferenceProperty(self)->bool:...
    def IsTextureConnectableProperty(self)->bool:...
    def IsUserProperty(self)->bool:...
    def ModifyPropertyFlag(self,Flag:FBPropertyFlag,bValue:bool):
        """### Parameters:
        - Flag: The flag to switch to True or False.
        - bValue: The value to set about this flag.
        
        ### Warning:
        Flags are not saved into or read from a FBX file."""
        ...
    def NotifyEnumStringListChanged(self):
        """Notify system that the enum list was modified."""
        ...
    def OriValueAsString(self)->str:
        """Get the property original value (before any modification) as string.
        ### Returns:
        returns the original value of the property in string with format same as AsString(kDataAsStringPersistence)"""
        ...
    def SetLocked(self,bLocked:bool):
        """### Parameters:
        - bLocked: True if the property is to be locked, false if it is to be unlocked."""
        ...
    def SetMax(self,Max:float,bForceMaxClamp:bool=False):
        """### Parameters:
        - Max: Maximum value of the property.
        - bForceMaxClamp: Force clamping to maximum value of the property."""
        ...
    def SetMemberLocked(self,Index:int,bLocked:bool):
        """### Parameters:
        - Index: Index of the sub-member of the property to lock or unlock.
        - bLocked: True if the sub-member is to be locked, false if it is to be unlocked."""
        ...
    def SetMin(self,Min:float,bForceMinClamp:bool=False):
        """### Parameters:
        - Min: Minimum value of the property.
        - bForceMinClamp: Force clamping to minimum value of the property."""
        ...
    def SetName(self,Name:str):
        """Set the property's name.
        ### Parameters:
        - Name: New name for the property."""
        ...
    def SetString(self,String:str)->bool:
        """Set the property value from a string.
        ### Parameters:
        - String: String to set property value from, with format same as AsString(kFBDataAsStringPersistence)
        
        ### Returns:
        True if it was possible.
        Reimplemented in FBPropertyStringList ."""
        ...
class FBComponent(FBPlug):
    Components:FBPropertyListComponent
    FullName:property
    LongName:str
    Name:str
    OwnerNamespace:property
    Parents:FBPropertyListComponent
    PropertyList:FBPropertyManager
    Selected:bool
    def DisableObjectFlags(self,Flags:FBObjectFlag):
        """Disable a specific Object Flags.
        ### Parameters:
        - Flags: Flags to disable."""
        ...
    def EnableObjectFlags(self,Flags:FBObjectFlag):
        """Enable a specific Object Flags.
        ### Parameters:
        - Flags: Flags to enable."""
        ...
    def FBCreate(self)->bool:
        """Open Reality Creation function.
        ### Returns:
        Outcome of creation (true/false).
        Reimplemented in FBDeviceCamera , FBDeviceSync , FBDeviceOptical , FBManipulator , FBDevice , FBConsole , FBCustomManager , FBAssetFolder , FBAssetFile , FBDeviceCameraLayout , and FBDeviceOpticalLayout ."""
        ...
    def FBDelete(self):
        """Open Reality deletion function.
        Reimplemented from FBPlug .
        Reimplemented in FBLayeredTexture , FBStoryGroupClip , FBStoryClip , FBStoryTrack , FBStoryFolder , FBScene , FBMotionClip , FBModel , FBKeyingGroup , FBImage , FBSet , FBGroup , FBFolder , FBTake , FBAnimationLayer , FBAnimationStack , FBFCurveCustomTangent , FBFCurve , FBCharacterFace , FBActorFace , FBCharacterExtension , FBCharacter , FBActor , FBAudioClip , and FBGenericMenu ."""
        ...
    def FBDestroy(self):
        """Open Reality destruction function.
        Reimplemented in FBDeviceCamera , FBDeviceSync , FBDeviceOptical , FBDevice , FBConsole , and FBDeviceCameraLayout ."""
        ...
    def GetObjectFlags(self)->FBObjectFlag:
        """Get all Object Flags (concatenated).
        ### Returns:
        Get all object flags in one call. Flags can be concatenated."""
        ...
    def GetObjectStatus(self,Status:FBObjectStatus)->bool:
        """Check to see if an object status is enabled.
        ### Parameters:
        - Status: Status to query."""
        ...
    def GetOwnerFileReference(self)->FBFileReference:
        """Get the owner FileReference object.
        ### Returns:
        the owner FileReference object"""
        ...
    def HardSelect(self):
        """Selects the object, and emits a hard select event for UI update notification."""
        ...
    def HasObjectFlags(self,Flags:FBObjectFlag)->bool:
        """Check whether a specific object flag is enabled.
        ### Parameters:
        - Flags: Flags to check if they are present.
        
        ### Returns:
        True if all flags in Flags are enabled."""
        ...
    def ProcessNamespaceHierarchy(self,NamespaceAction:FBNamespaceAction,NamespaceName:str,ReplaceTo:str=None,bAddRight:bool=True)->bool:
        """New Namespace name should only contains alphabet, digit and '_', Can't start with digit. This recursive function goes through the whole hierarchy (children) to add/replace the prefix. If you need to work on a single object, use the ProcessObjectPrefix function.
        ### Parameters:
        - NamespaceAction: Which operation to do on the hierarchy (children).
        - NamespaceName: The Namespace name on Add/Delete or the prefix to replace in case of replace.
        - ReplaceTo: The new Namespace Name or `None` in case of add or delete.
        - bAddRight: Whether to add the namespace on right-most or left-most side or other namespace.
        
        ### Returns:
        return true if process successful."""
        ...
    def ProcessObjectNamespace(self,NamespaceAction:FBNamespaceAction,NamespaceName:str,ReplaceTo:str=None,bAddRight:bool=True)->bool:
        """New Namespace name should only contains alphabet, digit and '_', Can't start with digit. This function is the same as ProcessNamespaceHierarchy except that it applies only on the current object and not to the object's children.
        ### Parameters:
        - NamespaceAction: Which operation to do on the hierarchy (children).
        - NamespaceName: The Namespace name on Add/Delete or the prefix to replace in case of replace.
        - ReplaceTo: The new Namespace Name or `None` in case of add or delete.
        - bAddRight: Whether to add the namespace on right-most or left-most side or other namespace.
        
        ### Returns:
        return true if process successful."""
        ...
    def PropertyAdd(self,Property:FBProperty)->int:
        """Add a property to the component's property manager.
        ### Parameters:
        - Property: The property to add to the property manager.
        
        ### Returns:
        Index in the property array where property was inserted."""
        ...
    def PropertyAddReferenceProperty(self,ReferenceProperty:FBProperty)->bool:
        """Add a reference property to the component's property manager.
        ### Parameters:
        - ReferenceProperty: The property to from an other object to add a reference to (property cannot be a custom ORSDK property).
        
        ### Returns:
        True if the reference property could be added."""
        ...
    def PropertyCreate(self,Name:str,Type:FBPropertyType,DataType:str,bAnimatable:bool,bIsUser:bool,ReferenceSource:FBProperty)->FBProperty:
        """Create user or dynamic property.
        ### Parameters:
        - Name: The name of the property.
        - Type: Type of the property. See enum FBPropertyType.
        - DataType: DataType of the property.
        - bAnimatable: To specify if the property can be animated.
        - bIsUser: To specify if the property is available as a custom property or dynamic and attached to the object.
        - ReferenceSource: Specifies the property that a reference refers to."""
        ...
    def PropertyGetModifiedList(self,PropList:FBPlugModificationFlag)->FBPropertyList:
        """Get list of properties which have been modified since last loading.
        ### Parameters:
        - PropList: property list to hold the modified properties."""
        ...
    def PropertyRemove(self,Property:FBProperty):
        """Remove a Property from the component's Property manager.
        If the property was dynamically allocated, it is deleted.
        ### Parameters:
        - Property: The property to remove from the property manager."""
        ...
    def SetObjectFlags(self,Flags:FBObjectFlag):
        """### Parameters:
        - Flags: Set flag values. Note: this function overwrites all flags with those passed in parameter."""
        ...
    def SetObjectStatus(self,Status:FBObjectStatus,bValue:bool):
        """Enable/Disable a specific Object Status.
        ### Parameters:
        - Status: Status to change.
        - bValue: Value to change the status to."""
        ...
class FBPropertyVector4d(FBProperty):
    def __getitem__(self,arg2)->float:...
    def __len__(self)->int:...
    def __setitem__(self,arg2,arg3):...
class FBReferenceTime(FBComponent):
    Count:int
    CurrentTimeReferenceID:int
    ItemIndex:int
    def Add(self,Name:str)->int:
        """Add a reference time to list.
        ### Parameters:
        - Name: Name of time to add the list.
        
        ### Returns:
        Unique ID of the reference time, use this ID to access the reference time in the future."""
        ...
    def GetReferenceTimeName(self,ID:int)->str:
        """Get the name of a time reference.
        ### Parameters:
        - ID: ID of the time reference whose name will be returned.
        
        ### Returns:
        Name of reference time with the ID ."""
        ...
    def GetTime(self,ID:int,System:FBTime)->FBTime:
        """Get a reference time.
        ### Parameters:
        - ID: ID of reference to get.
        - System: System time.
        
        ### Returns:
        Reference time at pIndex ."""
        ...
    def GetUniqueIDList(self)->list:
        """Get list of currently available IDs."""
        ...
    def Remove(self,ID:int):
        """Remove a reference time from the list.
        ### Parameters:
        - ID: ID of reference time to remove."""
        ...
    def SetTime(self,ID:int,ReferenceTime:FBTime,System:FBTime):
        """Set a reference time.
        ### Parameters:
        - ID: ID of reference time set.
        - ReferenceTime: Time to use as reference time.
        - System: System time."""
        ...
    def __init__(self):...
class FBPropertyViewManager(FBComponent):
    def AddPropertyView(self,ClassName:str,PropertyName:str,Hierarchy:str)->FBPropertyViewDefinition:
        """Add property view to global ('All') view set.
        ### Parameters:
        - ClassName: Property owner class name (ClassName if won't be found, a new entry for this class is created).
        - PropertyName: Property name.
        - Hierarchy: Hierarchy under which property view should be created, each level name is separated by dot (for example "Degrees of Freedom.Translation").
        
        ### Note:
        This call should be used on library registration, doesn't cause tool refresh.
        
        ### Returns:
        created object."""
        ...
    def CreatePropertyList(self,Object:FBComponent,ViewType:FBPropertyViewType,Name:str)->FBPropertyViewList:
        """Create new property view list.
        ### Parameters:
        - Object: Property view set attached to.
        - ViewType: Property view set type.
        - Name: Name for new view list.
        
        ### Returns:
        created object."""
        ...
    def FindPropertyList(self,Object:FBComponent,ViewType:FBPropertyViewType,Name:str)->FBPropertyViewList:
        """Find property view list.
        ### Parameters:
        - Object: Property view set attached to.
        - ViewType: Property view set type.
        - Name: Name of view set.
        
        ### Returns:
        Found property view set object or NULL."""
        ...
    def HidePropertyView(self,ClassName:str,PropertyName:str,bHide:bool):
        """Hide property view in global ('All') view set.
        ### Parameters:
        - ClassName: Property owner class name.
        - PropertyName: Property name.
        - bHide: Show/Hide.
        
        ### Note:
        This call should be used on library registration, doesn't cause tool refresh."""
        ...
    def RefreshPropertyViews(self):
        """Force refresh of browsing property tool."""
        ...
    def RemovePropertyList(self,Object:FBComponent,ViewType:FBPropertyViewType,Name:str)->bool:
        """Remove property view list (only if editable).
        ### Parameters:
        - Object: Property view set attached to.
        - ViewType: Property view set type.
        - Name: Name for property view list.
        
        ### Returns:
        True if successful."""
        ...
    def RemovePropertyView(self,ClassName:str,PropertyName:str)->bool:
        """Remove property view from global ('All') view set.
        ### Parameters:
        - ClassName: Property owner class name.
        - PropertyName: Property name.
        
        ### Returns:
        true if succeed (should not be call on system views).
        
        ### Note:
        This call should be used on library registration, doesn't cause tool refresh."""
        ...
    def __init__(self):...
class FBPropertyVector3d(FBProperty):
    def __getitem__(self,arg2)->float:...
    def __len__(self)->int:...
    def __setitem__(self,arg2,arg3):...
class FBPropertyVector2d(FBProperty):
    def __getitem__(self,arg2)->float:...
    def __len__(self)->int:...
    def __setitem__(self,arg2,arg3):...
class FBPropertyTimeCode(FBProperty):
    ...
class FBPropertyTime(FBProperty):
    ...
class FBPropertyStringList(FBProperty):
    def __contains__(self,arg2)->bool:...
    def __delitem__(self,arg2:int):...
    def __getitem__(self,Index:int)->str:...
    def __len__(self)->int:...
    def __setitem__(self,arg2,arg3):...
    def append(self,arg2):...
    def count(self,arg2)->int:...
    def findFromReference(self,arg2)->int:...
    def getReferenceAt(self,arg2)->int:...
    def insert(self,arg2:int,arg3):...
    @overload
    def pop(self)->object:...
    @overload
    def pop(self,arg2)->object:...
    def remove(self,arg2):...
    def removeAll(self):...
    def setReferenceAt(self,arg2,arg3):...
class FBPropertyString(FBProperty):
    ...
class FBPropertyListTreeNode(FBProperty):
    def __contains__(self,arg2)->bool:...
    def __delitem__(self,arg2:int):...
    def __getitem__(self,Index:int)->FBTreeNode:...
    def __len__(self)->int:...
    def __setitem__(self,arg2,arg3):...
    def append(self,arg2):...
    def count(self,arg2)->int:...
    def insert(self,arg2:int,arg3):...
    @overload
    def pop(self)->object:...
    @overload
    def pop(self,arg2)->object:...
    def remove(self,arg2):...
    def removeAll(self):...
class FBPropertyListComponent(FBProperty):
    def __contains__(self,arg2)->bool:...
    def __delitem__(self,arg2:int):...
    def __getitem__(self,arg2)->object:...
    def __len__(self)->int:...
    def __setitem__(self,arg2,arg3):...
    def append(self,arg2):...
    def count(self,arg2)->int:...
    def insert(self,arg2:int,arg3):...
    @overload
    def pop(self)->object:...
    @overload
    def pop(self,arg2)->object:...
    def remove(self,arg2):...
    def removeAll(self):...
class FBPropertyList(FBProperty):
    def __contains__(self,arg2)->bool:...
    def __delitem__(self,arg2:int):...
    def __getitem__(self,arg2)->object:...
    def __len__(self)->int:...
    def __setitem__(self,arg2,arg3):...
    def append(self,arg2):...
    def count(self,arg2)->int:...
    def insert(self,arg2:int,arg3):...
    @overload
    def pop(self)->object:...
    @overload
    def pop(self,arg2)->object:...
    def remove(self,arg2):...
    def removeAll(self):...
class FBPropertyListVideoOut(FBPropertyListComponent):
    ...
class FBPropertyListVideoIn(FBPropertyListComponent):
    ...
class FBPropertyListVideoClip(FBPropertyListComponent):
    ...
class FBPropertyListUserObject(FBPropertyListComponent):
    ...
class FBPropertyListTexture(FBPropertyListComponent):
    ...
class FBPropertyListTake(FBPropertyListComponent):
    ...
class FBPropertyListStoryTrack(FBPropertyListComponent):
    ...
class FBPropertyListStorySubTrack(FBPropertyListComponent):
    ...
class FBPropertyListStoryFolder(FBPropertyListComponent):
    ...
class FBPropertyListStoryDetails(FBPropertyListComponent):
    ...
class FBPropertyListStoryClip(FBPropertyListComponent):
    ...
class FBPropertyListShader(FBPropertyListComponent):
    ...
class FBPropertyListSet(FBPropertyListComponent):
    ...
class FBPropertyListRendererCallback(FBPropertyListComponent):
    ...
class FBPropertyListPose(FBPropertyListComponent):
    ...
class FBPropertyListPivot(FBPropertyListComponent):
    ...
class FBPropertyListPhysicalProperties(FBPropertyListComponent):
    ...
class FBPropertyListObjectPose(FBPropertyListComponent):
    ...
class FBPropertyListObject(FBPropertyListComponent):
    def GetSingleConnect(self)->bool:
        """Get if the connection support only one connection.
        ### Returns:
        true is the connection support only one connection."""
        ...
    def SetSingleConnect(self,bSingleConnect:bool):
        """Set if the connection is single or multiple.
        ### Parameters:
        - bSingleConnect: set to true for only one connection allowed."""
        ...
class FBPropertyListNote(FBPropertyListComponent):
    ...
class FBPropertyListNamespace(FBPropertyListComponent):
    ...
class FBPropertyListMotionClip(FBPropertyListComponent):
    ...
class FBPropertyListModelSkeleton(FBPropertyListComponent):
    ...
class FBPropertyListModelOptical(FBPropertyListComponent):
    ...
class FBPropertyListModel(FBPropertyListComponent):
    ...
class FBPropertyListMaterial(FBPropertyListComponent):
    ...
class FBPropertyListMarkerSet(FBPropertyListComponent):
    ...
class FBPropertyListLight(FBPropertyListComponent):
    ...
class FBPropertyListKeyingGroup(FBPropertyListComponent):
    ...
class FBPropertyListHandle(FBPropertyListComponent):
    ...
class FBPropertyListHUDElement(FBPropertyListComponent):
    ...
class FBPropertyListHUD(FBPropertyListComponent):
    ...
class FBPropertyListGroup(FBPropertyListComponent):
    ...
class FBPropertyListFolder(FBPropertyListComponent):
    ...
class FBPropertyListFileReference(FBPropertyListComponent):
    ...
class FBPropertyListDevice(FBPropertyListComponent):
    ...
class FBPropertyListDeformer(FBPropertyListComponent):
    ...
class FBPropertyListDeck(FBPropertyListComponent):
    ...
class FBPropertyListControlSet(FBPropertyListComponent):
    ...
class FBPropertyListConstraintSolver(FBPropertyListComponent):
    ...
class FBPropertyListActor(FBPropertyListComponent):
    ...
class FBPropertyListActorFace(FBPropertyListComponent):
    ...
class FBPropertyListAudioClip(FBPropertyListComponent):
    ...
class FBPropertyListAudioIn(FBPropertyListComponent):
    ...
class FBPropertyListAudioOut(FBPropertyListComponent):
    ...
class FBPropertyListBox(FBPropertyListComponent):
    ...
class FBPropertyListCamera(FBPropertyListComponent):
    ...
class FBPropertyListCharacter(FBPropertyListComponent):
    ...
class FBPropertyListCharacterExtension(FBPropertyListComponent):
    ...
class FBPropertyListCharacterFace(FBPropertyListComponent):
    ...
class FBPropertyListCharacterMarkerSet(FBPropertyListComponent):
    ...
class FBPropertyListCharacterPose(FBPropertyListComponent):
    ...
class FBPropertyListConstraint(FBPropertyListComponent):
    ...
class FBPropertyInt(FBProperty):
    ...
class FBPropertyFloat(FBProperty):
    ...
class FBPropertyEnum(FBProperty):
    ...
class FBPropertyDouble(FBProperty):
    ...
class FBPropertyComponent(FBProperty):
    ...
class FBPropertyColorAndAlpha(FBProperty):
    def __getitem__(self,arg2)->float:...
    def __len__(self)->int:...
    def __setitem__(self,arg2,arg3):...
class FBPropertyColor(FBProperty):
    def __getitem__(self,arg2)->float:...
    def __len__(self)->int:...
    def __setitem__(self,arg2,arg3):...
class FBPropertyBool(FBProperty):
    ...
class FBPropertyAnimatable(FBProperty):
    def AllowsMuting(self)->bool:
        """### Returns:
        true if property can be muted"""
        ...
    def GetAnimationNode(self)->FBAnimationNode:
        """Get the animation node for the property.
        ### Returns:
        Animation node for property. `None` is returned if property is not animated."""
        ...
    def GetBox(self)->FBBox:
        """Get the owner box.
        ### Returns:
        Handle to the owning box (i.e. model)."""
        ...
    def GetColor(self,Index:int)->FBColor:
        """Get the color of a particular FCurve of the property.
        ### Parameters:
        - Index: Index of the FCurve to get the color.
        
        ### Returns:
        The color of the FCurve at the specified index, a default FBColor object if the index is invalid."""
        ...
    def GetDataTypeName(self)->str:
        """Get the property datatype name.
        ### Returns:
        Datatype of property as a character string."""
        ...
    def HasSomethingMuted(self)->bool:
        """### Returns:
        true if property or any of its members is muted"""
        ...
    def IsAnimated(self)->bool:
        """Is the property animated.
        This is true if the property has an FCurve associated to it.
        ### Returns:
        true if animated, false if not animated."""
        ...
    def IsFocused(self)->bool:
        """Is the property focused (keyable).
        ### Returns:
        Current focus (keyable) state for the property."""
        ...
    def IsFocusedChild(self,Index:int)->bool:
        """Get the focus (keyable) state of child component.
        ### Parameters:
        - Index: Index of the child FCurve component.
        
        ### Returns:
        true if the component is in focus, false otherwise"""
        ...
    def IsMemberMuted(self,Index:int)->bool:
        """### Parameters:
        - Index: Index of the sub-member of the property to check.
        
        ### Returns:
        true if property sub-member is muted"""
        ...
    def IsMuted(self)->bool:
        """### Returns:
        true if property is muted"""
        ...
    def Key(self):
        """Key the property."""
        ...
    def KeyAt(self,Time:FBTime):
        """Key the property at time (t).
        ### Parameters:
        - Time: Time at which to insert the key."""
        ...
    def KeyRemoveAt(self,Time:FBTime):
        """Remove the key at time (t).
        ### Parameters:
        - Time: Time at which to insert the key."""
        ...
    def OriIsAnimated(self)->bool:...
    def ResetColor(self,Index:int)->bool:
        """Revert the FCurves to their default color.
        ### Parameters:
        - Index: Index of the FCurve to reset the color, use -1 to reset the color for all FCurves of the property.
        
        ### Returns:
        true if the color was reverted to its default value, false otherwise"""
        ...
    def SetAnimated(self,bState:bool,bCheckLocked:bool=False):
        """Set the animation state of the property.
        ### Parameters:
        - bState: State of animation for property, true to animate, false to remove curves.
        - bCheckLocked: Decides whether to check the locked status."""
        ...
    def SetColor(self,Color:FBColor,Index:int)->bool:
        """Set the color of the FCurves for the property.
        ### Parameters:
        - Color: Color to set for the FCurve(s).
        - Index: Index of the FCurve to set the new color, use -1 to set the color for all FCurves.
        
        ### Returns:
        true if the color was changed, false otherwise"""
        ...
    def SetFocus(self,bState:bool):
        """Set the property's focus (keyable) state.
        ### Parameters:
        - bState: Focus (keyable) state to set for the property."""
        ...
    def SetFocusChild(self,Index:int,bState:bool):
        """Set the focus (keyable) state of child component.
        ### Parameters:
        - Index: Index of the child FCurve component.
        - bState: Focus (keyable) state to set for the property component.
        
        ### Returns:
        true if the operation was successful, false otherwise"""
        ...
    def SetMemberMuted(self,Index:int,bMuted:bool):
        """### Parameters:
        - Index: Index of the sub-member of the property to mute or unmute.
        - bMuted: True if the sub-member is to be muted, false if it is to be unmuted."""
        ...
    def SetMuted(self,bMuted:bool):
        """### Parameters:
        - bMuted: True if the property is to be muted, false if it is to be unmuted."""
        ...
class FBPropertyAction(FBProperty):
    ...
class FBPropertyAnimatableVector4d(FBPropertyAnimatable):
    def __getitem__(self,arg2)->float:...
    def __len__(self)->int:...
    def __setitem__(self,arg2,arg3):...
class FBPropertyAnimatableVector3d(FBPropertyAnimatable):
    def __getitem__(self,arg2)->float:...
    def __len__(self)->int:...
    def __setitem__(self,arg2,arg3):...
class FBPropertyAnimatableVector2d(FBPropertyAnimatable):
    def __getitem__(self,arg2)->float:...
    def __len__(self)->int:...
    def __setitem__(self,arg2,arg3):...
class FBPropertyAnimatableUInt64(FBPropertyAnimatable):
    ...
class FBPropertyAnimatableTimeCode(FBPropertyAnimatable):
    ...
class FBPropertyAnimatableTime(FBPropertyAnimatable):
    ...
class FBPropertyAnimatableInt64(FBPropertyAnimatable):
    ...
class FBPropertyAnimatableInt(FBPropertyAnimatable):
    ...
class FBPropertyAnimatableEnum(FBPropertyAnimatable):
    ...
class FBPropertyAnimatableDouble(FBPropertyAnimatable):
    @overload
    def __add__(self,arg2:FBPropertyAnimatableDouble)->object:...
    @overload
    def __add__(self,arg2)->object:...
    def __float__(self)->object:...
    @overload
    def __mul__(self,arg2:FBPropertyAnimatableDouble)->object:...
    @overload
    def __mul__(self,arg2)->object:...
    def __radd__(self,arg2)->object:...
    def __rmul__(self,arg2)->object:...
    def __rsub__(self,arg2)->object:...
    def __rtruediv__(self,arg2)->object:...
    @overload
    def __sub__(self,arg2:FBPropertyAnimatableDouble)->object:...
    @overload
    def __sub__(self,arg2)->object:...
    @overload
    def __truediv__(self,arg2:FBPropertyAnimatableDouble)->object:...
    @overload
    def __truediv__(self,arg2)->object:...
class FBPropertyAnimatableColorAndAlpha(FBPropertyAnimatable):
    def __getitem__(self,arg2)->float:...
    def __len__(self)->int:...
    def __setitem__(self,arg2,arg3):...
class FBPropertyAnimatableColor(FBPropertyAnimatable):
    def __getitem__(self,arg2)->float:...
    def __len__(self)->int:...
    def __setitem__(self,arg2,arg3):...
class FBPropertyAnimatableBool(FBPropertyAnimatable):
    ...
class FBPropertyAnimatableAction(FBPropertyAnimatable):
    ...
class FBRenderer(FBComponent):
    AdvancedLightingMode:bool
    AdvancedMaterialMode:bool
    AutoEvaluate:bool
    Background:bool
    CurrentCamera:FBCamera
    CurrentPaneCallbackIndex:int
    CurrentPaneCallbackPrefIndex:int
    DisplayNormals:bool
    DisplaySetUpdateId:int
    DisplayableGeometryCount:int
    DisplayableLightCount:int
    FrustumCulling:bool
    HideManipulatorsOnManip:bool
    HideManipulatorsOnPlayback:bool
    IDBufferDisplay:bool
    IDBufferPicking:bool
    IDBufferPickingAlpha:float
    PickingEnabled:bool
    RegisteredCallbackCount:int
    RendererCallbacks:FBPropertyListRendererCallback
    RendererUpdateId:int
    Scene:FBScene
    SelectionForceSnapPointsDisplay:bool
    SelectionOverride:bool
    SelectionOverrideColor:FBColor
    SelectionOverrideTransparency:float
    ShowStats:bool
    UseCameraSwitcher:bool
    def ArrangeAllInSchematic(self,Mode:FBArrangeMode):
        """Request to arrange all objects in schematic view .
        ### Parameters:
        - Mode: Arrange mode."""
        ...
    def ArrangeObjectsInSchematicFromModel(self,Model:FBModel)->bool:
        """Request to arrange a node's tree in the Schematic View, given a starting node.
        ### Parameters:
        - Model: The starting node from which the arrange operation is requested.
        
        ### Returns:
        True if the operation is successful, false otherwise."""
        ...
    def ArrangeSelectedObjectsInSchematic(self):
        """Request to arrange selected objects in schematic view ."""
        ...
    def CreateSchematicBookmark(self,BookmarkName:str)->bool:
        """Create a new bookmark in the Schematic View.
        ### Parameters:
        - BookmarkName: The new bookmark name.
        
        ### Returns:
        True if the operation is successful, false otherwise. False is returned if the bookmark name is empty or if a bookmark with the given name already exists."""
        ...
    def DeleteSchematicBookmark(self,BookmarkName:str)->bool:
        """Delete a bookmark from the Schematic View.
        ### Parameters:
        - BookmarkName: The bookmark name to delete.
        
        ### Returns:
        True if the operation is successful, false otherwise. False is returned if the bookmark name is empty or if no bookmark exists with the given name."""
        ...
    def FrameCurrentCameraWithModels(self,bAll:bool)->bool:
        """Frame the current camera either with all models or with the currently selected models.
        ### Parameters:
        - bAll: true to frame with all models.
        
        ### Returns:
        true if successful."""
        ...
    def GetCameraInPane(self,PaneIndex:int)->FBCamera:
        """Return the camera displayed in the given pane index.
        If the Schematic View is displayed in the pane associated with the given pane index, the returned camera is the camera that would be displayed if the Schematic View was deactivated. If the Camera Switcher is on in the pane associated with the given pane index, the returned camera is the switcher's current camera.
        Note: To operate current camera in Camera Switcher, it is recommended to use FBCameraSwitcher() .
        ### Parameters:
        - PaneIndex: The pane index.
        
        ### Returns:
        The camera used in the given pane index, `None` if the pane index is invalid."""
        ...
    def GetCurrentSchematicBookmarkName(self)->str:
        """Return the current bookmark name used by the Schematic View.
        ### Returns:
        The current bookmark name used by the Schematic View. An empty string is returned if there is no current bookmark."""
        ...
    def GetDisplayableGeometry(self,Index:int)->FBModel:
        """Get the displayable geometry model.
        Those geometry models which have Show property ON are considered as "displayable".
        ### Parameters:
        - Index: displayable geometry model index to query.
        
        ### Returns:
        displayable geometry model."""
        ...
    def GetDisplayableGeometryInCameraFrustum(self,ModelList:FBModelList,Camera:FBCamera):
        """Get a list of displayable geometry inside given camera's frustum.
        This function will return conservative result. It's possible for some geometry outside of the frustum will be considered to be visible, but it will not skip any real visible geometry. This function should only be called in the main rendering thread.
        ### Parameters:
        - ModelList: ModelList holding the return models.
        - Camera: use current camera if NULL.
        
        ### Returns:
        Reference to ModelList. if ModelList is `None` return a const reference to internal static FBModelList and consecutive call to this function will invalidate the result of previous call."""
        ...
    def GetDisplayableLight(self,Index:int)->FBLight:
        """Get the displayable light.
        Those light models which have Show property ON are considered as "displayable".
        ### Parameters:
        - Index: displayable light index to query.
        
        ### Returns:
        displayable light."""
        ...
    def GetLastPickInfoList(self,PickInfosList:FBPickInfosList)->int:
        """Return the last picking info list in the current view pane.
        ### Parameters:
        - PickInfosList: The list of pick infos.
        
        ### Returns:
        number of item in the list."""
        ...
    def GetPaneCount(self)->int:
        """Return the number of panes displayed in the viewer's layout.
        ### Returns:
        The number of panes displayed."""
        ...
    def GetSchematicBookmarkNames(self)->FBStringList:
        """Return the bookmark names available in the Schematic View.
        ### Returns:
        A string list containing the bookmark names available in the Schematic View. An empty list is returned if no bookmark is available."""
        ...
    def GetSchematicNodesBoundingBox(self,bConsiderCollapsedNodes:bool)->bool:
        """Returns the bounding box (top, left, bottom, right) used by all the Schematic View nodes.
        ### Parameters:
        - bConsiderCollapsedNodes: True to also consider nodes which are not visible because collapsed, false otherwise.
        ### Returns:
        True if the operation is successful, false otherwise (e.g. the Schematic View has any node in it, etc.)."""
        ...
    def GetSchematicNodesBoundingBoxFromModel(self,Model:FBModel,bConsiderCollapsedNodes:bool)->bool:
        """Returns the bounding box (top, left, bottom, right) of a node's tree in the Schematic View, given a starting node.
        ### Parameters:
        - Model: The starting node from which the bounding box tree is requested.
        - bConsiderCollapsedNodes: True to also consider nodes which are not visible because collapsed, false otherwise.
        ### Returns:
        True if the operation is successful, false otherwise (e.g. the starting node is not in the Schematic View, etc.)."""
        ...
    def GetSchematicViewPaneIndex(self)->int:
        """Return the pane index of the pane displaying the Schematic View.
        ### Returns:
        The pane index of the pane displaying the Schematic View, -1 if the Schematic View is currently not displayed in any pane."""
        ...
    def GetSelectedPaneIndex(self)->int:
        """Return the pane index associated with the selected pane in the active viewer's layout.
        ### Returns:
        The selected pane index."""
        ...
    def GetViewingOptions(self)->FBViewingOptions:
        """Obtain the current viewing options.
        ### Returns:
        A structure that can be queried and updated for a call to SetViewingOptions."""
        ...
    def IsCameraSwitcherInPane(self,PaneIndex:int)->bool:
        """Return the Camera Switcher activeness in the given pane index.
        If the Schematic View is displayed in the pane associated with the given pane index, the returned value is the value that would be returned if the Schematic View was deactivated.
        ### Parameters:
        - PaneIndex: The pane index.
        
        ### Returns:
        True if the Camera Switcher is active in the pane associated with the given pane index, False otherwise."""
        ...
    def IsCurrentSchematicBookmarkDirty(self)->bool:
        """Return if the current bookmark used by the Schematic View is dirty or not.
        ### Returns:
        True if the current bookmark is dirty, false otherwise. False is returned if there is no current bookmark."""
        ...
    def IsModelInsideCameraFrustum(self,Geometry:FBModel,Camera:FBCamera)->bool:
        """To tell if given model is located inside camera's frustum.
        This function will return conservative result. It's possible for some geometry outside of the frustum will be considered to be visible, but it will not skip any real visible geometry. This function should only be called in the main rendering thread.
        ### Parameters:
        - Geometry: the geometry to be queried.
        - Camera: use current camera if NULL.
        
        ### Returns:
        true if Model is inside camera frustum."""
        ...
    def KeyboardInput(self,KeyIndex:FBDeviceKeyboardKey,bKeyState:bool,bIsTrigger:bool=False):
        """Keyboard input.
        ### Parameters:
        - KeyIndex: Key index. (See "enum FBDeviceKeyboardKey" above for supported keys)
        - bKeyState: Key state. (True == key is down, False == key is up)
        - bIsTrigger: When setting bKeyState to True, resets key state to False right after operation."""
        ...
    def MouseInput(self,X:int,Y:int,InputType:FBInputType,ButtonKey:int,Modifier:FBInputModifier,WheelDeltaValue:int=0,Layer:int=-1)->bool:
        """Mouse input.
        ### Parameters:
        - X: X position.
        - Y: Y position.
        - InputType: Type of input.
        - ButtonKey: Button/Key pressed.
        - Modifier: Modifier pressed (CTRL/ALT/SHIFT).
        - WheelDeltaValue: Mouse wheel delta value
        - Layer: Rendering layer ID(default=-1).
        
        ### Returns:
        true if successful."""
        ...
    def MouseInputNormalized(self,X:float,Y:float,InputType:FBInputType,ButtonKey:int,Modifier:FBInputModifier,WheelDeltaValue:int=None,Layer:int=-1,PaneId:int=-1)->bool:
        """Mouse input.
        ### Parameters:
        - X: X position, normalized to the range of [0, 1] in the view port dimension.
        - Y: Y position, normalized to the range of [0, 1] in the view port dimension.
        - InputType: Type of input.
        - ButtonKey: Button/Key pressed.
        - Modifier: Modifier pressed (CTRL/ALT/SHIFT).
        - WheelDeltaValue: Mouse wheel delta value
        - Layer: Rendering layer ID(default=-1).
        - PaneId: specify which pane's dimension used for normalization, default (-1) for the whole viewer.
        
        ### Returns:
        true if successful."""
        ...
    def OGLModelDisplay(self,arg2:FBRenderOptions,arg3:FBModel):...
    def OGLSetupSceneLights(self,RenderOptions:FBRenderOptions):
        """Setup the scene lights in OpenGL.
        ### Parameters:
        - RenderOptions: See FBRenderOptions for more detail."""
        ...
    def Pick(self,X:int,Y:int,PickInfosList:FBPickInfosList)->bool:
        """Object picking selection.
        ### Parameters:
        - X: X position.
        - Y: Y position.
        - PickInfosList: The list of pick infos."""
        ...
    def PickNormalized(self,X:float,Y:float,PickInfosList:FBPickInfosList,bNeedIntersectPosition:bool=False)->bool:
        """Object picking selection.
        ### Parameters:
        - X: X position, normalized to the range of [0, 1] in the view port dimension.
        - Y: Y position, normalized to the range of [0, 1] in the view port dimension.
        - PickInfosList: The list of pick infos.
        - bNeedIntersectPosition: require valid intersection position if true, this will take more time to process, and not reliable with very dense mesh."""
        ...
    def PreRender(self,Layer:int=-1)->bool:
        """PreRenders one frame (needed for some shaders) This functions destroys the frame buffer content and must be called every time a render is called the typical order of call must be Renderer->Prerender // at this point the frame buffer is garbage -Clear the ogl -Do your render functions Renderer->Render.
        ### Parameters:
        - Layer: Rendering layer ID(default=-1).
        
        ### Returns:
        true if successful."""
        ...
    def RectPick(self,X1:int,Y1:int,X2:int,Y2:int,PickInfosList:FBPickInfosList)->bool:
        """Object rectangle selection.
        ### Parameters:
        - X1: Left upper corner X position.
        - Y1: Left upper corner y position.
        - X2: Right bottom corner X position.
        - Y2: Right bottom corner y position.
        - PickInfosList: The list of pick infos."""
        ...
    def RectPickNormalized(self,X1:float,Y1:float,X2:float,Y2:float,PickInfosList:FBPickInfosList,PaneId:int=-1)->bool:
        """Object rectangle selection.
        ### Parameters:
        - X1: Left upper corner X position, normalized to the range of [0, 1] in the viewport dimension.
        - Y1: Left upper corner y position, normalized to the range of [0, 1] in the viewport dimension.
        - X2: Right bottom corner X position, normalized to the range of [0, 1] in the viewport dimension.
        - Y2: Right bottom corner y position, normalized to the range of [0, 1] in the viewport dimension.
        - PickInfosList: The list of pick infos.
        - PaneId: specify which pane's dimension used for normalization, default (-1) for the whole viewer."""
        ...
    def RenameSchematicBookmark(self,OldBookmarkName:str,NewBookmarkName:str)->bool:
        """Rename a bookmark in the Schematic View.
        ### Parameters:
        - OldBookmarkName: The bookmark name to rename.
        - NewBookmarkName: The new bookmark name.
        
        ### Returns:
        True if the operation is successful, false otherwise. False is returned if the old/new bookmark name is empty, if the old bookmark doesn't exist or if a bookmark with the new given name already exists."""
        ...
    def Render(self,Layer:int=-1)->bool:
        """Renders one frame.
        ### Parameters:
        - Layer: Rendering layer ID(default=-1).
        
        ### Returns:
        true if successful."""
        ...
    def RenderBegin(self,X:int,Y:int,W:int,H:int)->bool:
        """### Parameters:
        - X: X position where to render.
        - Y: Y position where to render.
        - W: Width of render area.
        - H: Hight of render area."""
        ...
    def RenderEnd(self)->bool:
        """### Remarks:
        Must be called at the end of rendering."""
        ...
    def SelectSchematicBookmark(self,BookmarkName:str)->bool:
        """Select an existing bookmark in the Schematic View and use it as the current bookmark.
        ### Parameters:
        - BookmarkName: The bookmark name to select.
        
        ### Returns:
        True if the operation is successful, false otherwise. False is returned if the bookmark name is empty or if no bookmark exists with the given name."""
        ...
    def SetCameraInPane(self,Camera:FBCamera,PaneIndex:int):
        """Set the camera to display in the given pane index.
        If the Schematic View is displayed in the pane associated with the given pane index, the camera will be displayed when the Schematic View will be deactivated from this pane.
        Note: If current pane uses Camera Switcher, it will be set to use Camera, rather than old behavior that still uses Camera Switcher and sets Camera to be Camera Switcher's current camera, which introduce a Zombie Camera Switcher problem. By using Camera, the problem is gone.
        Note: To operate current camera in Camera Switcher, it is recommended to use FBCameraSwitcher() .
        ### Parameters:
        - Camera: The camera to set.
        - PaneIndex: The pane index."""
        ...
    def SetCameraSwitcherInPane(self,PaneIndex:int,bActive:bool):
        """Set/Remove the Camera Switcher in the given pane index.
        To specify which camera the Camera Switcher should be displaying, use the SetCameraInPane method. If the Schematic View is displayed in the pane associated with the given pane index, the camera switcher will be displayed (if activated) when the Schematic View will be deactivated from this pane.
        ### Parameters:
        - PaneIndex: The pane index.
        - bActive: True to activate the Camera Switcher in the given pane, False to remove it."""
        ...
    def SetPaneCount(self,PaneCount:int):
        """Set the number of panes to display in the viewer's layout.
        ### Parameters:
        - PaneCount: The number of panes to display."""
        ...
    def SetSchematicViewInPane(self,PaneIndex:int,bActive:bool):
        """Set/Remove the Schematic View in the given pane index.
        When activating the Schematic View in the pane, if the Schematic View is already activated in another pane, the Schematic View will be removed from latter before being activated into the new pane.
        ### Parameters:
        - PaneIndex: The pane index.
        - bActive: True to activate the Schematic View in the given pane, False to remove it."""
        ...
    def SetSelectedPaneIndex(self,PaneIndex:int)->bool:
        """Select the pane associated with the given pane index in the active viewer's layout.
        ### Parameters:
        - PaneIndex: The pane index.
        
        ### Returns:
        True if the operation is successful, False otherwise."""
        ...
    def SetViewingOptions(self,Options:FBViewingOptions)->bool:
        """Set the viewing options.
        ### Parameters:
        - Options: See FBViewingOptions for more detail."""
        ...
    def SetViewport(self,X:int,Y:int,W:int,H:int):
        """Must be called before inputing if the same renderer is used on multiple views/cameras in the same application.
        ### Parameters:
        - X: X position where to render.
        - Y: Y position where to render.
        - W: Width of render area.
        - H: Hight of render area."""
        ...
    def UpdateCurrentSchematicBookmark(self)->bool:
        """Update the current bookmark in the Schematic View.
        ### Returns:
        True if the operation is successful, false otherwise. False is returned if there is no current bookmark."""
        ...
class FBProgress(FBComponent):
    Caption:str
    Percent:int
    Text:str
    def ProgressBegin(self):
        """Start progress, must be called before set Text & Percent property."""
        ...
    def ProgressDone(self):
        """End progress, must be called to reset progress bar UI to normal status after finishing the task."""
        ...
    def UserRequestCancell(self)->bool:
        """Return true if User is pressing and holding "ESC" key to request the cancellation.
        Must be called in between ProgressBegin() /ProgressDone()."""
        ...
    def __init__(self):...
class FBProfiler(FBComponent):
    ActiveSampling:bool
    BufferSize:int
    EvaluationDepth:int
    FrameReference:bool
    ProfilingMode:FBProfilingMode
    def GetEndEventSample(self,Index:int)->FBProfileTimeEvent:
        """Get end time event for event at given index.
        This function and FBProfileTimeEvent.IsSingleEvent are useful to identify duration of event action.
        ### Parameters:
        - Index: Sample index.
        
        ### Returns:
        Sample object if sample at given index is start sample."""
        ...
    def GetEventSample(self,Index:int)->FBProfileTimeEvent:
        """Only possible way to query collected FBProfileTimeEvent .
        ### Parameters:
        - Index: Sample index.
        
        ### Returns:
        Sample object."""
        ...
    def GetEventSampleCount(self)->int:
        """Get number of time event samples collected during last sampling.
        ### Returns:
        Number of FBProfileTimeEvent samples gathered during sampling."""
        ...
    def GetProfilingCost(self)->float:
        """Profiling collection can affect scene performace.
        This function return how costly is profiling.
        ### Returns:
        Cost of profiling the scene. (in mini seconds)"""
        ...
    def GetStatComment(self,Index:int)->str:
        """Get aditional information about what action is stat refering to.
        ### Parameters:
        - Index: Index of stat.
        
        ### Returns:
        Stat comment."""
        ...
    def GetStatCount(self)->int:
        """Stats are holding last execution time/duration of action.
        They are used for actions that doesn't appear frequently, like file IO.
        ### Returns:
        Stats count. They are created when stat occurs, so open or save action needs to be done first to get any information stored in stats."""
        ...
    def GetStatDuration(self,Index:int)->float:
        """Get time that was spend on execution of action.
        ### Parameters:
        - Index: Index of stat.
        
        ### Returns:
        Stat duration (in seconds)."""
        ...
    def GetStatIndex(self,Name:str)->int:
        """Search for index of given stat name.
        ### Parameters:
        - Name: Name of the sample that we are looking for.
        
        ### Returns:
        Stat index if found, -1 if not in the list."""
        ...
    def GetStatName(self,Index:int)->str:
        """Get information about what action is stat refering to.
        ### Parameters:
        - Index: Index of stat.
        
        ### Returns:
        Stat name."""
        ...
    def GetStatStart(self,Index:int)->float:
        """Get start time of action.
        ### Parameters:
        - Index: Index of stat.
        
        ### Returns:
        Start time (in seconds)."""
        ...
    def GetStatStop(self,Index:int)->float:
        """Get stop time of action.
        ### Parameters:
        - Index: Index of stat.
        
        ### Returns:
        Stop time (in seconds)."""
        ...
    def __init__(self):...
class FBPose(FBComponent):
    Type:FBPoseType
    def AddNode(self,Object:FBModel,Matrix:FBMatrix=None,bIsLocalMatrix:bool=False)->int:
        """Add a new pose node.
        ### Parameters:
        - Object: The object for which we are creating the pose information.
        - Matrix: The transformation of the object we want to save.
        - bIsLocalMatrix: Is the matrix a local matrix?"""
        ...
    def CreatePoseThumbnail(self):
        """Create an image thumbnail for the current pose."""
        ...
    def Find(self,NodeName:str)->int:
        """Look in this pose if the given node is present.
        ### Parameters:
        - NodeName: Name of the node we are looking for.
        
        ### Returns:
        -1 if the node is not in the list or it's position."""
        ...
    def GetNodeCount(self)->int:
        """Returns the number of pose nodes stored."""
        ...
    def GetNodeMatrix(self,Index:int)->FBMatrix:
        """Get the pose node matrix.
        ### Parameters:
        - Index: Index of the node.
        
        ### Returns:
        a reference to the node's Matrix.
        
        ### Remarks:
        if the index is invalid a reference to an identiy matrix is returned.
        The reference will become undefined if this object is destroyed."""
        ...
    def GetNodeName(self,Index:int)->str:
        """Get the pose node at specified index.
        ### Parameters:
        - Index: Index of the node.
        
        ### Remarks:
        if the index is invalid a reference to an empty string is returned.
        The reference will become undefined if this object is destroyed."""
        ...
    def GetNodeObject(self,Index:int)->FBModel:
        """Get the pose node object.
        ### Parameters:
        - Index: Index of the node.
        
        ### Returns:
        a pointer to the node's Object.
        
        ### Remarks:
        if the index is invalid a null pointer is returned."""
        ...
    def IsNodeLocalMatrix(self,Index:int)->bool:
        """Get the type of the Matrix for a given node.
        ### Parameters:
        - Index: Index of the node.
        
        ### Returns:
        true if the matrix is defined in Local coordinate space.
        
        ### Remarks:
        If this object is configured to hold BindPose data, this method will always return false."""
        ...
    def RemoveNode(self,Index:int):
        """Remove the pose node at specified index.
        ### Parameters:
        - Index: Index of the node to be removed."""
        ...
    def SetIsNodeLocalMatrix(self,Index:int,bIsNodeLocalMatrix:bool):
        """Set the type of the Matrix for a given node.
        ### Parameters:
        - Index: Index of the node.
        - bIsNodeLocalMatrix: True if the matrix of the node is a local matrix."""
        ...
    def SetNodeMatrix(self,Index:int,Matrix:FBMatrix):
        """Set the pose node matrix.
        ### Parameters:
        - Index: Index of the node.
        - Matrix: Matrix to set for this pose node."""
        ...
    def SetNodeObject(self,Index:int,Object:FBModel):
        """Set the pose node object.
        ### Parameters:
        - Index: Index of the node.
        - Object: Object to associate with this pose node."""
        ...
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of pose."""
        ...
class FBPointCacheManager(FBComponent):
    AllowCacheResampling:bool
    AlwaysAskForPath:bool
    ApplyCacheOnNewModel:bool
    ApplyGlobalTransform:bool
    CacheAABBox:bool
    CacheNormal:bool
    CreateFilePerFrameCache:bool
    CreateMultiChannelCache:bool
    DefaultPath:str
    Models:FBPropertyListObject
    NewModelRoot:FBModel
    SaveEveryFrame:int
    def SetTransformReference(self):
        """Action Property: Set the model's current transformation as the reference.
        Definition at line 448 of file fbsystem.h ."""
        ...
    def __init__(self):...
class FBCharacterPose(FBPose):
    def ApplyPoseCandidate(self):
        """After setting the candidate on the skeleton node, calling this function will allow subsequent call to get the TRS value of a skeleton node to return the candidate value."""
        ...
    def ClearCharacterExtensionsPose(self):
        """Clear only the pose of the character extensions (omit the character)."""
        ...
    def ClearCharacterPose(self):
        """Clear only the pose of the character (omit the extensions)."""
        ...
    def ClearPose(self):
        """Clear all the data of the pose."""
        ...
    def CopyFrom(self,FromPose:FBCharacterPose):
        """Copy everything from a given object.
        ### Remarks:
        Will copy everything, including the object name, properties, data etc. Objects will be identical.
        
        ### Parameters:
        - FromPose: Pose from which to copy."""
        ...
    def CopyPose(self,Character:FBCharacter):
        """Copy the pose of a character and its extensions.
        ### Parameters:
        - Character: Character to copy the pose from."""
        ...
    def CopyPoseCharacter(self,Character:FBCharacter):
        """Copy the pose of only the character (omit the extensions).
        ### Parameters:
        - Character: Character to copy the pose from."""
        ...
    def CopyPoseCharacterExtension(self,CharacterExtension:FBCharacterExtension):
        """Copy the pose of a single character extension.
        ### Parameters:
        - CharacterExtension: Character extension to copy the pose from."""
        ...
    def CopyPoseCharacterExtensions(self,Character:FBCharacter):
        """Copy the pose of only the character extensions (omit the character).
        ### Parameters:
        - Character: Character to copy the pose of the extensions from."""
        ...
    def CopyPoseCharacterExtensionsFrom(self,FromPose:FBCharacterPose):
        """Copy the pose data of only the character extensions from a given pose.
        ### Parameters:
        - FromPose: Pose from which to copy the data."""
        ...
    def CopyPoseCharacterFrom(self,FromPose:FBCharacterPose):
        """Copy the pose data of only the character from a given pose.
        ### Parameters:
        - FromPose: Pose from which to copy the data."""
        ...
    def CopyPoseDataFrom(self,FromPose:FBCharacterPose):
        """Copy all the pose data from a given pose.
        ### Remarks:
        Will copy all the data of the pose.
        
        ### Parameters:
        - FromPose: Pose from which to copy the data."""
        ...
    def GetCharacterExtensionNameFromPose(self,CharacterExtensionPose:FBObjectPose)->str:
        """Get the name of the character extension for the specified pose.
        ### Parameters:
        - CharacterExtensionPose: Pose of a character extension to check its name.
        
        ### Returns:
        The name of the character extension (It is the label name of the character extension)."""
        ...
    def GetCharacterExtensionPose(self,CharacterExtensionName:str)->FBObjectPose:
        """Get the pose of a character extension.
        ### Parameters:
        - CharacterExtensionName: Name of the character extension pose to get (It is the label name of the character extension).
        
        ### Returns:
        The pose of the character extension, `None` if not found."""
        ...
    def GetCharacterExtensionPoseAt(self,Index:int)->FBObjectPose:
        """Get the pose of a character extension.
        ### Parameters:
        - Index: Index of the character extension pose to get.
        
        ### Returns:
        The pose of the character extension."""
        ...
    def GetCharacterExtensionPoseCount(self)->int:
        """Get the number of character extension stored in the pose.
        ### Returns:
        Number of character extension stored in the pose."""
        ...
    def GetExtraBoneParentRotationOffset(self,R:FBVector3d,Index:int):
        """Get the extra bone transformation offset.
        ### Parameters:
        - R: A vector that will contains the parent rotation offset value on return.
        - Index: Index of the extra bone to get."""
        ...
    def GetExtraBoneTransform(self,T:FBVector3d,R:FBVector3d,S:FBVector3d,Index:int):
        """Get the extra bone transformation.
        ### Parameters:
        - T: A vector that will contains the translation value on return.
        - R: A vector that will contains the rotation value on return.
        - S: A vector that will contains the scale value on return.
        - Index: Index of the extra bone to get."""
        ...
    def GetExtraBoneTransformOffset(self,T:FBVector3d,R:FBVector3d,S:FBVector3d,Index:int):
        """Get the extra bone transformation offset.
        ### Parameters:
        - T: A vector that will contains the translation offset value on return.
        - R: A vector that will contains the rotation offset value on return.
        - S: A vector that will contains the scale offset value on return.
        - Index: Index of the extra bone to get."""
        ...
    def GetExtraBones(self)->list:...
    def GetMirrorPlaneEquation(self,MirrorPlaneEquation:FBVector4d,Character:FBCharacter,CharacterPoseOptions:FBCharacterPoseOptions):
        """Get the mirror plane equation that would be used to mirror according to the CharacterPoseOptions.
        ### Parameters:
        - MirrorPlaneEquation: Out: Mirror plane equation.
        - Character: Character to receive the pose.
        - CharacterPoseOptions: Options used to paste the pose."""
        ...
    def GetOrCreateCharacterExtensionPose(self,CharacterExtensionName:str)->FBObjectPose:
        """Get the pose of a character extension and create it if necessary.
        ### Remarks:
        Use this function to manually add a pose of a character extension.
        
        ### Parameters:
        - CharacterExtensionName: Name of the character extension pose to get (It is the label name of the character extension).
        
        ### Returns:
        The pose of the character extension."""
        ...
    def IsCharacterExtensionPoseStored(self,CharacterExtensionName:str)->bool:
        """Is the pose of the character extension stored in the pose?
        ### Parameters:
        - CharacterExtensionName: Name of the character extension.
        
        ### Returns:
        true if the pose of the character extension stored in the pose."""
        ...
    def IsCharacterPoseStored(self)->bool:
        """Is the pose of the character stored in the pose?
        ### Returns:
        true if the pose of the character stored in the pose."""
        ...
    def PastePose(self,Character:FBCharacter,CharacterPoseOptions:FBCharacterPoseOptions):
        """Paste the pose of a character and its extensions.
        ### Remarks:
        Supports the match and mirror options.
        When pasting in body part, the selected parts and extensions of the character will be pasted.
        
        ### Parameters:
        - Character: Character to paste the pose to.
        - CharacterPoseOptions: Options used to specify how to paste."""
        ...
    def PastePoseCharacter(self,Character:FBCharacter,CharacterPoseOptions:FBCharacterPoseOptions):
        """Paste the pose of only the character (omit the extensions).
        ### Remarks:
        Does not support the match and mirror options.
        
        ### Parameters:
        - Character: Character to paste the pose to.
        - CharacterPoseOptions: Options used to specify how to paste."""
        ...
    def PastePoseCharacterExtension(self,CharacterExtension:FBCharacterExtension,CharacterPoseOptions:FBCharacterPoseOptions):
        """Paste the pose of a single character extension.
        ### Remarks:
        Does not support the match and mirror options.
        
        ### Parameters:
        - CharacterExtension: Character extension to paste the pose to.
        - CharacterPoseOptions: Options used to specify how to paste."""
        ...
    def PastePoseCharacterExtensions(self,Character:FBCharacter,CharacterPoseOptions:FBCharacterPoseOptions):
        """Paste the pose of only the character extensions (omit the character).
        ### Remarks:
        Does not support the match and mirror options.
        
        ### Parameters:
        - Character: Character to paste the pose of the extensions to.
        - CharacterPoseOptions: Options used to specify how to paste."""
        ...
    def RemoveCharacterExtensionPose(self,CharacterExtensionName:str):
        """Remove the pose of a character extension.
        ### Parameters:
        - CharacterExtensionName: Name of the character extension pose to remove (It is the label name of the character extension)."""
        ...
    def RemoveCharacterExtensionPoseAt(self,Index:int):
        """Remove the pose of a character extension.
        ### Parameters:
        - Index: Index of the character extension pose to remove."""
        ...
    def __init__(self,Name:str):
        """This constructor is used to create a new object.
        ### Parameters:
        - Name: Object name."""
        ...
class FBObjectPose(FBPose):
    def AddStanceOffset(self,ObjectName:str,StancePose:FBObjectPose,PoseTransformType:FBPoseTransformType=FBPoseTransformType.kFBPoseTransformInvalid):
        """Add the StanceOffset to an object in the pose.
        ### Remarks:
        Working with poses with their StanceOffset removed is usefull for retargetting.
        If PoseTransformType is set to kFBPoseTransformInvalid, offsets will be added in all TransformTypes.
        
        ### Parameters:
        - ObjectName: Name of the object.
        - StancePose: Pose representing the stance of all objects.
        - PoseTransformType: Transform type in which to add the offset (Local, Global or LocalRef)."""
        ...
    def AddStanceOffsetAllObjects(self,StancePose:FBObjectPose,PoseTransformType:FBPoseTransformType=FBPoseTransformType.kFBPoseTransformInvalid):
        """Add the StanceOffset to all the objects in the pose.
        ### Remarks:
        Working with poses with their StanceOffset removed is usefull for retargetting.
        If PoseTransformType is set to kFBPoseTransformInvalid, offsets will be added in all TransformTypes.
        
        ### Parameters:
        - StancePose: Pose representing the stance of all objects.
        - PoseTransformType: Transform type in which to add the offset (Local, Global or LocalRef)."""
        ...
    def ClearPose(self):
        """Clear all the data of the pose."""
        ...
    def CopyFrom(self,FromPose:FBObjectPose):
        """Copy everything from a given object.
        ### Remarks:
        Will copy everything, including the object name, properties, data etc. Objects will be identical.
        
        ### Parameters:
        - FromPose: Pose from which to copy."""
        ...
    def CopyObjectPose(self,ObjectName:str,Object:FBComponent):
        """Copy the pose of all the properties of an object.
        ### Remarks:
        You can specify a ObjectName different from the name of Object.
        
        ### Parameters:
        - ObjectName: Name of the object to store in the pose.
        - Object: Object from which we'll read all the property values to store in the pose."""
        ...
    def CopyPoseAllObjectsTransformFrom(self,FromPose:FBObjectPose,PoseTransformType:FBPoseTransformType=FBPoseTransformType.kFBPoseTransformInvalid):
        """Copy all the transforms from a given pose.
        ### Remarks:
        If PoseTransformType is set to kFBPoseTransformInvalid, copy all TransformTypes.
        
        ### Parameters:
        - FromPose: Pose from which to copy the data.
        - PoseTransformType: Transform type from which to copy the transform (Local, Global or LocalRef)."""
        ...
    def CopyPoseDataFrom(self,FromPose:FBObjectPose):
        """Copy all the pose data from a given pose.
        ### Remarks:
        Will copy all the data of the pose including the transforms.
        
        ### Parameters:
        - FromPose: Pose from which to copy the data."""
        ...
    def CopyPoseTransformFrom(self,FromPose:FBObjectPose,ObjectName:str,PoseTransformType:FBPoseTransformType=FBPoseTransformType.kFBPoseTransformInvalid):
        """Copy the transforms of an object from a given pose.
        ### Remarks:
        If PoseTransformType is set to kFBPoseTransformInvalid, copy all TransformTypes.
        
        ### Parameters:
        - FromPose: Pose from which to copy the data.
        - ObjectName: Name of object to copy the transform from.
        - PoseTransformType: Transform type from which to copy the transform (Local, Global or LocalRef)."""
        ...
    def CopyPropertyPose(self,ObjectName:str,Property:FBProperty):
        """Copy the pose of a property of an object.
        ### Remarks:
        You can specify a ObjectName different from the name of pObject.
        
        ### Parameters:
        - ObjectName: Name of the object to store in the pose.
        - Property: Property from which we'll read the value to store in the pose."""
        ...
    def CopyTransform(self,ObjectName:str,Object:FBComponent,ObjectPoseOptions:FBObjectPoseOptions):
        """Copy the transform of an object.
        ### Remarks:
        This function will always copy all the TransformAttributes (T,R,S) in all TransformType (Local, Global, LocalRef).
        
        ### Parameters:
        - ObjectName: Name of the object to store in the pose.
        - Object: Object from which we'll evaluate the transform values to store in the pose.
        - ObjectPoseOptions: PoseOptions used to specify the transform of the reference object (Default: Identity)."""
        ...
    def GetPropertyValue(self,Value:list,Size:int,ObjectName:str,PropertyName:str):
        """Get the value of a property stored in the pose.
        ### Parameters:
        - Value: Value to get.
        - Size: Number of elements in Value.
        - ObjectName: Name of the object to get the value.
        - PropertyName: Name of the property to get the value."""
        ...
    def GetStoredObjectNames(self)->FBStringList:
        """Get all the object names currently stored in this pose.
        ### Returns:
        All the object names currently stored in this pose."""
        ...
    def GetTransform(self,T:FBVector4d,RM:FBMatrix,SM:FBMatrix,ObjectName:str,PoseTransformType:FBPoseTransformType)->bool:
        """Get the transform of an object in the pose.
        ### Parameters:
        - T: Translation to get.
        - RM: Rotation to get.
        - SM: Scaling to get.
        - ObjectName: Name of the object to get the transform.
        - PoseTransformType: Transform type in which to set the transform (Local, Global or LocalRef).
        
        ### Returns:
        True if the transform was found in the pose."""
        ...
    def IsPropertyPoseable(self,Property:FBProperty)->bool:
        """Is the property poseable?
        ### Returns:
        True if the value of this property can be stored in the pose."""
        ...
    def IsPropertyStored(self,ObjectName:str,PropertyName:str)->bool:
        """Is the property stored in the pose?
        ### Parameters:
        - ObjectName: Name of the object.
        - PropertyName: Name of the property.
        
        ### Returns:
        True if the property is stored in the pose."""
        ...
    def IsTransformStored(self,ObjectName:str,PoseTransformType:FBPoseTransformType=FBPoseTransformType.kFBPoseTransformInvalid)->bool:
        """Is the transform of this object stored in the specified TransformType?
        ### Remarks:
        If PoseTransformType is set to kFBPoseTransformInvalid, will check in all TransformTypes.
        
        ### Parameters:
        - ObjectName: Name of the object.
        - PoseTransformType: Transform type in which to check.
        
        ### Returns:
        True if the transform of this object is stored in the specified TransformType (Local, Global and LocalRef)."""
        ...
    def MirrorPose(self,ObjectName:str,ObjectPoseMirrorOptions:FBObjectPoseMirrorOptions):
        """Mirror the transform of an object in the pose.
        ### Parameters:
        - ObjectName: Name of the object to mirror.
        - ObjectPoseMirrorOptions: MirrorOptions used to specify the mirror plane."""
        ...
    def MirrorPoseAllObjects(self,ObjectPoseMirrorOptions:FBObjectPoseMirrorOptions):
        """Mirror the transform of all objects in the pose.
        ### Parameters:
        - ObjectPoseMirrorOptions: MirrorOptions used to specify the mirror plane."""
        ...
    def MultTransform(self,ObjectName:str,GX:FBMatrix,TransformAttribute:FBModelTransformationType,PoseTransformType:FBPoseTransformType):
        """Multiply the transform of an objects in the pose.
        ### Parameters:
        - ObjectName: Name of the object.
        - GX: Transformation matrix to apply.
        - TransformAttribute: Transform attribute to affect. Supported: T,R,S and Transformation.
        - PoseTransformType: Transform type in which to mult the transform (Local, Global or LocalRef)."""
        ...
    def MultTransformAllObjects(self,GX:FBMatrix,TransformAttribute:FBModelTransformationType,PoseTransformType:FBPoseTransformType):
        """Multiply the transform of all objects in the pose.
        ### Parameters:
        - GX: Transformation matrix to apply.
        - TransformAttribute: Transform attribute to affect. Supported: T,R,S and Transformation.
        - PoseTransformType: Transform type in which to mult the transform (Local, Global or LocalRef)."""
        ...
    def PasteObjectPose(self,ObjectName:str,Object:FBComponent):
        """Paste the pose of all the properties of an object.
        ### Remarks:
        You can specify a ObjectName different from the name of Object.
        Properties that were not stored in the pose will not be affected.
        
        ### Parameters:
        - ObjectName: Name of the object stored in the pose.
        - Object: Object which will receive the values stored in the pose."""
        ...
    def PastePropertyPose(self,ObjectName:str,Property:FBProperty):
        """Paste the pose of a property of an object.
        ### Remarks:
        You can specify a ObjectName different from the name of pObject.
        The property will not be affected if it was not stored in the pose.
        
        ### Parameters:
        - ObjectName: Name of the object stored in the pose.
        - Property: Property which will receive the value stored in the pose."""
        ...
    def PasteTransform(self,ObjectName:str,Object:FBComponent,ObjectPoseOptions:FBObjectPoseOptions):
        """Paste the transform of an object.
        ### Remarks:
        Use the ObjectPoseOptions to specify which TransformType to use when pasting.
        
        ### Parameters:
        - ObjectName: Name of the object stored in the pose.
        - Object: Object which will receive the transform values stored in the pose.
        - ObjectPoseOptions: PoseOptions used to specify the transform of the reference object, the TransformType and TransformAttributes to paste."""
        ...
    def RemoveStanceOffset(self,ObjectName:str,StancePose:FBObjectPose,PoseTransformType:FBPoseTransformType=FBPoseTransformType.kFBPoseTransformInvalid):
        """Remove the StanceOffset from an object in the pose.
        ### Remarks:
        Working with poses with their StanceOffset removed is usefull for retargetting.
        If PoseTransformType is set to kFBPoseTransformInvalid, offsets will be removed in all TransformTypes.
        
        ### Parameters:
        - ObjectName: Name of the object.
        - StancePose: Pose representing the stance of all objects.
        - PoseTransformType: Transform type in which to remove the offset (Local, Global or LocalRef)."""
        ...
    def RemoveStanceOffsetAllObjects(self,StancePose:FBObjectPose,PoseTransformType:FBPoseTransformType=FBPoseTransformType.kFBPoseTransformInvalid):
        """Remove the StanceOffset from all the objects in the pose.
        ### Remarks:
        Working with poses with their StanceOffset removed is usefull for retargetting.
        If PoseTransformType is set to kFBPoseTransformInvalid, offsets will be removed in all TransformTypes.
        
        ### Parameters:
        - StancePose: Pose representing the stance of all objects.
        - PoseTransformType: Transform type in which to remove the offset (Local, Global or LocalRef)."""
        ...
    def SetPropertyValue(self,ObjectName:str,PropertyName:str,Value:float,Size:int):
        """Set the value of a property in the pose.
        ### Parameters:
        - Value: Value to set.
        - Size: Number of elements in Value.
        - ObjectName: Name of the object to set the value.
        - PropertyName: Name of the property to set the value."""
        ...
    def SetTransform(self,T:FBVector4d,RM:FBMatrix,SM:FBMatrix,ObjectName:str,PoseTransformType:FBPoseTransformType):
        """Set the transform of an object in the pose.
        ### Parameters:
        - T: Translation to set.
        - RM: Rotation to set.
        - SM: Scaling to set.
        - ObjectName: Name of the object to set the transform.
        - PoseTransformType: Transform type in which to set the transform (Local, Global or LocalRef)."""
        ...
    def __init__(self,Name:str):
        """This constructor is used to create a new object.
        ### Parameters:
        - Name: Object name. If pObject is not NULL, Name will be ignored."""
        ...
class FBCluster(FBComponent):
    ClusterAccuracy:float
    ClusterMode:FBClusterMode
    def ClusterBegin(self,Index:int=-1)->int:
        """Begin cluster definition.
        ### Parameters:
        - Index: Link index.
        
        ### Returns:
        Index of last item(default=-1)."""
        ...
    def ClusterEnd(self)->int:
        """End cluster definition.
        ### Returns:
        0, (Not implemented)."""
        ...
    def LinkClearUnused(self,Threshold:float=-1.0):
        """Remove all unused links.
        ### Parameters:
        - Threshold: Weight value under which links are considered unused (default=-1)."""
        ...
    def LinkGetAssociateModel(self,LinkNumber:int)->FBModel:
        """Get model associated with link.
        ### Parameters:
        - LinkNumber: Number value of link to get associated model from.
        
        ### Returns:
        Model associated to link number LinkNumber ."""
        ...
    def LinkGetCount(self)->int:
        """Get number of links.
        ### Returns:
        Number of links."""
        ...
    def LinkGetModel(self,LinkNumber:int)->FBModel:
        """Get model from a link.
        ### Parameters:
        - LinkNumber: Number value of link to get model from.
        
        ### Returns:
        Model at link number LinkNumber ."""
        ...
    def LinkGetName(self,LinkNumber:int)->str:
        """Get the name of a link.
        ### Parameters:
        - LinkNumber: Number value of link to get name from.
        
        ### Returns:
        Name of link number LinkNumber ."""
        ...
    def LinkGetVertexIndex(self,Index:int)->int:
        """Get current vertex at link.
        ### Parameters:
        - Index: Index of link to get vertex from.
        
        ### Returns:
        Index value of the current vertex associated to link at index number Index"""
        ...
    def LinkRemove(self,LinkNumber:int):
        """Remove a link.
        ### Parameters:
        - LinkNumber: Number value of link to rename."""
        ...
    def LinkSetCurrentVertex(self,LinkIndex:int,PointIndex:int):
        """Link at current vertex.
        ### Parameters:
        - LinkIndex: Index of link to add vertex to.
        - PointIndex: Index of vertex to add."""
        ...
    def LinkSetModel(self,Model:FBModel):
        """Set model to a link.
        ### Parameters:
        - Model: Model to set."""
        ...
    def LinkSetName(self,Name:str,LinkNumber:int):
        """Set the name of a link.
        ### Parameters:
        - LinkNumber: Number value of link to name.
        - Name: Name of the link."""
        ...
    def VertexAdd(self,VertexIndex:int,Weight:float):
        """Add a vertex to a cluster.
        ### Parameters:
        - VertexIndex: Index of vertex to add.
        - Weight: Weight to give to vertex."""
        ...
    def VertexClear(self):
        """Clear all linked vertices."""
        ...
    def VertexGetCount(self)->int:
        """Get the number of vertices.
        ### Returns:
        Number of vertices in a cluster."""
        ...
    def VertexGetNumber(self,Index:int)->int:
        """Get vertex number.
        ### Parameters:
        - Index: Index of link to get vertex from.
        
        ### Returns:
        Number value of vertex at link number Index"""
        ...
    def VertexGetTransform(self,Position:FBVector3d,Rotation:FBVector3d,Scaling:FBVector3d):
        """Get transform of a cluster set.
        ### Return values:
        - Position: Position transform.
        - Rotation: Rotation transform.
        - Scaling: Scaling transform."""
        ...
    def VertexGetWeight(self,Index:int)->float:
        """Get vertex weight.
        ### Parameters:
        - Index: Index of link to get vertex from.
        
        ### Returns:
        Weight of vertex found at link number Index ."""
        ...
    def VertexRemove(self,VertexIndex:int):
        """Remove a vertex from a cluster.
        ### Parameters:
        - VertexIndex: Index of vertex to remove."""
        ...
    def VertexSetTransform(self,Position:FBVector3d,Rotation:FBVector3d,Scaling:FBVector3d):
        """Set transform of a cluster set.
        ### Parameters:
        - Position: Position transform.
        - Rotation: Rotation transform.
        - Scaling: Scaling transform."""
        ...
    def VertexSetWeight(self,Weight:float,Index:int):
        """Set vertex weight.
        ### Parameters:
        - Index: Index of link to get vertex from.
        - Weight: Weight to give to vertex."""
        ...
    def __init__(self,Model:FBModel):
        """protected access, call FBModel::Cluster instead.
        ### Parameters:
        - Model: Parent model in question."""
        ...
class FBCharacterMarkerSet(FBComponent):
    def GetExtractionProperty(self,NodeId:FBBodyNodeId)->FBProperty:
        """Get the extraction property associated with each body part of the character.
        ### Returns:
        The property associated with given NodeId."""
        ...
    def GetMarkersProperty(self,NodeId:FBBodyNodeId)->FBProperty:
        """Get the marker property associated with each body part of the character.
        ### Returns:
        The property associated with given NodeId."""
        ...
    def GetSnapProperty(self,NodeId:FBBodyNodeId,What:FBModelTransformationType)->FBProperty:
        """Get the snap property associated with each body part of the character for given transformation.
        Current version snap only translation and rotation.
        ### Returns:
        The property associated with given NodeId and What."""
        ...
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of new character marker set."""
        ...
class FBCameraSwitcherAudioManager(FBComponent):
    def GetAudioClip(self)->FBAudioClip:
        """Get the Audio Clip displayed on the Camera Switcher.
        ### Returns:
        The Audio Clip displayed, nullptr (C++) / None (Python) if any."""
        ...
    def GetAudioTrack(self)->FBStoryTrack:
        """Get the Audio Track displayed on the Camera Switcher.
        ### Returns:
        The Audio Track displayed, nullptr (C++) / None (Python) if any."""
        ...
    def GetLockPitchToSpeed(self)->bool:
        """Get the 'Lock Pitch to Speed' state.
        ### Returns:
        True if the 'Lock Pitch to Speed' state is set, false otherwise."""
        ...
    def GetShowAudio(self)->bool:
        """Get the 'Show Audio' state.
        ### Returns:
        True if the 'Show Audio' state is set, false otherwise."""
        ...
    def GetShowLeftChannel(self)->bool:
        """Get the 'Show Left Channel' state.
        ### Returns:
        True if the 'Show Left Channel' state is set, false otherwise."""
        ...
    def GetShowRightChannel(self)->bool:
        """Get the 'Show Right Channel' state.
        ### Returns:
        True if the 'Show Right Channel' state is set, false otherwise."""
        ...
    def RemoveAudio(self)->bool:
        """Remove the audio clip or audio track currently displayed on the Camera Switcher.
        ### Returns:
        True if the operation is successful, false otherwise."""
        ...
    def SetAudioClip(self,AudioClip:FBAudioClip)->bool:
        """Set the Audio Clip to display on the Camera Switcher.
        ### Parameters:
        - AudioClip: The Audio Clip to display.
        
        ### Returns:
        True if the operation is successful, false otherwise."""
        ...
    def SetAudioTrack(self,AudioTrack:FBStoryTrack)->bool:
        """Set the Audio Track to display on the Camera Switcher.
        ### Parameters:
        - AudioTrack: The Audio Track to display.
        
        ### Returns:
        True if the operation is successful, false otherwise."""
        ...
    def SetLockPitchToSpeed(self,bLock:bool)->bool:
        """Set the 'Lock Pitch to Speed' state.
        ### Parameters:
        - bLock: True to lock pitch to speed, false otherwise.
        
        ### Returns:
        True if the operation is successful, false otherwise."""
        ...
    def SetShowAudio(self,bShow:bool)->bool:
        """Set the 'Show Audio' state.
        ### Parameters:
        - bShow: True to show the Audio waveform, false otherwise.
        
        ### Returns:
        True if the operation is successful, false otherwise."""
        ...
    def SetShowLeftChannel(self,bShow:bool)->bool:
        """Set the 'Show Left Channel' state.
        ### Parameters:
        - bShow: True to show the left channel, false otherwise.
        
        ### Returns:
        True if the operation is successful, false otherwise."""
        ...
    def SetShowRightChannel(self,bShow:bool)->bool:
        """Set the 'Show Right Channel' state.
        ### Parameters:
        - bShow: True to show the right channel, false otherwise.
        
        ### Returns:
        True if the operation is successful, false otherwise."""
        ...
    def __init__(self):
        """Protected constructor, use TheOne() access instead."""
        ...
class FBBox(FBComponent):
    Animatable:bool
    Live:bool
    RecordMode:bool
    UniqueName:str
    def AnimationNodeDestroy(self,AnimationNode:FBAnimationNode)->bool:
        """Destroy an animation node.
        ### Parameters:
        - AnimationNode: Handle to the animation node to be destroyed.
        
        ### Returns:
        true if destruction was successful."""
        ...
    def AnimationNodeInGet(self)->FBAnimationNode:
        """Get the (IN/OUT) animation node for this box.
        ### Returns:
        A handle to the animation node for this box."""
        ...
    def AnimationNodeIsUserData(self,AnimationNode:FBAnimationNode)->bool:
        """Is the animation node user data?
        ### Parameters:
        - AnimationNode: Handle to the animation to be queried.
        
        ### Returns:
        true if node is user data."""
        ...
    def AnimationNodeOutGet(self)->object:...
    def GetInConnector(self,Index:int)->FBAnimationNode:
        """Get the animation node input associated with the given index.
        ### Parameters:
        - Index: The animation node input associated with the given index.
        
        ### Returns:
        The animation node input, or `None` if the Index value is invalid."""
        ...
    def GetInConnectorCount(self)->int:
        """Get the number of animation node inputs for this box.
        ### Returns:
        The number of animation node inputs for this box."""
        ...
    def GetOutConnector(self,Index:int)->FBAnimationNode:
        """Get the animation node output associated with the given index.
        ### Parameters:
        - Index: The animation node output associated with the given index.
        
        ### Returns:
        The animation node output, or `None` if the Index value is invalid."""
        ...
    def GetOutConnectorCount(self)->int:
        """Get the number of animation node outputs for this box.
        ### Returns:
        The number of animation node outputs for this box."""
        ...
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Box name."""
        ...
class FBAudioOut(FBComponent):
    def __init__(self):...
class FBBoxPlaceHolder(FBBox):
    Box:FBBox
class FBConstraint(FBBox):
    Active:bool
    Deformer:bool
    Description:str
    HasLayout:bool
    Lock:bool
    Weight:float
    def AnimationNodeInCreate(self,UserId,Property:FBModel,arg4:str)->FBAnimationNode:
        """Animation Node Creations (IN).
        Used to create the In connectors on an animation node. This function will return a newly created animation node, connected to the model specified by Property .
        ### Parameters:
        - UserId: User specified reference number.
        - Property: Property of model to animate (must be animatable)
        
        ### Returns:
        Newly created IN animation node."""
        ...
    def AnimationNodeOutCreate(self,UserId,Model:FBModel,Attribute:str)->FBAnimationNode:
        """Animation Node Creations (IN/OUT).
        Used to create the connectors (in or out) on an animation node. This function will return a newly created animation node, connected to the model specified by Model .
        ### Parameters:
        - UserId: User specified reference number.
        - Model: Model to associate with animation node.
        - Attribute: Attribute of model to animate (i.e. Translation, Lcl Translation, etc.)
        
        ### Returns:
        Newly created IN/OUT animation node."""
        ...
    def Clone(self)->FBConstraint:
        """Clone the constraint.
        ### Returns:
        Newly created (and copied) constraint.
        Reimplemented in FBCharacter ."""
        ...
    def DeformerBind(self,Model:FBModel)->bool:
        """Bind/Unbind Model to deformation constraint.
        These functions are used for adding/removing a deformation binding to/from Model if the constraint is a deformation constraint.
        ### Parameters:
        - Model: Model to bind/unbind.
        
        ### Returns:
        true if successful."""
        ...
    def DeformerUnBind(self,arg2:FBModel)->bool:...
    def Disable(self,Model:FBModel)->bool:
        """Disable constraint on Model .
        ### Parameters:
        - Model: Model on which constraint should be disabled.
        
        ### Returns:
        true if successful."""
        ...
    def FreezeSRT(self,Model:FBModel,bS:bool,bR:bool,bT:bool):
        """Freeze current model state.
        ### Parameters:
        - Model: Model to freeze constraint on.
        - bS: Scaling freeze?
        - bR: Rotation freeze?
        - bT: Translation freeze?"""
        ...
    def FreezeSuggested(self):
        """Suggest 'freeze'."""
        ...
    def ReferenceAdd(self,GroupIndex:int,Model:FBModel)->bool:
        """Add a reference to a specified group.
        ### Parameters:
        - GroupIndex: Group to add reference to.
        - Model: Model to place at new reference.
        
        ### Returns:
        true if successful.
        
        ### Warning:
        If you try to add a model to a group that is already full, the success of the operation will be false and the reference will not be added."""
        ...
    def ReferenceGet(self,GroupIndex:int,ItemIndex:int=0)->FBModel:
        """Get a reference.
        ### Parameters:
        - GroupIndex: Index of reference group containing desired reference.
        - ItemIndex: Index of reference in group to get (default is 0).
        
        ### Returns:
        Model at specified reference."""
        ...
    def ReferenceGetCount(self,GroupIndex:int)->int:
        """Get number of references in a specified group.
        ### Parameters:
        - GroupIndex: Index of group to query the number of references.
        
        ### Returns:
        Number of references in specified group."""
        ...
    def ReferenceGroupAdd(self,GroupName:str,MaxItemCount:int)->int:
        """Add a group of references.
        ### Parameters:
        - GroupName: Name of reference group to add.
        - MaxItemCount: Maximum number of items in GroupName .
        
        ### Returns:
        Index of new reference group."""
        ...
    def ReferenceGroupGetCount(self)->int:
        """Return the number of reference groups.
        ### Returns:
        Number of reference groups."""
        ...
    def ReferenceGroupGetMaxCount(self,GroupIndex:int)->int:
        """Get the maximum number of items that can exist in the reference group in question.
        ### Parameters:
        - GroupIndex: Index of reference group.
        
        ### Returns:
        Maximum number of items that can be added to the reference group."""
        ...
    def ReferenceGroupGetName(self,GroupIndex:int)->str:
        """Get the name of the reference group.
        ### Parameters:
        - GroupIndex: Index of the reference group to get the name for.
        
        ### Returns:
        The name of the reference group GroupIndex ."""
        ...
    def ReferenceRemove(self,GroupIndex:int,Model:FBModel)->bool:
        """Remove a reference to Model from the group at GroupIndex .
        ### Parameters:
        - GroupIndex: Index to remove reference from.
        - Model: Model to remove reference from.
        
        ### Returns:
        true if successful."""
        ...
    def RemoveAllAnimationNodes(self):
        """Remove animation nodes."""
        ...
    def RestoreModelState(self,Model:FBModel):
        """Restore the saved model state onto Model .
        ### Parameters:
        - Model: Model to affect with previous state."""
        ...
    def SaveModelState(self,Model:FBModel,bS:bool,bR:bool,bT:bool):
        """Save current state of Model .
        ### Parameters:
        - Model: Model to save.
        - bS: Scaling information?
        - bR: Rotation information?
        - bT: Translation information?"""
        ...
    def SetupAllAnimationNodes(self):
        """Setup animation nodes."""
        ...
    def Snap(self):
        """Function Property: Snap constraint.
        Definition at line 341 of file fbconstraint.h ."""
        ...
    def SnapSuggested(self):
        """Suggest 'snap'."""
        ...
    def __copy__(self)->object:...
class FBModelPlaceHolder(FBBoxPlaceHolder):
    Model:FBModel
    UseGlobalTransforms:bool
class FBCharacterSolver(FBConstraint):
    ExtraBones:property
    ExtraFK:property
    Source:FBComponent
    def GetParentRotationOffset(self,R:FBModel)->FBVector3d:
        """Get the Parent Rotation Offset of the Given Extra Bone Index.
        The rotation Offset if extracted at Characterisation (in Stance Pose). You don't need this value if the parent of the bone is characterized too.
        ### Parameters:
        - R: Offset Rotation between the Bone and is parent at Stance Pose."""
        ...
    @staticmethod
    def GetRegisteredSolverNames()->list:...
    def GetTarget(self)->object:...
    def GetTransformationOffset(self,arg2:FBModel)->list:...
    def SetParentRotationOffset(self,R:FBModel,Index:FBVector3d):
        """Set the Parent Rotation Offset of the Given Extra Bone Index.
        The rotation Offset if extracted at Characterisation (in Stance Pose). You don't need this value if the parent of the bone is characterized too.
        ### Parameters:
        - R: Offset Rotation between the Bone and is parent at Stance Pose.
        - Index: Index of extra Bone to get."""
        ...
    def SetTransformationOffset(self,arg2:FBModel,arg3:FBVector3d,arg4:FBVector3d,arg5:FBVector3d):...
    def __init__(self,Name:str,Object:FBCharacter,arg4:str):
        """### Parameters:
        - Name: Name of constraint.
        - Object: For internal use only (default is NULL)."""
        ...
class FBCharacterFace(FBConstraint):
    ActiveInput:bool
    InputActorFace:FBActorFace
    def ClusterGroupAdd(self,List:FBModelList,Name:str)->int:
        """Add a cluster group to the character face.
        ### Parameters:
        - List: List of clusters to add to this group.
        - Name: Optional name to assign to this cluster group.
        
        ### Returns:
        Index of the new cluster group -1 if the operation failed to complete."""
        ...
    def ClusterGroupFindByName(self,Name:str)->int:
        """Find a cluster group by name.
        ### Parameters:
        - Name: Name to search for on the face.
        
        ### Returns:
        Index of the matching cluster group. -1 if not found."""
        ...
    def ClusterGroupGetCount(self)->int:
        """Retrieve the total number of cluster groups.
        ### Returns:
        Number of cluster groups on the face."""
        ...
    def ClusterGroupGetName(self,ClusterGrpId:int)->str:
        """Retrieve the name of a cluster group.
        ### Parameters:
        - ClusterGrpId: Index of the cluster group to query.
        
        ### Returns:
        Name of the specified cluster group."""
        ...
    def ClusterGroupRemove(self,ClusterGrpId:int)->bool:
        """Remove a cluster group from the character face.
        ### Parameters:
        - ClusterGrpId: Index of the cluster group to remove.
        
        ### Returns:
        True if the operation completed successfully."""
        ...
    def ClusterGroupSetName(self,ClusterGrpId:int,Name:str)->bool:
        """Set the name of a cluster group.
        ### Parameters:
        - ClusterGrpId: Index of the cluster group to modify.
        - Name: New name for the cluster group.
        
        ### Returns:
        True of the operation completed successfully."""
        ...
    def ClusterGroupSnapRest(self,ClusterGrpId:int)->bool:
        """Set a cluster group's rest pose to the current pose.
        ### Parameters:
        - ClusterGrpId: Index of the cluster group to modify.
        
        ### Returns:
        True if the operation completed succesfully."""
        ...
    def ClusterShapeAdd(self,ClusterGrpId:int,Name:str)->int:
        """Add a cluster shape to a cluster group.
        ### Parameters:
        - ClusterGrpId: Index of the cluster group to modify.
        - Name: Optional name to assign to the shape.
        
        ### Returns:
        Index of the new shape. -1 if the operation failed to complete."""
        ...
    def ClusterShapeFindByName(self,ClusterGrpId:int,Name:str)->int:
        """Find a cluster shape in a cluster group by name.
        ### Parameters:
        - ClusterGrpId: Index of the cluster group to search.
        - Name: Name to search for in the cluster group.
        
        ### Returns:
        Index of the matching shape. -1 if not found."""
        ...
    def ClusterShapeGetCount(self,ClusterGrpId:int)->int:
        """Retrieve the total number of shapes in a cluster group.
        ### Parameters:
        - ClusterGrpId: Index of the cluster group to query.
        
        ### Returns:
        Number of shapes in the specified cluster group."""
        ...
    def ClusterShapeGetName(self,ClusterGrpId:int,ClusterShapeId:int)->str:
        """Retrieve the name of a shape in a cluster group.
        ### Parameters:
        - ClusterGrpId: Index of the cluster group to query.
        - ClusterShapeId: Index of the cluster shape to query.
        
        ### Returns:
        Name of the specified shape."""
        ...
    def ClusterShapeRemove(self,ClusterGrpId:int,ClusterShapeId:int)->bool:
        """Remove a cluster shape from a cluster group.
        ### Parameters:
        - ClusterGrpId: Index of the cluster group to modify.
        - ClusterShapeId: Index of the shape in the cluster group to remove.
        
        ### Returns:
        True of the operation completed succesfully."""
        ...
    def ClusterShapeSetName(self,ClusterGrpId:int,ClusterShapeId:int,Name:str)->bool:
        """Set the name of a shape in a cluster group.
        ### Parameters:
        - ClusterGrpId: Index of the cluster group to modify.
        - ClusterShapeId: Index of the cluster shape to modify.
        - Name: Name to assign to the cluster shape.
        
        ### Returns:
        True if the operation completed successfully."""
        ...
    def ClusterShapeSnap(self,ClusterGrpId:int,ClusterShapeId:int)->bool:
        """Record the current pose of the cluster group to a cluster shape.
        ### Parameters:
        - ClusterGrpId: Index of the cluster group to record.
        - ClusterShapeId: Index of the cluster shape to record the pose.
        
        ### Returns:
        True if the operation completed successfully."""
        ...
    def ExpressionAdd(self,Name:str)->int:
        """Add an expression to the face.
        ### Parameters:
        - Name: Optional name to assign to the new expression.
        
        ### Returns:
        Index of the new expression. -1 if the operation failed to complete."""
        ...
    def ExpressionFindByName(self,Name:str)->int:
        """Find an expression on the face by name.
        ### Parameters:
        - Name: Name of the expression to search for.
        
        ### Returns:
        Index of the matching expression. -1 if not found."""
        ...
    def ExpressionGetCount(self)->int:
        """Retrieve the total number of expressions on the face.
        ### Returns:
        Number of expressions on the face."""
        ...
    def ExpressionGetName(self,ExpressionId:int)->str:
        """Retrieve the name of an expression.
        ### Parameters:
        - ExpressionId: Index of the expression to query.
        
        ### Returns:
        Name of the specified expression."""
        ...
    def ExpressionGetShapeWeight(self,ExpressionId:int,GrpId:int,ShapeId:int)->float:
        """Retrieve the weight of a shape to an expression.
        ### Parameters:
        - ExpressionId: Index of the expression.
        - GrpId: Index of the blendshape or cluster group containing the shape of interest.
        - ShapeId: Index of the blendshape or cluster shape.
        
        ### Returns:
        Weight of the desired shape to an expression. A weight of 0.0 represents 0%, while a weight of 1.0 represents 100%. Returns 0.0 if the weight cannot be found."""
        ...
    def ExpressionRemove(self,ExpressionId:int)->bool:
        """Remove an expression from the face.
        ### Parameters:
        - ExpressionId: Index of the expression to remove.
        
        ### Returns:
        True if the operation completed successfully."""
        ...
    def ExpressionSetName(self,ExpressionId:int,Name:str)->bool:
        """Set the name of an expression.
        ### Parameters:
        - ExpressionId: Index of the expression to modify.
        - Name: Name to assign to the expression.
        
        ### Returns:
        True if the operation completed successfully."""
        ...
    def ExpressionSetShapeWeight(self,ExpressionId:int,GrpId:int,ShapeId:int,Value:float)->bool:
        """Assign the weight of a shape to an expression.
        ### Parameters:
        - ExpressionId: Index of the expression to modify.
        - GrpId: Index of the blendshape or cluster group containing the shape of interest.
        - ShapeId: Index of the blendshape or cluster shape to weight.
        - Value: Weight of the shape to assign to this expression. A weight of 0.0 represents 0%, while a weight of 1.5 represents 150%. The weight cannot be less than 0.0; if so, the weight will be clamped to 0.0.
        
        ### Returns:
        True if the operation completed successfully."""
        ...
    def GotoRest(self):
        """Set the character face back to its rest shape."""
        ...
    def PlotAnimation(self)->bool:
        """Plot the animation of the character face.
        ### Returns:
        True if the operation completed successfully."""
        ...
    def ShapeFindByName(self,ShapeGrpId:int,Name:str)->int:
        """Find a shape in a blendshape group by name.
        ### Parameters:
        - ShapeGrpId: Index of the blendshape group to search.
        - Name: Name to search for.
        
        ### Returns:
        Index of the shape, -1 if not found."""
        ...
    def ShapeGetCount(self,ShapeGrpId:int)->int:
        """Retrieve the total number of shapes in a blendshape group.
        ### Parameters:
        - ShapeGrpId: Index of the blendshape group to query.
        
        ### Returns:
        Number of shapes in the specified blendshape group."""
        ...
    def ShapeGetName(self,ShapeGrpId:int,ShapeId:int)->str:
        """Retrieve the name of the shape in a blendshape group.
        ### Parameters:
        - ShapeGrpId: Index of the blendshape group to query.
        - ShapeId: Index of the shape in the blendshape group to query.
        
        ### Returns:
        Name of the specified shape."""
        ...
    def ShapeGroupAdd(self,List:FBModelList,Name:str)->bool:
        """Add a blendshape model group for each input model.
        ### Parameters:
        - List: List of models to create a blendshape model group.
        - Name: Unused. Instead, use the ShapeGroupGetName member function to set the name of each added blendshape model group individually.
        
        ### Returns:
        True if the operation completed successfully, false otherwise."""
        ...
    def ShapeGroupFindByName(self,Name:str)->int:
        """Find a blendshape group by name.
        ### Parameters:
        - Name: Name to search for.
        
        ### Returns:
        Index of the blendshape group, -1 if not found."""
        ...
    def ShapeGroupGetCount(self)->int:
        """Retrieve the total number of blendshape groups on this character face.
        ### Returns:
        Number of blendshape groups on this character face."""
        ...
    def ShapeGroupGetName(self,ShapeGrpId:int)->str:
        """Retrieve the name of a blendshape group.
        ### Parameters:
        - ShapeGrpId: Index of the blendshape group to query.
        
        ### Returns:
        Name of the blendshape group."""
        ...
    def ShapeGroupRemove(self,ShapeGrpId:int)->bool:
        """Remove a blendshape model group.
        ### Parameters:
        - ShapeGrpId: Index of the blendshape group to remove.
        
        ### Returns:
        True if the operation completed successfully."""
        ...
    def ShapeGroupSetName(self,ShapeGrpId:int,Name:str)->bool:
        """Set the name of a blendshape group.
        ### Parameters:
        - ShapeGrpId: Index of the blendshape group to modify.
        - Name: Name to set on the blendshape group.
        
        ### Returns:
        True if the operation completed successfully."""
        ...
    def ShapeSetName(self,ShapeGrpId:int,ShapeId:int,Name:str)->bool:
        """Set the name of the shape in a blendshape group.
        ### Parameters:
        - ShapeGrpId: Index of the blendshape group to query.
        - ShapeId: Index of the shape in the blendshape group to set.
        - Name: Name to set on the shape.
        
        ### Returns:
        True if the operation completed successfully."""
        ...
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of new character."""
        ...
class FBCharacter(FBConstraint):
    ActiveInput:bool
    CharacterExtensions:FBPropertyListCharacterExtension
    ContactBehaviour:FBCharacterContactBehaviour
    FKFingerMultiplier:float
    FKFingerTipMultiplier:float
    FKThumbTipMultiplier:float
    HipsTranslationMode:FBCharacterHipsTranslationMode
    HumanFingerLimits:bool
    InputActor:FBActor
    InputCharacter:FBCharacter
    InputType:FBCharacterInputType
    InverseLeftElbow:bool
    InverseLeftKnee:bool
    InverseRightElbow:bool
    InverseRightKnee:bool
    KeyingMode:FBCharacterKeyingMode
    LeftElbowKillPitch:bool
    LeftHandIndexIndex:float
    LeftHandIndexMiddle:float
    LeftHandIndexPinky:float
    LeftHandIndexRing:float
    LeftHandMiddleIndex:float
    LeftHandMiddleMiddle:float
    LeftHandMiddlePinky:float
    LeftHandMiddleRing:float
    LeftHandPinkyIndex:float
    LeftHandPinkyMiddle:float
    LeftHandPinkyPinky:float
    LeftHandPinkyRing:float
    LeftHandRingIndex:float
    LeftHandRingMiddle:float
    LeftHandRingPinky:float
    LeftHandRingRing:float
    LeftKneeKillPitch:bool
    LockX:bool
    LockY:bool
    LockZ:bool
    MirrorMode:bool
    RightElbowKillPitch:bool
    RightHandIndexIndex:float
    RightHandIndexMiddle:float
    RightHandIndexPinky:float
    RightHandIndexRing:float
    RightHandMiddleIndex:float
    RightHandMiddleMiddle:float
    RightHandMiddlePinky:float
    RightHandMiddleRing:float
    RightHandPinkyIndex:float
    RightHandPinkyMiddle:float
    RightHandPinkyPinky:float
    RightHandPinkyRing:float
    RightHandRingIndex:float
    RightHandRingMiddle:float
    RightHandRingPinky:float
    RightHandRingRing:float
    RightKneeKillPitch:bool
    RollSolver:FBCharacterRollSolver
    ShoulderCorrection:float
    SyncMode:bool
    WriteReference:bool
    def AddCharacterExtension(self,Ext:FBCharacterExtension):
        """### Parameters:
        - Ext: extension to be added to the character."""
        ...
    def ConnectControlRig(self,ControlSet:FBControlSet,bUpdateLimit:bool,bResetHierarchy:bool):
        """Connect a Control-Rig to the character.
        ### Parameters:
        - ControlSet: The control set to connect. `None` will disconnect the Control-Rig from the character.
        - bUpdateLimit: Whether to update the models' limit for a character. E.g. the Pre rotation and post rotation.
        - bResetHierarchy: Whether to reset hierarchy for a character."""
        ...
    def CopyAnimation(self):
        """Copy the animation from the input character to us."""
        ...
    def CreateAuxiliary(self,EffectorId:FBEffectorId,bPivot:bool,AuxReachT:float=100,AuxReachR:float=100)->bool:
        """Create auxiliary on effector.
        ### Parameters:
        - EffectorId: The effector ID.
        - bPivot: Create effector or pivot (pivot offset should be set on IKPivot property, at creation default values are set).
        - AuxReachT: Default auxiliary effector reach for translation (IK Blend T since MotionBuilder 2013).
        - AuxReachR: Default auxiliary effector reach for rotation (IK Blend R since MotionBuilder 2013).
        
        ### Returns:
        True if auxiliary was created (can fail if FBLastEffectorSetIndex limit reached)."""
        ...
    def CreateCharacterMarkerSet(self,bSetActive:bool)->bool:
        """Create the Character Marker Set.
        ### Parameters:
        - bSetActive: True when new input should be set and active.
        
        ### Returns:
        True when marker got created and connected to character."""
        ...
    def CreateControlRig(self,bSetFKIK:bool)->bool:
        """Create the Control-Rig.
        ### Parameters:
        - bSetFKIK: true to use FK/IK or false to use IK only.
        
        ### Returns:
        current state of the flag after the operation (true if it did succeed)."""
        ...
    def CycleAnalysisCurrentCharacter(self):
        """Run Cycle Analysis on current character."""
        ...
    def DisconnectControlRig(self):
        """Disconnect the Control-Rig from the character."""
        ...
    def GetActiveBodyPart(self)->list:
        """Get the active body part array."""
        ...
    def GetCharacterMarkerSet(self,bForce:bool)->FBCharacterMarkerSet:
        """Obtain Input CharacterMarkerSet.
        ### Parameters:
        - bForce: If True, will return the current CharacterMarkerSet even if the character is not in CharacterMarkerSet Input.
        
        ### Returns:
        Return current Active CharacterMarkerSet, `None` if none."""
        ...
    def GetCharacterize(self)->bool:
        """Get Characterize flag.
        ### Returns:
        Current state of the Characterize flag."""
        ...
    def GetCharacterizeError(self)->str:
        """Get error message for the previous SetCharacterizeOn operation.
        ### Returns:
        The string containing all errors and warnings."""
        ...
    def GetCtrlRigModel(self,BodyNodeId:FBBodyNodeId)->FBModel:
        """Get the model associated with each body part in the Control Rig of the character.
        ### Returns:
        The model in the Control Rig corresponding to the specified body part."""
        ...
    def GetCurrentControlSet(self)->FBControlSet:
        """Obtain Input ControlSet.
        ### Returns:
        Return current Active ControlSet, `None` if none."""
        ...
    def GetCycleAnalysisNode(self)->FBCycleAnalysisNode:
        """Get the Cycle Analysis Node from the current character.
        ### Returns:
        Cycle Analysis Node linked to the current character, or create a new node"""
        ...
    def GetEffectorModel(self,EffectorId:FBEffectorId,EffectorSetID:FBEffectorSetID=FBEffectorSetID.FBEffectorSetDefault)->FBModel:
        """Get the model associated with each effector in the Control Rig of the character.
        ### Parameters:
        - EffectorId: The effector ID.
        - EffectorSetID: Id of the ControlSet to obtain, if not specified the current one is taken.
        
        ### Returns:
        The model in the Control Rig corresponding to the specified Effector."""
        ...
    def GetExternalSolver(self)->FBCharacterSolver:
        """Get a pointer to the external solver of a character, or `None` is no external solver is used on the character.
        ### Returns:
        The pointer of the current External Solver, `None` if it's the internal solver."""
        ...
    def GetFKVisibility(self)->FBVisibilityState:
        """Get the FK visibility state.
        ### Returns:
        The FK visibility state."""
        ...
    def GetFloorContactModel(self,MemberIndex:FBFloorContactID)->FBModel:
        """Get the model associated with the floor contact ID.
        ### Parameters:
        - MemberIndex: Id of the floor contact
        
        ### Returns:
        The model associated with the floor contact ID"""
        ...
    def GetGoalModel(self,BodyNodeId:FBBodyNodeId)->FBModel:
        """Get the goal model associated with each body part in the Character Marker Set of the character.
        ### Returns:
        The model in the Character Marker Set corresponding to the specified body part."""
        ...
    def GetIKVisibility(self)->FBVisibilityState:
        """Get the IK visibility state.
        ### Returns:
        The IK visibility state."""
        ...
    def GetIndexByModel(self,Model:FBModelSkeleton)->FBBodyNodeId:
        """Get the index associated with Given Model.
        ### Returns:
        The model linked to the specified body part."""
        ...
    def GetModel(self,BodyNodeId:FBBodyNodeId)->FBModel:
        """Get the model associated with each body part of the character.
        ### Returns:
        The model linked to the specified body part."""
        ...
    def GetParentROffset(self,arg2:FBBodyNodeId,arg3:FBVector3d):...
    def GetROffset(self,arg2:FBBodyNodeId,arg3:FBVector3d):...
    def GetSOffset(self,arg2:FBBodyNodeId,arg3:FBVector3d):...
    def GetSkeletonVisibility(self)->FBVisibilityState:
        """Get the skeleton visibility state.
        ### Returns:
        The skeleton visibility state."""
        ...
    def GetSkinModelList(self,SkinModelList:FBModelList):
        """Get the skin model associated with character bones.
        Could be deformable model connected to bone via cluster, or non deformable model parented directly under the bones.
        ### Parameters:
        - SkinModelList: List to be filled up. (will not be cleared)"""
        ...
    def GetTOffset(self,arg2:FBBodyNodeId,arg3:FBVector4d):...
    def GetTransformOffset(self,arg2:FBBodyNodeId,arg3:FBMatrix):...
    def GoToStancePose(self,bPushUndo:bool=False,bIncludeCharacterExtensions:bool=True):
        """Set the character in stance pose.
        ### Parameters:
        - bPushUndo: Should we push an undo transaction on the undo stack? Don't push undo in non UI thread.
        - bIncludeCharacterExtensions: Should the character extensions go to stance pose too?"""
        ...
    def IsParentNodeOffset(self,NodeId:FBBodyNodeId)->bool:
        """Check if there is an offset on Parent.
        ### Parameters:
        - NodeId: Node Id to Check.
        
        ### Returns:
        True if there is an offset on Parent."""
        ...
    def IsRotationPin(self,EffectorIndex:FBEffectorId)->bool:
        """Return true if the object is Pinned in Rotation (Manipulation).
        ### Parameters:
        - EffectorIndex: Given Index to obtain Model
        
        ### Returns:
        True if the effector is pinned in Rotation"""
        ...
    def IsTranslationPin(self,EffectorIndex:FBEffectorId)->bool:
        """Return true if the object is Pinned in Translation (Manipulation).
        ### Parameters:
        - EffectorIndex: Given Index to obtain Model
        
        ### Returns:
        True if the effector is pinned in Translation"""
        ...
    def PlotAnimation(self,PlotWhere:FBCharacterPlotWhere,PlotOptions:FBPlotOptions)->bool:
        """Plot the animation of the character.
        When plotting onto Control Rig while the Control Rig being the source of the Character, only the selected properties, based on the active keying group, will be plotted.
        ### Parameters:
        - PlotWhere: Where to plot a character, control rig or Skeleton
        - PlotOptions: Option parameters for plotting
        
        ### Returns:
        True if the operation completed successfully."""
        ...
    def ReadyForRetarget(self)->bool:
        """Test if character is ready for the Retarget operation (basically, is it in character input ?).
        ### Returns:
        True if the character is ready."""
        ...
    def RemoveCharacterExtension(self,Ext:FBCharacterExtension):
        """Get the model associated with each body part of the character.
        ### Parameters:
        - Ext: extension to be removed to the character."""
        ...
    def ResetProperties(self,Type:FBCharacterResetProperties):
        """Reset the properties of the character.
        ### Parameters:
        - Type: Speficy which properties will be reset."""
        ...
    def Retarget(self,bOnBaseLayer:bool):
        """Retarget the animation from the input character to us.
        ### Parameters:
        - bOnBaseLayer: if true, keys corrections will be made on base layer; else they will be made on another layer."""
        ...
    def SelectModels(self,bSelect:bool,bApplyToCharacter:bool,bApplyToRig:bool,bApplyToExtensions:bool):
        """Select the objects that make a character.
        ### Parameters:
        - bSelect: True to select, false to deselect.
        - bApplyToCharacter: TSould the character contraint be selected ?
        - bApplyToRig: should The rig (and its children) be selected ?
        - bApplyToExtensions: Should the character extensions (and their children) be selected ?"""
        ...
    def SetCharacterizeOff(self):
        """Set Characterize flag off."""
        ...
    def SetCharacterizeOn(self,bSetAsBiped:bool)->bool:
        """Set the Characterize flag on.
        ### Parameters:
        - bSetAsBiped: true to use biped characterization or false to use quadruped.
        
        ### Returns:
        current state of the flag after the operation (true if it did succeed)."""
        ...
    def SetExternalSolver(self,Solver:FBCharacterSolver):
        """Set character solver.
        ### Parameters:
        - Solver: Character solver that will be used by the character."""
        ...
    def SetExternalSolverWithIndex(self,arg2):...
    def SetFKVisibility(self,bState:bool)->bool:
        """Set the FK visibility state.
        ### Parameters:
        - bState: The FK visibility state.
        
        ### Returns:
        True if the operation is successful, false otherwise."""
        ...
    def SetIKVisibility(self,bState:bool)->bool:
        """Set the IK visibility state.
        ### Parameters:
        - bState: The IK visibility state.
        
        ### Returns:
        True if the operation is successful, false otherwise."""
        ...
    def SetRotationPin(self,EffectorIndex:FBEffectorId,bValue:bool)->bool:
        """Set the object Pinned in Rotation (Manipulation) status.
        ### Parameters:
        - EffectorIndex: Given Index to obtain Model.
        - bValue: The object Pinned in Rotation status.
        
        ### Returns:
        True if the operation is successful, false otherwise."""
        ...
    def SetSkeletonVisibility(self,bState:bool)->bool:
        """Set the skeleton visibility state.
        ### Parameters:
        - bState: The skeleton visibility state.
        
        ### Returns:
        True if the operation is successful, false otherwise."""
        ...
    def SetTranslationPin(self,EffectorIndex:FBEffectorId,bValue:bool)->bool:
        """Set the object Pinned in Translation (Manipulation) status.
        ### Parameters:
        - EffectorIndex: Given Index to obtain Model
        - bValue: The object Pinned in Translation status.
        
        ### Returns:
        True if the operation is successful, false otherwise."""
        ...
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of new character."""
        ...
class FBActor(FBConstraint):
    BodyColor:FBColor
    ChestOffsetR:FBVector3d
    ChestOffsetT:FBVector3d
    ChestPosition:FBVector3d
    FKFingerMultiplier:float
    FKFingerTipMultiplier:float
    FKThumbTipMultiplier:float
    HeadOffsetR:FBVector3d
    HeadOffsetT:FBVector3d
    HeadPosition:FBVector3d
    HipsOffsetR:FBVector3d
    HipsOffsetT:FBVector3d
    HipsPosition:FBVector3d
    HumanFingerLimits:bool
    IKManip:bool
    LeftAnkleOffsetR:FBVector3d
    LeftAnkleOffsetT:FBVector3d
    LeftAnklePosition:FBVector3d
    LeftCollarOffsetR:FBVector3d
    LeftCollarOffsetT:FBVector3d
    LeftCollarPosition:FBVector3d
    LeftElbowOffsetR:FBVector3d
    LeftElbowOffsetT:FBVector3d
    LeftElbowPosition:FBVector3d
    LeftFootOffsetR:FBVector3d
    LeftFootOffsetT:FBVector3d
    LeftFootPosition:FBVector3d
    LeftHandIndexIndex:float
    LeftHandIndexMiddle:float
    LeftHandIndexPinky:float
    LeftHandIndexRing:float
    LeftHandMiddleIndex:float
    LeftHandMiddleMiddle:float
    LeftHandMiddlePinky:float
    LeftHandMiddleRing:float
    LeftHandPinkyIndex:float
    LeftHandPinkyMiddle:float
    LeftHandPinkyPinky:float
    LeftHandPinkyRing:float
    LeftHandRingIndex:float
    LeftHandRingMiddle:float
    LeftHandRingPinky:float
    LeftHandRingRing:float
    LeftHipOffsetR:FBVector3d
    LeftHipOffsetT:FBVector3d
    LeftHipPosition:FBVector3d
    LeftIndexAOffsetR:FBVector3d
    LeftIndexAOffsetT:FBVector3d
    LeftIndexBOffsetR:FBVector3d
    LeftIndexBOffsetT:FBVector3d
    LeftIndexCOffsetR:FBVector3d
    LeftIndexCOffsetT:FBVector3d
    LeftKneeOffsetR:FBVector3d
    LeftKneeOffsetT:FBVector3d
    LeftKneePosition:FBVector3d
    LeftMiddleAOffsetR:FBVector3d
    LeftMiddleAOffsetT:FBVector3d
    LeftMiddleBOffsetR:FBVector3d
    LeftMiddleBOffsetT:FBVector3d
    LeftMiddleCOffsetR:FBVector3d
    LeftMiddleCOffsetT:FBVector3d
    LeftPinkyAOffsetR:FBVector3d
    LeftPinkyAOffsetT:FBVector3d
    LeftPinkyBOffsetR:FBVector3d
    LeftPinkyBOffsetT:FBVector3d
    LeftPinkyCOffsetR:FBVector3d
    LeftPinkyCOffsetT:FBVector3d
    LeftRingAOffsetR:FBVector3d
    LeftRingAOffsetT:FBVector3d
    LeftRingBOffsetR:FBVector3d
    LeftRingBOffsetT:FBVector3d
    LeftRingCOffsetR:FBVector3d
    LeftRingCOffsetT:FBVector3d
    LeftShoulderOffsetR:FBVector3d
    LeftShoulderOffsetT:FBVector3d
    LeftShoulderPosition:FBVector3d
    LeftThumbAOffsetR:FBVector3d
    LeftThumbAOffsetT:FBVector3d
    LeftThumbBOffsetR:FBVector3d
    LeftThumbBOffsetT:FBVector3d
    LeftThumbCOffsetR:FBVector3d
    LeftThumbCOffsetT:FBVector3d
    LeftWristOffsetR:FBVector3d
    LeftWristOffsetT:FBVector3d
    LeftWristPosition:FBVector3d
    ManipulateOffsets:bool
    MarkerSet:FBMarkerSet
    MarkerSetSize:float
    NeckOffsetR:FBVector3d
    NeckOffsetT:FBVector3d
    NeckPosition:FBVector3d
    OutputMarkerSet:FBMarkerSet
    PivotColor:FBColor
    PivotPointsVisibility:bool
    PivotSize:float
    RightAnkleOffsetR:FBVector3d
    RightAnkleOffsetT:FBVector3d
    RightAnklePosition:FBVector3d
    RightCollarOffsetR:FBVector3d
    RightCollarOffsetT:FBVector3d
    RightCollarPosition:FBVector3d
    RightElbowOffsetR:FBVector3d
    RightElbowOffsetT:FBVector3d
    RightElbowPosition:FBVector3d
    RightFootOffsetR:FBVector3d
    RightFootOffsetT:FBVector3d
    RightFootPosition:FBVector3d
    RightHandIndexIndex:float
    RightHandIndexMiddle:float
    RightHandIndexPinky:float
    RightHandIndexRing:float
    RightHandMiddleIndex:float
    RightHandMiddleMiddle:float
    RightHandMiddlePinky:float
    RightHandMiddleRing:float
    RightHandPinkyIndex:float
    RightHandPinkyMiddle:float
    RightHandPinkyPinky:float
    RightHandPinkyRing:float
    RightHandRingIndex:float
    RightHandRingMiddle:float
    RightHandRingPinky:float
    RightHandRingRing:float
    RightHipOffsetR:FBVector3d
    RightHipOffsetT:FBVector3d
    RightHipPosition:FBVector3d
    RightIndexAOffsetR:FBVector3d
    RightIndexAOffsetT:FBVector3d
    RightIndexBOffsetR:FBVector3d
    RightIndexBOffsetT:FBVector3d
    RightIndexCOffsetR:FBVector3d
    RightIndexCOffsetT:FBVector3d
    RightKneeOffsetR:FBVector3d
    RightKneeOffsetT:FBVector3d
    RightKneePosition:FBVector3d
    RightMiddleAOffsetR:FBVector3d
    RightMiddleAOffsetT:FBVector3d
    RightMiddleBOffsetR:FBVector3d
    RightMiddleBOffsetT:FBVector3d
    RightMiddleCOffsetR:FBVector3d
    RightMiddleCOffsetT:FBVector3d
    RightPinkyAOffsetR:FBVector3d
    RightPinkyAOffsetT:FBVector3d
    RightPinkyBOffsetR:FBVector3d
    RightPinkyBOffsetT:FBVector3d
    RightPinkyCOffsetR:FBVector3d
    RightPinkyCOffsetT:FBVector3d
    RightRingAOffsetR:FBVector3d
    RightRingAOffsetT:FBVector3d
    RightRingBOffsetR:FBVector3d
    RightRingBOffsetT:FBVector3d
    RightRingCOffsetR:FBVector3d
    RightRingCOffsetT:FBVector3d
    RightShoulderOffsetR:FBVector3d
    RightShoulderOffsetT:FBVector3d
    RightShoulderPosition:FBVector3d
    RightThumbAOffsetR:FBVector3d
    RightThumbAOffsetT:FBVector3d
    RightThumbBOffsetR:FBVector3d
    RightThumbBOffsetT:FBVector3d
    RightThumbCOffsetR:FBVector3d
    RightThumbCOffsetT:FBVector3d
    RightWristOffsetR:FBVector3d
    RightWristOffsetT:FBVector3d
    RightWristPosition:FBVector3d
    SkeletonColor:FBColor
    SkeletonVisibility:bool
    SymmetryEditRotation:bool
    SymmetryEditScaling:bool
    SymmetryEditTranslation:bool
    Visibility:bool
    WaistOffsetR:FBVector3d
    WaistOffsetT:FBVector3d
    WaistPosition:FBVector3d
    @overload
    def GetCurrentSkeletonState(self)->FBSkeletonState:...
    @overload
    def GetCurrentSkeletonState(self,bResetOrientation:bool)->FBSkeletonState:
        """Return the Current Skeleton State.
        ### Parameters:
        - bResetOrientation: When set to true, all rotations in the state will be reset to characterization values.
        
        ### Returns:
        Current Skeleton State
        
        ### Note:
        Usage of this function can be found in script sample /bin/config/Scripts/Samples/Character/CharacterMarkerSetFromActor.py"""
        ...
    def GetDefaultSkeletonState(self)->FBSkeletonState:
        """Return the Default Skeleton State.
        ### Returns:
        Default Skeleton State"""
        ...
    def GetDefinitionRotationVector(self,SkeletonId:FBSkeletonNodeId,RotationVector:FBVector3d):
        """Get Actor Rotation Definition.
        Only effective when IKManip property is set to false.
        ### Parameters:
        - SkeletonId: Skeleton Node Id
        
        ### Return values:
        - RotationVector: Actor Rotation Definition for the given ID"""
        ...
    def GetDefinitionScaleVector(self,SkeletonId:FBSkeletonNodeId,ScaleVector:FBVector3d):
        """Get Actor Scaling Definition.
        ### Parameters:
        - SkeletonId: Skeleton Node Id
        
        ### Return values:
        - ScaleVector: Actor Scaling Definition for the given ID"""
        ...
    def GetDefinitionTranslationVector(self,SkeletonId:FBSkeletonNodeId,TranslationVector:FBVector3d):
        """Get Actor Translation Definition.
        Only effective when IKManip property is set to false.
        ### Parameters:
        - SkeletonId: Skeleton Node Id
        
        ### Return values:
        - TranslationVector: Actor Translation Definition for the given ID"""
        ...
    def SetActorTranslation(self,TranslationVector:FBVector3d):
        """Translate Actor, similar to moving the hips of the Actor in the UI.
        Only effective when IKManip property is set to false.
        ### Parameters:
        - TranslationVector: Will move the entire Actor to TranslationVector coordinate"""
        ...
    def SetDefinitionRotationVector(self,SkeletonId:FBSkeletonNodeId,RotationVector:FBVector3d,bSymmetricUpdate:bool=True):
        """Set Actor Rotation Definition.
        Only effective when IKManip property is set to false.
        ### Parameters:
        - SkeletonId: Skeleton Node Id
        - RotationVector: Actor Rotation value for the given ID
        - bSymmetricUpdate: Update right and left part at the same time"""
        ...
    def SetDefinitionScaleVector(self,SkeletonId:FBSkeletonNodeId,ScaleVector:FBVector3d,bSymmetricUpdate:bool=True):
        """Set Actor Scaling Definition.
        ### Parameters:
        - SkeletonId: Skeleton Node Id
        - ScaleVector: Actor Scaling value for the given ID
        - bSymmetricUpdate: Update right and left part at the same time"""
        ...
    def SetDefinitionTranslationVector(self,SkeletonId:FBSkeletonNodeId,TranslationVector:FBVector3d,bSymmetricUpdate:bool=True):
        """Set Actor Translation Definition.
        Only effective when IKManip property is set to false.
        ### Parameters:
        - SkeletonId: Skeleton Node Id
        - TranslationVector: Actor Translation value for the given ID
        - bSymmetricUpdate: Update right and left part at the same time"""
        ...
    def UpdateValues(self,EvalInfo:FBEvaluateInfo):
        """Update Internal Values to be corresponding to the Given Evaluate Information.
        ### Parameters:
        - EvalInfo: Evaluate Info of the Values"""
        ...
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of new actor."""
        ...
class FBConstraintRelation(FBConstraint):
    Boxes:FBPropertyListBox
    def ConstrainObject(self,ConstrainedObject:FBBox)->FBBox:
        """Create a receiver box.
        Use an existing FBBox object to create a receiver in the relation.
        ### Parameters:
        - ConstrainedObject: Destination box to insert in the constraint.
        
        ### Returns:
        A place holder box for the object."""
        ...
    def CreateFunctionBox(self,Group:str,Name:str)->FBBox:
        """Create a function box.
        Ask the constraint to create new function box.
        ### Parameters:
        - Group: Name of the group under which the function is located in the Constraint Relation GUI (case-sensitive!).
        - Name: Name of the function, as seen in the GUI (case-sensitive!).
        
        ### Returns:
        The newly created function box, or `None` if the name/group combination was invalid."""
        ...
    def GetBoxPosition(self,Box:FBBox)->bool:
        """Get a box position in the GUI.
        Get the position of a box within the constraint layout view.
        ### Parameters:
        - Box: Box from which the information will be queried.
        ### Returns:
        A boolean value indicating success (True) or failure (False).
        
        ### Warning:
        Should the function return False, the X and Y values will not be set."""
        ...
    def SetAsSource(self,Source:FBBox)->FBBox:
        """Create a sender box.
        Use an existing FBBox object to create a sender in the relation.
        ### Parameters:
        - Source: Source box to insert in the constraint.
        
        ### Returns:
        A place holder box for the object."""
        ...
    def SetBoxPosition(self,Box:FBBox,X:int,Y:int)->bool:
        """Set a box position in the GUI.
        Set the position of a box within the constraint layout view.
        ### Parameters:
        - Box: Box which needs to be moved.
        - X: New X position.
        - Y: New Y position.
        
        ### Returns:
        A boolean value indicating success (True) or failure (False)."""
        ...
    def __init__(self,Name:str=None):
        """### Parameters:
        - Name: Name of constraint."""
        ...
class FBCycleAnalysisNode(FBBox):
    RealTime:bool
    RootHMode:FBRootHMode
    RootRMode:FBRootRMode
    RootSpeedMode:FBRootSpeedMode
    RootXZMode:FBRootXZMode
    def GetPoseFCurve(self)->object:...
    def GetRootHFCurve(self)->object:...
    def GetRootRFCurve(self)->object:...
    def GetRootSpeedFCurve(self)->object:...
    def GetRootXZFCurve(self)->object:...
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of new cycle analysis node."""
        ...
class FBConstraintSolver(FBConstraint):
    def __init__(self,arg2:str=None):...
class FBDevice(FBBox):
    CommType:int
    HardwareVersionInfo:str
    Information:str
    ModelBindingRoot:FBModel
    ModelTemplate:FBModelTemplate
    Online:bool
    RecordingStartTime:FBTime
    RecordingStopTime:FBTime
    SamplingMode:FBDeviceSamplingMode
    SamplingPeriod:FBTime
    Status:str
    def AckOneBadSampleReceived(self):
        """Acknowlege that one bad sample was received (for statistical purposes)."""
        ...
    def AckOneSampleReceived(self):
        """Acknowlege that one sample was received (for statistical purposes)."""
        ...
    def AckOneSampleSent(self):
        """Acknowlege that one sample was sent (for statistical purposes)."""
        ...
    def ModelBindingCreate(self)->FBModel:
        """Create a new model binding.
        ### Returns:
        The model root that has been created or `None` is an error occured."""
        ...
    def ModelBindingRootsList(self,List:FBModelList):
        """Get the list of all the possible root models for binding.
        ### Return values:
        - List: List to add found models to."""
        ...
    def RecordingDoneAnimation(self,AnimationNode:FBAnimationNode):
        """When recording, finish animation.
        ### Parameters:
        - AnimationNode: Animation node to write information to."""
        ...
    def RecordingInitAnimation(self,AnimationNode:FBAnimationNode):
        """When recording, initialize animation.
        ### Parameters:
        - AnimationNode: Animation node to read information from."""
        ...
class FBGlobalLight(FBBox):
    AmbientColor:FBColor
    FogBegin:float
    FogColor:FBColor
    FogDensity:float
    FogEnable:bool
    FogEnd:float
    FogMode:FBFogMode
    def __init__(self):...
class FBDeviceOptical(FBDevice):
    AutoAntialiasing:bool
    DampingTime:float
    ForceOpticalSamplingRate:bool
    MarkerTimeStamp:FBTime
    Markers:FBPropertyListDeviceOpticalMarker
    ModelOptical:FBModel
    OpticalSamplingRate:float
    SkipFrame:bool
    SupportOcclusion:bool
    UseMarkerTimeStamp:bool
    def DeviceOperation(self,Operation:kDeviceOperations)->bool:
        """Operate device.
        This is an operation such as Init, Start, Done, Reset, etc.
        ### Parameters:
        - Operation: Operation to have device perform.
        
        ### Returns:
        Current state : <b true if online.
        Reimplemented from FBDevice ."""
        ...
    def DeviceOpticalBeginSetup(self):
        """Begin device setup."""
        ...
    def DeviceOpticalEndSetup(self):
        """End device setup."""
        ...
    def DeviceOpticalRecordFrame(self,Time:FBTime,DeviceNotifyInfo:FBDeviceNotifyInfo):
        """Record a frame of information from device.
        Virtual function that derived class may overide
        ### Parameters:
        - Time: Time of evaluation.
        - DeviceNotifyInfo: Notification information when thread was called."""
        ...
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Unique name of optical device."""
        ...
class FBGroup(FBBox):
    Items:FBPropertyListComponent
    Pickable:bool
    Show:bool
    Transformable:bool
    def Clone(self)->FBGroup:
        """Clone the group.
        This will duplicated the current group.
        ### Returns:
        Newly created group."""
        ...
    def Contains(self,Component:FBComponent)->bool:
        """### Parameters:
        - Component: Component to verify if it is in the Group
        
        ### Returns:
        True if the object is in the Group"""
        ...
    def Select(self,bSelect:bool):
        """### Parameters:
        - bSelect: If true , group contents will be selected."""
        ...
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Group name."""
        ...
class FBHUD(FBBox):
    EStockElement:type
    Elements:FBPropertyListHUDElement
    HUDs:FBPropertyListHUD
    OnDisplay:FBEvent
    Visibility:bool
    eBloopSlate:EStockElement
    eFlashElement:EStockElement
    eRecordLight:EStockElement
    eRectElement:EStockElement
    eTextElement:EStockElement
    eTextureElement:EStockElement
    eTimeline:EStockElement
    def CreateCustomElement(self,HUDElementClassName:str,Name:str)->FBHUDElement:
        """Creates a custom HUD Element.
        ### Parameters:
        - HUDElementClassName: The HUD Element class name (mainly, the ClassName parameter of the FBStorableCustomHUDElementImplementation macro).
        - Name: Name for the custom HUD Element to create.
        
        ### Returns:
        The created custom HUD Element."""
        ...
    def CreateElement(self,Type:EStockElement,Name:str)->FBHUDElement:
        """Creates a stock HUD Element.
        ### Parameters:
        - Type: View to be called for expose.
        - Name: Name for the HUD Element to create.
        
        ### Returns:
        The created HUD Element."""
        ...
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of new HUD."""
        ...
class FBHUDElement(FBBox):
    Height:float
    HorizontalDock:FBHUDElementHAlignment
    Justification:FBHUDElementHAlignment
    PositionByPercent:bool
    ScaleByPercent:bool
    ScaleUniformly:bool
    Show:bool
    VerticalDock:FBHUDElementVAlignment
    Visibility:bool
    Width:float
    X:float
    Y:float
class FBHandle(FBBox):
    Follow:FBPropertyListObject
    Image:FBPropertyListObject
    Manipulate:FBPropertyListObject
    ManipulateRotation:FBPropertyListObject
    ManipulateScaling:FBPropertyListObject
    ManipulateTranslation:FBPropertyListObject
    def Select(self):
        """Meta selection.
        With this method, the handle itself is selected as well as all the models that are manipulated by the handle."""
        ...
    def __init__(self,Name:str):
        """This constructor is used to create a new object.
        ### Parameters:
        - Name: Object name."""
        ...
class FBHUDFlashElement(FBHUDElement):
    FilePath:str
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of new HUD flash element."""
        ...
class FBHUDRectElement(FBHUDElement):
    Color:FBColorAndAlpha
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of new HUD rectangle element."""
        ...
class FBHUDBloopSlateElement(FBHUDFlashElement):
    BackgroundColor:FBColorAndAlpha
    Enable:bool
    ForegroundColor:FBColorAndAlpha
    ShowAfterDelayOnRecordPlay:FBTime
    ShowDuration:FBTime
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of new HUD flash element."""
        ...
class FBHUDTimelineElement(FBHUDFlashElement):
    CutActiveColor:FBColorAndAlpha
    CutIdleColor:FBColorAndAlpha
    HeadActiveColor:FBColorAndAlpha
    HeadDuration:FBTime
    HeadIdleColor:FBColorAndAlpha
    TailActiveColor:FBColorAndAlpha
    TailDuration:FBTime
    TailIdleColor:FBColorAndAlpha
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of new HUD flash element."""
        ...
class FBHUDTextElement(FBHUDElement):
    AdjustWidthToFitText:bool
    BackgroundColor:FBColorAndAlpha
    Color:FBColorAndAlpha
    Content:str
    Font:str
    ForceTimeCodeDisplay:bool
    def GetFontList(self)->FBStringList:
        """Returns a list of supported fonts."""
        ...
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of new HUD text element."""
        ...
class FBHUDTextureElement(FBHUDElement):
    Texture:FBPropertyListTexture
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of new HUD texture element."""
        ...
class FBMaterial(FBBox):
    Ambient:FBColor
    AmbientFactor:float
    Bump:FBColor
    BumpFactor:float
    Diffuse:FBColor
    DiffuseFactor:float
    DisplacementColor:FBColor
    DisplacementFactor:float
    Emissive:FBColor
    EmissiveFactor:float
    NormalMap:FBColor
    Reflection:FBColor
    ReflectionFactor:float
    Shininess:float
    Specular:FBColor
    SpecularFactor:float
    TransparencyFactor:float
    TransparentColor:FBColor
    def Clone(self)->FBMaterial:
        """Clone the material.
        This will duplicated the current material.
        ### Returns:
        Newly created material."""
        ...
    def GetTexture(self,Type:FBMaterialTextureType=FBMaterialTextureType.kFBMaterialTextureDiffuse)->FBTexture:
        """Retrieve associated texture.
        ### Parameters:
        - Type: MaterialTextureType to get connected texture from (default is Diffuse is not specified)."""
        ...
    def OGLInit(self):
        """Setup OpenGL fixed pipeline material settings."""
        ...
    def SetTexture(self,Texture:FBTexture,Type:FBMaterialTextureType=FBMaterialTextureType.kFBMaterialTextureDiffuse):
        """Set associated texture.
        ### Parameters:
        - Texture: texture to be connected.
        - Type: MaterialTextureType to set connected texture to."""
        ...
    def __copy__(self)->object:...
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of material."""
        ...
class FBModel(FBBox):
    AnimationNode:FBAnimationNode
    BlendShapeDeformable:bool
    CastsShadows:bool
    Children:FBPropertyListModel
    ConstrainDeformable:bool
    CullingMode:property
    Deformers:FBPropertyListDeformer
    GeometricRotation:FBVector3d
    GeometricScaling:FBVector3d
    GeometricTranslation:FBVector3d
    Geometry:FBGeometry
    GeometryUpdateId:int
    Icon3D:bool
    IsConstrained:bool
    IsDeformable:bool
    IsVisible:bool
    LookAt:FBModel
    Materials:FBPropertyListMaterial
    ModelVertexData:FBModelVertexData
    Parent:FBModel
    Pickable:bool
    PointCacheDeformable:bool
    PointCacheRecord:bool
    PostRotation:FBVector3d
    PreRotation:FBVector3d
    PrimaryVisibility:bool
    QuaternionInterpolate:bool
    ReceiveShadows:bool
    Rotation:FBVector3d
    RotationActive:bool
    RotationMax:FBVector3d
    RotationMaxX:bool
    RotationMaxY:bool
    RotationMaxZ:bool
    RotationMin:FBVector3d
    RotationMinX:bool
    RotationMinY:bool
    RotationMinZ:bool
    RotationOrder:FBModelRotationOrder
    RotationSpaceForLimitOnly:bool
    Scaling:FBVector3d
    Scene:FBScene
    Shaders:FBPropertyListShader
    ShadingMode:FBModelShadingMode
    Show:bool
    SkeletonDeformable:bool
    SoftSelected:bool
    Textures:FBPropertyListTexture
    Transformable:bool
    Translation:FBVector3d
    UniqueColorId:FBColor
    UpVector:FBModel
    Visibility:bool
    VisibilityInheritance:bool
    def Clone(self)->FBModel:
        """Clone the model.
        This will duplicate the current model.
        ### Returns:
        Newly created model."""
        ...
    def CollapseInSchematic(self):
        """Collapse the model in the schematic view."""
        ...
    def DofToLRM(self,LM:FBMatrix,Dof:FBVector3d):
        """Convert object space vector to local matrix.
        ### Parameters:
        - LM: Resulting local rotation matrix.
        - Dof: Vector to convert
        
        ### Note:
        Use this function when you want to convert euler to local rotation with proper pre/post transformation and rotation order applied from this model."""
        ...
    def ExpandInSchematic(self):
        """Expand the model in the schematic view."""
        ...
    def FbxGetObjectSubType(self)->str:
        """Returns the class sub type inherited by the class of an object, for example: 'Default', 'Mesh'.
        Reimplemented from FBBox .
        Reimplemented in FBModelMarker , and FBModelNull ."""
        ...
    def FbxGetObjectType(self)->str:
        """Returns the class type inherited by the class of an object, for example: 'Model'.
        Reimplemented from FBBox .
        Reimplemented in FBModelMarker , and FBModelNull ."""
        ...
    def ForceAlwaysEvaluate(self):
        """Force Always Evaluate.
        In some case, MoBu kernel perform optimization by skipping certain evaluation tasks. This function stop skipping for this model."""
        ...
    def GetAdditionalUniqueColorID(self,Index:int)->FBColor:
        """Get Additional Unique Color Id.
        ### Parameters:
        - Index: the requested unique color id index, can't be larger than GetAdditionalColorIDCount()
        
        ### Returns:
        Additional Unique ColorId."""
        ...
    def GetAdditionalUniqueColorIDCount(self)->int:
        """Get additional unique color count.
        ### Returns:
        Additional Unique Color Count."""
        ...
    def GetBoundingBox(self,Min:FBVector3d,Max:FBVector3d):
        """Get the bounding box of the model.
        Note. for deformable model, this function will provide the approximated (larger than the smallest) bounding box for performance consideration.
        ### Parameters:
        - Min: Output parameter. Minimum value of the bounding box.
        - Max: Output parameter. Maximum value of the bounding box."""
        ...
    def GetHierarchyWorldMatrices(self,MatricesArray:int,MatricesArrayCount:FBModelHiercharyTraverserType,HiercharyTraverserType:FBEvaluateInfo=None)->list:
        """Computes the global transform matrices between this model and all its children (all levels).
        The hierarchy world matrix for a model is represented as a global transform matrix applied on an arbitrary root hierarchy node (this model for instance), considered as the world reference.
        ### Parameters:
        - MatricesArray: The matrix array (memory already allocated) to fill in with the hierarchy world matrix of all the model's children models
        - MatricesArrayCount: The size of the matrix array
        ### Return values:
        - HiercharyTraverserType: The hierarchy traverser type
        
        ### Parameters:
        ### Return values:
        - Number: of matrices filled in the array. The value may be different than MatricesArrayCount if the number of children models is less than the size of the matrix array."""
        ...
    def GetLocalTransformationMatrixWithGlobalRotationDoF(self,Matrix:FBMatrix,bInverse:bool=False,EvaluateInfo:FBEvaluateInfo=None):
        """Get the local transformation (or local inverse transformation) matrix with the global Rotation DoF values from the model.
        The GetMatrix method was previously wrongly returning the local transformation (and local inverse transformation) matrices with global Rotation DoF values. The GetMatrix method implementation has been updated to not include the global Rotation DoF values. This method returns the same matrix values returned by the legacy GetMatrix implementation when retrieving the local transformation (and local inverse transformation) matrices.
        ### Parameters:
        - Matrix: Matrix to fill with requested information.
        - bInverse: False for the transformation matrix, true for the inverse transformation matrix.
        - EvaluateInfo: EvaluateInfo, Take Display if none specified."""
        ...
    def GetMatrix(self,Matrix:FBMatrix,What:FBModelTransformationType=FBModelTransformationType.kModelTransformation,bGlobalInfo:bool=True,EvaluateInfo:FBEvaluateInfo=None):
        """Get a matrix from the model.
        ### Parameters:
        - Matrix: Matrix to fill with requested information.
        - What: Type of information requested (default=transformation).
        - bGlobalInfo: true if it is GlobalInfo, false if Local (default=true).
        - EvaluateInfo: EvaluateInfo, Take Display if none specified."""
        ...
    def GetSchematicPosition(self)->FBVector2d:
        """Get the position in the schematic view for the model.
        ### Returns:
        Current position for the model."""
        ...
    def GetSelectedPointsCount(self)->int:
        """Get the number of selected points in the model.
        ### Returns:
        Number of selected points."""
        ...
    def GetVector(self,Vector:FBVector3d,What:FBModelTransformationType=FBModelTransformationType.kModelTranslation,bGlobalInfo:bool=True,EvaluateInfo:FBEvaluateInfo=None):
        """Get a vector from the model.
        ### Parameters:
        - Vector: Vector to fill with requested values.
        - What: Type of information requested (default=translation, inverses not supported).
        - bGlobalInfo: true if it is GlobalInfo, false if Local (default=true).
        - EvaluateInfo: EvaluateInfo, Take Display if none specified"""
        ...
    def IsCollapsedInSchematic(self)->bool:
        """Returns if the model is collapsed or not (expanded) in the schematic view.
        ### Returns:
        true if the model is collapsed in the schematic view, false if it is expanded."""
        ...
    def IsEvaluationReady(self,What:FBModelEvaluationTaskType,EvaluateInfo:FBEvaluateInfo=None)->bool:
        """Is the model's evaluation task result ready.
        ### Parameters:
        - What: Type of evaluation task.
        - EvaluateInfo: EvaluateInfo, Take Display if none specified
        
        ### Return values:"""
        ...
    def IsForceAlwaysEvaluate(self)->bool:
        """Return Force Always Evaluate status."""
        ...
    def LRMToDof(self,Dof:FBVector3d,LM:FBMatrix):
        """Convert local matrix to object space vector.
        ### Parameters:
        - Dof: Resulting object space vector.
        - LM: Local rotation matrix to convert
        
        ### Note:
        Use this function when you want to convert local rotation to euler with proper pre/post transformation and rotation order applied from this model."""
        ...
    def MatrixToRotation(self,Rotation:FBVector3d,Matrix:FBMatrix):
        """Convert Rotation Matrix to Euler Vector based on model's rotation order.
        ### Parameters:
        - Rotation: Resulting euler vector, whose angles are stored in [X,Y,Z] order.
        - Matrix: Matrix to convert."""
        ...
    def NoFrustumCullingRelease(self)->int:
        """Release no frustum culling request.
        ### Returns:
        Current no frustum culling request count after function call."""
        ...
    def NoFrustumCullingRequire(self)->int:
        """Acquire no frustum culling request.
        ### Returns:
        Current no frustum culling request count after function call."""
        ...
    def RayCast(self,Camera:FBCamera,MouseX:int,MouseY:int,HitPosition:FBVector3d,HitNormal:FBVector3d)->bool:
        """Ray cast test.
        ### Parameters:
        - Camera: Camera to use for casting.
        - MouseX: Mouse X position.
        - MouseY: Mouse Y position.
        - HitPosition: Ray cast position on the object.
        - HitNormal: Normal at the ray cast position on the object.
        
        ### Returns:
        true if it hit the meshes, hit would contains the precise position & normal."""
        ...
    def RotationToMatrix(self,Matrix:FBMatrix,Rotation:FBVector3d):
        """Convert Euler Vector to Rotation Matrix based on model's rotation order.
        ### Parameters:
        - Matrix: Resulting rotation matrix.
        - Rotation: Object space rotation vector to convert, whose angles are stored in [X,Y,Z] order."""
        ...
    def SetAdditionalUniqueColorIDCount(self,Count:int)->bool:
        """Request additional Unique color IDs.
        ### Parameters:
        - Count: User should note that Unique Color ID resource is limited (only 24 bits), hence should avoid to use unnecessary large number.
        
        ### Returns:
        True if Unique ColorId resource is available."""
        ...
    def SetMatrix(self,Matrix:FBMatrix,What:FBModelTransformationType=FBModelTransformationType.kModelTransformation,bGlobalInfo:bool=True,PushUndo:FBEvaluateInfo=False):
        """Set a matrix for the model.
        ### Parameters:
        - Matrix: Information to use to set the model's matrix.
        - What: Type of matrix to set (default=transformation).
        - bGlobalInfo: true if it is GlobalInfo, false if Local (default=true).
        - PushUndo: true if this operation is undoable, don't push undo in non UI thread."""
        ...
    def SetMatrixWithPrecision(self,Matrix:FBMatrix,What:FBModelTransformationType=FBModelTransformationType.kModelTransformation,bGlobalInfo:bool=True,PushUndo:FBEvaluateInfo=False,EvaluateInfo:FBEvaluateInfo=None):
        """Set a matrix for the model.
        ### Parameters:
        - Matrix: Information to use to set the model's matrix.
        - What: Type of matrix to set (default=transformation).
        - bGlobalInfo: true if it is GlobalInfo, false if Local (default=true).
        - PushUndo: true if this operation is undoable, don't push undo in non UI thread.
        - EvaluateInfo: EvaluateInfo, Take Display if none specified"""
        ...
    @overload
    def SetSchematicPosition(self,X:int,Y:int):
        """Set the position in the schematic view for the model.
        ### Parameters:
        - X: X position to set.
        - Y: Y position to set."""
        ...
    @overload
    def SetSchematicPosition(self,Vector2d:FBVector2d):
        """Set the position in the schematic view for the model.
        ### Parameters:
        - Vector2d: Position to set."""
        ...
    def SetVector(self,Vector:FBVector3d,What:FBModelTransformationType=FBModelTransformationType.kModelTranslation,bGlobalInfo:bool=True,PushUndo:FBEvaluateInfo=False):
        """Set a vector for the model.
        ### Parameters:
        - Vector: Vector to use to set values.
        - What: Type of information to set (default=translation, inverses not supported).
        - bGlobalInfo: true if it is GlobalInfo, false if Local (default=true).
        - PushUndo: true if this operation is undoable, don't push undo in non UI thread."""
        ...
    def SetupPropertiesForShapes(self):
        """Setup Shape Properties.
        Normally this function is called automatically at the next global synchronization point after the geometry has been updated. However you must call it explicitly to access the shape properties immediately after shapes adding/removing before next global synchronization point."""
        ...
    def UseFrustumCulling(self)->bool:
        """Get the current Frustum Culling Status.
        ### Returns:
        True if model don't use frustum culling currently."""
        ...
    def __copy__(self)->object:...
class FBNote(FBBox):
    StaticComment:str
    def Attach(self,Comp:FBComponent=None)->bool:
        """Attach the note to a component.
        Will attach the note to the component. If Comp is NULL, the note will only be added to the scene.
        ### Parameters:
        - Comp: Component on which to attach note.
        
        ### Returns:
        A boolean indicating if the operation was successful or not."""
        ...
    def Detach(self,Comp:FBComponent=None)->bool:
        """Detach the note from a component.
        Will detach the note from the component. If Comp is NULL, the note will be removed from the scene and detached from all components.
        ### Parameters:
        - Comp: Component from which to detach note.
        
        ### Returns:
        A boolean indicating if the operation was successful or not."""
        ...
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of note."""
        ...
class FBModelCube(FBModel):
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of cube."""
        ...
class FBLight(FBModel):
    AreaLightShape:property
    AttenuationType:FBAttenuationType
    BottomBarnDoor:float
    CastLightOnObject:bool
    CastShadows:bool
    ConeAngle:float
    DiffuseColor:FBColor
    DrawFrontFacingVolumetric:bool
    DrawGroundProjection:bool
    DrawVolumetricLight:bool
    EAreaLightShapes:type
    EnableBarnDoor:bool
    FogIntensity:float
    GoboMedia:FBVideo
    InnerAngle:float
    Intensity:float
    LeftBarnDoor:float
    LightType:FBLightType
    OuterAngle:float
    RightBarnDoor:float
    TopBarnDoor:float
    eRectangle:EAreaLightShapes
    eSphere:EAreaLightShapes
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of light."""
        ...
class FBCameraSwitcher(FBModel):
    CurrentCamera:FBCamera
    CurrentCameraIndex:int
    def PlotToCamera(self,Camera:FBCamera)->bool:
        """Plot the Camera Switcher animation onto a destination camera.
        The destination camera cannot be a system camera nor a camera currently used by the Camera Switcher.
        ### Parameters:
        - Camera: Destination camera to plot on.
        
        ### Returns:
        True if the plot operation has been processed successfully, false otherwise."""
        ...
    def UseEvaluateSwitch(self):...
    def __init__(self):...
class FBCamera(FBModel):
    AnimatableFarPlane:property
    AnimatableNearPlane:property
    AntiAliasingIntensity:float
    AntiAliasingMethod:FBCameraAntiAliasingMethod
    ApertureMode:FBCameraApertureMode
    BackGroundColor:FBColor
    BackGroundImageCenter:bool
    BackGroundImageCrop:bool
    BackGroundImageFit:bool
    BackGroundImageKeepRatio:bool
    BackGroundImageOffsetX:float
    BackGroundImageOffsetY:float
    BackGroundImageScaleX:float
    BackGroundImageScaleY:float
    BackGroundMedia:FBVideo
    BackGroundPlaneDistance:float
    BackGroundPlaneDistanceMode:FBCameraDistanceMode
    BackGroundTexture:FBTexture
    CameraViewportHeight:int
    CameraViewportWidth:int
    CameraViewportX:int
    CameraViewportY:int
    Display2DMagnifierFrame:bool
    DisplayTurnTableIcon:bool
    FarPlaneDistance:float
    FieldOfView:float
    FieldOfViewX:float
    FieldOfViewY:float
    FilmAspectRatio:float
    FilmBackType:FBCameraFilmBackType
    FilmSizeHeight:float
    FilmSizeWidth:float
    FocalLength:float
    FocusAngle:float
    FocusDistanceSource:FBCameraFocusDistanceSource
    FocusModel:FBModel
    FocusSpecificDistance:float
    ForeGroundAlpha:float
    ForeGroundImageCenter:bool
    ForeGroundImageCrop:bool
    ForeGroundImageFit:bool
    ForeGroundImageKeepRatio:bool
    ForeGroundImageOffsetX:float
    ForeGroundImageOffsetY:float
    ForeGroundImageScaleX:float
    ForeGroundImageScaleY:float
    ForeGroundMaterialThreshold:float
    ForeGroundMedia:FBVideo
    ForeGroundPlaneDistance:float
    ForeGroundPlaneDistanceMode:FBCameraDistanceMode
    ForeGroundTexture:FBTexture
    ForeGroundTransparent:bool
    FrameColor:FBColor
    FrameSizeMode:FBCameraFrameSizeMode
    HUDs:FBPropertyListHUD
    InteractiveMode:bool
    Interest:FBModel
    MagnifierPosX:float
    MagnifierPosY:float
    MagnifierZoom:float
    MotionBlurIntensity:float
    MouseLockCamera:bool
    NearPlaneDistance:float
    NumberOfSamples:int
    OpticalCenterX:float
    OpticalCenterY:float
    OrthoFactor:float
    OrthoZoom:float
    PixelAspectRatio:float
    ResolutionHeight:float
    ResolutionMode:FBCameraResolutionMode
    ResolutionWidth:float
    Roll:float
    SafeAreaMode:FBCameraSafeAreaMode
    SamplingType:FBCameraSamplingType
    SqueezeRatio:float
    SystemCamera:bool
    TurnTable:float
    Type:FBCameraType
    Use2DMagnifier:bool
    UseAccumulationBuffer:bool
    UseAntiAliasing:bool
    UseDepthOfField:bool
    UseFrameColor:bool
    UseMotionBlur:bool
    UseRealTimeMotionBlur:bool
    ViewBackGroundPlaneMode:FBCameraViewPlaneMode
    ViewCameraInterest:bool
    ViewDisplaySafeArea:bool
    ViewForeGroundPlaneMode:FBCameraViewPlaneMode
    ViewNearFarPlane:bool
    ViewOpticalCenter:bool
    ViewShowAxis:bool
    ViewShowGrid:bool
    ViewShowName:bool
    ViewShowTimeCode:bool
    WindowHeight:float
    WindowWidth:float
    def GetCameraMatrix(self,Matrix:FBMatrix,Type:FBCameraMatrixType,EvalInfo:FBEvaluateInfo=None):
        """Obtains the camera's matrix.
        ### Parameters:
        - Matrix: Matrix to fill with requested information.
        - Type: Camera Matrix type to obtain.
        - EvalInfo: Take Display if none specified."""
        ...
    @overload
    def InverseProjection(self,arg2,arg3,arg4)->FBVector4d:...
    @overload
    def InverseProjection(self,X:int,Y:int,DistanceFromCamera:float,bRelativeToViewport:bool)->FBVector4d:
        """Returns the world coordinates based on screen coordinates and input distance from the camera.
        ### Parameters:
        - X: Screen horizontal coordinate in pixel. When bRelativeToViewport is false, the range is between 0 and (WindowWidth - 1). When bRelativeToViewport is true, the range is between 0 to (CameraViewportWidth - 1). The coordinate starts at left of the region.
        - Y: Screen vertical coordinate in pixel. When bRelativeToViewport is false, the range is between 0 and (WindowHeight - 1). When bRelativeToViewport is true, the range is between 0 to (CameraViewportHeight - 1). The coordinate starts at top of the region.
        - DistanceFromCamera: Distance from the camera to the resulting world coordinate position
        - bRelativeToViewport: true indicates (X,Y) is relative to the window; false indicates (X,Y) is relative to the viewport of the camera.
        
        ### Returns:
        The world coordinates in 3D space"""
        ...
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of camera."""
        ...
class FBModelMarker(FBModel):
    Color:FBColor
    IKPivot:FBVector3d
    Length:float
    Look:FBMarkerLook
    ResLevel:FBMarkerResolutionLevel
    Size:float
    Type:FBMarkerType
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of model marker. If pObject is not NULL, Name will be ignored."""
        ...
class FBCameraStereo(FBCamera):
    CenterCamera:property
    DisplayZeroParallaxPlane:property
    FilmOffsetLeftCam:property
    FilmOffsetRightCam:property
    InteraxialSeparation:property
    LeftCamera:property
    PrecompFileName:property
    RelativePrecompFileName:property
    RightCamera:property
    Stereo:property
    ToeInAdjust:property
    ZeroParallax:property
    ZeroParallaxPlaneColor:property
    ZeroParallaxPlaneTransparency:property
    def __init__(self,arg2:str):...
class FBModelNull(FBModel):
    Size:float
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of null."""
        ...
class FBModelMarkerOptical(FBModelMarker):
    Data:FBAnimationNode
    Done:bool
    Gaps:FBPropertyListOpticalGap
    Optical:FBModelOptical
    Segments:FBPropertyListMarkerSegment
    def ExportBegin(self)->int:
        """Begin export of optical data.
        Sample communication with optical device and return the number of samples that were taken during the sampling period for statistical purposes.
        ### Returns:
        Number of frames to export."""
        ...
    def ExportEnd(self)->bool:
        """End exportation from optical model.
        ### Returns:
        true if successful."""
        ...
    def ExportKey(self,X:float,Y:float,Z:float=None,Occlusion:float=None)->bool:
        """Export a key of optical data.
        ### Return values:
        - X.: X position.
        - Y.: Y position.
        - Z.: Z position(default=NULL).
        - Occlusion.: Occlusion value(default=NULL).
        
        ### Returns:
        true if successful."""
        ...
    def GetRigidBody(self)->FBRigidBody:
        """Get the rigid body for the marker.
        ### Returns:
        Rigid body for marker (check IsValid())"""
        ...
    def ImportBegin(self)->int:
        """Begin import of optical data.
        Sample communication with optical device and return the number of samples that were taken during the sampling period for statistical purposes.
        ### Returns:
        The number of samples taken."""
        ...
    def ImportEnd(self)->bool:
        """End importation and clean up data.
        Interpolates optical data to create a curve from the input key frams.
        ### Returns:
        true if successful."""
        ...
    def ImportKey(self,X:float,Y:float,Z:float=0.0,Occlusion:float=0.0)->bool:
        """Import a key of optical data.
        ### Parameters:
        - X: X position.
        - Y: Y position.
        - Z: Z position(default=0.0).
        - Occlusion: Occlusion value(default=0.0).
        
        ### Returns:
        true if successful."""
        ...
    def InsertSegmentedData(self,TData:FBAnimationNode,OData:FBAnimationNode):
        """Insert segmented data.
        ### Parameters:
        - TData: Translation data.
        - OData: Occlusion data."""
        ...
    def SetModelOptical(self,Optical:FBModelOptical):
        """Set the current optical model.
        ### Parameters:
        - Optical: New optical model."""
        ...
    def __init__(self,Name:str,Optical:FBModelOptical):
        """If no optical model is given, be sure to add one before accessing the Segments and Gaps properties.
        ### Parameters:
        - Name: Name of optical marker(default=NULL).
        - Optical: Optical model(default=NULL)."""
        ...
class FBModelOptical(FBModel):
    MarkerSize:float
    Markers:FBPropertyListModelMarkerOptical
    RigidBodies:FBPropertyListRigidBody
    SamplingPeriod:FBTime
    SamplingStart:FBTime
    SamplingStop:FBTime
    Segments:FBPropertyListOpticalSegment
    def ClearSegments(self,bUnUsedOnly:bool=True):
        """Clear the segments (by default only the unused).
        ### Parameters:
        - bUnUsedOnly: Clear only the unused segments if true (default=true)."""
        ...
    def CreateRigidBody(self,RigidBodyName:str,Markers:list)->FBRigidBody:
        """Create a new rigid body from the given optical markers.
        ### Parameters:
        - RigidBodyName: The name for the new rigid body to create. If left empty, the default "Rigid Body" name will be used.
        - Markers: The optical markers for creating the new rigid body.
        
        ### Returns:
        The created rigid body if successful, and invalid rigid body otherwise. You can use the FBRigidBody.IsValid() method to test if the returned rigid body object is valid or not."""
        ...
    def ExportSetup(self)->bool:
        """Setup exportation from optical model.
        ### Returns:
        true if successful."""
        ...
    def ImportSetup(self)->bool:
        """Setup importation for optical model.
        ### Returns:
        true if successful."""
        ...
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of optical model."""
        ...
class FBModelPath3D(FBModel):
    AutoControlNode:bool
    Color:FBColor
    EKeyPropertyBehavior:type
    ELengthUnitType:type
    EPathEndCapStyle:type
    KeyPropertyBehavior:property
    PathEndCapScale:float
    PathEndCapStyle:property
    PathLength:float
    PathLengthInString:str
    PathLengthShow:bool
    PathLengthUnit:property
    TextBackground:FBColorAndAlpha
    TextScale:float
    eArchitectural:ELengthUnitType
    eArrow:EPathEndCapStyle
    eCM:ELengthUnitType
    eKM:ELengthUnitType
    eLegacyVector4:EKeyPropertyBehavior
    eM:ELengthUnitType
    eMI:ELengthUnitType
    eNone:EPathEndCapStyle
    eVector:EKeyPropertyBehavior
    def ConvertSegmentPercentToTotalPercent(self,Percent:float,EvaluateInfo:FBEvaluateInfo=None)->float:
        """Converting one key type Segment (time) to Total (percent).
        ### Parameters:
        - Percent: Double value (as time)
        
        ### Returns:
        Double value which represents the corresponding percentage"""
        ...
    def ConvertToSegmentPercentFactor(self)->float:
        """Get factor for multiplying the derivative of a key for segment mode.
        ### Returns:
        Returns the derivative multiplication factor"""
        ...
    def ConvertToTotalPercentFactor(self)->float:
        """Get factor for multiplying the derivative of a key for total mode.
        ### Returns:
        Returns the time factor"""
        ...
    def ConvertTotalPercentToSegmentPercent(self,Percent:float,EvaluateInfo:FBEvaluateInfo=None)->float:
        """Converting one key type Total (percent) to Segment (time).
        ### Parameters:
        - Percent: Double value (as percentage)
        
        ### Returns:
        Double value which represents the corresponding time."""
        ...
    def GetSelectedPathKeyCount(self)->int:
        """Query the number of keys present in the selected path.
        ### Returns:
        Returns the number of keys in the selected path"""
        ...
    def InsertNewEndKey(self)->int:
        """Insert a new key at the end of the path.
        ### Returns:
        Returns (N) where (N+1) is the new total number of keys, and since the new key becomes the Nth key (index starts from 0). If path is invalid, returns 0."""
        ...
    def InsertNewStartKey(self)->int:
        """Insert a new key at the start of the path.
        ### Returns:
        Returns 0 since the new key becomes the first key. If path is invalid, returns 0."""
        ...
    def PathKeyClear(self):
        """Clear the path keys."""
        ...
    def PathKeyEndAdd(self,TLocal:FBVector4d)->int:
        """Adds a new key to the end of the path (with time gap of 1 sec).
        The derivative value for the new key is copied from the left tangent of the last key.
        ### Parameters:
        - TLocal: Vector value for the new added Key
        
        ### Returns:
        Returns (N) where (N+1) is the new total number of keys, and since the new key becomes the Nth key (index starts from 0). If path is invalid, returns 0."""
        ...
    def PathKeyGet(self,KeyIndex:int)->FBVector4d:
        """Get path's key vector for at a particular key index.
        ### Parameters:
        - KeyIndex: Key ID to set with
        
        ### Returns:
        Return the vector containing the value of the path key."""
        ...
    def PathKeyGetControlNode(self,KeyIndex:int)->FBModel:
        """Get the path key's control node.
        Only works when KeyPropertyBehavior is eVector.
        ### Parameters:
        - KeyIndex: Key ID to get
        
        ### Returns:
        Path key's corresponding control node if successful, otherwise NULL."""
        ...
    def PathKeyGetCount(self)->int:
        """Query the number of keys present in the path.
        ### Returns:
        Number of keys present in the path"""
        ...
    def PathKeyGetLeftTangent(self,KeyIndex:int)->FBVector4d:
        """Get the path key left tangent's vector value for designated index.
        ### Parameters:
        - KeyIndex: Key ID at which left tangent value is required
        
        ### Returns:
        Vector containing value of left tangent"""
        ...
    def PathKeyGetLeftTangentLength(self,KeyIndex:int)->float:
        """Query the length of the left tangent.
        ### Parameters:
        - KeyIndex: Key ID to set with
        
        ### Returns:
        Double value of the length of left tangent"""
        ...
    def PathKeyGetProperty(self,KeyIndex:int)->FBProperty:
        """Get the path key's corresponding property.
        Only works when KeyPropertyBehavior is eVector.
        ### Parameters:
        - KeyIndex: Key ID to get
        
        ### Returns:
        Path key's corresponding property if successful, otherwise NULL."""
        ...
    def PathKeyGetRightTangent(self,KeyIndex:int)->FBVector4d:
        """Get the path key right tangent's vector value for designated index.
        ### Parameters:
        - KeyIndex: Key ID to set with
        
        ### Returns:
        Vector containing value of left tangent"""
        ...
    def PathKeyGetRightTangentLength(self,KeyIndex:int)->float:
        """Query the value of the right tangent.
        ### Parameters:
        - KeyIndex: Key ID to set with
        
        ### Returns:
        Double value of the length of right tangent"""
        ...
    def PathKeyGetXYZDerivative(self,KeyIndex:int)->FBVector4d:
        """Get vector in XYZ coordinates for a path tangent.
        This works only if key interpolation type is CUBIC and tangent mode is User, Break or Auto.
        ### Parameters:
        - KeyIndex: Key ID to set with
        
        ### Returns:
        Vector with value for path's tangent XYZ derivatives"""
        ...
    def PathKeyInsertAfter(self,KeyIndex:int,TLocal:FBVector4d)->int:
        """Adds a new key immediately after the specified key ID (with time gap of 1 sec).
        The following keys are all shifted by 1 sec.
        ### Parameters:
        - KeyIndex: Key ID to insert after. If key ID < 0 then the behavior is the same as PathKeyStartAdd. If key ID >= PathKeyGetCount-1 then the behavior is the same as PathKeyEndAdd.
        - TLocal: Vector value for the new added Key
        
        ### Returns:
        Returns the newly inserted key ID."""
        ...
    def PathKeyRemove(self,KeyIndex:int):
        """Remove key at a particular index.
        ### Parameters:
        - KeyIndex: Key ID at which key is to be removed."""
        ...
    def PathKeyRemoveSelected(self):
        """Remove the selected keys from the path."""
        ...
    def PathKeySet(self,KeyIndex:int,TLocal:FBVector4d,bUpdate:bool=True):
        """Set the local coordinate vector values for path at a particular key index.
        ### Parameters:
        - KeyIndex: Key ID to set with
        - TLocal: Vector to use to set values to Key
        - bUpdate: true if geometry update is required, false if not required (default=true)"""
        ...
    def PathKeySetControlNode(self,KeyIndex:int,ControlNode:FBModel)->bool:
        """Set the path key's control node.
        Only works when KeyPropertyBehavior is eVector and AutoControlNode is disabled.
        ### Parameters:
        - KeyIndex: Key ID to set
        - ControlNode: Model to set as path key's control node.
        
        ### Returns:
        True if successful, otherwise false."""
        ...
    def PathKeySetLeftRightTangent(self,KeyIndex:int,KeyTLocal:FBVector4d,LeftTangentTLocal:FBVector4d,RightTangentTLocal:FBVector4d,bUpdate:bool=True):
        """Set path's vectors for key, left tangent and right tangent at a particular key index.
        ### Parameters:
        - KeyIndex: Key ID to set key for left and right tangents
        - KeyTLocal: Vector to use to set values to Key
        - LeftTangentTLocal: Vector to use to set values to Key Left Tangent
        - RightTangentTLocal: Vector to use to set values to Key Right Tangent
        - bUpdate: true if geometry update is required, false if not required (default=true)"""
        ...
    def PathKeySetLeftTangent(self,KeyIndex:int,TLocal:FBVector4d,bUpdate:bool=True):
        """Set path's key left tangent vector for designated index.
        ### Parameters:
        - KeyIndex: Key ID at which left tangent is to be set
        - TLocal: Vector to use to set values to Key
        - bUpdate: true if geometry update is required, false if not required (default=true)"""
        ...
    def PathKeySetRightTangent(self,KeyIndex:int,TLocal:FBVector4d,bUpdate:bool=True):
        """Set 3D path's key right tangent vector for designated index.
        ### Parameters:
        - KeyIndex: Key ID at which right tangent is to be set
        - TLocal: Vector to use to set values to Key
        - bUpdate: true if geometry update is required, false if not required (default=true)"""
        ...
    def PathKeySetXDerivative(self,KeyIndex:int,Derivative:float,bUpdate:bool):
        """Set derivative in X coordinate for a path tangent.
        This works only if key interpolation type is CUBIC and tangent mode is User, Break or Auto.
        ### Parameters:
        - KeyIndex: Key ID to set with
        - Derivative: Value of the derivative to apply to tangent
        - bUpdate: true if geometry update is required, false if not required (default=true)"""
        ...
    def PathKeySetXYZDerivative(self,KeyIndex:int,Derivative:FBVector4d,bUpdate:bool):
        """Set derivative in XYZ coordinates for a path tangent.
        This works only if key interpolation type is CUBIC and tangent mode is User, Break or Auto.
        ### Parameters:
        - KeyIndex: Key ID to set with
        - Derivative: Value of the derivative to apply to tangent
        - bUpdate: true if geometry update is required, false if not required (default=true)"""
        ...
    def PathKeySetYDerivative(self,KeyIndex:int,Derivative:float,bUpdate:bool):
        """Set derivative in Y coordinate for a path tangent.
        This works only if key interpolation type is CUBIC and tangent mode is User, Break or Auto.
        ### Parameters:
        - KeyIndex: Key ID to set with
        - Derivative: Value of the derivative to apply to tangent
        - bUpdate: true if geometry update is required, false if not required (default=true)"""
        ...
    def PathKeySetZDerivative(self,KeyIndex:int,Derivative:float,bUpdate:bool):
        """Set derivative in Z coordinate for a path tangent.
        This works only if key interpolation type is CUBIC and tangent mode is User, Break or Auto.
        ### Parameters:
        - KeyIndex: Key ID to set with
        - Derivative: Value of the derivative to apply to tangent
        - bUpdate: true if geometry update is required, false if not required (default=true)"""
        ...
    def PathKeyStartAdd(self,TLocal:FBVector4d)->int:
        """Adds a new key to the start of the path (with time gap of 1 sec).
        The derivative value for the new key is copied from the right tangent of the first key.
        ### Parameters:
        - TLocal: Vector value for the new added Key
        
        ### Returns:
        Returns 0 since the new key becomes the first key. If path is invalid, returns 0."""
        ...
    def Segment_GlobalPathEvaluate(self,SegmentPercent:float,EvaluateInfo:FBEvaluateInfo=None)->FBVector4d:
        """Get the path's vector at a particular point within the curve, in global coordinates.
        ### Parameters:
        - SegmentPercent: Double value (as time) at which the path vector would be computed
        
        ### Returns:
        Vector value at the required point in the path"""
        ...
    def Segment_GlobalPathEvaluateDerivative(self,SegmentPercent:float,EvaluateInfo:FBEvaluateInfo=None)->FBVector4d:
        """Get the path's derivative at a particular point within the curve, in global coordinates.
        ### Parameters:
        - SegmentPercent: Double value (as time) at which the path derivative would be computed
        
        ### Returns:
        Vector value at the required point in the path"""
        ...
    def Segment_IsPathKey(self,SegmentPercent:float,EvaluateInfo:FBEvaluateInfo=None)->int:
        """Query whether a percentage value has a key associated at that point in the path.
        ### Parameters:
        - SegmentPercent: Double value (as time) at which the path would be queried for existence of key
        
        ### Returns:
        A valid key index in integer if key is present, otherwise -1"""
        ...
    def Segment_LocalPathEvaluate(self,SegmentPercent:float,EvaluateInfo:FBEvaluateInfo=None)->FBVector4d:
        """Get the path's vector at a particular point within the curve, in local coordinates.
        ### Parameters:
        - SegmentPercent: Double value (as time) at which the path vector would be computed
        
        ### Returns:
        Vector value at the required point in the path"""
        ...
    def Segment_LocalPathEvaluateDerivative(self,SegmentPercent:float,EvaluateInfo:FBEvaluateInfo=None)->FBVector4d:
        """Get the path's derivative at a particular point within the curve, in local coordinates.
        ### Parameters:
        - SegmentPercent: Double value (as time) at which the path derivative would be computed
        
        ### Returns:
        Vector value at the required point in the path"""
        ...
    def ShowCurveControls(self,bShow:bool):
        """Enable or disable displaying Curve Controls for the 3D model path.
        ### Parameters:
        - bShow: true if curve controls are to be displayed false if not required"""
        ...
    def ShowCurvePoints(self,bShow:bool):
        """Enable or disable displaying Curve Points for the 3D model path.
        ### Parameters:
        - bShow: true if curve points are to be displayed false if not required"""
        ...
    def Total_GlobalPathEvaluate(self,TotalPercent:float,EvaluateInfo:FBEvaluateInfo=None)->FBVector4d:
        """Get the path's vector at a particular point within the curve, in global coordinates.
        ### Parameters:
        - TotalPercent: Double value (as percentage) at which the path vector would be computed
        
        ### Returns:
        Vector value at the required point in the path"""
        ...
    def Total_GlobalPathEvaluateDerivative(self,TotalPercent:float,EvaluateInfo:FBEvaluateInfo=None)->FBVector4d:
        """Get the path's derivative at a particular point within the curve, in global coordinates.
        ### Parameters:
        - TotalPercent: Double value (as percentage) at which the path derivative would be computed
        
        ### Returns:
        Derivative value at the required point in the path"""
        ...
    def Total_IsPathKey(self,TotalPercent:float,EvaluateInfo:FBEvaluateInfo=None)->int:
        """Query whether a percentage value has a key associated at that point in the path.
        ### Parameters:
        - TotalPercent: Double value (as percentage) at which the path would be queried for existence of key
        
        ### Returns:
        A valid key index in integer if key is present, otherwise -1"""
        ...
    def Total_LocalPathEvaluate(self,TotalPercent:float,EvaluateInfo:FBEvaluateInfo=None)->FBVector4d:
        """Get the path's vector at a particular point within the curve, in local coordinates.
        ### Parameters:
        - TotalPercent: Double value (as percentage) at which the path vector would be computed
        
        ### Returns:
        Vector value at the required point in the path"""
        ...
    def Total_LocalPathEvaluateDerivative(self,TotalPercent:float,EvaluateInfo:FBEvaluateInfo=None)->FBVector4d:
        """Get the path's derivative at a particular point within the curve, in local coordinates.
        ### Parameters:
        - TotalPercent: Double value (as percentage) at which the path derivative would be computed
        
        ### Returns:
        Derivative value at the required point in the path"""
        ...
    def UpdateGeometry(self):
        """Update path geometry explicitly."""
        ...
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of Path 3D."""
        ...
class FBModelPlane(FBModel):
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of Plane."""
        ...
class FBModelRoot(FBModel):
    Size:float
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of root."""
        ...
class FBModelSkeleton(FBModel):
    Color:FBColor
    Length:float
    LinkFollowGeometryOffset:bool
    Look:FBSkeletonLook
    PreserveLinkEndPosition:bool
    Resolution:FBSkeletonResolutionLevel
    Size:float
    def GetSkinModelList(self,SkinModelList:FBModelList):
        """Return the list of skin model associated with this Skeleton(Bone), which could be the deformable skins connected via cluster, or non deformable skins which are parented directly under this bone.
        ### Parameters:
        - SkinModelList: List to be appended with skin models (with no duplicated items)."""
        ...
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of skeleton."""
        ...
class FBPhysicalProperties(FBBox):
    def __init__(self,arg2:str=None):...
class FBAudioIn(FBComponent):
    def GetDelay(self)->FBTime:
        """Returns the delay currently set.
        (Windows only).
        ### Returns:
        The delay currently set."""
        ...
    def GetDestination(self)->FBAudioOut:
        """Returns the Audio Out object currently used as the destination.
        (Windows only).
        ### Returns:
        The Audio Out object currently used as the destination. Returns a NULL pointer (None in Python) if any Audio Out object is currently set."""
        ...
    def GetRecordingFormat(self)->int:
        """Returns the recording format (i.e.
        Bit Depth, Rate and Channel(s)) currently set.
        ### Returns:
        The audio format currently set for recording."""
        ...
    def GetSupportedFormats(self)->int:
        """Returns all the Audio In supported formats (i.e.
        Bit Depths, Rates and Channels).
        ### Returns:
        The Audio In supported formats."""
        ...
    def IsOnline(self)->bool:
        """Is the Audio In online?
        ### Returns:
        True if the Audio In is online, false if it is offline."""
        ...
    def IsReadyToRecord(self)->bool:
        """Is the Audio In ready to record (has it been prepared properly)?
        ### Returns:
        True if the audio is ready to record, false otherwise."""
        ...
    def PrepareToRecord(self,RecordingPath:str,ExistingClipAction:FBExistingClipAction=FBExistingClipAction.kFBExistingClipAskUser,ExistingFileAction:FBExistingFileAction=FBExistingFileAction.kFBExistingFileAskUser)->bool:
        """Prepares the Audio In for recording (similar as checking the "Record" checkbox in the UI).
        If the Audio In is not already online, it will turn it online automatically. If the Audio In is already ready to record, it will turn it off first automatically.
        ### Parameters:
        - RecordingPath: The file path for the desired output wav file. The file must have the .wav extension.
        - ExistingClipAction: The action to perform when the action clip associated to the recording path is already in the scene.
        - ExistingFileAction: The action to perform when the file associated to the recording path already exists on disk and it not empty.
        
        ### Returns:
        True if operation is successful, false otherwise. It could fail for different reasons (e.g. the specified file is not a WAV file or is invalid, the operation is abort by the user, etc.)."""
        ...
    def SetDelay(self,Delay:FBTime)->bool:
        """Sets the delay to use.
        The Audio In must be offline when this method is called. (Windows only).
        ### Parameters:
        - Delay: The delay to use. To mimic the UI, the FBTime should refer to a frame number.
        
        ### Returns:
        True if operation is successful, false otherwise."""
        ...
    def SetDestination(self,AudioOut:FBAudioOut)->bool:
        """Sets the Audio Out object to be used as the destination.
        The Audio In must be offline when this method is called. (Windows only).
        ### Parameters:
        - AudioOut: The Audio Out object to be used as the destination. Use a NULL pointer (None in Python) to unset the destination.
        
        ### Returns:
        True if operation is successful, false otherwise."""
        ...
    def SetOnline(self,bOnline:bool)->bool:
        """Turns Audio In online or offline.
        ### Parameters:
        - bOnline: True to turn the Audio In online, false to turn it offline.
        
        ### Returns:
        True if operation is successful, false otherwise."""
        ...
    def SetRecordingFormat(self,AudioFormat)->bool:
        """Sets the recording format (i.e.
        Bit Depth, Rate and Channel(s)) to use. The Audio In must be offline when this method is called.
        ### Parameters:
        - AudioFormat: The audio format to use for recording. It must specify a unique Bit Depth, Rate and Channels.
        
        ### Returns:
        True if operation is successful, false otherwise. It could fail for different reasons (e.g. the specified audio format is not supported, more than one Bit Depth is specified, etc.)."""
        ...
    def TurnOffRecording(self)->bool:
        """Turns off the Audio In recording (similar as un-checking the "Record" checkbox in the UI).
        ### Returns:
        True if operation is successful, false otherwise."""
        ...
    def __init__(self):...
class FBAudioClip(FBComponent):
    AccessMode:FBAccessMode
    Bits:int
    Channels:int
    ClipSpeed:float
    ConstrainDstToTake:bool
    CurrentTake:FBTake
    Destination:FBAudioOut
    DstDuration:FBTime
    DstEnd:FBTime
    DstIn:FBTime
    Duration:FBTime
    EndPoint:FBTime
    Filename:str
    Format:int
    InPoint:FBTime
    LockClipSpeed:bool
    LockPitchToSpeed:bool
    Path:str
    Pitch:float
    Rate:int
    RelativePath:str
    Scrubbing:bool
    SrcDuration:FBTime
    SrcEnd:FBTime
    SrcIn:FBTime
    TakeSetsInPoint:bool
    UseChannel:FBUseChnMode
    UseChannelMode:FBUseChnMode
    def IsMediaReady(self)->bool:
        """Check if the audio clip constructed properly.
        ### Returns:
        true if the audio clip was constructed properly."""
        ...
    def Play(self,Style:FBTriggerStyle=FBTriggerStyle.kFBTriggerStyleContinue,Destination:FBAudioOut=None)->bool:
        """Play audio clip now.
        ### Parameters:
        - Style: How the audio clip should be triggered.
        - Destination: Where the audio clip should be played. If NULL, it will play on the default destination.
        
        ### Returns:
        Return true if the buffer for the audio clip was successfully allocated so that you can hear the sound."""
        ...
    def Stop(self,Destination:FBAudioOut=None):
        """Stop any playing triggered audio clip on a specified destination.
        ### Parameters:
        - Destination: Where the audio clip is playing. If NULL, the default destination will be used."""
        ...
    def __init__(self,FileName:str):
        """### Parameters:
        - FileName: The complete file path of the media file to access."""
        ...
class FBAssetMng(FBComponent):
    Description:str
    LastError:str
    MenuFlags:int
    def BrowseForFile(self)->FBAssetFile:
        """Let the user browse the asset database to select a file.
        ### Returns:
        A file object representing the file that was selected, or `None` if none."""
        ...
    def BrowseForFolder(self)->FBAssetFolder:
        """Let the user browse the asset database to select a folder.
        ### Returns:
        A FBAssetFolder* object representing the folder that was selected, or `None` if none."""
        ...
    def CheckAvailability(self)->bool:
        """Check if this manager can be used on the computer."""
        ...
    def CreateServerPath(self,ServerPath:str)->FBAssetFolder:
        """Create a folder path on the server side by adding each missing folders.
        ### Parameters:
        - ServerPath: The path to create on the server side.
        
        ### Returns:
        A FBAssetFolder* object representing the deepest folder of the path."""
        ...
    def FileIsManaged(self,Filename:str)->bool:
        """Is the specified local file managed (ie.
        also present in the database).
        ### Parameters:
        - Filename: Path to the file on the local disk.
        
        ### Returns:
        A boolean indicating if the file is managed or not."""
        ...
    def GetAssetFile(self,ServerFilename:str)->FBAssetFile:
        """Get a file object using it's server path.
        ### Parameters:
        - ServerFilename: Path to the file on the server.
        
        ### Returns:
        An FBAssetFile* object, or `None` if the file was not found."""
        ...
    def GetAssetFileFromLocalPath(self,LocalFilename:str)->FBAssetFile:
        """Get a file object using it's local path.
        ### Parameters:
        - LocalFilename: Path to the file on the local disk.
        
        ### Returns:
        An FBAssetFile* object, or `None` if the file was not found or no mapping could be done."""
        ...
    def GetAssetFolder(self,ServerPath:str)->FBAssetFolder:
        """Get a folder object using it's server path.
        ### Parameters:
        - ServerPath: Path the the folder on the server.
        
        ### Returns:
        An FBAssetFolder* object, or `None` if the folder was not found."""
        ...
    def GetAssetFolderFromLocalPath(self,LocalPath:str)->FBAssetFolder:
        """Get a folder object using it's local path.
        ### Parameters:
        - LocalPath: Path to the folder on the local disk.
        
        ### Returns:
        An FBAssetFolder* object, or `None` if the folder was not found or no mapping could be done."""
        ...
    def GetFileOptions(self)->int:
        """Get the file options (i.e.
        what to do when loading, saving or closing managed files).
        ### Returns:
        The options."""
        ...
    def Initialize(self)->bool:
        """Initialize the connection to the server.
        ### Returns:
        True if the connection was established, false otherwise."""
        ...
    def MapLocalPathToServerPath(self,LocalPath:str)->str:
        """Convert the local path to a server path by using managed paths mapping.
        ### Parameters:
        - LocalPath: Local path to be mapped.
        
        ### Returns:
        A string with the resulting server path, will be empty if the mapping fail."""
        ...
    def ShowSettings(self):
        """Display a dialog that let the user changes settings."""
        ...
    def WithinManagedPath(self,LocalPath:str)->bool:
        """Is the specified local path below a managed path.
        ### Parameters:
        - LocalPath: Local path to be checked.
        
        ### Returns:
        A boolean indicating if the path is within a managed path or not."""
        ...
class FBAssetItem(FBComponent):
    LastError:str
    def CheckIn(self,Comment:str="",bKeepCheckedOut:bool=False,bSilent:bool=False)->bool:
        """Checks in this item and all its children (if this is a folder item).
        ### Parameters:
        - Comment: Comment to be applied for the check in.
        - bKeepCheckedOut: Flag that indicates whether the item will be kept checked out.
        - bSilent: If bSilent is set to true, no dialog will be displayed by this method.
        
        ### Returns:
        A boolean indicating if the operation was successful."""
        ...
    def CheckOut(self,Comment:str="",bDontGetLocal:bool=False,bSilent:bool=False)->bool:
        """Checks out this item and it's childs (if this is a folder item) and makes them writeable on the local disk.
        ### Parameters:
        - Comment: Comment to be applied for the check out.
        - bDontGetLocal: Indicate if local copy should retrieved or not.
        - bSilent: If bSilent is set to true, no dialog will be displayed by this method.
        
        ### Returns:
        A boolean indicating if the operation was successful."""
        ...
    def GetLatest(self,bReplaceCheckedOut:bool=False,bSilent:bool=False)->bool:
        """Obtain the latest version of the item from the server.
        ### Parameters:
        - bReplaceCheckedOut: Whether to replace the checked out file or not.
        - bSilent: If bSilent is set to true, no dialog will be displayed by this method.
        
        ### Returns:
        A boolean indicating if the operation was successful."""
        ...
    def GetLocalPath(self)->str:
        """Get the path to this item on the local hard disk.
        ### Returns:
        The path as an FBString ."""
        ...
    def GetName(self)->str:
        """Get the name of this item (file name or folder name).
        ### Returns:
        The name of the item, as an FBString ."""
        ...
    def GetParent(self)->FBAssetFolder:
        """Get the parent folder of this item.
        ### Returns:
        An FBAssetFolder* if the parent was found, or `None` if this is the root item."""
        ...
    def GetServerPath(self)->str:
        """Get the path to this item on the database.
        ### Returns:
        The server path as an FBString ."""
        ...
    def ShowHistory(self):
        """Display a dialog with this item history."""
        ...
    def ShowProperties(self):
        """Display a dialog showing the properties of this item."""
        ...
    def UndoCheckOut(self,bReplaceLocalFile:bool=True,bSilent:bool=False)->bool:
        """Cancel the last check out operation.
        ### Parameters:
        - bReplaceLocalFile: Flag indicating if the local item(s) should be replaced by the server version.
        - bSilent: If bSilent is set to true, no dialog will be displayed by this method.
        
        ### Returns:
        A boolean indicating if the operation was successful."""
        ...
class FBApplication(FBComponent):
    CurrentActor:FBActor
    CurrentCharacter:FBCharacter
    FBXFileName:str
    OnFileExit:FBEvent
    OnFileMerge:FBEvent
    OnFileNew:FBEvent
    OnFileNewCompleted:FBEvent
    OnFileOpen:FBEvent
    OnFileOpenCompleted:FBEvent
    OnFileSave:FBEvent
    OnFileSaveCompleted:FBEvent
    OnOverrideFileOpen:FBEventOverrideFileOpen
    def AudioRender(self,AudioRenderOptions:FBAudioRenderOptions=None)->bool:
        """Render audio of current scene to media file, currently WAV file only.
        ### Parameters:
        - AudioRenderOptions: The options used when rendering audio of the scene. Default value: 2 channels, 16 bits, 44100 hz, the begin and end time span for current time referential, Default file name is "Output.wav" in the last audio output path, ro the default document path if the last path doesn't exist.
        
        ### Returns:
        True if the file was rendered successfully
        
        ### Warning:
        If the destination media file exist, it will be overwritten by default. If the destination media file is opened by other application, the audio render process may not success because of not able to open it."""
        ...
    def ExecuteScript(self,Filename:str)->bool:
        """Execute a python script file.
        ### Parameters:
        - Filename: The script file to execute.
        
        ### Returns:
        True if the script file was found and executed.
        
        ### Remarks:
        This function can only be used in the UI thread."""
        ...
    def FileAppend(self,Filename:str,bShowUIMsg:bool=False,Options:FBFbxOptions=None)->bool:
        """Append one or multiple files to the current scene.
        Same as File->Merge in the menus with all options set to append. In earlier versions of MotionBuilder, a namespace could be specified with a parameter in this function, or FBFbxOptions::CustomImportNamespace, Now this is now done with FBFbxOptions::NamespaceList .
        ### Parameters:
        - Filename: File(s) to merge. For multiple files, use a list of files separated by '~'.
        - bShowUIMsg: Set false if don't want to popup any UI dialog or messages (default=false).
        - Options: Provide finer control on file open options (default=NULL). if not null, Option dialog will only show if both option's ShowOptionsDialog property and bShowUIMsg are true. It is possible to append multiple scenes, each one within its own user specified namespace, by calling the FBFbxOptions::SetMultiLoadNamespaceList method first. When doing so though, the FBFbxOption.NamespaceList property is then ignored.
        
        ### Returns:
        true if successful."""
        ...
    def FileBatch(self,BatchOptions:FBBatchOptions,PlotOptions:FBPlotOptions=None)->FBBatchStatus:
        """Start a batch.
        Command File->Batch... in the menus.
        ### Parameters:
        - BatchOptions: The options for the batch process (same as in the batch UI).
        - PlotOptions: The options for plotting (same as in the plot UI)(default=NULL).
        
        ### Returns:
        The status of the operation."""
        ...
    def FileExit(self,bSave:bool=False,ExitCode:int=0):
        """Quit application.
        Command File->Exit in the menus.
        ### Parameters:
        - bSave: true if file is saved on exit(default=false).
        - ExitCode: Exit code of the application(default=0)."""
        ...
    def FileExport(self,Filename:str)->bool:
        """Export a motion file.
        Command File->Motion File Export... in the menus.
        ### Parameters:
        - Filename: The file to create. To create two files at the same time (ex: .amc & .asf), separate the two files path with a comma ("Path1,Path2").
        
        ### Returns:
        True if the export succeeded.
        
        ### Remarks:
        If the file exists, it will be overwritten.
        current take is use.
        The last parameter is only used for motion files.
        For now, you cannot export custom file types.
        Currently, only the default export options are used.
        
        ### Warning:
        The signature of this function might change in the future to support export options."""
        ...
    def FileExportBatch(self,Name:str,Take:FBTake,BatchOptions:FBBatchOptions,ExportModels:FBModelList)->bool:
        """Export a motion file using batch options.
        Export used for saving files in batch process.
        ### Parameters:
        - Name: The name of the file without extension. Extension and path will be taken from batch options.
        - Take: Animation take to the export.
        - BatchOptions: The options for the export.
        - ExportModels: Models to the export.
        
        ### Returns:
        True if the export succeeded.
        
        ### Remarks:
        Not all options have to be set, only those that belong to process."""
        ...
    def FileImport(self,Filename:str,bMatchModels:bool=False,bCreateUnmatchedModels:bool=True)->bool:
        """Import a motion file.
        Command File->Motion File Import... in the menus.
        ### Parameters:
        - Filename: The file to import. To import two files at the same time (ex: .amc & .asf), separate the two files path with a comma ("Path1,Path2").
        - bMatchModels: If there is already a model in the scene with the same name, the model will not be created and we replace the animation of the given model.
        - bCreateUnmatchedModels: Whether unmatched models will be created. This flag matters only when bMatchModels is true. when bMatchModels is false, all the models are created.
        
        ### Returns:
        True if the import succeeded.
        
        ### Remarks:
        No models selected, all the models in the scene will be checked for a potential name match.
        If there are models selected in the scene, only these models will be checked for a potential name match.
        If only one model is selected (ex: hips), this models and its hierarchy will be used.
        The data will be imported in the current take.
        The last two parameter are only used for motion files.
        For now, you cannot import custom file types.
        Currently, only the default import options are used.
        
        ### Warning:
        The signature of this function might change in the future to support import options."""
        ...
    def FileImportBatch(self,Name:str,BatchOptions:FBBatchOptions,Reference:FBModel)->bool:
        """Import a motion file using batch options.
        Import used for loading files in batch process.
        ### Parameters:
        - Name: The name of the file without extension. Extension and path will be taken from batch options.
        - BatchOptions: The options for the import.
        - Reference: Reference model for the import.
        
        ### Returns:
        True if the import succeeded.
        
        ### Remarks:
        Not all options have to be set, only those that belong to process."""
        ...
    def FileImportWithOptions(self,Options:FBMotionFileOptions)->bool:
        """Import a motion file with the ability to specify options.
        Command File->Motion File Import... in the menus.
        ### Parameters:
        - Options: A FBMotionFileOptions object that contains the path to the files, as well as the options to load those motion files.
        
        ### Returns:
        True if the import succeeded.
        
        ### Remarks:
        The import will only work if you open files of the same type.
        For now, you cannot import custom file types.
        Not all options can be applied to a particular motion file type, please use the Motion File Import UI as a reference."""
        ...
    @overload
    def FileMerge(self,Pathlist:str,bShowUIMsg:bool=False,Options:FBFbxOptions=None)->bool:
        """Merge multiple files with the current scene.
        Command File->Merge in the menus.
        ### Parameters:
        - Pathlist: Files to merge.
        - bShowUIMsg: Set false if don't want to popup any UI dialog or messages (default=false).
        - Options: Provide finer control on file open options (default=NULL). if not null, Option dialog will only show if both option's ShowOptionsDialog property and bShowUIMsg are true. It is possible to merge multiple scenes, each one within its own user specified namespace, by calling the FBFbxOptions::SetMultiLoadNamespaceList method first. When doing so though, the FBFbxOption.NamespaceList property is then ignored.
        
        ### Returns:
        true if successful."""
        ...
    @overload
    def FileMerge(self,Filename:FBStringList,bShowUIMsg:bool=False,Options:FBFbxOptions=None)->bool:
        """Merge one or multiple files with the current scene.
        Command File->Merge in the menus.
        ### Parameters:
        - Filename: File(s) to merge. For multiple files, use a list of files separated by '~'.
        - bShowUIMsg: Set false if don't want to popup any UI dialog or messages (default=false).
        - Options: Provide finer control on file open options (default=NULL). if not null, Option dialog will only show if both option's ShowOptionsDialog property and bShowUIMsg are true. It is possible to merge multiple scenes, each one within its own user specified namespace, by calling the FBFbxOptions::SetMultiLoadNamespaceList method first. When doing so though, the FBFbxOption.NamespaceList property is then ignored.
        
        ### Returns:
        true if successful."""
        ...
    def FileNew(self,bAskUser:bool=False,bClearSceneName:bool=True)->bool:
        """Command File->New in the menus.
        ### Parameters:
        - bAskUser: Set to true to cause a save dialog to popup. Default is false.
        - bClearSceneName: Set to true to clear the scene name, set to false to retain it. Default is true.
        
        ### Returns:
        true if successful."""
        ...
    @overload
    def FileOpen(self,Filename:str,bShowUIMsg:bool=False,Options:FBFbxOptions=None)->bool:
        """Open a file, replacing the current scene.
        Command File->Open in the menus.
        ### Parameters:
        - Filename: File to open.
        - bShowUIMsg: Set false if don't want to popup any UI dialog or messages (default=false).
        - Options: Provide finer control on file open options (default=NULL). if not null, Option dialog will only show if both option's ShowOptionsDialog property and bShowUIMsg are true.
        
        ### Returns:
        true if file open successfully."""
        ...
    @overload
    def FileOpen(self,Buffer:None,BufferLength:int)->bool:
        """Open a file from memory.
        ### Warning:
        this is advanced & not supported function, use with caution.
        
        ### Parameters:
        - Buffer: the memory buffer for the file. Raw memory address is expected in pyfbsdk.
        - BufferLength: the memory buffer size.
        
        ### Returns:
        true if file opened successfully."""
        ...
    def FileRender(self,RenderOptions:FBVideoGrabOptions=None)->bool:
        """Render current scene to media file.
        Command File->Render in the menus.
        ### Parameters:
        - RenderOptions: The options used when rendering the scene. If you don't specify them, current one are used.
        
        ### Returns:
        True if the file was rendered successfully otherwise False and FBVideoGrabber.GetLastErrorMsg() contains the description of the error.
        
        ### Remarks:
        Render options can be changed if they are not valid.
        
        ### Warning:
        If the destination media file exist, it will be overwritten by default."""
        ...
    def FileSave(self,Filename:str=None,Options:FBFbxOptions=None)->bool:
        """Save the file under another name.
        Command File->SaveAs in the menus.
        ### Parameters:
        - Filename: Save file as Filename . A value of `None` will use the current file name.
        - Options: Provide finer control on file save options (default=NULL)
        
        ### Returns:
        true if successful."""
        ...
    def FlushEventQueue(self):
        """Flush event queue.
        Processes all pending events for the calling thread until there are no more events to process. You can call this function occasionally when your code is busy performing a long operation (e.g. copying a file)."""
        ...
    def GetMaxFrameCount(self,Buffer:None,BufferLength:int,FrameCount:int)->bool:
        """Get max frame count from a scene file in memory.
        ### Warning:
        this is advanced & not supported function, use with caution.
        
        ### Parameters:
        - Buffer: the memory buffer for the file. Raw memory address is expected in pyfbsdk.
        - BufferLength: the memory buffer size.
        - FrameCount: out parameter to hold max frame count. this parameter is not needed in pyfbsdk.
        ### Returns:
        true if file opened successfully. In pyfbsdk, a tuple (bool, kLong) will return instead, the first one is ORSDK function return value, the second is for max frame count."""
        ...
    def GetSceneAuthor(self)->str:
        """Return the scene author from the scene properties."""
        ...
    def GetSceneComment(self)->str:
        """Return the scene comment from the scene properties."""
        ...
    def GetSceneKeywords(self)->str:
        """Return the scene keywords from the scene properties."""
        ...
    def GetSceneRevisionNumber(self)->str:
        """Return the scene revision number from the scene properties."""
        ...
    def GetSceneSubject(self)->str:
        """Return the scene subject from the scene properties."""
        ...
    def GetSceneTitle(self)->str:
        """Return the scene title from the scene properties."""
        ...
    def IsSceneModified(self)->bool:
        """Is the scene modified since last save / new scene creation?
        ### Returns:
        True if the scene is modified since last save / new scene creation, false otherwise."""
        ...
    def IsValidBatchFile(self,Filename:str)->bool:
        """Verify motion file readability.
        ### Parameters:
        - Filename: The file to test.
        
        ### Returns:
        True if file was opened successfully (file is closed at the end)."""
        ...
    def LoadAnimationOnCharacter(self,FileName:str,Character:FBCharacter,FbxOptions:FBFbxOptions,PlotOptions:FBPlotOptions)->bool:
        """Load a rig and its animation from a file.
        ### Parameters:
        - FileName: File name.
        - Character: Target character.
        - FbxOptions: The options for the character rig and animation load
        - PlotOptions: If the animation should be plotted on the target rig, these plot options will be used. Set to `None` if animation will not be plotted.
        
        ### Returns:
        true if successful."""
        ...
    def Maximize(self)->bool:
        """Maximize window (minimized).
        ### Returns:
        Operation was successful (true or false)."""
        ...
    def Minimize(self,bBlocking:bool=True)->bool:
        """Minimize window.
        ### Parameters:
        - bBlocking: Is the minimization blocking operation (default = true).
        
        ### Returns:
        Operation was successful (true or false)."""
        ...
    def OneClickAddToCurrentScene(self)->bool:
        """Send the scene and add it to the current scene in the specified application.
        ### Returns:
        True if transfer successful."""
        ...
    def OneClickIsConnectedTo(self)->FBOneClickApplication:
        """Return the other application that MotionBuilder is connected to.
        ### Returns:
        The application that MotionBuilder is connected to."""
        ...
    def OneClickSelectPreviouslySentObject(self):
        """Select, in MotionBuilder, the object that were sent."""
        ...
    def OneClickSendAsNewScene(self,Application:FBOneClickApplication)->bool:
        """Send the current scene as a new scene in the specified application.
        ### Parameters:
        - Application: The application that will receive the scene.
        
        ### Returns:
        True if transfer successful."""
        ...
    def OneClickUpdateCurrentScene(self)->bool:
        """Send the scene to update the current scene in the specified application.
        ### Returns:
        True if transfer successful."""
        ...
    def SaveCharacterRigAndAnimation(self,FileName:str,Character:FBCharacter,FbxOptions:FBFbxOptions)->bool:
        """Save the rig and its animation in a file.
        ### Parameters:
        - FileName: File name.
        - Character: Character to save.
        - FbxOptions: The options for the character rig and animation export
        
        ### Warning:
        After save, the current scene selection will be reset."""
        ...
    def SetSceneAuthor(self,Author:str):
        """Set the scene author.
        ### Parameters:
        - Author: The author to set in the scene properties."""
        ...
    def SetSceneComment(self,Comment:str):
        """Set the scene comment.
        ### Parameters:
        - Comment: The comment to set in the scene properties."""
        ...
    def SetSceneKeywords(self,Keywords:str):
        """Set the scene keywords.
        ### Parameters:
        - Keywords: The keywords to set in the scene properties."""
        ...
    def SetSceneRevisionNumber(self,RevNumber:str):
        """Set the scene revision number.
        ### Parameters:
        - RevNumber: The revision number to set in the scene properties."""
        ...
    def SetSceneSubject(self,Subject:str):
        """Set the scene subject.
        ### Parameters:
        - Subject: The subject to set in the scene properties."""
        ...
    def SetSceneTitle(self,Title:str):
        """Set the scene title.
        ### Parameters:
        - Title: The title to set in the scene properties."""
        ...
    def UpdateAllWidgets(self):
        """Request to refresh display of all UI widgets."""
        ...
    def __init__(self):...
class FBAssetFile(FBAssetItem):
    def GetCheckedOutBy(self)->str:
        """Returns the name of the user who currently has this file checked out.
        ### Returns:
        The user name if the file is checked out, or an empty string if it is not."""
        ...
    def IsCheckedOut(self)->bool:
        """Returns a boolean value indicating if this file is checked out by any user.
        ### Returns:
        A boolean value indicating if this node is checked out."""
        ...
    def IsCheckedOutByMe(self)->bool:
        """Returns a boolean value indicating if this file is checked out by the current user.
        ### Returns:
        A boolean value indicating if this node is checked out by the current user."""
        ...
class FBAssetFolder(FBAssetItem):
    def AddFile(self,LocalPath:str,Comment:str,bCheckOut:bool,bSilent:bool)->FBAssetFile:
        """Add a specified file into the database.
        It will be added in this folder.
        ### Parameters:
        - LocalPath: The full path to the file on the local disk.
        - Comment: Comment to be applied for the operation.
        - bCheckOut: Whether the file should be checked out or not.
        - bSilent: If bSilent is set to true, no dialog will be displayed by this method.
        
        ### Returns:
        An FBAssetfile* object representing the newly added file."""
        ...
    def AddFolder(self,Name:str,Comment:str,bSilent:bool)->FBAssetFolder:
        """Add a folder in the database.
        It will be added in this folder.
        ### Parameters:
        - Name: Name of the folder to be created.
        - Comment: Comment to be applied for the operation.
        - bSilent: If bSilent is set to true, no dialog will be displayed by this method.
        
        ### Returns:
        An FBAssetFolder* object representing the newly added folder."""
        ...
    def GetChild(self,Index:int)->FBAssetItem:
        """Get the child at index Index .
        ### Returns:
        The child at Index , or `None` if the index was out of range."""
        ...
    def GetChildCount(self)->int:
        """Get the number of items in this folder.
        ### Returns:
        The number of items in this folder."""
        ...
    def GetFile(self,Name:str)->FBAssetFile:
        """Get a file present in this folder by using it's name.
        ### Returns:
        The file with the given name, or `None` if it was not found."""
        ...
    def GetFolder(self,Name:str)->FBAssetFolder:
        """Get a folder present in this folder by using it's name.
        ### Returns:
        The folder with the given name, or `None` if it was not found."""
        ...
class FBAnimationNode(FBComponent):
    ConnectorType:property
    DefaultInterpolation:property
    FCurve:property
    KeyCount:property
    Label:property
    Live:property
    Nodes:property
    RecordMode:property
    UserName:property
    def ConvertGlobalToNodeTime(self,arg2:FBTime)->FBTime:...
    def ConvertNodeToGlobalTime(self,arg2:FBTime)->FBTime:...
    def GetAnimationToPlay(self)->object:...
    def GetAnimationToRecord(self)->object:...
    def GetDataDoubleArrayCount(self)->int:...
    def GetSizeOfData(self)->int:...
    def IsKey(self)->bool:...
    @overload
    def KeyAdd(self,arg2:FBTime,arg3,arg4:FBInterpolation=None,arg5:FBTangentMode=None):...
    @overload
    def KeyAdd(self,arg2,arg3:FBInterpolation=None,arg4:FBTangentMode=None):...
    @overload
    def KeyAdd(self,arg2:FBTime,arg3:list,arg4:FBInterpolation=None,arg5:FBTangentMode=None):...
    @overload
    def KeyAdd(self,arg2:list,arg3:FBInterpolation=None,arg4:FBTangentMode=None):...
    def KeyCandidate(self,arg2:FBTime=None):...
    def KeyRemove(self):...
    def KeyRemoveAt(self,arg2:FBTime):...
    @overload
    def ReadData(self,arg2:FBEvaluateInfo=None,arg3=None)->list:...
    @overload
    def ReadData(self,arg2:FBTime,arg3=None)->list:...
    def ReadLastEvalData(self)->list:...
    def SetBufferType(self,arg2):...
    def SetCandidate(self,arg2:list,arg3=None)->bool:...
    def WriteData(self,arg2:list,arg3:FBEvaluateInfo=None)->int:...
    def __init__(self,arg2:str):...
class FBAnimationLayer(FBComponent):
    LayerMode:FBLayerMode
    LayerRotationMode:FBLayerRotationMode
    Lock:bool
    Mute:bool
    Solo:bool
    Weight:float
    def AddChildLayer(self,AnimationLayer:FBAnimationLayer):
        """Add a child to the layer.
        Layer ID of the new child layer might change after parenting depending where the child layer was originally located.
        ### Parameters:
        - AnimationLayer: Layer to set as a child."""
        ...
    def GetChildCount(self)->int:
        """Get the child layer count of this layer.
        The count will only includes direct child of the layer.
        ### Returns:
        Child layer count, or -1 if unsuccessful"""
        ...
    def GetChildLayer(self,Index:int)->FBAnimationLayer:
        """Get the nth child layer of this layer.
        ### Parameters:
        - Index: Index of the child layer to get.
        
        ### Returns:
        Child animation layer located at Index"""
        ...
    def GetCompleteChildHierarchy(self,ChildArray:FBComponent)->list:
        """Get the all the children hierarchy of the layer, including children not directly connected to this layer.
        ### Python:
        The function takes no parameter and returns a Python list. ex : lArray = lAnimationLayer.GetCompleteChildHierarchy()
        
        ### Parameters:
        - ChildArray: Array of child layers, will be filled by the function."""
        ...
    def GetLayerIndex(self)->int:
        """Get the layer index.
        ### Returns:
        The layer index in the current layer hierarchy. This value will change if the hierarchy is modified. Return -1 if unsuccessful."""
        ...
    def GetParentLayer(self)->FBAnimationLayer:
        """Get the parent layer.
        ### Returns:
        A pointer to the parent layer or `None` if the layer doesn't have a parent."""
        ...
    def IsSelected(self)->bool:
        """Verify if the layer is selected.
        ### Returns:
        True if the layer is selected, false otherwise."""
        ...
    def SelectLayer(self,bValue:bool,bExclusiveSelect:bool):
        """Select the layer.
        This is the equivalent of selecting the layer in the UI in the Animation Layer Editor tool
        ### Parameters:
        - bValue: True if the layer will be selected, false otherwise.
        - bExclusiveSelect: If bValue is true, passing true will deselect all the other layers, creating an exclusive selection, it will also set the layer as the current layer."""
        ...
    def SetParentLayer(self,ParentLayer:FBAnimationLayer):
        """Set the parent layer.
        ### Parameters:
        - ParentLayer: A pointer to the parent layer or `None` if you want to unparent the layer."""
        ...
    def __init__(self,Name:str,LayerID:int):
        """### Parameters:
        - Name: Name of the animation layer.
        - LayerID: ID to set for the new layer."""
        ...
class FBActorFace(FBComponent):
    def PlotAnimation(self)->bool:
        """Plot the animation of the actor face.
        ### Returns:
        True if the operation completed successfully."""
        ...
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of new actor face."""
        ...
class FBActionManager(FBComponent):
    CurrentInteractionMode:property
    def __init__(self):...
class FBConstraintManager(FBComponent):
    @overload
    def TypeCreateConstraint(self,TypeIndex:int)->FBConstraint:
        """Create a constraint by index.
        Given the index in the registry, this function create an instance of this constraint. The newly created constraint will be automatically added to the scene.
        ### Parameters:
        - TypeIndex: Index of constraint type, must in range [0, TypeGetCount() ).
        
        ### Returns:
        The newly created constraint, or `None` if pIndex is out of range."""
        ...
    @overload
    def TypeCreateConstraint(self,Name:str)->FBConstraint:
        """Create a constraint by name.
        Given the constraint type name in the registry, this function create an instance of this constraint. The newly created constraint will be automatically added to the scene.
        ### Parameters:
        - Name: the name of the constraint to be created.
        
        ### Returns:
        The newly created constraint, or `None` if Name doesn't match any registered constraints."""
        ...
    def TypeGetCount(self)->int:
        """Get the number of registered constraint types.
        ### Returns:
        Number of registered constraint types."""
        ...
    def TypeGetName(self,TypeIndex:int)->str:
        """Get the name of a registered type of constraint.
        This will search in the registry for a constraint at the index TypeIndex .
        ### Parameters:
        - TypeIndex: Index of a constraint type.
        
        ### Returns:
        Name of constraint type."""
        ...
    def __init__(self):...
class FBConstructionHistory(FBComponent):
    OnChange:FBEvent
    def GetDeltaOperations(self,Operations:list,sinceCommandId:int):
        """GetDeltaOperations Get the list of delta operations in the construction history.
        ### Parameters:
        - sinceCommandId: 
        - Operations: Array of operations, will be filled by the function."""
        ...
    def GetScriptOutput(self,script:list,errors:list):
        """GetScriptOutput Returns the output from the scripting engine.
        ### Parameters:
        - script: the script text
        - errors: the error outputted from the scripting engine"""
        ...
    def GetState(self)->FBConstructionHistoryState:
        """GetState returns the current state of the construction history manager.
        ### Returns:
        returns a FBConstructionHistoryState indicating the state"""
        ...
    def NetDelete(self,component:FBComponent,key:int):
        """NetDelete Network delete with support for Network Undo.
        ### Parameters:
        - component: 
        - key: A key that uniquely identifies the operation"""
        ...
    def NetUndo(self,key:int):
        """NetUndo Perform network undo operation.
        ### Parameters:
        - key: The operation to undo"""
        ...
    def RunOperation(self,operation:FBConstructionOperation,out_errors:list)->int:
        """RunOperation Runs an operation.
        ### Parameters:
        - operation: The operation to run
        - out_errors: A string containing the text of errors generated by running the operations (if any)"""
        ...
class FBControlSet(FBComponent):
    ControlSetType:FBControlSetType
    UseAxis:bool
    def GetFKIndex(self,Model:FBModel)->int:
        """Return The Index of the Given Model.
        ### Parameters:
        - Model: Given Model to obtain Index
        
        ### Returns:
        The Index of the Given Model."""
        ...
    def GetFKModel(self,Index:FBBodyNodeId)->FBModel:
        """Return the object associated to the given Index.
        ### Parameters:
        - Index: Given Index to obtain Model
        
        ### Returns:
        return the model at the specified Index."""
        ...
    def GetFKName(self,Index:FBBodyNodeId)->str:
        """return the name of FK Effector at the given index
        ### Parameters:
        - Index: Given Index
        
        ### Returns:
        return the name of IK Effector Slot"""
        ...
    def GetIKEffectorIndex(self,Model:FBModel)->int:
        """Return the Index of the Given Model.
        ### Parameters:
        - Model: Given Model to Obtain Index
        
        ### Returns:
        The Index of the Given Model."""
        ...
    def GetIKEffectorModel(self,EffectorIndex:FBEffectorId,PivotIndex:int)->FBModel:
        """Return the object associated to the given Index.
        ### Parameters:
        - EffectorIndex: Given Index to obtain Model
        - PivotIndex: Index of effector pivot
        
        ### Returns:
        return the model at the specified Index."""
        ...
    def GetIKEffectorName(self,EffectorIndex:FBEffectorId)->str:
        """return the name of IK Effector
        ### Parameters:
        - EffectorIndex: Given Index to obtain Name
        
        ### Returns:
        the name of IK Effector"""
        ...
    def GetIKEffectorPivotCount(self,EffectorIndex:FBEffectorId)->int:
        """return the number of IK Effector Slot
        ### Returns:
        return the number of IK Effector Slot"""
        ...
    def GetReferenceModel(self)->FBModel:
        """Get the reference model associated with this Control Set.
        ### Returns:
        The reference model associated with the Control Set."""
        ...
    def GetReferenceName(self)->str:
        """Get the reference name associated with this Control Set.
        ### Returns:
        The reference name associated with the Control Set."""
        ...
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of new control set."""
        ...
class FBCycleCreator(FBComponent):
    def CreateCycle(self,arg2:FBTime,arg3:FBTime,arg4:FBCharacter=None,arg5=None,arg6=None,arg7:str=None,arg8:FBModel=None,arg9=None,arg10=None,arg11=None,arg12=None,arg13=None)->bool:...
    def __init__(self):...
class FBDeck(FBComponent):
    CassetteInside:bool
    EE:bool
    IconFilename:str
    Latency:FBTime
    Offset:FBTime
    Online:bool
    PlayingBackward:bool
    PlayingForward:bool
    PostRoll:FBTime
    PreRoll:FBTime
    StandBy:bool
    TransportControl:FBDeckTransportMode
    UniqueName:str
    def CueAt(self,Time:FBTime):
        """Cue deck at a given time.
        ### Parameters:
        - Time: Time to cue deck at."""
        ...
    def DeckAutoCommandsNotify(self):
        """Deck auto commands notification."""
        ...
    def DeckStatusUpdateNotify(self):
        """Interface to IObject.
        Deck status update notification."""
        ...
    def Eject(self):
        """Eject tape."""
        ...
    def Forward(self):
        """Fast forward."""
        ...
    def GetTime(self)->FBTime:
        """Get the deck's time.
        ### Returns:
        Time of deck."""
        ...
    def Play(self,Speed:float=1.0):
        """Play forwards.
        ### Parameters:
        - Speed: Playback speed (default is 1.0)."""
        ...
    def ReversePlay(self,Speed:float=1.0):
        """Play backwards.
        ### Parameters:
        - Speed: Playback speed(default is 1.0)."""
        ...
    def Rewind(self):...
    def StepBack(self):
        """Step backwards."""
        ...
    def StepForward(self):
        """Step forwards."""
        ...
    def Stop(self):...
    def ThreadSync(self):...
class FBDeformer(FBComponent):
    DeformerType:FBDeformerType
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of deformer."""
        ...
class FBDeviceInstrument(FBComponent):
    Active:bool
    Device:FBDevice
    ModelTemplate:FBModelTemplate
    def InstrumentRecordFrame(self,RecordTime:FBTime,NotifyInfo:FBDeviceNotifyInfo):
        """Record the data to the function curves for the instrument.
        ### Parameters:
        - RecordTime: Time to record data at.
        - NotifyInfo: Device notification information structure."""
        ...
    def InstrumentWriteData(self,EvaluateInfo:FBEvaluateInfo)->bool:
        """Write data to instrument's connectors.
        In the evaluation engine callback, this will take the data in the instrument's temporary data holders and write it to the connectors.
        ### Parameters:
        - EvaluateInfo: Evaluation information structure.
        
        ### Returns:
        true if successful.
        Reimplemented in FBDeviceCameraInstrument ."""
        ...
    def __init__(self,Device:FBDevice):
        """### Parameters:
        - Device: Parent device."""
        ...
class FBDeformerPointCache(FBDeformer):
    Active:bool
    ChannelCount:int
    ChannelEnd:FBTime
    ChannelFrameRate:float
    ChannelIndex:int
    ChannelName:str
    ChannelPointCount:int
    ChannelSampleRegular:bool
    ChannelStart:FBTime
    PointCacheFile:FBPointCacheFile
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of deformer."""
        ...
class FBDeviceOpticalMarker(FBComponent):
    IsUsed:bool
    Model:FBModel
    Occlusion:float
    Translation:property
    def SetData(self,X:float,Y:float,Z:float=0.0,Occlusion:float=0.0):
        """Set data for optical marker.
        ### Parameters:
        - X: X position for marker.
        - Y: Y position for marker.
        - Z: Z position for marker(default=0.0).
        - Occlusion: Occulsion information for marker(default=0.0)."""
        ...
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of optical marker."""
        ...
class FBEvaluateManager(FBComponent):
    DeviceCount:property
    DualQuaternionSkinning:property
    FrameSkipOptimization:property
    NodeCount:property
    OnRenderingPipelineEvent:property
    OnSynchronizationEvent:property
    ParallelDeformation:property
    ParallelEvaluation:property
    ParallelPipeline:property
    ParallelScheduleType:property
    UseGPUDeformation:property
    def InvalidateDAG(self):...
    def IsInteractiveMode(self)->bool:...
    def __init__(self):...
class FBFCurveEditorUtility(FBComponent):
    def Frame(self,bSelectedKeysOnly:bool,Editor:FBFCurveEditor=None)->bool:
        """Frame keys in the FCurve Editor interface.
        ### Parameters:
        - bSelectedKeysOnly: If true, only the selected keys will be framed, otherwise all keys will be framed.
        - Editor: Pointer to a FBFCurveEditor for framing the keys in that custom editor, `None` to frame in the default editor.
        
        ### Note:
        Editor is currently not supported in this implementation, as the FBFCurveEditor is still in development.
        
        ### Returns:
        True if successful, false otherwise."""
        ...
    def GetObjects(self,ObjectList:list)->bool:
        """Get all the objects displayed in the left pane of the FCurve Editor.
        ### Parameters:
        - ObjectList: A list that will be filled with the objects displayed in the FCurve Editor.
        
        ### Returns:
        True if successful, false otherwise."""
        ...
    def GetProperties(self,Properties:list,bSelectedOnly:bool,Editor:FBFCurveEditor=None)->bool:
        """Get the displayed properties.
        ### Parameters:
        - pPropertyList: Array that will contain the properties displayed.
        - bSelectedOnly: If true, only the selected properties will be returned.
        - Editor: Pointer to a FBFCurveEditor for getting the properties in that custom editor, `None` to frame in the default editor.
        
        ### Returns:
        True if successful, false otherwise."""
        ...
    def GetTimeSpan(self,Editor:FBFCurveEditor=None)->FBTimeSpan:
        """Get the displayed time range of the FCurve Editor.
        ### Parameters:
        - Editor: Pointer to a FBFCurveEditor where the time span will be get, `None` to get the time span from the default editor.
        
        ### Returns:
        FCurve Editor time span, default FBTimeSpan if not successful."""
        ...
    def SetTimeSpan(self,TimeSpan:FBTimeSpan,Editor:FBFCurveEditor=None)->bool:
        """Set the displayed time range of the FCurve Editor.
        ### Parameters:
        - TimeSpan: The time span that will be set.
        - Editor: Pointer to a FBFCurveEditor where the time span will be set, `None` to set the time span on the default editor.
        
        ### Returns:
        True if successful, false otherwise."""
        ...
    def __init__(self):...
class FBFCurveEventManager(FBComponent):
    OnFCurveEvent:property
    OnPropertyEvent:property
    def RegisterProperty(self,Property:FBPropertyAnimatable)->bool:
        """Register a property to the FCurve Event Manager.
        Properties that are registered will receive events with the OnFCurveEvent/OnPropertyEvent properties when their FCurves are modified.
        ### Parameters:
        - Property: The property to track.
        
        ### Returns:
        True if the registration was successful, False otherwise."""
        ...
    def UnregisterProperty(self,Property:FBPropertyAnimatable)->bool:
        """Unregister a property from the FCurve Event Manager.
        Those properties will not be tracked and no update will be sent with the OnFCurveEvent/OnPropertyEvent properties anymore.
        ### Parameters:
        - Property: The property to stop tracking.
        
        ### Returns:
        True if the unregistration was successful, False otherwise."""
        ...
    def __init__(self):...
class FBFbxOptions(FBComponent):
    ActorFaces:FBElementAction
    ActorFacesAnimation:bool
    Actors:FBElementAction
    Audio:FBElementAction
    BaseCameras:bool
    Bones:FBElementAction
    BonesAnimation:bool
    CacheSize:int
    CameraSwitcherSettings:bool
    Cameras:FBElementAction
    CamerasAnimation:bool
    CharacterExtensions:FBElementAction
    CharacterFaces:FBElementAction
    CharacterFacesAnimation:bool
    Characters:FBElementAction
    CharactersAnimation:bool
    ClearSelectionBeforeSave:bool
    ConsiderMuteSolo:bool
    Constraints:FBElementAction
    ConstraintsAnimation:bool
    CopyCharacterExtensions:bool
    CurrentCameraSettings:bool
    Devices:FBElementAction
    DevicesAnimation:bool
    EmbedMedia:bool
    FileFormatAndVersion:FBFileFormatAndVersion
    FileReference:bool
    FileReferenceEdit:bool
    FileReferences:FBElementAction
    GlobalLightingSettings:bool
    Groups:FBElementAction
    IgnoreConflicts:bool
    KeepTransformHierarchy:bool
    KeyingGroups:FBElementAction
    Lights:FBElementAction
    LightsAnimation:bool
    Materials:FBElementAction
    MaterialsAnimation:bool
    Models:FBElementAction
    ModelsAnimation:bool
    NamespaceList:str
    Notes:FBElementAction
    NotesAnimation:bool
    OpticalData:FBElementAction
    PhysicalProperties:FBElementAction
    PhysicalPropertiesAnimation:bool
    Poses:FBElementAction
    ProcessAnimationOnExtension:bool
    RemoveConstraintReference:bool
    RemoveEmptyLayer:bool
    ReplaceControlSet:bool
    ResetDOF:bool
    ResetHierarchy:bool
    RetargetOnBaseLayer:bool
    SaveCharacter:bool
    SaveCharacterExtensions:bool
    SaveControlSet:bool
    SaveSelectedModelsOnly:bool
    Scripts:FBElementAction
    SetPropertyStaticIfPossible:bool
    Sets:FBElementAction
    Shaders:FBElementAction
    ShadersAnimation:bool
    ShowFileDialog:bool
    ShowOptionsDialog:bool
    Solvers:FBElementAction
    SolversAnimation:bool
    Story:FBElementAction
    StoryAnimation:bool
    TakeSpan:FBTakeSpanOnLoad
    Textures:FBElementAction
    TexturesAnimation:bool
    TransferMethod:FBCharacterLoadAnimationMethod
    TransportSettings:bool
    UpdateRecentFiles:bool
    UseASCIIFormat:bool
    Video:FBElementAction
    def GetMultiLoadNamespaceList(self)->FBStringList:
        """Returns the list of namespaces that will be used when merging multiple scenes (see FBApplication::FileMerge ).
        This list is affecting only the merge operation. When merging multiple scenes, if this list of namespaces is set, the FBFbxOptions::NamespaceList property value is ignored.
        ### Returns:
        The multi load namespace list currently set."""
        ...
    def GetTakeCount(self)->int:
        """Return the count of takes in the scene to saved or the file to loaded.
        ### Warning:
        You need to use appropriate constructor to be able to take infos."""
        ...
    def GetTakeDescription(self,TakeIndex:int)->str:
        """Take Description.
        ### Parameters:
        - TakeIndex: index of take to get."""
        ...
    def GetTakeDestinationName(self,TakeIndex:int)->str:
        """Take Destination Name upon save or load.
        ### Parameters:
        - TakeIndex: index of take to get."""
        ...
    def GetTakeKeyRange(self,TakeIndex:int)->FBTimeSpan:
        """Get take key range.
        ### Parameters:
        - TakeIndex: index of take to get.
        
        ### Returns:
        A time range, keys inside that time range will be kept. Keys outside that time range will be removed when importing the animation, by default the time range is FBTime::MinusInfinity -> FBTime::Infinity
        
        ### Remarks:
        Valid only on load/merge, not when saving a file."""
        ...
    def GetTakeName(self,TakeIndex:int)->str:
        """Take Original Name.
        ### Parameters:
        - TakeIndex: index of take to get."""
        ...
    def GetTakeSelect(self,TakeIndex:int)->bool:
        """Return if true if the take will be saved or Loaded.
        ### Parameters:
        - TakeIndex: index of take to get."""
        ...
    def SaveToString(self)->str:
        """Serialize all options to a string Serialize all options to a string specifying a context."""
        ...
    def SetAll(self,ElementAction:FBElementAction,bAnimation:bool):
        """Set All Options.
        Initialize all loading/saving properties to ElementAction and animation specified.
        ### Parameters:
        - ElementAction: Default value for all FBPropertyElementAction properties.
        - bAnimation: Default value for all Animation properties."""
        ...
    def SetFromString(self,String:str):
        """Set all options from string Set all parameters from a formatted string (previously serialized with SaveToString)
        ### Parameters:
        - String: The string containing all settings. See SaveToFile"""
        ...
    def SetMultiLoadNamespaceList(self,MultiLoadNamespaceList:FBStringList):
        """Sets the list of namespaces that will be used when merging multiple scenes (see FBApplication::FileMerge ).
        The number of namespaces contained in this list must match the number of files merged, otherwise the merge operation will abort. The first namespace in the list will be applied on the first merged scene, the second namespace in the list will be applied on the second merged scene, and so one and so forth. This list is affecting only the merge operation. When merging multiple scenes, if this list of namespaces is set, the FBFbxOptions::NamespaceList property value is ignored.
        ### Parameters:
        - MultiLoadNamespaceList: The multi load namespace list to set. # This example shows how to merge multiple scenes, each scene in its own user specified namespace:"""
        ...
    def SetObjectsToSave(self,ObjectsToSave:list):
        """Sets the list of objects that will be saved.
        This needs to be set before calling FBApplication::FileSave . The list is affecting only one save operation. Once the save is completed, the list is cleared.
        ### Parameters:
        - ObjectsToSave: The objects to save."""
        ...
    def SetTakeDescription(self,TakeIndex:int,Description:str):
        """Take Description.
        ### Parameters:
        - TakeIndex: index of take to set.
        - Description: take description to set"""
        ...
    def SetTakeDestinationName(self,TakeIndex:int,DestinationName:str):
        """Take Destination Name upon save or load.
        ### Parameters:
        - TakeIndex: index of take to set.
        - DestinationName: take description to set"""
        ...
    def SetTakeKeyRange(self,TakeIndex:int,KeyTimeSpan:FBTimeSpan):
        """Set take key range.
        ### Parameters:
        - TakeIndex: index of take to set.
        - KeyTimeSpan: Timespan indicating the time range to keep the keys. Keys that are outside the time range for this take will be removed, by default the time range is FBTime::MinusInfinity -> FBTime::Infinity
        
        ### Remarks:
        Valid only on load/merge, not when saving a file."""
        ...
    def SetTakeName(self,TakeIndex:int,Name:str):
        """Take Original Name.
        ### Parameters:
        - TakeIndex: index of take to set.
        - Name: take name to set"""
        ...
    def SetTakeSelect(self,TakeIndex:int,bSelect:bool):
        """Return if true if the take will be saved or Loaded.
        ### Parameters:
        - TakeIndex: index of take to set
        - bSelect: set true if should be saved or loaded."""
        ...
    @overload
    def __init__(self,arg2):...
    @overload
    def __init__(self,arg2,arg3:str):...
class FBFileMonitoringManager(FBComponent):
    OnFileChangeAnimationClip:FBEvent
    OnFileChangeFileReference:FBEvent
    OnFileChangeMainScene:FBEvent
    OnFileChangePythonEditorScript:FBEvent
    def AddFileToMonitor(self,FilePath:str,FileMonitoringType:FBFileMonitoringType):
        """Add file to monitor.
        ### Parameters:
        - FilePath: The file path to monitor.
        - FileMonitoringType: The monitor type of this file."""
        ...
    def CleanFileMonitoring(self,bIncludePythonEditorScripts:bool=True):
        """Clean files and directories currently been monitored.
        ### Parameters:
        - bIncludePythonEditorScripts: True to also clean the monitoring of Python Editor script files loaded, false otherwise."""
        ...
    def PauseFileMonitoring(self,bPause:bool=True):
        """Pause file from monitoring, except for Python Editor script files loaded.
        ### Parameters:
        - bPause: True to pause the file monitoring, false to resume."""
        ...
    def RemoveFileFromMonitor(self,FilePath:str):
        """Remove file from monitoring.
        ### Parameters:
        - FilePath: The file path to be removed."""
        ...
    def __init__(self):...
class FBFilter(FBComponent):
    Start:FBTime
    Stop:FBTime
    @overload
    def Apply(self,Node:FBAnimationNode,bRecursive:bool)->bool:
        """Apply the filter to an animation node.
        This is the other apply method and it can be used on an object's animation node.
        ### Parameters:
        - Node: Node to apply filter to.
        - bRecursive: Recursively apply filter on child nodes?
        
        ### Returns:
        true if successful."""
        ...
    @overload
    def Apply(self,Curve:FBFCurve)->bool:
        """Apply the filter to an FCurve.
        This is one of the two apply method that is meant to be called by client code. The FCurve can be a standalone independant FCurve, or can be associated to an object's animated property.
        ### Parameters:
        - Curve: FCurve to apply filter to.
        
        ### Returns:
        true if successful."""
        ...
    def Reset(self):
        """Reset properties.
        ### Warning:
        This method will only work on plug-in filters, not built-in types."""
        ...
class FBFolder(FBComponent):
    Items:FBPropertyListComponent
    def __init__(self,Name:str,Component:FBComponent):
        """### Parameters:
        - Name: Name to assign to new folder.
        - Component: Object used to determine folder's category."""
        ...
class FBGenericMenu(FBComponent):
    OnMenuActivate:FBEvent
    def DeleteItem(self,ToDelete:FBGenericMenuItem):
        """Remove a menu item from the menu and delete it.
        ### Parameters:
        - ToDelete: The item to remove."""
        ...
    def Execute(self,X:int,Y:int,bRightAlign:bool=True)->FBGenericMenuItem:
        """Starts the menu as a pop-up menu at a specific location on screen.
        It returns the item that was clicked by the user.
        ### Parameters:
        - X: X location in pixel on screen where the menu is to be popped.
        - Y: Y location in pixel on screen where the menu is to be popped.
        - bRightAlign: All menu item will be align to the right justified (if true) or left justified (if false)
        
        ### Returns:
        The selected item by the user. `None` if the user clicks outside the menu."""
        ...
    def GetFirstItem(self)->FBGenericMenuItem:
        """Returns the first menu item (if existing) in this menu.
        You can then use GetNextItem to iterate on other menu items.
        ### Returns:
        The first menu item in this Menu."""
        ...
    def GetItem(self,ItemId:int)->FBGenericMenuItem:
        """Returns the menu item corresponding to an id.
        ### Parameters:
        - ItemId: Id of the item we are looking for.
        
        ### Returns:
        Will return the Item corresponding to an id (null if not found)."""
        ...
    def GetLastItem(self)->FBGenericMenuItem:
        """Returns the last menu item (if existing) in this menu.
        You can then use GetPrevItem to reverse iterate on other menu items.
        ### Returns:
        The last menu item in this Menu."""
        ...
    def GetNextItem(self,Item:FBGenericMenuItem)->FBGenericMenuItem:
        """Returns the menu item following an other item.
        Returns `None` if this is the last item in menu.
        ### Parameters:
        - Item: Will return the item after Item
        
        ### Returns:
        Will return the item after Item. `None` if Item is the last item."""
        ...
    def GetPrevItem(self,Item:FBGenericMenuItem)->FBGenericMenuItem:
        """Returns the menu item preceding an other item.
        Returns `None` if this is the first item in menu.
        ### Parameters:
        - Item: Will return the item BEFORE Item
        
        ### Returns:
        Will return the item BEFORE Item. `None` if Item is the first item."""
        ...
    def InsertAfter(self,BeforeItem:FBGenericMenuItem,ItemName:str,ItemId:int,Menu:FBGenericMenu=None)->FBGenericMenuItem:
        """Inserts a new menu Item AFTER another item.
        ### Parameters:
        - BeforeItem: The reference item. We will create a new item AFTER this one.
        - ItemName: Caption of the newly added item.
        - ItemId: Unique id of this menu item.
        - Menu: Optional. If this Item leads to another menu (embedded) it can be specified here.
        
        ### Returns:
        Will return the menu item created from this insertion."""
        ...
    def InsertBefore(self,AfterItem:FBGenericMenuItem,ItemName:str,ItemId:int,Menu:FBGenericMenu=None)->FBGenericMenuItem:
        """Inserts a new menu Item BEFORE another item.
        ### Parameters:
        - AfterItem: The reference item. We will create a new item BEFORE this one.
        - ItemName: Caption of the newly added item.
        - ItemId: Unique id of this menu item.
        - Menu: Optional. If this Item leads to another menu (embedded) it can be specified here.
        
        ### Returns:
        Will return the menu item created from this insertion."""
        ...
    def InsertFirst(self,ItemName:str,ItemId:int,Menu:FBGenericMenu=None)->FBGenericMenuItem:
        """Inserts a new menu Item at the first position in the menu list.
        ### Parameters:
        - ItemName: Caption of the newly added item.
        - ItemId: Unique id of this menu item.
        - Menu: Optional. If this Item leads to another menu (embedded) it can be specified here.
        
        ### Returns:
        Will return the menu item created from this insertion."""
        ...
    def InsertLast(self,ItemName:str,ItemId:int,Menu:FBGenericMenu=None)->FBGenericMenuItem:
        """Inserts a new menu Item at the last position in the menu list.
        ### Parameters:
        - ItemName: Caption of the newly added item.
        - ItemId: Unique id of this menu item.
        - Menu: Optional. If this Item leads to another menu (embedded) it can be specified here.
        
        ### Returns:
        Will return the menu item created from this insertion."""
        ...
    def __init__(self):
        """Used to create embedded menu (inside another menu item) or pop-up menu."""
        ...
class FBGenericMenuItem(FBComponent):
    Caption:str
    Enable:bool
    Id:int
    Menu:FBGenericMenu
class FBGeometry(FBComponent):
    BinormalMappingMode:FBGeometryMappingMode
    BinormalReferenceMode:FBGeometryReferenceMode
    MaterialMappingMode:FBGeometryMappingMode
    NormalMappingMode:FBGeometryMappingMode
    NormalReferenceMode:FBGeometryReferenceMode
    TangentMappingMode:FBGeometryMappingMode
    TangentReferenceMode:FBGeometryReferenceMode
    VertexColorMappingMode:FBGeometryMappingMode
    VertexColorReferenceMode:FBGeometryReferenceMode
    def GeometryBegin(self)->bool:
        """Begin geometry editing.
        ### Returns:
        true if successful."""
        ...
    def GeometryEnd(self)->bool:
        """End geometry editing.
        ### Returns:
        true if successful."""
        ...
    def GetBinormalsDirectArray(self)->list:
        """Get a pointer to the direct array of binormals.
        Modify array value will be only effective when geometry editing is enabled.
        ### See also:
        GeometryBegin() /GeometryEnd()
        
        ### Returns:
        Pointer to direct array of binormals, or `None` if the array hasn't been allocated yet."""
        ...
    def GetBinormalsIndexArray(self)->list:
        """Get a pointer to the index array of binormals.
        Modify array value will be only effective when geometry editing is enabled.
        ### See also:
        GeometryBegin() /GeometryEnd()
        
        ### Returns:
        Pointer to index array of binormals, or `None` if the array hasn't been allocated yet."""
        ...
    def GetMaterialIndexArray(self)->list:
        """Get a pointer to the index array of Material.
        Modify array value will be only effective when geometry editing is enabled.
        ### See also:
        GeometryBegin() /GeometryEnd()
        
        ### Returns:
        Pointer to index array of Material, or `None` if the array hasn't been allocated yet."""
        ...
    def GetNormalsDirectArray(self)->list:
        """Get a pointer to the direct array of normals.
        Modify array value will be only effective when geometry editing is enabled.
        ### See also:
        GeometryBegin() /GeometryEnd()
        
        ### Returns:
        Pointer to direct array of normals, or `None` if the array hasn't been allocated yet."""
        ...
    def GetNormalsIndexArray(self)->list:
        """Get a pointer to the index array of normals.
        Modify array value will be only effective when geometry editing is enabled.
        ### See also:
        GeometryBegin() /GeometryEnd()
        
        ### Returns:
        Pointer to index array of normals, or `None` if the array hasn't been allocated yet."""
        ...
    def GetPositionsArray(self)->list:
        """Get a pointer to the position array.
        Modify array value will be only effective when geometry editing is enabled.
        ### See also:
        GeometryBegin() /GeometryEnd()
        
        ### Returns:
        Pointer to index array of normals, or `None` if the array hasn't been allocated yet."""
        ...
    def GetTangentsDirectArray(self)->list:
        """Get a pointer to the direct array of tangents.
        Modify array value will be only effective when geometry editing is enabled.
        ### See also:
        GeometryBegin() /GeometryEnd()
        
        ### Returns:
        Pointer to direct array of tangents, or `None` if the array hasn't been allocated yet."""
        ...
    def GetTangentsIndexArray(self)->list:
        """Get a pointer to the index array of tangents.
        Modify array value will be only effective when geometry editing is enabled.
        ### See also:
        GeometryBegin() /GeometryEnd()
        
        ### Returns:
        Pointer to index array of tangents, or `None` if the array hasn't been allocated yet."""
        ...
    def GetUVSetDirectArray(self,OutArrayCount:str=None)->list:
        """Get a pointer to the direct array of UVset Modify array value will be only effective when geometry editing is enabled.
        ### See also:
        GeometryBegin() /GeometryEnd()
        
        ### Parameters:
        - OutArrayCount: To return the length the array.
        ### Returns:
        pointer to the array of UV, or `None` is the array hasn't been allocated yet."""
        ...
    def GetUVSetIndexArray(self,OutArrayCount:str=None)->list:
        """Get a pointer to the index array of UVset.
        Modify array value will be only effective when geometry editing is enabled.
        ### See also:
        GeometryBegin() /GeometryEnd()
        
        ### Parameters:
        - OutArrayCount: To return the length the array.
        ### Returns:
        Pointer to index array of UVSet, or `None` if the array hasn't been allocated yet."""
        ...
    def GetUVSetMappingMode(self,UVSetName:str=None)->FBGeometryMappingMode:
        """Get UVSet mapping mode.
        ### Parameters:
        - UVSetName: The name of UVset, `None` for the first UVset.
        
        ### Returns:
        Mapping mode of the UVset."""
        ...
    def GetUVSetReferenceMode(self,UVSetName:str=None)->FBGeometryReferenceMode:
        """Get UVSet reference mode.
        ### Parameters:
        - UVSetName: The name of UVset, `None` for the first UVset.
        
        ### Returns:
        Reference mode of the UVset."""
        ...
    def GetUVSets(self)->FBStringList:
        """Get available UVSet name.
        ### Returns:
        StringList contain all the available UVSets' name."""
        ...
    def GetVertexColorsDirectArray(self)->list:
        """Get a pointer to the direct array of vertex color.
        Modify array value will be only effective when geometry editing is enabled.
        ### See also:
        GeometryBegin() /GeometryEnd()
        
        ### Returns:
        Pointer to direct array of vertex colors, or `None` if the array hasn't been allocated yet."""
        ...
    def GetVertexColorsIndexArray(self)->list:
        """Get a pointer to the index array of vertex color.
        Modify array value will be only effective when geometry editing is enabled.
        ### See also:
        GeometryBegin() /GeometryEnd()
        
        ### Returns:
        Pointer to index array of vertex color, or `None` if the array hasn't been allocated yet."""
        ...
    def SetBinormalsDirectArray(self,arg2:list)->bool:...
    def SetBinormalsIndexArray(self,arg2:list)->bool:...
    def SetMaterialIndexArray(self,arg2:list)->bool:...
    def SetNormalsDirectArray(self,arg2:list)->bool:...
    def SetNormalsIndexArray(self,arg2:list)->bool:...
    def SetPositionsArray(self,arg2:list)->bool:...
    def SetTangentsDirectArray(self,arg2:list)->bool:...
    def SetTangentsIndexArray(self,arg2:list)->bool:...
    def SetUVSetDirectArray(self,arg2:list,arg3:str=None)->bool:...
    def SetUVSetIndexArray(self,arg2:list,arg3:str=None)->bool:...
    def SetVertexColorsDirectArray(self,arg2:list)->bool:...
    def SetVertexColorsIndexArray(self,arg2:list)->bool:...
    def ShapeAdd(self,Name:str)->int:
        """Add new shape.
        ### Parameters:
        - Name: the shape name
        
        ### Returns:
        the index of the new shape, -1 if the shape adding fail."""
        ...
    def ShapeClearAll(self):
        """Clears all the shapes."""
        ...
    def ShapeGetCount(self)->int:
        """Get Shape Count."""
        ...
    def ShapeGetDiffPoint(self,ShapeIdx:int,DiffIndex:int,OriIndex:int,PosDiff:FBVertex,arg6:FBNormal)->bool:
        """Get the differentiate point.
        ### Parameters:
        - ShapeIdx: The index of the shape
        - DiffIndex: The index of the diff point in this shape.
        - OriIndex: The index of the diff point in the original geometry.
        - PosDiff: The position differentiation."""
        ...
    def ShapeGetDiffPointAsList(self,arg2,arg3,arg4:list,arg5:FBVertex,arg6:FBNormal)->bool:...
    def ShapeGetName(self,ShapeIdx:int)->str:
        """Return the shape Name."""
        ...
    def ShapeInit(self,ShapeIdx:int,DiffSize:int,bWithNormal:bool):
        """Init the shape.
        ### Parameters:
        - ShapeIdx: The index of the shape to be initialized
        - DiffSize: Total number of different point (pos or normal) compared to base geometry.
        - bWithNormal: Currently normal won't be considered during shape blending."""
        ...
    def ShapeSetDiffPoint(self,ShapeIdx:int,DiffIndex:int,OriIndex:int,PosDiff:FBVertex,arg6:FBNormal=None)->bool:
        """Set the differentiate point.
        ### Parameters:
        - ShapeIdx: The index of the shape
        - DiffIndex: The index of the diff point in this shape.
        - OriIndex: The index of the diff point in the original geometry.
        - PosDiff: The position differentiation."""
        ...
    @overload
    def VertexAdd(self,Vertex:FBVertex)->int:
        """Add a vertex.
        ### Parameters:
        - Vertex: Vertex values used to add vertex.
        
        ### Returns:
        Index where vertex was added.
        
        ### Remarks:
        Set Normal with default value"""
        ...
    @overload
    def VertexAdd(self,Vertex:FBVertex,Normal:FBNormal,UV:FBUV)->int:
        """Add a vertex.
        ### Parameters:
        - Vertex: Vertex values used to add vertex.
        - Normal: Normal values used to add vertex.
        - UV: UV values used to add vertex.
        
        ### Returns:
        Index where vertex was added."""
        ...
    def VertexArrayClear(self)->bool:
        """Clear all geometry vertex arrays.
        Call this function to clear Position, Normal, UV, Color and etc vertex arrays, and it won't affect geometry's topology (polygon, Surface and etc.,).
        ### Returns:
        true if successful."""
        ...
    def VertexArrayInit(self,Vertexcount:int,bUniqueMaterial:bool,FBGeometryArrayIDs:int=0)->bool:
        """Init geometry vertex arrays.
        Init position, normal and UV arrays (tangent, bi-normal and color on demand) with kFBGeometryMapping_BY_CONTROL_POINT / kFBGeometryReference_DIRECT mode. Will call VertexArrayClear() internally. User should then call GetXXXDirectyArray() to edit the vertex attributes directly.
        ### Parameters:
        - Vertexcount: number of control points (vertex)
        - bUniqueMaterial: User could specify per polygon mapping mode for mesh
        - FBGeometryArrayIDs: Request to init other attribute arrays, bitwise combined value of FBGeometryArrayID enum items, currently support Tangent, Binormal and VertexColor. Only useful for mesh."""
        ...
    def VertexClear(self)->bool:
        """Clear all Vertex arrays.
        Call this function to clear Position, Normal, UV, Color and etc vertex arrays, and it won't affect geometry's topology (polygon, Surface and etc.,).
        ### Returns:
        true if successful."""
        ...
    def VertexColorGet(self,Index:int)->FBColorAndAlpha:
        """Get a Vertex Color.
        ### Parameters:
        - Index: Index of Vertex to get Color for(default=-1).
        
        ### Returns:
        Color of vertex at UVSetIndex ."""
        ...
    @overload
    def VertexColorSet(self,Color:FBColorAndAlpha,Index:int=-1)->bool:
        """Set a Vertex Color.
        ### Parameters:
        - Color: Vertex Color to set.
        - Index: Index of Vertex to affect with Color(default=-1).
        
        ### Returns:
        true if successful."""
        ...
    @overload
    def VertexColorSet(self,Red:float,Green:float,Blue:float,Alpha:float,Index:int=-1)->bool:
        """Set a UV coordinate.
        ### Parameters:
        - Red: Red Color Channel to set, range [0, 1].
        - Green: Green Color Channel to set, range [0, 1].
        - Blue: Blue Color Channel to set, range [0, 1].
        - Alpha: Alpha Color Channel to set, range [0, 1].
        - Index: Index of Vertex to affect with Red, Green, Blue and Alpha (default=-1).
        
        ### Returns:
        true if successful."""
        ...
    def VertexCount(self)->int:
        """Get the number of vertices in the geometry.
        ### Returns:
        Number of vertices in the geometry."""
        ...
    def VertexGet(self,Index:int)->FBVertex:
        """Get a vertex.
        ### Parameters:
        - Index: Index of vertex to get.
        
        ### Returns:
        Vertex stored at Index ."""
        ...
    def VertexGetSelected(self,Index:int)->bool:
        """Get the selected state of a vertex.
        ### Parameters:
        - Index: The index of the vertex
        
        ### Returns:
        true if the vertex is selected, false if not"""
        ...
    def VertexGetTransformable(self,Index:int)->bool:
        """Get the Transformable state of a vertex.
        ### Parameters:
        - Index: The index of the vertex
        
        ### Returns:
        true if the vertex is Transformable, false if not"""
        ...
    def VertexGetVisible(self,Index:int)->bool:
        """Get the visible state of a vertex.
        ### Parameters:
        - Index: The index of the vertex
        
        ### Returns:
        true if the vertex is visible, false if not"""
        ...
    def VertexInit(self,Size:int,bResize:bool,bInitUV:bool=True,bInitVertexColor:bool=False):
        """Resize or Reserve vertex, normal and UV array for performance.
        ### Parameters:
        - Size: Number of vertices to resize or reserve.
        - bResize: True , for the geometry with known vertex count, we should resize the arrays to fixed size, and call VertexSet() afterwards; False , While for dynamic size geometry, we should only reserve the arrays with the estimated optimal size, then call VertexAdd() to dynamically increase the vertex count.
        - bInitUV: init Vertex UV array if true
        - bInitVertexColor: Init Vertex Color Array if true."""
        ...
    def VertexNormalGet(self,Index:int)->FBNormal:
        """Get a normal at a vertex.
        ### Parameters:
        - Index: Vertex to get normal at(default=-1).
        
        ### Returns:
        Normal of vertex at Index ."""
        ...
    @overload
    def VertexNormalSet(self,Vertex:FBNormal,Index:int=-1)->bool:
        """Set a normal at a vertex.
        ### Parameters:
        - Vertex: Normal to set.
        - Index: Index of vertex to set Normal at(default=-1).
        
        ### Returns:
        true if successful."""
        ...
    @overload
    def VertexNormalSet(self,x:float,y:float,z:float,Index:int=-1)->bool:
        """Set a normal at a vertex.
        ### Parameters:
        - x: X coordinate of normal.
        - y: Y coordinate of normal.
        - z: Z coordinate of normal.
        - Index: Index of vertex to set Normal at(default=-1).
        
        ### Returns:
        true if successful."""
        ...
    @overload
    def VertexSet(self,Vertex:FBVertex,Index:int=-1)->bool:
        """Set a vertex.
        ### Parameters:
        - Vertex: Vertex values used to set vertex.
        - Index: Index of vertex to affect (default=-1).
        
        ### Returns:
        true if successful."""
        ...
    @overload
    def VertexSet(self,x:float,y:float,z:float,Index:int=-1)->bool:
        """Set a vertex.
        ### Parameters:
        - x: X coordinate to set.
        - y: Y coordinate to set.
        - z: Z coordinate to set.
        - Index: Index of vertex to set(default=-1).
        
        ### Returns:
        true if successful."""
        ...
    def VertexSetSelected(self,Index:int,bState:bool)->bool:
        """Set the selected state of a vertex.
        ### Parameters:
        - Index: The index of the vertex
        - bState: The true to selected, false to deselect
        
        ### Returns:
        true if the vertex is selected, false if not"""
        ...
    def VertexSetVisible(self,Index:int,bState:bool)->bool:
        """Set the visible state of a vertex.
        ### Parameters:
        - Index: The index of the vertex
        - bState: true to be visible
        
        ### Returns:
        true if the vertex is visible, false if not"""
        ...
    def VertexUVGet(self,Index:int)->FBUV:
        """Get a UV coordinate.
        ### Parameters:
        - Index: Index of Vertex to get UV coordinate for(default=-1).
        
        ### Returns:
        UV coordinate of vertex at UVSetIndex ."""
        ...
    @overload
    def VertexUVSet(self,UV:FBUV,Index:int=-1)->bool:
        """Set a UV coordinate.
        ### Parameters:
        - UV: UV coordinate to set.
        - Index: Index of Vertex to affect with UV coordinate(default=-1).
        
        ### Returns:
        true if successful."""
        ...
    @overload
    def VertexUVSet(self,U:float,V:float,Index:int=-1)->bool:
        """Set a UV coordinate.
        ### Parameters:
        - U: U coordinate to set.
        - V: V coordinate to set.
        - Index: Index of Vertex to affect with UV coordinate(default=-1).
        
        ### Returns:
        true if successful."""
        ...
class FBHUDManager(FBComponent):
    DefaultHUD:property
    def __init__(self):...
class FBMesh(FBGeometry):
    def ComputeVertexNormals(self,bCW:bool=False):
        """Compute Mesh Vertex Normal.
        ### Parameters:
        - bCW: True for clock wise normal, otherwise for counter-clock wise"""
        ...
    def InverseNormal(self):
        """Inverse Normal."""
        ...
    def IsTriangleMesh(self)->bool:
        """Determines if the mesh is composed entirely of triangles.
        ### Returns:
        true if all polygons are triangles, false otherwise"""
        ...
    def PolygonBegin(self,MaterialId:int=0)->int:
        """Begin Polygon definition.
        ### Parameters:
        - MaterialId: Index of material for this polygon. Only effective when MaterialMappingMode is kFBGeometryMapping_BY_POLYGON mode.
        
        ### Returns:
        Number of existing polygons in Mesh"""
        ...
    def PolygonCount(self)->int:
        """Get number of polygons in mesh.
        ### Returns:
        Number of polygons in mesh."""
        ...
    def PolygonEnd(self)->int:
        """End Polygon definition.
        Clean up and associate vertices internally.
        ### Returns:
        Current number of polygons.
        
        ### Note:
        MoBu expect each polygon to contain at least 3 vertices, the behavior is undefined if user add less than 3 vertices polygon."""
        ...
    def PolygonListAdd(self,PolygonSize:int,IndexArraySize:int,IndexArray:list,MaterialId:int=0)->bool:
        """Add Polygon List Must be called in-between FBGeometry::GeometryBegin() / GeometryEnd() It's user's responsibility to make sure to input valid index values, otherwise afterwards behavior will be undefined.
        ### Parameters:
        - PolygonSize: Size of polygon, 3 mean triangle, 4 for quadrilateral, and so on. minimum input value is 3.
        - IndexArraySize: Size of IndexArray, Added polygon count is floor(max(IndexArraySize, 0) / PolygonSize)
        - IndexArray: Index array of triangle strip.
        - MaterialId: Index of material for this polygon. Only effective when MaterialMappingMode is kFBGeometryMapping_BY_POLYGON mode.
        
        ### Note:
        The indexes' value in input IndexArray won't be validated, and the behavior is undefined if out of range."""
        ...
    def PolygonMaterialIdGet(self,Index:int=-1)->int:
        """Get a Material ID for the given Polygon index.
        ### Parameters:
        - Index: Polygon's index to get material ID at (default=-1).
        
        ### Returns:
        ID of material of vertex at Index ."""
        ...
    def PolygonVertexAdd(self,Vertex:int)->bool:
        """Add a vertex.
        ### Parameters:
        - Vertex: Index in mesh of vertex to add to polygon, must be in range of [0, ControlPointCount)
        
        ### Returns:
        true if successful."""
        ...
    def PolygonVertexArrayGet(self)->list:
        """Get the array of polygon vertex (i.e.
        index to control points). This array is a concatenation of the list of polygon vertices of all the polygons. Example: a mesh made of 2 triangles [1,2,3] and [2,3,4] results in [1,2,3,2,3,4]. The first polygon starts at position 0 and the second at position 3.
        ### Returns:
        Readonly polygon vertex array."""
        ...
    def PolygonVertexCount(self,PolygonIndex:int)->int:
        """Get Polygon vertex count.
        ### Parameters:
        - PolygonIndex: Index of polygon to get vertex count from.
        
        ### Returns:
        Number of vertices in polygon at PolygonIndex ."""
        ...
    def PolygonVertexIndex(self,PolygonIndex:int,VertexPolygonIndex:int)->int:
        """Get global (for the mesh) index of a vertex from a polygon.
        ### Parameters:
        - PolygonIndex: Index of polygon in question.
        - VertexPolygonIndex: Polygon vertex index.
        
        ### Returns:
        Index in mesh of vertex."""
        ...
    def TriangleListAdd(self,IndexArraySize:int,IndexArray:list,MaterialId:int=0)->bool:
        """Add Triangle List, Must be called in-between FBGeometry::GeometryBegin() / GeometryEnd() It's user's responsibility to make sure to input valid index values, otherwise afterwards behavior will be undefined.
        ### Parameters:
        - IndexArraySize: Size of IndexArray, Added triangle count is floor(max(IndexArraySize, 0) / 3)
        - IndexArray: Index array of triangle list.
        - MaterialId: Index of material for this polygon. Only effective when MaterialMappingMode is kFBGeometryMapping_BY_POLYGON mode.
        
        ### Note:
        The indexes' value in input IndexArray won't be validated, and the behavior is undefined if out of range."""
        ...
    def TriangleStripAdd(self,IndexArraySize:int,IndexArray:list,MaterialId:int=0)->bool:
        """Add Triangle Strip Must be called in-between FBGeometry::GeometryBegin() / GeometryEnd() It's user's responsibility to make sure to input valid index values, otherwise afterwards behavior will be undefined.
        ### Parameters:
        - IndexArraySize: Size of IndexArray, Added triangle count is max(IndexArraySize - 2, 0)
        - IndexArray: Index array of triangle strip.
        - MaterialId: Index of material for this polygon. Only effective when MaterialMappingMode is kFBGeometryMapping_BY_POLYGON mode.
        
        ### Note:
        The indexes' value in input IndexArray won't be validated, and the behavior is undefined if out of range."""
        ...
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of Mesh."""
        ...
class FBImage(FBComponent):
    Depth:int
    Format:FBImageFormat
    Height:int
    InterleaveType:FBImageInterleaveType
    InterpolationType:FBImageInterpolationType
    Type:FBImageType
    Width:int
    def Cleanup(self):
        """Cleanup image data, making it black."""
        ...
    def ConvertFormat(self,NewFormat:FBImageFormat)->bool:
        """Convert the image data format to another format.
        ### Parameters:
        - NewFormat: The new format to convert the image to.
        
        ### Returns:
        Return true if the convert was successful."""
        ...
    def ConvertSize(self,Width:int,Height:int)->bool:
        """Convert the image size.
        ### Parameters:
        - Width: New width of the image.
        - Height: New height of the image.
        
        ### Returns:
        Return true if the convert was successful."""
        ...
    def GetBufferAddress(self)->int:
        """Access image data buffer, allow modifications.
        ### Returns:
        Pointer to the image data, values ranging from 0 to 255."""
        ...
    def Init(self,Format:FBImageFormat,Width:int,Height:int)->bool:
        """### Parameters:
        - Format: Image format used to initialize data buffer.
        - Width: Image width in pixels.
        - Height: Image height in pixels."""
        ...
    def IsCompressedTif(self,FileName:str)->bool:
        """Query TIF file about its compressed status.
        ### Parameters:
        - FileName: Full TIF file path name of the file to query.
        
        ### Returns:
        Return true if the TIF file image data is compressed."""
        ...
    def VerticalFlip(self):
        """Flip the image vertically."""
        ...
    def WriteToTif(self,FileName:str,Comments:str,bCompressed:bool)->bool:
        """Write image data to a TIF file on disk.
        ### Parameters:
        - FileName: Full TIF file path name of the file to write.
        - Comments: Comments appended to the TIF file.
        - bCompressed: If true, the image data in the file will be compressed.
        
        ### Returns:
        Return true if the image was successfully written on disk."""
        ...
    def __init__(self,FileName:str):
        """### Parameters:
        - FileName: Path to the image file. If pObject is not NULL, FileName will be ignored."""
        ...
class FBKeyControl(FBComponent):
    AutoKey:bool
    NewKeyInterpolationType:FBNewKeyInterpolationType
    def MoveKeys(self,TimeSpan:FBTimeSpan,Pivot:FBModel,T:FBVector3d,R:FBVector3d,S:FBVector3d,Time:FBTime,ModelList:FBModelList=None):
        """Move animation keys in space, with respect to a pivot object.
        Equivalent to using the "Move Keys" button in the Key Controls panel. Only keys that are part of the current animation layer will get affected.
        ### Parameters:
        - TimeSpan: The time span in which the animation keys will be modified
        - Pivot: The pivot object to use as a reference. The pivot needs to be part of ModelList (or the current keying group) otherwise the move keys operation will abort
        - T: The global translation to apply to the pivot
        - R: The global Euler rotation to apply to the pivot (deg)
        - S: The global scaling factors to apply to the pivot
        - Time: The time at which the transformation values are applied to the pivot object
        - ModelList: List of models for which the animation will be modified. Optional parameter. If not supplied, the models in the current keying group will be used"""
        ...
    def __init__(self):...
class FBKeyingGroup(FBComponent):
    def AddObjectDependency(self,Obj:FBComponent):
        """AddObjectDependency An object dependency is the content of a keying group and will activate keying group when selected (activation only works if the keying group is a character extension).
        ### Parameters:
        - Obj: a Dependency of the keying group."""
        ...
    def AddProperty(self,Prop:FBProperty):
        """Add property to be keyed when current keying group is active.
        ### Parameters:
        - Prop: Property to be added."""
        ...
    def ClearAllItems(self):
        """ClearAllItems clear object dependency, properties and child keying group."""
        ...
    @staticmethod
    def DeselectAllAnimatableProperties():
        """FBDeselectAllAnimatableProperties, deselect all animatable properties in the scene."""
        ...
    def FindPropertyIndex(self,Prop:FBProperty)->int:
        """### Parameters:
        - Prop: must be in the list (return -1 if not).
        
        ### Returns:
        the index of Prop in the keyinggroup property list."""
        ...
    def GetCumulativeProperty(self,Index:int,bStopAtVisible:bool)->FBProperty:
        """GetCumulativeProperty Same as GetSubKeyingGroup but recursive in child keying group.
        ### Parameters:
        - Index: index in the content Object Dependency list
        - bStopAtVisible: consider all keying group and stop to the first visible keying group.
        
        ### Returns:
        he number of ObjectDependency of the keying group."""
        ...
    def GetCumulativePropertyCount(self,bStopAtVisible:bool=False)->int:
        """GetCumulativePropertyCount Same as GetSubKeyingGroupCount but recursive in child keying group.
        ### Parameters:
        - bStopAtVisible: consider all keying group and stop to the first visible keying group.
        
        ### Returns:
        he number of ObjectDependency of the keying group."""
        ...
    def GetParentKeyingGroup(self,Index:int)->FBKeyingGroup:
        """### Parameters:
        - Index: is the index of the parent list of the current keying group.
        
        ### Returns:
        the parent keying group."""
        ...
    def GetParentKeyingGroupCount(self)->int:
        """### Returns:
        the number of parent."""
        ...
    def GetProperty(self,Index:int)->FBProperty:
        """GetProperty from the keyinggroup list.
        ### Parameters:
        - Index: index of the desired property.
        
        ### Returns:
        property coresponding to Index."""
        ...
    def GetPropertyCount(self)->int:
        """### Returns:
        the number of properties in the keying group."""
        ...
    def GetSubKeyingGroup(self,Index:int)->FBKeyingGroup:
        """### Parameters:
        - Index: index of the desired keying group child.
        
        ### Returns:
        the the child at the index."""
        ...
    def GetSubKeyingGroupCount(self)->int:
        """### Returns:
        the number of child keying group."""
        ...
    def GetSubObject(self,Index:int)->FBComponent:
        """### Parameters:
        - Index: index in the content Object Dependency list
        
        ### Returns:
        the desired object at Index ."""
        ...
    def GetSubObjectCount(self)->int:
        """### Returns:
        the number of ObjectDependency of the keying group."""
        ...
    def IsObjectDependency(self,Obj:FBComponent)->bool:
        """IsObjectDependency determine if the Obj is a dependency.
        ### Parameters:
        - Obj: an object to test the Dependency.
        
        ### Returns:
        true if it depend."""
        ...
    def IsObjectDependencySelected(self)->bool:
        """### Returns:
        return true as soon as a Property Owner or another Object Dependency is selected."""
        ...
    def RemoveAllObjectDependency(self):
        """IsObjectDependencySelected empty the content list."""
        ...
    def RemoveAllProperties(self):
        """IsObjectDependencySelected empty the property list."""
        ...
    def RemoveAllSubKeyingGroup(self):
        """RemoveAllSubKeyingGroup empty the child keying group."""
        ...
    def RemoveObjectDependency(self,Obj:FBComponent):
        """RemoveObjectDependency An object dependency is the content of a keying group and will activate keying group when selected (activation only works if the keying group is a character extension).
        ### Parameters:
        - Obj: a Dependency of the keying group."""
        ...
    def RemoveProperty(self,Prop:FBProperty):
        """RemoveProperty from the keyinggroup list.
        ### Parameters:
        - Prop: Property to be removed."""
        ...
    def SetActive(self,bActive:bool):
        """SetActive, activate the keying group, replacing the other keying group."""
        ...
    def SetActiveAppend(self,bActive:bool):
        """SetActiveAppend, activate and append the keying group to the other keying groups."""
        ...
    def SetEnabled(self,bEnable:bool):
        """SetEnabled, makes the keying group available in keying group list of the key control UI."""
        ...
    def SetObjectType(self,Object:FBComponent):
        """Set the object type filter for and object type keying group.
        ### Parameters:
        - Object: Object that will be used to set the keying group object type. Use `None` to remove the filter."""
        ...
    def __init__(self,Name:str,Type:FBKeyingGroupType):
        """### Parameters:
        - Name: Group name.
        - Type: Keying group type."""
        ...
class FBLogger(FBComponent):
    def DisableClear(self):
        """DisableClear - disable and clear the log."""
        ...
    def DumpObject(self,arg2:FBPlug,arg3)->object:...
    @overload
    def Enable(self,TypeInfo:int,bEnable:bool)->bool:
        """Enable - enable logging for a specific type.
        ### Parameters:
        - TypeInfo: - the static TypeInfo value for the FB class we're interested in
        - bEnable: 
        
        ### Returns:
        True if the class could be found."""
        ...
    @overload
    def Enable(self,ClassName:str,bEnable:bool)->bool:
        """Enable logging for a specific class ID.
        ### Parameters:
        - ClassName: The internal ID of class to be traced.
        - bEnable: 
        
        ### Returns:
        True if the class could be found."""
        ...
    def GetLog(self)->object:...
    def __init__(self):...
class FBCharacterExtension(FBKeyingGroup):
    IncludePartInBodyPart:bool
    IncludePartInFullBody:bool
    Label:str
    MirrorLabel:int
    PlotAllowed:FBPlotAllowed
    ReferenceModel:FBModel
    RetargetMode:FBCharacterExtensionRetargetMode
    StancePoseMode:FBCharacterExtensionStancePoseMode
    SyncActivationAndVisibilityMode:FBSyncActivationAndVisibilityMode
    def AddObjectProperties(self,Obj:FBComponent):
        """Add TR Properties from Object.
        ### Parameters:
        - Obj: Object to add TR properties."""
        ...
    def GetCharacter(self)->FBCharacter:
        """Return the attached Character.
        ### Returns:
        attached Character."""
        ...
    def GetExtensionObjectWithLabelName(self,LabelName:str)->FBComponent:
        """Find stored object based on label name.
        ### Parameters:
        - LabelName: The label name.
        
        ### Returns:
        The extension object."""
        ...
    def GetLabelNameWithExtensionObject(self,LabelName:FBComponent,Obj:FBComponent)->str:
        """Find the label name that was used to store object pose.
        ### Parameters:
        - LabelName: The label name that was used to store object pose.
        - Obj: The extension object."""
        ...
    def GetMirrorExtension(self)->FBCharacterExtension:
        """Return the character extension determined by MirrorLabel.
        ### Returns:
        character extension determined by MirrorLabel."""
        ...
    def GetRetargetPropertyCount(self)->int:
        """Return the total number of retarget properties.
        ### Returns:
        The total number of retarget properties."""
        ...
    def GetRetargetReferenceProperty(self,PropIndex:int)->FBProperty:
        """Return the reference property of the given index.
        ### Parameters:
        - PropIndex: Index to query.
        
        ### Returns:
        Reference property of the given index."""
        ...
    def GetRetargetSourceProperty(self,PropIndex:int)->FBProperty:
        """Return the source property of the given index (the source property is the property that drives the reference property during retargeting).
        ### Parameters:
        - PropIndex: Index to query.
        
        ### Returns:
        Source property (the property that drives the reference property during retargeting) of the given index."""
        ...
    def GetSourceExtension(self)->FBCharacterExtension:
        """Return the character extension that is used to drive this extension during retargeting.
        ### Returns:
        The character extension that is used to drive this extension during retargeting."""
        ...
    def GetSourceExtensionIndex(self)->int:
        """Return the enum that indicate which extension is used as a source during retargeting, 0 is none, 1-n represent the (ith - 1)character extension in the source character.
        ### Returns:
        The enum that indicate which extension is used as a source during retargeting, 0 is none, 1-n represent the (ith - 1)character extension in the source character."""
        ...
    def GetStancePose(self)->FBObjectPose:
        """Return stance pose.
        ### Returns:
        stance pose."""
        ...
    def GoToStancePose(self):
        """Reset object position to the stance."""
        ...
    def IsElementSelected(self)->bool:
        """Return true if one object in object dependency list is selected.
        ### Returns:
        true if one object in object dependency list is selected."""
        ...
    def IsPropertyIncluded(self,Prop:FBProperty)->bool:
        """Return true if the property is in character extension.
        ### Parameters:
        - Prop: Property to check.
        
        ### Returns:
        true if the property is in character extension."""
        ...
    def RemoveObjectAndProperties(self,Obj:FBComponent):
        """Remove TR Properties from Object.
        ### Parameters:
        - Obj: Object to remove TR properties."""
        ...
    def RemoveRetargetSourceProperty(self,PropIndex:int):
        """Remove the source property for retargeting.
        Only applicable if RetargetMode is Manually Assign.
        ### Remarks:
        Only applicable if RetargetMode is Manually Assign.
        
        ### Parameters:
        - PropIndex: Index to remove."""
        ...
    def SetRetargetSourceProperty(self,PropIndex:int,SourceProp:FBProperty):
        """Set the source property for retargeting.
        Only applicable if RetargetMode is Manually Assign.
        ### Remarks:
        Only applicable if RetargetMode is Manually Assign.
        
        ### Parameters:
        - PropIndex: Index to set.
        - SourceProp: Source property to set."""
        ...
    def SetSourceExtension(self,SourceExtension:FBCharacterExtension):
        """Set the character extension to drive this extension during retargeting.
        Only applicable if RetargetMode is Assign.
        ### Remarks:
        Only applicable if RetargetMode is Assign.
        
        ### Parameters:
        - SourceExtension: The source extension to drive this extension during retargeting."""
        ...
    def SetSourceExtensionIndex(self,SrcExtIndex:int):
        """Set the enum that indicate which extension is used as a source during retargeting, 0 is none, 1-n represent the (ith - 1)character extension in the source character.
        Only applicable if RetargetMode is Manually Assign.
        ### Remarks:
        Only applicable if RetargetMode is Manually Assign.
        
        ### Parameters:
        - SrcExtIndex: Enum that indicate which extension is used as a source during retargeting, 0 is none, 1-n represent the (ith - 1)character extension in the source character."""
        ...
    def UpdateStancePose(self):
        """Update the stance pose to the current position of the character extension element."""
        ...
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Group name."""
        ...
class FBManipulator(FBComponent):
    Active:bool
    AlwaysActive:bool
    ConsumeEvent:bool
    DefaultBehavior:bool
    ViewerText:str
    Visible:bool
class FBMarkerSet(FBComponent):
    def AddMarker(self,NodeId:FBSkeletonNodeId,Model:FBModel=None,bIsOriented:bool=False)->int:
        """Add a marker to the marker set.
        ### Parameters:
        - NodeId: Id of Actor skeleton node. For hand, use the "C" index (ex:kFBSkeletonLeftThumbCIndex, kFBSkeletonLeftMiddleCIndex...)
        - Model: The model to be associated with the marker (Optional).
        - bIsOriented: Set marker to be oriented or not (Optional).
        
        ### Returns:
        Index of the new marker."""
        ...
    def BeginTransaction(self):
        """Specify that you are about to call a group of functions.
        ### Remarks:
        This is used to speed up operations, the UI won't be refreshed until EndTransaction() is called."""
        ...
    def EndTransaction(self):
        """Specify that you are done calling a group of functions.
        ### Remarks:
        This is used to speed up operations, the UI won't be refreshed until EndTransaction() is called."""
        ...
    def GetLinkToModelOk(self)->bool:
        """Get the marker set association correctness.
        ### Returns:
        True if all used markers are link with models."""
        ...
    def GetMarkerCount(self,NodeId:FBSkeletonNodeId=FBSkeletonNodeId.kFBSkeletonInvalidIndex)->int:
        """Get the number of marker in the set.
        ### Parameters:
        - NodeId: If specified, obtain the number of marker for the specific node.
        
        ### Returns:
        Total number of marker."""
        ...
    def GetMarkerModel(self,NodeId:FBSkeletonNodeId,MarkerIndex:int)->FBModel:
        """Get the model associated with a marker.
        ### Parameters:
        - NodeId: Id of Actor skeleton node.
        - MarkerIndex: Index of marker.
        
        ### Returns:
        The model associated with the marker."""
        ...
    def GetMarkerName(self,NodeId:FBSkeletonNodeId,MarkerIndex:int)->str:
        """Get the name of marker at index MarkerIndex .
        ### Parameters:
        - NodeId: Id of Actor skeleton node.
        - MarkerIndex: Index of marker to access.
        
        ### Returns:
        Name of marker at index MarkerIndex ."""
        ...
    def GetMarkerOriented(self,NodeId:FBSkeletonNodeId,MarkerIndex:int)->bool:
        """Is marker orientated ?
        ### Parameters:
        - NodeId: Id of Actor body node.
        - MarkerIndex: Index of marker to access.
        
        ### Returns:
        True if marker is oriented, false otherwise."""
        ...
    def GetMarkerROffset(self,NodeId:FBSkeletonNodeId,MarkerIndex:int,ROffset:FBVector3d):
        """Get/Set a marker rotation.
        ### Parameters:
        - NodeId: Id of Actor skeleton node.
        - MarkerIndex: Index of marker to access.
        
        ### Return values:
        - ROffset: Current or new value of the marker rotation."""
        ...
    def GetMarkerSetVisibility(self)->int:
        """Get the marker set visibility.
        ### Returns:
        1 if all markers are visible, 2 if some are visible, 0 if none are visible."""
        ...
    def GetMarkerTOffset(self,NodeId:FBSkeletonNodeId,MarkerIndex:int,TOffset:FBVector3d):
        """Get/Set a marker translation.
        ### Parameters:
        - NodeId: Id of Actor skeleton node.
        - MarkerIndex: Index of marker to access.
        
        ### Return values:
        - TOffset: Current or new value of the marker translation."""
        ...
    def GetMarkerUsed(self,NodeId:FBSkeletonNodeId,MarkerIndex:int)->bool:
        """Is marker used ?
        ### Parameters:
        - NodeId: Id of Actor skeleton node.
        - MarkerIndex: Index of marker to access.
        
        ### Returns:
        True if marker is used, false otherwise."""
        ...
    def GetReferenceModel(self)->FBModel:
        """Get the reference model associated with this marker set.
        ### Returns:
        The reference model associated with the marker set."""
        ...
    def GetUsedMarkerCount(self,NodeId:FBSkeletonNodeId=FBSkeletonNodeId.kFBSkeletonInvalidIndex)->int:
        """Get the number of used marker in the set.
        ### Parameters:
        - NodeId: If specified, obtain the number of used marker for the specific node.
        
        ### Returns:
        Total number of used marker."""
        ...
    def SetMarkerModel(self,NodeId:FBSkeletonNodeId,MarkerIndex:int,Model:FBModel):
        """Associate a model to a marker.
        ### Parameters:
        - NodeId: Id of Actor skeleton node.
        - MarkerIndex: Index of marker.
        - Model: Model to be associated to the marker."""
        ...
    def SetMarkerName(self,NodeId:FBSkeletonNodeId,MarkerIndex:int,MarkerName:str):
        """Set the name of marker at index MarkerIndex .
        ### Parameters:
        - NodeId: Id of Actor skeleton node.
        - MarkerIndex: Index of marker to access.
        - MarkerName: New name to give to the marker."""
        ...
    def SetMarkerOriented(self,NodeId:FBSkeletonNodeId,MarkerIndex:int,bIsOriented:bool):
        """Set marker to be oriented or not.
        ### Parameters:
        - NodeId: Id of Actor skeleton node.
        - MarkerIndex: Index of marker to access.
        - bIsOriented: Oriented or not."""
        ...
    def SetMarkerROffset(self,arg2:FBSkeletonNodeId,arg3,arg4:FBVector3d):...
    def SetMarkerSetVisibility(self,bVisibility:bool):
        """Set the marker set visibility.
        ### Parameters:
        - bVisibility: True will make to markers visible, false will hide them."""
        ...
    def SetMarkerTOffset(self,arg2:FBSkeletonNodeId,arg3,arg4:FBVector3d):...
    def SetMarkerUsed(self,NodeId:FBSkeletonNodeId,MarkerIndex:int,bUsed:bool):
        """Set marker to be used or not.
        ### Parameters:
        - NodeId: Id of Actor skeleton node.
        - MarkerIndex: Index of marker to access.
        - bUsed: Used or not."""
        ...
    def SetMultipleMarkerModels(self,ModelList:FBModelList)->bool:
        """Associate multiple models to markers, matching them by name.
        ### Parameters:
        - ModelList: A list of models to be matched with marker names.
        
        ### Returns:
        True if at least one marker was matched."""
        ...
    def SetReferenceModel(self,ReferenceModel:FBModel):
        """Associate a model to a marker.
        ### Parameters:
        - ReferenceModel: Model to be associated to the marker."""
        ...
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of new marker set."""
        ...
class FBMenuManager(FBComponent):
    def ExecuteMenuItem(self,MenuPath:str,MenuItemID:int)->bool:
        """Execute a particular menu item.
        The menu path specifies the menu containing the menu item to execute. The ID specifies which menu item to execute in the menu.
        ### Parameters:
        - MenuPath: Path containing the menu item to execute.
        - MenuItemID: Unique ID of the menu item to execute.
        
        ### Returns:
        True if the menu item has been executed, false otherwise. It could returns false if the menu item cannot be found or if the menu item is found but is disabled or is a separator."""
        ...
    def ExecuteMenuItemFromFullPath(self,MenuItemFullPath:str)->bool:
        """Execute a particular menu item.
        The menu path specifies the menu item (NOT menu) to execute. Don't forget that most menu path already in MotionBuilder have a "&" as the first letter of their name. You have to use the "/" character as a separator in the specified menu path (ex: "Settings/&Preferences..."), and exactly what is written in the menu item (ex: "Edit/D&eselect\tShift+D").
        ### Parameters:
        - pMenuItemPath: Path of the menu item to execute.
        
        ### Returns:
        True if the menu item has been executed, false otherwise. It could returns false if the menu item cannot be found or if the menu item is found but is disabled or is a separator. # This example shows how to display the About Box, as if the user opened it via the main menu Help > About MotionBuilder:"""
        ...
    def GetMenu(self,Path:str)->FBGenericMenu:
        """Get the Menu (NOT menu item) corresponding to a menu path.
        Don't forget that most menu path already in MotionBuilder have a "&" character as the first letter of their name. You have to use the "/" character as a separator in the specified menu path (ex: "Help/&Communities").
        ### Parameters:
        - Path: Path of the menu to retrieve
        
        ### Returns:
        the FBGenericMenu at this path./"""
        ...
    def InsertAfter(self,MenuPath:str,BeforeMenuName:str,MenuName:str)->FBGenericMenuItem:
        """Insert a new menu at a specific path AFTER another item.
        ### Parameters:
        - MenuPath: Path where to insert the menu. If this is `None` (None) it will insert a new root menu.
        - BeforeMenuName: Name of the menu item AFTER which we will insert the new item.
        
        ### Returns:
        Returns the menu item corresponding to the newly inserted menu."""
        ...
    def InsertBefore(self,MenuPath:str,AfterMenuName:str,MenuName:str)->FBGenericMenuItem:
        """Insert a new menu at a specific path BEFORE another item.
        ### Parameters:
        - MenuPath: Path where to insert the menu. If this is `None` (None) it will insert a new root menu.
        - AfterMenuName: Name of the menu item BEFORE which we will insert the new item.
        
        ### Returns:
        Returns the menu item corresponding to the newly inserted menu."""
        ...
    def InsertFirst(self,MenuPath:str,MenuName:str)->FBGenericMenuItem:
        """Insert a new menu at the first position of a specific path.
        ### Parameters:
        - MenuPath: Path where to insert the menu. If this is `None` (None) it will insert a new root menu.
        - MenuName: Name (Caption) of the newly inserted menu.
        
        ### Returns:
        Returns the menu item corresponding to the newly inserted menu."""
        ...
    def InsertLast(self,MenuPath:str,MenuName:str)->FBGenericMenuItem:
        """Insert a new menu at the last position of a specific path.
        ### Parameters:
        - MenuPath: Path where to insert the menu. If this is `None` (None) it will insert a new root menu.
        - MenuName: Name (Caption) of the newly inserted menu.
        
        ### Returns:
        Returns the menu item corresponding to the newly inserted menu."""
        ...
    def IsItemEnable(self,MenuPath:str,ItemId:int)->bool:
        """Check if a particular item is enabled or disabled.
        The menu path specifies the menu where we find the item to be enabled/disabled. The Id specifies which item in the menu.
        ### Parameters:
        - MenuPath: Path where to find the menu to check
        - ItemId: Id of the item to check.
        
        ### Returns:
        Is the item enable or not."""
        ...
    def SetItemEnable(self,MenuPath:str,ItemId:int,bEnable:bool):
        """Enable or disable a specific menu item.
        The menu path specifies the menu where we find the item to be enabled/disabled. The Id specifies which item in the menu.
        ### Parameters:
        - MenuPath: Path where to find the menu to enable/disable
        - ItemId: Id of the item in the menu to disable.
        - bEnable: Enable (true) or disable (false) a menu item."""
        ...
    def __init__(self):
        """There is only one MenuManager in MotionBuilder, creating multiple FBMenuManager always return the same handle to the same global menu manager."""
        ...
class FBModelOpticalAdvanced(FBComponent):
    Active:bool
    AutoPlayToNextSegment:bool
    ControllerMode:FBControllerMode
    GenerationMode:FBGenerationMode
    InsertSegmentMode:FBInsertSegmentMode
    MaxMatchDistance:float
    PlayToNextSegment:bool
    Quality:FBAnimationNode
    SegmentMode:FBSegmentMode
    ShowRigidQuality:bool
    UsedTake:FBTake
    def AcceptAllSegments(self):
        """Accept all segments."""
        ...
    def AcceptSegment(self):
        """Accept current segment."""
        ...
    def AutomaticBuild(self):
        """Automatic build."""
        ...
    def CropSegmentsAnimation(self):
        """Crop segment animation."""
        ...
    def SkipSegment(self):
        """Skip segment."""
        ...
    def __init__(self,Optical:FBModelOptical):
        """### Parameters:
        - Optical: Optical model."""
        ...
class FBModelTemplate(FBComponent):
    Bindings:FBPropertyListModelTemplateBinding
    Children:FBPropertyListModelTemplate
    DefaultRotation:FBVector3d
    DefaultScaling:FBVector3d
    DefaultTranslation:FBVector3d
    Model:FBModel
    Prefix:str
class FBModelVertexData(FBComponent):
    def DisableOGLUVSet(self):...
    def DisableOGLVertexData(self):...
    def DrawSubPatch(self,arg2,arg3=None):...
    def DrawSubRegion(self,arg2,arg3=None):...
    def EnableOGLUVSet(self,arg2:FBTextureMapping=None,arg3:str=None):...
    def EnableOGLVertexData(self,arg2=None):...
    def GetIndexArray(self)->list:...
    def GetIndexArraySize(self)->int:...
    def GetIndexArrayVBOId(self)->int:...
    def GetSubPatchCount(self)->int:...
    def GetSubPatchIndexOffset(self,arg2)->int:...
    def GetSubPatchIndexSize(self,arg2)->int:...
    def GetSubPatchMaterial(self,arg2)->object:...
    def GetSubPatchMaterialId(self,arg2)->int:...
    def GetSubPatchPrimitiveType(self,arg2)->tuple:...
    def GetSubRegionCount(self)->int:...
    def GetSubRegionMaterial(self,arg2)->object:...
    def GetUVSetArray(self,arg2:FBTextureMapping=None,arg3:str=None)->list:...
    def GetUVSetArrayFormat(self,arg2:FBTextureMapping=None,arg3:str=None)->FBGeometryArrayElementType:...
    def GetUVSetUVCount(self,arg2:FBTextureMapping=None,arg3:str=None)->int:...
    def GetUVSetVBOId(self,arg2:FBTextureMapping=None,arg3:str=None)->int:...
    def GetUVSetVBOOffset(self,arg2:FBTextureMapping=None,arg3:str=None)->int:...
    def GetVertexArray(self,arg2:FBGeometryArrayID,arg3=None)->list:...
    def GetVertexArrayDuplicationMap(self)->list:...
    def GetVertexArrayType(self,arg2:FBGeometryArrayID,arg3=None)->FBGeometryArrayElementType:...
    def GetVertexArrayVBOId(self,arg2:FBGeometryArrayID,arg3=None)->int:...
    def GetVertexArrayVBOOffset(self,arg2:FBGeometryArrayID,arg3=None)->int:...
    def GetVertexCount(self)->int:...
    def IsDeformable(self)->bool:...
    def IsDrawable(self)->bool:...
    def PopZDepthClipOverride(self):...
    def PushZDepthClipOverride(self):...
    def VertexArrayMappingRelease(self):...
    def VertexArrayMappingRequest(self):...
class FBMotionClip(FBComponent):
    Filename:str
    RelativePath:str
    Start:FBTime
    Stop:FBTime
    def __init__(self,FileName:str):
        """### Parameters:
        - FileName: The complete file path of the media file to access."""
        ...
class FBMotionFileOptions(FBComponent):
    BaseRotationOnPreRotation:bool
    BaseTranslationOnRotationOffset:bool
    CreateInsteadOfMerge:bool
    CreateOpticalSegments:bool
    CreateReferenceNode:bool
    CreateUnmatchedModels:bool
    CreateUnusedOpticalSegments:bool
    IgnoreModelType:bool
    ImportDOF:bool
    ImportScaling:bool
    KeepActorPrefix:bool
    KeepDummyNode:bool
    ModelSelection:FBModelSelection
    SetLimits:bool
    SetOccludedToLastValidPosition:bool
    TakeStartEnd:FBTakeSpanOnLoad
    UpAxisUsedInFile:FBUpAxis
    def GetTakeCount(self)->int:
        """Return the take count in the file to be loaded.
        ### Warning:
        You need to use an appropriate constructor with the file path to be able to get the take information.
        
        ### Returns:
        Take count"""
        ...
    def GetTakeName(self,TakeIndex:int)->str:
        """Get the take name.
        ### Parameters:
        - TakeIndex: Index of take to get the name.
        
        ### Returns:
        Take name"""
        ...
    def GetTakeSamples(self,TakeIndex:int)->int:
        """Return the number of samples.
        ### Parameters:
        - TakeIndex: Index of take to get the samples count.
        
        ### Returns:
        Number of samples"""
        ...
    def GetTakeSamplingRate(self,TakeIndex:int)->float:
        """Return the actual sampling rate as a double, useful when you have a custom sampling rate.
        ### Parameters:
        - TakeIndex: Index of take to get the sampling rate
        
        ### Returns:
        Sample rate"""
        ...
    def GetTakeSamplingRateMode(self,TakeIndex:int)->FBTimeMode:
        """Return the sampling rate mode.
        ### Parameters:
        - TakeIndex: Index of take to get the sampling rate mode
        
        ### Returns:
        Sample rate mode
        
        ### Remarks:
        Use GetTakeSamplingRate if you have a custom sampling rate to get the actual rate."""
        ...
    def GetTakeSelect(self,TakeIndex:int)->bool:
        """Return true if the take will be loaded.
        ### Parameters:
        - TakeIndex: Index of take.
        
        ### Returns:
        True is the take will be loaded"""
        ...
    def GetTakeStart(self,TakeIndex:int)->FBTime:
        """Return the Take Start time.
        ### Parameters:
        - TakeIndex: Index of take to get the start time.
        
        ### Returns:
        Start time of the take"""
        ...
    def GetTakeStop(self,TakeIndex:int)->FBTime:
        """Return the Take Stop time.
        ### Parameters:
        - TakeIndex: Index of take to get the stop time.
        
        ### Returns:
        Stop time of the take"""
        ...
    def SetTakeName(self,TakeIndex:int,Name:str):
        """Set the take name.
        ### Parameters:
        - TakeIndex: Index of take to set.
        - Name: Take name to set"""
        ...
    def SetTakeSamples(self,TakeIndex:int,SamplesCount:int):
        """Set the number of samples for a particular take.
        ### Parameters:
        - TakeIndex: Index of take to set.
        - SamplesCount: Number of samples
        
        ### Remarks:
        Must be set to a value bigger than 0 and smaller than the number of samples in the file. The stop time of the motion will be changed based on the new samples count."""
        ...
    def SetTakeSamplingRate(self,TakeIndex:int,TimeMode:FBTimeMode,CustomSamplingRate:float=30.0):
        """Set the sampling rate for a particular take.
        ### Parameters:
        - TakeIndex: Index of take to set.
        - TimeMode: Time mode to set.
        - CustomSamplingRate: Custom sampling rate if TimeMode is set to kFBTimeModeCustom, unused otherwise (default is 30.0)
        
        ### Remarks:
        Changing the sampling rate will change the stop time of the motion."""
        ...
    def SetTakeSelect(self,TakeIndex:int,bSelect:bool):
        """Indicate if the take will be loaded.
        ### Parameters:
        - TakeIndex: Index of take to set.
        - bSelect: Set to true if the take should be loaded."""
        ...
    def SetTakeStart(self,TakeIndex:int,StartTime:FBTime):
        """Set the Take Start time.
        ### Parameters:
        - TakeIndex: Index of take to set.
        - StartTime: Time of the first frame of the take
        
        ### Remarks:
        Changing the start time of the take will also change the stop time, since the duration is constant. Please change the samples count to change the length of the motion."""
        ...
    def SetTakeStop(self,TakeIndex:int,StopTime:FBTime):
        """Set the Take Stop time.
        ### Parameters:
        - TakeIndex: Index of take to set.
        - StopTime: Time of the last frame of the take
        
        ### Remarks:
        Changing the stop time of the take will also change the start time, since the duration is constant. Please change the samples count to change the length of the motion."""
        ...
    def __init__(self,StringList:FBStringList):
        """Create a FBMotionFileOptions to be used when importing a motion file. Pass file paths to get the appropriate information about those files, modify the options and then call the file import process. Not all options are usable at the same time, some of them are for specific motion type. You can see the valid configuration by looking at the motion file dialog (accessible from File/Motion File Import...).
        ### Parameters:
        - StringList: The client needs to pass a list of files path to load to collect the motion file information."""
        ...
class FBNamespace(FBComponent):
    ChildrenNamespaces:FBPropertyListNamespace
    ContentCount:property
    ContentLocked:bool
    def GetContent(self,Index:int)->FBComponent:
        """Get the namespace content object count (Not Recursive).
        ### Parameters:
        - Index: content object index to query. return content object inside this namespace (not recursive)"""
        ...
    def GetContentCount(self)->int:
        """Get the namespace content objects count (Not Recursive).
        return content objects count inside this namespace (not recursive)"""
        ...
    def GetContentList(self,ContentList:FBComponentList,ModificationFlags:FBPlugModificationFlag=FBPlugModificationFlag.kFBPlugAllContent,bRecursive:bool=True,TypeInfo:int=FBPlug.TypeInfo,bExactTypeMatch:bool=False):
        """Get List of the namespace content.
        ### Parameters:
        - ContentList: the list of content to return.
        - ModificationFlags: bitwise combination of kFBConnectionSrcObjectModified, kFBConnectionDstObjectModified, kFBConnectionSrcPropertyModified, kFBConnectionDstPropertyModified flags. kFBAllContent means all the content.
        - bRecursive: True only work on the direct children level namespace, otherwise will work on the whole children namespace hierarchy recursively.
        - TypeInfo: the typeInfo of the type of interested object, 0 for all the objects.
        - bExactTypeMatch: if True , the derived typeInfo won't be considered (For example, FBCamera won't be considered when passing FBModel::TypeInfo )."""
        ...
    def __init__(self,MultiLevelNamespace:str,Object:FBNamespace):
        """For Internal use only.
        ### Parameters:
        - MultiLevelNamespace: FBNamespace name. This name will be used as namespace itself. it should follow such pattern "NS1[:NS2[:NS3]]]", where content inside [] is optional.
        - Object: For internal use only."""
        ...
class FBOpticalGap(FBComponent):
    Data:FBAnimationNode
    Interpolation:FBGapMode
    TimeSpan:FBTimeSpan
    def InsertControlKey(self,Time:FBTime):
        """Insert a control key for the gap.
        ### Parameters:
        - Time: Insert time for the control key."""
        ...
    def IsValid(self)->bool:
        """Check if valid (if item exists).
        ### Returns:
        true if segment is valid."""
        ...
    def __init__(self,Marker:FBModelMarkerOptical):
        """### Parameters:
        - Marker: Model marker(default=NULL)."""
        ...
class FBFileReference(FBNamespace):
    IsLoaded:bool
    ReferenceFilePath:str
    def ApplyRefEditPyScriptFromFile(self,RefEditPyScriptFilePath:str):
        """Apply specified reference edits from python script file.
        ### Parameters:
        - RefEditPyScriptFilePath: Reference edits Python script file path."""
        ...
    def ApplyRefEditPyScriptFromString(self,RefEditPyScript:str):
        """Apply specified reference edits from Python script string.
        ### Parameters:
        - RefEditPyScript: Reference edits Python script."""
        ...
    def BakeRefEditToFile(self,FilePath:str)->bool:
        """Save the current status of the referenced content back to disk.
        If FilePath is ReferenceFilePath, we're saving all the modification back to the original referenced file. Otherwise, we will export the referenced file plus modification to another file.
        ### Parameters:
        - FilePath: File path to export.
        
        ### Returns:
        true if successful."""
        ...
    def ClearAllRefEdit(self)->bool:
        """Clear all cached Ref edit.
        ### Returns:
        True if the RefEdits are cleared properly."""
        ...
    def ClearRefEdit(self,FilePath:str)->bool:
        """Clear the cached RefEdit for the given ref file path.
        ### Parameters:
        - FilePath: The Ref File Path to query against, default to be current Ref File.
        
        ### Returns:
        True if the RefEdit for the given Ref File Path is cached and cleared properly."""
        ...
    def DuplicateFileRef(self,DstNameSpaceList:FBStringList,bWithRefEdit:bool=False)->bool:
        """Duplicate/Clone the FileRef object and its referenced content (with/without refEdit).
        ### Parameters:
        - DstNameSpaceList: the list of target new namespace(s) for duplication. These new namespace(s) must be residing in editable scene segments.
        - bWithRefEdit: false by default, duplication won't include the existing ref edit. otherwise ref edit will be applied on the instantiated FileRef in someway.
        
        ### Returns:
        true if successful, false is fail."""
        ...
    def GetRefEdit(self,FilePath:str=None)->str:
        """Return the RefEdit for given RefFile Path.
        ### Parameters:
        - FilePath: The Ref File Path to query against, default to be current Ref File.
        
        ### Returns:
        RefEdit as string"""
        ...
    def GetRefFileList(self,RefFileList:FBStringList):
        """Return a list of ref file path which has cached Ref Edit.
        ### Parameters:
        - RefFileList: the output parameter to collect the Ref File Path."""
        ...
    def RevertRefEdit(self,Plug:FBPlug=None,ModificationFlag:FBPlugModificationFlag=FBPlugModificationFlag.kFBAllModifiedMask):
        """Revert the modification on the referenced object/property to original state.
        ### Parameters:
        - Plug: the plug to revert, revert all if NULL.
        - ModificationFlag: the modification type to revert."""
        ...
    def SwapReferenceFilePath(self,FilePath:str,bApplyAvailableRefEdit:bool,bMergeCurrentRefEdit:bool)->bool:
        """Swap the Ref File Path and apply ref edit.
        ### Parameters:
        - FilePath: The new Ref File path to be used
        - bApplyAvailableRefEdit: Apply the cached Ref Edit (if exist) for the Ref File to be used if True .
        - bMergeCurrentRefEdit: Merge the current RefEdit to if True if the reference items' name are matching.
        
        ### Returns:
        True if swap successfully."""
        ...
    def __init__(self,MultiLevelNamespace:str,Object:FBNamespace):
        """For internal use only.
        ### Parameters:
        - MultiLevelNamespace: FileReference name. This name will be used as namespace itself. it should follow such pattern "NS1[:NS2[:NS3]]]", where content inside [] is optional
        - Object: For internal use only."""
        ...
class FBOpticalSegment(FBComponent):
    Data:FBAnimationNode
    Marker:FBModelMarkerOptical
    MarkerTimeSpan:FBTimeSpan
    OriginalTimeSpan:FBTimeSpan
    TimeSpan:FBTimeSpan
    Used:bool
    def Cut(self,Time:FBTime):
        """Cut the segment for the marker at a given time.
        ### Parameters:
        - Time: Time to cut segment at."""
        ...
    def IsValid(self)->bool:
        """Check if valid (if item exists).
        ### Returns:
        true if segment is valid."""
        ...
    def Reset(self):
        """Reset the marker segment."""
        ...
    def __init__(self,Optical:FBModelOptical):
        """### Parameters:
        - Optical: Optical model(default=NULL)."""
        ...
class FBPlayerControl(FBComponent):
    IsPlaying:bool
    IsPlotting:bool
    IsRecording:bool
    LoopActive:bool
    LoopMode:FBTransportLoopMode
    LoopStart:FBTime
    LoopStop:FBTime
    NextMarker:FBTime
    OnChange:FBEvent
    PlotSamplingPeriod:FBTime
    PreviousMarker:FBTime
    RecordingSamplingPeriod:FBTime
    SnapMode:FBTransportSnapMode
    TransportTimeFormat:FBTransportTimeFormat
    ZoomWindowStart:FBTime
    ZoomWindowStop:FBTime
    def AddGlobalTimeMark(self,Time:FBTime)->int:
        """Add a global time mark.
        It doesn't allow creating a time mark at the same time of another time mark. Note: Internally, the global time marks are stored in time order. Adding a time mark before other existing time marks will modify the index of these other time marks.
        ### Parameters:
        - Time: Time where to add the time mark.
        ### Returns:
        The index of the time mark added if the operation is successful, -1 otherwise."""
        ...
    def DeleteAllGlobalTimeMarks(self):
        """Delete all global time marks."""
        ...
    def DeleteGlobalTimeMark(self,Index:int)->bool:
        """Delete a global time mark.
        Note: Internally, the global time marks are stored in time order. Deleting a time mark will modify the index of time marks laying after the deleted time mark.
        ### Parameters:
        - Index: Index of the time mark to delete.
        
        ### Returns:
        True if the operation is successful, false otherwise."""
        ...
    def EvaluationPause(self):
        """Pause device evaluation thread."""
        ...
    def EvaluationResume(self):
        """Resume device evaluation thread."""
        ...
    def GetEditCurrentTime(self)->FBTime:
        """Get Edit Current Time.
        ### Returns:
        The current time, in the edit time referential."""
        ...
    def GetEditStart(self)->FBTime:
        """Get Edit Start.
        ### Returns:
        Start value for the edit time range."""
        ...
    def GetEditStop(self)->FBTime:
        """Get Edit Stop.
        ### Returns:
        Stop value for the edit time range."""
        ...
    def GetEditZoomStart(self)->FBTime:
        """Get Edit Zoom Start.
        ### Returns:
        Start value for the edit zoom window."""
        ...
    def GetEditZoomStop(self)->FBTime:
        """Get Edit Zoom Stop.
        ### Returns:
        Stop value for the edit zoom window."""
        ...
    def GetGlobalTimeMarkAction(self,Index:int)->FBTimeMarkAction:
        """Returns the action associated with a global time mark.
        ### Parameters:
        - Index: Index of the time mark.
        
        ### Returns:
        The action associated with the time mark."""
        ...
    def GetGlobalTimeMarkColor(self,Index:int)->FBColor:
        """Returns the color associated with a global time mark.
        ### Parameters:
        - Index: Index of the time mark.
        
        ### Returns:
        The color associated with the time mark."""
        ...
    def GetGlobalTimeMarkCount(self)->int:
        """Returns the number of global time marks.
        ### Returns:
        The number of global time marks."""
        ...
    def GetGlobalTimeMarkName(self,Index:int)->str:
        """Returns the name associated with a global time mark.
        ### Parameters:
        - Index: Index of the time mark.
        
        ### Returns:
        The name associated with the time mark."""
        ...
    def GetGlobalTimeMarkTime(self,Index:int)->FBTime:
        """Returns the time associated with a global time mark.
        ### Parameters:
        - Index: Index of the time mark.
        
        ### Returns:
        The time associated with the time mark."""
        ...
    def GetNextGlobalTimeMarkIndex(self)->int:
        """Returns the next global time mark index, based on the current local time.
        ### Returns:
        The next global time mark index, -1 if any next time mark is available."""
        ...
    def GetPlaySpeed(self)->float:
        """Get Play Speed .
        ### Returns:
        transport current playback speed."""
        ...
    def GetPlaySpeedMode(self)->FBTransportPlaySpeed:
        """Get Play Speed Mode.
        ### Returns:
        transport current playback speed mode, including kFBSpeed_Custom mode."""
        ...
    def GetPreviousGlobalTimeMarkIndex(self)->int:
        """Returns the previous global time mark index, based on the current local time.
        ### Returns:
        The previous global time mark index, -1 if any previous time mark is available."""
        ...
    def GetTimeReferential(self)->FBTimeReferential:
        """Get Time Referential.
        ### Returns:
        Current time referential."""
        ...
    def GetTransportFps(self)->FBTimeMode:
        """Get the UI frame rate use for display configure in the system.
        ### Returns:
        current FrameRate selected for the system."""
        ...
    def GetTransportFpsValue(self,TimeMode:FBTimeMode=FBTimeMode.kFBTimeModeDefault)->float:
        """Get the UI frame rate value.
        ### Parameters:
        - TimeMode: the time mode whose frame rate will be returned
        
        ### Returns:
        Frame rate of the input time mode or system time mode when TimeMode is not provided."""
        ...
    def GetTransportMode(self)->FBTransportMode:
        """Get Transport Mode.
        ### Returns:
        Current mode of the transport controls."""
        ...
    def Goto(self,Time:FBTime,arg3:FBTimeReferential=None)->bool:
        """Goto a time specified by Time .
        ### Parameters:
        - Time: Time to jump to.
        
        ### Returns:
        true if successful."""
        ...
    def GotoEnd(self,arg2:FBTimeReferential=None)->bool:
        """GotoEnd button (FastForward).
        ### Returns:
        true if successful."""
        ...
    def GotoNextKey(self):
        """Go to the next key."""
        ...
    def GotoPreviousKey(self):
        """Go to the previous key."""
        ...
    def GotoStart(self,arg2:FBTimeReferential=None)->bool:
        """GotoStart button (Rewind).
        ### Returns:
        true if successful."""
        ...
    def IsLocked(self)->bool:
        """Return the current locking state of the transport."""
        ...
    def Key(self):
        """Key default data.
        Key all selected data."""
        ...
    def LockTransport(self,bLock:bool):
        """Lock the transport control.
        ### Parameters:
        - bLock: boolean value that indicates the new locked state of the transport."""
        ...
    def Play(self,bUseMarkers:bool=False)->bool:
        """Play button.
        ### Parameters:
        - bUseMarkers: Play until next marker if true, ignore markers otherwise.
        
        ### Returns:
        true if successful."""
        ...
    def PlayReverse(self,bUseMarkers:bool=False)->bool:
        """Play Reverse button.
        ### Parameters:
        - bUseMarkers: Play until next marker if true, ignore markers otherwise.
        
        ### Returns:
        true if successful."""
        ...
    def Record(self,bOverrideTake:bool=False,bCopyData:bool=True)->bool:
        """Begin recording.
        ### Parameters:
        - bOverrideTake: Write over current take?(default=false)
        - bCopyData: Unused. Necessary for compatibility(default=true).
        
        ### Returns:
        true if successful."""
        ...
    def SetEditStart(self,Time:FBTime):
        """Set Edit Start.
        ### Parameters:
        - Time: The new start value for the edit time range."""
        ...
    def SetEditStop(self,Time:FBTime):
        """Set Edit Stop.
        ### Parameters:
        - Time: The new stop value for the edit time range."""
        ...
    def SetEditZoomStart(self,Time:FBTime):
        """Set Edit Zoom Start.
        ### Parameters:
        - Time: The new start value for the edit zoom window."""
        ...
    def SetEditZoomStop(self,Time:FBTime):
        """Set Edit Zoom Stop.
        ### Parameters:
        - Time: The new stop value for the edit zoom window."""
        ...
    def SetGlobalTimeMarkAction(self,Index:int,Action:FBTimeMarkAction)->bool:
        """Sets a new action for an existing global time mark.
        ### Parameters:
        - Index: Index of the time mark.
        - Action: The new action for the time mark.
        
        ### Returns:
        True if the operation is successful, false otherwise."""
        ...
    def SetGlobalTimeMarkColor(self,Index:int,Color:FBColor)->bool:
        """Sets a new color for an existing global time mark.
        ### Parameters:
        - Index: Index of the time mark.
        - Color: The new color for the time mark.
        
        ### Returns:
        True if the operation is successful, false otherwise."""
        ...
    def SetGlobalTimeMarkName(self,Index:int,Name:str)->bool:
        """Sets a new name for an existing global time mark.
        ### Parameters:
        - Index: Index of the time mark.
        - Name: The new name for the time mark.
        
        ### Returns:
        True if the operation is successful, false otherwise."""
        ...
    def SetGlobalTimeMarkTime(self,Index:int,Time:FBTime)->int:
        """Sets a new time for an existing global time mark.
        Note: Internally, the global time marks are stored in time order. Modifying the time of a time mark may modify the index of all time marks.
        ### Parameters:
        - Index: Index of the time mark.
        - Time: The new time for the time mark.
        
        ### Returns:
        The new index of the modified time mark."""
        ...
    def SetPlaySpeed(self,Speed:float):
        """Set Play Speed.
        ### Parameters:
        - pPlaySpeed: set customized speed. It will automatically convert to one of pre-defined play speed mode if it is equal to the pre-defined speed."""
        ...
    def SetPlaySpeedMode(self,PlaySpeedMode:FBTransportPlaySpeed):
        """Set Play Speed Mode.
        ### Parameters:
        - PlaySpeedMode: a pre-defined play speed mode. Don't make sense to input kFBSpeed_Custom. To set the custom speed, use SetPlaySpeed() function directly."""
        ...
    def SetTimeReferential(self,TimeReferential:FBTimeReferential):
        """Set Time Referential.
        ### Parameters:
        - TimeReferential: The new time referential. Only kFBTimeReferentialAction and kFBTimeReferentialEdit are supported"""
        ...
    def SetTransportFps(self,TimeMode:FBTimeMode,Custom:float=0.0):
        """Set the system frame rate use for display.
        ### Parameters:
        - TimeMode: Indicate the frame rate value to use base on the FBTimeMode values enum.(kFBTimeModeDefault will be stored in fps)
        - Custom: Should the time mode be kFBTimeModeCustom, this is used to specify the custom framerate."""
        ...
    def StepBackward(self,arg2:FBTimeReferential=None)->bool:
        """Step one frame backward.
        ### Returns:
        true if successful."""
        ...
    def StepForward(self,arg2:FBTimeReferential=None)->bool:
        """Step one frame ahead.
        ### Returns:
        true if successful."""
        ...
    def Stop(self)->bool:
        """Stop button.
        ### Returns:
        true if successful."""
        ...
    def __init__(self):...
class FBPointCacheFile(FBComponent):
    CacheFileName:str
    ChannelCount:int
    FreeRunning:bool
    Loop:bool
    Offset:FBTime
    PlaySpeed:float
    StartTime:FBTime
    StopTime:FBTime
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of Point Cache File Object."""
        ...
class FBRendererCallback(FBComponent):
    DefaultCameraBackPlateRendering:bool
    DefaultCameraFrontPlateRendering:bool
    DefaultLightGroundProjectionRendering:bool
    DefaultLightVolumeRendering:bool
    SupportIDBufferPicking:bool
    def __init__(self,Name:str):...
class FBRigidBody(FBComponent):
    Done:bool
    Markers:FBPropertyListRigidBodyMarkers
    Mode:FBRigidBodyMode
    Model:FBModel
    QualityData:FBAnimationNode
    SmoothWidth:int
    def ComputeAnimation(self):
        """Compute the rigid body animation."""
        ...
    def IsValid(self)->bool:
        """Check if valid (if item exists).
        ### Returns:
        true if segment is valid."""
        ...
    def Snap(self):
        """Snap the rigid body."""
        ...
    def __init__(self,Optical:FBModelOptical):
        """### Parameters:
        - Optical: Optical model(default=NULL)."""
        ...
class FBSVector():
    @overload
    def CopyFrom(self,arg2:FBSVector)->FBSVector:...
    @overload
    def CopyFrom(self,arg2:list)->FBSVector:...
    def DotProduct(self,arg2:FBSVector)->float:...
    def GetList(self)->list:...
    def IsEqual(self,arg2:FBSVector)->bool:...
    def Length(self)->float:
        """Get the length of a vector.
        ### Returns:
        Length of vector pV ."""
        ...
    def Normalize(self)->FBSVector:...
    def NotEqual(self,arg2:FBSVector)->bool:...
    def SquareLength(self)->float:...
    @overload
    def __add__(self,arg2:FBSVector)->object:...
    @overload
    def __add__(self,arg2)->object:...
    def __getitem__(self,arg2)->float:...
    @overload
    def __iadd__(self,arg2:FBSVector)->object:...
    @overload
    def __iadd__(self,arg2)->object:...
    @overload
    def __idiv__(self,arg2:FBSVector)->object:...
    @overload
    def __idiv__(self,arg2)->object:...
    @overload
    def __imul__(self,arg2:FBSVector)->object:...
    @overload
    def __imul__(self,arg2)->object:...
    @overload
    def __init__(self):...
    @overload
    def __init__(self,Value:FBSVector):
        """Constructor from array.
        ### Parameters:
        - Value: Array to take values from."""
        ...
    @overload
    def __init__(self,p1:float,p2:float,p3:float):
        """### Parameters:
        - p1: First element
        - p2: Second element.
        - p3: Third element(default=1.0)."""
        ...
    @overload
    def __init__(self,arg2):...
    @overload
    def __init__(self,arg2:list):...
    @overload
    def __isub__(self,arg2:FBSVector)->object:...
    @overload
    def __isub__(self,arg2)->object:...
    def __len__(self)->int:...
    @overload
    def __mul__(self,arg2:FBSVector)->object:...
    @overload
    def __mul__(self,arg2)->object:...
    def __neg__(self)->object:...
    def __setitem__(self,arg2,arg3):...
    @overload
    def __sub__(self,arg2:FBSVector)->object:...
    @overload
    def __sub__(self,arg2)->object:...
    @overload
    def __truediv__(self,arg2:FBSVector)->object:...
    @overload
    def __truediv__(self,arg2)->object:...
class FBScene(FBComponent):
    ActorFaces:FBPropertyListActorFace
    Actors:FBPropertyListActor
    AudioClips:FBPropertyListAudioClip
    Cameras:FBPropertyListCamera
    CharacterExtensions:FBPropertyListCharacterExtension
    CharacterFaces:FBPropertyListCharacterFace
    CharacterMarkerSets:FBPropertyListCharacterMarkerSet
    CharacterPoses:FBPropertyListCharacterPose
    Characters:FBPropertyListCharacter
    ConstraintSolvers:FBPropertyListConstraintSolver
    Constraints:FBPropertyListConstraint
    ControlSets:FBPropertyListControlSet
    Deformers:FBPropertyListDeformer
    Devices:FBPropertyListDevice
    FileReferences:FBPropertyListFileReference
    Folders:FBPropertyListFolder
    Groups:FBPropertyListGroup
    HUDs:FBPropertyListHUD
    Handles:FBPropertyListHandle
    KeyingGroups:FBPropertyListKeyingGroup
    Lights:FBPropertyListLight
    MarkerSets:FBPropertyListMarkerSet
    Materials:FBPropertyListMaterial
    ModelOpticals:FBPropertyListModelOptical
    ModelSkeletons:FBPropertyListModelSkeleton
    MotionClips:FBPropertyListMotionClip
    Namespaces:FBPropertyListNamespace
    Notes:FBPropertyListNote
    ObjectPoses:FBPropertyListObjectPose
    OnChange:FBEvent
    OnTakeChange:FBEvent
    PhysicalProperties:FBPropertyListPhysicalProperties
    Poses:FBPropertyListPose
    Renderer:FBRenderer
    RootModel:FBModel
    Sets:FBPropertyListSet
    Shaders:FBPropertyListShader
    Takes:FBPropertyListTake
    Textures:FBPropertyListTexture
    UserObjects:FBPropertyListUserObject
    VideoClips:FBPropertyListVideoClip
    def CandidateEvaluationAndResolve(self)->bool:
        """Resolving the Candidate.
        ### Returns:
        true if successful."""
        ...
    def CleanEmptyGroups(self)->int:
        """Remove all empty groups present in the scene.
        ### Returns:
        The number of empty groups removed."""
        ...
    def CleanEmptyRelationConstraints(self)->int:
        """Remove all empty relation constraints present in the scene.
        ### Returns:
        The number of empty relation constraints removed."""
        ...
    def CleanEmptySets(self)->int:
        """Remove all empty sets present in the scene.
        ### Returns:
        The number of empty sets removed."""
        ...
    def CleanInactiveConstraints(self)->int:
        """Remove all inactive constraints present in the scene.
        ### Returns:
        The number of inactive constraints removed."""
        ...
    def CleanRelationConstraintsUnusedBoxes(self)->int:
        """Remove all unused boxes in relations constraints present in the scene.
        ### Returns:
        The number of unused boxes in relations constraints removed."""
        ...
    def CleanUnusedAudioClips(self)->int:
        """Remove all unused audio clips present in the scene.
        ### Returns:
        The number of unused audio clips removed."""
        ...
    def CleanUnusedMaterials(self)->int:
        """Remove all unused materials present in the scene.
        ### Returns:
        The number of unused material removed."""
        ...
    def CleanUnusedShaders(self)->int:
        """Remove all unused shaders present in the scene.
        ### Returns:
        The number of unused shaders removed."""
        ...
    def CleanUnusedTextures(self)->int:
        """Remove all unused textures present in the scene.
        ### Returns:
        The number of unused textures removed."""
        ...
    def CleanUnusedVideoClips(self)->int:
        """Remove all unused video clips present in the scene.
        ### Returns:
        The number of unused video clips removed."""
        ...
    def Clear(self):
        """Clears the elements part of the scene.
        Not those that belong to all the scenes."""
        ...
    def Evaluate(self)->bool:
        """Evaluate the scene.
        ### Note:
        MoBu's is highly optimized for real-time performance, due to its multi-thread, double buffer and lazy-evaluation architecture, complex scripts are often required to call FBScene::Evaluate() to commit previous scene change commands before execute following operations. Also, certain operations in SDK may require cached data to be reevaluated. In typical large scenes this call may be consider as very costly. That's why user is responsible to design code in the way that requires as little as possible calls to FBScene::Evaluate . We should consider use FBScene::Evaluate() between scene change commands as "common scripting practice
        
        ### Returns:
        true if successful."""
        ...
    def EvaluateDeformations(self)->bool:
        """Evaluate the deformations of the scene.
        ### Returns:
        true if successful."""
        ...
    def GetScriptsPaths(self)->FBStringList:
        """Get paths of all the python scripts object in the scene."""
        ...
    def NamespaceCleanup(self)->bool:
        """Remove all empty namespaces.
        During some namespace operations, empty namespace may left over, while this is not harmful but could be annoying. Save the scene and load it back those empty namespaces will disappear. And this function also allow user to remove all empty namespaces from the scene easily via SDK.
        ### Returns:
        True if operation successfully."""
        ...
    def NamespaceDelete(self,Namespace:str)->bool:
        """Delete the namespace & all its content.
        ### Parameters:
        - Namespace: the namespace to work on
        
        ### Returns:
        True if operation successfully, False is this namespace doesn't exist, or is locked (by FileReferencing or etc.,)"""
        ...
    def NamespaceDeleteContent(self,Namespace:str,ModificationFlags:FBPlugModificationFlag=FBPlugModificationFlag.kFBPlugAllContent,bRecursive:bool=True,TypeInfo:int=FBPlug.TypeInfo,bExactTypeMatch:bool=False)->bool:
        """Delete the namespace content.
        ### Parameters:
        - Namespace: the namespace to work on
        - ModificationFlags: bitwise combination of kFBConnectionSrcObjectModified, kFBConnectionDstObjectModified, kFBConnectionSrcPropertyModified, kFBConnectionDstPropertyModified flags. kFBPlugAllContent means all the content. Modification flags beside kFBPlugAllContent will only work on FileReference Namespace.
        - bRecursive: True only work on the direct children level namespace, otherwise will work on the children namespace hierarchy recursively.
        - TypeInfo: the typeInfo of the type of interested object, default for all the objects.
        - bExactTypeMatch: if True , the derived typeInfo won't be considered (For example, FBCamera won't be considered when passing FBModel::TypeInfo ).
        
        ### Returns:
        False is the given namespace doesn't exist, or is locked (by FileRef or etc.,), True otherwise.
        
        ### Note:
        Not all the objects will be deletable (system objects and etc.,). Deletion of partial FileRef content isn't prevented, however the behavior is undefined."""
        ...
    def NamespaceEmpty(self,Namespace:str)->bool:
        """Query if namespace is empty.
        ### Parameters:
        - Namespace: the namespace to query, `None` for whole scene.
        
        ### Returns:
        True if the namespace (don't include nested children namespace) is empty"""
        ...
    def NamespaceExist(self,Namespace:str)->bool:
        """Query if namespace exists.
        ### Parameters:
        - Namespace: the namespace to query
        
        ### Returns:
        True if the namespace exist, otherwise return False ."""
        ...
    def NamespaceExport(self,Namespace:str,FilePath:str,bASCIIFormat:bool=False)->bool:
        """Export scene content within namespace to file.
        ### Parameters:
        - Namespace: the namespace to use, must exist
        - FilePath: the referenced file path to export.
        - bASCIIFormat: save the file in ASCII format.
        
        ### Returns:
        True if successfully."""
        ...
    def NamespaceGet(self,Namespace:str)->FBNamespace:
        """Get Namespace object.
        ### Parameters:
        - Namespace: the namespace to query
        
        ### Returns:
        Namespace with exact name matching"""
        ...
    def NamespaceGetChildrenList(self,NamespaceList:FBStringList,Namespace:str=None,bRecursive:bool=True)->int:
        """Get list of children namespaces in the given namespace.
        ### Parameters:
        - NamespaceList: the list of namespace to return.
        - Namespace: specify the parent namespace, `None` for the whole scene.
        - bRecursive: True only work on the direct children level namespace, otherwise will work on the whole children namespace hierarchy recursively.
        
        ### Returns:
        the list of children namespaces."""
        ...
    def NamespaceGetContentList(self,ContentList:FBComponentList,Namespace:str,ModificationFlags:FBPlugModificationFlag=FBPlugModificationFlag.kFBPlugAllContent,bRecursive:bool=True,TypeInfo:int=FBPlug.TypeInfo,bExactTypeMatch:bool=False):
        """Get List of the namespace content.
        ### Parameters:
        - ContentList: the list of content to return.
        - Namespace: the namespace to work on, `None` for whole scene.
        - ModificationFlags: bitwise combination of kFBConnectionSrcObjectModified, kFBConnectionDstObjectModified, kFBConnectionSrcPropertyModified, kFBConnectionDstPropertyModified flags. kFBPlugAllContent means all the content. Modification flags beside kFBPlugAllContent will only work on FileReference Namespace.
        - bRecursive: True only work on the direct children level namespace, otherwise will work on the whole children namespace hierarchy recursively.
        - TypeInfo: the typeInfo of the type of interested object, 0 for all the objects.
        - bExactTypeMatch: if True , the derived typeInfo won't be considered (For example, FBCamera won't be considered when passing FBModel::TypeInfo )."""
        ...
    def NamespaceGetOwnerFileReference(self,Namespace:str)->FBFileReference:
        """Get Owner FileReference object if the namespace is originated from File Reference.
        ### Parameters:
        - Namespace: the namespace to work on, could be nested namespace inside the FileReference's namespace.
        
        ### Returns:
        the FileReference object is the namespace is originated from. `None` otherwise."""
        ...
    def NamespaceImport(self,Namespace:str,FilePath:str,bAsFileReference:bool=False)->bool:
        """Import file into Namespace (or as file reference)
        ### Parameters:
        - Namespace: the namespace to import to, must be in editable scope.
        - FilePath: the referenced file path to import.
        - bAsFileReference: import the file as file reference. The default value is false.
        
        ### Returns:
        True if successfully."""
        ...
    def NamespaceImportToMultiple(self,DstNamespaceList:FBStringList,FilePath:str,bAsFileReference:bool=False)->bool:
        """Import file into multiple Namespaces (or as file references)
        ### Parameters:
        - DstNamespaceList: the Dst namespaces list to import, must not exist or be self contained.
        - FilePath: the referenced file path to import.
        - bAsFileReference: import the file as file reference. The default value is false.
        
        ### Returns:
        True if successfully.
        
        ### Note:
        Nested destination namespaces are not allowed (e.g. a DstNamespaceList contains "NS1" and "NS1:NS2" will return False)."""
        ...
    def NamespaceRename(self,NameSpace:str,NewNamespace:str,bRecursive:bool=True,TypeInfo:int=FBPlug.TypeInfo,bExactTypeMatch:bool=False)->bool:
        """Rename the namespace.
        ### Parameters:
        - NameSpace: the namespace to work on, `None` for whole scene.
        - NewNamespace: the new namespace
        - bRecursive: True only work on the direct children level namespace, otherwise will work on the children namespace hierarchy recursively.
        - TypeInfo: the typeInfo of the type of interested object, default for all the objects.
        - bExactTypeMatch: if True , the derived typeInfo won't be considered (For example, FBCamera won't be considered when passing FBModel::TypeInfo ).
        
        ### Returns:
        True if operation successfully, False is this namespace (or TypeInfo type of objects) doesn't exist, or locked (by FileReferencing or etc.,)
        
        ### Note:
        call with default parameters is considered as renaming of the whole namespace structure, otherwise will be considered as partially renaming individual objects. Renaming permission will be validated accordingly."""
        ...
    def NamespaceSelectContent(self,Namespace:str,bSelect:bool,ModificationFlags:FBPlugModificationFlag=FBPlugModificationFlag.kFBPlugAllContent,bRecursive:bool=True,TypeInfo:int=FBPlug.TypeInfo,bExactTypeMatch:bool=False):
        """Select (or de-select) the namespace content.
        ### Parameters:
        - Namespace: the namespace to work on, `None` for whole scene.
        - bSelect: True (or False ) indicate to select (or de-select)
        - ModificationFlags: bitwise combination of kFBConnectionSrcObjectModified, kFBConnectionDstObjectModified, kFBConnectionSrcPropertyModified, kFBConnectionDstPropertyModified flags. kFBPlugAllContent means all the content. Modification flags beside kFBPlugAllContent will only work on FileReference Namespace.
        - bRecursive: True only work on the direct children level namespace, otherwise will work on the children namespace hierarchy recursively.
        - TypeInfo: the typeInfo of the type of interested object, default for all the objects.
        - bExactTypeMatch: if True , the derived typeInfo won't be considered (For example, FBCamera won't be considered when passing FBModel::TypeInfo )."""
        ...
class FBSet(FBBox):
    Items:FBPropertyListComponent
    Pickable:bool
    Transformable:bool
    Visibility:bool
    def Contains(self,Component:FBComponent)->int:
        """### Parameters:
        - Component: Component to verify if it is in the Group
        
        ### Returns:
        0 if the component is not in the FBSet , 1 if it is in this FBSet , 2 if it is in another FBSet"""
        ...
    def Select(self,bSelect:bool):
        """### Parameters:
        - bSelect: If true , set contents will be selected."""
        ...
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Set name."""
        ...
class FBShader(FBBox):
    RenderingPass:FBRenderingPass
    ShaderDescription:str
    def Append(self,Model:FBModel)->bool:
        """Append shader to Model .
        ### Parameters:
        - Model: Model to append shader to.
        
        ### Returns:
        True if the operation is successful, false otherwise."""
        ...
    def CloneShaderParameter(self,NewShader:FBShader):
        """Clone shader.
        ### Parameters:
        - NewShader: Shader to copy data to."""
        ...
    def ReplaceAll(self,Model:FBModel)->bool:
        """Replace all shader in Model .
        ### Parameters:
        - Model: Model to replace all shader to.
        
        ### Returns:
        True if the operation is successful, false otherwise."""
        ...
    def ShaderNeedBeginRender(self)->bool:
        """Does the shader need a begin render call.
        ### Remarks:
        Re-implement this function and return true if you need it. This method is called once per shader on each render pass."""
        ...
class FBShaderLighted(FBShader):
    Alpha:float
    Contrast:float
    Luminosity:float
    Specular:float
    Transparency:FBAlphaSource
    UseContrast:bool
    UseLuminosity:bool
    UseSpecular:bool
    def __init__(self,Name:str=None):
        """### Parameters:
        - Name: Name of shader."""
        ...
class FBShaderManager():
    ShaderTypeNames:FBStringList
    ShaderTypeNamesLocalized:FBStringList
    def CreateShader(self,ShaderTypeName:str)->FBShader:
        """Creates a shader according to the shader type provided.
        This method provides a generic way of creating shaders using the type name, internal or localized. The name of the new shader will be the same as the type name used, subject to changes according to the system's unique name policy.
        ### Parameters:
        - ShaderTypeName: Name of the type of shader desired.
        
        ### Returns:
        A pointer to the newly created shader object, or a NULL pointer if the type name was not recognised."""
        ...
    def __init__(self):...
class FBShaderModelInfo():
    Model:property
    Model_Version:property
    Shader_Version:property
class FBShaderShadowLive(FBShader):
    Lights:FBPropertyListObject
    LocalShadow:bool
    Models:FBPropertyListObject
    ShadowFrameType:FBShadowFrameType
    ShadowIntensity:float
    ShadowType:FBShadowType
    ShadowZOffset:float
    UseGobo:bool
    def __init__(self,Name:str=None):
        """### Parameters:
        - Name: Name of shader."""
        ...
class FBSkeletonState():
    def GetNodeMatrix(self,arg2:FBSkeletonNodeId,arg3:FBMatrix):...
class FBSpreadPart(FBComponent):
    Column:int
    Enabled:bool
    Justify:FBTextJustify
    ReadOnly:bool
    Row:int
    Style:FBCellStyle
class FBSpreadRow(FBSpreadPart):
    Caption:str
    Parent:property
    RowSelected:bool
    def EditCaption(self)->bool:
        """Edit the row caption.
        This will initiate the UI edit of a row caption.
        ### Returns:
        Operation was successful ( true or false )."""
        ...
    def Remove(self):
        """Remove (destroy) row."""
        ...
class FBSpreadColumn(FBSpreadPart):
    Caption:str
    Width:int
class FBSpreadCell(FBSpreadPart):
    ...
class FBStory(FBComponent):
    ClipsTextsVisible:bool
    LockedShot:bool
    MaintainShotAndClipShotLengthsSynced:bool
    Mute:bool
    NoneBlockingPostprocess:bool
    RecordToDisk:bool
    RootEditFolder:FBStoryFolder
    RootFolder:FBStoryFolder
    SummaryClip:bool
    def CleanEmptyTracksAndFolders(self)->int:
        """Remove all empty tracks and folders present in the Story Tool.
        ### Returns:
        The number of empty story tracks and/or folders removed."""
        ...
    def __init__(self):...
class FBStoryClip(FBComponent):
    AudioClip:FBAudioClip
    AutoLoop:bool
    ClipAnimationPath:str
    ClipAudioPath:str
    ClipPitch:float
    ClipVideoPath:str
    Color:FBColor
    ConnectedToTake:bool
    CustomTimeWarp:FBAnimationNode
    FrameRate:float
    Ghost:bool
    GhostCustomTime:FBTime
    GhostManipulatorCustomTime:FBTime
    GhostManipulatorMode:FBStoryClipGhostTimeMode
    GhostManipulatorOffset:FBVector3d
    GhostModel:bool
    GhostPivot:bool
    GhostTravelling:bool
    ImageSequence:bool
    Loaded:bool
    LockPitchToSpeed:bool
    Loop:bool
    LoopTranslation:FBVector3d
    MarkIn:FBTime
    MarkOut:FBTime
    MirrorAnimation:bool
    MirrorPlane:FBStoryClipMirrorPlane
    Offset:FBTime
    OnChange:FBEvent
    Pivots:FBPropertyListPivot
    PostBlend:FBTimeSpan
    PreBlend:FBTimeSpan
    Rotation:FBVector3d
    Scale:float
    ShotActionStart:FBTime
    ShotActionStop:FBTime
    ShotBackplate:FBVideo
    ShotCamera:FBCamera
    ShotFrontplate:FBVideo
    ShotStartStopLocked:bool
    ShowBackplate:bool
    ShowEmbeddedTimecode:bool
    ShowFrontplate:bool
    ShowGhostClipMode:FBStoryClipShowGhostMode
    SolvingMode:FBStoryClipSolveMode
    Speed:float
    Start:FBTime
    StartStopLocked:bool
    Stop:FBTime
    TimeWarpEnabled:bool
    TimeWarpInterpolatorType:FBStoryClipTimeWarpInterpolatorType
    TimeWarpReverse:bool
    Translation:FBVector3d
    TravellingNode:FBPropertyListObject
    TravellingNodeFunction:FBStoryClipNodeFunction
    UseSystemFrameRate:bool
    def CanAssignSourcesToDestinations(self)->bool:
        """Determines if the animation clip can assign its sources to some destinations or not.
        ### Returns:
        Returns true if the animation clip can assign its sources to some destinations, false otherwise."""
        ...
    def Clone(self)->FBStoryClip:
        """Clone the clip."""
        ...
    def DestinationSetObject(self,SrcName:str,Object:FBComponent)->bool:
        """Assign source to destination if the SrcName is found in source list and Object is in the Details list.
        ### Parameters:
        - SrcName: The name of the source.
        - Object: The destination object.
        
        ### Returns:
        Returns true if assignment has been executed when the SrcName is found in source list and Object is in the Details list.
        
        ### Remarks:
        Assignment success depends on if they have the same name property and with animation on the source property."""
        ...
    def ExportToFile(self,OutputFile:str)->bool:
        """Export animation clip to disk file.
        ### Parameters:
        - OutputFile: Output file path name.
        
        ### Returns:
        Returns true if successful."""
        ...
    def GetAffectedAnimationNodes(self,AffectedAnimationNodes:FBComponent)->list:
        """Get the list of animation nodes affected by this story clip, for a specific object.
        ### Python:
        The function takes only one parameter (pClipObject) and returns a Python list. ex : lArray = lClip.GetAffectedAnimationNodes(lObject)
        
        ### Parameters:
        - AffectedAnimationNodes: Array of affected animation nodes, will be filled by the function."""
        ...
    def GetAffectedObjects(self)->list:
        """Get the list of objects affected by this story clip.
        ### Python:
        The function takes no parameter and returns a Python list. ex : lArray = lClip.GetAffectedObjects()"""
        ...
    def GetAssignSourcesToDestinationsInfo(self)->tuple:
        """Returns the information about the current state of Sources to Destinations assignment. The pSrcList, pDefaultDstList & pEffectiveDstList parameters will all be of same size, each index being related to the same index in the other lists. The pAvailableDstList parameter can contains more item than the other lists."""
        ...
    def GetReadOnly(self)->bool:
        """GetReadOnly Retrieves the clip read-only status.
        ### Returns:
        Returns the clip read-only status."""
        ...
    def MakeWritable(self)->bool:
        """Imports FCurves from story clip scene making them accessible for the user.
        ### Returns:
        Returns true if successful."""
        ...
    @overload
    def Match(self):
        """Match the animation clip with the specified pivot property."""
        ...
    @overload
    def Match(self,ObjectName:str,TimeType:FBStoryClipMatchingTimeType,TranslationType:FBStoryClipMatchingTranslationType,RotationType:FBStoryClipMatchingRotationType):
        """Match the animation clip to its previous/next animation clip, one to each other.
        ### Parameters:
        - ObjectName: The object name that specifies which part of the track content to use to match clips. If the object name is not valid, or empty, the match object will be disabled so that the blend does not take it into account when matching clips.
        - TimeType: The time type specifying which point of a cross-blend the selected clip is matched.
        - TranslationType: The translation type specifying if/how a clip's match object is translated to match another clip's animation.
        - RotationType: The rotation type specifying if/how a clip's match object is rotated to match another clip's animation."""
        ...
    def Move(self,Delta:FBTime,bForce:bool)->FBTime:
        """Move the clip of a delta offset.
        ### Parameters:
        - Delta: Delta time to apply to the clip.
        - bForce: Force clip to find the nearest position if the move fail.
        
        ### Returns:
        Return the delta between the new and previous clip's position."""
        ...
    def MoveTo(self,Time:FBTime,bForce:bool)->FBTime:
        """Move the clip to the specified time.
        ### Parameters:
        - Time: Time where to put the clip.
        - bForce: Force clip to find the nearest position if the move fail.
        
        ### Returns:
        Returns the new clip's time position."""
        ...
    def Razor(self,Time:FBTime)->FBStoryClip:
        """Cut (razor) the clip at the specified time.
        ### Parameters:
        - Time: Time where to cut. This time is local to the track, not to the clip.
        
        ### Returns:
        Returns the new clip generated by the razor action (right part)."""
        ...
    def SetAssignSourcesToDestinationsInfo(self,EffectiveDstList:list)->bool:
        """Sets the new effective destinations information for the Sources to Destinations assignment. The input string list size must contain the same number of items than the effective destination list returned by the GetAssignSourcesToDestinationsInfo method. Each item in the input string list must match an item in the available destination list returned by the GetAssignSourcesToDestinationsInfo method. The item at a given index of the input string list will be related to the same index of the sources list returned by the GetAssignSourcesToDestinationsInfo method.
        ### Parameters:
        - EffectiveDstList: String list containing the new effective destination.
        
        ### Returns:
        Returns true if the assign succeeded, false otherwise."""
        ...
    def SetReadOnly(self,bMakeClipReadOnly:bool,OutputFile:str=None)->bool:
        """SetReadOnly Assigns the clip read-only status.
        ### Parameters:
        - bMakeClipReadOnly: New read-only status
        - OutputFile: Output file path name, when setting the clip's read-only status to true.
        
        ### Returns:
        Returns true if successful."""
        ...
    def SetTime(self,SourceIn:FBTime,SourceOut:FBTime,DestinationIn:FBTime,DestinationOut:FBTime,bUseAlternateSrcInProp:bool):
        """SetTime Sets any in/out values for the source/destination times.
        In and out values are optional and the current values for the story clip will be used if not supplied. The story "Speed" property will be adjusted in order for the supplied values to be respected by the story clip.
        ### Parameters:
        - SourceIn: New value for the source IN time. Passing a value will modify the "MarkIn" and/or the "Speed" properties.
        - SourceOut: New value for the source OUT time. Passing a value will modify the "MarkOut" and/or the "Speed" properties.
        - DestinationIn: New value for the destination IN time. Passing a value will modify the "Stop" and/or the "Speed" properties.
        - DestinationOut: New value for the destination OUT time. Passing a value will modify the "Start" and/or the "Speed" properties.
        - bUseAlternateSrcInProp: Will work on the "ExtractStart" property instead of the "MarkIn" property when passing SourceIn."""
        ...
    def UpdateFromCurrentTake(self)->bool:
        """Update clip animation from current take animation for clip track's scope, works only for clip created by Insert Current Take and connected to current take.
        ### Returns:
        Returns true if succeed."""
        ...
    @overload
    def __init__(self,arg2:FBComponent,arg3:FBStoryTrack,arg4:FBTime):...
    @overload
    def __init__(self,arg2:str,arg3:FBStoryTrack,arg4:FBTime):...
    @overload
    def __init__(self,FilePath:str,Track:FBStoryTrack,Time:FBTime,Object:FBTime):
        """### Parameters:
        - FilePath: Media file path to create clip with.
        - Track: The track in which we create the clip.
        - Time: Time where the clip should begin.
        - Object: For internal use only."""
        ...
class FBStoryFolder(FBComponent):
    Childs:FBPropertyListStoryFolder
    Collapsed:bool
    Label:str
    Mute:bool
    Parent:FBStoryFolder
    RecordClipPath:str
    Solo:bool
    Tracks:FBPropertyListStoryTrack
    def AlignSelectedClips(self,Type:FBStoryClipAlignmentType,ReferenceClip:FBComponent):
        """Used to align selected clips .
        ### Parameters:
        - Type: Type of alignment that will be done.
        - ReferenceClip: Needed when kFBStoryClipAlignmentEndPreviousAllAligned, kFBStoryClipAlignmentBeginningNextAllAligned or kFBStoryClipAlignmentCurrentTimelineWithOffset are used."""
        ...
    def AlignSelectedClipsGroup(self,Type:FBStoryGroupClipAlignmentType):
        """Used to align clips inside a group.
        ### Parameters:
        - Type: Type of alignment that will be done."""
        ...
    def ConvertClipsToReadOnly(self,bSelected:bool,FilePath:str):
        """Convert all clips to read-only clips.
        Identical clips are replaced by the same read-only clip.
        ### Parameters:
        - bSelected: Only selected clip will be converted.
        - FilePath: Folder path where the read-only clips will be saved.
        
        ### Remarks:
        Currently only animation clips are supported in the Root Folder"""
        ...
    def ExpandSelectedClips(self,bPreserveOverlap:bool):
        """Used to expand selected clips .
        ### Parameters:
        - bPreserveOverlap: If true, portion of clips that overlap other clips won't be modified."""
        ...
    def ExpandSelectedClipsGroup(self,bPreserveOverlap:bool):
        """ExpandSelectedClipsGroup Used to expand group clip dependent clips.
        ### Parameters:
        - bPreserveOverlap: If true, portion of clips that overlap other clips won't be modified."""
        ...
    def Load(self,bLoad:bool):
        """Allow to load/unload all story clips under this folder.
        ### Remarks:
        Currently only animation clips are supported."""
        ...
    def __init__(self,ParentFolder:FBStoryFolder=None):
        """### Parameters:
        - ParentFolder: If NULL, parent will be the global root folder, according to its type.
        ### Remarks:
        You can't create a folder with the RootEditFolder as parent."""
        ...
class FBStoryGroupClip(FBComponent):
    DependentClips:FBPropertyListObject
    Start:FBTime
    StartStopLocked:bool
    Stop:FBTime
    def Move(self,Delta:FBTime,bForce:bool)->FBTime:
        """Move the clip of a delta offset.
        ### Parameters:
        - Delta: Delta time to apply to the clip.
        - bForce: Force clip to find the nearest position if the move fail.
        
        ### Returns:
        Return the delta between the new and previous clip's position."""
        ...
    def MoveTo(self,Time:FBTime,bForce:bool)->FBTime:
        """Move the clip to the specified time.
        ### Parameters:
        - Time: Time where to put the clip.
        - bForce: Force clip to find the nearest position if the move fail.
        
        ### Returns:
        Returns the new clip's time position."""
        ...
    def Razor(self,Time:FBTime):
        """Cut (razor) the clip at the specified time.
        ### Parameters:
        - Time: Time where to cut. This time is local to the track, not to the clip."""
        ...
    def __init__(self,AffectedClipObject:list):
        """### Parameters:
        - AffectedClipObject: Clips that will be controlled by the group clip."""
        ...
class FBStoryTrack(FBConstraint):
    AcceptKey:bool
    AudioOutIndex:int
    Character:FBCharacter
    CharacterIndex:int
    ClipNameConvention:str
    Clips:FBPropertyListStoryClip
    Details:FBPropertyListStoryDetails
    Ghost:bool
    GhostModel:bool
    GhostPivot:bool
    GhostShowTrackMode:FBStoryTrackGhostShowMode
    GhostTravelling:bool
    Label:str
    Mute:bool
    OffsetEnable:bool
    ParentFolder:FBStoryFolder
    ParentTrack:FBStoryTrack
    PassThrough:bool
    RecordClipPath:str
    RecordTrack:bool
    ReferenceMode:FBStoryTrackRefMode
    ShowBackplate:bool
    ShowFrontplate:bool
    Solo:bool
    SubTracks:FBPropertyListStorySubTrack
    TrackVideo:FBVideo
    Type:FBStoryTrackType
    def AddClip(self,Clip:FBComponent,Time:FBTime):
        """AddClip Add the clip to the track."""
        ...
    def ChangeDetailsBegin(self):
        """You must call this function before adding/removing any object to the Details list or it won't work."""
        ...
    def ChangeDetailsEnd(self):
        """You must call this function after adding/removing any object to the Details list or it won't work."""
        ...
    def CopyTakeIntoTrack(self,TimeSpan:FBTimeSpan,Take:FBTake,OutputOffset:FBTime=0,bMakeUndoable:bool=False)->FBStoryClip:
        """CopyTakeIntoTrack Copy animation from the specified take for affected objects of the track.
        ### Parameters:
        - TimeSpan: Time span for the clip to create.
        - Take: Take to get the animation from.
        - OutputOffset: Time offset for the clip if necessary.
        - bMakeUndoable: If the operation should be undoable.
        
        ### Returns:
        Created story clip if the operation succeeded otherwize NULL."""
        ...
    def CreateSubTrack(self,TrackType:FBStoryTrackType,RefMode:FBStoryTrackRefMode)->FBStoryTrack:
        """Create a sub track, Only Character and Animation tracks can have sub-tracks.
        ### Parameters:
        - TrackType: Type of the sub track to be created.
        - RefMode: Composition mode of the sub track, kFBStoryTrackOverride or kFBStoryTrackAdditive.
        
        ### Returns:
        Created sub story track if the operation succeeded otherwise NULL."""
        ...
    def EnableBodyPart(self,Part:FBStoryTrackBodyPart,bEnable:bool):
        """### Parameters:
        - Part: Which part to enable/disable.
        - bEnable: If True, this will enable the body part solving while false will disable it. Enable a specific body part for character solving."""
        ...
    def IsBodyPartEnabled(self,Part:FBStoryTrackBodyPart)->bool:
        """Is a specific body part is enabled."""
        ...
    def Load(self,bLoad:bool):
        """Allow to load/unload all story clips under this track.
        ### Remarks:
        Currently only animation clips are supported."""
        ...
    @overload
    def __init__(self,arg2:FBStoryTrackType,arg3:FBStoryFolder=None):...
    @overload
    def __init__(self,arg2:FBComponent,arg3:FBStoryFolder=None):...
class FBStringList():
    def Add(self,S:str,Ref=0)->int:
        """Add a string to the list.
        ### Parameters:
        - S: String to add to list.
        - Ref: Reference to store with string (default = 0)
        
        ### Returns:
        Index where item was stored."""
        ...
    def AsString(self,Separator:str='~')->str:
        """Get as string.
        ### Parameters:
        - Separator: the string list separator.
        
        ### Returns:
        String list."""
        ...
    def Clear(self):
        """Clear the list (remove all the items)."""
        ...
    @overload
    def Find(self,Ref)->int:
        """Find the index where Ref is stored.
        ### Parameters:
        - Ref: Reference to look for.
        
        ### Returns:
        Index at which Ref can be found."""
        ...
    @overload
    def Find(self,String:str,bCaseSensitive:bool=True,bStartWith:bool=False)->int:
        """Find the index with the string String (or start with String )
        ### Parameters:
        - String: String to search for.
        - bCaseSensitive: true if considering case.
        - bStartWith: true if to find the index of the string which start with String.
        
        ### Returns:
        Index where S is stored."""
        ...
    def GetAt(self,Index:int)->str:
        """Get the string at Index .
        ### Parameters:
        - Index: Index to get string at.
        
        ### Returns:
        String at Index ."""
        ...
    def GetReferenceAt(self,Index:int)->int:
        """Get the reference store with the string at Index .
        ### Parameters:
        - Index: Index to get reference at.
        
        ### Returns:
        Reference stored with value at Index ."""
        ...
    def IndexOf(self,S:str)->int:
        """Get the index of a string.
        ### Parameters:
        - S: String to look for.
        
        ### Returns:
        Index where string S was found."""
        ...
    def InsertAt(self,Index:int,S:str,Ref=0):
        """Insert an entry at Index .
        ### Parameters:
        - Index: Index where item is to be inserted.
        - S: String to insert.
        - Ref: Reference to store with string(default=0)."""
        ...
    def Remove(self,S:str)->int:
        """Remove a string from the list.
        ### Parameters:
        - S: String to remove from the list.
        
        ### Returns:
        Index where item was found."""
        ...
    def RemoveAt(self,Index:int):
        """Remove an entry at Index .
        ### Parameters:
        - Index: Index where item is to be removed from."""
        ...
    def SetAt(self,Index:int,String:str)->bool:
        """Set the string at Index .
        ### Parameters:
        - Index: Index where string is to be set.
        - String: String to set value at Index with."""
        ...
    def SetReferenceAt(self,Index:int,Ref):
        """Set the reference stored with the string at Index .
        ### Parameters:
        - Index: Index to store reference at.
        - Ref: Reference to store at Index ."""
        ...
    def SetString(self,String:str,Separator:str='~')->bool:
        """Set string for list.
        ### Parameters:
        - Separator: the string list separator.
        - String: String to set for list."""
        ...
    def Sort(self):
        """Sort the string list (ascending)"""
        ...
    def __getitem__(self,Index:int)->str:...
    @overload
    def __init__(self):...
    @overload
    def __init__(self,String:str,Separator:str='~'):
        """### Parameters:
        - Separator: the string list separator.
        - String: String to set for list."""
        ...
    def __len__(self)->int:...
    def __setitem__(self,arg2,arg3:str)->bool:...
class FBSurface(FBGeometry):
    SurfaceMode:FBSurfaceMode
    UClosed:bool
    USize:int
    UStep:int
    VClosed:bool
    VSize:int
    VStep:int
    def ControlPointsBegin(self):...
    def ControlPointsEnd(self):...
    def GetControlPoint(self,arg2,arg3,arg4,arg5,arg6):...
    def GetSurfaceCapped(self,arg2,arg3)->bool:...
    def SetControlPoint(self,arg2,arg3,arg4,arg5,arg6):...
    def SurfaceBegin(self):...
    def SurfaceEditBegin(self):...
    def SurfaceEditEnd(self):...
    def SurfaceEnd(self):...
class FBSystem(FBComponent):
    ApplicationPath:str
    AreMessageBoxesSuspended:bool
    AssetManager:FBAssetMng
    AudioInputs:FBPropertyListAudioIn
    AudioOutputs:FBPropertyListAudioOut
    BuildId:str
    BuildVersion:str
    Cameras:property
    ComputerName:str
    ConfigPath:property
    ConstructionHistory:FBConstructionHistory
    CurrentTake:FBTake
    DesktopSize:FBVector2d
    Devices:property
    EPluginItemInfo:type
    FrameRate:float
    FullScreenViewer:bool
    Lights:property
    LocalTime:FBTime
    Manipulators:FBPropertyListManipulator
    Materials:property
    OnConnectionDataNotify:FBEventConnectionDataNotify
    OnConnectionKeyingNotify:FBEventConnectionKeyingNotify
    OnConnectionNotify:FBEventConnectionNotify
    OnConnectionStateNotify:FBEventConnectionStateNotify
    OnUIIdle:property
    OnVideoFrameRendering:FBEventVideoFrameRendering
    PathImages:str
    PathMeshs:str
    ProcessMemory:float
    ProcessMemoryPeak:float
    PythonVersion:int
    Renderer:FBRenderer
    RootModel:FBModel
    Scene:FBScene
    SceneRootModel:FBModel
    Shaders:property
    SuspendMessageBoxes:bool
    SystemTime:FBTime
    Takes:property
    Textures:property
    UserConfigPath:property
    Version:float
    VideoInputs:FBPropertyListVideoIn
    VideoOutputs:FBPropertyListVideoOut
    ePluginItemDescription:EPluginItemInfo
    ePluginItemFileName:EPluginItemInfo
    ePluginItemIconName:EPluginItemInfo
    def CurrentDirectory(self)->str:
        """Get current work directory.
        ### Returns:
        current work directory."""
        ...
    def GetCommandLineArgs(self)->FBStringList:
        """Returns the command line arguments for SDK.
        This function returns portion of the command line arguments within a pair of delimiters (–sdk-begin & –sdk-end). Example:
        motionbuilder -console -G500,500 -suspendMessages –sdk-begin –department mocap –usage on-stage –sdk-end C:/temp/sample.fbx
        Note that "-console", "-G500,500", "-suspendMessages" and "C:/temp/sample.fbx" are for MotionBuilder itself hence are consumed accordingly. Only those arguments between –sdk-begin and –sdk-end are accessible with this function. In this example, they will be "--department mocap --usage on-stage"
        This SDK command line argument is useful for plugin deployment and management in large production facility, where different department or different workflow may require a different set of plugins or functionality/behavior dynamically.
        Python users also have access to this through official built-in module sys.argv which could be parsed easily via argparse module.
        ### Returns:
        the command line arguments"""
        ...
    def GetLoadedPluginItemGroups(self,PluginItemName:str)->FBStringList:
        """Returns a string list containing the groups list in which the specified plug-in item's name belongs to.
        ### Returns:
        the groups list in which the specified plug-in item's name belongs to."""
        ...
    def GetLoadedPluginItemInfo(self,PluginItemName:str)->FBStringList:
        """Returns a string list containing the information of the specified plug-in item's name.
        A specific plug-in item information can be retrieved from the returned string list with a EPluginItemInfo enum value.
        ### Returns:
        the information of the specified plug-in item's name."""
        ...
    def GetLoadedPluginItemsName(self)->FBStringList:
        """Returns a string list containing the names of all the loaded plug-in.
        ### Returns:
        the names of all the loaded plug-in."""
        ...
    def GetPluginPath(self)->FBStringList:
        """Returns the plugin path.
        By default, MotionBuilder searches C++ plug-ins and load them at start-up. Users could provide additional plugin paths by setting environment variable "MOTIONBUILDER_PLUGIN_PATH" before running MotionBuilder.
        ### Returns:
        the plugin path"""
        ...
    def GetPythonStartupPath(self)->FBStringList:
        """Returns the python startup path.
        User could put python script in the startup folders, and MotionBuilder will search scripts from those folders and run them at startup. By default, there are two startup folders: /config/PythonStartup and /bin/config/PythonStartup. Users could append additional paths by setting environment variable "MOTIONBUILDER_PYTHON_STARTUP" before launching application.
        ### Returns:
        the python startup path"""
        ...
    def MakeFullPath(self,RelativeFilePath:str)->str:
        """Return the full path.
        ### Parameters:
        - RelativeFilePath: The relative file path
        
        ### Returns:
        Full file path based on combining the current directory"""
        ...
    def __init__(self):...
class FBPatch(FBSurface):
    USurfaceType:FBSurfaceType
    VSurfaceType:FBSurfaceType
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of Patch."""
        ...
class FBNurbs(FBSurface):
    UNurbType:FBNurbType
    UOrder:int
    VNurbType:FBNurbType
    VOrder:int
    def GetControlKnotValue(self,UorV:int,Index:int)->float:
        """Get knot vector value of control point.
        ### Parameters:
        - UorV: 1 if V knot vector, 0 if U knot vector.
        - Index: Index of control point to set knot value for."""
        ...
    def GetControlMultiplicity(self,UorV:int,Index:int)->int:
        """Get multiplicity (number of "instances") of control point.
        ### Parameters:
        - UorV: 1 if V multiplicity, 0 if U multlipicity.
        - Index: Index of control point to get multiplicity for."""
        ...
    def GetControlWeight(self,Index:int)->float:
        """Get weight of control point.
        ### Parameters:
        - Index: Index of control point to get weight from.
        
        ### Returns:
        Weight of control point at index Index ."""
        ...
    def GetKnotCount(self,UorV:int)->int:
        """Number of knot vectors.
        ### Parameters:
        - UorV: 1 if V knot vector, 0 if U knot vector.
        
        ### Returns:
        Number of knot vectors on NURBS surface"""
        ...
    def SetControlKnotValue(self,UorV:int,Index:int,KnotValue:float):
        """Set knot vector value of control point.
        ### Parameters:
        - UorV: 1 if V knot vector, 0 if U knot vector.
        - Index: Index of control point to set knot value for.
        - KnotValue: Knot value for control point at Index ."""
        ...
    def SetControlMultiplicity(self,UorV:int,Index:int,Multiplicity:int):
        """Set multiplicity (number of "instances") of control point.
        ### Parameters:
        - UorV: 1 if V multiplicity, 0 if U multlipicity.
        - Index: Index of control point to set multiplicity for.
        - Multiplicity: Multiplicity value for control point at Index ."""
        ...
    def SetControlWeight(self,Index:int,Weight:float):
        """Set weight of control point.
        ### Parameters:
        - Index: Index of control point to set weight at.
        - Weight: Weight of control point."""
        ...
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of Nurbs."""
        ...
class FBTexture(FBBox):
    Alpha:property
    BlendMode:property
    Height:property
    Mapping:property
    Rotation:property
    Scaling:property
    SwapUV:property
    TextureOGLId:property
    Translation:property
    UseType:property
    Video:property
    Width:property
    def Clone(self)->object:...
    def OGLInit(self):...
    def __copy__(self)->object:...
    def __init__(self,arg2:str):...
class FBLayeredTexture(FBTexture):
    BackgroundColor:FBColorAndAlpha
    Layers:FBPropertyListTexture
    def SetLayerConfigDirty(self):
        """Set layer config dirty to trigger new composition."""
        ...
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of texture media. Can be a NULL pointer. If set, this will create a FBVideo object used as the Video property."""
        ...
class FBTime():
    ETimeFormats:type
    Infinity:FBTime
    MinusInfinity:FBTime
    OneHour:FBTime
    OneMinute:FBTime
    OneSecond:FBTime
    Zero:FBTime
    eDefaultFormat:ETimeFormats
    eFrame:ETimeFormats
    eSMPTE:ETimeFormats
    def Get(self)->int:
        """Get time value (long)
        ### Returns:
        Time value as long."""
        ...
    def GetFrame(self,TimeMode:FBTimeMode=FBTimeMode.kFBTimeModeDefault)->int:
        """Get the frame count.
        With this function, it is possible to obtain the cumulative and local frame counts.
        ### Parameters:
        - TimeMode: Time mode to get the constant (default is kFBTimeModeDefault).
        
        ### Returns:
        Frames per second constant for the specified time mode."""
        ...
    def GetMilliSeconds(self)->int:
        """Get milliseconds for time.
        ### Returns:
        MilliSeconds value."""
        ...
    def GetSecondDouble(self)->float:
        """Get seconds as double.
        ### Returns:
        Seconds in double form."""
        ...
    def GetTimeString(self,Mode:FBTimeMode=FBTimeMode.kFBTimeModeDefault,Format:ETimeFormats=eDefaultFormat)->str:
        """Get time as a string.
        ### Parameters:
        - Mode: Time mode (default=kFBTimeModeDefault) to use (call FBSystem() .GetTransportFps() to the the current UI displayed mode).
        - Format: Format to use for the returned string(default= FBTime::eDefaultFormat ).
        
        ### Returns:
        String value of time."""
        ...
    def Set(self,Time:float):
        """Set time value from a long.
        ### Parameters:
        - Time: Time value to set."""
        ...
    def SetFrame(self,Frames:float,TimeMode:FBTimeMode=FBTimeMode.kFBTimeModeDefault):
        """Set time in frame format.
        ### Parameters:
        - Frames: The number of frames.
        - TimeMode: The time mode identifier which will dictate the extraction algorithm."""
        ...
    def SetMilliSeconds(self,MilliSeconds:float):
        """Set milliseconds time.
        ### Parameters:
        - MilliSeconds: MilliSeconds value."""
        ...
    def SetSecondDouble(self,Time:float):
        """Set seconds from double.
        ### Parameters:
        - Time: Time to set seconds from."""
        ...
    def SetTime(self,Hour:int,Minute:int=0,Second:int=0,Frame:int=0,Field:int=0,TimeMode:FBTimeMode=FBTimeMode.kFBTimeModeDefault):
        """Set time (from separate values)
        ### Parameters:
        - Hour: Hour value.
        - Minute: Minute value(default=0).
        - Second: Second value(default=0).
        - Frame: Frame value(default=0).
        - Field: Field value(default=0).
        - TimeMode: Time mode to get time as(default=kFBTimeModeDefault)."""
        ...
    def SetTimeString(self,Time:str):
        """Set time from string.
        ### Parameters:
        - Time: String to set time from."""
        ...
    @overload
    def __add__(self,arg2:FBTime)->object:...
    @overload
    def __add__(self,arg2)->object:...
    @overload
    def __init__(self,arg2=None):...
    @overload
    def __init__(self,Hour:int,Minute:int,Second:int=0,Frame:int=0,Field:int=0,TimeMode:FBTimeMode=FBTimeMode.kFBTimeModeDefault):
        """### Parameters:
        - Hour: Hour value.
        - Minute: Minute value.
        - Second: Second value.
        - Frame: Frame value.
        - Field: Field value.
        - TimeMode: Time mode(default=kFBTimeModeDefault)."""
        ...
    @overload
    def __init__(self,arg2:FBTime):...
    @overload
    def __sub__(self,Constant:FBTime)->FBTime:
        """Overloaded arithmetic operators with constants.
        ### Parameters:
        - Constant: Double constant to add to time.
        
        ### Returns:
        Result in FBTime data."""
        ...
    @overload
    def __sub__(self,Time:FBTime)->FBTime:
        """Overloaded arithmetic operators with FBTime objects.
        ### Parameters:
        - Time: Time to use in operation.
        
        ### Returns:
        Result in FBTime data."""
        ...
class FBTimeCode():
    FILM_23976:float
    FILM_24:float
    FRAMES_11988:float
    FRAMES_30:float
    FRAMES_5994:float
    Frame:property
    FrameRate:property
    MPAL_30:float
    NTSC_DROP:float
    NTSC_FULL:float
    PAL_25:float
    TimeCodeString:property
    def GetRawFrame(self)->float:
        """Get the raw value for the frame.
        ### Returns:
        raw value for the frame."""
        ...
    def GetRawRate(self)->float:
        """Get the raw value for the rate.
        ### Returns:
        raw value for the rate."""
        ...
    def GetRawSecond(self)->float:
        """Get the raw value for the second.
        ### Returns:
        raw value for the second."""
        ...
    def GetTime(self)->FBTime:
        """Return a Time corresponding to the timecode."""
        ...
    def GetTimeCodeString(self,Format:ETimeFormats=FBTime.eDefaultFormat)->str:
        """Get time as a string.
        ### Parameters:
        - Format: Format to use for the returned string(default= FBTime::eDefaultFormat ).
        
        ### Returns:
        String value of time."""
        ...
    def SetTime(self,Time:FBTime):
        """Set TimeCode according to the given time.
        ### Parameters:
        - Time: Time value to set."""
        ...
    def SetTimeCode(self,Hour:int,Minute:int=0,Second:int=0,Frame:float=0):
        """Set timecode.
        ### Parameters:
        - Hour: Hour value.
        - Minute: Minute value.
        - Second: Second value.
        - Frame: Frame value."""
        ...
    def SetTimeCodeString(self,Time:str,Format:ETimeFormats=FBTime.eDefaultFormat):
        """Set time from string.
        ### Parameters:
        - Time: String to set time from.
        - Format: Format to use for the string(default= FBTime::eDefaultFormat )."""
        ...
    @overload
    def __init__(self):...
    @overload
    def __init__(self,Rate:float=FRAMES_30):
        """### Parameters:
        - Rate: Framerate value."""
        ...
    @overload
    def __init__(self,arg2:FBTimeCode):...
class FBTake(FBComponent):
    Comments:str
    LocalTimeSpan:FBTimeSpan
    ReferenceTimeSpan:FBTimeSpan
    def AddTimeMark(self,Time:FBTime)->int:
        """Add a time mark to the take.
        It doesn't allow creating a time mark at the same time of another time mark. Note: Internally, the time marks are stored in time order. Adding a time mark before other existing time marks will modify the index of these other time marks.
        ### Parameters:
        - Time: Time where to add the time mark on the take.
        ### Returns:
        The index of the time mark added if the operation is successful, -1 otherwise."""
        ...
    def ClearAllProperties(self,bOnSelectedObjectsOnly:bool,bOnLockedProperties:bool=False):
        """Clear the animation on all the properties.
        ### Parameters:
        - bOnSelectedObjectsOnly: Specify if clear will be performed on all objects or only on the one that are currently selected.
        - bOnLockedProperties: Specify if clear will be performed on locked properties as well."""
        ...
    def ClearAllPropertiesOnCurrentLayer(self):
        """Clear all the animation on the current layer."""
        ...
    def CopyTake(self,NewTakeName:str)->FBTake:
        """Copy the take.
        Will create a copy of the current take, with the current take data. This is analogous to creating a new take, and copying the current take data into it. The Layers data and the TimeWarp date will be copied. The newly created take will be set as the current take. The newly created take is automatically added to the scene and available in the Transport control.
        ### Parameters:
        - NewTakeName: The name for the new take.
        
        ### Returns:
        Handle to the newly created take."""
        ...
    def CreateNewLayer(self):
        """Create a new layer."""
        ...
    def DeleteAllTimeMarks(self):
        """Delete all time marks from the take."""
        ...
    def DeleteAnimation(self,StartTime:FBTime=FBTime.MinusInfinity,StopTime:FBTime=FBTime.Infinity,bInclusive:bool=True,LayerID:int=-1,bOnLockedProperties:bool=False)->bool:
        """Delete animation (FCurve keys) of this take object within a time range.
        ### Parameters:
        - StartTime: Start of time range.
        - StopTime: End of time range.
        - bInclusive: True to include within the time range the keys at StartTime and StopTime, false otherwise.
        - LayerID: The animation layer ID being affected by the delete operation, -1 to delete the animation of all animations layers.
        - bOnLockedProperties: True to delete animation on locked properties, false to skip deleting animation on locked properties.
        
        ### Returns:
        True if the delete operation is successful (at least one FCurve has been modified), false otherwise (e.g. no keys found within the time range, invalid layer ID, etc.)."""
        ...
    def DeleteAnimationOnObjects(self,Objects:list,StartTime:FBTime=FBTime.MinusInfinity,StopTime:FBTime=FBTime.Infinity,bInclusive:bool=True,LayerID:int=-1,bOnLockedProperties:bool=False)->bool:
        """Delete animation (FCurve keys) of this take object on given objects within a time range.
        ### Parameters:
        - Objects: Objects affected by the delete operation.
        - StartTime: Start of time range.
        - StopTime: End of time range.
        - bInclusive: True to include within the time range the keys at StartTime and StopTime, false otherwise.
        - LayerID: The animation layer ID being affected by the delete operation, -1 to delete the animation of all animations layers.
        - bOnLockedProperties: True to delete animation on locked properties, false to skip deleting animation on locked properties.
        
        ### Returns:
        True if the delete operation is successful (at least one FCurve has been modified), false otherwise (e.g. no keys found within the time range, invalid layer ID, etc.)."""
        ...
    def DeleteAnimationOnProperties(self,Properties:list,StartTime:FBTime=FBTime.MinusInfinity,StopTime:FBTime=FBTime.Infinity,bInclusive:bool=True,LayerID:int=-1,bOnLockedProperties:bool=False,PropertyComponents:FBPropertyComponents=FBPropertyComponents.kFBPropertyComponentAll)->bool:
        """Delete animation (FCurve keys) of this take object on given properties within a time range.
        ### Parameters:
        - Properties: Properties affected by the delete operation.
        - StartTime: Start of time range.
        - StopTime: End of time range.
        - bInclusive: True to include within the time range the keys at StartTime and StopTime, false otherwise.
        - LayerID: The animation layer ID being affected by the delete operation, -1 to delete the animation of all animations layers.
        - bOnLockedProperties: True to delete animation on locked properties, false to skip deleting animation on locked properties.
        - PropertyComponents: The component bit field considered when performing the delete operation, for properties having such components. By default, all components are considered. If a property don't have any component, this parameter is not affecting that property.
        
        ### Returns:
        True if the delete operation is successful (at least one FCurve has been modified), false otherwise (e.g. no keys found within the time range, invalid layer ID, etc.)."""
        ...
    def DeleteTimeMark(self,Index:int)->bool:
        """Delete a time mark from the take.
        Note: Internally, the time marks are stored in time order. Deleting a time mark will modify the index of time marks laying after the deleted time mark.
        ### Parameters:
        - Index: Index of the time mark to delete.
        
        ### Returns:
        True if the operation is successful, false otherwise."""
        ...
    def DuplicateSelectedLayers(self):
        """Duplicate the selected layers.
        This is equivalent of doing a copy-paste."""
        ...
    def GetCurrentLayer(self)->int:
        """Get the current layer for the take.
        ### Returns:
        The current layer index."""
        ...
    def GetLayer(self,LayerIndex:int)->FBAnimationLayer:
        """Get the layer object that have the specified ID.
        ### Parameters:
        - LayerIndex: The index of the layer that will be returned.
        
        ### Returns:
        Layer with the specified ID."""
        ...
    def GetLayerByName(self,Name:str)->FBAnimationLayer:
        """Get the layer object that have the specified name.
        ### Parameters:
        - Name: The name of the animation layer to get.
        
        ### Returns:
        Layer with the specified name or `None` if no layer has been found."""
        ...
    def GetLayerCount(self)->int:
        """Get the layer count.
        ### Returns:
        The layer count."""
        ...
    def GetLayerRealSelection(self)->bool:
        """Real selection for layer.
        Check the SetLayerRealSelection function for more information about this.
        ### Returns:
        True if selecting a layer will also select the FBComponent of that layer."""
        ...
    def GetNextTimeMarkIndex(self)->int:
        """Returns the next time mark index, based on the current local time.
        ### Returns:
        The next time mark index, -1 if any next time mark is available."""
        ...
    def GetPreviousTimeMarkIndex(self)->int:
        """Returns the previous time mark index, based on the current local time.
        ### Returns:
        The previous time mark index, -1 if any previous time mark is available."""
        ...
    def GetTimeMarkAction(self,Index:int)->FBTimeMarkAction:
        """Returns the action associated with a time mark.
        ### Parameters:
        - Index: Index of the time mark.
        
        ### Returns:
        The action associated with the time mark."""
        ...
    def GetTimeMarkColor(self,Index:int)->FBColor:
        """Returns the color associated with a time mark.
        ### Parameters:
        - Index: Index of the time mark.
        
        ### Returns:
        The color associated with the time mark."""
        ...
    def GetTimeMarkCount(self)->int:
        """Returns the number of time marks on the take.
        ### Returns:
        The number of time marks on the take."""
        ...
    def GetTimeMarkName(self,Index:int)->str:
        """Returns the name associated with a time mark.
        ### Parameters:
        - Index: Index of the time mark.
        
        ### Returns:
        The name associated with the time mark."""
        ...
    def GetTimeMarkTime(self,Index:int)->FBTime:
        """Returns the time associated with a time mark.
        ### Parameters:
        - Index: Index of the time mark.
        
        ### Returns:
        The time associated with the time mark."""
        ...
    def MergeLayers(self,MergeOptions:FBAnimationLayerMergeOptions,bDeleteMergedLayers:bool,MergeMode:FBMergeLayerMode,bMergeLockedProperties:bool=False):
        """Merge the selected layers.
        This is equivalent of pressing the merge button in the Animation Layer editor.
        ### Parameters:
        - MergeOptions: Indicate which objects, layers and properties (selected or all) should be merged.
        - bDeleteMergedLayers: The source layer will be deleted after the merge if no animation is left on those layers, or if those layers are not parent of another layer.
        - MergeMode: Set the layer mode of the resulting layer, if possible (the BaseAnimation layer cannot be modified).
        - bMergeLockedProperties: The properties will be merged even if they are locked."""
        ...
    def MoveCurrentLayerDown(self)->bool:
        """Move the current layer down, similar to using the button to move the layer in the Animation Layer tool.
        Use the SetCurrentLayer to specify the current layer.
        ### Returns:
        True if successful."""
        ...
    def MoveCurrentLayerUp(self)->bool:
        """Move the current layer up, similar to using the button to move the layer in the Animation Layer tool.
        Use the SetCurrentLayer to specify the current layer.
        ### Returns:
        True if successful."""
        ...
    def OffsetAnimation(self,OffsetTime:FBTime,StartTime:FBTime=FBTime.MinusInfinity,StopTime:FBTime=FBTime.Infinity,bInclusive:bool=True,LayerID:int=-1,bOnLockedProperties:bool=False)->bool:
        """Offset the animation (FCurve keys) of this take object within a time range by a given offset time.
        Non-moving FCurve keys that are situated in the target range are deleted automatically, to preserve the animation being offset.
        ### Parameters:
        - OffsetTime: The offset time to apply.
        - StartTime: Start of time range.
        - StopTime: End of time range.
        - bInclusive: True to include within the time range the keys at StartTime and StopTime, false otherwise.
        - LayerID: The animation layer ID being affected by the offset operation, -1 to offset the animation of all animations layers.
        - bOnLockedProperties: True to offset animation on locked properties, false to skip offsetting animation on locked properties.
        
        ### Returns:
        True if the offset operation is successful (at least one FCurve has been modified), false otherwise (e.g. no keys found within the time range, invalid layer ID, etc.)."""
        ...
    def OffsetAnimationOnObjects(self,Objects:list,OffsetTime:FBTime,StartTime:FBTime=FBTime.MinusInfinity,StopTime:FBTime=FBTime.Infinity,bInclusive:bool=True,LayerID:int=-1,bOnLockedProperties:bool=False)->bool:
        """Offset the animation (FCurve keys) of this take object on given objects within a time range by a given offset time.
        Non-moving FCurve keys that are situated in the target range are deleted automatically, to preserve the animation being offset.
        ### Parameters:
        - Objects: Objects affected by the offset operation.
        - OffsetTime: The offset time to apply.
        - StartTime: Start of time range.
        - StopTime: End of time range.
        - bInclusive: True to include within the time range the keys at StartTime and StopTime, false otherwise.
        - LayerID: The animation layer ID being affected by the offset operation, -1 to offset the animation of all animations layers.
        - bOnLockedProperties: True to offset animation on locked properties, false to skip offsetting animation on locked properties.
        
        ### Returns:
        True if the offset operation is successful (at least one FCurve has been modified), false otherwise (e.g. no keys found within the time range, invalid layer ID, etc.)."""
        ...
    def OffsetAnimationOnProperties(self,Properties:list,OffsetTime:FBTime,StartTime:FBTime=FBTime.MinusInfinity,StopTime:FBTime=FBTime.Infinity,bInclusive:bool=True,LayerID:int=-1,bOnLockedProperties:bool=False,PropertyComponents:FBPropertyComponents=FBPropertyComponents.kFBPropertyComponentAll)->bool:
        """Offset the animation (FCurve keys) of this take object on given properties within a time range by a given offset time.
        Non-moving FCurve keys that are situated in the target range are deleted automatically, to preserve the animation being offset.
        ### Parameters:
        - Properties: Properties affected by the offset operation.
        - OffsetTime: The offset time to apply.
        - StartTime: Start of time range.
        - StopTime: End of time range.
        - bInclusive: True to include within the time range the keys at StartTime and StopTime, false otherwise.
        - LayerID: The animation layer ID being affected by the offset operation, -1 to offset the animation of all animations layers.
        - bOnLockedProperties: True to offset animation on locked properties, false to skip offsetting animation on locked properties.
        - PropertyComponents: The component bit field considered when performing the offset operation, for properties having such components. By default, all components are considered. If a property don't have any component, this parameter is not affecting that property.
        
        ### Returns:
        True if the offset operation is successful (at least one FCurve has been modified), false otherwise (e.g. no keys found within the time range, invalid layer ID, etc.)."""
        ...
    def PlotAllTakesOnObjects(self,PlotPeriod:FBTime,ObjectsToPlot:list):
        """Plot the animation on given objects for all takes.
        This method will plot the animation of all takes to the specified objects. Although the method supports boxes, the most common use case it to specify FBModels that have been cast to boxes.
        ### Parameters:
        - PlotPeriod: Period for the plot.
        - ObjectsToPlot: Objects to plot."""
        ...
    def PlotAllTakesOnProperties(self,PlotPeriod:FBTime,PropertiesToPlot:list):
        """Plot the animation on given properties for all takes.
        Will plot the animation for all takes on the given properties in the scene.
        ### Parameters:
        - PlotPeriod: Period for the plot.
        - PropertiesToPlot: Properties to plot."""
        ...
    def PlotAllTakesOnSelected(self,PlotPeriod:FBTime):
        """Plot the animation on selected models for all takes.
        Will plot the animation for all takes on the selected models in the scene.
        ### Parameters:
        - PlotPeriod: Period for the plot."""
        ...
    def PlotAllTakesOnSelectedProperties(self,PlotPeriod:FBTime):
        """Plot the animation on selected properties for all takes.
        Will plot the animation for all takes on the selected properties in the scene.
        ### Parameters:
        - PlotPeriod: Period for the plot."""
        ...
    @overload
    def PlotTakeOnObjects(self,PlotPeriod:FBTime,ObjectsToPlot:list):
        """Plot the animation on given objects.
        This method will plot the animation of the take to the specified objects. Although the method supports boxes, the most common use case it to specify FBModels that have been cast to boxes.
        ### Parameters:
        - PlotPeriod: Period for the plot.
        - ObjectsToPlot: Objects to plot."""
        ...
    @overload
    def PlotTakeOnObjects(self,PlotOptions:FBPlotOptions,ObjectsToPlot:list):
        """Plot the animation on given objects.
        This method will plot the animation of the take to the specified objects. Although the method supports boxes, the most common use case it to specify FBModels that have been cast to boxes.
        ### Parameters:
        - PlotOptions: Option parameters for plotting
        - ObjectsToPlot: Objects to plot."""
        ...
    def PlotTakeOnProperties(self,PlotPeriod:FBTime,PropertiesToPlot:list):
        """Plot the animation on given properties.
        Will plot the animation of the take in question on the given properties in the scene.
        ### Parameters:
        - PlotPeriod: Period for the plot.
        - PropertiesToPlot: Properties to plot."""
        ...
    @overload
    def PlotTakeOnSelected(self,PlotPeriod:FBTime):
        """Plot the animation on selected models.
        Will plot the animation of the take in question on the selected models in the scene.
        ### Parameters:
        - PlotPeriod: Period for the plot."""
        ...
    @overload
    def PlotTakeOnSelected(self,PlotOptions:FBPlotOptions):
        """Plot the animation on selected models.
        Will plot the animation of the take in question on the selected models in the scene.
        ### Parameters:
        - PlotOptions: Option parameters for plotting"""
        ...
    @overload
    def PlotTakeOnSelectedProperties(self,PlotPeriod:FBTime):
        """Plot the animation on selected properties.
        Will plot the animation of the take in question on the selected properties in the scene.
        ### Parameters:
        - PlotPeriod: Period for the plot."""
        ...
    @overload
    def PlotTakeOnSelectedProperties(self,PlotOptions:FBPlotOptions):
        """Plot the animation on selected properties.
        Will plot the animation of the take in question on the selected properties in the scene.
        ### Parameters:
        - PlotOptions: Option parameters for plotting"""
        ...
    def RemoveLayer(self,LayerIndex:int):
        """Remove a layer.
        ### Parameters:
        - LayerIndex: Layer with at the specified index will be removed."""
        ...
    def SetCurrentLayer(self,LayerIndex:int):
        """Set the current layer for the take.
        Note that this will not deselect the other layers.
        ### Parameters:
        - LayerIndex: The layer index to be set as the current one."""
        ...
    def SetLayerRealSelection(self,bValue:bool):
        """Set real selection for layer.
        This method is used to specify if using the SelectLayer method of the FBAnimationLayer object will also select the FBComponent object. In previous version of MotionBuilder, an animation layer was always selected, causing the layer to be displayed in the property editor. Also, when parsing the selected objects in the SDK, a layer would always be there. Setting this value to false will prevent this.
        ### Parameters:
        - bValue: True if future layer selection will also select the FBComponent object."""
        ...
    def SetTimeMarkAction(self,Index:int,Action:FBTimeMarkAction)->bool:
        """Sets a new action for an existing time mark.
        ### Parameters:
        - Index: Index of the time mark.
        - Action: The new action for the time mark.
        
        ### Returns:
        True if the operation is successful, false otherwise."""
        ...
    def SetTimeMarkColor(self,Index:int,Color:FBColor)->bool:
        """Sets a new color for an existing time mark.
        ### Parameters:
        - Index: Index of the time mark.
        - Color: The new color for the time mark.
        
        ### Returns:
        True if the operation is successful, false otherwise."""
        ...
    def SetTimeMarkName(self,Index:int,Name:str)->bool:
        """Sets a new name for an existing time mark.
        ### Parameters:
        - Index: Index of the time mark.
        - Name: The new name for the time mark.
        
        ### Returns:
        True if the operation is successful, false otherwise."""
        ...
    def SetTimeMarkTime(self,Index:int,Time:FBTime)->int:
        """Sets a new time for an existing time mark.
        Note: Internally, the time marks are stored in time order. Modifying the time of a time mark may modify the index of all time marks.
        ### Parameters:
        - Index: Index of the time mark.
        - Time: The new time for the time mark.
        
        ### Returns:
        The new index of the modified time mark."""
        ...
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of take."""
        ...
class FBFCurve(FBComponent):
    Keys:FBPropertyListFCurveKey
    def CreateInterpolatorCurve(self,CurveType:FBInterpolatorCurveType)->FBFCurve:
        """Create and interpolator curve.
        ### Parameters:
        - CurveType: Interpolator curve type to create."""
        ...
    def EditBegin(self,KeyCount:int=-1):
        """Setup function to begin adding keys.
        ### Parameters:
        - KeyCount: Key to begin adding at(default is -1)."""
        ...
    def EditClear(self):
        """Empty FCurve of all keys."""
        ...
    def EditEnd(self,KeyCount:int=-1):
        """End key adding sequence.
        ### Parameters:
        - KeyCount: Key to finish adding at (default is -1)."""
        ...
    def Evaluate(self,Time:FBTime)->float:
        """Evaluate FCurve at Time .
        ### Parameters:
        - Time: Time at which FCurve is to be evaluated.
        
        ### Returns:
        Value of FCurve at Time ."""
        ...
    def GetPostExtrapolationCount(self)->int:
        """Get count for post extrapolation."""
        ...
    def GetPostExtrapolationMode(self)->FBExtrapolationMode:
        """Get modes for post extrapolation."""
        ...
    def GetPreExtrapolationCount(self)->int:
        """Get count for pre extrapolation."""
        ...
    def GetPreExtrapolationMode(self)->FBExtrapolationMode:
        """Get modes for pre extrapolation."""
        ...
    def KeyAdd(self,Time:FBTime,Value:float)->int:
        """Add a key at the specified time.
        ### Parameters:
        - Time: Time at which to insert the key.
        - Value: Value of the key.
        ### Returns:
        The position of the new key in the list of FCurve keys.
        
        ### Warning:
        Since there are no parameter to indicate the interpolation and tangent mode, the neighbor keys may be affected by the newly inserted key."""
        ...
    @overload
    def KeyDelete(self,StartIndex:int,StopIndex:int)->bool:
        """Delete keys within an index range.
        This function is much faster than multiple removes.
        ### Parameters:
        - StartIndex: Index of first deleted key.
        - StopIndex: Index of last deleted key.
        
        ### Returns:
        True if the delete operation is successful, false otherwise (e.g. the FCurve is locked, the index range is invalid, etc.)."""
        ...
    @overload
    def KeyDelete(self,Start:FBTime,Stop:FBTime,bInclusive:bool=False)->bool:
        """Delete keys within a time range.
        This function is much faster than multiple removes.
        ### Parameters:
        - Start: Start of time range.
        - Stop: End of time range.
        - bInclusive: True to include within the time range the keys at StartTime and StopTime, false otherwise.
        
        ### Returns:
        True if the delete operation is successful, false otherwise (e.g. the FCurve is locked, no keys found within the time range, etc.)."""
        ...
    def KeyDeleteByIndexRange(self,arg2,arg3)->bool:...
    def KeyDeleteByTimeRange(self,arg2:FBTime,arg3:FBTime,arg4=None)->bool:...
    def KeyGetInterpolation(self,Index:int)->FBInterpolation:
        """Get the key interpolation type at the specified index.
        ### Parameters:
        - Index: Index of the key to query.
        
        ### Returns:
        Type of interpolation."""
        ...
    def KeyGetLeftBezierTangent(self,Index:int)->float:
        """Get the key left bezier tangent value at the specified index.
        ### Parameters:
        - Index: Index of the key to query.
        
        ### Returns:
        Left bezier tangent."""
        ...
    def KeyGetLeftDerivative(self,Index:int)->float:
        """Get the key left derivative value at the specified index.
        ### Parameters:
        - Index: Index of the key to query.
        
        ### Returns:
        Left derivative value, in units/seconds."""
        ...
    def KeyGetLeftTangentWeight(self,Index:int)->float:
        """Get the key left tangent weight at the specified index.
        ### Parameters:
        - Index: Index of the key to query.
        
        ### Returns:
        Left tangent weight."""
        ...
    def KeyGetMarkedForManipulation(self,Index:int)->bool:
        """Get the key manipulation state.
        ### Parameters:
        - Index: Index of the key to query.
        
        ### Returns:
        True if the key is being manipulated, false otherwise."""
        ...
    def KeyGetRightBezierTangent(self,Index:int)->float:
        """Get the key right bezier tangent value at the specified index.
        ### Parameters:
        - Index: Index of the key to query.
        
        ### Returns:
        Right bezier tangent."""
        ...
    def KeyGetRightDerivative(self,Index:int)->float:
        """Get the key right derivative value at the specified index.
        ### Parameters:
        - Index: Index of the key to query.
        
        ### Returns:
        Right derivative value, in units/seconds."""
        ...
    def KeyGetRightTangentWeight(self,Index:int)->float:
        """Get the key right tangent weight at the specified index.
        ### Parameters:
        - Index: Index of the key to query.
        
        ### Returns:
        Right tangent weight."""
        ...
    def KeyGetSelected(self,Index:int)->bool:
        """Get the key selected state.
        ### Parameters:
        - Index: Index of the key to query.
        
        ### Returns:
        True if the key is selected, false otherwise."""
        ...
    def KeyGetTCBBias(self,Index:int)->float:
        """Get the key bias value at the specified index (TCB key).
        ### Parameters:
        - Index: Index of the key to query.
        
        ### Returns:
        Bias value."""
        ...
    def KeyGetTCBContinuity(self,Index:int)->float:
        """Get the key continuity value at the specified index (TCB key).
        ### Parameters:
        - Index: Index of the key to query.
        
        ### Returns:
        Continuity value."""
        ...
    def KeyGetTCBTension(self,Index:int)->float:
        """Get the key tension value at the specified index (TCB key).
        ### Parameters:
        - Index: Index of the key to query.
        
        ### Returns:
        Tension value."""
        ...
    def KeyGetTangentBreak(self,Index:int)->bool:
        """Get the key tangent's break status at the specified index.
        ### Parameters:
        - Index: Index of the key to query.
        
        ### Returns:
        Tangent's break status."""
        ...
    def KeyGetTangentClampMode(self,Index:int)->FBTangentClampMode:
        """Get the key tangent's clamp method at the specified index.
        ### Parameters:
        - Index: Index of the key to query.
        
        ### Returns:
        Tangent's clamp method."""
        ...
    def KeyGetTangentConstantMode(self,Index:int)->FBTangentConstantMode:
        """Get the key tangent's constant mode at the specified index.
        ### Parameters:
        - Index: Index of the key to query.
        
        ### Returns:
        Tangent's constant mode."""
        ...
    def KeyGetTangentCustomIndex(self,Index:int)->FBTangentCustomIndex:
        """Get the key tangent's custom index at the specified index.
        ### Parameters:
        - Index: Index of the key to query.
        
        ### Returns:
        Tangent's custom index."""
        ...
    def KeyGetTangentMode(self,Index:int)->FBTangentMode:
        """Get the key tangent mode at the specified index.
        ### Parameters:
        - Index: Index of the key to query.
        
        ### Returns:
        Tangent calculation method."""
        ...
    def KeyGetTangentWeightMode(self,Index:int)->FBTangentWeightMode:
        """Get the tangent weight mode for a key.
        ### Parameters:
        - Index: Index of the key to query.
        
        ### Returns:
        Current weight mode."""
        ...
    def KeyGetTime(self,Index:int)->FBTime:
        """Get the key time value at the specified index.
        ### Parameters:
        - Index: Index of the key to query.
        
        ### Returns:
        Time of key."""
        ...
    def KeyGetValue(self,Index:int)->float:
        """Get the key value at the specified index.
        ### Parameters:
        - Index: Index of the key to query.
        
        ### Returns:
        Value of the key."""
        ...
    def KeyInsert(self,Time:FBTime,Interpolation:FBInterpolation=FBInterpolation.kFBInterpolationCubic,TangentMode:FBTangentMode=FBTangentMode.kFBTangentModeAuto):
        """Insert a key without affecting the curve shape.
        ### Parameters:
        - Time: Time at which the key is to be inserted.
        - Interpolation: Interpolation type of the inserted key, default value is Cubic interpolation.
        - TangentMode: Tangent calculation method of the inserted key, default value is Auto (Smooth)."""
        ...
    @overload
    def KeyOffset(self,OffsetTime:FBTime,StartIndex:int,StopIndex:int)->bool:
        """Offset keys within an index range by a given offset time.
        When offsetting many keys at once, all non-moving keys that are situated in the target range are deleted automatically, to preserve the animation being offset.
        ### Parameters:
        - OffsetTime: The offset time to apply on keys.
        - StartIndex: Index of first key to be offset.
        - StopIndex: Index of last key to be offset.
        
        ### Returns:
        True if the offset operation is successful, false otherwise (e.g. the FCurve is locked, the index range is invalid, etc.)."""
        ...
    @overload
    def KeyOffset(self,OffsetTime:FBTime,StartTime:FBTime=FBTime.MinusInfinity,StopTime:FBTime=FBTime.Infinity,bInclusive:bool=True)->bool:
        """Offset keys within a time range by a given offset time.
        Non-moving keys that are situated in the target range are deleted automatically, to preserve the animation being offset.
        ### Parameters:
        - OffsetTime: The offset time to apply on keys.
        - StartTime: Start of time range.
        - StopTime: End of time range.
        - bInclusive: True to include within the time range the keys at StartTime and StopTime, false otherwise.
        
        ### Returns:
        True if the offset operation is successful, false otherwise (e.g. the FCurve is locked, no keys found within the time range, etc.)."""
        ...
    def KeyReplaceBy(self,Source:FBFCurve,Start:FBTime=FBTime.MinusInfinity,Stop:FBTime=FBTime.Infinity,bUseExactGivenSpan:bool=False,bKeyStartEndOnNoKey:bool=True):
        """Replace keys within a range in current function curve with keys found in a source function curve.
        ### Parameters:
        - Source: Source function curve.
        - Start: Start of time range.
        - Stop: End of time range.
        - bUseExactGivenSpan: When false , the time of the first and last key in the range will be used.
        - bKeyStartEndOnNoKey: When true , inserts a key at the beginning and at the end of the range if there is no key to insert."""
        ...
    def KeySetInterpolation(self,Index:int,Value:FBInterpolation):
        """Set the key interpolation type at the specified index.
        ### Parameters:
        - Index: Index of the key to set.
        - Value: Type of interpolation."""
        ...
    def KeySetLeftBezierTangent(self,Index:int,Value:float):
        """Set the key left bezier tangent value at the specified index.
        ### Parameters:
        - Index: Index of the key to set.
        - Value: Left bezier tangent."""
        ...
    def KeySetLeftDerivative(self,Index:int,Value:float):
        """Set the key left derivative value at the specified index.
        ### Parameters:
        - Index: Index of the key to set.
        - Value: Left derivative value, in units/seconds."""
        ...
    def KeySetLeftTangentWeight(self,Index:int,Value:float):
        """Set the key left tangent weight at the specified index.
        ### Parameters:
        - Index: Index of the key to set.
        - Value: Left tangent weight."""
        ...
    def KeySetMarkedForManipulation(self,Index:int,bValue:bool)->bool:
        """Set the key manipulation state.
        ### Parameters:
        - Index: Index of the key to set.
        - bValue: New manipulation state.
        
        ### Returns:
        True if the operation was successful, false otherwise."""
        ...
    def KeySetRightBezierTangent(self,Index:int,Value:float):
        """Set the key right bezier tangent value at the specified index.
        ### Parameters:
        - Index: Index of the key to set.
        - Value: Right bezier tangent."""
        ...
    def KeySetRightDerivative(self,Index:int,Value:float):
        """Set the key right derivative value at the specified index.
        ### Parameters:
        - Index: Index of the key to set.
        - Value: Right derivative value, in units/seconds."""
        ...
    def KeySetRightTangentWeight(self,Index:int,Value:float):
        """Set the key right tangent weight at the specified index.
        ### Parameters:
        - Index: Index of the key to set.
        - Value: Right tangent weight."""
        ...
    def KeySetSelected(self,Index:int,bValue:bool)->bool:
        """Set the key selected state.
        ### Parameters:
        - Index: Index of the key to set.
        - bValue: New selection state.
        
        ### Returns:
        True if the operation was successful, false otherwise."""
        ...
    def KeySetTCBBias(self,Index:int,Value:float):
        """Set the key bias value at the specified index (TCB key).
        ### Parameters:
        - Index: Index of the key to set.
        - Value: Bias value."""
        ...
    def KeySetTCBContinuity(self,Index:int,Value:float):
        """Set the key continuity value at the specified index (TCB key).
        ### Parameters:
        - Index: Index of the key to set.
        - Value: Continuity value."""
        ...
    def KeySetTCBTension(self,Index:int,Value:float):
        """Set the key tension value at the specified index (TCB key).
        ### Parameters:
        - Index: Index of the key to set.
        - Value: Tension value."""
        ...
    def KeySetTangentBreak(self,Index:int,bValue:bool):
        """Set the key tangent's break status at the specified index.
        ### Parameters:
        - Index: Index of the key to set.
        - bValue: Tangent's break status."""
        ...
    def KeySetTangentClampMode(self,Index:int,Value:FBTangentClampMode):
        """Set the key tangent's clamp method at the specified index.
        ### Parameters:
        - Index: Index of the key to set.
        - Value: Tangent's clamp method."""
        ...
    def KeySetTangentConstantMode(self,Index:int,Value:FBTangentConstantMode):
        """Set the key tangent's constant mode at the specified index.
        ### Parameters:
        - Index: Index of the key to set.
        - Value: Tangent's constant mode."""
        ...
    def KeySetTangentCustomIndex(self,Index:int,Value:FBTangentCustomIndex):
        """Set the key tangent's custom index at the specified index.
        ### Parameters:
        - Index: Index of the key to set.
        - Value: Tangent's custom index."""
        ...
    def KeySetTangentMode(self,Index:int,Value:FBTangentMode):
        """Set the key tangent mode at the specified index.
        ### Parameters:
        - Index: Index of the key to set.
        - Value: Tangent calculation method."""
        ...
    def KeySetTangentWeightMode(self,Index:int,Value:FBTangentWeightMode):
        """Change the tangent weight for a key.
        Setting the value for LeftTangentWeight/RightTangentWeight will also activate the weight for that part. Please see the note provided with FBTangentWeightMode for the left weight of a key.
        ### Parameters:
        - Index: Index of the key to set.
        - Value: Set the Value according to the desired mode, kFBTangentWeightModeNone to disable it."""
        ...
    def KeySetTime(self,Index:int,Value:FBTime):
        """Set the key time value at the specified index.
        ### Parameters:
        - Index: Index of the key to set.
        - Value: Time of key."""
        ...
    def KeySetValue(self,Index:int,Value:float):
        """Set the key value at the specified index.
        ### Parameters:
        - Index: Index of the key to set.
        - Value: Value of the key."""
        ...
    def SetPostExtrapolationCount(self,Count:int):
        """Set count for post extrapolation."""
        ...
    def SetPostExtrapolationMode(self,ExtrapolationMode:FBExtrapolationMode):
        """Set modes for post extrapolation."""
        ...
    def SetPreExtrapolationCount(self,Count:int):
        """Set count for pre extrapolation."""
        ...
    def SetPreExtrapolationMode(self,ExtrapolationMode:FBExtrapolationMode):
        """Set modes for pre extrapolation."""
        ...
    def __init__(self):...
class FBTimeSpan():
    def GetDirection(self)->int:
        """Get the direction of the timespan.
        Returns 1 if positive, -1 otherwise.
        ### Returns:
        Direction of timespan."""
        ...
    def GetDuration(self)->FBTime:
        """Get the unsigned duration value of a timespan.
        ### Returns:
        Unsigned duration of the timespan."""
        ...
    def GetSignedDuration(self)->FBTime:
        """Get the signed duration value of a timespan.
        ### Returns:
        Signed duration of the timespan."""
        ...
    def GetStart(self)->FBTime:
        """Get the start/stop time.
        ### Returns:
        Start/Stop time."""
        ...
    def GetStop(self)->FBTime:...
    def Set(self,Start:FBTime,Stop:FBTime):
        """Set the TimeSpan.
        ### Parameters:
        - Start: Start time.
        - Stop: Stop time."""
        ...
    def __init__(self,Start:FBTime=0,Stop:FBTime=0):
        """### Parameters:
        - Start: Start time(default=0).
        - Stop: Stop time(default=0)."""
        ...
class FBTimeWarpManager(FBComponent):
    def ApplyTimeWarp(self,Take:FBTake,EvalProp:FBProperty,TimeWarp:FBAnimationNode)->bool:
        """Apply the TimeWarp in a Take to an evaluation property, just connect the storing property for the TimeWarp to the evaluation property.
        ### Parameters:
        - Take: The Take where the TimeWarp in.
        - EvalProp: The evaluation property to be applied on.
        - TimeWarp: The TimeWarp to apply.
        
        ### Returns:
        True if apply successfully."""
        ...
    def DestroyTimeWarpFromTake(self,Take:FBTake,TimeWarp:FBAnimationNode):
        """Destroy the TimeWarp in a Take, and removed from the DataSet.
        ### Parameters:
        - Take: The Take where the TimeWarp in.
        - TimeWarp: The TimeWarp to be Destroyed."""
        ...
    def FindTimeWarpNickNumberGlobal(self,TimeWarp:FBAnimationNode)->int:
        """Find the Nick Number of one timewarp globally
        ### Parameters:
        - TimeWarp: The TimeWarp queried.
        
        ### Returns:
        the Nick Number of the timewarp."""
        ...
    def GetTimeWarpAtIndex(self,Take:FBTake,Index:int)->FBAnimationNode:
        """Get the TimeWarp in a Take At specific Index.
        ### Parameters:
        - Take: The Take queried.
        - Index: The index of the TimeWarp.
        
        ### Returns:
        TimeWarp at specific Index in a Take."""
        ...
    def GetTimeWarpCount(self,Take:FBTake)->int:
        """Get the count of TimeWarp in a Take.
        ### Parameters:
        - Take: The Take queried.
        
        ### Returns:
        the TimeWarp count."""
        ...
    def GetTimeWarpFromNickNumber(self,Take:FBTake,Number:int)->FBAnimationNode:
        """Get the timeWarp of specific Nick Number in a Take.
        ### Parameters:
        - Take: The Take queried.
        - Number: the Nick Number of one TimeWarp.
        
        ### Returns:
        the TimeWarp of specific Nick Number."""
        ...
    def GetTimeWarpNickNumber(self,Take:FBTake,TimeWarp:FBAnimationNode)->int:
        """Get the Nick Number of one TimeWarp in a Take.
        ### Parameters:
        - Take: The Take queried.
        - TimeWarp: The TimeWarp queried.
        
        ### Returns:
        the Nick Number of one TimeWarp."""
        ...
    def GetTimeWarpNickNumberAtIndex(self,Take:FBTake,Index:int)->int:
        """Get the Nick Number of one TimeWarp At specific index in a Take.
        ### Parameters:
        - Take: The Take queried.
        - Index: The index a TimeWarp at.
        
        ### Returns:
        the Nick Number of one TimeWarp At specific index."""
        ...
    def RemoveTimeWarp(self,Take:FBTake,EvalProp:FBProperty):
        """Undo apply a timeWarp in a Take to an evaluation property, just disconnect the evaluation property from storing property.
        ### Parameters:
        - Take: The Take where the TimeWarp evaluation property connected is in.
        - EvalProp: The evaluation property connected a TimeWarp in the storing property of one take."""
        ...
    def RemoveTimeWarpFromScene(self,TimeWarp:FBAnimationNode):
        """Remove a TimeWarp from Scene.
        ### Parameters:
        - TimeWarp: The TimeWarp to be Removed."""
        ...
    def SetTimeWarpNickNumber(self,Take:FBTake,TimeWarp:FBAnimationNode,Number:int)->bool:
        """Set the Nick Number of one TimeWarp in a Take.
        ### Parameters:
        - Take: The Take specific.
        - TimeWarp: The TimeWarp specific.
        - Number: The Nick Number to set.
        
        ### Returns:
        True if set successfully."""
        ...
    def TimeWarpAddToTake(self,Take:FBTake,TimeWarp:FBAnimationNode,NickNumber:int=0):
        """Add one TimeWarp to a Take.
        ### Parameters:
        - Take: The Take one TimeWarp added to.
        - TimeWarp: The TimeWarp to be added.
        - NickNumber: The Nick Number for the TimeWarp."""
        ...
    def TimeWarpClearTake(self,Take:FBTake):
        """Clear all TimeWarp in a Take, and removed from the DataSet.
        ### Parameters:
        - Take: The Take to be cleared."""
        ...
    def TimeWarpCopyTake(self,DstTake:FBTake,SrcTake:FBTake):
        """Copy all the TimeWarp in one Take, add to another Take.
        ### Parameters:
        - DstTake: Copy all TimeWarp to.
        - SrcTake: Copy all TimeWarp from."""
        ...
    def TimeWarpCreateNew(self,Name:str)->FBAnimationNode:
        """Create a TimeWarp with a specific name
        ### Parameters:
        - Name: The name for the TimeWarp.
        
        ### Returns:
        the TimeWarp created."""
        ...
    def TimeWarpInitTake(self,Take:FBTake):
        """Allocate container for the TimeWarp in one Take.
        ### Parameters:
        - Take: The Take allocated for."""
        ...
    def TimeWarpMergeCurveNode(self,Take:FBTake,EvalProp:FBProperty,Node:FBAnimationNode,TimeWarpNode:FBAnimationNode):
        """Merge the TimeWarp to a function curve, and Remove the connection between the storing property and the evaluation property for the TimeWarp
        ### Parameters:
        - Take: The Take that the TimeWarp is in.
        - EvalProp: the evaluation property the TimeWarp connected.
        - Node: The function curve to merge on.
        - pTimeWarNode: The TimeWarp to be merged."""
        ...
    def TimeWarpRename(self,Take:FBTake,TimeWarp:FBAnimationNode,NewName:str):
        """Rename a TimeWarp
        ### Parameters:
        - Take: The Take where the timeWarp is in.
        - TimeWarp: The TimeWarp to be renamed.
        - NewName: The new name for the TimeWarp."""
        ...
    def TimeWarpTakeChange(self):
        """Call registered callbacks when changes related to TimeWarp happen."""
        ...
    def __init__(self):
        """### Note:
        protect"""
        ...
class FBToolLayoutManager(FBComponent):
    def CreateLayout(self,LayoutName:str)->str:
        """Create a new layout from the current layout state.
        ### Parameters:
        - LayoutName: The new layout name to create.
        
        ### Returns:
        The new layout's name (could be different that the one supplied) if the operation is successful, nullptr (C++) or None (Python) otherwise."""
        ...
    @overload
    def DeleteLayout(self,LayoutIdx:int)->bool:
        """Delete the layout associated with the given layout index.
        Deleting a factory layout is not permitted.
        ### Parameters:
        - LayoutIdx: The layout index to delete.
        
        ### Returns:
        True if the operation is successful, false otherwise."""
        ...
    @overload
    def DeleteLayout(self,LayoutName:str)->bool:
        """Delete the layout with the given layout name.
        Deleting a factory layout is not permitted.
        ### Parameters:
        - LayoutName: The layout name to delete.
        
        ### Returns:
        True if the operation is successful, false otherwise."""
        ...
    def GetAutoUpdateLayout(self)->bool:
        """Get the 'Auto-update Layout' state value.
        ### Returns:
        The 'Auto-update Layout' state value."""
        ...
    def GetCurrentLayoutIdx(self)->int:
        """Get the layout index of the current layout.
        ### Returns:
        The layout index of the current layout."""
        ...
    def GetCurrentLayoutName(self)->str:
        """Get the name of the current layout.
        ### Returns:
        The name of the current layout."""
        ...
    def GetCustomLayoutCount(self)->int:
        """Get the number of custom layouts.
        ### Returns:
        The number of custom layouts."""
        ...
    def GetFactoryLayoutCount(self)->int:
        """Get the number of factory layouts.
        ### Returns:
        The number of factory layouts."""
        ...
    def GetLayoutName(self,LayoutIdx:int)->str:
        """Get the layout name associated with the given layout index.
        ### Parameters:
        - LayoutIdx: The layout index to query. The factory layouts are using negative indices.
        
        ### Returns:
        The layout name if the operation is successful, nullptr (C++) or None (Python) otherwise."""
        ...
    def RenameLayout(self,OldLayoutName:str,NewLayoutName:str)->str:
        """Rename a layout.
        Renaming a factory layout is not permitted.
        ### Parameters:
        - OldLayoutName: The layout's name to rename.
        - NewLayoutName: The new layout name.
        
        ### Returns:
        The new layout's name (could be different that the one supplied) if the operation is successful, nullptr (C++) or None (Python) otherwise."""
        ...
    def SetAutoUpdateLayout(self,bAutoUpdate:bool)->bool:
        """Set the 'Auto-update Layout' state value.
        ### Parameters:
        - bAutoUpdate: The 'Auto-update Layout' state value.
        
        ### Returns:
        True if the operation is successful, false otherwise."""
        ...
    @overload
    def SetCurrentLayout(self,LayoutIdx:int)->bool:
        """Set the current layout from the given layout index.
        ### Parameters:
        - LayoutIdx: The layout index to set as the current layout. The factory layouts are using negative indices.
        
        ### Returns:
        True if the operation is successful, false otherwise."""
        ...
    @overload
    def SetCurrentLayout(self,LayoutName:str)->bool:
        """Set the current layout from the given layout name.
        ### Parameters:
        - LayoutName: The layout's name to set as the current layout.
        
        ### Returns:
        True if the operation is successful, false otherwise."""
        ...
    def UpdateCurrentLayout(self)->bool:
        """Update the current layout from the current layout state.
        Updating a factory layout is not permitted.
        ### Returns:
        True if the operation is successful, false otherwise."""
        ...
    def __init__(self):
        """Protected constructor, use TheOne() access instead."""
        ...
class FBTransportAudioManager(FBComponent):
    def GetAudioClip(self)->FBAudioClip:
        """Get the Audio Clip displayed on the Transport Tool.
        ### Returns:
        The Audio Clip displayed, nullptr (C++) / None (Python) if any."""
        ...
    def GetAudioTrack(self)->FBStoryTrack:
        """Get the Audio Track displayed on the Transport Tool.
        ### Returns:
        The Audio Track displayed, nullptr (C++) / None (Python) if any."""
        ...
    def GetLockPitchToSpeed(self)->bool:
        """Get the 'Lock Pitch to Speed' state.
        ### Returns:
        True if the 'Lock Pitch to Speed' state is set, false otherwise."""
        ...
    def GetShowAudio(self)->bool:
        """Get the 'Show Audio' state.
        ### Returns:
        True if the 'Show Audio' state is set, false otherwise."""
        ...
    def GetShowLeftChannel(self)->bool:
        """Get the 'Show Left Channel' state.
        ### Returns:
        True if the 'Show Left Channel' state is set, false otherwise."""
        ...
    def GetShowRightChannel(self)->bool:
        """Get the 'Show Right Channel' state.
        ### Returns:
        True if the 'Show Right Channel' state is set, false otherwise."""
        ...
    def RemoveAudio(self)->bool:
        """Remove the audio clip or audio track currently displayed on the Transport Tool.
        ### Returns:
        True if the operation is successful, false otherwise."""
        ...
    def SetAudioClip(self,AudioClip:FBAudioClip)->bool:
        """Set the Audio Clip to display on the Transport Tool.
        ### Parameters:
        - AudioClip: The Audio Clip to display.
        
        ### Returns:
        True if the operation is successful, false otherwise."""
        ...
    def SetAudioTrack(self,AudioTrack:FBStoryTrack)->bool:
        """Set the Audio Track to display on the Transport Tool.
        ### Parameters:
        - AudioTrack: The Audio Track to display.
        
        ### Returns:
        True if the operation is successful, false otherwise."""
        ...
    def SetLockPitchToSpeed(self,bLock:bool)->bool:
        """Set the 'Lock Pitch to Speed' state.
        ### Parameters:
        - bLock: True to lock pitch to speed, false otherwise.
        
        ### Returns:
        True if the operation is successful, false otherwise."""
        ...
    def SetShowAudio(self,bShow:bool)->bool:
        """Set the 'Show Audio' state.
        ### Parameters:
        - bShow: True to show the Audio waveform, false otherwise.
        
        ### Returns:
        True if the operation is successful, false otherwise."""
        ...
    def SetShowLeftChannel(self,bShow:bool)->bool:
        """Set the 'Show Left Channel' state.
        ### Parameters:
        - bShow: True to show the left channel, false otherwise.
        
        ### Returns:
        True if the operation is successful, false otherwise."""
        ...
    def SetShowRightChannel(self,bShow:bool)->bool:
        """Set the 'Show Right Channel' state.
        ### Parameters:
        - bShow: True to show the right channel, false otherwise.
        
        ### Returns:
        True if the operation is successful, false otherwise."""
        ...
    def __init__(self):
        """Protected constructor, use TheOne() access instead."""
        ...
class FBTreeNode(FBComponent):
    Checked:bool
    Reference:property
class FBUV():
    @overload
    def CopyFrom(self,arg2:FBUV)->FBUV:...
    @overload
    def CopyFrom(self,arg2:list)->FBUV:...
    def GetBufferAddress(self)->int:...
    def GetList(self)->list:...
    def IsEqual(self,arg2:FBUV)->bool:...
    def NotEqual(self,arg2:FBUV)->bool:...
    @overload
    def __add__(self,arg2:FBUV)->object:...
    @overload
    def __add__(self,arg2)->object:...
    def __getitem__(self,arg2)->float:...
    @overload
    def __iadd__(self,arg2:FBUV)->object:...
    @overload
    def __iadd__(self,arg2)->object:...
    @overload
    def __idiv__(self,arg2:FBUV)->object:...
    @overload
    def __idiv__(self,arg2)->object:...
    @overload
    def __imul__(self,arg2:FBUV)->object:...
    @overload
    def __imul__(self,arg2)->object:...
    @overload
    def __init__(self):
        """Represents a UV coordinate as a FBVector2 of floats in the range of 0.0f to 1.0f; value 0 is the U value, and value 1 is the V value.
        Definition at line 556 of file fbtypes.h ."""
        ...
    @overload
    def __init__(self,arg2:FBUV):...
    @overload
    def __init__(self,arg2:float,arg3:float):...
    @overload
    def __init__(self,arg2):...
    @overload
    def __init__(self,arg2:list):...
    @overload
    def __isub__(self,arg2:FBUV)->object:...
    @overload
    def __isub__(self,arg2)->object:...
    def __len__(self)->int:...
    @overload
    def __mul__(self,arg2:FBUV)->object:...
    @overload
    def __mul__(self,arg2)->object:...
    def __neg__(self)->object:...
    def __setitem__(self,arg2,arg3:float):...
    @overload
    def __sub__(self,arg2:FBUV)->object:...
    @overload
    def __sub__(self,arg2)->object:...
    @overload
    def __truediv__(self,arg2:FBUV)->object:...
    @overload
    def __truediv__(self,arg2)->object:...
class FBUndoManager(FBComponent):
    OnRedo:FBEvent
    OnRedoCompleted:FBEvent
    OnUndo:FBEvent
    OnUndoCompleted:FBEvent
    def ActiveOperation(self)->bool:
        """Determine if an undo operation is in action.
        ### Returns:
        true the Undo Manager is performing an Undo or a Redo operation."""
        ...
    def Clear(self)->bool:
        """Clear the undo and redo stacks.
        ### Returns:
        A boolean value indicating success (true) or failure (false)."""
        ...
    def Redo(self):
        """Redo last undone action."""
        ...
    def TransactionAddModelTRS(self,Model:FBModel)->bool:
        """Add Transaction if transaction stack is open.
        Quick Function to add Model TRS in Undo Stack
        ### Parameters:
        - Model: Model to backup TRS
        
        ### Returns:
        true if add transaction successfully."""
        ...
    def TransactionAddObjectDestroy(self,Object:FBComponent)->bool:
        """Add Transaction if transaction stack is open.
        Function to add object to destroy in Undo Stack. No need to call FBDelete() on the object after calling this function.
        ### Parameters:
        - Object: Object to backup
        
        ### Returns:
        true if add transaction successfully."""
        ...
    def TransactionAddProperty(self,Property:FBProperty)->bool:
        """Add Transaction if transaction stack is open.
        Quick Function to add property value in Undo Stack
        ### Parameters:
        - Property: Property to backup
        
        ### Returns:
        true if add transaction successfully."""
        ...
    def TransactionBegin(self,TransactionName:str)->bool:
        """Open transaction stack for adding transactions.
        Users should call TransactionBegin() /TransactionEnd() in pairs, Transaction stack must be closed before UI event callback return.
        ### Parameters:
        - TransactionName: Name of Transaction.
        
        ### Returns:
        true if open transaction stack successfully."""
        ...
    def TransactionEnd(self)->bool:
        """Close transaction stack.
        Users should call TransactionBegin() /TransactionEnd() in pairs, Transaction stack must be closed before UI event callback return.
        ### Returns:
        true if transaction close successfully."""
        ...
    def TransactionIsOpen(self)->bool:
        """Query if transaction stack is already open.
        ### Returns:
        true if transaction is already open."""
        ...
    def Undo(self,bNoRedo:bool=False):
        """Undo last action.
        ### Parameters:
        - bNoRedo: If true, once the action is undone, it cannot be redone."""
        ...
    def __init__(self):...
class FBUserObject(FBBox):
    def __init__(self,arg2:str):...
class FBVector2d():
    @overload
    def CopyFrom(self,arg2:FBVector2d)->FBVector2d:...
    @overload
    def CopyFrom(self,arg2:list)->FBVector2d:...
    def GetBufferAddress(self)->int:...
    def GetList(self)->list:...
    def IsEqual(self,arg2:FBVector2d)->bool:...
    def NotEqual(self,arg2:FBVector2d)->bool:...
    @overload
    def __add__(self,arg2:FBVector2d)->object:...
    @overload
    def __add__(self,arg2)->object:...
    def __getitem__(self,arg2)->float:...
    @overload
    def __iadd__(self,arg2:FBVector2d)->object:...
    @overload
    def __iadd__(self,arg2)->object:...
    @overload
    def __idiv__(self,arg2:FBVector2d)->object:...
    @overload
    def __idiv__(self,arg2)->object:...
    @overload
    def __imul__(self,arg2:FBVector2d)->object:...
    @overload
    def __imul__(self,arg2)->object:...
    @overload
    def __init__(self):
        """2D vector.
        Definition at line 1 of file fbtypes.h ."""
        ...
    @overload
    def __init__(self,arg2:FBVector2d):...
    @overload
    def __init__(self,arg2,arg3):...
    @overload
    def __init__(self,arg2):...
    @overload
    def __init__(self,arg2:list):...
    @overload
    def __isub__(self,arg2:FBVector2d)->object:...
    @overload
    def __isub__(self,arg2)->object:...
    def __len__(self)->int:...
    @overload
    def __mul__(self,arg2:FBVector2d)->object:...
    @overload
    def __mul__(self,arg2)->object:...
    def __neg__(self)->object:...
    def __setitem__(self,arg2,arg3):...
    @overload
    def __sub__(self,arg2:FBVector2d)->object:...
    @overload
    def __sub__(self,arg2)->object:...
    @overload
    def __truediv__(self,arg2:FBVector2d)->object:...
    @overload
    def __truediv__(self,arg2)->object:...
class FBVector3d():
    @overload
    def CopyFrom(self,arg2:FBVector3d)->FBVector3d:...
    @overload
    def CopyFrom(self,arg2:list)->FBVector3d:...
    def CrossProduct(self,arg2:FBVector3d)->FBVector3d:...
    def Distance(self,arg2:FBVector3d)->float:...
    def DotProduct(self,arg2:FBVector3d)->float:...
    def GetBufferAddress(self)->int:...
    def GetList(self)->list:...
    def IsEqual(self,arg2:FBVector3d)->bool:...
    def Length(self)->float:
        """Get the length of a vector.
        ### Returns:
        Length of vector pV ."""
        ...
    def Normalize(self)->FBVector3d:...
    def NotEqual(self,arg2:FBVector3d)->bool:...
    def SquareLength(self)->float:...
    @overload
    def __add__(self,arg2:FBVector3d)->object:...
    @overload
    def __add__(self,arg2)->object:...
    def __getitem__(self,Index:int)->float:...
    @overload
    def __iadd__(self,arg2:FBVector3d)->object:...
    @overload
    def __iadd__(self,arg2)->object:...
    @overload
    def __idiv__(self,arg2:FBVector3d)->object:...
    @overload
    def __idiv__(self,arg2)->object:...
    @overload
    def __imul__(self,arg2:FBVector3d)->object:...
    @overload
    def __imul__(self,arg2)->object:...
    @overload
    def __init__(self):...
    @overload
    def __init__(self,Value:FBVector3d):
        """Constructor from array.
        ### Parameters:
        - Value: Array to take values from."""
        ...
    @overload
    def __init__(self,p1:float,p2:float,p3:float):
        """### Parameters:
        - p1: First element
        - p2: Second element.
        - p3: Third element(default=0)."""
        ...
    @overload
    def __init__(self,Vector:List[float]):...
    @overload
    def __init__(self,arg2:list):...
    @overload
    def __isub__(self,arg2:FBVector3d)->object:...
    @overload
    def __isub__(self,arg2)->object:...
    def __len__(self)->int:...
    @overload
    def __mul__(self,arg2:FBVector3d)->object:...
    @overload
    def __mul__(self,arg2)->object:...
    def __neg__(self)->object:...
    def __setitem__(self,arg2,arg3):...
    @overload
    def __sub__(self,arg2:FBVector3d)->object:...
    @overload
    def __sub__(self,arg2)->object:...
    @overload
    def __truediv__(self,arg2:FBVector3d)->object:...
    @overload
    def __truediv__(self,arg2)->object:...
class FBVector4d():
    @overload
    def CopyFrom(self,arg2:FBVector4d)->FBVector4d:...
    @overload
    def CopyFrom(self,arg2:list)->FBVector4d:...
    def CrossProduct(self,arg2:FBVector4d)->FBVector4d:...
    def Distance(self,arg2:FBVector4d)->float:...
    def DotProduct(self,arg2:FBVector4d)->float:...
    def GetBufferAddress(self)->int:...
    def GetList(self)->list:...
    def IsEqual(self,arg2:FBVector4d)->bool:...
    def Length(self)->float:
        """Get the length of a vector.
        ### Returns:
        Length of vector pV ."""
        ...
    def Normalize(self)->FBVector4d:...
    def NotEqual(self,arg2:FBVector4d)->bool:...
    def SquareLength(self)->float:...
    @overload
    def __add__(self,arg2:FBVector4d)->object:...
    @overload
    def __add__(self,arg2)->object:...
    def __getitem__(self,Index:int)->float:...
    @overload
    def __iadd__(self,arg2:FBVector4d)->object:...
    @overload
    def __iadd__(self,arg2)->object:...
    @overload
    def __idiv__(self,arg2:FBVector4d)->object:...
    @overload
    def __idiv__(self,arg2)->object:...
    @overload
    def __imul__(self,arg2:FBVector4d)->object:...
    @overload
    def __imul__(self,arg2)->object:...
    @overload
    def __init__(self):...
    @overload
    def __init__(self,Value:FBVector4d):
        """Constructor from array.
        ### Parameters:
        - Value: Array to take values from."""
        ...
    @overload
    def __init__(self,p1:float,p2:float,p3:float,p4:float):
        """### Parameters:
        - p1: First element
        - p2: Second element.
        - p3: Third element.
        - p4: Fourth element."""
        ...
    @overload
    def __init__(self,Vector:List[float]):...
    @overload
    def __init__(self,arg2:list):...
    @overload
    def __isub__(self,arg2:FBVector4d)->object:...
    @overload
    def __isub__(self,arg2)->object:...
    def __len__(self)->int:...
    @overload
    def __mul__(self,arg2:FBVector4d)->object:...
    @overload
    def __mul__(self,arg2)->object:...
    def __neg__(self)->object:...
    def __setitem__(self,arg2,arg3):...
    @overload
    def __sub__(self,arg2:FBVector4d)->object:...
    @overload
    def __sub__(self,arg2)->object:...
    @overload
    def __truediv__(self,arg2:FBVector4d)->object:...
    @overload
    def __truediv__(self,arg2)->object:...
class FBVertex():
    @overload
    def CopyFrom(self,arg2:FBVertex)->FBVertex:...
    @overload
    def CopyFrom(self,arg2:list)->FBVertex:...
    def CrossProduct(self,arg2:FBVertex)->FBVertex:...
    def Distance(self,arg2:FBVertex)->float:...
    def DotProduct(self,arg2:FBVertex)->float:...
    def GetBufferAddress(self)->int:...
    def GetList(self)->list:...
    def IsEqual(self,arg2:FBVertex)->bool:...
    def Length(self)->float:
        """Get the length of a vector.
        ### Returns:
        Length of vector pV ."""
        ...
    def Normalize(self)->FBVertex:...
    def NotEqual(self,arg2:FBVertex)->bool:...
    def SquareLength(self)->float:...
    @overload
    def __add__(self,arg2:FBVertex)->object:...
    @overload
    def __add__(self,arg2)->object:...
    def __getitem__(self,arg2)->float:...
    @overload
    def __iadd__(self,arg2:FBVertex)->object:...
    @overload
    def __iadd__(self,arg2)->object:...
    @overload
    def __idiv__(self,arg2:FBVertex)->object:...
    @overload
    def __idiv__(self,arg2)->object:...
    @overload
    def __imul__(self,arg2:FBVertex)->object:...
    @overload
    def __imul__(self,arg2)->object:...
    @overload
    def __init__(self):
        """Vertex.
        Definition at line 556 of file fbtypes.h ."""
        ...
    @overload
    def __init__(self,arg2:FBVertex):...
    @overload
    def __init__(self,arg2:float,arg3:float,arg4:float,arg5:float):...
    @overload
    def __init__(self,arg2):...
    @overload
    def __init__(self,arg2:list):...
    @overload
    def __isub__(self,arg2:FBVertex)->object:...
    @overload
    def __isub__(self,arg2)->object:...
    def __len__(self)->int:...
    @overload
    def __mul__(self,arg2:FBVertex)->object:...
    @overload
    def __mul__(self,arg2)->object:...
    def __neg__(self)->object:...
    def __setitem__(self,arg2,arg3:float):...
    @overload
    def __sub__(self,arg2:FBVertex)->object:...
    @overload
    def __sub__(self,arg2)->object:...
    @overload
    def __truediv__(self,arg2:FBVertex)->object:...
    @overload
    def __truediv__(self,arg2)->object:...
class FBVideo(FBBox):
    KeepOnGPU:bool
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of video media.
        ### Warning:
        The Name parameter must point to a valid media file, otherwise the object will not be valid. Use the method 'IsValid()' to confirm the object status."""
        ...
class FBVideoClip(FBVideo):
    CurrentFrame:property
    CurrentFrameTime:property
    CurrentFrameTimeCode:property
    Filename:property
    Format:property
    FrameRate:property
    FrameTime:property
    FreeRunning:property
    Height:property
    InterlaceMode:property
    LastFrame:property
    LastFrameTime:property
    Loop:property
    PlaySpeed:property
    PowerOfTwoHeight:property
    PowerOfTwoWidth:property
    ProxyMode:property
    RelativePath:property
    StartFrame:property
    StopFrame:property
    StorageMode:property
    TimeOffset:property
    Width:property
    def DrawImage(self,arg2=None,arg3=None,arg4=None,arg5=None,arg6=None):...
    def GetEmbeddedTimecode(self,arg2)->FBTimeCode:...
    def GetTextureID(self)->int:...
    def IsValid(self)->bool:...
    def __init__(self,arg2:str):...
class FBVideoClipImage(FBVideoClip):
    ImageSequence:property
    MaxMipMapResolution:property
    UseSystemFrameRate:property
    def __init__(self,arg2:str):...
class FBVideoCodecManager():
    VideoCodecMode:property
    def GetCodecIdList(self,FileFormatInfo:str)->list:
        """Get all codec id available for a given file format.
        ### Parameters:
        - FileFormatInfo: file format description string (AVI, MOV...)"""
        ...
    def GetDefaultCodec(self,FileFormatInfo:str)->str:
        """Get the default codec id for a given file format. This is the codec that will be used if codec mode is FBVideoCodecUseDefault
        ### Parameters:
        - FileFormatInfo: file format description string (AVI, MOV...)"""
        ...
    def RegisterExternalVideoFormat(self,FormatSuffix:str)->bool:
        """Register external video format suffix.
        Only alphabetic and number is allowed in provided suffix, and can not be empty suffix or the system exist suffixes. This will allow this suffix to be appeared in the filters of file dialog when importing video, also allow to create a texture/video object with a path containing this suffix via SDK. However it will the custom SDK plug-in developer's responsibility to load the file into memory.
        ### Remarks:
        After register an external video format, and save a scene with this kind of video. when start MotionBuilder next time and before load the scene back,
        It is necessary to call RegisterExternalVideoFormat to register this kind of video format again, otherwise this kind of video will not be loaded.
        
        ### Parameters:
        - FormatSuffix: Suffix/File extension of external video file format
        
        ### Returns:
        true if register successful"""
        ...
    def SetDefaultCodec(self,FileFormatInfo:str,CodecId:str):
        """Set the default codec id for a given file format. This is the codec that will be used if codec mode is FBVideoCodecUseDefault
        ### Parameters:
        - FileFormatInfo: file format description string (AVI, MOV...)
        - CodecId: the codec id to set as default"""
        ...
    def __init__(self):...
class FBVideoGrabOptions():
    AntiAliasing:property
    AudioCustomStandaloneFileName:property
    AudioOutputLocation:property
    AudioRenderFormat:property
    AudioUseCustomStandaloneFileName:property
    BitsPerPixel:property
    CameraResolution:property
    FieldMode:property
    OutputFileName:property
    RenderAudio:property
    RendererCallbackIndex:property
    RendererCallbackPrefIndex:property
    ShowCameraLabel:property
    ShowSafeArea:property
    ShowTimeCode:property
    StereoDisplayMode:property
    StillImageCompression:property
    TimeSpan:property
    TimeSteps:property
    ViewingMode:property
    def __init__(self):...
class FBVideoGrabber(FBComponent):
    def BeginGrab(self)->bool:
        """Begin video grabbing session.
        ### Returns:
        True if we can begin the grab session."""
        ...
    def EndGrab(self):
        """Close video grabbing session."""
        ...
    def GetLastErrorMsg(self)->str:
        """### Returns:
        If an error occured, this function returns the last error message, otherwise an empty string."""
        ...
    def GetOptions(self)->FBVideoGrabOptions:
        """GetOptions give you a copy of current grabbing options.
        ### Returns:
        Struct that contain all grabbing options."""
        ...
    def GetStatistics(self)->object:
        """### Returns:
        Struct that contain all grabbing statistics."""
        ...
    def Grab(self):
        """Grab all specified video frames."""
        ...
    def RenderSnapshot(self,Width:int=-1,Height:int=-1,bCameraLabel:bool=False,bTimeCode:bool=False,bSafeArea:bool=False,bAxis:bool=False,bGrid:bool=False,bFrontPlate:bool=False,bBackPlate:bool=False)->FBImage:
        """Render a snapshot of the actual display.
        ### Parameters:
        - Width: 
        - Height: 
        - bCameraLabel: 
        - bTimeCode: 
        - bSafeArea: 
        - bAxis: 
        - bGrid: 
        - bFrontPlate: 
        - bBackPlate: 
        
        ### Returns:
        An FBimage containing data of the rendered snapshot."""
        ...
    def ResetOptions(self):
        """SetDefaultOptions.
        This function reset all grabbing options to the default value."""
        ...
    def SetOptions(self,Options:FBVideoGrabOptions):
        """### Parameters:
        - Options: Struct that contain all grabbing options."""
        ...
    def __init__(self):...
class FBVideoIn(FBVideo):
    FilePath:str
    Online:bool
    RecordAudio:bool
    Recording:bool
    def LiveGetCompressor(self)->int:
        """Get the current compressor index.
        ### Returns:
        Index of the current compressor."""
        ...
    def LiveGetCompressorCount(self)->int:
        """Get the compressor count.
        ### Returns:
        Number of available compressor."""
        ...
    def LiveGetCompressorName(self,CompressorIndex:int)->str:
        """Get the compressor name at a particular index.
        ### Returns:
        Name of the compressor. If the CompressorIndex is higher than the number of compressor, the function will return NULL."""
        ...
    def LiveGetResolutionFR(self)->int:
        """Get the current resolution and frame rate index.
        ### Returns:
        Index of the current resolution and frame rate."""
        ...
    def LiveGetResolutionFRCount(self)->int:
        """Get the number of resolution and frame rate available for the device.
        ### Returns:
        Number of available resolution and frame rate."""
        ...
    def LiveGetResolutionFRName(self,Index:int)->str:
        """Get the resolution and frame rate string description at the specified index.
        ### Parameters:
        - Index: Index of the resolution and frame rate.
        
        ### Returns:
        Name of the resolution and frame rate."""
        ...
    def LiveGetType(self)->FBVideoLiveType:
        """Get the type of the video input device.
        ### Returns:
        Type of the video input device."""
        ...
    def LiveSetCompressor(self,CompressorIndex:int):
        """Set the current compressor to be used when recording.
        ### Parameters:
        - CompressorIndex: Index of the compressor.
        
        ### Returns:
        True if successful."""
        ...
    def LiveSetResolutionFR(self,Index:int):
        """Set the current resolution and frame rate for the device.
        ### Parameters:
        - Index: Index of the resolution and frame rate."""
        ...
    def __init__(self):...
class FBVideoMemory(FBVideo):
    TextureOGLId:int
    def SetObjectImageSize(self,W:int,H:int):
        """Set image size to allow MoBu preview texture with proper dimension / aspect.
        ### Parameters:
        - W: Width of image.
        - H: Height of image."""
        ...
    def __init__(self,Name:str):
        """### Parameters:
        - Name: Name of video media."""
        ...
class FBVideoOut(FBVideo):
    Online:bool
    def __init__(self):...
class FBViewingOptions():
    DisplayMode:property
    DisplayWhat:int
    PaneIndex:int
    PickingMode:FBPickingMode
    ShowCameraLabel:bool
    ShowSafeArea:bool
    ShowTimeCode:bool
    StereoDisplayMode:FBStereoDisplayMode
    def InPicking(self)->bool:...
    def IsInColorBufferPicking(self)->bool:
        """Is the rendering routine during picking status with GL color buffer method."""
        ...
    def IsInSelectionBufferPicking(self)->bool:
        """Is the rendering routine during picking status with GL selection buffer method."""
        ...
    def RenderCallbackPrefIndex(self)->int:
        """Current Render callback Settings Index."""
        ...
class FBVisualComponent(FBComponent):
    BorderCaption:property
    BorderCornerRadius:property
    BorderInSet:property
    BorderMaxAngle:property
    BorderShowCaption:property
    BorderSpacing:property
    BorderStyle:property
    BorderWidth:property
    Caption:str
    Enabled:bool
    Height:int
    Hint:str
    Left:int
    ReadOnly:bool
    RegionAttachToHeight:property
    RegionAttachToWidth:property
    RegionAttachToX:property
    RegionAttachToY:property
    RegionAttachTypeHeight:property
    RegionAttachTypeWidth:property
    RegionAttachTypeX:property
    RegionAttachTypeY:property
    RegionName:property
    RegionOffsetHeight:property
    RegionOffsetWidth:property
    RegionOffsetX:property
    RegionOffsetY:property
    RegionPosMaxX:property
    RegionPosMaxY:property
    RegionPosMinX:property
    RegionPosMinY:property
    RegionRatioHeight:property
    RegionRatioWidth:property
    RegionRatioX:property
    RegionRatioY:property
    Top:int
    Visible:bool
    Width:int
    def AddChild(self,Child:FBVisualComponent,Id:int=0)->bool:
        """Add a child component.
        ### Parameters:
        - Child: Visual component to add as a child.
        - Id: User reference number to associate with Child (default=0).
        
        ### Returns:
        Operation was successful ( true or false )."""
        ...
    def GetChild(self,Id:int)->FBVisualComponent:
        """Get a child component.
        ### Parameters:
        - Id: User reference number to look for child with(default=0).
        
        ### Returns:
        Handle to child (NULL if not found)."""
        ...
    def GetQWidgetAddress(self)->int:
        """Get internal QWidget.
        ### Returns:
        Handle to internal QWidget object."""
        ...
    def IsView(self)->bool:
        """Is component a view?
        ### Returns:
        true if component is a view.
        Reimplemented in FBView ."""
        ...
    def Refresh(self,bNow:bool=False):
        """Refresh component.
        ### Parameters:
        - bNow: Refresh immediately if true (default = false )."""
        ...
    def ViewExpose(self):
        """Exposed view callback function."""
        ...
    def ViewInput(self,MouseX:int,MouseY:int,Action:FBInputType,ButtonKey:int,Modifier:int):
        """Input callback function.
        ### Parameters:
        - MouseX: Mouse X position.
        - MouseY: Mouse Y position.
        - Action: Mouse action.
        - ButtonKey: Keyboard input.
        - Modifier: Keyboard input modifier."""
        ...
class FBVisualContainer(FBVisualComponent):
    IconPosition:FBIconPosition
    ItemHeight:int
    ItemIndex:int
    ItemWidth:int
    ItemWrap:bool
    Items:FBStringList
    OnChange:FBEvent
    OnDblClick:FBEvent
    OnDragAndDrop:FBEvent
    Orientation:FBOrientation
    def GetSelection(self)->int:
        """Get the selected item.
        ### Returns:
        Index of current selection."""
        ...
    @overload
    def ItemIconSet(self,Ref,Image:FBImage,bUseACopyOfTheImage:bool=True)->bool:
        """Set an item's icon.
        ### Parameters:
        - Ref: Reference to item in container.
        - Image: Handle to image to use.
        - bUseACopyOfTheImage: Create a copy of the image?(default=true)
        
        ### Returns:
        Operation was successful ( true or false )."""
        ...
    @overload
    def ItemIconSet(self,Ref,Filename:str)->bool:
        """Set an item's icon.
        ### Parameters:
        - Ref: Reference to item in container.
        - Filename: Name of file where image is located.
        
        ### Returns:
        Operation was successful ( true or false )."""
        ...
    def ItemNameEdit(self,Ref)->bool:
        """Edit a container item.
        ### Parameters:
        - Ref: Reference of container to edit.
        
        ### Returns:
        Operation was successful ( true or false )."""
        ...
    def __init__(self):...
class FBView(FBVisualComponent):
    DoubleBuffer:bool
    GraphicOGL:bool
    def DrawString(self,Text:str,X:float,Y:float,Enable:int=-1):
        """Draw a string in the view.
        ### Parameters:
        - Text: Text to draw.
        - X: X position of string.
        - Y: Y position of string.
        - Enable: Is string enabled? (default =-1)"""
        ...
    def SetViewport(self,X:int,Y:int,W:int,H:int)->bool:
        """Set view's viewport.
        ### Parameters:
        - X: Viewport X value.
        - Y: Viewport Y value.
        - W: Viewport W (width) value.
        - H: Viewport H (height) value.
        
        ### Returns:
        Operation was successful ( true or false )."""
        ...
    def __init__(self):...
class FBTree(FBVisualComponent):
    AllowCollapse:bool
    AllowExpansion:bool
    AutoExpandOnDblClick:bool
    AutoExpandOnDragOver:bool
    AutoScroll:bool
    AutoScrollOnExpand:bool
    CheckBoxes:bool
    DeselectOnCollapse:bool
    EditNodeOn2Select:bool
    HighlightOnRightClick:bool
    Indent:int
    ItemHeight:int
    MultiDrag:bool
    MultiSelect:bool
    NoSelectOnDrag:bool
    NoSelectOnRightClick:bool
    OnChange:FBEvent
    OnClick:FBEvent
    OnClickCheck:FBEvent
    OnCollapsed:FBEvent
    OnCollapsing:FBEvent
    OnDblClick:FBEvent
    OnDragAndDrop:FBEvent
    OnExpanded:FBEvent
    OnExpanding:FBEvent
    OnSelect:FBEvent
    SelectedCount:int
    SelectedNodes:FBPropertyListTreeNode
    SelectionActive:bool
    ShowLines:bool
    TreeHeight:int
    TreeWidth:int
    VisibleItemCount:int
    def Clear(self):
        """Clear the tree (remove all nodes)."""
        ...
    def GetRoot(self)->FBTreeNode:
        """Get the root node.
        ### Returns:
        the root node of the tree."""
        ...
    def InsertLast(self,Node:FBTreeNode,Name:str)->FBTreeNode:
        """Insert node at the end.
        ### Parameters:
        - Node: Node under which the new node will appear.
        - Name: Text to display for this node.
        
        ### Returns:
        the newly created node."""
        ...
    def __init__(self):...
class FBThermometer(FBVisualComponent):
    Max:float
    Min:float
    Value:float
    def Clear(self):
        """Reset bounds and value."""
        ...
    def __init__(self):...
class FBTabPanel(FBVisualComponent):
    ItemIndex:int
    Items:FBStringList
    Layout:FBLayout
    OnChange:FBEvent
    TabStyle:int
    def __init__(self):...
class FBSpread(FBVisualComponent):
    Column:int
    MultiSelect:bool
    OnCellChange:FBEvent
    OnColumnClick:FBEvent
    OnDragAndDrop:FBEvent
    OnRowClick:FBEvent
    Row:property
    def Clear(self):
        """Clear spreadsheet This function will empty spreadsheet of all its rows, columns and cells."""
        ...
    def ColumnAdd(self,String:str,Ref=0):
        """Add a column.
        ### Parameters:
        - String: Text to display with column.
        - Ref: User-define column reference number(default=0)."""
        ...
    def GetCellValue(self,arg2,arg3)->object:...
    def GetCellView(self,Ref,Column:int)->object:
        """Get a cell's internal toolkit view.
        ### Parameters:
        - Ref: Row of cell.
        - Column: Column of cell.
        ### Return values:
        - pView: Handle of view."""
        ...
    def GetColumn(self,Column:int)->FBSpreadColumn:
        """Get a column from a column number.
        ### Parameters:
        - Column: Column number.
        
        ### Returns:
        A copy of column."""
        ...
    def GetCurrentCell(self)->FBSpreadCell:
        """Get the current cell.
        ### Returns:
        A copy of the the current cell."""
        ...
    def GetRow(self,Ref)->FBSpreadRow:
        """Get a row from a row reference.
        ### Parameters:
        - Ref: Reference to a row.
        
        ### Returns:
        A copy of the row."""
        ...
    def GetSpreadCell(self,arg2,arg3)->object:...
    def RowAdd(self,String:str,Ref=0):
        """Add a row.
        ### Parameters:
        - String: Text to display with row.
        - Ref: User-defined reference for row(default=0)."""
        ...
    def RowSort(self,bAscending:bool=True):
        """Sort rows.
        ### Parameters:
        - bAscending: If true , sort ascending."""
        ...
    def SetCellValue(self,arg2,arg3,arg4):...
    def SetCellView(self,Ref,Column:int,View:FBVisualComponent):
        """Set a cell's internal toolkit view.
        ### Parameters:
        - Ref: Row of cell.
        - Column: Column of cell.
        - View: View to use to set cell's view."""
        ...
    def __init__(self):...
class FBSlider(FBVisualComponent):
    Max:float
    Min:float
    OnChange:FBEvent
    OnTransaction:FBEvent
    Orientation:FBOrientation
    Value:float
    def __init__(self):...
class FBScrollBox(FBVisualComponent):
    Content:property
    def SetContentSize(self,arg2,arg3):...
    def __init__(self):...
class FBPropertyConnectionEditor(FBVisualComponent):
    Property:property
    def PopupList(self):
        """Launch a list of connected objects."""
        ...
    def PopupTree(self):
        """Launch a tree of object connections."""
        ...
    def __init__(self):...
class FBPlotPopup(FBVisualComponent):
    EnableEvaluateDeformation:bool
    EnablePlotAuxEffectors:bool
    EnablePlotCharacterExtension:bool
    EnablePlotLockedProperties:bool
    EnablePlotTranslationOnRootOnly:bool
    EnableSmartPlotControls:bool
    def GetPlotOptions(self)->FBPlotOptions:
        """Get plot options.
        ### Returns:
        plot options."""
        ...
    def Popup(self,WindowName:str)->bool:
        """Execute plot popup.
        ### Returns:
        true if OK is clicked by user."""
        ...
    def SetPlotOptions(self,PlotOptions:FBPlotOptions):
        """Set plot options.
        ### Parameters:
        - PlotOptions: Set the plot options that will be used when displaying the plot popup. First use the GetPlotOptions() , change the options and use the SetPlotOptions() to set them before calling the Popup() function."""
        ...
    def __init__(self):...
class FBList(FBVisualComponent):
    ExtendedSelect:bool
    ItemIndex:int
    Items:FBStringList
    MultiSelect:bool
    OnChange:FBEvent
    OnDragAndDrop:FBEvent
    Style:property
    def IsSelected(self,Index:int)->bool:
        """Returns whether or not the item Index is currently selected.
        ### Parameters:
        - Index: Index to see if select or not.
        
        ### Returns:
        true if item at Index is selected."""
        ...
    def __init__(self):...
class FBLayoutRegion(FBVisualComponent):
    def __init__(self):...
class FBLayout(FBVisualComponent):
    OnIdle:FBEvent
    OnInput:FBEvent
    OnPaint:FBEvent
    OnResize:FBEvent
    OnShow:FBEvent
    def AddRegion(self,Name:str,Title:str,X:FBAddRegionParam,XType:FBAddRegionParam,XRelative:FBAddRegionParam,MultX:FBAddRegionParam)->bool:
        """Add a region to the layout.
        ### Parameters:
        - Name: Name of region.
        - Title: Title to display.
        - X: X: Position.
        - XType: X: Type of attachment.
        - XRelative: X: Item to attach to.
        - MultX: X: Multiplier of relative value.
        ### Returns:
        Operation was successful ( true or false )."""
        ...
    def ClearControl(self,Name:str):
        """Remove a control from a region in a visual component.
        ### Parameters:
        - Name: Name of region to remove control."""
        ...
    def GetControl(self,Name:str)->FBVisualComponent:
        """Get control of a region in a visual component.
        ### Parameters:
        - Name: Name of region to find.
        
        ### Returns:
        The component if it is found."""
        ...
    def GetRegion(self,Name:str)->bool:
        """Verify if a region with Name exists.
        ### Parameters:
        - Name: Name of region to check.
        
        ### Returns:
        Operation was successful (true or false)."""
        ...
    def GetRegionPositions(self,Name:str,bComputed:bool,X:int,Y:int,W:int=None,H:int=None)->bool:
        """Get region Name information (position and size)
        ### Parameters:
        - Name: Name of region.
        - bComputed: Is the information retrieved relative or absolute?
        
        ### Return values:
        - X: Position in X of the region.
        - Y: Position in Y of the region.
        - W: Width of the region.
        - H: Height of the region.
        
        ### Returns:
        Operation was successful (true or false)."""
        ...
    def GetSplitStyle(self,Name:str)->FBSplitStyle:
        """Get a region's splitstyle.
        ### Parameters:
        - Name: Name of Region to get splitstyle from.
        
        ### Returns:
        Split style of specified region."""
        ...
    def MoveRegion(self,Name:str,X:int,Y:int)->bool:
        """Move a region.
        ### Parameters:
        - Name: Name of region to move.
        - X: New X position.
        - Y: New Y position.
        
        ### Returns:
        Operation was successful (true or false)."""
        ...
    def RemoveRegion(self,Name:str)->bool:
        """Remove a region.
        ### Parameters:
        - Name: Name of region to remove.
        
        ### Returns:
        Operation was successful (true or false)."""
        ...
    def RenameRegion(self,OldName:str,NewName:str)->bool:
        """Rename a region.
        ### Parameters:
        - OldName: Region's old name.
        - NewName: Region's new name.
        
        ### Returns:
        Operation was successful (true or false)."""
        ...
    def Restructure(self,bNoMove:bool):
        """Force a recomputation of all region placements in the layout."""
        ...
    def SetAutoRestructure(self,bAutoRestructure:bool):
        """Suspend all automatic layout recomputation.
        ### Parameters:
        - bAutoRestructure: If true, Suspend all automatic layout recomputation, else restore it."""
        ...
    def SetBorder(self,Name:str,Type:FBBorderStyle,bShowTitle:bool,bInSet:bool,Width:int,Spacing:int,MaxAngle:float,CornerRadius:int)->bool:
        """Set border properties for a region.
        ### Parameters:
        - Name: Name of Region to change border properties.
        - Type: Border style to use.
        - bShowTitle: Show region title?
        - bInSet: Is region inset?
        - Width: Border width.
        - Spacing: Border spacing.
        - MaxAngle: Max angle for rounding.
        - CornerRadius: Corner radius for rounding.
        
        ### Returns:
        Operation was successful (true or false)."""
        ...
    def SetControl(self,Name:str,Component:FBVisualComponent)->bool:
        """Set control of a region to a visual component.
        ### Parameters:
        - Name: Name of region to affect.
        - Component: Component to control region.
        
        ### Returns:
        Operation was successful (true or false)."""
        ...
    def SetRegionTitle(self,Name:str,Title:str)->bool:
        """Set a region's title.
        ### Parameters:
        - Name: Name of region to change title.
        - Title: New title for region.
        
        ### Returns:
        Operation was successful (true or false)."""
        ...
    def SetSplitStyle(self,Name:str,RegionType:FBSplitStyle)->bool:
        """Set a region's splitstyle.
        ### Parameters:
        - Name: Name of Region to set splitstyle.
        - RegionType: Split style give to region.
        
        ### Returns:
        Operation was successful (true or false)."""
        ...
    def SetView(self,Name:str,Component:FBVisualComponent)->bool:
        """Set view.
        ### Parameters:
        - Name: Name of Region.
        - Component: Component to set as view.
        
        ### Returns:
        Operation was successful (true or false)."""
        ...
    def SizeRegion(self,Name:str,W:int,H:int)->bool:
        """Change a region's size.
        ### Parameters:
        - Name: Name of region to resize.
        - W: New region width.
        - H: New region height.
        
        ### Returns:
        Operation was successful (true or false)."""
        ...
    def __init__(self):...
class FBLabel(FBVisualComponent):
    Justify:FBTextJustify
    Style:FBTextStyle
    WordWrap:bool
    def __init__(self):...
class FBTool(FBLayout):
    DisplayName:str
    MaxSizeX:property
    MaxSizeY:property
    MinSizeX:property
    MinSizeY:property
    StartPosX:property
    StartPosY:property
    StartSizeX:property
    StartSizeY:property
    ToolName:property
    def GetPossibleDockPosition(self)->FBToolPossibleDockPosition:
        """Get the possible docking position for the tool (concatenated).
        ### Returns:
        Get all the docking flags in one call. Flags can be concatenated."""
        ...
    def SetPossibleDockPosition(self,Flags:FBToolPossibleDockPosition):
        """Set the possible docking position for the tool.
        Be sure to call this function once the tool is visible, a good place to call it is when the OnShow event of the layout is called.
        ### Parameters:
        - Flags: Set the docking position flag values. Note: this function overwrites all flags with those passed in parameter."""
        ...
    def __init__(self,Name:str,arg3=None):
        """### Parameters:
        - Name: Name of tool."""
        ...
class FBPopup(FBLayout):
    Modal:bool
    def Close(self,bOk:bool):
        """Close popup.
        ### Parameters:
        - bOk: Equivalent of OK button clicked if true (default = false )."""
        ...
    def Show(self,Parent:FBVisualComponent=None):
        """Show popup.
        ### Parameters:
        - Parent: Parent object for popup
        
        ### Returns:
        Operation was successful ( true or false )."""
        ...
    def __init__(self):...
class FBImageContainer(FBVisualComponent):
    Filename:str
    OnDragAndDrop:FBEvent
    def __init__(self):...
class FBFCurveEditor(FBVisualComponent):
    def AddAnimationNode(self,Node:FBAnimationNode):
        """Add an animation node to the editor.
        ### Parameters:
        - Node: Animation node to show in the editor."""
        ...
    def AddProperty(self,Property:FBPropertyAnimatable):
        """Add an animatable property to the editor.
        ### Parameters:
        - Property: Property to show in the editor."""
        ...
    def Clear(self):
        """Clear the editor."""
        ...
    def RemoveAnimationNode(self,Node:FBAnimationNode):
        """Remove an animation node from the editor.
        ### Parameters:
        - Node: Animation node to hide from editor."""
        ...
    def __init__(self):...
class FBEditVector(FBVisualComponent):
    OnChange:FBEvent
    Value:FBVector3d
    def __init__(self):...
class FBEditTimeCode(FBVisualComponent):
    OnChange:property
    Value:property
    def __init__(self):...
class FBEditPropertyModern(FBVisualComponent):
    LargeInc:float
    Precision:float
    Property:property
    SliderMax:float
    SliderMin:float
    SmallInc:float
    def SetBackgroundColorIndex(self,Index):
        """Set the background color index.
        Use the system-defined color palette to set the backgound color. By default the color used is kFBColorIndexStdListBg1"""
        ...
    def __init__(self):...
class FBEditProperty(FBVisualComponent):
    LargeInc:float
    Precision:float
    Property:property
    SliderMax:float
    SliderMin:float
    SmallInc:float
    def __init__(self):...
class FBEditNumber(FBVisualComponent):
    LargeStep:float
    Max:float
    Min:float
    OnChange:FBEvent
    Precision:float
    SmallStep:float
    Value:float
    def __init__(self):...
class FBEditColor(FBVisualComponent):
    ColorMode:int
    OnChange:FBEvent
    Value:FBColor
    def __init__(self):...
class FBEdit(FBVisualComponent):
    OnChange:FBEvent
    PasswordMode:bool
    Text:str
    def __init__(self):...
class FBButton(FBVisualComponent):
    Justify:FBTextJustify
    Look:FBButtonLook
    OnClick:FBEvent
    State:int
    Style:FBButtonStyle
    def GetStateColor(self,State:FBButtonState)->FBColor:
        """Queries the color associated with a button state.
        This method is only useful for buttons of style kFB2States.
        ### Parameters:
        - State: The state to be queried.
        
        ### Returns:
        The color vector."""
        ...
    def SetImageFileNames(self,UpImage:str,DownImage:str=0,ThirdImage:str=0,bFromResources:bool=False):
        """Sets the image used to generate a kFBBitmap2States.
        ### Parameters:
        - UpImage: The image used when button is unpushed
        - DownImage: The image used when button is pushed
        - ThirdImage: 
        - bFromResources: Add resource path to image path."""
        ...
    def SetStateColor(self,State:FBButtonState,Color:FBColor):
        """Returns whether or not the item pIndex is currently selected.
        ### Parameters:
        - State: The state to be set.
        - Color: The desired color vector."""
        ...
    def __init__(self):...
class FBMemo(FBEdit):
    def GetStrings(self,Lines:FBStringList):
        """Get the content of the memo.
        ### Parameters:
        - Lines: Content of the memo will be copied to it."""
        ...
    def SetStrings(self,Lines:FBStringList):
        """Set the content of the memo.
        ### Parameters:
        - Lines: Content of the memo from will be set to it."""
        ...
    def __init__(self):...
class FBBrowsingProperty(FBVisualComponent):
    def AddObject(self,Object:FBPlug):
        """Add an object whose properties will be displayed.
        ### Parameters:
        - Object: Object whose properties will be displayed in the property brwoser."""
        ...
    def ObjectGet(self,Index:int)->FBPlug:
        """Return the object at the specified index.
        ### Parameters:
        - Index: Index of the object to get.
        
        ### Returns:
        Object at the index specified currently displayed in the property browser."""
        ...
    def ObjectGetCount(self)->int:
        """Get the number of object displayed in the property browser.
        ### Returns:
        Object currently displayed in the property browser."""
        ...
    def RemoveObject(self,Object:FBPlug):
        """Remove an object from the property browser.
        ### Parameters:
        - Object: Object to remove."""
        ...
    def __init__(self):...
class FBArrowButton(FBVisualComponent):
    def SetContent(self,Title:str,Content:FBVisualComponent,ContentWidth:int,ContentHeight:int):
        """Sets the content to be hidden/shown by button.
        The FBArrowButton must already have been added to a layout before calling this method.
        ### Parameters:
        - Title: Title of the content managed by the FBArrowButton
        - Content: Content that the FBArrowButton displays or hides
        - ContentWidth: Width of the content
        - ContentHeight: Height of the content"""
        ...
    def __init__(self):...
class FBWebView(FBVisualComponent):
    def Load(self,URL:str):
        """Load the specified Url.
        ### Parameters:
        - URL: url to load in the WebView."""
        ...
    def __init__(self):...
class FBWidgetHolder(FBVisualComponent):
    def __init__(self):...
def CloseTool(Tool:FBTool)->bool:
    """This function will close a specific tool in the GUI.
    ### Parameters:
    - Tool: A pointer to the tool to close.
    
    ### Returns:
    True if the tool was closed successfully, false otherwise."""
    ...
def CloseToolByName(ToolName:str)->bool:
    """This function will close a specific tool in the GUI.
    ### Parameters:
    - ToolName: The name of the tool as shown in the Open Reality menu.
    
    ### Returns:
    True if the tool was closed successfully, false otherwise."""
    ...
def FBActionManager_TypeInfo()->int:...
def FBActorFace_TypeInfo()->int:...
def FBActor_TypeInfo()->int:...
def FBAdd(Result:FBVector4d,V1:FBVector4d,V2:FBVector4d):
    """Add two vectors together ( Result = V1 + V2 )
    ### Return values:
    - Result: Resulting vector.
    
    ### Parameters:
    - V1: 1st vector.
    - V2: 2nd vector."""
    ...
def FBAnimationLayer_TypeInfo()->int:...
def FBAnimationNode_TypeInfo()->int:...
def FBApplication_TypeInfo()->int:...
def FBArrowButton_TypeInfo()->int:...
def FBAssetFile_TypeInfo()->int:...
def FBAssetFolder_TypeInfo()->int:...
def FBAssetItem_TypeInfo()->int:...
def FBAssetMng_TypeInfo()->int:...
def FBAudioClip_TypeInfo()->int:...
@overload
def FBAudioFmt_AppendFormat(Format,Channels:int,Bits:int,Rate:int)->int:
    """Append the rendering audio format using the specified settings.
    For example, to set audio format to 2 channels, 16 bit, 44100 rate, use the following function: AudioFormat = FBAudioFmt_AppendFormat(0, 2, 16, 44100)
    ### Parameters:
    - Format: Audio format to use. Set this to 0 if there is no audio format to be appended.
    - Channels: Number of channels. Valid values are 0, 1, 2, 4, 8.
    - Bits: Bit depth. Valid values are 0, 8, 16, 24, 32.
    - Rate: Audio rate. Valid values are 0, 8000, 11025, 12000, 12500, 16000, 22050, 24000, 25000, 32000, 44100, 48000, 50000, 64000, 88200, 96000, 100000.
    
    ### Returns:
    An audio format object with the specified format.
    Python sample code: from pyfbsdk import *"""
    ...
@overload
def FBAudioFmt_AppendFormat(Format,SrcFormat)->int:
    """Append the rendering audio format with another audio format.
    ### Parameters:
    - Format: Audio format to use.
    - SrcFormat: Audio format to be appended.
    
    ### Returns:
    An audio format object with the specified format."""
    ...
def FBAudioFmt_ConvertBitDepthMode(BitDepthMode:FBAudioBitDepthMode)->int:
    """Converts an FBAudioBitDepthMode enum value to its FBAudioFmt object equivalent.
    ### Parameters:
    - BitDepthMode: The bit depth mode enum value.
    
    ### Returns:
    The FBAudioFmt object equivalent to the input bit depth mode enum value."""
    ...
def FBAudioFmt_ConvertChannelMode(ChannelMode:FBAudioChannelMode)->int:
    """Converts an FBAudioChannelMode enum value to its FBAudioFmt object equivalent.
    ### Parameters:
    - ChannelMode: The channel mode enum value.
    
    ### Returns:
    The FBAudioFmt object equivalent to the input channel mode enum value."""
    ...
def FBAudioFmt_ConvertRateMode(RateMode:FBAudioRateMode)->int:
    """Converts an FBAudioRateMode enum value to its FBAudioFmt object equivalent.
    ### Parameters:
    - RateMode: The rate mode enum value.
    
    ### Returns:
    The FBAudioFmt object equivalent to the input rate mode enum value."""
    ...
def FBAudioFmt_GetBitsValue(Format)->int:
    """Get the bit depth value of the Audio format object.
    ### Parameters:
    - Format: Audio format to use.
    
    ### Returns:
    Bit depth value as an integer value."""
    ...
def FBAudioFmt_GetBytesValue(Format)->int:
    """Get the bytes value of the Audio format object.
    ### Parameters:
    - Format: Audio format to use.
    
    ### Returns:
    Bytes value as an integer value."""
    ...
def FBAudioFmt_GetChannelValue(Format)->int:
    """Get the channel value of the Audio format object.
    ### Parameters:
    - Format: Audio format to use.
    
    ### Returns:
    Channel value as an integer value."""
    ...
def FBAudioFmt_GetDefaultFormat()->int:
    """Get default audio format.
    ### Returns:
    An audio format object."""
    ...
def FBAudioFmt_GetRateValue(Format)->int:
    """Get the rate value of the Audio format object.
    ### Parameters:
    - Format: Audio format to use.
    
    ### Returns:
    Audio rate value as an integer value."""
    ...
@overload
def FBAudioFmt_RemoveFormat(Format,Channels:int,Bits:int,Rate:int)->int:
    """Remove channels, bit depth, or rate from the specified audio format object.
    Please refer to python example in FBAudioFmt_AppendFormat.
    ### Parameters:
    - Format: Audio format to use.
    - Channels: Number of channels to remove. Set this to 0 if you don't want to remove the channel.
    - Bits: Bit depth to remove. Set this to 0 if you don't want to remove bit depth.
    - Rate: Audio rate to remove. Set this to 0 if you don't want to remove audio rate.
    
    ### Returns:
    An audio format object without the specified format settings passed in parameter."""
    ...
@overload
def FBAudioFmt_RemoveFormat(Format,SrcFormat)->int:
    """Remove audio format from another audio format object.
    ### Parameters:
    - Format: Audio format to use.
    - SrcFormat: Audio format to remove.
    
    ### Returns:
    An audio format object without the specified format settings passed in parameter."""
    ...
def FBAudioFmt_TestFormat(SrcFormat,Channels:int,Bits:int,Rate:int)->bool:
    """Test if the given audio format object contains the channel, bit depth, and rate.
    ### Parameters:
    - pFormat: Audio format to test.
    - Channels: Number of channels to test.
    - Bits: Bit depth to test.
    - Rate: Audio rate to test.
    
    ### Returns:
    True if the given audio format object contains the channel, bit depth, and rate."""
    ...
def FBAudioIn_TypeInfo()->int:...
def FBAudioOut_TypeInfo()->int:...
def FBBeginChangeAllModels():
    """Call begin change to all models (need to be closed).
    Useful for selection of many models that can trigger many related callbacks)"""
    ...
def FBBoxPlaceHolder_TypeInfo()->int:...
def FBBox_TypeInfo()->int:...
def FBBrowsingProperty_TypeInfo()->int:...
def FBButton_TypeInfo()->int:...
def FBCameraStereo_TypeInfo()->int:...
def FBCameraSwitcherAudioManager_TypeInfo()->int:...
def FBCameraSwitcher_TypeInfo()->int:...
def FBCamera_TypeInfo()->int:...
def FBCharacterExtension_TypeInfo()->int:...
def FBCharacterFace_TypeInfo()->int:...
def FBCharacterMarkerSet_TypeInfo()->int:...
def FBCharacterPose_TypeInfo()->int:...
def FBCharacterSolver_TypeInfo()->int:...
def FBCharacter_TypeInfo()->int:...
def FBClamp(V:float,L:float,H:float)->float:
    """Clamp value.
    ### Parameters:
    - V: Value to clamp.
    - L: Low limit.
    - H: High limit.
    
    ### Returns:
    Clamped value."""
    ...
def FBCluster_TypeInfo()->int:...
def FBComponent_TypeInfo()->int:...
def FBConnect(Src:FBPlug,Dst:FBPlug,ConnectionType:FBConnectionType=FBConnectionType.kFBConnectionTypeNone)->bool:
    """Request the connection two FBPlug objects.
    ### Parameters:
    - Src: Source plug.
    - Dst: Destination plug.
    - ConnectionType: Type of connection, taken from FBConnectionType.
    
    ### Returns:
    A boolean indicating success (True) or failure (False).
    
    ### Remarks:
    This global function is used primarily to connect connectors in a FBConstraintRelation ."""
    ...
def FBConstraintManager_TypeInfo()->int:...
def FBConstraintRelation_TypeInfo()->int:...
def FBConstraintSolver_TypeInfo()->int:...
def FBConstraint_TypeInfo()->int:...
def FBConstructionHistory_TypeInfo()->int:...
def FBControlSet_TypeInfo()->int:...
def FBCreateObject(GroupName:str,EntryName:str,Name:str,Data:None=None)->FBComponent:
    """### Parameters:
    - EntryName: Set the name of the Entry.
    - Name: Set the name of the Object to create.
    - Data: Data to pass to object creator function."""
    ...
def FBCycleAnalysisNode_TypeInfo()->int:...
def FBCycleCreator_TypeInfo()->int:...
def FBDeck_TypeInfo()->int:...
def FBDeformerPointCache_TypeInfo()->int:...
def FBDeformer_TypeInfo()->int:...
def FBDeleteCharacterPinningPreset(PresetName:str)->bool:
    """Deletes a pinning preset from the Character Controls Tool.
    ### Parameters:
    - PresetName: The preset name to delete (not the file path nor the filename of the preset).
    
    ### Returns:
    True if the operation is successful, false otherwise."""
    ...
def FBDeleteObjectsByName(NamePattern:str,NameSpace:str=None,GroupName:str=None)->int:
    """This function will query the system for objects fulfilling a particular name pattern and delete them. specify a namespace preferred, delete all objects with the group name without specified a namespace specified may lead to inconsistent in scene. Wrap multiple calls to FBDeleteObjectsByName() inside pair of FBPreventUIUpdateBegin() / FBPreventUIUpdateEnd() could improve application's performance.
    ### Parameters:
    - NamePattern: if not NULL, indicate the name pattern to search. This pattern can contain any amount of *. (ex: *tr*mod*scene ). if is `None` or Empty string, * will be used for match all.
    - NameSpace: if not NULL, the objects must be inside the given namespace.
    - GroupName: if not NULL, indicate the object group name (type).
    
    ### Returns:
    the count of objects found and deleted."""
    ...
def FBDeviceInstrument_TypeInfo()->int:...
def FBDeviceOpticalMarker_TypeInfo()->int:...
def FBDeviceOptical_TypeInfo()->int:...
def FBDevice_TypeInfo()->int:...
def FBDisconnect(Src:FBPlug,Dst:FBPlug)->bool:
    """Connect two FBPlug objects.
    ### Parameters:
    - Src: Source plug.
    - Dst: Destination plug.
    
    ### Returns:
    A boolean indicating success (True) or failure (False).
    
    ### Remarks:
    This global function is used primarily to disconnect connectors in a FBConstraintRelation ."""
    ...
def FBDot(V1:FBVector4d,V2:FBVector4d)->float:
    """Calculate the dot product of two vectors.
    ### Parameters:
    - V1: 1st vector.
    - V2: 2nd vector.
    
    ### Returns:
    Dot product."""
    ...
def FBEditColor_TypeInfo()->int:...
def FBEditNumber_TypeInfo()->int:...
def FBEditPropertyModern_TypeInfo()->int:...
def FBEditProperty_TypeInfo()->int:...
def FBEditTimeCode_TypeInfo()->int:...
def FBEditVector_TypeInfo()->int:...
def FBEdit_TypeInfo()->int:...
def FBEndChangeAllModels():
    """Call end change to all models (should be first open)."""
    ...
def FBEvaluateManager_TypeInfo()->int:...
def FBFCurveEditorUtility_TypeInfo()->int:...
def FBFCurveEditor_TypeInfo()->int:...
def FBFCurveEventManager_TypeInfo()->int:...
def FBFCurve_TypeInfo()->int:...
def FBFbxOptions_TypeInfo()->int:...
def FBFileMonitoringManager_TypeInfo()->int:...
def FBFileReference_TypeInfo()->int:...
def FBFilter_TypeInfo()->int:...
def FBFindModelByLabelName(ModelLabelName:str)->FBModel:
    """Find a model in the scene by its label name.
    Searches the scene for a model, based on the model's label name. Label name is "NameSpaceName:ObjectName". also known as "PrefixName::ObjectName" Full name is "GroupName::NameSpaceName:ObjectName".
    ### Parameters:
    - ModelLabelName: LabelName of model to search for. Specify it with schema like "NameSpaceName:ObjectName",or "ObjectName" if no NameSpaceName.
    
    ### Returns:
    A handle onto the model with Label name matching, returns `None` if no model was found by the search."""
    ...
def FBFindModelByUniqueColorId(Color:FBColor)->FBModel:
    """Find a model in the scene by its unique color id.
    A model could have a single unique ColorID, but SDK plugin user could request additional ColorID per model to support multi sub items picking. see FBModel::SetAdditionalUniqueColorIDCount() .
    ### Parameters:
    - Color: Color channel values are in range of [0,1] with precision 1.0/255
    ### Returns:
    A handle onto the model with unique color id matching, returns `None` if no model was found by the search. In pyfbsdk return tuple [model, subItemIndex]"""
    ...
def FBFindObjectByFullName(ObjectFullName:str)->FBComponent:
    """This function will query the system for an object with its FullName matching. Full name is "GroupName::NameSpaceName:ObjectName". Label name is "NameSpaceName:ObjectName". also known as "PrefixName::ObjectName"
    ### Parameters:
    - ObjectFullName: Full Name of object to search for. Specify it with schema like "GroupName::NameSpaceName:ObjectName",or "GroupName::ObjectName" if no NameSpaceName.
    
    ### Returns:
    A handle onto the object with Full name matching ObjectFullName, returns `None` if no object was found by the search."""
    ...
def FBFindObjectsByName(NamePattern:str,List:FBComponentList,bIncludeNamespace:bool=True,bModelsOnly:bool=False):
    """This function will query the system for objects fulfilling a particular name pattern
    ### Parameters:
    - NamePattern: Indicate the name pattern to search. This pattern can contain any amount of *. (ex: *tr*mod*scene )
    - List: List that contains the objects
    - bIncludeNamespace: Does the search use the complete name (with namespace)
    - bModelsOnly: Is the search on models or all types of objects"""
    ...
def FBFolder_TypeInfo()->int:...
def FBGenericMenuItem_TypeInfo()->int:...
def FBGenericMenu_TypeInfo()->int:...
def FBGeometry_TypeInfo()->int:...
def FBGetActorMarkerSetVisibility()->bool:
    """Queries visibility of the marker set of the current actor.
    ### Returns:
    True if the marker set of the current actor are visible, or false if it is hidden."""
    ...
def FBGetCharacterExternalSolverCount()->int:...
def FBGetCharacterExternalSolverIndex(arg1:str)->int:...
def FBGetCharacterExternalSolverName(arg1)->str:...
def FBGetCharacterFingerTipsVisibility()->bool:
    """Queries visibility of the finger-tips of the current character.
    ### Returns:
    True if finger-tips of the current character are visible, or false if they are hidden."""
    ...
def FBGetCharacterFloorContactsVisibility()->bool:
    """Queries visibility of the floor contacts of the current character.
    ### Returns:
    True if floor contacts of the current character are visible, or false if they are hidden."""
    ...
def FBGetCharactersKeyingMode()->FBCharacterKeyingMode:
    """return Character Manipulation/Keying Mode
    ### Returns:
    Keying Mode"""
    ...
def FBGetConstantKeyReducerThresholdValue(ThresholdType:FBConstantKeyReducerThresholdType)->float:
    """Return a specific threshold value used by the Constant Key Reducer filter.
    ### Parameters:
    - ThresholdType: The threshold type to retrieve its value.
    
    ### Returns:
    The threshold value."""
    ...
def FBGetContinuousRotation(ROut:FBVector3d,R0:FBVector3d,R1:FBVector3d):
    """Get a continuous rotation in Euler space.
    This routine will help to avoid gimble locks due to interpolation.
    ### Return values:
    - ROut: Successful continuous rotation (gimble-lock free).
    
    ### Parameters:
    - R0: Suggested next rotation.
    - R1: Previous rotation."""
    ...
def FBGetDisplayInfo()->FBEvaluateInfo:...
def FBGetEffectorBodyPart(EffectorId:FBEffectorId)->FBBodyPartId:
    """return BodyPart ID from Effector.
    ### Parameters:
    - EffectorId: Effector ID.
    
    ### Returns:
    ID of the BodyPart the effector is in."""
    ...
def FBGetEvaluationTaskCycle()->FBProfileTaskCycle:...
def FBGetGlobalMatrix(Matrix:FBMatrix,MatrixParent:FBMatrix,LocalMatrix:FBMatrix):
    """Get global matrix from parent and child matrices.
    From an input referential, this function will calculate the global matrix corresponding to the input local matrix (which is with respect to the parent matrix).
    ### Return values:
    - Matrix: Calculated local matrix.
    
    ### Parameters:
    - MatrixParent: Parent matrix.
    - LocalMatrix: Local matrix."""
    ...
def FBGetLastSelectedModel()->FBModel:
    """Get the last selected model, which is the one having the manipulator in the viewer.
    ### Returns:
    The last selected model or nullptr (C++) or None (Python) if no model is selected."""
    ...
def FBGetLocalMatrix(Matrix:FBMatrix,MatrixParent:FBMatrix,MatrixChild:FBMatrix):
    """Get local matrix from parent and child matrices.
    Will calculate the local matrix from two global matrices. The resulting matrix will be a local matrix containing the local transformations to go from the parent referentialto the child referential.
    ### Return values:
    - Matrix: Calculated local matrix.
    
    ### Parameters:
    - MatrixParent: Parent matrix (new base referential).
    - MatrixChild: Child matrix."""
    ...
def FBGetMainThreadTaskCycle()->FBProfileTaskCycle:...
def FBGetMainWindow()->int:
    """Return the MotionBuilder main window.
    ### Returns:
    The MotionBuilder main window.
    The following Python snippet shows how to get the MotionBuilder main window. from PySide2 import QtWidgets"""
    ...
@overload
def FBGetMultiLangText(Context:FBPlug,Key:str,bFlagReturnKey:bool=False)->str:
    """Name lookup in the context of an object.
    Most application objects have an internal name which differs from the name shown by the GUI. This will often be the case for the names of an object's properties.
    The way that support for multiple languages has been implemented is using conversion tables that will map the internal name to a localized name. Since the same internal name might mean different things for different objects, we can provide a context to help the lookup process.
    In this case, the context is a class object instance. When the lookup fails within a context, we sucessively try a lookup using the parent classes in the object hierarchy.
    It is important to note that for given property, it only knows about its internal name. The localized name is not attached to the property object itself as it resides elsewhere, in a lookup table. This is also the case for any other application object.
    The lookup table used to find the localized, or GUI name, of an object is dependent on the current language used. This information is available via the class FBMultiLangManager , which can indicate which language are availables and provides methode to query and change the current language.
    ### Parameters:
    - Context: Object which dictates the context of the lookup.
    - Key: String to look up.
    - bFlagReturnKey: Should the lookup fail, will return the key instead of an empty string.
    
    ### Returns:
    The corresponding string if the lookup was succesfull. If not will return an empty string if bFlagReturnKey was false. Otherwise will return the key string.
    Python sample code: from pyfbsdk import *"""
    ...
@overload
def FBGetMultiLangText(Context:str,Key:str,bFlagReturnKey:bool=False)->str:
    """Name lookup in the context of an object.
    Most application objects have an internal name which differs from the name shown by the GUI. This will often be the case for the names of an object's properties.
    The way that support for multiple languages has been implemented is using conversion tables that will map the internal name to a localized name. Since the same internal name might mean different things for different objects, we can provide a context to help the lookup process.
    In this case, the context is a class object instance. When the lookup fails within a context, we sucessively try a lookup using the parent classes in the object hierarchy.
    It is important to note that for given property, it only knows about its internal name. The localized name is not attached to the property object itself as it resides elsewhere, in a lookup table. This is also the case for any other application object.
    The lookup table used to find the localized, or GUI name, of an object is dependent on the current language used. This information is available via the class FBMultiLangManager , which can indicate which language are availables and provides methode to query and change the current language.
    ### Parameters:
    - Context: Object which dictates the context of the lookup.
    - Key: String to look up.
    - bFlagReturnKey: Should the lookup fail, will return the key instead of an empty string.
    
    ### Returns:
    The corresponding string if the lookup was succesfull. If not will return an empty string if bFlagReturnKey was false. Otherwise will return the key string.
    Python sample code: from pyfbsdk import *"""
    ...
def FBGetRenderingTaskCycle()->FBProfileTaskCycle:...
def FBGetSelectedModels(List:FBModelList,Parent:FBModel=None,bSelected:bool=True,bSortBySelectOrder:bool=False):
    """Find all models that are selected (if bSelected is true) Searches recursively from a root model for models that are selected, and adds them to a list of models.
    ### Return values:
    - List: List to add found models to.
    
    ### Parameters:
    - Parent: Root model to look from (default=NULL(root)).
    - bSelected: true to find selected models, false to find unselected models(default=true).
    - bSortBySelectOrder: true to sort the result by selection order, first selected model in the first part of the list; false to sort the result by scene graph order"""
    ...
def FBGlobalLight_TypeInfo()->int:...
def FBGroup_TypeInfo()->int:...
def FBHUDBloopSlateElement_TypeInfo()->int:...
def FBHUDElement_TypeInfo()->int:...
def FBHUDFlashElement_TypeInfo()->int:...
def FBHUDManager_TypeInfo()->int:...
def FBHUDRectElement_TypeInfo()->int:...
def FBHUDTextElement_TypeInfo()->int:...
def FBHUDTextureElement_TypeInfo()->int:...
def FBHUDTimelineElement_TypeInfo()->int:...
def FBHUD_TypeInfo()->int:...
def FBHandle_TypeInfo()->int:...
def FBImageContainer_TypeInfo()->int:...
def FBImage_TypeInfo()->int:...
@overload
def FBInterpolateRotation(ROut:FBVector3d,R0:FBVector3d,R1:FBVector3d,U:float):
    """Interpolate a rotation in Euler space.
    ### Return values:
    - ROut: Resulting, interpolated rotation.
    
    ### Parameters:
    - R0: 1st rotation.
    - R1: 2nd rotation.
    - U: Interpolation ratio."""
    ...
@overload
def FBInterpolateRotation(ROut:FBVector4d,R0:FBVector4d,R1:FBVector4d,U:float):
    """Interpolate a rotation in Euler space.
    ### Return values:
    - ROut: Resulting, interpolated rotation.
    
    ### Parameters:
    - R0: 1st rotation.
    - R1: 2nd rotation.
    - U: Interpolation ratio."""
    ...
def FBKeyControl_TypeInfo()->int:...
def FBKeyingGroup_TypeInfo()->int:...
def FBLabel_TypeInfo()->int:...
def FBLayeredTexture_TypeInfo()->int:...
def FBLayoutRegion_TypeInfo()->int:...
def FBLayout_TypeInfo()->int:...
@overload
def FBLength(V:FBVector4d)->float:
    """Get the length of a vertex (from origin)
    ### Parameters:
    - V: Vertex for which length is to be measured.
    
    ### Returns:
    Length of vertex (from origin)."""
    ...
@overload
def FBLength(V:FBVertex)->float:
    """Get the length of a vertex (from origin)
    ### Parameters:
    - V: Vertex for which length is to be measured.
    
    ### Returns:
    Length of vertex (from origin)."""
    ...
def FBLight_TypeInfo()->int:...
def FBList_TypeInfo()->int:...
def FBLoadCharacterPinningPreset(PresetName:str)->bool:
    """Loads a pinning preset in the Character Controls Tool.
    ### Parameters:
    - PresetName: The preset name to load (not the file path nor the filename of the preset).
    
    ### Returns:
    True if the operation is successful, false otherwise."""
    ...
def FBLoadFbxPrimitivesModel(ModelName:str)->FBModel:
    """Load a model.
    ### Parameters:
    - ModelName: Name of primitive model to load.
    
    ### Returns:
    A handle onto the model that was loaded, returns `None` if no model was found."""
    ...
def FBLogger_TypeInfo()->int:...
def FBManipulator_TypeInfo()->int:...
def FBMarkerSet_TypeInfo()->int:...
def FBMaterial_TypeInfo()->int:...
def FBMatrixInverse(Matrix:FBMatrix,Src:FBMatrix):
    """Invert a matrix.
    ### Return values:
    - Matrix: Calculated inverse matrix.
    
    ### Parameters:
    - Src: Source matrix to invert."""
    ...
def FBMatrixMult(Matrix:FBMatrix,A:FBMatrix,B:FBMatrix):
    """Multiply two matrices.
    ### Return values:
    - Matrix: Calculated resulting matrix.
    
    ### Parameters:
    - A: 1st matrix.
    - B: 2nd matrix."""
    ...
def FBMatrixOrthogonalize(Matrix:FBMatrix):
    """Make sure that rotation vectors are orthogonal and normalized (fast way for removing scaling from matrix)
    ### Return values:
    - Matrix: Orthogonalized matrix.
    
    ### Parameters:
    - Matrix: Rotation Matrix to Orthogonalize."""
    ...
def FBMatrixToQuaternion(Quaternion:FBVector4d,Matrix:FBMatrix):
    """Get a quaternion from a matrix (potential ).
    ### Return values:
    - Quaternion: Calculated quaternion.
    
    ### Parameters:
    - Matrix: Input matrix.
    
    ### Warning:
    Matrix can contain scaling and/or translation, we orthogonalize matrix before."""
    ...
def FBMatrixToRotation(Vector:FBVector3d,Matrix:FBMatrix,RotationOrder:FBRotationOrder=FBRotationOrder.kFBXYZ):
    """Obtain rotation vector from a matrix.
    ### Return values:
    - Vector: Extracted rotation vector, ordered the same way as the rotation order specified by RotationOrder.
    
    ### Parameters:
    - Matrix: Input matrix.
    - RotationOrder: Rotation order."""
    ...
def FBMatrixToRotationWithPrecision(Vector:FBVector3d,Matrix:FBMatrix,RotationOrder:FBRotationOrder,Precision:float):
    """Obtain rotation vector from a matrix.
    ### Return values:
    - Vector: Extracted rotation vector.
    
    ### Parameters:
    - Matrix: Input matrix.
    - RotationOrder: Rotation Order.
    - Precision: Indicate the precision level (pow(10.0, -Precision)) used when calculating the threshold value for gimble lock.
    
    ### Warning:
    Rotation is in EulerXYZ or EulerZYX only"""
    ...
def FBMatrixToScaling(Vector:FBSVector,Matrix:FBMatrix):
    """Obtain scaling vector from a matrix.
    ### Return values:
    - Vector: Extracted scaling vector.
    
    ### Parameters:
    - Matrix: Input matrix."""
    ...
def FBMatrixToTQS(TVector:FBVector4d,Quaternion:FBVector4d,SVector:FBSVector,Matrix:FBMatrix):
    """Obtain translation vector, rotation quaternion, and scaling vector from a matrix.
    ### Return values:
    - TVector: Extracted translation vector.
    - Quaternion: Extracted rotation quaternion.
    - SVector: Extracted scaling vector.
    
    ### Parameters:
    - Matrix: Input matrix."""
    ...
def FBMatrixToTRS(TVector:FBVector4d,RVector:FBVector3d,SVector:FBSVector,Matrix:FBMatrix):
    """Obtain translation, rotation, and scaling vectors from a matrix.
    ### Return values:
    - TVector: Extracted translation vector.
    - RVector: Extracted rotation vector.
    - SVector: Extracted scaling vector.
    
    ### Parameters:
    - Matrix: Input matrix.
    
    ### Warning:
    Rotation is in EulerXYZ"""
    ...
def FBMatrixToTranslation(Vector:FBVector4d,Matrix:FBMatrix):
    """Obtain translation vector from a matrix.
    ### Return values:
    - Vector: Extracted translation vector.
    
    ### Parameters:
    - Matrix: Input matrix."""
    ...
def FBMatrixTranspose(Matrix:FBMatrix,Src:FBMatrix):
    """Transpose a matrix.
    ### Return values:
    - Matrix: Calculated transpose matrix.
    
    ### Parameters:
    - Src: Source matrix to transpose."""
    ...
def FBMemo_TypeInfo()->int:...
def FBMenuManager_TypeInfo()->int:...
def FBMergeTransactionBegin():
    """Call to begin the transaction for merging multiple files.
    Useful to consecutively merge multiple files into scene.
    ### Note:
    The transaction need to be closed by calling FBMergeTransactionEnd() . There is no need to call FBPreventUIUpdateBegin() with this function, since it already contains the same optimization."""
    ...
def FBMergeTransactionEnd():
    """Call to end the merge transaction."""
    ...
def FBMergeTransactionFileRefEditBegin():
    """Call to begin the transaction for merging multiple files and applying File Reference edit at the same time.
    Useful to consecutively merge multiple files into scene with FileRef edit operation in between.
    ### Note:
    The transaction need to be closed by calling FBMergeTransactionFileRefEditEnd() ."""
    ...
def FBMergeTransactionFileRefEditEnd():
    """Call to end merge transaction with File Reference edit."""
    ...
def FBMergeTransactionFileRefEditIsOn()->bool:
    """Call to tell if system is during File Reference Edit Merge transaction."""
    ...
def FBMergeTransactionIsOn()->bool:
    """Call to tell if system is during Merge transaction."""
    ...
def FBMesh_TypeInfo()->int:...
def FBMessageBox(BoxTitle:str,Message:str,Button1Str:str,Button2Str:str=None,Button3Str:str=None,DefaultButton:int=0,ScrolledMessage:int=0)->int:
    """Dialog popup box.
    Opens a message box containing a message and up to three buttons. Waits for the user to click a button.
    ### Parameters:
    - BoxTitle: Title of message box.
    - Message: Message to place in box.
    - Button1Str: String for first button (Cannot be NULL).
    - Button2Str: String for second button (NULL will not create a button).
    - Button3Str: String for third button (NULL will not create a button).
    - DefaultButton: Indicates the default (pre-selected) button (default is 0).
    - ScrolledMessage: Scroll message (default is 0).
    
    ### Returns:
    The number of the button selected."""
    ...
def FBMessageBoxGetUserValue(BoxTitle:str,Message:str,Value:None,ValueType:FBPopupInputType,Button1Str:str,Button2Str:str=None,Button3Str:str=None,DefaultButton:int=0,bLastButtonCancel:bool=True)->int:
    """Dialog popup box to get user input.
    Opens a message box, with up to three buttons, asking the user to enter data. The type of data to be entered is specified by the Value and ValueType parameters.
    ### Parameters:
    - BoxTitle: Title of message box.
    - Message: Message to place in box.
    
    ### Return values:
    - Value: Value entered by user (must correspond with ValueType).
    
    ### Parameters:
    - ValueType: Type of pointer specified in Value.
    - Button1Str: String for first button (Cannot be NULL).
    - Button2Str: String for second button (NULL will not create a button).
    - Button3Str: String for third button (NULL will not create a button).
    - DefaultButton: Indicates the default (pre-selected) button(default=0).
    - bLastButtonCancel: Indicates the last button is Cancel (if more than one button) so Value won't be updated if the last button is clicked.
    
    ### Returns:
    The number of the button selected."""
    ...
def FBMessageBoxWithCheck(BoxTitle:str,Message:str,Button1Str:str,Button2Str:str,Button3Str:str,CheckBoxStr:str,bCheckBoxValue:bool,DefaultButton:int=0,ScrolledMessage:int=0)->int:
    """Dialog popup box with a check box.
    Opens a message box containing a message, up to three buttons and a check box. Waits for the user to click a button.
    ### Parameters:
    - BoxTitle: Title of message box.
    - Message: Message to place in box.
    - Button1Str: String for first button (Cannot be NULL).
    - Button2Str: String for second button (NULL will not create a button).
    - Button3Str: String for third button (NULL will not create a button).
    - CheckBoxStr: Check box string (Cannot be NULL).
    
    ### Return values:
    - bCheckBoxValue: Check box value.
    
    ### Parameters:
    - DefaultButton: Indicates the default (pre-selected) button (default is 0).
    - ScrolledMessage: Scroll message (default is 0).
    
    ### Returns:
    The number of the button selected."""
    ...
def FBModelCube_TypeInfo()->int:...
def FBModelMarkerOptical_TypeInfo()->int:...
def FBModelMarker_TypeInfo()->int:...
def FBModelNull_TypeInfo()->int:...
def FBModelOpticalAdvanced_TypeInfo()->int:...
def FBModelOptical_TypeInfo()->int:...
def FBModelPath3D_TypeInfo()->int:...
def FBModelPlaceHolder_TypeInfo()->int:...
def FBModelPlane_TypeInfo()->int:...
def FBModelRoot_TypeInfo()->int:...
def FBModelSkeleton_TypeInfo()->int:...
def FBModelTemplate_TypeInfo()->int:...
def FBModelTransactionBegin():
    """This set of functions speeds up the process of batch operations on models."""
    ...
def FBModelTransactionEnd():
    """This set of functions speeds up the process of batch operations on models."""
    ...
def FBModelVertexData_TypeInfo()->int:...
def FBModel_TypeInfo()->int:...
def FBMotionClip_TypeInfo()->int:...
def FBMotionFileOptions_TypeInfo()->int:...
@overload
def FBMult(Result:FBVector4d,V1:FBVector4d,V2:float):
    """Multiply V2 from V1 ( Result = V1 * V2 )
    ### Return values:
    - Result: Resulting vector.
    
    ### Parameters:
    - V1: 1st vector.
    - V2: 2nd vector."""
    ...
@overload
def FBMult(Result:FBVector4d,V1:FBVector4d,V2:FBVector4d):
    """Multiply V2 from V1 ( Result = V1 * V2 )
    ### Return values:
    - Result: Resulting vector.
    
    ### Parameters:
    - V1: 1st vector.
    - V2: 2nd vector."""
    ...
@overload
def FBMult(Result:FBMatrix,V1:FBMatrix,V2:FBSVector):
    """Multiply V2 from V1 ( Result = V1 * V2 )
    ### Return values:
    - Result: Resulting vector.
    
    ### Parameters:
    - V1: 1st vector.
    - V2: 2nd vector."""
    ...
@overload
def FBMult(Result:FBMatrix,V1:FBMatrix,V2:FBSVector):
    """Multiply V2 from V1 ( Result = V1 * V2 )
    ### Return values:
    - Result: Resulting vector.
    
    ### Parameters:
    - V1: 1st vector.
    - V2: 2nd vector."""
    ...
def FBNamespace_TypeInfo()->int:...
def FBNote_TypeInfo()->int:...
def FBNurbs_TypeInfo()->int:...
def FBObjectGetGlobalUniqueId()->int:
    """Get the global static object unique ID counter.
    Each new created object will be assigned this global unique ID. Object.UniqueID = GlobalUniqueID++"""
    ...
def FBObjectGetLivingCount()->int:
    """Get current total living object count."""
    ...
def FBObjectLifeLogEnable(bEnable:bool):
    """Enable object creation / deletion logging.
    Default logging if off This logging may hurt performance slightly. use it only for debug purpose.
    ### Parameters:
    - bEnable: true to enable logging."""
    ...
def FBObjectPose_TypeInfo()->int:...
def FBObjectPrintLivings(StartUniqueId:int):
    """Print those living objects created when logging is enabled.
    ### Parameters:
    - StartUniqueId: Any living object has been logged and with its uniqueId no less than StartUniqueId will be printed out."""
    ...
def FBObject_GetEntryCount(arg1)->int:...
def FBObject_GetEntryDLLName(arg1,arg2,arg3=None)->str:...
def FBObject_GetEntryDescription(arg1,arg2,arg3=None)->str:...
def FBObject_GetEntryName(arg1,arg2)->str:...
def FBObject_GetGroupCount()->int:
    """A set of functions to query the registration table."""
    ...
def FBObject_GetGroupName(arg1)->str:...
def FBObject_GetIconName(arg1,arg2,arg3=None)->str:...
def FBObject_GetMultiplicity(arg1,arg2,arg3=None)->bool:...
def FBOpticalGap_TypeInfo()->int:...
def FBOpticalSegment_TypeInfo()->int:...
def FBPatch_TypeInfo()->int:...
def FBPhysicalProperties_TypeInfo()->int:...
def FBPlayerControl_TypeInfo()->int:...
def FBPlotPopup_TypeInfo()->int:...
def FBPlug_TypeInfo()->int:...
def FBPointCacheFile_TypeInfo()->int:...
def FBPointCacheManager_TypeInfo()->int:...
def FBPopNormalTool(ToolName:str,bSetFocus:bool=True)->bool:
    """This function is used to bring up a specific tool in the GUI.
    ### Parameters:
    - ToolName: The name of the tool as shown in the Open Reality menu.
    - bSetFocus: Indicate if the tool will have the focus.
    
    ### Returns:
    If the tool was brought up successfully."""
    ...
def FBPopup_TypeInfo()->int:...
def FBPose_TypeInfo()->int:...
def FBPreventUIUpdateBegin():
    """Call to prevent UI updates when creating/deleting/renaming objects.
    Useful to speed up script operations. Previously, FBMergeTransactionBegin() / FBMergeTransactionEnd() could be used to do this kind of optimization, even if no merge operations were done. However, using FBMergeTransactionBegin() / FBMergeTransactionEnd() with non-merge operation could lead to issues, like objects with invalid namespaces. FBPreventUIUpdateBegin() /FBPreventUIUpdateEnd() fix this issue, while giving the same speed increase.
    ### Note:
    The transaction need to be closed by calling FBPreventUIUpdateEnd() . There is no need to call this function when using FBMergeTransactionBegin() , since FBMergeTransactionBegin() already has the same optimization."""
    ...
def FBPreventUIUpdateEnd():
    """Call to end blocking the UI updates."""
    ...
def FBPreventUIUpdateIsOn():
    """Call to tell if UI updates are blocked."""
    ...
def FBProfiler_TypeInfo()->int:...
def FBProgress_TypeInfo()->int:...
def FBPropertyConnectionEditor_TypeInfo()->int:...
def FBPropertyViewManager_TypeInfo()->int:...
def FBProperty_TypeInfo()->int:...
def FBQAdd(Result:FBVector4d,Q1:FBVector4d,Q2:FBVector4d):
    """Add two quaternions together ( Result = Q1 + Q2 )
    ### Return values:
    - Result: Resulting quaternion.
    
    ### Parameters:
    - Q1: 1st quaternion.
    - Q2: 2nd quaternion."""
    ...
def FBQDot(Q1:FBVector4d,Q2:FBVector4d)->float:
    """Calculate the dot product of two quaternions.
    ### Parameters:
    - Q1: 1st quaternion.
    - Q2: 2nd quaternion.
    
    ### Returns:
    Dot product."""
    ...
def FBQLength(Q:FBVector4d)->float:
    """Get the length of a quaternion.
    ### Parameters:
    - Q: Quaternion to calculate length for.
    
    ### Returns:
    Length of quaternion Q ."""
    ...
@overload
def FBQMult(Result:FBVector4d,Q1:FBVector4d,Q2:float):
    """Multiply Q2 from Q1 ( Result = Q1 * Q2 )
    ### Return values:
    - Result: Resulting quaternion.
    
    ### Parameters:
    - Q1: 1st quaternion.
    - Q2: 2nd quaternion."""
    ...
@overload
def FBQMult(Result:FBVector4d,Q1:FBVector4d,Q2:FBVector4d):
    """Multiply Q2 from Q1 ( Result = Q1 * Q2 )
    ### Return values:
    - Result: Resulting quaternion.
    
    ### Parameters:
    - Q1: 1st quaternion.
    - Q2: 2nd quaternion."""
    ...
def FBQSub(Result:FBVector4d,Q1:FBVector4d,Q2:FBVector4d):
    """Subtract Q2 from Q1 ( Result = Q1 - Q2 )
    ### Return values:
    - Result: Resulting quaternion.
    
    ### Parameters:
    - Q1: 1st quaternion.
    - Q2: 2nd quaternion."""
    ...
def FBQuaternionToMatrix(Matrix:FBMatrix,Quaternion:FBVector4d):
    """Get a rotation matrix from a quaternion vector.
    ### Return values:
    - Matrix: Calculated rotation matrix.
    
    ### Parameters:
    - Quaternion: Input quaternion."""
    ...
def FBQuaternionToRotation(Vector:FBVector3d,Quaternion:FBVector4d,RotationOrder:FBRotationOrder=FBRotationOrder.kFBXYZ):
    """Get a rotation vector from a quaternion vector.
    ### Return values:
    - Vector: Calculated rotation vector, ordered the same way as the rotation order specified by RotationOrder.
    
    ### Parameters:
    - Quaternion: Input quaternion.
    - RotationOrder: Rotation order.
    
    ### Warning:
    Rotation is in EulerXYZ or kFBZYX only"""
    ...
def FBQuaternionToRotationWithPrecision(Vector:FBVector3d,Quaternion:FBVector4d,RotationOrder:FBRotationOrder,Precision:float):
    """Get a rotation vector from a quaternion vector.
    ### Return values:
    - Vector: Calculated rotation vector.
    
    ### Parameters:
    - Quaternion: Input quaternion.
    - RotationOrder: Rotation order of the rotation vector.
    - Precision: Indicate the precision level (pow(10.0, -Precision)) used when calculating the threshold value for gimble lock.
    
    ### Warning:
    Rotation is in EulerXYZ or kFBZYX only"""
    ...
def FBReferenceTime_TypeInfo()->int:...
def FBRendererCallback_TypeInfo()->int:...
def FBRenderer_TypeInfo()->int:...
def FBRigidBody_TypeInfo()->int:...
def FBRotationToMatrix(Matrix:FBMatrix,Vector:FBVector3d,RotationOrder:FBRotationOrder=FBRotationOrder.kFBXYZ):
    """Convert a rotation vector to a matrix.
    ### Return values:
    - Matrix: Calculated resulting matrix.
    
    ### Parameters:
    - Vector: Rotation vector, ordered the same way as the rotation order specified by RotationOrder.
    - RotationOrder: Rotation order."""
    ...
def FBRotationToQuaternion(Quaternion:FBVector4d,Vector:FBVector3d,RotationOrder:FBRotationOrder=FBRotationOrder.kFBXYZ):
    """Get a quaternion from a rotation vector.
    ### Return values:
    - Quaternion: Calculated quaternion.
    
    ### Parameters:
    - Vector: Input rotation vector, ordered the same way as the rotation order specified by RotationOrder.
    - RotationOrder: Rotation order."""
    ...
def FBSaveCharacterPinningPreset(PresetName:str,bAllowOverwriting:bool=False)->bool:
    """Saves a pinning preset from the current pinning values in the Character Controls Tool.
    ### Parameters:
    - PresetName: The preset name to save (not the file path nor the filename of the preset).
    - bAllowOverwriting: True to allow overwriting an existing preset having the same name as the one provided, false otherwise.
    
    ### Returns:
    True if the operation is successful, false otherwise."""
    ...
def FBScalingToMatrix(Matrix:FBMatrix,Vector:FBSVector):
    """Convert a scaling vector to a matrix.
    ### Return values:
    - Matrix: Calculated resulting matrix.
    
    ### Parameters:
    - Vector: Scaling vector."""
    ...
def FBScene_TypeInfo()->int:...
def FBSchedulingDependencyOutput(bEnable:bool):
    """Debug function for MT dependency debug.
    When enabled log file will be created and updated each time MultiThreaded scheduling is happening (scene rebuild)
    ### Parameters:
    - bEnable: ON/OFF switch. This is not stored in config (should be changed only for debug purpose, because slow down rebuild process )"""
    ...
def FBScrollBox_TypeInfo()->int:...
def FBSetActorMarkerSetVisibility(bShow:bool)->bool:
    """Sets visibility of the marker set of the current actor.
    ### Parameters:
    - bShow: Specifies if the market of the current actor should be visible.
    
    ### Returns:
    True if the operation is successful, false otherwise."""
    ...
def FBSetCharacterFingerTipsVisibility(bShow:bool):
    """Sets visibility of the finger-tips of the current character.
    ### Parameters:
    - bShow: Specifies if finger-tips of the current character should be visible."""
    ...
def FBSetCharacterFloorContactsVisibility(bShow:bool):
    """Sets visibility of the floor contacts of the current character.
    ### Parameters:
    - bShow: Specifies if floor contacts of the current character should be visible."""
    ...
def FBSetConstantKeyReducerThresholdValue(ThresholdType:FBConstantKeyReducerThresholdType,Value:float):
    """Set a specific threshold value used by the Constant Key Reducer filter.
    ### Parameters:
    - ThresholdType: The threshold type to set its value.
    - Value: The new threshold value to set."""
    ...
def FBSetLastSelectedModel(Model:FBModel):
    """Set the given model as the last one selected, so the manipulator in the viewer will then be on that particular model.
    If the model is not selected, it will also be selected.
    ### Parameters:
    - Model: Model that will be flagged as the last selected model."""
    ...
def FBSet_TypeInfo()->int:...
def FBShaderLighted_TypeInfo()->int:...
def FBShaderShadowLive_TypeInfo()->int:...
def FBShader_TypeInfo()->int:...
def FBSleep(MilliSeconds:int):
    """Sleep function Puts system to sleep for specified time.
    ### Parameters:
    - MilliSeconds: Time to sleep for."""
    ...
def FBSlider_TypeInfo()->int:...
def FBSpreadCell_TypeInfo()->int:...
def FBSpreadColumn_TypeInfo()->int:...
def FBSpreadPart_TypeInfo()->int:...
def FBSpreadRow_TypeInfo()->int:...
def FBSpread_TypeInfo()->int:...
def FBStoryClip_TypeInfo()->int:...
def FBStoryFolder_TypeInfo()->int:...
def FBStoryGroupClip_TypeInfo()->int:...
def FBStoryTrack_TypeInfo()->int:...
def FBStory_TypeInfo()->int:...
def FBSub(Result:FBVector4d,V1:FBVector4d,V2:FBVector4d):
    """Subtract V2 from V1 ( Result = V1 - V2 )
    ### Return values:
    - Result: Resulting vector.
    
    ### Parameters:
    - V1: 1st vector.
    - V2: 2nd vector."""
    ...
def FBSurface_TypeInfo()->int:...
def FBSystem_TypeInfo()->int:...
def FBTQSToMatrix(Matrix:FBMatrix,TVector:FBVector4d,Quaternion:FBVector4d,SVector:FBSVector):
    """Convert translation vector, rotation quaternion, and scaling vector to a matrix.
    ### Return values:
    - Matrix: Calculated resulting matrix.
    
    ### Parameters:
    - TVector: Translation vector.
    - Quaternion: Rotation quaternion.
    - SVector: Scaling vector."""
    ...
def FBTRSToMatrix(Matrix:FBMatrix,TVector:FBVector4d,RVector:FBVector3d,SVector:FBSVector):
    """Convert translation, rotation, and scaling vectors to a matrix.
    ### Return values:
    - Matrix: Calculated resulting matrix.
    
    ### Parameters:
    - TVector: Translation vector.
    - RVector: Rotation vector.
    - SVector: Scaling vector.
    
    ### Warning:
    Rotation is in EulerXYZ"""
    ...
def FBTabPanel_TypeInfo()->int:...
def FBTake_TypeInfo()->int:...
def FBTexture_TypeInfo()->int:...
def FBThermometer_TypeInfo()->int:...
def FBTimeWarpManager_TypeInfo()->int:...
def FBToolLayoutManager_TypeInfo()->int:...
def FBTool_TypeInfo()->int:...
def FBTrace(FormatString:str):
    """This function prints useful debugging strings in the console with kFBNORMAL_TRACE output detailed level.
    ### Parameters:
    - FormatString: A printf-style format string, to use the following arguments in the list.
    
    ### Warning:
    There is currently a limitation which sets the maximum length of the resulting string to be limited to 2048 bytes.
    Not thread safe, as an static array is used internally."""
    ...
def FBTraceGetLevel()->int:
    """Get Global Trace Detailed Level which affects all the output targets.
    ### Returns:
    Current global trace detailed level.
    
    ### Note:
    Python console trace current output level could be queried via pythonidelib.GetTraceLevel()."""
    ...
def FBTraceSetLevel(NewLevel:int):
    """Set Global Trace Detailed Level which affects all the output targets.
    ### Parameters:
    - NewLevel: Any trace message with detailed level higher than this new level will be ignored, valid value range [kFBNO_TRACE, kFBALL_TRACE]
    
    ### Note:
    Python console trace current output level could be further adjusted via pythonidelib.SetTraceLevel()."""
    ...
def FBTraceWithLevel(Level:int,FormatString:str):
    """This function prints useful debugging strings in the console.
    ### Parameters:
    - Level: to control trace output detailed level, valid value range [kFBCRITICAL_TRACE, kFBALL_TRACE]
    - FormatString: A printf-style format string, to use the following arguments in the list.
    
    ### Warning:
    There is currently a limitation which sets the maximum length of the resulting string to be limited to 2048 bytes.
    Not thread safe, as an static array is used internally."""
    ...
def FBTranslationToMatrix(Matrix:FBMatrix,Vector:FBVector4d):
    """Convert a translation vector to a matrix.
    ### Return values:
    - Matrix: Calculated resulting matrix.
    
    ### Parameters:
    - Vector: Translation vector."""
    ...
def FBTransportAudioManager_TypeInfo()->int:...
def FBTreeNode_TypeInfo()->int:...
def FBTree_TypeInfo()->int:...
def FBUndoManager_TypeInfo()->int:...
def FBUserObject_TypeInfo()->int:...
def FBVectorMatrixMult(OutVector:FBVector4d,Matrix:FBMatrix,Vector:FBVector4d):
    """Multiply a vector by a matrix.
    ### Return values:
    - OutVector: Resulting vector.
    
    ### Parameters:
    - Matrix: Matrix to affect the vector with.
    - Vector: Source vector."""
    ...
def FBVertexMatrixMult(OutVertex:FBVertex,Matrix:FBMatrix,Vertex:FBVertex):
    """Multiply a vertex by a matrix.
    ### Return values:
    - OutVertex: Resulting vertex.
    
    ### Parameters:
    - Matrix: Matrix to affect the vertex with.
    - Vertex: Source vertex."""
    ...
def FBVideoClipImage_TypeInfo()->int:...
def FBVideoClip_TypeInfo()->int:...
def FBVideoGrabber_TypeInfo()->int:...
def FBVideoIn_TypeInfo()->int:...
def FBVideoMemory_TypeInfo()->int:...
def FBVideoOut_TypeInfo()->int:...
def FBVideo_TypeInfo()->int:...
def FBView_TypeInfo()->int:...
def FBVisualComponent_TypeInfo()->int:...
def FBVisualContainer_TypeInfo()->int:...
def FBWebView_TypeInfo()->int:...
def FBWidgetHolder_TypeInfo()->int:...
def GetToolPosition(Tool:FBTool)->tuple:
    """This function will get the position of a specific tool.
    ### Parameters:
    - Tool: A pointer to the tool."""
    ...
def GetToolPositionByName(ToolName:str)->tuple:
    """This function will get the position of a specific tool.
    ### Parameters:
    - ToolName: The name of the tool as shown in the Open Reality menu."""
    ...
def GetToolSize(Tool:FBTool)->tuple:
    """This function will get the size of a specific tool in the GUI.
    ### Parameters:
    - Tool: A pointer to the tool."""
    ...
def GetToolSizeByName(ToolName:str)->tuple:
    """This function will get the size of a specific tool in the GUI.
    ### Parameters:
    - ToolName: The name of the tool as shown in the Open Reality menu."""
    ...
def SetToolPosition(Tool:FBTool,PosX:int,PosY:int):
    """This function will set the position of a specific tool.
    ### Parameters:
    - Tool: A pointer to the tool.
    - PosX: New position in X for the tool.
    - PosY: New position in Y for the tool."""
    ...
def SetToolPositionByName(ToolName:str,PosX:int,PosY:int):
    """This function will set the position of a specific tool.
    ### Parameters:
    - ToolName: The name of the tool as shown in the Open Reality menu.
    - PosX: New position in X for the tool.
    - PosY: New position in Y for the tool."""
    ...
def SetToolSize(Tool:FBTool,Width:int,Height:int):
    """This function will set the size of a specific tool in the GUI.
    ### Parameters:
    - Tool: A pointer to the tool.
    - Width: New width of the tool.
    - Height: New height of the tool."""
    ...
def SetToolSizeByName(ToolName:str,Width:int,Height:int):
    """This function will set the size of a specific tool in the GUI.
    ### Parameters:
    - ToolName: The name of the tool as shown in the Open Reality menu.
    - Width: New width of the tool.
    - Height: New height of the tool."""
    ...
def ShowTool(Tool:FBTool,bResizeWnd:bool=True)->FBTool:
    """This function will show a specific tool in the GUI.
    ### Parameters:
    - Tool: A pointer to the tool to show.
    - bResizeWnd: Adjust the size of the tool window if needed (if started too close to the end of the screen for example).
    
    ### Returns:
    A pointer to the FBTool object, `None` otherwise."""
    ...
def ShowToolByName(ToolName:str,bResizeWnd:bool=True)->FBTool:
    """This function will show a specific tool in the GUI.
    ### Parameters:
    - ToolName: The name of the tool as shown in the Open Reality menu.
    - bResizeWnd: Adjust the size of the tool window if needed (if started too close to the end of the screen for example).
    
    ### Returns:
    A pointer to the FBTool object, `None` otherwise."""
    ...