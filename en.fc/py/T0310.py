from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0310   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0310.x',
        MapIndex            = 15,
        MapDefaultBGM       = "ed60088",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Cassius',                              # 9
        'Joshua',                               # 10
        'Estelle',                              # 11
        'Estelle',                              # 12
        'Boy',                                  # 13
        'Cassius',                              # 14
        'Dish',                                 # 15
        'Dish',                                 # 16
        'Dish',                                 # 17
        'Coffee',                               # 18
        'Coffee',                               # 19
        'Coffee',                               # 20
        'French Bread',                         # 21
        'Frying Pan',                           # 22
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 270,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 15,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 66900,
        Unknown_04              = 800,
        Unknown_08              = 35500,
        Unknown_0C              = 4,
        Unknown_0E              = 180,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = -32600,
        Unknown_20              = 0,
        Unknown_24              = -41000,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 45,
        Unknown_34              = 45,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 15,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 66900,
        Unknown_04              = 800,
        Unknown_08              = 35500,
        Unknown_0C              = 4,
        Unknown_0E              = 180,
        Unknown_10              = 0,
        Unknown_14              = 6000,
        Unknown_18              = -10000,
        Unknown_1C              = -1040,
        Unknown_20              = 0,
        Unknown_24              = -3230,
        Unknown_28              = 3000,
        Unknown_2C              = 280,
        Unknown_30              = 45,
        Unknown_32              = 45,
        Unknown_34              = 45,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 15,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02000 ._CH',             # 00
        'ED6_DT07/CH00010 ._CH',             # 01
        'ED6_DT06/CH20008 ._CH',             # 02
        'ED6_DT06/CH20005 ._CH',             # 03
        'ED6_DT06/CH20006 ._CH',             # 04
        'ED6_DT07/CH02210 ._CH',             # 05
        'ED6_DT07/CH02220 ._CH',             # 06
        'ED6_DT06/CH20011 ._CH',             # 07
        'ED6_DT07/CH00003 ._CH',             # 08
        'ED6_DT07/CH00013 ._CH',             # 09
        'ED6_DT07/CH02003 ._CH',             # 0A
        'ED6_DT07/CH00023 ._CH',             # 0B
        'ED6_DT06/CH20020 ._CH',             # 0C
        'ED6_DT06/CH20021 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT07/CH02000P._CP',             # 00
        'ED6_DT07/CH00010P._CP',             # 01
        'ED6_DT06/CH20008P._CP',             # 02
        'ED6_DT06/CH20005P._CP',             # 03
        'ED6_DT06/CH20006P._CP',             # 04
        'ED6_DT07/CH02210P._CP',             # 05
        'ED6_DT07/CH02220P._CP',             # 06
        'ED6_DT06/CH20011P._CP',             # 07
        'ED6_DT07/CH00003P._CP',             # 08
        'ED6_DT07/CH00013P._CP',             # 09
        'ED6_DT07/CH02003P._CP',             # 0A
        'ED6_DT07/CH00023P._CP',             # 0B
        'ED6_DT06/CH20020P._CP',             # 0C
        'ED6_DT06/CH20021P._CP',             # 0D
    )

    DeclNpc(
        X                   = -1600,
        Z                   = 0,
        Y                   = 3011,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x141,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 11500,
        Z                   = 0,
        Y                   = -3400,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 148000,
        Z                   = 520,
        Y                   = 145400,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -8230,
        Z                   = 200,
        Y                   = -520,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1C0,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -9550,
        Z                   = 200,
        Y                   = -520,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -8100,
        Z                   = 200,
        Y                   = 2200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65548,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65548,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65548,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1572876,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1572876,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1572876,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 720908,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2031628,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 146290,
        TriggerZ            = 0,
        TriggerY            = 144760,
        TriggerRange        = 800,
        ActorX              = 147910,
        ActorZ              = 1500,
        ActorY              = 144780,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 72010,
        TriggerZ            = 0,
        TriggerY            = 71390,
        TriggerRange        = 800,
        ActorX              = 72570,
        ActorZ              = 1500,
        ActorY              = 72600,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3AA",          # 00, 0
        "Function_1_77B",          # 01, 1
        "Function_2_7B3",          # 02, 2
        "Function_3_7C9",          # 03, 3
        "Function_4_A52",          # 04, 4
        "Function_5_D33",          # 05, 5
        "Function_6_1DFD",         # 06, 6
        "Function_7_1E86",         # 07, 7
        "Function_8_1EF0",         # 08, 8
        "Function_9_2A81",         # 09, 9
        "Function_10_2B42",        # 0A, 10
        "Function_11_2BE6",        # 0B, 11
        "Function_12_2C1D",        # 0C, 12
        "Function_13_42C9",        # 0D, 13
        "Function_14_4370",        # 0E, 14
        "Function_15_6FFE",        # 0F, 15
        "Function_16_729B",        # 10, 16
    )


    def Function_0_3AA(): pass

    label("Function_0_3AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_3B9")
    SetChrFlags(0x8, 0x80)
    Jump("loc_4B1")

    label("loc_3B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_3D9")
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 3554, 0, 71683, 161)
    Jump("loc_4B1")

    label("loc_3D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 2)), scpexpr(EXPR_END)), "loc_49D")
    SetChrPos(0x8, -8100, 200, 2200, 180)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x10)
    SetChrChipByIndex(0x8, 10)
    SetChrPos(0xE, -8360, 700, 300, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x11, -7860, 700, 200, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0xF, -9620, 700, 300, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x12, -9120, 700, 200, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x10, -8260, 700, 1100, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x13, -8860, 700, 1200, 0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x14, -9520, 700, 1100, 0)
    ClearChrFlags(0x14, 0x80)
    Jump("loc_4B1")

    label("loc_49D")

    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)

    label("loc_4B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_4C8")
    OP_A3(0x3FA)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x30), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 14)

    label("loc_4C8")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (1, "loc_4E4"),
        (2, "loc_587"),
        (3, "loc_69D"),
        (102, "loc_6A4"),
        (103, "loc_70F"),
        (SWITCH_DEFAULT, "loc_77A"),
    )


    label("loc_4E4")

    ClearMapFlags(0x1)
    OP_6D(-6600, 0, 1400, 0)
    SetChrSubChip(0xE, 10)
    SetChrSubChip(0xF, 10)
    SetChrSubChip(0x10, 1)
    SetChrPos(0xE, -8360, 700, 300, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xF, -9620, 700, 300, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x10, -8260, 700, 1100, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x14, -9520, 700, 1100, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x15, -640, 800, 2960, 0)
    ClearChrFlags(0x15, 0x80)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 4)
    Jump("loc_77A")

    label("loc_587")

    ClearMapFlags(0x1)
    OP_6D(-3500, 0, 1700, 0)
    SetChrPos(0xA, -8230, 200, -520, 0)
    SetChrPos(0x9, -9550, 200, -520, 0)
    SetChrPos(0x8, -8100, 200, 2200, 180)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrChipByIndex(0xA, 8)
    SetChrChipByIndex(0x9, 9)
    SetChrChipByIndex(0x8, 10)
    SetChrPos(0xE, -8360, 700, 300, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x11, -7860, 700, 200, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0xF, -9620, 700, 300, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x12, -9120, 700, 200, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x10, -8260, 700, 1100, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x13, -8860, 700, 1200, 0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x14, -9520, 700, 1100, 0)
    ClearChrFlags(0x14, 0x80)
    FadeToBright(1000, 0)
    Event(0, 5)
    Jump("loc_77A")

    label("loc_69D")

    Event(0, 5)
    Jump("loc_77A")

    label("loc_6A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_6AE")
    Jump("loc_70C")

    label("loc_6AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_70C")
    ClearMapFlags(0x1)
    OP_6D(6187, 0, 71060, 0)
    SetChrPos(0x101, 3012, 0, 67051, 0)
    SetChrPos(0x102, 3891, 0, 66840, 0)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 3060, 200, 71360, 180)
    SetChrChipByIndex(0x8, 10)
    Event(0, 8)

    label("loc_70C")

    Jump("loc_77A")

    label("loc_70F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_719")
    Jump("loc_777")

    label("loc_719")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_777")
    ClearMapFlags(0x1)
    OP_6D(6187, 0, 71060, 0)
    SetChrPos(0x101, 8324, 0, 71386, 270)
    SetChrPos(0x102, 8138, 0, 70528, 270)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 3060, 200, 71360, 180)
    SetChrChipByIndex(0x8, 10)
    Event(0, 8)

    label("loc_777")

    Jump("loc_77A")

    label("loc_77A")

    Return()

    # Function_0_3AA end

    def Function_1_77B(): pass

    label("Function_1_77B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_793")
    OP_B1("t0310_y")
    Jump("loc_79C")

    label("loc_793")

    OP_B1("t0310_n")

    label("loc_79C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_7B2")
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7B2")

    Return()

    # Function_1_77B end

    def Function_2_7B3(): pass

    label("Function_2_7B3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7C8")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_7B3")

    label("loc_7C8")

    Return()

    # Function_2_7B3 end

    def Function_3_7C9(): pass

    label("Function_3_7C9")

    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7EE")
    SetChrSubChip(0xFE, 1)
    Jump("loc_809")

    label("loc_7EE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_804")
    SetChrSubChip(0xFE, 2)
    Jump("loc_809")

    label("loc_804")

    SetChrSubChip(0xFE, 0)

    label("loc_809")

    OP_8C(0xFE, 180, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E1")
    OP_A2(0x3)

    ChrTalk(    #0
        0x101,
        (
            "#004FBy the way, Dad. Is it going to be all right if you\x01",
            "stay at home like this instead of going to the guild\x01",
            "today?\x02\x03",

            "You haven't been there for a couple of days now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "#080FUnfortunately, I have a lot of paperwork to sort out.\x02\x03",

            "#080FBut don't you worry, I'm carrying a big enough\x01",
            "workload that the guild's not likely to fire me\x01",
            "any time soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#505F(That's not exactly the most\x01",
            "convincing thing I've heard\x01",
            "come out of your mouth...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A49")

    label("loc_9E1")


    ChrTalk(    #3
        0x8,
        (
            "#080FHow about yourself? Shouldn't you be getting\x01",
            "over to the guild? Scherazard is waiting, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A49")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_3_7C9 end

    def Function_4_A52(): pass

    label("Function_4_A52")

    OP_24(0x1C2, 0x46)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 5)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    SetChrFlags(0x101, 0x8)
    OP_22(0xCA, 0x0, 0x64)
    OP_6D(-1590, 0, 1830, 4000)
    Sleep(1000)
    OP_0D()
    Fade(1000)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x10)
    OP_6D(148000, 540, 145400, 0)
    OP_67(0, 5940, -10000, 0)
    OP_6B(3120, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x101, 0x258, 1200, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x101)
    OP_8C(0xA, 45, 0)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xA, 0x2)
    OP_99(0xA, 0xF, 0x10, 0x3E8)
    OP_24(0x1C2, 0x41)
    Sleep(1000)
    OP_23(0x1C2)
    OP_61(0x101)

    ChrTalk(    #4
        0xA,
        "#459F...Ugghhh... It's so bright in here...\x02",
    )

    CloseMessageWindow()

    def lambda_B51():
        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B51)
    Sleep(200)
    OP_6F(0x0, 5)
    OP_70(0x0, 0x14)
    Sleep(1500)

    def lambda_B79():
        OP_99(0xFE, 0x8, 0xC, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B79)

    ChrTalk(    #5 op#A op#5
        0xA,
        "#458F#3S#15A*yaaaaaaaawn*\x05\x02",
    )

    OP_9E(0xA, 0xF, 0x0, 0x7D0, 0xFA0)

    def lambda_BBB():
        OP_99(0xFE, 0xC, 0xE, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_BBB)
    Sleep(1000)

    ChrTalk(    #6
        0xA,
        "#455FMmm... I slept like a rock.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    OP_99(0xA, 0x11, 0x12, 0x3E8)
    Sleep(400)

    ChrTalk(    #7
        0xA,
        (
            "#457FHmmm...that must mean it's Dad's turn to\x01",
            "cook this morning.\x02\x03",

            "I wonder if that means Joshua's still in bed?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0x5DC)
    OP_21()
    OP_1D(0x46)
    OP_1F(0x50, 0xC8)
    Sleep(2000)
    OP_62(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_99(0xA, 0x13, 0x15, 0x3E8)

    ChrTalk(    #8
        0xA,
        "#450FAh! Guess that's a no.\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_99(0xA, 0x16, 0x17, 0x3E8)

    ChrTalk(    #9
        0xA,
        (
            "#454FWell, I guess I'd better get myself ready then,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMapFlags(0x2000000)
    NewScene("ED6_DT01/T0300   ._SN", 1, 0, 0)
    IdleLoop()
    Return()

    # Function_4_A52 end

    def Function_5_D33(): pass

    label("Function_5_D33")

    EventBegin(0x0)
    OP_6D(-3500, 0, 1700, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    AddParty(0x1, 0xFF)
    SetChrFlags(0x102, 0x80)
    SetChrPos(0x102, -4460, 0, 230, 0)
    ClearMapFlags(0x1)
    OP_43(0x101, 0x0, 0x0, 0x6)
    OP_43(0x9, 0x0, 0x0, 0x7)
    OP_A2(0x0)
    OP_67(0, 7000, -11000, 3000)
    OP_A5(0x0)

    ChrTalk(    #10
        0xA,
        (
            "#001FThanks for the grub, Dad!\x02\x03",

            "#001FBoy, am I stuffed!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 2)
    Sleep(300)

    ChrTalk(    #11
        0x9,
        (
            "#010F#6PAre you eating or inhaling,\x01",
            "Estelle?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 1)
    Sleep(300)

    ChrTalk(    #12
        0xA,
        (
            "#502FHmph.\x01",
            "Like people say, 'Kids who eat and sleep a\x01",
            "lot, grow a lot.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "#080FWell, make sure you get enough to eat,\x01",
            "but don't forget to pour that energy into your\x01",
            "work, too.\x02\x03",

            "#080FThat reminds me, you two are finishing up\x01",
            "your training at the guild today, aren't you?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0)
    SetChrSubChip(0xA, 0)
    Sleep(300)

    ChrTalk(    #14
        0x9,
        (
            "#010F#6PThat's right. It'll be a review of everything\x01",
            "we've learned up to this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xA,
        (
            "#006FAnd once we're finished, we'll be bracers just\x01",
            "like you, Dad!\x02\x03",

            "That means I'm not going to let you treat me\x01",
            "like a kid anymore either!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "#080FYou still lack understanding, Estelle.\x02\x03",

            "You can only become a junior bracer in the beginning--\x01",
            "or in other words, a trainee.\x02\x03",

            "If you want to be treated like an adult, then you should\x01",
            "work extra hard in your training to become a full-fledged bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xA,
        (
            "#009FWell, I'm not afraid of a little hard work!\x02\x03",

            "Just you watch and see what I'm capable of, Dad! I'll be so\x01",
            "successful that it won't be long before I pass you, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "#081FThat's the spirit!\x01",
            "Let's see what you're made of then,\x01",
            "shall we?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 2)
    Sleep(300)

    ChrTalk(    #19
        0x9,
        (
            "#017F#6PLet's not start a rivalry here, you two...\x02\x03",

            "#010FAnd Estelle, keep your focus on the task at\x01",
            "hand.\x02\x03",

            "#010FWe have a test later on today, remember?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 1)
    Sleep(300)

    ChrTalk(    #20
        0xA,
        (
            "#004FHuh...?! \x02\x03",

            "...\x02\x03",

            "#501FWait...what test?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #21
        0x9,
        (
            "#018F#6PPlease tell me that you didn't forget about the test,\x01",
            "Estelle...\x02\x03",

            "You know, the one that checks whether or not we've\x01",
            "mastered the skills we've been learning in training.\x02\x03",

            "Don't you remember Schera saying that if we failed,\x01",
            "we'd be stuck with a ton of extra homework?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #22
        0xA,
        (
            "#505FCrap...\x01",
            "Totally forgot...\x02\x03",

            "Now that you mention it, I guess I kind of\x01",
            "remember her saying something like that... \x02\x03",

            "#001FDon't sweat it!\x01",
            "I'm sure we'll manage somehow or other. ☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x9,
        (
            "#017F#6PI honestly don't know how you've survived this\x01",
            "long, Estelle. Your brain is like a sieve.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "#083FPapa is sad!\x02\x03",

            "How could any child of mine end up with such a\x01",
            "careless, overoptimistic personality?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0)
    Sleep(300)

    ChrTalk(    #25
        0xA,
        (
            "#009FHa! You're the one that raised me,\x01",
            "so I definitely got it from you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x9,
        (
            "#017F#6PI swear, the two of you act so much alike,\x01",
            "but whatever.\x02\x03",

            "#010FWe should probably head over to the guild soon,\x01",
            "Estelle.\x02\x03",

            "#010FSchera's going to be waiting there for us.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 1)
    Sleep(300)

    ChrTalk(    #27
        0xA,
        (
            "#006FSounds like a plan. You know how crazy\x01",
            "scary she gets when someone keeps her\x01",
            "waiting.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(200)
    Fade(1000)
    OP_A2(0x0)
    OP_A2(0x1)
    Sleep(200)
    OP_6D(-5050, 0, -70, 4000)
    OP_A5(0x0)

    ChrTalk(    #28
        0x101,
        (
            "#006FOh, before I forget, it's my turn to cook dinner\x01",
            "tonight.\x02\x03",

            "Is there anything in particular you'd like to eat,\x01",
            "Dad?\x02\x03",

            "Any requests?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "#085FHmm...\x01",
            "Something I'd like to eat, huh?\x02\x03",

            "#085F...\x02\x03",

            "#080FHow about Ruan-style scalloped fish in a balsamic\x01",
            "vinegar sauce?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        "#004FWh-What's that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x9,
        (
            "#019FI think that's a little more than Estelle's cooking skills\x01",
            "can handle... Or our stomachs...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "#081FYou're right.\x01",
            "I just wanted to see what kind of reaction I could\x01",
            "get.\x02\x03",

            "I'll just have the usual fried fish and omelet.\x02\x03",

            "No need for anything fancy,\x01",
            "but do try to make something edible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "\x09#509FHow rude!\x01",
            "...But I can't actually say he's wrong...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "#080FActually, I do have one favor to ask before you\x01",
            "head out.\x02\x03",

            "I'd like you to pick me up a copy of the Liberl News\x01",
            "from the general goods store.\x02\x03",

            "They're supposed to be getting the latest edition in\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        (
            "#006FGot it. One copy of the Liberl News from the\x01",
            "general goods store.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1B62():
        OP_6D(-5870, 0, 1160, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1B62)
    OP_8E(0x101, 0xFFFFE5E8, 0x0, 0x86E, 0x7D0, 0x0)
    TurnDirection(0x101, 0x8, 500)
    SetChrSubChip(0x8, 1)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #36
        "\x07\x00Received \x07\x04500\x07\x00 mira.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    AddMira(500)
    OP_3E(0x35F, 1)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #37
        0x8,
        (
            "#080FIf there's any money left over,\x01",
            "you can have it as your allowance.\x02\x03",

            "#080FHowever, that means: no wasteful spending.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #38
        0x101,
        "#4P#001FAll right! Thanks, Dad!\x02",
    )

    CloseMessageWindow()

    def lambda_1CAD():
        OP_6D(-4460, 0, 230, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1CAD)
    OP_8E(0x101, 0xFFFFEE94, 0x0, 0xE6, 0x7D0, 0x0)
    SetChrSubChip(0x8, 0)
    TurnDirection(0x101, 0x8, 500)

    ChrTalk(    #39
        0x9,
        (
            "#010FOkay, we're heading out now.\x01",
            "See you later, Dad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x8,
        (
            "#080FWork hard and give Scherazard my\x01",
            "regards.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x101, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0x8, 0xFF)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x9, 0x4)
    SetChrFlags(0x8, 0x10)
    OP_A2(0x202)
    ClearChrFlags(0x102, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    ClearMapFlags(0x2000000)
    OP_6D(-2770, 0, -440, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -2770, 0, -440, 180)
    SetChrPos(0x102, -2770, 0, -440, 180)
    FadeToBright(1000, 0)
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    Return()

    # Function_5_D33 end

    def Function_6_1DFD(): pass

    label("Function_6_1DFD")

    OP_A6(0x0)
    OP_6D(-8500, 0, 1700, 3000)
    OP_A3(0x0)
    OP_A6(0x0)
    ClearChrFlags(0xFE, 0x8)
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0xA, 0x80)
    SetChrPos(0xFE, -8810, 0, -1170, 180)
    Sleep(200)
    OP_8E(0xFE, 0xFFFFDE9A, 0x0, 0xFFFFF768, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFEE94, 0x0, 0xE6, 0x7D0, 0x0)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    TurnDirection(0xFE, 0x8, 500)
    OP_A3(0x0)
    Return()

    # Function_6_1DFD end

    def Function_7_1E86(): pass

    label("Function_7_1E86")

    OP_A6(0x1)
    SetChrChipByIndex(0xFE, 1)
    SetChrPos(0xFE, -10410, 0, -800, 180)
    Sleep(200)
    OP_8E(0xFE, 0xFFFFD77E, 0x0, 0xFFFFF880, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFE3C2, 0x0, 0xFFFFF880, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF222, 0x0, 0xFFFFFC0E, 0x7D0, 0x0)
    Sleep(300)
    TurnDirection(0xFE, 0x8, 500)
    OP_A3(0x1)
    Return()

    # Function_7_1E86 end

    def Function_8_1EF0(): pass

    label("Function_8_1EF0")

    EventBegin(0x0)
    OP_43(0x101, 0x0, 0x0, 0x9)
    OP_43(0x102, 0x0, 0x0, 0xA)
    OP_43(0x8, 0x0, 0x0, 0xB)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #41
        0x101,
        "#501FWe're home, Dad!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    OP_A2(0x1)
    OP_A5(0x1)
    OP_A5(0x0)

    ChrTalk(    #42
        0x101,
        (
            "#006F#4PWe finished reporting to the guild\x01",
            "like you told us to.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 1)
    Sleep(100)

    ChrTalk(    #43
        0x8,
        (
            "#080F#5PGood work, kids.\x02\x03",

            "#080FThe details of your reports will be reviewed\x01",
            "at each branch and will affect your pay\x01",
            "and rank advancement in the future.\x02\x03",

            "#080FPlease make sure that you always\x01",
            "remember to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#006F#4PDon't worry, we will.\x02\x03",

            "#501FAnd before I forget, I got that copy\x01",
            "of the Liberl News you wanted.\x02\x03",

            "#501FThere was this letter for you at\x01",
            "the guild, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    OP_A5(0x0)
    OP_8C(0x101, 270, 400)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #45
        "\x07\x00Handed over the \x07\x02Liberl News\x07\x00 and \x07\x02letter\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x347, 1)
    OP_3F(0x336, 1)

    ChrTalk(    #46
        0x8,
        "#084F#5PA letter, huh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#000F#4PWell, I'm going to get cleaned up\x01",
            "and start dinner.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    OP_A5(0x0)

    ChrTalk(    #48
        0x101,
        "#004F#4POh, and, Dad.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    OP_8C(0x101, 270, 400)

    ChrTalk(    #49
        0x101,
        (
            "#008F#4PUm...\x01",
            "Thanks for coming when you did today...\x01",
            "You really helped me out back there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        (
            "#084F#5PI see you're being rather gracious\x01",
            "today. \x02\x03",

            "Papa is happy! How delightful that my\x01",
            "daughter has finally understood what\x01",
            "a great man her father truly is! \x02\x03",

            "#081FThere's no need to hold back,\x01",
            "Estelle! Come and jump into\x01",
            "your father's loving arms!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #51
        0x101,
        (
            "#582F#4PIn your dreams!\x02\x03",

            "#509FI swear, the men in this house\x01",
            "have one thing in common:\x01",
            "they never know when to shut up...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_240D():
        OP_6D(6187, 0, 70000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_240D)
    SetMapFlags(0x400000)
    OP_A2(0x0)
    OP_A2(0x1)
    Sleep(300)
    SetChrSubChip(0x8, 0)
    OP_A5(0x0)
    OP_A5(0x1)
    Sleep(500)

    ChrTalk(    #52
        0x8,
        (
            "#080F#6PI guess she's not as depressed\x01",
            "as I had thought she'd be...\x02\x03",

            "Should I be thanking you, Joshua?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(    #53
        0x102,
        (
            "#010F#4PI didn't do much. I just gave her a\x01",
            "push in the right direction.\x02\x03",

            "Estelle's a resilient girl\x01",
            "to begin with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x8,
        (
            "#085F#6PYes, she is, but she still has\x01",
            "a long way to go.\x02\x03",

            "She'll run into more than just a\x01",
            "few stumbling blocks in this\x01",
            "line of work.\x02\x03",

            "#082FAnd overcoming those obstacles\x01",
            "is what will teach her to stand on\x01",
            "her own two feet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x102,
        (
            "#019F#4PThere's that soft side of yours\x01",
            "talking again.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x97, 0x0, 0x64)
    Sleep(1500)

    NpcTalk(    #56
        0x101,
        "Estelle's Voice",
        (
            "#1POh noooooo!\x01",
            "Are eggs supposed to\x01",
            "explode like that...?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    NpcTalk(    #57
        0x101,
        "Estelle's Voice",
        (
            "#1PI guess I shouldn't have gone in\x01",
            "expecting to make a perfect\x01",
            "meal in a single try...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #58
        0x101,
        "Estelle's Voice",
        (
            "#1PNo, wait! Cooking is supposed to be\x01",
            "about passion! Exploding eggs are\x01",
            "passionate, right?! Now, once more...!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #59
        0x8,
        (
            "#083F#6PThat daughter of mine can sometimes\x01",
            "be a little too...'passionate'.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(    #60
        0x102,
        (
            "#010F#4PI think I'll go help with dinner.\x01",
            "We don't want the curtains to\x01",
            "catch fire again.\x02\x03",

            "#010FBut at this rate, there's no telling\x01",
            "when we can expect to have a bite\x01",
            "of food ready on the dinner table.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    OP_A5(0x1)

    ChrTalk(    #61
        0x8,
        (
            "#080F#6PHa ha...\x02\x03",

            "#085FAll right then, let's see\x01",
            "what this letter is all\x01",
            "about, shall we?\x02",
        )
    )

    CloseMessageWindow()
    OP_6D(5500, 0, 72500, 1500)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #62
        "\x07\x05Cassius cuts the letter's seal.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(1000)
    OP_20(0xBB8)

    ChrTalk(    #63
        0x8,
        (
            "#080F#5PHmmm...a message from the\x01",
            "Erebonian Empire...?\x02\x03",

            "#080F...\x02\x03",

            "#082F...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_21()

    ChrTalk(    #64
        0x8,
        "#086F#5P#3SWhat...?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(500)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x8, 0xFF)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T0311   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_1EF0 end

    def Function_9_2A81(): pass

    label("Function_9_2A81")

    OP_A6(0x0)
    OP_8E(0xFE, 0x1592, 0x0, 0x11334, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    OP_A3(0x0)
    OP_A6(0x0)
    OP_8E(0xFE, 0x1082, 0x0, 0x115DC, 0x7D0, 0x0)
    OP_A3(0x0)
    OP_A6(0x0)
    OP_8E(0xFE, 0x1592, 0x0, 0x11334, 0x7D0, 0x0)
    OP_A3(0x0)
    OP_A6(0x0)
    OP_8E(0xFE, 0xD7B, 0x0, 0x10693, 0xFA0, 0x1)
    OP_8E(0xFE, 0xBA4, 0x0, 0x10306, 0xFA0, 0x1)

    def lambda_2B07():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2B07)
    OP_8E(0xFE, 0xBA4, 0x0, 0xFADC, 0x7D0, 0x1)
    SetChrFlags(0xFE, 0x80)
    OP_A3(0x1)
    OP_A3(0x2)
    OP_A3(0x0)
    OP_A6(0x0)
    OP_A3(0x0)
    OP_A6(0x0)
    OP_A3(0x0)
    Return()

    # Function_9_2A81 end

    def Function_10_2B42(): pass

    label("Function_10_2B42")

    OP_A6(0x1)
    Sleep(500)
    OP_8E(0xFE, 0x1647, 0x0, 0x10E4D, 0xBB8, 0x0)
    TurnDirection(0xFE, 0x8, 400)
    OP_A3(0x1)
    OP_A6(0x1)

    label("loc_2B6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2B7D")
    TurnDirection(0xFE, 0x101, 0)
    OP_48()
    Jump("loc_2B6B")

    label("loc_2B7D")

    OP_A6(0x1)
    OP_8E(0xFE, 0xD7B, 0x0, 0x10693, 0xBB8, 0x1)
    OP_8E(0xFE, 0xBA4, 0x0, 0x10306, 0xBB8, 0x1)

    def lambda_2BAE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2BAE)
    OP_8E(0xFE, 0xBA4, 0x0, 0xFADC, 0x7D0, 0x1)
    SetChrFlags(0xFE, 0x80)
    OP_A3(0x2)
    OP_A3(0x1)
    OP_A6(0x1)
    OP_A3(0x1)
    OP_A6(0x1)
    OP_A3(0x1)
    Return()

    # Function_10_2B42 end

    def Function_11_2BE6(): pass

    label("Function_11_2BE6")

    OP_A6(0x2)

    label("loc_2BE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2BFB")
    TurnDirection(0xFE, 0x101, 0)
    OP_48()
    Jump("loc_2BE9")

    label("loc_2BFB")

    OP_A6(0x2)

    label("loc_2BFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2C10")
    TurnDirection(0xFE, 0x102, 0)
    OP_48()
    Jump("loc_2BFE")

    label("loc_2C10")

    OP_A6(0x2)
    OP_A3(0x2)
    OP_A6(0x2)
    OP_A3(0x2)
    Return()

    # Function_11_2BE6 end

    def Function_12_2C1D(): pass

    label("Function_12_2C1D")

    OP_6D(-7500, 0, 1700, 0)
    SetChrPos(0x101, -7950, 0, -500, 0)
    SetChrPos(0x102, -9310, 0, -300, 0)
    SetChrPos(0xA, -8230, 200, -520, 0)
    SetChrPos(0x9, -9550, 200, -520, 0)
    SetChrPos(0x8, -8100, 200, 2200, 180)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0x9, 0x4)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0x9, 0x8)
    SetChrChipByIndex(0xA, 8)
    SetChrChipByIndex(0x9, 9)
    SetChrSubChip(0xE, 0)
    SetChrSubChip(0xF, 0)
    SetChrSubChip(0x10, 0)
    SetChrSubChip(0x14, 8)
    SetChrPos(0xE, -8360, 700, 300, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x11, -7860, 700, 200, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0xF, -9620, 700, 300, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x12, -9120, 700, 200, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x10, -8260, 700, 1100, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x13, -8860, 700, 1200, 0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x14, -9520, 700, 1100, 0)
    ClearChrFlags(0x14, 0x80)
    FadeToBright(1000, 0)
    OP_1D(0x54)
    OP_0D()

    ChrTalk(    #65
        0x8,
        "#084FWow! This is a surprise...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #66
        0x101,
        (
            "#502FThis new dish is what I call,\x01",
            "'Estelle's Egg-Splosion Over Rice'! \x02\x03",

            "#502FBe sure to savor every last morsel.♪\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 2)
    Sleep(300)

    ChrTalk(    #67
        0x102,
        (
            "#019F#6PI will. Your cooking this evening\x01",
            "is excellent.\x02\x03",

            "#019FMy compliments to the chef.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 1)
    Sleep(300)

    ChrTalk(    #68
        0x101,
        (
            "#001FHeehee.\x01",
            "This is raw talent at its best!\x02\x03",

            "#001FToday certainly has been a busy\x01",
            "but great day nonetheless.\x02\x03",

            "#001FWe qualified as junior bracers,\x01",
            "had our first real assignment...\x02\x03",

            "#001F...and I didn't even lose my\x01",
            "eyebrows making dinner this\x01",
            "time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        (
            "#081FNot to mention the food being\x01",
            "delicious. For a first attempt,\x01",
            "this dish is actually quite edible.\x02\x03",

            "#081FAt first I thought I might have to pitch it out\x01",
            "the window when you weren't looking, but it\x01",
            "seems that technique won't be necessary tonight.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0)
    Sleep(300)

    ChrTalk(    #70
        0x101,
        (
            "#009FSometimes you're just so despicably rude,\x01",
            "Dad. Don't you know how to be humble\x01",
            "and just say something tastes nice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x8,
        (
            "#080FAll right then, how about this? Boy, I never\x01",
            "thought I'd be able to eat something wonderful\x01",
            "like this before I had to leave on business.\x02\x03",

            "#080FYou made a splendid meal, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        (
            "#001FThanks, Dad...\x02\x03",

            "#001F...\x02\x03",

            "#501FWait...\x01",
            "Business?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0)
    Sleep(300)

    ChrTalk(    #73
        0x102,
        "#014F#6PAre you really leaving again...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x8,
        (
            "#080FYes.\x02\x03",

            "#080FSomething unexpected came up.\x01",
            "This time, I'm going to be away\x01",
            "for a while.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #75
        0x101,
        (
            "#004FH-Hold on a minute!\x02\x03",

            "#004FYou're leaving...when?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x8,
        "#080FTomorrow morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        (
            "#005FWhat?! I don't care what kind\x01",
            "of job you're doing! That's just\x01",
            "too soon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x102,
        (
            "#012F#6PIt's about that letter, isn't it?\x01",
            "Was there some sort of incident?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        (
            "#080FOh, it's nothing like that...\x01",
            "just a simple investigation.\x02\x03",

            "#080FI'll have to visit a number of\x01",
            "places, so it'll take me about a\x01",
            "solid month before I'm through.\x02\x03",

            "#080FThat being the case, please\x01",
            "take good care of the house\x01",
            "while I'm away.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #80
        0x101,
        (
            "#005FWhat do you mean,\x01",
            "'That being the case'?!\x02\x03",

            "#003FYou always use some vague\x01",
            "excuse like that and take off\x01",
            "for who knows how long...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x102,
        (
            "#015F#6PWe have to accept it, Estelle.\x02\x03",

            "#015FA bracer's job is to help those\x01",
            "who come to us for help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        (
            "#002FI know, I know...but what are you\x01",
            "going to do about all your jobs\x01",
            "here at the Rolent branch?\x02\x03",

            "#002FYou've already accepted a few\x01",
            "of them, haven't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x8,
        (
            "#080FOh, only about 5 or 6.\x02\x03",

            "#080FSo I was thinking, and...\x02\x03",

            "#080FHow about the both of you handle\x01",
            "them for me instead?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        (
            "#004FWhat...?\x02\x03",

            "#004FAre you really asking us to do\x01",
            "the work that you're supposed\x01",
            "to be doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x8,
        (
            "#080FThat I am. I'll have you do the ones\x01",
            "which I think you can accomplish.\x02\x03",

            "#080FAnd I'll ask Scherazard to handle\x01",
            "the difficult ones.\x02\x03",

            "#080FSo, what do you say?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "[Sure!]\x01",                    # 0
            "[I'd like to, but...]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_386D"),
        (1, "loc_3CD0"),
        (SWITCH_DEFAULT, "loc_4136"),
    )


    label("loc_386D")


    ChrTalk(    #86
        0x101,
        "#001FSure! Of course, we will!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 1)
    Sleep(300)

    ChrTalk(    #87
        0x101,
        (
            "#501FYou're okay doing these too,\x01",
            "right Joshua?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 2)
    Sleep(300)

    ChrTalk(    #88
        0x102,
        (
            "#010F#6PYeah, no problem. Looks like a\x01",
            "good way to get some experience\x01",
            "as a bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x8,
        (
            "#080FThen it's settled.\x02\x03",

            "#080FI'll stop by the guild and let\x01",
            "Aina know about the change of\x01",
            "plan before I leave.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0)
    SetChrSubChip(0xA, 0)
    Sleep(300)

    ChrTalk(    #90
        0x101,
        (
            "#006FAll right.\x01",
            "I'm starting to feel more\x01",
            "determined than ever!\x02\x03",

            "#006FWe'll have to bust our tails with\x01",
            "these jobs so we don't tarnish your\x01",
            "name while you're gone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x8,
        (
            "#084FOh, Estelle, my beloved daughter...\x01",
            "Papa is so proud...\x02\x03",

            "#085FOh, my dear Lena, who art in heaven,\x01",
            "can you see your daughter now?\x02\x03",

            "#085FOur little Estelle has grown up to be\x01",
            "such a lovely young woman!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        (
            "#007FFace it, Dad, you're getting old. If people\x01",
            "lose their trust in you at this age, you\x01",
            "might as well just throw in the towel forever.\x02\x03",

            "#007FI'm only helping you out because I'm\x01",
            "your daughter, and I have a duty to\x01",
            "pay you back for the last 16 years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x8,
        (
            "#086FI-I'm only 45! And what's more,\x01",
            "I'm very likely the most active\x01",
            "member in the entire guild!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x102,
        "#017F#6PNot bad for a pair of comedians.\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Jump("loc_4136")

    label("loc_3CD0")


    ChrTalk(    #95
        0x101,
        (
            "#003FI'd like to but...when I think about\x01",
            "how I messed up today...\x02\x03",

            "#003FIs it really okay to leave these jobs\x01",
            "in the hands of new recruits...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x8,
        (
            "#080FComparatively speaking, none of the jobs are\x01",
            "that difficult, but there are a few in which\x01",
            "you would be entrusted with someone's life.\x02\x03",

            "#080FI'm not going to force you to do\x01",
            "anything. However, I would like\x01",
            "you to sit down and think about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        "#002F...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 1)
    Sleep(300)

    ChrTalk(    #98
        0x101,
        (
            "#002FI don't know...\x01",
            "What do you think, Joshua?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 2)
    Sleep(300)

    ChrTalk(    #99
        0x102,
        (
            "#010F#6PI agree with Dad on this one.\x01",
            "Besides, I think it would be a\x01",
            "great experience for the both of us.\x02\x03",

            "#010FI know as junior bracers we're only like\x01",
            "half a bracer each, but there are two of\x01",
            "us, and two halves make a whole, right?\x02\x03",

            "#010FDon't you think we can manage\x01",
            "these jobs as long as we make\x01",
            "sure to back each other up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        (
            "#501F'Two halves make a whole,' huh?\x02\x03",

            "#006FI think you're right, Joshua!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0)
    Sleep(300)

    ChrTalk(    #101
        0x101,
        (
            "#001FDad, we'll do them for you!\x02\x03",

            "#001FIn fact, I'm really excited to\x01",
            "do them now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x8,
        (
            "#080FThen it's settled.\x02\x03",

            "#080FI'll stop by the guild and let\x01",
            "Aina know about the change of\x01",
            "plan before I leave.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0)
    Sleep(300)
    Jump("loc_4136")

    label("loc_4136")


    ChrTalk(    #103
        0x102,
        (
            "#010F#6PBy the way, Dad. Which flight\x01",
            "will you be on tomorrow?\x02\x03",

            "#010FThe one headed for Grancel\x01",
            "or the one headed for Bose?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x8,
        (
            "#080FI'll be on the one headed for\x01",
            "Grancel. My flight departs at\x01",
            "10 o'clock in the morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        (
            "#001FThat means I'll have to get\x01",
            "up a little earlier tomorrow.\x02\x03",

            "#001FI'd better set my alarm clock\x01",
            "just in case.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_21()
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x8, 0xFF)
    Call(0, 13)
    Return()

    # Function_12_2C1D end

    def Function_13_42C9(): pass

    label("Function_13_42C9")

    OP_1D(0x54)
    SetChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x80)
    SetChrFlags(0x101, 0x8)
    SetChrPos(0x101, 67000, 300, 35500, 225)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x8, 0x80)
    OP_77(0x7, 0x45, 0x91, 0x0, 0x0)
    SetChrPos(0xA, 148000, 520, 145400, 315)
    SetChrChipByIndex(0xA, 2)
    SetChrSubChip(0xA, 0)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xA, 0x80)
    OP_69(0xA, 0x0)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_62(0xA, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(3000)
    SetMapFlags(0x2000000)
    NewScene("ED6_DT01/T0300   ._SN", 2, 0, 0)
    IdleLoop()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x8, 0xFF)
    Return()

    # Function_13_42C9 end

    def Function_14_4370(): pass

    label("Function_14_4370")

    OP_77(0x5A, 0x5A, 0x7D, 0x0, 0x0)
    AddParty(0x0, 0xFF)
    AddParty(0x1, 0xFF)
    AddParty(0x2, 0xFF)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    SetMapFlags(0x400000)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x102, 0x40)
    SetChrFlags(0x103, 0x40)
    SetChrPos(0xB, -7995, 0, 2276, 180)
    OP_69(0xB, 0x0)
    OP_6B(3300, 0)
    FadeToBright(2000, 0)
    Sleep(2000)

    def lambda_43E1():
        OP_6B(2500, 7000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_43E1)
    Sleep(2000)
    Fade(5000)
    ClearChrFlags(0xB, 0x80)
    OP_77(0xFF, 0xC8, 0x96, 0x0, 0x0)
    OP_0D()
    WaitChrThread(0x0, 0x1)
    OP_66(0x0)
    Sleep(1000)

    ChrTalk(    #106
        0xB,
        (
            "#290FMmm...\x02\x03",

            "Daddy's really late.\x02\x03",

            "I even got a message from the\x01",
            "guild saying he'd be home today,\x01",
            "too...\x02",
        )
    )

    CloseMessageWindow()
    Fade(400)
    Sleep(1000)

    def lambda_448F():
        OP_6D(-7866, 1000, 5490, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_448F)
    OP_8C(0xB, 90, 0)
    OP_95(0xB, 0x3E8, 0x0, 0x0, 0x258, 0x1770)
    Sleep(500)
    OP_8E(0xB, 0xFFFFE629, 0x0, 0xB5E, 0xBB8, 0x0)
    OP_8E(0xB, 0xFFFFE146, 0x0, 0x1572, 0xBB8, 0x0)
    Sleep(1500)

    ChrTalk(    #107
        0xB,
        (
            "#290F...and Schera's gone traveling around the\x01",
            "kingdom on some kinda training...\x02\x03",

            "I'm sooooo bored! Maybe I'll just practice\x01",
            "with my staff a bit more before dinner.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xF, 0x0, 0x64)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -1550, 0, -3450, 0)
    Sleep(500)

    NpcTalk(    #108
        0x8,
        "Man's Voice",
        "Hey! I'm home!\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xB, 180, 400)

    ChrTalk(    #109
        0xB,
        "#291FDaddy!\x02",
    )

    CloseMessageWindow()

    def lambda_4615():
        OP_6D(-1110, 0, -1690, 2500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4615)
    OP_8E(0xB, 0xFFFFF772, 0x0, 0xFFFFFA92, 0xFA0, 0x0)
    OP_8C(0xB, 180, 400)

    ChrTalk(    #110
        0x8,
        (
            "#080F#4PSorry to have kept you waiting, Estelle.\x02\x03",

            "Did you take good care of the house\x01",
            "while I was away?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xB,
        (
            "#290F#1P*giggle*\x01",
            "Of course I did!\x02\x03",

            "#290FDid you run into any trouble, Daddy?\x02\x03",

            "You didn't get hurt fighting the bad\x01",
            "monsters, did you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x8,
        (
            "#080F#4PNope. I'm as fit as a fiddle!\x02\x03",

            "That reminds me though, I brought you a\x01",
            "present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xB,
        (
            "#291F#1PReally?! What kind of present?!\x02\x03",

            "A new fishing pole? Sneakers?\x01",
            "Something for my training?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x8,
        (
            "#083F#4P...\x01",
            "Maybe I raised you wrong, Estelle...\x02\x03",

            "Aren't little girls supposed to like clothes\x01",
            "and jewelry?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xB,
        (
            "#290F#1PI like pretty clothes, but they just get\x01",
            "dirty.\x02\x03",

            "And jewelry breaks when you go play\x01",
            "outside with it on.\x02\x03",

            "Anyway, Daddy.\x01",
            "What's with the big blanket?\x02\x03",

            "Is THAT my present?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x8,
        (
            "#080F#4POh, you're a sharp one! \x02\x03",

            "#080FNow why don't you come have a\x01",
            "look?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #117
        (
            "\x07\x05Cassius turns over the top\x01",
            "of the blanket in his arms.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    def lambda_49DC():
        OP_6D(-400, 0, -2200, 1200)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_49DC)
    Sleep(2000)

    NpcTalk(    #118
        0x8,
        "Boy",
        "#305F#2P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xB,
        (
            "#293F#1PWhaa...?\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x8,
        (
            "#081F#4PWell, here you are.\x02\x03",

            "Quite a handsome boy,\x01",
            "don't you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xB,
        (
            "#293F#1PWh-Wh-Wh...\x02\x03",

            "#294F#4SWhy is my present a BOY?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x8,
        (
            "#080F#4PDon't make such a fuss or you'll\x01",
            "wake him up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xB,
        (
            "#292F#1PWake him up...?\x01",
            "You mean he's still alive?\x02\x03",

            "Looks kind of dead if you ask me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x8,
        (
            "#080F#4PI've treated his wounds, so he\x01",
            "should be in stable condition.\x02\x03",

            "In the meantime, however...\x01",
            "we'll need to let him rest.\x02\x03",

            "I'll put him to bed, so if you\x01",
            "wouldn't mind heating a kettle of\x01",
            "water on the stove, I'd appreciate it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xB,
        "#291F#1POkay!\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_66(0x1)
    SetChrFlags(0xB, 0x40)
    OP_6D(8550, 0, 69460, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(44000, 0)
    OP_6E(280, 0)
    SetChrPos(0xB, 8900, 0, 68600, 180)
    SetChrPos(0x8, 8550, 0, 69460, 180)
    SetChrPos(0xC, 9300, 0, 67150, 270)
    ClearChrFlags(0xC, 0x80)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #126
        0xB,
        (
            "#290F#2PHe sure sleeps soundly...\x02\x03",

            "And he almost looks the same age as\x01",
            "me.\x02\x03",

            "This is the first time I've ever seen\x01",
            "black hair like that, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x8,
        (
            "#080FHe certainly does have a nice\x01",
            "head of dark hair.\x02\x03",

            "And a pair of amber eyes to go\x01",
            "with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xB,
        "#290F#2PHmmm.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 0, 400)

    ChrTalk(    #129
        0xB,
        (
            "#292F#2PThat's nice and all, but how about you\x01",
            "come clean and fess up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x8,
        "#084FFess up...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xB,
        (
            "#292F#2PYeah.\x01",
            "Who is this kid, anyway?\x02\x03",

            "And why is he hurt?\x02\x03",

            "Why did you bring him to our house?\x02\x03",

            "Is he an illi-jit-mate child or something?\x01",
            "Did you betray Mommy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x8,
        (
            "#083FWhere have you been picking up these\x01",
            "kinds of words...?\x02\x03",

            "#080FNo doubt from Scherazard,\x01",
            "I assume.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xB,
        "#291F#2PYep! That's right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x8,
        (
            "#080FFor heaven's sake! That girl is\x01",
            "going to get me into trouble one\x01",
            "of these days with all her nonsense...\x02\x03",

            "#080FActually, I just met this boy\x01",
            "while I was out on business.\x02\x03",

            "And I don't even know his name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xB,
        "#290F#2PYou mean bracer business?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x8,
        (
            "#080FSomething like that.\x02\x03",

            "Oh, look...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xB,
        "#293F#2PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x8,
        "#080FHe's waking up.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xC, 400)
    OP_6D(8900, 0, 68600, 2000)

    ChrTalk(    #139
        0xC,
        "#306FMmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xB,
        (
            "#293FWow!\x01",
            "His eyes really are the color of\x01",
            "amber...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xC,
        (
            "#301F...\x02\x03",

            "#301FWh-Where...am I...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x8,
        (
            "#080FSo you're awake now, are you?\x02\x03",

            "Welcome to my humble home. You'll be safe\x01",
            "here, so please just try to rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xC,
        (
            "#300F...\x02\x03",

            "#300FWhat are you trying to pull...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xB,
        "#293FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xC,
        (
            "#300FYou must be out of your mind...\x02\x03",

            "#300FWhy...\x01",
            "Why didn't you just leave me there to die?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x8,
        (
            "#084FWhy? Now that's a question I don't know\x01",
            "how to answer.\x02\x03",

            "#081FDoes, 'Things just worked out that way,'\x01",
            "work for you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xC,
        (
            "#302FD-Don't toy with me, Cassius Bright!\x02\x03",

            "#302FDo you have any idea what you're\x01",
            "getting yourself involved in...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xB,
        "#294FHey!\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xB, 0x4)
    OP_95(0xB, 0x0, 0x2BC, 0xFFFFFB50, 0x4B0, 0x1770)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    OP_22(0x12, 0x0, 0x64)
    OP_95(0xB, 0x0, 0xFFFFFD44, 0x4B0, 0xC8, 0x1770)

    ChrTalk(    #149
        0xB,
        (
            "#294FYou're sure shouting a lot for someone\x01",
            "who's supposed to be hurt!\x02\x03",

            "Running your mouth like that is just gonna\x01",
            "make it take longer for your body to heal!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xC,
        (
            "#304F...\x02\x03",

            "#304F...And just who are you\x01",
            "supposed to be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xB,
        (
            "#294FI'm Estelle!\x02\x03",

            "Estelle Bright!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x8,
        (
            "#080FShe's my daughter.\x02\x03",

            "Don't you remember me telling you that I\x01",
            "have a daughter your age?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xC,
        (
            "#304FNow that you mention it...\x02\x03",

            "#302FWait a minute!\x01",
            "Don't try and change the sub--\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0xB, 0x0, 0x2BC, 0xFFFFFB50, 0x4B0, 0x1770)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    OP_22(0x12, 0x0, 0x64)
    OP_95(0xB, 0x0, 0xFFFFFD44, 0x4B0, 0xC8, 0x1770)
    OP_95(0xB, 0x0, 0x2BC, 0xFFFFFB50, 0x5DC, 0x1770)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_22(0x12, 0x0, 0x64)
    OP_95(0xB, 0x0, 0xFFFFFD44, 0x4B0, 0x1F4, 0x1770)

    ChrTalk(    #154
        0xC,
        "#303FOw!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xB,
        "#294FQuit yelling!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xC,
        (
            "#300FAll right, all right, already...!\x02\x03",

            "#300FBut you jumping on me like that isn't going to\x01",
            "make me heal any faster, either!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xB,
        "#292FI don't hear you yelling again, do I?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xC,
        (
            "#300FLook, jumping on me like that is just going to\x01",
            "make things worse...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xB,
        (
            "#292FDo I hear...\x01",
            "Y・E・L・L・I・N・G?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xC,
        "#304FN-Never mind. Just forget it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x8,
        (
            "#081FAs a word of advice, it would be wise not to\x01",
            "argue with Estelle while you're in this house.\x02\x03",

            "Even I wouldn't stand a chance if I made\x01",
            "her mad enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xC,
        "#304FYeah, I can see that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xB,
        (
            "#292FBy the way, aren't you\x01",
            "forgetting something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xC,
        "#304FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xB,
        (
            "#291FYour name.\x01",
            "You know, that thing that people call you?\x02\x03",

            "I told you mine already, so don't you think\x01",
            "it would be unfair and impolite not to tell me\x01",
            "yours?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xC,
        (
            "#304F...Umm...\x02\x03",

            "#301F...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x8,
        (
            "#080FIt seems like the logical thing to do if you\x01",
            "ask me.\x02\x03",

            "Trying to hide it now would only serve to\x01",
            "your detriment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xC,
        (
            "#301F...\x02\x03",

            "#301FF-Fine...\x02\x03",

            "#301FMy name is...\x02",
        )
    )

    CloseMessageWindow()
    Fade(3000)
    OP_77(0x0, 0x0, 0x0, 0xBB800, 0x0)
    OP_6B(3100, 3000)
    FadeToDark(0, 0, -1)
    Sleep(2000)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x103, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x8, 0x80)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_6D(78732, 0, -740, 0)
    SetChrPos(0x102, 78554, 0, -1046, 0)
    SetChrPos(0x101, 78930, 0, 1500, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #169
        0x102,
        "#013F...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0x10, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #170
        0x102,
        "#010FEstelle, are you in there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x101,
        "Joshua...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x102,
        (
            "#010FDinner's ready.\x02\x03",

            "Just to let you know, we'll be\x01",
            "having roasted basil chicken\x01",
            "and onion soup gratin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x101,
        (
            "That sounds sooo good...\x02\x03",

            "I'll...come down later, so why\x01",
            "don't you two go on ahead\x01",
            "and eat...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x102,
        (
            "#010FAll right...\x02\x03",

            "Well, make sure to come down\x01",
            "before your food gets cold.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(2000)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x102, 0x40)
    SetChrFlags(0x103, 0x40)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 11)
    SetChrPos(0x102, 3066, 0, -2366, 0)
    SetChrPos(0x101, 3066, 0, -2366, 0)
    SetChrPos(0x103, -9810, 250, 2050, 200)
    OP_6B(3000, 0)
    OP_69(0x103, 0x0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #175
        0x103,
        (
            "#026FThe Wheel of Fortune card...again.\x02\x03",

            "Something really IS going on...\x02\x03",

            "I just can't see what it is.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    SetChrSubChip(0x103, 1)

    def lambda_5D25():
        OP_6D(-7800, 1150, 1700, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5D25)
    OP_8E(0x102, 0xFFFFEDEA, 0x0, 0xFA, 0xBB8, 0x0)

    ChrTalk(    #176
        0x103,
        "#023FHm? Where's Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x102,
        (
            "#013F#2PShe said to go ahead and eat\x01",
            "without her... She didn't seem\x01",
            "to have an appetite.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x103,
        (
            "#022FI see...\x02\x03",

            "She took the news a lot better\x01",
            "than I thought she would.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x102,
        (
            "#013F#2PIt's not surprising she doesn't\x01",
            "want to come out of her room...\x02\x03",

            "...seeing as how close she is\x01",
            "with her father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x103,
        (
            "#026FI agree...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5EB2():
        OP_6D(-8020, 0, 1120, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5EB2)
    OP_8E(0x102, 0xFFFFE214, 0x0, 0xFFFFF902, 0xBB8, 0x0)
    OP_8E(0x102, 0xFFFFD7A6, 0x0, 0xFFFFFA60, 0xBB8, 0x0)
    SetChrSubChip(0x103, 0)
    OP_8E(0x102, 0xFFFFD76A, 0x0, 0xFFFFFDB2, 0xBB8, 0x0)
    Fade(1000)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 9)
    SetChrPos(0x102, -9550, 200, -520, 20)
    Sleep(1000)
    OP_62(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x102)

    ChrTalk(    #181
        0x102,
        (
            "#012F#4PSo what do you think about all\x01",
            "of this, Schera?\x02\x03",

            "Is it an accident...or an incident?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x103,
        (
            "#026F#1PTo be honest, I couldn't say\x01",
            "either way...\x02\x03",

            "Your dad is a top-class bracer.\x01",
            "When it comes to crisis management,\x01",
            "he's the best there is.\x02\x03",

            "Whichever it is, if your father\x01",
            "happens to be there, it'll be\x01",
            "resolved.\x02\x03",

            "But the fact is, an airliner,\x01",
            "along with your father,\x01",
            "has gone missing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x102,
        (
            "#013F#4PIn other words, what you're trying\x01",
            "to say is that things that shouldn't\x01",
            "have happened, happened, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x103,
        (
            "#020F#1PDon't lose heart on me now.\x02\x03",

            "You need to be a stout wall of\x01",
            "support and bear Estelle up.\x02\x03",

            "I'll get to work tomorrow and\x01",
            "see what I can find out...\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)

    ChrTalk(    #185
        0x101,
        (
            "#3PMan, it sure smells good down\x01",
            "here.\x02\x03",

            "I can't stand it any longer.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_21()
    OP_1D(0xF)

    def lambda_626F():
        OP_6D(-5000, 0, 1000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_626F)
    SetChrSubChip(0x103, 1)
    Sleep(500)
    SetChrSubChip(0x102, 2)
    OP_8E(0x101, 0xFFFFEDEA, 0x0, 0xFA, 0xBB8, 0x0)

    ChrTalk(    #186
        0x102,
        "#014FWha...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x103,
        "#023F#2PEstelle...are you okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x101,
        (
            "#007FI'm so hungry I thought I was gonna\x01",
            "pass out!\x02\x03",

            "#501FOh, this looks so good!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6337():
        OP_6D(-8590, 200, 780, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6337)
    OP_8E(0x101, 0xFFFFE2C8, 0x0, 0xFFFFFDEE, 0xBB8, 0x0)
    Fade(1000)
    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 8)
    SetChrPos(0x101, -8230, 200, -520, 0)
    SetChrSubChip(0x103, 0)
    OP_0D()
    Sleep(500)
    OP_62(0x101, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #189
        0x101,
        "#001F#2PBon appetit!\x02",
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x103)
    OP_63(0x102)
    SetChrSubChip(0x101, 1)

    ChrTalk(    #190
        0x101,
        (
            "#501F#2PAren't you two having any?\x02\x03",

            "This is great! The basil flavor really\x01",
            "comes out when you roast it...\x02\x03",

            "#001FYou sure know how to cook, Joshua. ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x102,
        "#014F#3PW-Well thanks...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x101,
        (
            "#000F#2PCome on, Schera.\x01",
            "Don't you just sit there, too.\x02\x03",

            "Do you want to drink some of my\x01",
            "dad's brandy from his secret stash?\x02\x03",

            "I'm pretty sure there's a bottle\x01",
            "of Steinrose that's about 20\x01",
            "years old in there.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #193
        0x103,
        (
            "#024FDid you say Steinrose?\x01",
            "And 20 years old, too?!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0)

    ChrTalk(    #194
        0x102,
        (
            "#017F#3PSchera, what do you think\x01",
            "you're doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x103,
        (
            "#023F...*sigh*\x01",
            "Sorry, Estelle. I'm going to\x01",
            "have to pass this time.\x02\x03",

            "#020FBy the way, what were you\x01",
            "doing up in your room?\x02\x03",

            "You didn't come down even after\x01",
            "Joshua called you for supper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x101,
        (
            "#501F#2PHuh? Oh, right. I was just looking\x01",
            "for some extra underwear.\x02\x03",

            "I was having a bit of trouble finding one\x01",
            "of my favorites because it was stuffed\x01",
            "in the back of one of the drawers.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 2)

    ChrTalk(    #197
        0x102,
        "#018F#3P...U-Underwear?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x101,
        (
            "#006F#2POh, and a set of gear for\x01",
            "traveling.\x02\x03",

            "I mean, who knows how long we'll be gone,\x01",
            "so I figure as long as we're prepared\x01",
            "we'll have nothing to worry about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x102,
        "#014F#3PUh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x103,
        (
            "#022FSo what you're saying is...\x02\x03",

            "You intend to head to Bose to\x01",
            "find your father?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x101,
        (
            "#006F#2PWell, duh, that's a no-brainer.\x02\x03",

            "And while I can't imagine anything\x01",
            "bad happened to him, despite his\x01",
            "horrible luck...\x02\x03",

            "Waiting around just doesn't suit\x01",
            "me, so I'm gonna go check things\x01",
            "out for myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x102,
        (
            "#011F#3PHa ha...\x01",
            "You really are something else...\x02\x03",

            "#011FWhether it's your positive attitude\x01",
            "or thick skin I can't say, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x101,
        (
            "#006F#2PWhat-!\x01",
            "You're soooo rude, Joshua...\x02\x03",

            "But, you are coming along too,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x102,
        (
            "#010F#3POf course.\x02\x03",

            "However, it looks like all airliner\x01",
            "flights have been canceled until\x01",
            "the army finishes their search.\x02\x03",

            "It seems like the only way to\x01",
            "Bose is on foot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x101,
        (
            "#000F#2PWalk to Bose, huh...?\x01",
            "I wonder how long that's\x01",
            "gonna take.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x103,
        (
            "#026FFor a bracer on foot, if they\x01",
            "hurry, they can make it there\x01",
            "in about half a day.\x02\x03",

            "#026FBut if that's the route you're\x01",
            "taking, that makes things easy.\x02\x03",

            "#020FI think I'll tag along, as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x101,
        (
            "#004F#2PReally?\x01",
            "You'll come with us?\x02\x03",

            "But, aren't you busy with a\x01",
            "bunch of other jobs...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x103,
        (
            "#020FHey! I trained under your father,\x01",
            "right?\x02\x03",

            "Did you honestly think I'd just sit here\x01",
            "when something could have happened\x01",
            "to the person I owe so much to?\x02\x03",

            "I'm going to talk to Aina and\x01",
            "have her pass my jobs at the\x01",
            "guild to another member.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x101,
        "#501F#2PSchera...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0)

    ChrTalk(    #210
        0x102,
        "#010F#3PWe really appreciate this, Schera.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x103,
        (
            "#027FYou really shouldn't be thanking me.\x02\x03",

            "I just can't leave a job as big as this\x01",
            "up to a bunch of newbies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x101,
        (
            "#007F#2PI hate to say it,\x01",
            "but you're probably right.\x02\x03",

            "#000FOh, well. Since Schera's along\x01",
            "for the ride now, I do feel a\x01",
            "bit more confident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x102,
        (
            "#010F#3PWe appreciate you coming\x01",
            "with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x103,
        (
            "#020FHeehee.\x01",
            "Myself as well.\x02\x03",

            "#020FAnyway, let's make sure to drop\x01",
            "by the guild tomorrow morning\x01",
            "before we leave.\x02\x03",

            "I'll need to explain the situation\x01",
            "to Aina.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_21()
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #215
        "\x07\x05Chapter 1 ～Disappearance of the Linde～\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T0121   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_14_4370 end

    def Function_15_6FFE(): pass

    label("Function_15_6FFE")

    EventBegin(0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x10, -8260, 700, 1100, 0)
    SetChrPos(0x14, -9520, 700, 1100, 0)
    SetChrPos(0x10, -8360, 800, 300, 0)
    SetChrPos(0x14, -9620, 800, 300, 0)
    SetChrChipByIndex(0x10, 13)
    SetChrChipByIndex(0x14, 12)
    SetChrSubChip(0x10, 0)
    SetChrSubChip(0x14, 0)

    ChrTalk(    #216
        0x0,
        "0\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 1)
    SetChrSubChip(0x14, 1)

    ChrTalk(    #217
        0x0,
        "1\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 2)
    SetChrSubChip(0x14, 2)

    ChrTalk(    #218
        0x0,
        "2\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 3)
    SetChrSubChip(0x14, 3)

    ChrTalk(    #219
        0x0,
        "3\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 4)
    SetChrSubChip(0x14, 4)

    ChrTalk(    #220
        0x0,
        "4\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 5)
    SetChrSubChip(0x14, 5)

    ChrTalk(    #221
        0x0,
        "5\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 6)
    SetChrSubChip(0x14, 6)

    ChrTalk(    #222
        0x0,
        "6\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 7)
    SetChrSubChip(0x14, 7)

    ChrTalk(    #223
        0x0,
        "7\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 8)
    SetChrSubChip(0x14, 8)

    ChrTalk(    #224
        0x0,
        "8\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 9)
    SetChrSubChip(0x14, 9)

    ChrTalk(    #225
        0x0,
        "9\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 10)
    SetChrSubChip(0x14, 10)

    ChrTalk(    #226
        0x0,
        "10\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 11)
    SetChrSubChip(0x14, 11)

    ChrTalk(    #227
        0x0,
        "11\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 12)
    SetChrSubChip(0x14, 12)

    ChrTalk(    #228
        0x0,
        "12\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 13)
    SetChrSubChip(0x14, 13)

    ChrTalk(    #229
        0x0,
        "13\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 14)
    SetChrSubChip(0x14, 14)

    ChrTalk(    #230
        0x0,
        "14\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 15)
    SetChrSubChip(0x14, 15)

    ChrTalk(    #231
        0x0,
        "15\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 16)
    SetChrSubChip(0x14, 16)

    ChrTalk(    #232
        0x0,
        "16\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 17)
    SetChrSubChip(0x14, 17)

    ChrTalk(    #233
        0x0,
        "17\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 18)
    SetChrSubChip(0x14, 18)

    ChrTalk(    #234
        0x0,
        "18\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 19)
    SetChrSubChip(0x14, 19)

    ChrTalk(    #235
        0x0,
        "19\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 20)
    SetChrSubChip(0x14, 20)

    ChrTalk(    #236
        0x0,
        "20\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 21)
    SetChrSubChip(0x14, 21)

    ChrTalk(    #237
        0x0,
        "21\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 22)
    SetChrSubChip(0x14, 22)

    ChrTalk(    #238
        0x0,
        "22\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 23)
    SetChrSubChip(0x14, 23)

    ChrTalk(    #239
        0x0,
        "23\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 24)
    SetChrSubChip(0x14, 24)

    ChrTalk(    #240
        0x0,
        "24\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 25)
    SetChrSubChip(0x14, 25)

    ChrTalk(    #241
        0x0,
        "25\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 26)
    SetChrSubChip(0x14, 26)

    ChrTalk(    #242
        0x0,
        "26\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 27)
    SetChrSubChip(0x14, 27)

    ChrTalk(    #243
        0x0,
        "27\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 28)
    SetChrSubChip(0x14, 28)

    ChrTalk(    #244
        0x0,
        "28\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 29)
    SetChrSubChip(0x14, 29)

    ChrTalk(    #245
        0x0,
        "29\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 30)
    SetChrSubChip(0x14, 30)

    ChrTalk(    #246
        0x0,
        "30\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 31)
    SetChrSubChip(0x14, 31)

    ChrTalk(    #247
        0x0,
        "31\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x14, 0x80)
    EventEnd(0x0)
    Return()

    # Function_15_6FFE end

    def Function_16_729B(): pass

    label("Function_16_729B")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7338")
    OP_20(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    Sleep(3500)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_7338")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7352")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_7352")

    Return()

    # Function_16_729B end

    SaveToFile()

Try(main)
