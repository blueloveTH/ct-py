import re
import os

enums_pyi = '''# ImDrawFlags_
ImDrawFlags_None = 0
ImDrawFlags_Closed = 1
ImDrawFlags_RoundCornersTopLeft = 16
ImDrawFlags_RoundCornersTopRight = 32
ImDrawFlags_RoundCornersBottomLeft = 64
ImDrawFlags_RoundCornersBottomRight = 128
ImDrawFlags_RoundCornersNone = 256
ImDrawFlags_RoundCornersTop = 48
ImDrawFlags_RoundCornersBottom = 192
ImDrawFlags_RoundCornersLeft = 80
ImDrawFlags_RoundCornersRight = 160
ImDrawFlags_RoundCornersAll = 240
ImDrawFlags_RoundCornersDefault_ = 240
ImDrawFlags_RoundCornersMask_ = 496

# ImDrawListFlags_
ImDrawListFlags_None = 0
ImDrawListFlags_AntiAliasedLines = 1
ImDrawListFlags_AntiAliasedLinesUseTex = 2
ImDrawListFlags_AntiAliasedFill = 4
ImDrawListFlags_AllowVtxOffset = 8

# ImFontAtlasFlags_
ImFontAtlasFlags_None = 0
ImFontAtlasFlags_NoPowerOfTwoHeight = 1
ImFontAtlasFlags_NoMouseCursors = 2
ImFontAtlasFlags_NoBakedLines = 4

# ImGuiActivateFlags_
ImGuiActivateFlags_None = 0
ImGuiActivateFlags_PreferInput = 1
ImGuiActivateFlags_PreferTweak = 2
ImGuiActivateFlags_TryToPreserveState = 4

# ImGuiAxis
ImGuiAxis_None = -1
ImGuiAxis_X = 0
ImGuiAxis_Y = 1

# ImGuiBackendFlags_
ImGuiBackendFlags_None = 0
ImGuiBackendFlags_HasGamepad = 1
ImGuiBackendFlags_HasMouseCursors = 2
ImGuiBackendFlags_HasSetMousePos = 4
ImGuiBackendFlags_RendererHasVtxOffset = 8

# ImGuiButtonFlagsPrivate_
ImGuiButtonFlags_PressedOnClick = 16
ImGuiButtonFlags_PressedOnClickRelease = 32
ImGuiButtonFlags_PressedOnClickReleaseAnywhere = 64
ImGuiButtonFlags_PressedOnRelease = 128
ImGuiButtonFlags_PressedOnDoubleClick = 256
ImGuiButtonFlags_PressedOnDragDropHold = 512
ImGuiButtonFlags_Repeat = 1024
ImGuiButtonFlags_FlattenChildren = 2048
ImGuiButtonFlags_AllowOverlap = 4096
ImGuiButtonFlags_DontClosePopups = 8192
ImGuiButtonFlags_AlignTextBaseLine = 32768
ImGuiButtonFlags_NoKeyModifiers = 65536
ImGuiButtonFlags_NoHoldingActiveId = 131072
ImGuiButtonFlags_NoNavFocus = 262144
ImGuiButtonFlags_NoHoveredOnFocus = 524288
ImGuiButtonFlags_NoSetKeyOwner = 1048576
ImGuiButtonFlags_NoTestKeyOwner = 2097152
ImGuiButtonFlags_PressedOnMask_ = 1008
ImGuiButtonFlags_PressedOnDefault_ = 32

# ImGuiButtonFlags_
ImGuiButtonFlags_None = 0
ImGuiButtonFlags_MouseButtonLeft = 1
ImGuiButtonFlags_MouseButtonRight = 2
ImGuiButtonFlags_MouseButtonMiddle = 4
ImGuiButtonFlags_MouseButtonMask_ = 7
ImGuiButtonFlags_MouseButtonDefault_ = 1

# ImGuiCol_
ImGuiCol_Text = 0
ImGuiCol_TextDisabled = 1
ImGuiCol_WindowBg = 2
ImGuiCol_ChildBg = 3
ImGuiCol_PopupBg = 4
ImGuiCol_Border = 5
ImGuiCol_BorderShadow = 6
ImGuiCol_FrameBg = 7
ImGuiCol_FrameBgHovered = 8
ImGuiCol_FrameBgActive = 9
ImGuiCol_TitleBg = 10
ImGuiCol_TitleBgActive = 11
ImGuiCol_TitleBgCollapsed = 12
ImGuiCol_MenuBarBg = 13
ImGuiCol_ScrollbarBg = 14
ImGuiCol_ScrollbarGrab = 15
ImGuiCol_ScrollbarGrabHovered = 16
ImGuiCol_ScrollbarGrabActive = 17
ImGuiCol_CheckMark = 18
ImGuiCol_SliderGrab = 19
ImGuiCol_SliderGrabActive = 20
ImGuiCol_Button = 21
ImGuiCol_ButtonHovered = 22
ImGuiCol_ButtonActive = 23
ImGuiCol_Header = 24
ImGuiCol_HeaderHovered = 25
ImGuiCol_HeaderActive = 26
ImGuiCol_Separator = 27
ImGuiCol_SeparatorHovered = 28
ImGuiCol_SeparatorActive = 29
ImGuiCol_ResizeGrip = 30
ImGuiCol_ResizeGripHovered = 31
ImGuiCol_ResizeGripActive = 32
ImGuiCol_Tab = 33
ImGuiCol_TabHovered = 34
ImGuiCol_TabActive = 35
ImGuiCol_TabUnfocused = 36
ImGuiCol_TabUnfocusedActive = 37
ImGuiCol_PlotLines = 38
ImGuiCol_PlotLinesHovered = 39
ImGuiCol_PlotHistogram = 40
ImGuiCol_PlotHistogramHovered = 41
ImGuiCol_TableHeaderBg = 42
ImGuiCol_TableBorderStrong = 43
ImGuiCol_TableBorderLight = 44
ImGuiCol_TableRowBg = 45
ImGuiCol_TableRowBgAlt = 46
ImGuiCol_TextSelectedBg = 47
ImGuiCol_DragDropTarget = 48
ImGuiCol_NavHighlight = 49
ImGuiCol_NavWindowingHighlight = 50
ImGuiCol_NavWindowingDimBg = 51
ImGuiCol_ModalWindowDimBg = 52
ImGuiCol_COUNT = 53

# ImGuiColorEditFlags_
ImGuiColorEditFlags_None = 0
ImGuiColorEditFlags_NoAlpha = 2
ImGuiColorEditFlags_NoPicker = 4
ImGuiColorEditFlags_NoOptions = 8
ImGuiColorEditFlags_NoSmallPreview = 16
ImGuiColorEditFlags_NoInputs = 32
ImGuiColorEditFlags_NoTooltip = 64
ImGuiColorEditFlags_NoLabel = 128
ImGuiColorEditFlags_NoSidePreview = 256
ImGuiColorEditFlags_NoDragDrop = 512
ImGuiColorEditFlags_NoBorder = 1024
ImGuiColorEditFlags_AlphaBar = 65536
ImGuiColorEditFlags_AlphaPreview = 131072
ImGuiColorEditFlags_AlphaPreviewHalf = 262144
ImGuiColorEditFlags_HDR = 524288
ImGuiColorEditFlags_DisplayRGB = 1048576
ImGuiColorEditFlags_DisplayHSV = 2097152
ImGuiColorEditFlags_DisplayHex = 4194304
ImGuiColorEditFlags_Uint8 = 8388608
ImGuiColorEditFlags_Float = 16777216
ImGuiColorEditFlags_PickerHueBar = 33554432
ImGuiColorEditFlags_PickerHueWheel = 67108864
ImGuiColorEditFlags_InputRGB = 134217728
ImGuiColorEditFlags_InputHSV = 268435456
ImGuiColorEditFlags_DefaultOptions_ = 177209344
ImGuiColorEditFlags_DisplayMask_ = 7340032
ImGuiColorEditFlags_DataTypeMask_ = 25165824
ImGuiColorEditFlags_PickerMask_ = 100663296
ImGuiColorEditFlags_InputMask_ = 402653184

# ImGuiComboFlagsPrivate_
ImGuiComboFlags_CustomPreview = 1048576

# ImGuiComboFlags_
ImGuiComboFlags_None = 0
ImGuiComboFlags_PopupAlignLeft = 1
ImGuiComboFlags_HeightSmall = 2
ImGuiComboFlags_HeightRegular = 4
ImGuiComboFlags_HeightLarge = 8
ImGuiComboFlags_HeightLargest = 16
ImGuiComboFlags_NoArrowButton = 32
ImGuiComboFlags_NoPreview = 64
ImGuiComboFlags_HeightMask_ = 30

# ImGuiCond_
ImGuiCond_None = 0
ImGuiCond_Always = 1
ImGuiCond_Once = 2
ImGuiCond_FirstUseEver = 4
ImGuiCond_Appearing = 8

# ImGuiConfigFlags_
ImGuiConfigFlags_None = 0
ImGuiConfigFlags_NavEnableKeyboard = 1
ImGuiConfigFlags_NavEnableGamepad = 2
ImGuiConfigFlags_NavEnableSetMousePos = 4
ImGuiConfigFlags_NavNoCaptureKeyboard = 8
ImGuiConfigFlags_NoMouse = 16
ImGuiConfigFlags_NoMouseCursorChange = 32
ImGuiConfigFlags_IsSRGB = 1048576
ImGuiConfigFlags_IsTouchScreen = 2097152

# ImGuiContextHookType
ImGuiContextHookType_NewFramePre = 0
ImGuiContextHookType_NewFramePost = 1
ImGuiContextHookType_EndFramePre = 2
ImGuiContextHookType_EndFramePost = 3
ImGuiContextHookType_RenderPre = 4
ImGuiContextHookType_RenderPost = 5
ImGuiContextHookType_Shutdown = 6
ImGuiContextHookType_PendingRemoval_ = 7

# ImGuiDataTypePrivate_
ImGuiDataType_String = 11
ImGuiDataType_Pointer = 12
ImGuiDataType_ID = 13

# ImGuiDataType_
ImGuiDataType_S8 = 0
ImGuiDataType_U8 = 1
ImGuiDataType_S16 = 2
ImGuiDataType_U16 = 3
ImGuiDataType_S32 = 4
ImGuiDataType_U32 = 5
ImGuiDataType_S64 = 6
ImGuiDataType_U64 = 7
ImGuiDataType_Float = 8
ImGuiDataType_Double = 9
ImGuiDataType_COUNT = 10

# ImGuiDebugLogFlags_
ImGuiDebugLogFlags_None = 0
ImGuiDebugLogFlags_EventActiveId = 1
ImGuiDebugLogFlags_EventFocus = 2
ImGuiDebugLogFlags_EventPopup = 4
ImGuiDebugLogFlags_EventNav = 8
ImGuiDebugLogFlags_EventClipper = 16
ImGuiDebugLogFlags_EventSelection = 32
ImGuiDebugLogFlags_EventIO = 64
ImGuiDebugLogFlags_EventMask_ = 127
ImGuiDebugLogFlags_OutputToTTY = 1024

# ImGuiDir_
ImGuiDir_None = -1
ImGuiDir_Left = 0
ImGuiDir_Right = 1
ImGuiDir_Up = 2
ImGuiDir_Down = 3
ImGuiDir_COUNT = 4

# ImGuiDragDropFlags_
ImGuiDragDropFlags_None = 0
ImGuiDragDropFlags_SourceNoPreviewTooltip = 1
ImGuiDragDropFlags_SourceNoDisableHover = 2
ImGuiDragDropFlags_SourceNoHoldToOpenOthers = 4
ImGuiDragDropFlags_SourceAllowNullID = 8
ImGuiDragDropFlags_SourceExtern = 16
ImGuiDragDropFlags_SourceAutoExpirePayload = 32
ImGuiDragDropFlags_AcceptBeforeDelivery = 1024
ImGuiDragDropFlags_AcceptNoDrawDefaultRect = 2048
ImGuiDragDropFlags_AcceptNoPreviewTooltip = 4096
ImGuiDragDropFlags_AcceptPeekOnly = 3072

# ImGuiFocusRequestFlags_
ImGuiFocusRequestFlags_None = 0
ImGuiFocusRequestFlags_RestoreFocusedChild = 1
ImGuiFocusRequestFlags_UnlessBelowModal = 2

# ImGuiFocusedFlags_
ImGuiFocusedFlags_None = 0
ImGuiFocusedFlags_ChildWindows = 1
ImGuiFocusedFlags_RootWindow = 2
ImGuiFocusedFlags_AnyWindow = 4
ImGuiFocusedFlags_NoPopupHierarchy = 8
ImGuiFocusedFlags_RootAndChildWindows = 3

# ImGuiHoveredFlagsPrivate_
ImGuiHoveredFlags_DelayMask_ = 245760
ImGuiHoveredFlags_AllowedMaskForIsWindowHovered = 12463
ImGuiHoveredFlags_AllowedMaskForIsItemHovered = 262048

# ImGuiHoveredFlags_
ImGuiHoveredFlags_None = 0
ImGuiHoveredFlags_ChildWindows = 1
ImGuiHoveredFlags_RootWindow = 2
ImGuiHoveredFlags_AnyWindow = 4
ImGuiHoveredFlags_NoPopupHierarchy = 8
ImGuiHoveredFlags_AllowWhenBlockedByPopup = 32
ImGuiHoveredFlags_AllowWhenBlockedByActiveItem = 128
ImGuiHoveredFlags_AllowWhenOverlappedByItem = 256
ImGuiHoveredFlags_AllowWhenOverlappedByWindow = 512
ImGuiHoveredFlags_AllowWhenDisabled = 1024
ImGuiHoveredFlags_NoNavOverride = 2048
ImGuiHoveredFlags_AllowWhenOverlapped = 768
ImGuiHoveredFlags_RectOnly = 928
ImGuiHoveredFlags_RootAndChildWindows = 3
ImGuiHoveredFlags_ForTooltip = 4096
ImGuiHoveredFlags_Stationary = 8192
ImGuiHoveredFlags_DelayNone = 16384
ImGuiHoveredFlags_DelayShort = 32768
ImGuiHoveredFlags_DelayNormal = 65536
ImGuiHoveredFlags_NoSharedDelay = 131072

# ImGuiInputEventType
ImGuiInputEventType_None = 0
ImGuiInputEventType_MousePos = 1
ImGuiInputEventType_MouseWheel = 2
ImGuiInputEventType_MouseButton = 3
ImGuiInputEventType_Key = 4
ImGuiInputEventType_Text = 5
ImGuiInputEventType_Focus = 6
ImGuiInputEventType_COUNT = 7

# ImGuiInputFlags_
ImGuiInputFlags_None = 0
ImGuiInputFlags_Repeat = 1
ImGuiInputFlags_RepeatRateDefault = 2
ImGuiInputFlags_RepeatRateNavMove = 4
ImGuiInputFlags_RepeatRateNavTweak = 8
ImGuiInputFlags_RepeatRateMask_ = 14
ImGuiInputFlags_CondHovered = 16
ImGuiInputFlags_CondActive = 32
ImGuiInputFlags_CondDefault_ = 48
ImGuiInputFlags_CondMask_ = 48
ImGuiInputFlags_LockThisFrame = 64
ImGuiInputFlags_LockUntilRelease = 128
ImGuiInputFlags_RouteFocused = 256
ImGuiInputFlags_RouteGlobalLow = 512
ImGuiInputFlags_RouteGlobal = 1024
ImGuiInputFlags_RouteGlobalHigh = 2048
ImGuiInputFlags_RouteMask_ = 3840
ImGuiInputFlags_RouteAlways = 4096
ImGuiInputFlags_RouteUnlessBgFocused = 8192
ImGuiInputFlags_RouteExtraMask_ = 12288
ImGuiInputFlags_SupportedByIsKeyPressed = 15
ImGuiInputFlags_SupportedByShortcut = 16143
ImGuiInputFlags_SupportedBySetKeyOwner = 192
ImGuiInputFlags_SupportedBySetItemKeyOwner = 240

# ImGuiInputSource
ImGuiInputSource_None = 0
ImGuiInputSource_Mouse = 1
ImGuiInputSource_Keyboard = 2
ImGuiInputSource_Gamepad = 3
ImGuiInputSource_Clipboard = 4
ImGuiInputSource_COUNT = 5

# ImGuiInputTextFlagsPrivate_
ImGuiInputTextFlags_Multiline = 67108864
ImGuiInputTextFlags_NoMarkEdited = 134217728
ImGuiInputTextFlags_MergedItem = 268435456

# ImGuiInputTextFlags_
ImGuiInputTextFlags_None = 0
ImGuiInputTextFlags_CharsDecimal = 1
ImGuiInputTextFlags_CharsHexadecimal = 2
ImGuiInputTextFlags_CharsUppercase = 4
ImGuiInputTextFlags_CharsNoBlank = 8
ImGuiInputTextFlags_AutoSelectAll = 16
ImGuiInputTextFlags_EnterReturnsTrue = 32
ImGuiInputTextFlags_CallbackCompletion = 64
ImGuiInputTextFlags_CallbackHistory = 128
ImGuiInputTextFlags_CallbackAlways = 256
ImGuiInputTextFlags_CallbackCharFilter = 512
ImGuiInputTextFlags_AllowTabInput = 1024
ImGuiInputTextFlags_CtrlEnterForNewLine = 2048
ImGuiInputTextFlags_NoHorizontalScroll = 4096
ImGuiInputTextFlags_AlwaysOverwrite = 8192
ImGuiInputTextFlags_ReadOnly = 16384
ImGuiInputTextFlags_Password = 32768
ImGuiInputTextFlags_NoUndoRedo = 65536
ImGuiInputTextFlags_CharsScientific = 131072
ImGuiInputTextFlags_CallbackResize = 262144
ImGuiInputTextFlags_CallbackEdit = 524288
ImGuiInputTextFlags_EscapeClearsAll = 1048576

# ImGuiItemFlags_
ImGuiItemFlags_None = 0
ImGuiItemFlags_NoTabStop = 1
ImGuiItemFlags_ButtonRepeat = 2
ImGuiItemFlags_Disabled = 4
ImGuiItemFlags_NoNav = 8
ImGuiItemFlags_NoNavDefaultFocus = 16
ImGuiItemFlags_SelectableDontClosePopup = 32
ImGuiItemFlags_MixedValue = 64
ImGuiItemFlags_ReadOnly = 128
ImGuiItemFlags_NoWindowHoverableCheck = 256
ImGuiItemFlags_AllowOverlap = 512
ImGuiItemFlags_Inputable = 1024

# ImGuiItemStatusFlags_
ImGuiItemStatusFlags_None = 0
ImGuiItemStatusFlags_HoveredRect = 1
ImGuiItemStatusFlags_HasDisplayRect = 2
ImGuiItemStatusFlags_Edited = 4
ImGuiItemStatusFlags_ToggledSelection = 8
ImGuiItemStatusFlags_ToggledOpen = 16
ImGuiItemStatusFlags_HasDeactivated = 32
ImGuiItemStatusFlags_Deactivated = 64
ImGuiItemStatusFlags_HoveredWindow = 128
ImGuiItemStatusFlags_FocusedByTabbing = 256
ImGuiItemStatusFlags_Visible = 512

# ImGuiKey
ImGuiKey_None = 0
ImGuiKey_Tab = 512
ImGuiKey_LeftArrow = 513
ImGuiKey_RightArrow = 514
ImGuiKey_UpArrow = 515
ImGuiKey_DownArrow = 516
ImGuiKey_PageUp = 517
ImGuiKey_PageDown = 518
ImGuiKey_Home = 519
ImGuiKey_End = 520
ImGuiKey_Insert = 521
ImGuiKey_Delete = 522
ImGuiKey_Backspace = 523
ImGuiKey_Space = 524
ImGuiKey_Enter = 525
ImGuiKey_Escape = 526
ImGuiKey_LeftCtrl = 527
ImGuiKey_LeftShift = 528
ImGuiKey_LeftAlt = 529
ImGuiKey_LeftSuper = 530
ImGuiKey_RightCtrl = 531
ImGuiKey_RightShift = 532
ImGuiKey_RightAlt = 533
ImGuiKey_RightSuper = 534
ImGuiKey_Menu = 535
ImGuiKey_0 = 536
ImGuiKey_1 = 537
ImGuiKey_2 = 538
ImGuiKey_3 = 539
ImGuiKey_4 = 540
ImGuiKey_5 = 541
ImGuiKey_6 = 542
ImGuiKey_7 = 543
ImGuiKey_8 = 544
ImGuiKey_9 = 545
ImGuiKey_A = 546
ImGuiKey_B = 547
ImGuiKey_C = 548
ImGuiKey_D = 549
ImGuiKey_E = 550
ImGuiKey_F = 551
ImGuiKey_G = 552
ImGuiKey_H = 553
ImGuiKey_I = 554
ImGuiKey_J = 555
ImGuiKey_K = 556
ImGuiKey_L = 557
ImGuiKey_M = 558
ImGuiKey_N = 559
ImGuiKey_O = 560
ImGuiKey_P = 561
ImGuiKey_Q = 562
ImGuiKey_R = 563
ImGuiKey_S = 564
ImGuiKey_T = 565
ImGuiKey_U = 566
ImGuiKey_V = 567
ImGuiKey_W = 568
ImGuiKey_X = 569
ImGuiKey_Y = 570
ImGuiKey_Z = 571
ImGuiKey_F1 = 572
ImGuiKey_F2 = 573
ImGuiKey_F3 = 574
ImGuiKey_F4 = 575
ImGuiKey_F5 = 576
ImGuiKey_F6 = 577
ImGuiKey_F7 = 578
ImGuiKey_F8 = 579
ImGuiKey_F9 = 580
ImGuiKey_F10 = 581
ImGuiKey_F11 = 582
ImGuiKey_F12 = 583
ImGuiKey_Apostrophe = 584
ImGuiKey_Comma = 585
ImGuiKey_Minus = 586
ImGuiKey_Period = 587
ImGuiKey_Slash = 588
ImGuiKey_Semicolon = 589
ImGuiKey_Equal = 590
ImGuiKey_LeftBracket = 591
ImGuiKey_Backslash = 592
ImGuiKey_RightBracket = 593
ImGuiKey_GraveAccent = 594
ImGuiKey_CapsLock = 595
ImGuiKey_ScrollLock = 596
ImGuiKey_NumLock = 597
ImGuiKey_PrintScreen = 598
ImGuiKey_Pause = 599
ImGuiKey_Keypad0 = 600
ImGuiKey_Keypad1 = 601
ImGuiKey_Keypad2 = 602
ImGuiKey_Keypad3 = 603
ImGuiKey_Keypad4 = 604
ImGuiKey_Keypad5 = 605
ImGuiKey_Keypad6 = 606
ImGuiKey_Keypad7 = 607
ImGuiKey_Keypad8 = 608
ImGuiKey_Keypad9 = 609
ImGuiKey_KeypadDecimal = 610
ImGuiKey_KeypadDivide = 611
ImGuiKey_KeypadMultiply = 612
ImGuiKey_KeypadSubtract = 613
ImGuiKey_KeypadAdd = 614
ImGuiKey_KeypadEnter = 615
ImGuiKey_KeypadEqual = 616
ImGuiKey_GamepadStart = 617
ImGuiKey_GamepadBack = 618
ImGuiKey_GamepadFaceLeft = 619
ImGuiKey_GamepadFaceRight = 620
ImGuiKey_GamepadFaceUp = 621
ImGuiKey_GamepadFaceDown = 622
ImGuiKey_GamepadDpadLeft = 623
ImGuiKey_GamepadDpadRight = 624
ImGuiKey_GamepadDpadUp = 625
ImGuiKey_GamepadDpadDown = 626
ImGuiKey_GamepadL1 = 627
ImGuiKey_GamepadR1 = 628
ImGuiKey_GamepadL2 = 629
ImGuiKey_GamepadR2 = 630
ImGuiKey_GamepadL3 = 631
ImGuiKey_GamepadR3 = 632
ImGuiKey_GamepadLStickLeft = 633
ImGuiKey_GamepadLStickRight = 634
ImGuiKey_GamepadLStickUp = 635
ImGuiKey_GamepadLStickDown = 636
ImGuiKey_GamepadRStickLeft = 637
ImGuiKey_GamepadRStickRight = 638
ImGuiKey_GamepadRStickUp = 639
ImGuiKey_GamepadRStickDown = 640
ImGuiKey_MouseLeft = 641
ImGuiKey_MouseRight = 642
ImGuiKey_MouseMiddle = 643
ImGuiKey_MouseX1 = 644
ImGuiKey_MouseX2 = 645
ImGuiKey_MouseWheelX = 646
ImGuiKey_MouseWheelY = 647
ImGuiKey_ReservedForModCtrl = 648
ImGuiKey_ReservedForModShift = 649
ImGuiKey_ReservedForModAlt = 650
ImGuiKey_ReservedForModSuper = 651
ImGuiKey_COUNT = 652
ImGuiMod_None = 0
ImGuiMod_Ctrl = 4096
ImGuiMod_Shift = 8192
ImGuiMod_Alt = 16384
ImGuiMod_Super = 32768
ImGuiMod_Shortcut = 2048
ImGuiMod_Mask_ = 63488
ImGuiKey_NamedKey_BEGIN = 512
ImGuiKey_NamedKey_END = 652
ImGuiKey_NamedKey_COUNT = 140
ImGuiKey_KeysData_SIZE = 652
ImGuiKey_KeysData_OFFSET = 0

# ImGuiLayoutType_
ImGuiLayoutType_Horizontal = 0
ImGuiLayoutType_Vertical = 1

# ImGuiLocKey
ImGuiLocKey_VersionStr = 0
ImGuiLocKey_TableSizeOne = 1
ImGuiLocKey_TableSizeAllFit = 2
ImGuiLocKey_TableSizeAllDefault = 3
ImGuiLocKey_TableResetOrder = 4
ImGuiLocKey_WindowingMainMenuBar = 5
ImGuiLocKey_WindowingPopup = 6
ImGuiLocKey_WindowingUntitled = 7
ImGuiLocKey_COUNT = 8

# ImGuiLogType
ImGuiLogType_None = 0
ImGuiLogType_TTY = 1
ImGuiLogType_File = 2
ImGuiLogType_Buffer = 3
ImGuiLogType_Clipboard = 4

# ImGuiMouseButton_
ImGuiMouseButton_Left = 0
ImGuiMouseButton_Right = 1
ImGuiMouseButton_Middle = 2
ImGuiMouseButton_COUNT = 5

# ImGuiMouseCursor_
ImGuiMouseCursor_None = -1
ImGuiMouseCursor_Arrow = 0
ImGuiMouseCursor_TextInput = 1
ImGuiMouseCursor_ResizeAll = 2
ImGuiMouseCursor_ResizeNS = 3
ImGuiMouseCursor_ResizeEW = 4
ImGuiMouseCursor_ResizeNESW = 5
ImGuiMouseCursor_ResizeNWSE = 6
ImGuiMouseCursor_Hand = 7
ImGuiMouseCursor_NotAllowed = 8
ImGuiMouseCursor_COUNT = 9

# ImGuiMouseSource
ImGuiMouseSource_Mouse = 0
ImGuiMouseSource_TouchScreen = 1
ImGuiMouseSource_Pen = 2
ImGuiMouseSource_COUNT = 3

# ImGuiNavHighlightFlags_
ImGuiNavHighlightFlags_None = 0
ImGuiNavHighlightFlags_TypeDefault = 1
ImGuiNavHighlightFlags_TypeThin = 2
ImGuiNavHighlightFlags_AlwaysDraw = 4
ImGuiNavHighlightFlags_NoRounding = 8

# ImGuiNavInput
ImGuiNavInput_Activate = 0
ImGuiNavInput_Cancel = 1
ImGuiNavInput_Input = 2
ImGuiNavInput_Menu = 3
ImGuiNavInput_DpadLeft = 4
ImGuiNavInput_DpadRight = 5
ImGuiNavInput_DpadUp = 6
ImGuiNavInput_DpadDown = 7
ImGuiNavInput_LStickLeft = 8
ImGuiNavInput_LStickRight = 9
ImGuiNavInput_LStickUp = 10
ImGuiNavInput_LStickDown = 11
ImGuiNavInput_FocusPrev = 12
ImGuiNavInput_FocusNext = 13
ImGuiNavInput_TweakSlow = 14
ImGuiNavInput_TweakFast = 15
ImGuiNavInput_COUNT = 16

# ImGuiNavLayer
ImGuiNavLayer_Main = 0
ImGuiNavLayer_Menu = 1
ImGuiNavLayer_COUNT = 2

# ImGuiNavMoveFlags_
ImGuiNavMoveFlags_None = 0
ImGuiNavMoveFlags_LoopX = 1
ImGuiNavMoveFlags_LoopY = 2
ImGuiNavMoveFlags_WrapX = 4
ImGuiNavMoveFlags_WrapY = 8
ImGuiNavMoveFlags_WrapMask_ = 15
ImGuiNavMoveFlags_AllowCurrentNavId = 16
ImGuiNavMoveFlags_AlsoScoreVisibleSet = 32
ImGuiNavMoveFlags_ScrollToEdgeY = 64
ImGuiNavMoveFlags_Forwarded = 128
ImGuiNavMoveFlags_DebugNoResult = 256
ImGuiNavMoveFlags_FocusApi = 512
ImGuiNavMoveFlags_IsTabbing = 1024
ImGuiNavMoveFlags_IsPageMove = 2048
ImGuiNavMoveFlags_Activate = 4096
ImGuiNavMoveFlags_NoSelect = 8192
ImGuiNavMoveFlags_NoSetNavHighlight = 16384

# ImGuiNextItemDataFlags_
ImGuiNextItemDataFlags_None = 0
ImGuiNextItemDataFlags_HasWidth = 1
ImGuiNextItemDataFlags_HasOpen = 2

# ImGuiNextWindowDataFlags_
ImGuiNextWindowDataFlags_None = 0
ImGuiNextWindowDataFlags_HasPos = 1
ImGuiNextWindowDataFlags_HasSize = 2
ImGuiNextWindowDataFlags_HasContentSize = 4
ImGuiNextWindowDataFlags_HasCollapsed = 8
ImGuiNextWindowDataFlags_HasSizeConstraint = 16
ImGuiNextWindowDataFlags_HasFocus = 32
ImGuiNextWindowDataFlags_HasBgAlpha = 64
ImGuiNextWindowDataFlags_HasScroll = 128

# ImGuiOldColumnFlags_
ImGuiOldColumnFlags_None = 0
ImGuiOldColumnFlags_NoBorder = 1
ImGuiOldColumnFlags_NoResize = 2
ImGuiOldColumnFlags_NoPreserveWidths = 4
ImGuiOldColumnFlags_NoForceWithinWindow = 8
ImGuiOldColumnFlags_GrowParentContentsSize = 16

# ImGuiPlotType
ImGuiPlotType_Lines = 0
ImGuiPlotType_Histogram = 1

# ImGuiPopupFlags_
ImGuiPopupFlags_None = 0
ImGuiPopupFlags_MouseButtonLeft = 0
ImGuiPopupFlags_MouseButtonRight = 1
ImGuiPopupFlags_MouseButtonMiddle = 2
ImGuiPopupFlags_MouseButtonMask_ = 31
ImGuiPopupFlags_MouseButtonDefault_ = 1
ImGuiPopupFlags_NoOpenOverExistingPopup = 32
ImGuiPopupFlags_NoOpenOverItems = 64
ImGuiPopupFlags_AnyPopupId = 128
ImGuiPopupFlags_AnyPopupLevel = 256
ImGuiPopupFlags_AnyPopup = 384

# ImGuiPopupPositionPolicy
ImGuiPopupPositionPolicy_Default = 0
ImGuiPopupPositionPolicy_ComboBox = 1
ImGuiPopupPositionPolicy_Tooltip = 2

# ImGuiScrollFlags_
ImGuiScrollFlags_None = 0
ImGuiScrollFlags_KeepVisibleEdgeX = 1
ImGuiScrollFlags_KeepVisibleEdgeY = 2
ImGuiScrollFlags_KeepVisibleCenterX = 4
ImGuiScrollFlags_KeepVisibleCenterY = 8
ImGuiScrollFlags_AlwaysCenterX = 16
ImGuiScrollFlags_AlwaysCenterY = 32
ImGuiScrollFlags_NoScrollParent = 64
ImGuiScrollFlags_MaskX_ = 21
ImGuiScrollFlags_MaskY_ = 42

# ImGuiSelectableFlagsPrivate_
ImGuiSelectableFlags_NoHoldingActiveID = 1048576
ImGuiSelectableFlags_SelectOnNav = 2097152
ImGuiSelectableFlags_SelectOnClick = 4194304
ImGuiSelectableFlags_SelectOnRelease = 8388608
ImGuiSelectableFlags_SpanAvailWidth = 16777216
ImGuiSelectableFlags_SetNavIdOnHover = 33554432
ImGuiSelectableFlags_NoPadWithHalfSpacing = 67108864
ImGuiSelectableFlags_NoSetKeyOwner = 134217728

# ImGuiSelectableFlags_
ImGuiSelectableFlags_None = 0
ImGuiSelectableFlags_DontClosePopups = 1
ImGuiSelectableFlags_SpanAllColumns = 2
ImGuiSelectableFlags_AllowDoubleClick = 4
ImGuiSelectableFlags_Disabled = 8
ImGuiSelectableFlags_AllowOverlap = 16

# ImGuiSeparatorFlags_
ImGuiSeparatorFlags_None = 0
ImGuiSeparatorFlags_Horizontal = 1
ImGuiSeparatorFlags_Vertical = 2
ImGuiSeparatorFlags_SpanAllColumns = 4

# ImGuiSliderFlagsPrivate_
ImGuiSliderFlags_Vertical = 1048576
ImGuiSliderFlags_ReadOnly = 2097152

# ImGuiSliderFlags_
ImGuiSliderFlags_None = 0
ImGuiSliderFlags_AlwaysClamp = 16
ImGuiSliderFlags_Logarithmic = 32
ImGuiSliderFlags_NoRoundToFormat = 64
ImGuiSliderFlags_NoInput = 128

# ImGuiSortDirection_
ImGuiSortDirection_None = 0
ImGuiSortDirection_Ascending = 1
ImGuiSortDirection_Descending = 2

# ImGuiStyleVar_
ImGuiStyleVar_Alpha = 0
ImGuiStyleVar_DisabledAlpha = 1
ImGuiStyleVar_WindowPadding = 2
ImGuiStyleVar_WindowRounding = 3
ImGuiStyleVar_WindowBorderSize = 4
ImGuiStyleVar_WindowMinSize = 5
ImGuiStyleVar_WindowTitleAlign = 6
ImGuiStyleVar_ChildRounding = 7
ImGuiStyleVar_ChildBorderSize = 8
ImGuiStyleVar_PopupRounding = 9
ImGuiStyleVar_PopupBorderSize = 10
ImGuiStyleVar_FramePadding = 11
ImGuiStyleVar_FrameRounding = 12
ImGuiStyleVar_FrameBorderSize = 13
ImGuiStyleVar_ItemSpacing = 14
ImGuiStyleVar_ItemInnerSpacing = 15
ImGuiStyleVar_IndentSpacing = 16
ImGuiStyleVar_CellPadding = 17
ImGuiStyleVar_ScrollbarSize = 18
ImGuiStyleVar_ScrollbarRounding = 19
ImGuiStyleVar_GrabMinSize = 20
ImGuiStyleVar_GrabRounding = 21
ImGuiStyleVar_TabRounding = 22
ImGuiStyleVar_ButtonTextAlign = 23
ImGuiStyleVar_SelectableTextAlign = 24
ImGuiStyleVar_SeparatorTextBorderSize = 25
ImGuiStyleVar_SeparatorTextAlign = 26
ImGuiStyleVar_SeparatorTextPadding = 27
ImGuiStyleVar_COUNT = 28

# ImGuiTabBarFlagsPrivate_
ImGuiTabBarFlags_DockNode = 1048576
ImGuiTabBarFlags_IsFocused = 2097152
ImGuiTabBarFlags_SaveSettings = 4194304

# ImGuiTabBarFlags_
ImGuiTabBarFlags_None = 0
ImGuiTabBarFlags_Reorderable = 1
ImGuiTabBarFlags_AutoSelectNewTabs = 2
ImGuiTabBarFlags_TabListPopupButton = 4
ImGuiTabBarFlags_NoCloseWithMiddleMouseButton = 8
ImGuiTabBarFlags_NoTabListScrollingButtons = 16
ImGuiTabBarFlags_NoTooltip = 32
ImGuiTabBarFlags_FittingPolicyResizeDown = 64
ImGuiTabBarFlags_FittingPolicyScroll = 128
ImGuiTabBarFlags_FittingPolicyMask_ = 192
ImGuiTabBarFlags_FittingPolicyDefault_ = 64

# ImGuiTabItemFlagsPrivate_
ImGuiTabItemFlags_SectionMask_ = 192
ImGuiTabItemFlags_NoCloseButton = 1048576
ImGuiTabItemFlags_Button = 2097152

# ImGuiTabItemFlags_
ImGuiTabItemFlags_None = 0
ImGuiTabItemFlags_UnsavedDocument = 1
ImGuiTabItemFlags_SetSelected = 2
ImGuiTabItemFlags_NoCloseWithMiddleMouseButton = 4
ImGuiTabItemFlags_NoPushId = 8
ImGuiTabItemFlags_NoTooltip = 16
ImGuiTabItemFlags_NoReorder = 32
ImGuiTabItemFlags_Leading = 64
ImGuiTabItemFlags_Trailing = 128

# ImGuiTableBgTarget_
ImGuiTableBgTarget_None = 0
ImGuiTableBgTarget_RowBg0 = 1
ImGuiTableBgTarget_RowBg1 = 2
ImGuiTableBgTarget_CellBg = 3

# ImGuiTableColumnFlags_
ImGuiTableColumnFlags_None = 0
ImGuiTableColumnFlags_Disabled = 1
ImGuiTableColumnFlags_DefaultHide = 2
ImGuiTableColumnFlags_DefaultSort = 4
ImGuiTableColumnFlags_WidthStretch = 8
ImGuiTableColumnFlags_WidthFixed = 16
ImGuiTableColumnFlags_NoResize = 32
ImGuiTableColumnFlags_NoReorder = 64
ImGuiTableColumnFlags_NoHide = 128
ImGuiTableColumnFlags_NoClip = 256
ImGuiTableColumnFlags_NoSort = 512
ImGuiTableColumnFlags_NoSortAscending = 1024
ImGuiTableColumnFlags_NoSortDescending = 2048
ImGuiTableColumnFlags_NoHeaderLabel = 4096
ImGuiTableColumnFlags_NoHeaderWidth = 8192
ImGuiTableColumnFlags_PreferSortAscending = 16384
ImGuiTableColumnFlags_PreferSortDescending = 32768
ImGuiTableColumnFlags_IndentEnable = 65536
ImGuiTableColumnFlags_IndentDisable = 131072
ImGuiTableColumnFlags_IsEnabled = 16777216
ImGuiTableColumnFlags_IsVisible = 33554432
ImGuiTableColumnFlags_IsSorted = 67108864
ImGuiTableColumnFlags_IsHovered = 134217728
ImGuiTableColumnFlags_WidthMask_ = 24
ImGuiTableColumnFlags_IndentMask_ = 196608
ImGuiTableColumnFlags_StatusMask_ = 251658240

# ImGuiTableFlags_
ImGuiTableFlags_None = 0
ImGuiTableFlags_Resizable = 1
ImGuiTableFlags_Reorderable = 2
ImGuiTableFlags_Hideable = 4
ImGuiTableFlags_Sortable = 8
ImGuiTableFlags_NoSavedSettings = 16
ImGuiTableFlags_ContextMenuInBody = 32
ImGuiTableFlags_RowBg = 64
ImGuiTableFlags_BordersInnerH = 128
ImGuiTableFlags_BordersOuterH = 256
ImGuiTableFlags_BordersInnerV = 512
ImGuiTableFlags_BordersOuterV = 1024
ImGuiTableFlags_BordersH = 384
ImGuiTableFlags_BordersV = 1536
ImGuiTableFlags_BordersInner = 640
ImGuiTableFlags_BordersOuter = 1280
ImGuiTableFlags_Borders = 1920
ImGuiTableFlags_NoBordersInBody = 2048
ImGuiTableFlags_NoBordersInBodyUntilResize = 4096
ImGuiTableFlags_SizingFixedFit = 8192
ImGuiTableFlags_SizingFixedSame = 16384
ImGuiTableFlags_SizingStretchProp = 24576
ImGuiTableFlags_SizingStretchSame = 32768
ImGuiTableFlags_NoHostExtendX = 65536
ImGuiTableFlags_NoHostExtendY = 131072
ImGuiTableFlags_NoKeepColumnsVisible = 262144
ImGuiTableFlags_PreciseWidths = 524288
ImGuiTableFlags_NoClip = 1048576
ImGuiTableFlags_PadOuterX = 2097152
ImGuiTableFlags_NoPadOuterX = 4194304
ImGuiTableFlags_NoPadInnerX = 8388608
ImGuiTableFlags_ScrollX = 16777216
ImGuiTableFlags_ScrollY = 33554432
ImGuiTableFlags_SortMulti = 67108864
ImGuiTableFlags_SortTristate = 134217728
ImGuiTableFlags_SizingMask_ = 57344

# ImGuiTableRowFlags_
ImGuiTableRowFlags_None = 0
ImGuiTableRowFlags_Headers = 1

# ImGuiTextFlags_
ImGuiTextFlags_None = 0
ImGuiTextFlags_NoWidthForLargeClippedText = 1

# ImGuiTooltipFlags_
ImGuiTooltipFlags_None = 0
ImGuiTooltipFlags_OverridePrevious = 2

# ImGuiTreeNodeFlagsPrivate_
ImGuiTreeNodeFlags_ClipLabelForTrailingButton = 1048576
ImGuiTreeNodeFlags_UpsideDownArrow = 2097152

# ImGuiTreeNodeFlags_
ImGuiTreeNodeFlags_None = 0
ImGuiTreeNodeFlags_Selected = 1
ImGuiTreeNodeFlags_Framed = 2
ImGuiTreeNodeFlags_AllowOverlap = 4
ImGuiTreeNodeFlags_NoTreePushOnOpen = 8
ImGuiTreeNodeFlags_NoAutoOpenOnLog = 16
ImGuiTreeNodeFlags_DefaultOpen = 32
ImGuiTreeNodeFlags_OpenOnDoubleClick = 64
ImGuiTreeNodeFlags_OpenOnArrow = 128
ImGuiTreeNodeFlags_Leaf = 256
ImGuiTreeNodeFlags_Bullet = 512
ImGuiTreeNodeFlags_FramePadding = 1024
ImGuiTreeNodeFlags_SpanAvailWidth = 2048
ImGuiTreeNodeFlags_SpanFullWidth = 4096
ImGuiTreeNodeFlags_NavLeftJumpsBackHere = 8192
ImGuiTreeNodeFlags_CollapsingHeader = 26

# ImGuiViewportFlags_
ImGuiViewportFlags_None = 0
ImGuiViewportFlags_IsPlatformWindow = 1
ImGuiViewportFlags_IsPlatformMonitor = 2
ImGuiViewportFlags_OwnedByApp = 4

# ImGuiWindowFlags_
ImGuiWindowFlags_None = 0
ImGuiWindowFlags_NoTitleBar = 1
ImGuiWindowFlags_NoResize = 2
ImGuiWindowFlags_NoMove = 4
ImGuiWindowFlags_NoScrollbar = 8
ImGuiWindowFlags_NoScrollWithMouse = 16
ImGuiWindowFlags_NoCollapse = 32
ImGuiWindowFlags_AlwaysAutoResize = 64
ImGuiWindowFlags_NoBackground = 128
ImGuiWindowFlags_NoSavedSettings = 256
ImGuiWindowFlags_NoMouseInputs = 512
ImGuiWindowFlags_MenuBar = 1024
ImGuiWindowFlags_HorizontalScrollbar = 2048
ImGuiWindowFlags_NoFocusOnAppearing = 4096
ImGuiWindowFlags_NoBringToFrontOnFocus = 8192
ImGuiWindowFlags_AlwaysVerticalScrollbar = 16384
ImGuiWindowFlags_AlwaysHorizontalScrollbar = 32768
ImGuiWindowFlags_AlwaysUseWindowPadding = 65536
ImGuiWindowFlags_NoNavInputs = 262144
ImGuiWindowFlags_NoNavFocus = 524288
ImGuiWindowFlags_UnsavedDocument = 1048576
ImGuiWindowFlags_NoNav = 786432
ImGuiWindowFlags_NoDecoration = 43
ImGuiWindowFlags_NoInputs = 786944
ImGuiWindowFlags_NavFlattened = 8388608
ImGuiWindowFlags_ChildWindow = 16777216
ImGuiWindowFlags_Tooltip = 33554432
ImGuiWindowFlags_Popup = 67108864
ImGuiWindowFlags_Modal = 134217728
ImGuiWindowFlags_ChildMenu = 268435456
'''

class Lines:
    def __init__(self):
        self.lines = []
        self.depth = 0
    def add(self, line):
        self.lines.append(' '*4*self.depth + line)
    def __str__(self):
        return '\n'.join(self.lines)
    def begin(self):
        self.depth += 1
    def end(self):
        self.depth -= 1
    def __len__(self):
        return len(self.lines)

def eat_spaces(s, pos):
    while pos < len(s) and (s[pos].isspace() or s[pos] == '\n'):
        pos += 1
    return pos

def match_string(s, pos):
    """eat a string, return the end position"""
    assert pos < len(s), f'out of range: {pos} >= {len(s)}'
    if s[pos] != '"':
        return None
    pos += 1
    start = pos
    while True:
        if s[pos] == '\\':
            pos += 2
        elif s[pos] == '"':
            pos += 1
            break
        else:
            pos += 1
    return pos, s[start:pos-1]

def eat_string(s, pos):
    pos = eat_spaces(s, pos)
    ret = match_string(s, pos)
    if ret is None:
        raise ValueError(f'expect a string, got {s[pos:pos+10]}')
    return ret

def eat_concat_string(s, pos) -> str:
    pos, string = eat_string(s, pos)
    while True:
        pos = eat_spaces(s, pos)
        ret = match_string(s, pos)
        if ret is None:
            break
        pos, s2 = ret
        string += s2
    return pos, string

with open('src/imguiw.cpp') as f:
    imguiw_cpp = f.read()

structs_pyi = '''class _IO:
    ConfigFlags: int                                            # int
    BackendFlags: int                                           # int
    DisplaySize: vec2                                           # struct ImVec2
    DeltaTime: float                                            # float
    IniSavingRate: float                                        # float
    IniFilename = ...                                           # const char*
    LogFilename = ...                                           # const char*
    UserData = ...                                              # void*
    Fonts = ...                                                 # ImFontAtlas*
    FontGlobalScale: float                                      # float
    FontAllowUserScaling: bool                                  # bool
    FontDefault = ...                                           # ImFont*
    DisplayFramebufferScale: vec2                               # struct ImVec2
    MouseDrawCursor: bool                                       # bool
    ConfigMacOSXBehaviors: bool                                 # bool
    ConfigInputTrickleEventQueue: bool                          # bool
    ConfigInputTextCursorBlink: bool                            # bool
    ConfigInputTextEnterKeepActive: bool                        # bool
    ConfigDragClickToInputText: bool                            # bool
    ConfigWindowsResizeFromEdges: bool                          # bool
    ConfigWindowsMoveFromTitleBarOnly: bool                     # bool
    ConfigMemoryCompactTimer: float                             # float
    MouseDoubleClickTime: float                                 # float
    MouseDoubleClickMaxDist: float                              # float
    MouseDragThreshold: float                                   # float
    KeyRepeatDelay: float                                       # float
    KeyRepeatRate: float                                        # float
    ConfigDebugBeginReturnValueOnce: bool                       # bool
    ConfigDebugBeginReturnValueLoop: bool                       # bool
    ConfigDebugIgnoreFocusLoss: bool                            # bool
    ConfigDebugIniSettings: bool                                # bool
    BackendPlatformName = ...                                   # const char*
    BackendRendererName = ...                                   # const char*
    BackendPlatformUserData = ...                               # void*
    BackendRendererUserData = ...                               # void*
    BackendLanguageUserData = ...                               # void*
    ClipboardUserData = ...                                     # void*
    PlatformLocaleDecimalPoint = ...                            # ImWchar16
    WantCaptureMouse: bool                                      # bool
    WantCaptureKeyboard: bool                                   # bool
    WantTextInput: bool                                         # bool
    WantSetMousePos: bool                                       # bool
    WantSaveIniSettings: bool                                   # bool
    NavActive: bool                                             # bool
    NavVisible: bool                                            # bool
    Framerate: float                                            # float
    MetricsRenderVertices: int                                  # int
    MetricsRenderIndices: int                                   # int
    MetricsRenderWindows: int                                   # int
    MetricsActiveWindows: int                                   # int
    MetricsActiveAllocations: int                               # int
    MouseDelta: vec2                                            # struct ImVec2
    Ctx = ...                                                   # ImGuiContext*
    MousePos: vec2                                              # struct ImVec2
    MouseWheel: float                                           # float
    MouseWheelH: float                                          # float
    MouseSource = ...                                           # ImGuiMouseSource
    KeyCtrl: bool                                               # bool
    KeyShift: bool                                              # bool
    KeyAlt: bool                                                # bool
    KeySuper: bool                                              # bool
    KeyMods: int                                                # int
    WantCaptureMouseUnlessPopupClose: bool                      # bool
    MousePosPrev: vec2                                          # struct ImVec2
    MouseWheelRequestAxisSwap: bool                             # bool
    PenPressure: float                                          # float
    AppFocusLost: bool                                          # bool
    AppAcceptingEvents: bool                                    # bool
    BackendUsingLegacyKeyArrays: int                            # signed char
    BackendUsingLegacyNavInputArray: bool                       # bool
    InputQueueSurrogate: int                                    # unsigned short

class _Style:
    Alpha: float                                                # float
    DisabledAlpha: float                                        # float
    WindowPadding: vec2                                         # struct ImVec2
    WindowRounding: float                                       # float
    WindowBorderSize: float                                     # float
    WindowMinSize: vec2                                         # struct ImVec2
    WindowTitleAlign: vec2                                      # struct ImVec2
    WindowMenuButtonPosition: int                               # int
    ChildRounding: float                                        # float
    ChildBorderSize: float                                      # float
    PopupRounding: float                                        # float
    PopupBorderSize: float                                      # float
    FramePadding: vec2                                          # struct ImVec2
    FrameRounding: float                                        # float
    FrameBorderSize: float                                      # float
    ItemSpacing: vec2                                           # struct ImVec2
    ItemInnerSpacing: vec2                                      # struct ImVec2
    CellPadding: vec2                                           # struct ImVec2
    TouchExtraPadding: vec2                                     # struct ImVec2
    IndentSpacing: float                                        # float
    ColumnsMinSpacing: float                                    # float
    ScrollbarSize: float                                        # float
    ScrollbarRounding: float                                    # float
    GrabMinSize: float                                          # float
    GrabRounding: float                                         # float
    LogSliderDeadzone: float                                    # float
    TabRounding: float                                          # float
    TabBorderSize: float                                        # float
    TabMinWidthForCloseButton: float                            # float
    ColorButtonPosition: int                                    # int
    ButtonTextAlign: vec2                                       # struct ImVec2
    SelectableTextAlign: vec2                                   # struct ImVec2
    SeparatorTextBorderSize: float                              # float
    SeparatorTextAlign: vec2                                    # struct ImVec2
    SeparatorTextPadding: vec2                                  # struct ImVec2
    DisplayWindowPadding: vec2                                  # struct ImVec2
    DisplaySafeAreaPadding: vec2                                # struct ImVec2
    MouseCursorScale: float                                     # float
    AntiAliasedLines: bool                                      # bool
    AntiAliasedLinesUseTex: bool                                # bool
    AntiAliasedFill: bool                                       # bool
    CurveTessellationTol: float                                 # float
    CircleTessellationMaxError: float                           # float
    HoverStationaryDelay: float                                 # float
    HoverDelayShort: float                                      # float
    HoverDelayNormal: float                                     # float
    HoverFlagsForTooltipMouse: int                              # int
    HoverFlagsForTooltipNav: int                                # int
'''

# remove all #include
imguiw_cpp = re.sub(r'#include.*\n', '', imguiw_cpp)
with open('tmp.cpp', 'wt') as f:
    f.write(imguiw_cpp)
# run cpp
import subprocess
imguiw_cpp = subprocess.check_output([
    'clang++', '-E', '-std=c++17', 'tmp.cpp']).decode('utf-8')
with open ('tmp.cpp', 'wt') as f:
    f.write(imguiw_cpp)

lines = Lines()
lines.add('from linalg import *')
lines.add('from c import *')
lines.add('from raylib import *')
lines.add('\n')

# enums
lines.add(enums_pyi)
# structs
lines.add(structs_pyi)

total_cnt = re.findall(r'vm->bind\(imgui, ', imguiw_cpp).__len__()

valid_cnt = 0
for m in re.finditer(r'vm->bind\(imgui, ', imguiw_cpp):
    pos = m.end()
    pos, sig = eat_concat_string(imguiw_cpp, pos)
    pos = eat_spaces(imguiw_cpp, pos)
    assert imguiw_cpp[pos] == ','
    pos += 1
    pos = eat_spaces(imguiw_cpp, pos)
    if imguiw_cpp[pos] == '"':
        pos, docstring = eat_concat_string(imguiw_cpp, pos)
    else:
        docstring = None

    valid_cnt += 1
    lines.add('def ' + sig + ':')
    lines.begin()
    if docstring:
        lines.add('"""' + docstring + '"""')
    else:
        lines.add('pass')
    lines.end()
    lines.add('')

assert total_cnt == valid_cnt, f'{total_cnt} != {valid_cnt}'
print(f'generated {valid_cnt} functions')

with open('builtins/typings/imgui.pyi', 'w') as f:
    f.write(str(lines))

os.remove('tmp.cpp')