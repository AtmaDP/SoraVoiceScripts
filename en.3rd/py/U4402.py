from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U4402   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4402.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
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


    DeclActor(
        TriggerX            = 4480,
        TriggerZ            = 0,
        TriggerY            = 8670,
        TriggerRange        = 1000,
        ActorX              = 3640,
        ActorZ              = 1000,
        ActorY              = 8740,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_CE",           # 00, 0
        "Function_1_CF",           # 01, 1
        "Function_2_105",          # 02, 2
    )


    def Function_0_CE(): pass

    label("Function_0_CE")

    Return()

    # Function_0_CE end

    def Function_1_CF(): pass

    label("Function_1_CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E4, 1)), scpexpr(EXPR_END)), "loc_E2")
    OP_B1("U4402_y")
    Jump("loc_EB")

    label("loc_E2")

    OP_B1("U4402_n")

    label("loc_EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FD")
    OP_6F(0x2, 0)
    Jump("loc_104")

    label("loc_FD")

    OP_6F(0x2, 60)

    label("loc_104")

    Return()

    # Function_1_CF end

    def Function_2_105(): pass

    label("Function_2_105")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DE")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x14C, 1)"), scpexpr(EXPR_END)), "loc_173")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\x4C\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27B8)
    Jump("loc_1DB")

    label("loc_173")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\x4C\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x4C\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_1DB")

    Jump("loc_2D6")

    label("loc_1DE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05[18/36] The shop and its contents was now his to do with as he pleased,\x01",
            "and as far as he was concerned, he would be a happier man if he never\x01",
            "had to experience the nauseating smell of freshly cut wood ever again.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x138, 0x0)

    label("loc_2D6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_105 end

    SaveToFile()

Try(main)
