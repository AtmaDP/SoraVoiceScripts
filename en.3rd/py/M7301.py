from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M7301   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7301.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60175",
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
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT29/CH14720 ._CH',             # 00
        'ED6_DT29/CH14721 ._CH',             # 01
        'ED6_DT29/CH14550 ._CH',             # 02
        'ED6_DT29/CH14551 ._CH',             # 03
        'ED6_DT29/CH14440 ._CH',             # 04
        'ED6_DT29/CH14440 ._CH',             # 05
        'ED6_DT29/CH14760 ._CH',             # 06
        'ED6_DT29/CH14761 ._CH',             # 07
        'ED6_DT29/CH14770 ._CH',             # 08
        'ED6_DT29/CH14771 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT29/CH14720P._CP',             # 00
        'ED6_DT29/CH14721P._CP',             # 01
        'ED6_DT29/CH14550P._CP',             # 02
        'ED6_DT29/CH14551P._CP',             # 03
        'ED6_DT29/CH14440P._CP',             # 04
        'ED6_DT29/CH14440P._CP',             # 05
        'ED6_DT29/CH14760P._CP',             # 06
        'ED6_DT29/CH14761P._CP',             # 07
        'ED6_DT29/CH14770P._CP',             # 08
        'ED6_DT29/CH14771P._CP',             # 09
    )

    DeclMonster(
        X                   = -1550,
        Z                   = 10180,
        Y                   = 30270,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2BC,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 19670,
        Z                   = 19250,
        Y                   = 58220,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2BD,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 2760,
        Z                   = 28450,
        Y                   = 104650,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2BC,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -42460,
        Z                   = 41940,
        Y                   = 126170,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2BF,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -52870,
        Z                   = 40790,
        Y                   = 119500,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2BD,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 6030,
        Z                   = 57820,
        Y                   = 151010,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2BC,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 28530,
        TriggerZ            = 18900,
        TriggerY            = 61820,
        TriggerRange        = 1000,
        ActorX              = 28530,
        ActorZ              = 19900,
        ActorY              = 61820,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 41470,
        TriggerZ            = 28550,
        TriggerY            = 122550,
        TriggerRange        = 1000,
        ActorX              = 41470,
        ActorZ              = 29550,
        ActorY              = 122550,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -54110,
        TriggerZ            = 31200,
        TriggerY            = 80380,
        TriggerRange        = 1000,
        ActorX              = -54110,
        ActorZ              = 32200,
        ActorY              = 80380,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -54470,
        TriggerZ            = 40800,
        TriggerY            = 128150,
        TriggerRange        = 1000,
        ActorX              = -54470,
        ActorZ              = 41800,
        ActorY              = 128150,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_232",          # 00, 0
        "Function_1_233",          # 01, 1
        "Function_2_2BF",          # 02, 2
        "Function_3_3DD",          # 03, 3
        "Function_4_4FB",          # 04, 4
        "Function_5_619",          # 05, 5
    )


    def Function_0_232(): pass

    label("Function_0_232")

    Return()

    # Function_0_232 end

    def Function_1_233(): pass

    label("Function_1_233")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFF6B90, 0x230094)
    OP_22(0x17B, 0x1, 0x64)
    SetMapFlags(0x100000)
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26C")
    OP_6F(0x0, 0)
    Jump("loc_273")

    label("loc_26C")

    OP_6F(0x0, 60)

    label("loc_273")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_285")
    OP_6F(0x1, 0)
    Jump("loc_28C")

    label("loc_285")

    OP_6F(0x1, 60)

    label("loc_28C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29E")
    OP_6F(0x2, 0)
    Jump("loc_2A5")

    label("loc_29E")

    OP_6F(0x2, 60)

    label("loc_2A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B7")
    OP_6F(0x3, 0)
    Jump("loc_2BE")

    label("loc_2B7")

    OP_6F(0x3, 60)

    label("loc_2BE")

    Return()

    # Function_1_233 end

    def Function_2_2BF(): pass

    label("Function_2_2BF")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_398")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_32D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\xFD\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C60)
    Jump("loc_395")

    label("loc_32D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\xFD\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xFD\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_395")

    Jump("loc_3CF")

    label("loc_398")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05The chest is empty.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x0, 0x0)

    label("loc_3CF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_2BF end

    def Function_3_3DD(): pass

    label("Function_3_3DD")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x5B5, 1)"), scpexpr(EXPR_END)), "loc_44B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05Found \x1F\xB5\x05\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C61)
    Jump("loc_4B3")

    label("loc_44B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05Found \x1F\xB5\x05\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xB5\x05\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_4B3")

    Jump("loc_4ED")

    label("loc_4B6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05The chest is empty.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x0, 0x0)

    label("loc_4ED")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_3DD end

    def Function_4_4FB(): pass

    label("Function_4_4FB")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D4")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x618, 1)"), scpexpr(EXPR_END)), "loc_569")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05Found \x1F\x18\x06\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C62)
    Jump("loc_5D1")

    label("loc_569")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "\x07\x05Found \x1F\x18\x06\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x18\x06\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_5D1")

    Jump("loc_60B")

    label("loc_5D4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05The chest is empty.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x0, 0x0)

    label("loc_60B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_4FB end

    def Function_5_619(): pass

    label("Function_5_619")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F2")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x201, 1)"), scpexpr(EXPR_END)), "loc_687")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05Found \x1F\x01\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C63)
    Jump("loc_6EF")

    label("loc_687")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "\x07\x05Found \x1F\x01\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x01\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_6EF")

    Jump("loc_729")

    label("loc_6F2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05The chest is empty.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x0, 0x0)

    label("loc_729")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_619 end

    SaveToFile()

Try(main)
