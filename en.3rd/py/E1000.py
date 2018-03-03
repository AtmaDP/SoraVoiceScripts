from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E1000   ._SN',
        MapName             = 'Event',
        Location            = 'E1000.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/E1000   ._SN',
            'ED6_DT21/E1000_1 ._SN',
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
        'Campanella',                           # 9
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
        'ED6_DT27/CH03600 ._CH',             # 00
        'ED6_DT26/CH20305 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT27/CH03600P._CP',             # 00
        'ED6_DT26/CH20305P._CP',             # 01
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_DA",           # 00, 0
        "Function_1_F2",           # 01, 1
        "Function_2_F3",           # 02, 2
        "Function_3_1B3",          # 03, 3
        "Function_4_B5F",          # 04, 4
        "Function_5_11AF",         # 05, 5
        "Function_6_17F6",         # 06, 6
        "Function_7_1E69",         # 07, 7
        "Function_8_2410",         # 08, 8
        "Function_9_265B",         # 09, 9
        "Function_10_2721",        # 0A, 10
        "Function_11_48F3",        # 0B, 11
        "Function_12_765D",        # 0C, 12
        "Function_13_765E",        # 0D, 13
        "Function_14_76B7",        # 0E, 14
        "Function_15_7B93",        # 0F, 15
        "Function_16_7BBD",        # 10, 16
        "Function_17_A74D",        # 11, 17
        "Function_18_D356",        # 12, 18
        "Function_19_D3C2",        # 13, 19
    )


    def Function_0_DA(): pass

    label("Function_0_DA")

    Event(0, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_F1")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 15)

    label("loc_F1")

    Return()

    # Function_0_DA end

    def Function_1_F2(): pass

    label("Function_1_F2")

    Return()

    # Function_1_F2 end

    def Function_2_F3(): pass

    label("Function_2_F3")

    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_110")
    Call(0, 3)
    Jump("loc_1A8")

    label("loc_110")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_123")
    Call(0, 9)
    Jump("loc_1A8")

    label("loc_123")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_136")
    Call(0, 12)
    Jump("loc_1A8")

    label("loc_136")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_149")
    Call(0, 14)
    Jump("loc_1A8")

    label("loc_149")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15C")
    Call(0, 16)
    Jump("loc_1A8")

    label("loc_15C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1F), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16F")
    Call(0, 17)
    Jump("loc_1A8")

    label("loc_16F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_182")
    Call(1, 2)
    Jump("loc_1A8")

    label("loc_182")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_195")
    Call(1, 3)
    Jump("loc_1A8")

    label("loc_195")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x22), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A8")
    Call(1, 4)
    Jump("loc_1A8")

    label("loc_1A8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_2_F3 end

    def Function_3_1B3(): pass

    label("Function_3_1B3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x20000000)
    SetMapFlags(0x10)
    OP_11(0x0, 0x0, 0x0, 0x1004, 0x32C8, 0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(0, 80000, 1000, 0)
    OP_67(0, 9300, -10000, 0)
    OP_6B(1000, 0)
    OP_6C(0, 0)
    OP_6E(665, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 80000, 0, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 4)), scpexpr(EXPR_END)), "loc_2F6")
    StopSound(0x3264, 0x61A8, 0x0)
    FadeToBright(4000, 0)
    OP_0D()
    Sleep(200)

    ChrTalk(    #0
        0x10,
        (
            "#5P#850FWhy, hello! You came back to see me again,\x01",
            "did you? Well, aren't you just a doll?\x02\x03",

            "#5PSo, would you like to play another round?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_65A")

    label("loc_2F6")

    OP_A2(0x2F14)
    SetChrPos(0x10, 0, 80000, 0, 0)
    FadeToBright(4000, 0)
    OP_0D()
    Sleep(200)
    SetMessageWindowPos(-1, 80, -1, -1)
    SetChrName("Mysterious Voice")

    AnonymousTalk(    #1
        "\x07\x00Hey. How've you been doing?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    StopSound(0x3264, 0x61A8, 0x9C4)
    OP_0D()
    Sleep(2500)
    OP_8C(0x10, 180, 400)
    Sleep(800)

    ChrTalk(    #2
        0x10,
        "#5P#850FHeehee. It's me! You remember me, right?\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    Fade(100)
    ClearChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    OP_0D()
    OP_99(0x10, 0x0, 0x3, 0x3E8)
    Sleep(500)

    ChrTalk(    #3
        0x10,
        (
            "#5P#853FThanks for coming all this way to see me.\x02\x03",

            "#854FI hope we both have enough fun to make\x01",
            "it worth your while. ♪\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1500)
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1200)
    Fade(700)
    ClearChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #4
        0x10,
        (
            "#5P#850F...What? What am I even doing here?\x02\x03",

            "#851FYou didn't really ask me that, did you? Now, now.\x01",
            "A boy's gotta have his secrets. ㈱\x02\x03",

            "#5P#853FAnyway, let's move on to more important matters,\x01",
            "shall we? I've got something really fun in store for\x01",
            "you today.\x02\x03",

            "#850FIt's called 'Who Wants to Be a Mirannaire?'\x01",
            "In case you didn't already realize, this is a game\x01",
            "full of fun pop questions to see how well you\x01",
            "know your Trails.\x02\x03",

            "Ready to give it a go? You are, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65A")

    OP_C4(0x1, 0x20000000)
    Sleep(300)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #5
        "\x18\x07\x05Become a Mirannaire?\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_69B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B5E")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        330,
        0,
        (
            "Play\x01",      # 0
            "Quit\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6E1"),
        (1, "loc_AA8"),
        (SWITCH_DEFAULT, "loc_B5B"),
    )


    label("loc_6E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x41, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_79C")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        380,
        330,
        1,
        (
            "★ Normal\x01",      # 0
            "★ Hard\x01",        # 1
            "★ Brutal\x01",      # 2
            "★ Maniac\x01",      # 3
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_5F(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_758"),
        (1, "loc_765"),
        (2, "loc_772"),
        (3, "loc_77F"),
        (SWITCH_DEFAULT, "loc_78C"),
    )


    label("loc_758")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_799")

    label("loc_765")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_799")

    label("loc_772")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_799")

    label("loc_77F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_799")

    label("loc_78C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_799")

    label("loc_799")

    Jump("loc_997")

    label("loc_79C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1B, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_858")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        380,
        330,
        1,
        (
            "★ Normal\x01",       # 0
            "★ Hard\x01",         # 1
            "★ Brutal\x01",       # 2
            "    Maniac\x01",      # 3
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_5F(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_814"),
        (1, "loc_821"),
        (2, "loc_82E"),
        (3, "loc_83B"),
        (SWITCH_DEFAULT, "loc_848"),
    )


    label("loc_814")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_855")

    label("loc_821")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_855")

    label("loc_82E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_855")

    label("loc_83B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_855")

    label("loc_848")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_855")

    label("loc_855")

    Jump("loc_997")

    label("loc_858")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1A, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_8F9")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        380,
        330,
        1,
        (
            "★ Normal\x01",       # 0
            "★ Hard\x01",         # 1
            "    Brutal\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_5F(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8C2"),
        (1, "loc_8CF"),
        (2, "loc_8DC"),
        (SWITCH_DEFAULT, "loc_8E9"),
    )


    label("loc_8C2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8F6")

    label("loc_8CF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8F6")

    label("loc_8DC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8F6")

    label("loc_8E9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8F6")

    label("loc_8F6")

    Jump("loc_997")

    label("loc_8F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x19, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_97F")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        380,
        330,
        1,
        (
            "★ Normal\x01",      # 0
            "    Hard\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_5F(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_955"),
        (1, "loc_962"),
        (SWITCH_DEFAULT, "loc_96F"),
    )


    label("loc_955")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_97C")

    label("loc_962")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_97C")

    label("loc_96F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_97C")

    label("loc_97C")

    Jump("loc_997")

    label("loc_97F")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    OP_5F(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_997")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A5F")
    OP_56(0x0)

    ChrTalk(    #6
        0x10,
        (
            "#5P#853FVery nice. I was hoping you'd say that.\x02\x03",

            "#5P#850FWell, if you'll excuse me, I'd better go and get\x01",
            "changed...\x02\x03",

            "#851FI won't keep you waiting too long, okay? ♪\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(300, 0, -1)
    OP_0D()

    label("loc_A5F")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (101, "loc_A7C"),
        (102, "loc_A83"),
        (103, "loc_A8A"),
        (104, "loc_A91"),
        (255, "loc_A98"),
        (SWITCH_DEFAULT, "loc_AA5"),
    )


    label("loc_A7C")

    Call(0, 4)
    Jump("loc_AA5")

    label("loc_A83")

    Call(0, 5)
    Jump("loc_AA5")

    label("loc_A8A")

    Call(0, 6)
    Jump("loc_AA5")

    label("loc_A91")

    Call(0, 7)
    Jump("loc_AA5")

    label("loc_A98")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AA5")

    label("loc_AA5")

    Jump("loc_B5B")

    label("loc_AA8")

    OP_5F(0x0)
    OP_56(0x0)

    ChrTalk(    #7
        0x10,
        (
            "#5P#855FAww... Well, you're no fun.\x02\x03",

            "#5P#850FOh, well. If you change your mind, I'll be right\x01",
            "here.\x02\x03",

            "#5PBye for now!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(200)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_E3(0x1, 0x0)
    OP_11(0x0, 0x0, 0x0, 0xF4240, 0x1E8480, 0x0)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M5402   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_B5B")

    label("loc_B5B")

    Jump("loc_69B")

    label("loc_B5E")

    Return()

    # Function_3_1B3 end

    def Function_4_B5F(): pass

    label("Function_4_B5F")

    Sleep(1000)
    OP_1D(0x19)
    OP_AD(0x240133, 0x0, 0x0, 0x1F4)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B88")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DEE")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        330,
        0,
        (
            "Start\x01",      # 0
            "Rules\x01",      # 1
            "Quit\x01",       # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0xFF)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_BDC"),
        (1, "loc_BE9"),
        (2, "loc_DB1"),
        (SWITCH_DEFAULT, "loc_DEB"),
    )


    label("loc_BDC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DEB")

    label("loc_BE9")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "\x07\x05#0W―――――――――――――――――――――――――――\x01\x01",
            "Each round contains ten multiple choice questions. Choose the right answer\x01",
            "for each of them within the allotted time to win.\x01\x01",
            "Choosing a wrong answer or running out of time on a question will darken\x01",
            "one of the circles at the top of the screen. When all three of them turn\x01",
            "gray, and you will lose the round.\x01\x01",
            "―――――――――――――――――――――――――――#20W\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_DEB")

    label("loc_DB1")

    OP_AE(0x1F4)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_E3(0x1, 0x0)
    OP_11(0x0, 0x0, 0x0, 0xF4240, 0x1E8480, 0x0)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M5402   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_DEB")

    label("loc_DEB")

    Jump("loc_B88")

    label("loc_DEE")

    OP_20(0x3E8)
    OP_AE(0x1F4)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_21()
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x1A, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventBegin(0x0)
    OP_20(0x7D0)
    OP_21()
    OP_28(0x19, 0x4, 0x10)
    FadeToBright(4000, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF3")
    OP_0D()
    Sleep(200)

    ChrTalk(    #9
        0x10,
        (
            "#5P#853FD'aww. That was too bad.\x02\x03",

            "#854FSo, what would you like to do now?\x01",
            "Ready to give it another shot?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 80, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        "\x18\x07\x05Try again?\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_EF3")

    OP_0D()
    Sleep(200)

    ChrTalk(    #11
        0x10,
        (
            "#5P#853FYay! You did it! I knew you could. ♪\x02\x03",

            "#850FWell, I've had plenty of fun for today,\x01",
            "so I think I'll go do my own thing now.\x02\x03",

            "If you ever feel like another round,\x01",
            "though, you know where to find me.\x02\x03",

            "#851FBye bye for now! ♪\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_F7(0xB, 0x5, 0x0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x00Side Story [Campanella's Quiz Game] finished!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_E3(0x1, 0x0)
    Call(0, 8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x19, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_119D")
    OP_28(0x19, 0x4, 0x20)
    OP_28(0x1A, 0x4, 0x2)
    OP_3E(0x1E6, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #13
        "\x07\x05Received \x1F\xE6\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10DD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x45)"), scpexpr(EXPR_END)), "loc_10B5")
    Jump("loc_10DD")

    label("loc_10B5")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #14
        "\x07\x05Learned the recipe for \x1F\xE6\x01\x07\x05.\x02",
    )

    CloseMessageWindow()

    label("loc_10DD")

    Sleep(1000)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x05Congrats! You can now play the 'Hard' difficulty.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #16
        (
            "\x07\x05You can select the difficulty after entering the\x01",
            "Sun Door and deciding whether or not to play\x01",
            "another round.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_119D")

    Sleep(1000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M5402   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_4_B5F end

    def Function_5_11AF(): pass

    label("Function_5_11AF")

    OP_28(0x1A, 0x4, 0x8)
    Sleep(1000)
    OP_1D(0x19)
    OP_AD(0x240134, 0x0, 0x0, 0x1F4)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1443")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        330,
        0,
        (
            "Start\x01",      # 0
            "Rules\x01",      # 1
            "Quit\x01",       # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0xFF)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1231"),
        (1, "loc_123E"),
        (2, "loc_1406"),
        (SWITCH_DEFAULT, "loc_1440"),
    )


    label("loc_1231")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1440")

    label("loc_123E")

    SetMessageWindowPos(-1, 85, 55, 10)
    SetChrName("")

    AnonymousTalk(    #17
        (
            "\x07\x05#0W―――――――――――――――――――――――――――\x01\x01",
            "Each round contains ten multiple choice questions. Choose the right answer\x01",
            "for each of them within the allotted time to win.\x01\x01",
            "Choosing a wrong answer or running out of time on a question will darken\x01",
            "one of the circles at the top of the screen. When all three of them turn\x01",
            "gray, and you will lose the round.\x01\x01",
            "―――――――――――――――――――――――――――#20W\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_1440")

    label("loc_1406")

    OP_AE(0x1F4)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_E3(0x1, 0x0)
    OP_11(0x0, 0x0, 0x0, 0xF4240, 0x1E8480, 0x0)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M5402   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_1440")

    label("loc_1440")

    Jump("loc_11DD")

    label("loc_1443")

    OP_20(0x3E8)
    OP_AE(0x1F4)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_21()
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x1A, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventBegin(0x0)
    OP_20(0x7D0)
    OP_21()
    OP_28(0x1A, 0x4, 0x10)
    FadeToBright(4000, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1548")
    OP_0D()
    Sleep(200)

    ChrTalk(    #18
        0x10,
        (
            "#5P#853FD'aww. That was too bad.\x02\x03",

            "#854FSo, what would you like to do now?\x01",
            "Ready to give it another shot?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 80, -1, -1)
    SetChrName("")

    AnonymousTalk(    #19
        "\x18\x07\x05Try again?\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_1548")

    OP_0D()
    Sleep(200)

    ChrTalk(    #20
        0x10,
        (
            "#5P#853FYay! You did it! I knew you could. ♪\x02\x03",

            "#850FWell, I've had plenty of fun for today,\x01",
            "so I think I'll go do my own thing now.\x02\x03",

            "If you ever feel like another round,\x01",
            "though, you know where to find me.\x02\x03",

            "#851FBye bye for now! ♪\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_F7(0xB, 0x5, 0x1)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #21
        "\x07\x00Side Story [Campanella's Quiz Game] finished!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_E3(0x1, 0x0)
    Call(0, 8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1A, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17E9")
    OP_28(0x1A, 0x4, 0x20)
    OP_28(0x1B, 0x4, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x8)"), scpexpr(EXPR_END)), "loc_16D1")
    Jump("loc_1719")

    label("loc_16D1")

    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #22
        "\x06\x07\x05Learned the recipe for \x07\x02Enigmatic Stew\x07\x05.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_1719")

    Sleep(1000)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #23
        "\x07\x05Congrats! You can now play the 'Brutal' difficulty.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #24
        (
            "\x07\x05You can select the difficulty after entering the\x01",
            "Sun Door and deciding whether or not to play\x01",
            "another round.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(2000)

    label("loc_17E9")

    OP_A2(0x2505)
    NewScene("ED6_DT21/M5402   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_5_11AF end

    def Function_6_17F6(): pass

    label("Function_6_17F6")

    OP_28(0x1B, 0x4, 0x8)
    Sleep(1000)
    OP_1D(0x19)
    OP_AD(0x240135, 0x0, 0x0, 0x1F4)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1824")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A8A")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        330,
        0,
        (
            "Start\x01",      # 0
            "Rules\x01",      # 1
            "Quit\x01",       # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0xFF)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1878"),
        (1, "loc_1885"),
        (2, "loc_1A4D"),
        (SWITCH_DEFAULT, "loc_1A87"),
    )


    label("loc_1878")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A87")

    label("loc_1885")

    SetMessageWindowPos(-1, 85, 55, 10)
    SetChrName("")

    AnonymousTalk(    #25
        (
            "\x07\x05#0W―――――――――――――――――――――――――――\x01\x01",
            "Each round contains ten multiple choice questions. Choose the right answer\x01",
            "for each of them within the allotted time to win.\x01\x01",
            "Choosing a wrong answer or running out of time on a question will darken\x01",
            "one of the circles at the top of the screen. When all three of them turn\x01",
            "gray, and you will lose the round.\x01\x01",
            "―――――――――――――――――――――――――――#20W\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_1A87")

    label("loc_1A4D")

    OP_AE(0x1F4)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_E3(0x1, 0x0)
    OP_11(0x0, 0x0, 0x0, 0xF4240, 0x1E8480, 0x0)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M5402   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_1A87")

    label("loc_1A87")

    Jump("loc_1824")

    label("loc_1A8A")

    OP_20(0x3E8)
    OP_AE(0x1F4)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_21()
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x1A, 0x2, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventBegin(0x0)
    OP_20(0x7D0)
    OP_21()
    OP_28(0x1B, 0x4, 0x10)
    FadeToBright(4000, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B8F")
    OP_0D()
    Sleep(200)

    ChrTalk(    #26
        0x10,
        (
            "#5P#853FD'aww. That was too bad.\x02\x03",

            "#854FSo, what would you like to do now?\x01",
            "Ready to give it another shot?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 80, -1, -1)
    SetChrName("")

    AnonymousTalk(    #27
        "\x18\x07\x05Try again?\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_1B8F")

    OP_0D()
    Sleep(200)

    ChrTalk(    #28
        0x10,
        (
            "#5P#854FWow... I wasn't expecting you to be able\x01",
            "to beat that one. You really DO know your\x01",
            "Trails.\x02\x03",

            "#853FWell, I've had plenty of fun for today,\x01",
            "so I think I'll go do my own thing now.\x02\x03",

            "#850FIf you ever feel like another round,\x01",
            "though, you know where to find me.\x02\x03",

            "#851FBye bye for now! ♪\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_F7(0xB, 0x5, 0x2)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #29
        "\x07\x00Side Story [Campanella's Quiz Game] finished!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_E3(0x1, 0x0)
    OP_11(0x0, 0x0, 0x0, 0xF4240, 0x1E8480, 0x0)
    Call(0, 8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1B, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E53")
    OP_28(0x1B, 0x4, 0x20)
    OP_28(0x41, 0x4, 0x2)
    OP_3E(0x2E9, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #30
        "\x07\x05Received \x1F\xE9\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #31
        "\x07\x05Congrats! You can now play the 'Maniac' difficulty.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #32
        (
            "\x07\x05You can select the difficulty after entering the\x01",
            "Sun Door and deciding whether or not to play\x01",
            "another round.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(2000)

    label("loc_1E53")

    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M5402   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_6_17F6 end

    def Function_7_1E69(): pass

    label("Function_7_1E69")

    OP_28(0x41, 0x4, 0x8)
    Sleep(1000)
    OP_1D(0x19)
    OP_AD(0x240136, 0x0, 0x0, 0x1F4)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E97")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20FD")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        330,
        0,
        (
            "Start\x01",      # 0
            "Rules\x01",      # 1
            "Quit\x01",       # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0xFF)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1EEB"),
        (1, "loc_1EF8"),
        (2, "loc_20C0"),
        (SWITCH_DEFAULT, "loc_20FA"),
    )


    label("loc_1EEB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_20FA")

    label("loc_1EF8")

    SetMessageWindowPos(-1, 85, 55, 10)
    SetChrName("")

    AnonymousTalk(    #33
        (
            "\x07\x05#0W―――――――――――――――――――――――――――\x01\x01",
            "Each round contains ten multiple choice questions. Choose the right answer\x01",
            "for each of them within the allotted time to win.\x01\x01",
            "Choosing a wrong answer or running out of time on a question will darken\x01",
            "one of the circles at the top of the screen. When all three of them turn\x01",
            "gray, and you will lose the round.\x01\x01",
            "―――――――――――――――――――――――――――#20W\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_20FA")

    label("loc_20C0")

    OP_AE(0x1F4)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_E3(0x1, 0x0)
    OP_11(0x0, 0x0, 0x0, 0xF4240, 0x1E8480, 0x0)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M5402   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_20FA")

    label("loc_20FA")

    Jump("loc_1E97")

    label("loc_20FD")

    OP_20(0x3E8)
    OP_AE(0x1F4)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_21()
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x1A, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventBegin(0x0)
    OP_20(0x7D0)
    OP_21()
    OP_28(0x41, 0x4, 0x10)
    FadeToBright(4000, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2202")
    OP_0D()
    Sleep(200)

    ChrTalk(    #34
        0x10,
        (
            "#5P#853FD'aww. That was too bad.\x02\x03",

            "#854FSo, what would you like to do now?\x01",
            "Ready to give it another shot?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 80, -1, -1)
    SetChrName("")

    AnonymousTalk(    #35
        "\x18\x07\x05Try again?\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_2202")

    OP_0D()
    Sleep(200)

    ChrTalk(    #36
        0x10,
        (
            "#5P#854FAmazing! You've conquered the Maniac difficulty.\x01",
            "You maniac. Pun absolutely intended. ㈱\x02\x03",

            "#853FWell, that's all I've got. I had lots\x01",
            "of fun hanging out with you, you know.\x02\x03",

            "#850FOh, but feel free to swing by again any time.\x01",
            "I'm always up for brushing up on my Trails.\x02\x03",

            "#851FTa-ta, babe! ♪\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_F7(0xB, 0x5, 0x3)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #37
        "\x07\x00Side Story [Campanella's Quiz Game] finished!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_E3(0x1, 0x0)
    OP_11(0x0, 0x0, 0x0, 0xF4240, 0x1E8480, 0x0)
    Call(0, 8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x41, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23FA")
    OP_28(0x41, 0x4, 0x20)
    OP_3E(0x2EE, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #38
        "\x07\x05Received \x1F\xEE\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_23FA")

    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M5402   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_7_1E69 end

    def Function_8_2410(): pass

    label("Function_8_2410")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2456")
    AddMira(1)

    AnonymousTalk(    #39
        "\x07\x05[Rank 10] Received \x07\x021 mira\x07\x05.\x02",
    )

    Jump("loc_264E")

    label("loc_2456")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_248C")
    AddMira(10)

    AnonymousTalk(    #40
        "\x07\x05[Rank 9] Received \x07\x0210 mira\x07\x05.\x02",
    )

    Jump("loc_264E")

    label("loc_248C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24C3")
    AddMira(100)

    AnonymousTalk(    #41
        "\x07\x05[Rank 8] Received \x07\x02100 mira\x07\x05.\x02",
    )

    Jump("loc_264E")

    label("loc_24C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24FA")
    AddMira(500)

    AnonymousTalk(    #42
        "\x07\x05[Rank 7] Received \x07\x02500 mira\x07\x05.\x02",
    )

    Jump("loc_264E")

    label("loc_24FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2533")
    AddMira(1000)

    AnonymousTalk(    #43
        "\x07\x05[Rank 6] Received \x07\x021,000 mira\x07\x05.\x02",
    )

    Jump("loc_264E")

    label("loc_2533")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_256C")
    AddMira(2000)

    AnonymousTalk(    #44
        "\x07\x05[Rank 5] Received \x07\x022,000 mira\x07\x05.\x02",
    )

    Jump("loc_264E")

    label("loc_256C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25A5")
    AddMira(3000)

    AnonymousTalk(    #45
        "\x07\x05[Rank 4] Received \x07\x023,000 mira\x07\x05.\x02",
    )

    Jump("loc_264E")

    label("loc_25A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25DE")
    AddMira(4000)

    AnonymousTalk(    #46
        "\x07\x05[Rank 3] Received \x07\x024,000 mira\x07\x05.\x02",
    )

    Jump("loc_264E")

    label("loc_25DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2617")
    AddMira(5000)

    AnonymousTalk(    #47
        "\x07\x05[Rank 2] Received \x07\x025,000 mira\x07\x05.\x02",
    )

    Jump("loc_264E")

    label("loc_2617")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_264E")
    AddMira(10000)

    AnonymousTalk(    #48
        "\x07\x05[Rank 1] Received \x07\x0210,000 mira\x07\x05.\x02",
    )


    label("loc_264E")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Return()

    # Function_8_2410 end

    def Function_9_265B(): pass

    label("Function_9_265B")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_271C")
    OP_1D(0xBF)
    SetMessageWindowPos(-1, 60, -1, -1)
    SetChrName("")

    AnonymousTalk(    #49
        "\x18\x07\x05The Casino -Gambler Jack-\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        160,
        0,
        (
            "Start From the Beginning\x01",          # 0
            "Start From Jack's Appearance\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Sleep(100)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2715")
    OP_20(0x7D0)
    OP_21()
    Call(0, 10)
    Jump("loc_2719")

    label("loc_2715")

    Call(0, 11)

    label("loc_2719")

    Jump("loc_2720")

    label("loc_271C")

    Call(0, 10)

    label("loc_2720")

    Return()

    # Function_9_265B end

    def Function_10_2721(): pass

    label("Function_10_2721")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x20000000)
    OP_1D(0x1)
    OP_C4(0x0, 0x800)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS511._CH")
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #50
        (
            "\x07\x00The Calvard Republic.\x02\x01",

            "    There's a city in this country, a place where\x01",
            "migrants from the East have recreated their\x01",
            "homeland down to the bright lacquered tiles. \x02\x01",

            "Nicknamed the Eastern Quarter, it was home to\x01",
            "people of all kinds from all places.\x02\x01",

            " On the northern outskirts of that town was a little,\x01",
            "run-down bar. Doubtless it had been presentable\x01",
            "once, but now the plaster was crumbling and what\x01",
            "doors were left barely fit their pitted frames.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #51
        (
            "\x07\x00Of course, such a seedy place attracted the clientele\x01",
            "to match.\x02\x01",

            "Inside were two gamblers of exceptional skill.\x01",
            "It was only mere months ago when they had turned\x01",
            "the underworld on its head in the match of the\x01",
            "century.\x02\x01",

            "The first was Jack, a prolific, blue-eyed gambler\x01",
            "known by the moniker 'Victory Jack,' who was\x01",
            "finally able to put his past behind him...\x02\x01",

            "and the second was Halle, a petite gambler who\x01",
            "remained doggedly by his side despite his best\x01",
            "attempts to shake her.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #52
        (
            "\x07\x00Today was yet another ordinary day at that bar;\x01",
            "however, the shriek of the door opening announced\x01",
            "the arrival of someone who was anything but.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0x7D0)
    OP_21()
    OP_1D(0xBF)
    OP_22(0xEA, 0x1, 0x64)
    OP_C6(0x0, 0x3, -1, 3000, 0)
    Sleep(3000)
    OP_C4(0x1, 0x800)
    OP_22(0x177, 0x0, 0x64)
    Sleep(2500)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(600)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(600)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(600)
    Sleep(1000)
    SetMessageWindowPos(340, 120, -1, -1)
    SetChrName("Loud Voice")

    AnonymousTalk(    #53
        (
            "\x07\x0C...Huh?\x02\x03",

            "Who the hell're you?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(40, 80, -1, -1)
    SetChrName("Unpleasant Voice")

    AnonymousTalk(    #54
        (
            "\x07\x0CGotta be either really dumb or really brave,\x01",
            "and that's sayin' something with this joint!\x02\x03",

            "I'm putting my money on the former!\x01",
            "How 'bout you? Bwahaha!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Girl's Voice")

    AnonymousTalk(    #55
        "\x07\x00H-Hey! Get away from him, guys!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(300)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(300)
    OP_22(0x1A, 0x0, 0x64)
    OP_22(0xEA, 0x1, 0x0)
    OP_C5(0x1, 0x0, 0x0, 0x200, 0x200, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS550._CH")
    OP_C5(0x3, 0x0, 0x0, 0x200, 0x200, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS551._CH")
    OP_C6(0x1, 0x3, -1, 1500, 0)
    OP_C6(0x1, 0x4, 0, 0, 0)
    Sleep(2500)
    SetMessageWindowPos(-1, 300, -1, -1)
    SetChrName("Girl")

    AnonymousTalk(    #56
        (
            "\x07\x00*sigh* I'm so sorry about them. I'm sure that\x01",
            "wasn't the welcome you were expecting when\x01",
            "you stepped in here.\x02\x03",

            "They're not bad people. Really, I swear...\x01",
            "Althooough, you could certainly be forgiven\x01",
            "for thinking so looking at them.\x02\x03",

            "Are you a customer, by chance?\x02\x03",

            "Here. Let me show you to a table.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x3, 16777215, 1200, 0)
    Sleep(1000)
    OP_43(0x0, 0x0, 0x0, 0x13)
    Sleep(2000)
    SetMessageWindowPos(150, -1, -1, -1)
    SetChrName("Girl")

    AnonymousTalk(    #57
        (
            "\x07\x00#1911FHeehee. Still, you're quite the unusual one,\x01",
            "if you don't mind me saying so.\x02\x03",

            "Not many people would willingly come to a\x01",
            "run-down bar like this, especially not in the\x01",
            "middle of the day.\x02\x03",

            "#1915FI'm not saying it was a bad idea to come here,\x01",
            "of course!\x02\x03",

            "Sure, it's in desperate need of renovations,\x01",
            "and the regulars are rowdy bunch...\x02\x03",

            "#1910F...but there's just something...I dunno, warm\x01",
            "about this place. Like I'm home.\x02\x03",

            "The food's a lot better than you'd think, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_44(0x0, 0x0)
    Sleep(700)
    OP_22(0x16C, 0x0, 0x96)
    Sleep(200)
    SetMessageWindowPos(150, -1, -1, -1)
    SetChrName("Girl")

    AnonymousTalk(    #58
        (
            "\x07\x00#1913FOh, watch your feet. I'm pretty sure that floor\x01",
            "panel there's going to snap any day now.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(600)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(600)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Girl")

    AnonymousTalk(    #59
        "\x07\x00#1910FWell, here's your seat.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x16E, 0x0, 0x64)
    Sleep(700)
    OP_22(0xD1, 0x0, 0x64)
    Sleep(500)
    Sleep(1000)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    Sleep(1500)
    OP_C6(0x3, 0x3, 16777215, 500, 0)
    Sleep(800)
    SetMessageWindowPos(-1, 300, -1, -1)
    SetChrName("Girl")

    AnonymousTalk(    #60
        (
            "\x07\x00Anything you'd like to order?\x02\x03",

            "You don't look like you're here for booze, anyway.\x01",
            "How about something to eat?\x02\x03",

            "Personally, I'd recommend the tom yum goong!\x02\x03",

            "It's the most popular thing on our menu, and for\x01",
            "good reason! That mix of spicy with just the right\x01",
            "amount of sourness is perfect.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, -1)
    SetChrName("Girl")

    AnonymousTalk(    #61
        (
            "\x07\x00Aha! I can see your mouth watering already.\x01",
            "That's a definite 'yes.'\x02\x03",

            "How about something to drink? Just water?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x3, 0x0, 0x0, 0x200, 0x200, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS553._CH")
    OP_C6(0x3, 0x4, 0, 0, 0)
    OP_C6(0x3, 0x3, -1, 500, 0)
    Sleep(1000)
    OP_C6(0x1, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(-1, 300, -1, -1)
    SetChrName("Girl")

    AnonymousTalk(    #62
        (
            "\x07\x00...Sorry, what was that?\x02\x03",

            "You're looking for Jack?\x02\x03",

            "Well, he's usually sleeping in the back\x01",
            "at this time of day...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x1, 0x0, 0x0, 0x200, 0x200, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS550._CH")
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(800)
    OP_C6(0x3, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(-1, 300, -1, -1)
    SetChrName("Girl")

    AnonymousTalk(    #63
        (
            "\x07\x00...Wait. Did you come here to challenge\x01",
            "him to a game of something?\x02\x03",

            "Sorry... I didn't even think to ask if that was\x01",
            "what you were here for.\x02\x03",

            "Hmm... Well, all right. I'll go and talk with him.\x02\x03",

            "If he's in a good mood, he MIGHT be willing. \x01",
            "Don't get your hopes up, though.\x02\x03",

            "Wait here for a minute, okay?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x3, 16777215, 1200, 0)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(300)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(300)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(500)
    OP_22(0xEA, 0x1, 0x64)
    Sleep(2000)
    SetMessageWindowPos(340, 80, -1, -1)
    SetChrName("Hushed Voice")

    AnonymousTalk(    #64
        (
            "\x07\x0C...Hey, you hear that?\x02\x03",

            "That guy over there wants to take Jack on!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(40, 120, -1, -1)
    SetChrName("Hushed Voice")

    AnonymousTalk(    #65
        (
            "\x07\x0CYeah. I heard.\x02\x03",

            "Haha. If he takes him up on it, this could get\x01",
            "real interesting.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(160, 20, -1, -1)
    SetChrName("Hushed Voice")

    AnonymousTalk(    #66
        (
            "\x07\x0C...Heh. Wouldn't be so sure about that.\x02\x03",

            "It ain't often Jack actually gets serious,\x01",
            "and I dunno if that guy's got what it'd\x01",
            "take to bring it out of him.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(500)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(500)
    OP_22(0xEA, 0x1, 0x0)
    OP_C6(0x1, 0x3, -1, 1500, 0)
    Sleep(2000)
    OP_22(0x16F, 0x0, 0x64)
    Sleep(500)
    SetMessageWindowPos(-1, 300, -1, -1)
    SetChrName("Girl")

    AnonymousTalk(    #67
        (
            "\x07\x00Well, here's the tom yum goong you ordered.\x02\x03",

            "Eat it while it's still hot!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_C5(0x3, 0x0, 0x0, 0x200, 0x200, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS554._CH")
    OP_C6(0x3, 0x4, 0, 0, 0)
    OP_C6(0x3, 0x3, -1, 500, 0)
    Sleep(800)
    OP_C6(0x1, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(-1, 300, -1, -1)
    SetChrName("Girl")

    AnonymousTalk(    #68
        (
            "\x07\x00Oh, and as for Jack... Sorry, but he says he'll\x01",
            "pass this time.\x02\x03",

            "Seems like he's still hungover from drinking\x01",
            "yesterday. Doesn't even want to get up.\x02\x03",

            "I'm sure that's not what you want to hear\x01",
            "after coming all this way to challenge him, \x01",
            "but that's Jack for you.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_C5(0x1, 0x0, 0x0, 0x200, 0x200, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS550._CH")
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(800)
    OP_C6(0x3, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(-1, 300, -1, -1)
    SetChrName("Girl")

    AnonymousTalk(    #69
        (
            "\x07\x00...Wait. No. I've got a great idea!\x02\x03",

            "How about you and I have a game first? If you\x01",
            "beat me, I'll go bug him again.\x02\x03",

            "I'm sure he'd be totally interested in someone\x01",
            "who's better than me.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(-1, 300, -1, -1)
    SetChrName("Girl")

    AnonymousTalk(    #70
        (
            "\x07\x00...Surprised? I'm actually quite the gambler,\x01",
            "you know.\x02\x03",

            "The name's Halle. I'm the daughter of the\x01",
            "legendary gambler 'King.'\x02\x03",

            "Not exactly a household name, but its a pretty\x01",
            "famous one in these kinds of circles.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x3, 0x0, 0x0, 0x200, 0x200, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS555._CH")
    OP_C6(0x3, 0x4, 0, 0, 0)
    OP_C6(0x3, 0x3, -1, 500, 0)
    Sleep(1000)
    OP_C6(0x1, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(-1, 300, -1, -1)
    SetChrName("Halle")

    AnonymousTalk(    #71
        (
            "\x07\x00Fair warning: I don't plan on holding back one\x01",
            "bit. If we're doing this, we're going all out.\x02\x03",

            "Plus if I win, I'm going to have to ask you to\x01",
            "leave.\x02\x03",

            "Are you good with that?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_22(0x170, 0x0, 0x64)
    Sleep(800)
    OP_C5(0x1, 0x0, 0x0, 0x200, 0x200, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS551._CH")
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(800)
    OP_C6(0x3, 0x3, 16777215, 500, 0)
    OP_C5(0x3, 0x0, 0x0, 0x200, 0x200, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS555._CH")
    SetMessageWindowPos(-1, 300, -1, -1)
    SetChrName("Halle")

    AnonymousTalk(    #72
        (
            "\x07\x00Heehee. I'll take that as a yes.\x02\x03",

            "Well, let's move to a more suitable table, shall we?\x02\x03",

            "As for the game...how does blackjack sound?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C4(0x1, 0x20000000)
    OP_C6(0x0, 0x3, 16777215, 1500, 0)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    Sleep(1600)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3F25")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4843")
    OP_AD(0x24013B, 0x0, 0x0, 0x1F4)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3F63")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_43AF")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        330,
        0,
        (
            "Start\x01",      # 0
            "Rules\x01",      # 1
            "Quit\x01",       # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0xFF)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3FB7"),
        (1, "loc_3FC4"),
        (2, "loc_4382"),
        (SWITCH_DEFAULT, "loc_43AC"),
    )


    label("loc_3FB7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_43AC")

    label("loc_3FC4")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #73
        (
            "\x07\x05#0W―――――――――――――――――――――――――――\x01\x01",
            "You will play a series of blackjack games against Halle, one on one.\x01",
            "A maximum of seven games will take place, and the first player to win\x01",
            "four games is the victor. The following commands can be used:\x01\x01",
            "[Hit] Take one additional card. You can take up to six additional cards\x01",
            "providing you don't bust (your total score reaches or exceeds 22).\x01\x01",
            "[Stand] Take no additional cards, and take on your opponent using the\x01",
            "ones you already have.\x01\x01\x01",
            "―――――――――――――――――――――――――――#20W\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #74
        (
            "\x07\x05#0W―――――――――――――――――――――――――――\x01\x01",
            "Having seven cards and a combined total score of 21 or less results in a\x01",
            "'Seven Cards' hand, which is even stronger than a Blackjack (two cards\x01",
            "with a total of 21 between them).\x01\x01",
            "There are no other possible special hands.\x01\x01\x01\x01\x01\x01\x01",
            "―――――――――――――――――――――――――――#20W\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_43AC")

    label("loc_4382")

    OP_AE(0x1F4)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_E3(0x1, 0x0)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M7203   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_43AC")

    label("loc_43AC")

    Jump("loc_3F63")

    label("loc_43AF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AE(0x1F4)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x1D, 0x2, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_20(0x7D0)
    OP_21()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_441C")
    Jump("loc_4843")

    label("loc_441C")

    Sleep(1000)
    OP_1D(0xBF)
    OP_22(0xEA, 0x1, 0x64)
    OP_C6(0x0, 0x3, -1, 3000, 0)
    Sleep(3000)
    OP_C5(0x1, 0x0, 0x0, 0x200, 0x200, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS556._CH")
    OP_C6(0x1, 0x3, -1, 1500, 0)
    OP_C6(0x1, 0x4, 0, 0, 0)
    Sleep(2000)
    SetMessageWindowPos(-1, 300, -1, -1)
    SetChrName("Halle")

    AnonymousTalk(    #75
        (
            "\x07\x00*sigh* Well, that was a letdown...\x02\x03",

            "If that's all you're capable of, even if I did\x01",
            "convince Jack to challenge you, you'd lose\x01",
            "against him anyway.\x02\x03",

            "Well, as harsh as this will sound, rules are\x01",
            "rules. You're gonna have to leave for today.\x02\x03",

            "Heehee. But only for today. Come back once\x01",
            "you've managed to brush up your skills, okay?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, -7829368, 500, 0)
    OP_C6(0x1, 0x3, -7829368, 500, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_C7(0x0, 0x1, 0x3)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("")

    AnonymousTalk(    #76
        "\x18\x07\x05Challenge Halle Again?\x02",
    )

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_478A")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        200,
        0,
        (
            "Lower Difficulty and Try Again\x01",             # 0
            "Try Again Without Lowering Difficulty\x01",      # 1
            "Leave\x01",                                      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_46CF"),
        (1, "loc_4715"),
        (2, "loc_4740"),
        (SWITCH_DEFAULT, "loc_4740"),
    )


    label("loc_46CF")

    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4712")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4712")

    Jump("loc_4787")

    label("loc_4715")

    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4787")

    label("loc_4740")

    OP_20(0x7D0)
    OP_C6(0x0, 0x3, 16777215, 1500, 0)
    OP_C6(0x1, 0x3, 16777215, 1500, 0)
    OP_21()
    OP_C7(0x0, 0x0, 0x3)
    OP_C7(0x0, 0x1, 0x3)
    OP_C7(0x1, 0xFF, 0x0)
    Sleep(1000)
    OP_E3(0x1, 0x0)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M7203   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_4787")

    label("loc_4787")

    Jump("loc_4840")

    label("loc_478A")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        200,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_47CE"),
        (1, "loc_47F9"),
        (SWITCH_DEFAULT, "loc_47F9"),
    )


    label("loc_47CE")

    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4840")

    label("loc_47F9")

    OP_20(0x7D0)
    OP_C6(0x0, 0x3, 16777215, 1500, 0)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    OP_21()
    OP_C7(0x0, 0x0, 0x3)
    OP_C7(0x0, 0x1, 0x3)
    OP_C7(0x1, 0xFF, 0x0)
    Sleep(1000)
    OP_E3(0x1, 0x0)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M7203   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_4840")

    label("loc_4840")

    Jump("loc_3F25")

    label("loc_4843")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48EE")
    Sleep(2000)
    OP_28(0x1F, 0x4, 0x10)
    OP_28(0x1F, 0x4, 0x20)
    OP_28(0x20, 0x4, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x2)"), scpexpr(EXPR_END)), "loc_486D")
    Jump("loc_48B4")

    label("loc_486D")

    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #77
        "\x06\x07\x05Learned the recipe for \x07\x02Tom Yum Goong\x07\x05.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_48B4")

    AddMira(5000)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #78
        "\x07\x05Received \x07\x025,000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_48EE")

    Call(0, 11)
    Return()

    # Function_10_2721 end

    def Function_11_48F3(): pass

    label("Function_11_48F3")

    OP_28(0x20, 0x4, 0x8)
    EventBegin(0x1)
    OP_C4(0x0, 0x20000000)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS511._CH")
    OP_C5(0x1, 0x0, 0x0, 0x200, 0x200, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS550._CH")
    Sleep(1000)
    OP_1D(0xBF)
    OP_22(0xEA, 0x1, 0x64)
    OP_C6(0x0, 0x3, -1, 3000, 0)
    Sleep(3000)
    OP_C6(0x1, 0x3, -1, 1500, 0)
    OP_C6(0x1, 0x4, 0, 0, 0)
    Sleep(2000)
    SetMessageWindowPos(-1, 300, -1, -1)
    SetChrName("Halle")

    AnonymousTalk(    #79
        (
            "\x07\x00...Wow. Who'd've thought? You're actually\x01",
            "really good.\x02\x03",

            "All right, a deal's a deal. I'll go and talk to\x01",
            "Jack again.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x3, 16777215, 1200, 0)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(300)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(300)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(300)
    Sleep(500)
    OP_22(0xEA, 0x1, 0x64)
    Sleep(1000)
    SetMessageWindowPos(340, 120, -1, -1)
    SetChrName("Hushed Voice")

    AnonymousTalk(    #80
        "\x07\x0CWow... He actually managed to beat her?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(40, 80, -1, -1)
    SetChrName("Hushed Voice")

    AnonymousTalk(    #81
        (
            "\x07\x0CLooks that way.\x02\x03",

            "Maybe we'll get to see something\x01",
            "interestin' after all.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1500)
    OP_22(0xEA, 0x1, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Husky Voice")

    AnonymousTalk(    #82
        "\x07\x00*yawn* Man, I'm tired...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x1C, 0x0, 0x64)
    Sleep(500)
    OP_22(0x1C, 0x0, 0x64)
    Sleep(500)
    OP_22(0x1C, 0x0, 0x64)
    Sleep(500)
    OP_C5(0x2, 0x0, 0x0, 0x200, 0x200, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS560._CH")
    OP_C6(0x2, 0x3, -1, 1500, 0)
    OP_C6(0x2, 0x4, 0, 0, 0)
    Sleep(2000)
    SetMessageWindowPos(-1, 280, -1, -1)
    SetChrName("Unkempt Man")

    AnonymousTalk(    #83
        (
            "\x07\x00Huh? There's a new face.\x02\x03",

            "So, what? That the guy who beat Halle?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x4, 0x0, 0x0, 0x200, 0x200, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS567._CH")
    OP_C6(0x4, 0x4, 0, 0, 0)
    OP_C6(0x4, 0x3, -1, 500, 0)
    Sleep(800)
    OP_C6(0x2, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(-1, 280, -1, -1)
    SetChrName("Unkempt Man")

    AnonymousTalk(    #84 op#A op#5
        "\x07\x00#40AGah... My head's throbbing like a bitch#150W...\x05\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("Unkempt Man")

    AnonymousTalk(    #85 op#A op#5
        "\x07\x00#5A#20WWha...?!\x05\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x171, 0x0, 0x64)
    OP_C6(0x4, 0x3, 16777215, 500, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Halle")

    AnonymousTalk(    #86
        "\x07\x00#1914F*sigh* There goes the floor...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(40, 120, -1, -1)
    SetChrName("Unpleasant Voice")

    AnonymousTalk(    #87
        (
            "\x07\x0CHahaha! See? Told ya!\x02\x03",

            "I knew he'd be the one to break it.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(340, 80, -1, -1)
    SetChrName("Loud Voice")

    AnonymousTalk(    #88
        (
            "\x07\x0CHaha! That you did!\x02\x03",

            "Poor guy. It's kinda crazy how he's amazingly \x01",
            "lucky at gambling yet amazingly unlucky at \x01",
            "everything else.\x02\x03",

            "...Actually, it's probably less unlucky and more\x01",
            "him always being out of it.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x2, 0x0, 0x0, 0x200, 0x200, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS562._CH")
    OP_C6(0x2, 0x3, -1, 1500, 0)
    OP_C6(0x2, 0x4, 0, 0, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, 270, -1, -1)
    SetChrName("Jack")

    AnonymousTalk(    #89
        (
            "\x07\x00Hey! I heard that, you!\x02\x03",

            "I'll take you on any time you want!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(240, 180, -1, -1)
    SetChrName("Halle")

    AnonymousTalk(    #90
        (
            "\x07\x00#1916F...That's enough, you two. If you want to fight,\x01",
            "you can take it outside.\x02\x03",

            "The last thing we need is this place ending up\x01",
            "any more run down than it already is.\x02\x03",

            "#1915FOh, and on that note--you're fixing that broken\x01",
            "floorboard yourself, Jack. That's on you.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(-1, 270, -1, -1)
    SetChrName("Jack")

    AnonymousTalk(    #91
        "\x07\x00Wh-Why do I have to do it?!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(240, 180, -1, -1)
    SetChrName("Halle")

    AnonymousTalk(    #92
        "\x07\x00#1912F(*glare*)\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x4, 0x0, 0x0, 0x200, 0x200, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS564._CH")
    OP_C6(0x4, 0x3, -1, 500, 0)
    OP_C6(0x4, 0x4, 0, 0, 0)
    Sleep(800)
    OP_C6(0x2, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(-1, 270, -1, -1)
    SetChrName("Jack")

    AnonymousTalk(    #93
        (
            "\x07\x00*sigh* Fine, fine...\x02\x03",

            "Ugh... This sucks...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(360, 220, -1, -1)
    SetChrName("Hushed Voice")

    AnonymousTalk(    #94
        (
            "\x07\x0CHeh. Never thought I'd see Jack get so wrapped\x01",
            "around somebody's finger.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(10, 110, -1, -1)
    SetChrName("Hushed Voice")

    AnonymousTalk(    #95
        "\x07\x0CYou're telling me.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x2, 0x0, 0x0, 0x200, 0x200, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS562._CH")
    OP_C6(0x2, 0x3, -1, 500, 0)
    OP_C6(0x2, 0x4, 0, 0, 0)
    Sleep(800)
    OP_C6(0x4, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(-1, 270, -1, -1)
    SetChrName("Jack")

    AnonymousTalk(    #96
        "\x07\x00...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    OP_C6(0x2, 0x0, -110000, 0, 1000)
    OP_C6(0x1, 0x0, 110000, 0, 0)
    OP_C5(0x1, 0x0, 0x0, 0x200, 0x200, 0x6E, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS550._CH")
    OP_C6(0x1, 0x3, -1, 1500, 0)
    OP_C6(0x1, 0x4, 0, 0, 0)
    Sleep(1500)
    SetMessageWindowPos(350, 310, -1, -1)
    SetChrName("Halle")

    AnonymousTalk(    #97
        "\x07\x00...Anyway, sorry for the wait. Here's Jack.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x4, 0x0, 0x0, 0x200, 0x200, 0xFF92, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS560._CH")
    OP_C6(0x4, 0x3, -1, 500, 0)
    OP_C6(0x4, 0x4, 0, 0, 0)
    Sleep(800)
    OP_C6(0x2, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(30, 270, -1, -1)
    SetChrName("Jack")

    AnonymousTalk(    #98
        (
            "\x07\x00So...\x02\x03",

            "...I was right, then? This is the guy who wants\x01",
            "to take me on?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 310, -1, -1)
    SetChrName("Halle")

    AnonymousTalk(    #99
        "\x07\x00Sure is.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(30, 270, -1, -1)
    SetChrName("Jack")

    AnonymousTalk(    #100
        (
            "\x07\x00Really? He doesn't look like he's gonna put up\x01",
            "much of a fight to me.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 310, -1, -1)
    SetChrName("Halle")

    AnonymousTalk(    #101
        (
            "\x07\x00Never let your guard down, or you could find\x01",
            "yourself stumbling into something unexpected.\x02\x03",

            "Like, you know, the floorboard again.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 270, -1, -1)
    SetChrName("Jack")

    AnonymousTalk(    #102
        "\x07\x00Bah...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    OP_22(0x16E, 0x0, 0x64)
    Sleep(200)
    Sleep(500)
    OP_22(0xD1, 0x0, 0x64)
    Sleep(500)
    OP_C5(0x2, 0x0, 0x0, 0x200, 0x200, 0xFF92, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS561._CH")
    OP_C6(0x2, 0x3, -1, 500, 0)
    OP_C6(0x2, 0x4, 0, 0, 0)
    Sleep(800)
    OP_C6(0x4, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(30, 270, -1, -1)
    SetChrName("Jack")

    AnonymousTalk(    #103
        (
            "\x07\x00Anyway, I'm Jack. Think you already know that,\x01",
            "though.\x02\x03",

            "...And before we do any gambling, I need a drink.\x02\x03",

            "Get me a whiskey, Halle! On the rocks.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x3, 0x0, 0x0, 0x200, 0x200, 0x6E, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS554._CH")
    OP_C6(0x3, 0x4, 0, 0, 0)
    OP_C6(0x3, 0x3, -1, 500, 0)
    Sleep(1000)
    OP_C6(0x1, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(350, 310, -1, -1)
    SetChrName("Halle")

    AnonymousTalk(    #104
        (
            "\x07\x00*sigh* What was that you said earlier about\x01",
            "a hangover again?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(30, 270, -1, -1)
    SetChrName("Jack")

    AnonymousTalk(    #105
        (
            "\x07\x00Oh, I got rid of that just now.\x02\x03",

            "Come on! We haven't got all day!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 310, -1, -1)
    SetChrName("Halle")

    AnonymousTalk(    #106
        "\x07\x00*sigh* You are unbelievable...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x3, 0x3, 16777215, 1200, 0)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(300)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(300)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(2000)
    OP_C5(0x4, 0x0, 0x0, 0x200, 0x200, 0xFF92, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS560._CH")
    OP_C6(0x4, 0x3, -1, 500, 0)
    OP_C6(0x4, 0x4, 0, 0, 0)
    Sleep(800)
    OP_C6(0x2, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(30, 270, -1, -1)
    SetChrName("Jack")

    AnonymousTalk(    #107
        (
            "\x07\x00Hmm? Did Halle catch your eye?\x02\x03",

            "Girl's about as sexy as a lamppost right now,\x01",
            "but she's got potential.\x02\x03",

            "Couldn't tell you what made her want to work\x01",
            "in a shithole like this, but here she is.\x02\x03",

            "...Anyway, forget her for now.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x2, 0x0, 0x0, 0x200, 0x200, 0xFF92, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS565._CH")
    OP_C6(0x2, 0x3, -1, 500, 0)
    OP_C6(0x2, 0x4, 0, 0, 0)
    Sleep(800)
    OP_C6(0x4, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(30, 270, -1, -1)
    SetChrName("Jack")

    AnonymousTalk(    #108
        (
            "\x07\x00Let's talk about you, yeah?\x02\x03",

            "You're one brave guy to come in here all\x01",
            "on your own and out of the blue.\x02\x03",

            "I doubt many guys would have the guts to\x01",
            "do that. Or girls, for that matter.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(500)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(500)
    OP_C5(0x1, 0x0, 0x0, 0x200, 0x200, 0x6E, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS550._CH")
    OP_C6(0x1, 0x3, -1, 1000, 0)
    OP_C6(0x1, 0x4, 0, 0, 0)
    Sleep(1500)
    OP_22(0x16F, 0x0, 0x64)
    Sleep(500)
    SetMessageWindowPos(350, 310, -1, -1)
    SetChrName("Halle")

    AnonymousTalk(    #109
        (
            "\x07\x00Nice to see you two are hitting it off.\x01",
            "Here's your drink, Jack.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x4, 0x0, 0x0, 0x200, 0x200, 0xFF92, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS560._CH")
    OP_C6(0x4, 0x3, -1, 500, 0)
    OP_C6(0x4, 0x4, 0, 0, 0)
    Sleep(800)
    OP_C6(0x2, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(30, 270, -1, -1)
    SetChrName("Jack")

    AnonymousTalk(    #110
        (
            "\x07\x00Thanks.\x02\x03",

            "...Huh? You hanging around? I figured you'd\x01",
            "get back to work.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 310, -1, -1)
    SetChrName("Halle")

    AnonymousTalk(    #111
        (
            "\x07\x00As if I could work knowing there's an exciting\x01",
            "match going on over here.\x02\x03",

            "The owner's given me the okay, too, so I'm\x01",
            "gonna park my butt right here until you're\x01",
            "done.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(30, 270, -1, -1)
    SetChrName("Jack")

    AnonymousTalk(    #112
        (
            "\x07\x00*sigh* With an owner like that, it's no wonder\x01",
            "this place is the way it is...\x02\x03",

            "Well, whatever. Let's get this over with.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x2, 0x0, 0x0, 0x200, 0x200, 0xFF92, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS561._CH")
    OP_C6(0x2, 0x3, -1, 500, 0)
    OP_C6(0x2, 0x4, 0, 0, 0)
    Sleep(800)
    OP_C6(0x4, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(30, 270, -1, -1)
    SetChrName("Jack")

    AnonymousTalk(    #113
        (
            "\x07\x00Here we go.\x02\x03",

            "You're the challenger, so I'm gonna be the\x01",
            "one picking the game we play.\x02\x03",

            "And I'm going with the one I'm the best at:\x01",
            "poker!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C4(0x1, 0x20000000)
    OP_C6(0x0, 0x3, 16777215, 1500, 0)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    OP_C6(0x2, 0x3, 16777215, 1000, 0)
    Sleep(1600)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5E34")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6C36")
    OP_1D(0xBF)
    OP_AD(0x24013C, 0x0, 0x0, 0x1F4)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5E65")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_66B3")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        330,
        0,
        (
            "Start\x01",      # 0
            "Rules\x01",      # 1
            "Quit\x01",       # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0xFF)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5EB9"),
        (1, "loc_5EC6"),
        (2, "loc_6686"),
        (SWITCH_DEFAULT, "loc_66B0"),
    )


    label("loc_5EB9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_66B0")

    label("loc_5EC6")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #114
        (
            "\x07\x05#0W―――――――――――――――――――――――――――\x01\x01",
            "You will play a one-on-one game of poker against Jack using\x01",
            "unconventional rules. In this game, there are three 'table cards' in the\x01",
            "center of the table that players include in their hands.\x01\x01",
            "Both players are given three cards at the start of the turn, then they\x01",
            "eventually choose five of the three cards in their hand and three on the\x01",
            "table to make a hand.\x01\x01",
            "Both players attempt to steal the other's stars, and the first player to\x01",
            "reach seven stars wins. The player starts with three, while Jack has four.\x01",
            "Losing all of your stars will result in defeat.\x01",
            "―――――――――――――――――――――――――――#20W\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #115
        (
            "\x07\x05#0W―――――――――――――――――――――――――――\x01",
            "The following commands are available:\x01\x01",
            "[Change] - Exchange all cards which haven't been\x01",
            "           placed in hold status once, then play.\x01",
            "[All Hold] - Place all cards in hold status.\x01",
            "[Raise] - Bet 2 stars, not 1, on the next game.\x01",
            "[Fold] - Exchange all cards in hand with the\x01",
            "           table cards. Once per game only.\x01\x01",
            "Selecting a card allows you choose whether to hold it or not. If you want\x01",
            "to keep all of your cards, place them all in hold status.\x01\x01",
            "―――――――――――――――――――――――――――#20W\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #116
        (
            "\x07\x05#0W―――――――――――――――――――――――――――\x01",
            "These are possible hands. The lower down the list, the stronger the hand.\x01\x01",
            "[No Pair] - Hand doesn't fit any of the below.\x01",
            "[1 Pair] - 2 cards have the same number.\x01",
            "[2 Pair] - Hand has 2 groups of 1 Pair cards.\x01",
            "[3 of a Kind] - 3 cards have the same number.\x01",
            "[Straight] - 5 cards have sequential numbers.\x01",
            "[Flush] - 5 cards are from the same suit.\x01",
            "[Full House] - Meet 3 of a Kind & 1 Pair conditions.\x01",
            "[4 of a Kind] - 4 cards have the same number.\x01",
            "[Straight Flush] - Have a Straight and a Flush.\x01",
            "[Royal Flush] - Straight Flush of 10, J, Q, K, A.\x01",
            "―――――――――――――――――――――――――――#20W\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_66B0")

    label("loc_6686")

    OP_AE(0x1F4)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_E3(0x1, 0x0)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M7203   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_66B0")

    label("loc_66B0")

    Jump("loc_5E65")

    label("loc_66B3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AE(0x1F4)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x1C, 0x2, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_20(0x7D0)
    OP_21()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6720")
    Jump("loc_6C36")

    label("loc_6720")

    OP_1D(0xBF)
    OP_22(0xEA, 0x1, 0x64)
    OP_C6(0x0, 0x3, -1, 3000, 0)
    Sleep(3000)
    OP_C5(0x1, 0x0, 0x0, 0x200, 0x200, 0x6E, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS550._CH")
    OP_C5(0x2, 0x0, 0x0, 0x200, 0x200, 0xFF92, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS560._CH")
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 1500, 0)
    OP_C6(0x2, 0x3, -1, 1500, 0)
    Sleep(2000)
    SetMessageWindowPos(30, 270, -1, -1)
    SetChrName("Jack")

    AnonymousTalk(    #117
        (
            "\x07\x00*sigh* Halle wasn't blowin' smoke, was she?\x02\x03",

            "After hearing you beat her, I figured you might\x01",
            "give me a run for my money, but no such luck.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 310, -1, -1)
    SetChrName("Halle")

    AnonymousTalk(    #118
        (
            "\x07\x00I wasn't blowing smoke at all. I don't think he\x01",
            "beat me by pure chance.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(30, 270, -1, -1)
    SetChrName("Jack")

    AnonymousTalk(    #119
        (
            "\x07\x00...Doesn't really matter now. My interest's gone,\x01",
            "I'm afraid.\x02\x03",

            "By all means come back again, but make sure you\x01",
            "can do a whole lot better than that if you do.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, -7829368, 500, 0)
    OP_C6(0x1, 0x3, -7829368, 500, 0)
    OP_C6(0x2, 0x3, -7829368, 500, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_C7(0x0, 0x1, 0x3)
    OP_C7(0x0, 0x2, 0x3)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("")

    AnonymousTalk(    #120
        "\x18\x07\x05Challenge Jack Again?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6B64")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        200,
        0,
        (
            "Lower Difficulty and Try Again \x01",            # 0
            "Try Again Without Lowering Difficulty\x01",      # 1
            "Leave\x01",                                      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6A78"),
        (1, "loc_6ACD"),
        (2, "loc_6B07"),
        (SWITCH_DEFAULT, "loc_6B07"),
    )


    label("loc_6A78")

    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 0, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6ACA")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6ACA")

    Jump("loc_6B61")

    label("loc_6ACD")

    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 0, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6B61")

    label("loc_6B07")

    OP_20(0x7D0)
    OP_C6(0x0, 0x3, 16777215, 1500, 0)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    OP_C6(0x2, 0x3, 16777215, 1000, 0)
    OP_21()
    OP_C7(0x0, 0x0, 0x3)
    OP_C7(0x0, 0x1, 0x3)
    OP_C7(0x0, 0x2, 0x3)
    OP_C7(0x1, 0xFF, 0x0)
    Sleep(1000)
    OP_E3(0x1, 0x0)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M7203   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_6B61")

    label("loc_6B61")

    Jump("loc_6C33")

    label("loc_6B64")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        200,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6B9F"),
        (1, "loc_6BD9"),
        (SWITCH_DEFAULT, "loc_6C33"),
    )


    label("loc_6B9F")

    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 0, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6C33")

    label("loc_6BD9")

    OP_20(0x7D0)
    OP_C6(0x0, 0x3, 16777215, 1500, 0)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    OP_C6(0x2, 0x3, 16777215, 1000, 0)
    OP_21()
    OP_C7(0x0, 0x0, 0x3)
    OP_C7(0x0, 0x1, 0x3)
    OP_C7(0x0, 0x2, 0x3)
    OP_C7(0x1, 0xFF, 0x0)
    Sleep(1000)
    OP_E3(0x1, 0x0)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M7203   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_6C33")

    label("loc_6C33")

    Jump("loc_5E34")

    label("loc_6C36")

    OP_1D(0xBF)
    OP_C6(0x0, 0x3, -1, 3000, 0)
    OP_C4(0x0, 0x20000000)
    Sleep(3000)
    OP_C5(0x1, 0x0, 0x0, 0x200, 0x200, 0x6E, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS550._CH")
    OP_C5(0x2, 0x0, 0x0, 0x200, 0x200, 0xFF92, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS560._CH")
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 1500, 0)
    OP_C6(0x2, 0x3, -1, 1500, 0)
    Sleep(2000)
    SetMessageWindowPos(30, 270, -1, -1)
    SetChrName("Jack")

    AnonymousTalk(    #121
        (
            "\x07\x00...Heh. Well, I'll be damned. You're pretty good\x01",
            "after all.\x02\x03",

            "You beat me, fair and square. I ain't gonna make\x01",
            "excuses.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    OP_22(0xEA, 0x1, 0x64)
    Sleep(1000)
    SetMessageWindowPos(360, 220, -1, -1)
    SetChrName("Hushed Voice")

    AnonymousTalk(    #122
        "\x07\x0CAre you kidding me? He actually beat Jack.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 260, -1, -1)
    SetChrName("Hushed Voice")

    AnonymousTalk(    #123
        (
            "\x07\x0COnly because he was holding back. You know that\x01",
            "as well as I do.\x02\x03",

            "...The same could've been true for his opponent,\x01",
            "to be fair.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(280, 280, -1, -1)
    SetChrName("Hushed Voice")

    AnonymousTalk(    #124
        (
            "\x07\x0CY-Yeah. You're right... It was still a damn good\x01",
            "game, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0xEA, 0x1, 0x0)
    Sleep(1000)
    SetMessageWindowPos(350, 310, -1, -1)
    SetChrName("Halle")

    AnonymousTalk(    #125
        "\x07\x00Looks like we're the center of attention now.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x4, 0x0, 0x0, 0x200, 0x200, 0xFF92, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS565._CH")
    OP_C6(0x4, 0x4, 0, 0, 0)
    OP_C6(0x4, 0x3, -1, 500, 0)
    Sleep(800)
    OP_C6(0x2, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(30, 270, -1, -1)
    SetChrName("Jack")

    AnonymousTalk(    #126
        (
            "\x07\x00I'd say we entertained the bar enough, at least.\x02\x03",

            "Can't say I'm thrilled with losing, but that's\x01",
            "the first time in a while I felt the rush of a\x01",
            "good gamble.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 310, -1, -1)
    SetChrName("Halle")

    AnonymousTalk(    #127
        (
            "\x07\x00I'll say! That was a great game to watch.\x01",
            "I'm itching to play some poker, myself.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x2, 0x0, 0x0, 0x200, 0x200, 0xFF92, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS560._CH")
    OP_C6(0x2, 0x4, 0, 0, 0)
    OP_C6(0x2, 0x3, -1, 500, 0)
    Sleep(800)
    OP_C6(0x4, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(30, 270, -1, -1)
    SetChrName("Jack")

    AnonymousTalk(    #128
        (
            "\x07\x00Anyway...\x02\x03",

            "...if you ever feel like it, come on back,\x01",
            "I guess. I'll try and make time for you if\x01",
            "you do.\x02\x03",

            "But just so we're clear: you haven't seen\x01",
            "half of what I can really do yet.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x3, 0x0, 0x0, 0x200, 0x200, 0x6E, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS551._CH")
    OP_C6(0x3, 0x4, 0, 0, 0)
    OP_C6(0x3, 0x3, -1, 500, 0)
    Sleep(800)
    OP_C6(0x1, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(350, 310, -1, -1)
    SetChrName("Halle")

    AnonymousTalk(    #129
        (
            "\x07\x00You say that, Jack...\x02\x03",

            "...but for all you know, it's gonna be\x01",
            "you getting beaten next time, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(30, 270, -1, -1)
    SetChrName("Jack")

    AnonymousTalk(    #130
        "\x07\x00Heh. We'll see about that.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x1, 0x0, 0x0, 0x200, 0x200, 0x6E, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS557._CH")
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(800)
    OP_C6(0x3, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(350, 310, -1, -1)
    SetChrName("Halle")

    AnonymousTalk(    #131
        (
            "\x07\x00Still, I feel the exact same way as he does.\x02\x03",

            "You're always welcome back here. I'd love\x01",
            "to play you again, personally.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x3, 0x0, 0x0, 0x200, 0x200, 0x6E, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS550._CH")
    OP_C6(0x3, 0x4, 0, 0, 0)
    OP_C6(0x3, 0x3, -1, 500, 0)
    Sleep(800)
    OP_C6(0x1, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(30, 270, -1, -1)
    SetChrName("Jack")

    AnonymousTalk(    #132
        (
            "\x07\x00You better come back at least ONCE, though, got it?\x01",
            "I need a chance to get my own victory against you in\x01",
            "now you've got one on me.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_23(0xEA)
    OP_C6(0x0, 0x3, 16777215, 5000, 0)
    FadeToDark(5000, 16777215, -1)
    OP_0D()
    Sleep(1500)
    SetMessageWindowPos(350, 310, -1, -1)
    SetChrName("Halle")

    AnonymousTalk(    #133
        (
            "\x07\x00Oh, that's all for today? That's a shame...\x02\x03",

            "Well, come back again some time, all right?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_C4(0x1, 0x20000000)
    OP_C6(0x3, 0x3, 16777215, 2000, 0)
    OP_C6(0x2, 0x3, 16777215, 2000, 0)
    Sleep(2000)
    OP_20(0xFA0)
    FadeToBright(3000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_21()
    Sleep(1000)
    OP_F7(0xB, 0x4, 0x0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #134
        "\x07\x00Side Story [The Casino -Gambler Jack-] finished!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_E3(0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7650")
    Sleep(1000)
    OP_28(0x20, 0x4, 0x10)
    OP_28(0x20, 0x4, 0x20)
    OP_3E(0x163, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #135
        "\x07\x05Received \x1F\x63\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    AddMira(10000)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #136
        "\x07\x05Received \x07\x0210,000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_7650")

    OP_A2(0x2505)
    NewScene("ED6_DT21/M7203   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_11_48F3 end

    def Function_12_765D(): pass

    label("Function_12_765D")

    Return()

    # Function_12_765D end

    def Function_13_765E(): pass

    label("Function_13_765E")

    OP_24(0x1C3, 0x5A)
    Sleep(200)
    OP_24(0x1C3, 0x50)
    Sleep(200)
    OP_24(0x1C3, 0x46)
    Sleep(200)
    OP_24(0x1C3, 0x3C)
    Sleep(200)
    OP_24(0x1C3, 0x32)
    Sleep(200)
    OP_24(0x1C3, 0x28)
    Sleep(200)
    OP_24(0x1C3, 0x1E)
    Sleep(200)
    OP_24(0x1C3, 0x14)
    Sleep(200)
    OP_24(0x1C3, 0xA)
    Sleep(200)
    OP_24(0x1C3, 0x0)
    OP_23(0x1C3)
    Return()

    # Function_13_765E end

    def Function_14_76B7(): pass

    label("Function_14_76B7")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_1D(0x64)
    OP_C4(0x0, 0x800)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(3000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #137
        (
            "\x07\x00The night sky was full of stars that looked as\x01",
            "though they would fall at any moment.\x02\x01",

            "The night breeze blew, the trees rustled, and\x01",
            "then all of a sudden a single shooting star\x01",
            "flew across the night sky.\x02\x01",

            "That star was full of seven-colored light, and\x01",
            "almost looked like a tear shed by the Goddess\x01",
            "herself.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #138
        (
            "\x07\x00...But then, something even more strange happened.\x02\x01",

            "The star suddenly flashed, as if it was going to\x01",
            "disappear, but instead...\x02\x01",

            "...it split out into numerous other lines of light\x01",
            "which made their way down to the earth.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #139
        (
            "\x07\x00That number was sixteen, and those sixteen\x01",
            "lines of light descended upon sixteen people.\x02\x01",

            "Most unbelievably of all, those seven-colored\x01",
            "lights surrounded the sixteen, and spoke to \x01",
            "each of them.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #140
        (
            "\x07\x05'Child of Man... Child of Man, can you hear my \x01",
            "voice?'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #141
        (
            "\x07\x05'I shall give unto you a challenge... Tour the\x01",
            "kingdom once, and then visit the capital...'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #142
        (
            "\x07\x05'Follow the web of feelings that join the many\x01",
            "peoples of this world together.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #143
        "\x07\x05Child of Man... Child of Man...'\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #144
        (
            "\x07\x05'If you can achieve what I ask of you, you shall\x01",
            "be granted my blessings...'\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_56(0x0)
    OP_C4(0x1, 0x800)
    FadeToDark(300, 0, -1)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CE(0x5, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x19, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x2504)
    NewScene("ED6_DT21/E1000   ._SN", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_76B7 end

    def Function_15_7B93(): pass

    label("Function_15_7B93")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BAB")

    label("loc_7BAB")

    Sleep(1000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/U5110   ._SN", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_15_7B93 end

    def Function_16_7BBD(): pass

    label("Function_16_7BBD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x20000000)
    OP_C4(0x0, 0x800)
    Sleep(3500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #145
        (
            "\x07\x00#2S#80WEnclosed is a report on the damage dealt to the former \x01",
            "Principality of North Ambria by the Salt Pale.#20W\x02\x01",

            "　#80WAlso contained within is research on the pale itself.#20W\x02\x01",

            "#80WHoly City of Arteria - Congregation for the Sacraments#20W\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_1D(0x6E)
    Sleep(1500)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS328._CH")
    OP_C5(0x1, 0x0, 0x0, 0x14, 0x19, 0x267, 0x1C2, 0x100, 0x100, 0x0, 0x0, 0x28, 0x32, 0xFFFFFF, 0x0, "C_VIS349._CH")
    OP_C6(0x0, 0x3, -1, 2000, 0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    Sleep(3500)
    OP_43(0x0, 0x0, 0x0, 0x12)
    OP_56(0x2)
    OP_44(0x0, 0x0)
    OP_A2(0x0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_22(0x12, 0x0, 0x64)
    OP_C6(0x0, 0x3, -7829368, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #146
        (
            "\x07\x00#2SI hereby present this report to you, Your Holiness,\x01",
            "ever at the side of the Goddess#150W...#20W\x02\x01",

            "This report contains classified information and\x01",
            "may only be read by those with the clearance to\x01",
            "do so.\x02\x01",

            "Certain sections of the utmost secrecy have also\x01",
            "been blacked out.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    OP_22(0x12, 0x0, 0x64)
    Sleep(1000)
    OP_C7(0x1, 0x0, 0x0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #147
        "\x07\x00#2SProgression of events after the pale's appearance:\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)

    AnonymousTalk(    #148
        (
            "\x07\x00#2S\x01",
            "#150WJuly 1st, 1178, 5:45AM――#20W\x02\x01",

            "An urgent report came in from Haliask Cathedral in\x01",
            "the then-principality (now a state) of North Ambria\x01",
            "in northern Zemuria.\x02\x01",

            "It stated that a giant white pillar 'so tall it appears to\x01",
            "kiss the clouds' had appeared on the outskirts of the\x01",
            "city.\x02\x01",

            "Bishop Alexei, the one who sent the report, behaved\x01",
            "as if extremely unsettled by what was happening.\x02\x01",

            "By urgent order of the committee, two knights of the\x01",
            "Gralsritter (the Eighth Dominion a.k.a the Roaring Lion\x01",
            "and a squire), both of whom were working on another\x01",
            "mission in a nearby nation, were dispatched to perform\x01",
            "a formal investigation.#20W\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #149
        (
            "\x07\x00#2SThey hurried to the scene via the eighth Merkabah unit.\x01",
            "Please note that the Merkabahs had only recently been\x01",
            "put into use at this point.\x02\x01",

            "They arrived promptly...\x02\x01",

            "and at 6:22AM, this was what they saw#150W...#20W\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A3(0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS331._CH")
    OP_C6(0x0, 0x3, -1, 1000, 0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_22(0x12, 0x0, 0x64)
    Sleep(2000)
    SetMessageWindowPos(-1, 416, 52, 2)
    SetChrName("")

    AnonymousTalk(    #150
        "\x07\x00#2SEnclosed is a photograph the object now known as the Salt Pale.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetMessageWindowPos(-1, 416, 52, 2)

    AnonymousTalk(    #151
        (
            "\x07\x00#2SAt this point, however, it was far larger than the term 'pale' would\x01",
            "suggest.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 416, 52, 2)

    AnonymousTalk(    #152
        (
            "\x07\x00#2SIt was more akin to a massive tower that soared hundreds of arge\x01",
            "into the air.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 416, 52, 2)

    AnonymousTalk(    #153
        (
            "\x07\x00#2SThe two knights provided the following observation regarding\x01",
            "the situation on their arrival:\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 416, 52, 2)

    AnonymousTalk(    #154
        (
            "\x07\x00#2S'We were met with a mighty hailstorm blowing in our direction\x01",
            "from Haliask--or so it appeared at first, till we eventually realized\x01",
            "the storm contained not ice, but salt.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 416, 52, 2)

    AnonymousTalk(    #155
        (
            "\x07\x00#2S'The object's surface is completely covered with salt, making it\x01",
            "impossible to tell what it may actually look like underneath.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 416, 52, 2)

    AnonymousTalk(    #156
        (
            "\x07\x00#2S'The surrounding air has become powdered salt, and it falls to\x01",
            "the ground like snow falling on a tundra.'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    OP_22(0x12, 0x0, 0x64)
    Sleep(1000)
    OP_C7(0x1, 0x0, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #157
        (
            "\x07\x00#2SThe spread of that salinification process was startlingly\x01",
            "rapid, and the affected area spread in the blink of an eye.\x02\x01",

            "By the time the Gralsritter arrived, the entire landscape\x01",
            "of the capital had turned to salt, and the lives of many\x01",
            "who lived there, like the aforementioned Bishop Alexei,\x01",
            "had already been lost.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #158
        (
            "\x07\x00#2SYet the the spread did not stop there.\x02\x03",

            "A day after the Salt Pale first appeared, a vast coniferous\x01",
            "forest zone north of the capital crystallized and collapsed.\x02\x01",

            "Bridges also collapsed, rendering all of the main highways\x01",
            "out of the city unusable.\x02\x01",

            "Please note that by this point, then-ruler Prince Balmund\x01",
            "had already fled the country to a nearby nation.\x02\x01",

            "Two days passed since the pale's appearance...\x02\x01",

            "By this point, roughly half of the entire principality had\x01",
            "become a sea of salt.\x02\x01",

            "Countless refugees had fled to the southern side of the\x01",
            "country because the River Greve stood between it and the\x01",
            "affected area.\x02\x01",

            "Finally, three days after the pale's appearance...\x02\x01",

            "The salinification process stopped at dawn. As a result,\x01",
            "the knights were able to advance on the capital of Haliask\x01",
            "with the hope of investigating the Salt Pale.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #159
        (
            "\x07\x00#2SThat afternoon, they finally reached it...\x02\x01",

            "but what they found looked completely different from\x01",
            "how the pale had before when they first arrived in North\x01",
            "Ambria.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A3(0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS330._CH")
    OP_C6(0x0, 0x3, -1, 1000, 0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_22(0x12, 0x0, 0x64)
    Sleep(2500)
    OP_43(0x0, 0x0, 0x0, 0x12)
    OP_56(0x2)
    OP_44(0x0, 0x0)
    OP_A2(0x0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x0, 0x3, -7829368, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #160
        (
            "\x07\x00#2SIn the center of the salinified area, they found an\x01",
            "object that was a mere 2.5 arge in height.\x02\x01",

            "Its surface was no longer blanketed in salt. Rather,\x01",
            "it looked as if something had been carved out of it.\x02\x01",

            "It is now believed that the pale's mass decreased\x01",
            "as the salinification process progressed.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #161
        (
            "\x07\x00#2SIn its smaller state, the pale had lost its power to\x01",
            "turn swathes of the country to salt, but its ability\x01",
            "to salinify was still very much intact.\x02\x01",

            "Anything that touched it, even for a millisecond,\x01",
            "was instantaneously turned into salt. It was of the\x01",
            "utmost importance to handle it with care.\x02\x01",

            "In order to complete the mission without physical\x01",
            "contact, the Gralsritter required the of use the\x01",
            "sacred tool Gleipnir, which was delivered to them\x01",
            "from the High Seat in Arteria.\x02\x01",

            "Since then, it has been kept closely sealed away\x01",
            "deep within the High Seat in Arteria.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    OP_22(0x12, 0x0, 0x64)
    Sleep(1000)
    OP_C7(0x1, 0x0, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #162
        (
            "\x07\x00#2SStill, while the recovery mission was ultimately\x01",
            "deemed a success, the damage already caused was\x01",
            "equally vast and significant.\x02\x01",

            "No damage to the surrounding nations was reported,\x01",
            "but it resulted in the destruction of three of the five\x01",
            "administrative districts of the principality, including\x01",
            "its capital.\x02\x01",

            "Over a third of the total population, along with\x01",
            "travelers from elsewhere, lost their lives.\x02\x01",

            "This is to say nothing of the emotional damage\x01",
            "caused; due to its sudden outbreak, the hearts of\x01",
            "North Ambria's people were overwhelmed with fear\x01",
            "and uncertainty.\x02\x01",

            "From a humanitarian and a religious perspective,\x01",
            "a swift response from the Septian Church was all\x01",
            "but necessary.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #163
        (
            "\x07\x00#2SThe decision was made to dispatch personnel to\x01",
            "the region right away...\x02\x01",

            "and upon arrival, they set about rebuilding the\x01",
            "damaged churches and healing of both the physical\x01",
            "and mental wounds of the people.\x02\x01",

            "Those who were left orphaned in the crisis were\x01",
            "taken into gospel facilities, where they would be\x01",
            "cared for until adulthood.\x02\x01",

            "The northern region of the country, which had\x01",
            "been turned entirely to salt, was placed under the\x01",
            "church's control. It has been a restricted area \x01",
            "ever since.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    OP_A3(0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS352._CH")
    OP_C6(0x0, 0x3, -1, 3000, 0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    Sleep(2500)
    OP_43(0x0, 0x0, 0x0, 0x12)
    OP_56(0x2)
    OP_44(0x0, 0x0)
    OP_A2(0x0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x0, 0x3, -7829368, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #164
        (
            "\x07\x00#2SSupplementary Notes:\x02\x01",

            "After some time, the country's former leader,\x01",
            "Prince Balmunt, attempted to rebuild the \x01",
            "government...\x02\x01",

            "but given that he had fled the country during\x01",
            "its hour of need, caring only for himself and not\x01",
            "his people, all authority he once had was gone.\x02\x01",

            "The following year, the country's people led an\x01",
            "armed uprising, and the Principality of North\x01",
            "Ambria was no more.\x02\x01",

            "Eventually elections were held, and the country\x01",
            "became a democracy, thus bringing about the\x01",
            "birth of the autonomous state we know of now.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #165
        (
            "\x07\x00#2SThis was also when the former principality's\x01",
            "armed forces reformed as a vigilante corps.\x02\x01",

            "Given the extreme poverty of the state, however,\x01",
            "the majority of said corps considered gathering\x01",
            "foreign currency to be of the utmost importance.\x02\x01",

            "This was how the large-scale jaeger corps known\x01",
            "as the Northern Jaegers was first established.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    OP_AE(0x96)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    Sleep(1000)
    OP_C7(0x1, 0x0, 0x0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #166
        (
            "\x07\x00#2SAs far as the rest of Zemuria is concerned,\x01",
            "this is where the tale of the Salt Pale ends...\x02\x01",

            "but a number of very important questions still\x01",
            "remain unanswered.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #167
        (
            "\x07\x00#2SPerhaps the most obvious of these is where it\x01",
            "came from.\x02\x01",

            "Despite the considerable size of the object and\x01",
            "that it appeared on the outskirts of a populated\x01",
            "city, no information is available regarding the\x01",
            "moment it first appeared.\x02\x01",

            "The most popular theory is that its appearance was\x01",
            "due to something akin to spatial translocation, \x01",
            "but no hard evidence exists to support this--or any\x01",
            "other--theory.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #168
        (
            "\x07\x00#2SOf more importance, however, is its positioning in\x01",
            "the teachings of the Septian Church.\x02\x01",

            "The pale is clearly different in nature to artifacts,\x01",
            "and appears to be a more fundamental\x01",
            "'manifestation of the Goddess' powers of creation'\x01",
            "(committee report).\x02\x01",

            "With the limits of our knowledge at present, this is\x01",
            "as far as we can get to the truth.\x02\x01",

            "There are some who have proposed it may be one\x01",
            "of the Sept-Terrions, but no evidence has been\x01",
            "found in legend or scripture to support this belief.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #169
        (
            "\x07\x00#2SNevertheless, these questions and many others need\x01",
            "answering, and the Congregation for the Sacraments\x01",
            "continues to study the Salt Pale to this day.\x02\x01",

            "The most accepted proposal comes from those who\x01",
            "believe the pale should be seen as nothing more than\x01",
            "a gift from Aidios, and they continue to consider\x01",
            "various means for Her church to make good use of it.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A3(0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS329._CH")
    OP_C6(0x0, 0x3, -1, 1000, 0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_22(0x12, 0x0, 0x64)
    Sleep(2500)
    OP_43(0x0, 0x0, 0x0, 0x12)
    OP_56(0x2)
    OP_44(0x0, 0x0)
    OP_A2(0x0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x0, 0x3, -7829368, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #170
        (
            "\x07\x00#2SThe most realistic of these plans is using it in the\x01",
            "manufacture of a sacred tool used for execution.\x02\x01",

            "Parts of the pale are cut away using high-pressure\x01",
            "water and then surrounded with a cylinder made\x01",
            "from salt crystal, allowing them to be fired directly\x01",
            "into the target without requiring the user to make\x01",
            "direct contact. \x02\x01",

            "Should the bolt make successfully contact with a\x01",
            "human target, their whole body would turn to salt,\x01",
            "killing them in mere seconds.\x02\x01",

            "There are no known means for reversing or stopping\x01",
            "the process.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #171
        (
            "\x07\x00#2SThis approach does not come without flaws; it seems\x01",
            "unwise to be careless with an object we still do not\x01",
            "understand the true nature of, for one thing.\x01",
            "There are also humanitarian concerns with executing\x01",
            "someone in this manner.\x02\x01",

            "Still, it does bear mentioning that should there ever\x01",
            "be a case where a target needs to be eliminated\x01",
            "without fail, this would be the most surefire way to\x01",
            "carry it out.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #172
        (
            "\x07\x00#2SIt should go without saying that research on it is\x01",
            "intended to continue into the future.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 4000, 0)
    OP_22(0x12, 0x0, 0x64)
    OP_20(0xFA0)
    OP_21()
    OP_C7(0x1, 0x0, 0x0)
    Sleep(800)

    AnonymousTalk(    #173
        (
            "\x07\x00#2SAppendix regarding the aforementioned sacred tool:\x02\x01",

            "S****/** - Trial use begins of the sacred tool\x01",
            "(top-secret work only).\x02\x01",

            "S****/** - Permission granted to use in the\x01",
            "execution of *********.\x02\x01",

            "S****/** - Used in the execution of ********* \x01",
            "(fired from bowgun).\x02\x01",

            "Results were extremely favorable. No damage was\x01",
            "caused to the surrounding area.\x02\x01",

            "The target was also successfully erased.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_56(0x0)
    OP_59()

    AnonymousTalk(    #174
        (
            "\x07\x00#2SAppendix: About the target:\x02\x01",

            "The target, ***** *********, was orphaned by the\x01",
            "Salt Pale when it first appeared.\x02\x01",

            "A brief history of *** is as follows:\x02\x01",

            "S1180 - Joins the Septian Church.\x02\x01",

            "S1185 - Joins the Congregation for the Sacraments\x01",
            "as an official.\x02\x01",

            "S1190 - Promoted to bishop.\x02\x01",

            "S1195 - Declared a heretic and excommunicated from\x01",
            "the church.\x02",
        )
    )

    CloseMessageWindow()
    OP_C4(0x1, 0x20000000)
    Sleep(2000)
    OP_56(0x0)
    OP_59()
    Sleep(2000)
    OP_F7(0x9, 0x2, 0x0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #175
        "\x07\x00Side Story [The Salt Pale] finished!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_C4(0x1, 0x800)
    OP_C7(0x1, 0xFF, 0x0)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x13, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A72D")
    Sleep(1000)
    OP_28(0x13, 0x4, 0x10)
    OP_28(0x13, 0x4, 0x20)
    OP_3E(0x27F, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #176
        "\x07\x05Received \x1F\x7F\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    AddMira(3500)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #177
        "\x07\x05Received \x07\x023,500 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_A72D")

    OP_A2(0x2506)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_A743")
    NewScene("ED6_DT21/U4134   ._SN", 112, 0, 0)
    IdleLoop()
    Jump("loc_A74C")

    label("loc_A743")

    NewScene("ED6_DT21/U4131   ._SN", 112, 0, 0)
    IdleLoop()

    label("loc_A74C")

    Return()

    # Function_16_7BBD end

    def Function_17_A74D(): pass

    label("Function_17_A74D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x20000000)
    OP_C4(0x0, 0x800)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS332._CH")
    OP_C5(0x1, 0x0, 0x0, 0x14, 0x19, 0x267, 0x1C2, 0x100, 0x100, 0x0, 0x0, 0x28, 0x32, 0xFFFFFF, 0x0, "C_VIS349._CH")
    OP_1D(0x6E)
    Sleep(2000)
    OP_C6(0x0, 0x3, -1, 4000, 0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    Sleep(4000)
    OP_43(0x0, 0x0, 0x0, 0x12)
    OP_56(0x2)
    OP_44(0x0, 0x0)
    OP_A2(0x0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x0, 0x3, -7829368, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #178
        (
            "\x07\x00#2S#80WAn Investigative Report on Phantom Thief B\x02\x01",

            "His Crimes, His History, and His True Identity#20W\x02\x01",

            "#80WImperial Chronicle Investigative Team#20W\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    OP_22(0x12, 0x0, 0x64)
    Sleep(1000)
    OP_C7(0x1, 0x0, 0x0)
    OP_A3(0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS333._CH")
    OP_C6(0x0, 0x3, -1, 2000, 0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    Sleep(3500)
    OP_43(0x0, 0x0, 0x0, 0x12)
    OP_56(0x2)
    OP_44(0x0, 0x0)
    OP_A2(0x0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x0, 0x3, -7829368, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #179
        (
            "\x07\x00Phantom Thief B has had quite the lengthy and\x01",
            "productive career in thievery in the Empire, \x01",
            "as the amount of records we have been able to\x01",
            "find on his crimes proves beyond a doubt.\x02\x01",

            "From numerous paintings held in the Imperial Art \x01",
            "Gallery...\x02\x01",

            "to a septium crystal held in the Empire's customs \x01",
            "warehouse...\x02\x01",

            "to even a cutting-edge tank held in an\x01",
            "Imperial Army research facility...\x02\x01",

            "Nothing is truly safe when he desires to steal it.\x02\x01",

            "His conquests aren't limited to inanimate objects;\x01",
            "he has been guilty of pretending to be a military\x01",
            "officer and eloping with the wife of a marquis on\x01",
            "one reported occasion.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #180
        (
            "\x07\x00Yet--and this is perhaps the most baffling part--\x01",
            "there is no concrete evidence to suggest he has\x01",
            "profited from his exploits. \x02\x01",

            "Rather, the objects stolen usually end up in places\x01",
            "so bizarre, their owners are liable to faint upon\x01",
            "hearing about them.\x02\x01",

            "In other cases, they are transformed into mira\x01",
            "which is then rained down from the sky in areas\x01",
            "largely inhabited by those less fortunate.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #181
        (
            "\x07\x00Hearing this, one might be led to think him\x01",
            "a vigilante thief who takes from the rich and\x01",
            "giving to the poor.\x02\x01",

            "But make no mistake, the truth is not so simple.\x02\x01",

            "The wife of the marquis discussed earlier is a\x01",
            "fine example of that.\x02\x01",

            "As of this writing, it has been a little over half a\x01",
            "year since the elopement took place. Since then,\x01",
            "she has remained unaccounted for.\x02\x01",

            "Many of the items stolen by him may return to\x01",
            "the public eye in some fashion, but not all.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #182
        (
            "\x07\x00Between his eccentric techniques and bizarre behavior\x01",
            "regarding the objects he steals, it might appear as\x01",
            "though his thefts are purely whims and nothing else.\x02\x01",

            "Upon studying the overall picture and reviewing the\x01",
            "objects--and indeed, people--in play, you begin to\x01",
            "see that they all have one specific thing in common.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    OP_22(0x12, 0x0, 0x64)
    Sleep(1000)
    OP_C7(0x1, 0x0, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #183
        (
            "\x07\x00Take the artworks stolen from the Imperial Art Gallery,\x01",
            "for example. Each of them were works of pure genius,\x01",
            "painted by a master of their craft...\x02\x01",

            "but they gained a reputation for being too complex\x01",
            "for the target audience of such works--the nobility--\x01",
            "and were shamefully stored away instead of placed on\x01",
            "display.\x02\x01",

            "Similar could be said of the septium crystal. Known for\x01",
            "its unparalleled beauty, after being seized by customs,\x01",
            "it was sealed away in the warehouse and doomed never\x01",
            "to be admired by human eyes again.\x02\x01",

            "The tank, again, is one more example, with its promising\x01",
            "development cut short. Rather than be put to good use,\x01",
            "it was left collecting dust.\x02\x03",

            "As an aside, the case of the marquis' wife does contain\x01",
            "some striking similarities.\x02\x01",

            "Despite marrying her, he devoted most of his attention\x01",
            "to his concubines and barely spared a thought for her.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #184
        (
            "\x07\x00In conclusion, we can see now that the underlying motive\x01",
            "for his actions is finding objects of beauty that have been\x01",
            "abandoned by the world and freeing them from their foolish\x01",
            "owners.\x02\x01",

            "No matter how the world may see his crimes,\x01",
            "his motive is clear.\x02\x01",

            "The truth of that is evident in the cards he leaves\x01",
            "before committing his crimes.\x02\x01",

            "This is the so-called 'liberation of beauty' mentioned\x01",
            "upon each of them.\x02\x01",

            "Phantom Thief B steals not for money, but for an\x01",
            "ideal he believes in.\x02\x01",

            "...And it is in this fact, we believe, are clues to his\x01",
            "true identity.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A3(0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS334._CH")
    OP_C6(0x0, 0x3, -1, 2000, 0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    Sleep(3500)
    OP_43(0x0, 0x0, 0x0, 0x12)
    OP_56(0x2)
    OP_44(0x0, 0x0)
    OP_A2(0x0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x0, 0x3, -7829368, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #185
        (
            "\x07\x00A number of valid theories have come about on\x01",
            "the face behind our famed thief...\x02\x01",

            "Unfortunately, they are all as lacking in conclusive\x01",
            "proof as they are numerous, and so it is impossible\x01",
            "to say whether any of them are actually correct.\x02\x01",

            "To complicate matters further, we now even have\x01",
            "deranged individuals coming forward pretending to\x01",
            "be him and allowing themselves to be captured by\x01",
            "law enforcement.\x02\x01",

            "That is not to say, however, that none of the\x01",
            "theories circulating are at all plausible.\x02\x01",

            "Here, we will introduce three such theories which\x01",
            "have developed significant followings...and may not\x01",
            "turn out to be too far from the truth.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #186
        "\x07\x00[Theory 1 - Amorous Con Artist X]\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #187
        (
            "\x07\x00[X's Personal History]\x02\x01",

            "X is known for his exceptional skill as a con artist,\x01",
            "having faked his own identity in order to engage in\x01",
            "romantic relationships with many noblewomen.\x02\x01",

            "He was as handsome as he was capable, and he was\x01",
            "exceptionally proud in nature as well.\x02\x01",

            "Born to a poor family in the temperate south, he\x01",
            "became used to stealing in order to make ends meet\x01",
            "from a young age.\x02\x01",

            "According to testimony from a companion of his at\x01",
            "the time, he was never once caught for such thefts.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #188
        (
            "\x07\x00The reason X converted from being a common thief\x01",
            "to a con artist is believed to have stemmed from\x01",
            "falling in love with a noblewoman of much higher\x01",
            "social standing than he.\x02\x01",

            "The rule of the aristocracy was absolute in the\x01",
            "country he called home, and blessed romances\x01",
            "between those of different classes unthinkable.\x02\x01",

            "With that in mind, he resolved to create a false\x01",
            "identity in order to make his dream possible.\x02\x01",

            "Following his first rousing success, he came to\x01",
            "do the same on a myriad of other occasions,\x01",
            "indulging in one forbidden affair after another.\x02\x01",

            "It was a mere ten years ago that he was arrested\x01",
            "on suspicion of identity fraud, but he performed\x01",
            "a miraculous escape from prison. Ever since then,\x01",
            "his whereabouts have remained unknown.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #189
        (
            "\x07\x00[Thoughts]\x02\x01",

            "Both X's peerless skills as a thief \x02",

            "and his interest\x01",
            "in forbidden romances with noblewomen \x02",

            "sound\x01",
            "remarkably like what we know of Phantom Thief B.\x02\x01",

            "Also worth noting is that despite using his abilities\x01",
            "of deception to court those of vast wealth,\x01",
            "he displayed virtually no interest in their fortunes.\x02\x01",

            "That is to say, he gained no financial benefit from\x01",
            "his actions whatsoever.\x02\x01",

            "Instead, he simply lamented that he was unable to\x01",
            "indulge in them because of something as trivial as\x01",
            "his social class.\x02\x01",

            "We conclude that this attitude bears a striking\x01",
            "resemblance to the thief's own views on beauty.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #190
        "\x07\x00[Theory 2 - Tragic Artist Y]\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #191
        (
            "\x07\x00[Y's Personal History]\x02\x01",

            "Y was an artist with a rather tragic past.\x02\x01",

            "Born to a middle-class family in the north, he was\x01",
            "hired by an influential aristocrat to be their personal\x01",
            "artist, producing many a stunning piece of work.\x02\x01",

            "However, it was later discovered that wasn't all he\x01",
            "produced; on the contrary, he was also responsible\x01",
            "for a number of counterfeit pieces.\x02\x01",

            "The one who hired him sought to profit through ill\x01",
            "means thanks to his work, and so he created such\x01",
            "counterfeits under the noble's instructions.\x02\x01",

            "One day, however, Y suddenly left the noble's \x01",
            "service.\x02\x01",

            "(The reason remains unknown.)\x02\x01",

            "This is where his tragedy begins.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #192
        (
            "\x07\x00Immediately after leaving his client behind...\x02\x01",

            "Y received a terrible piece of news: his lover,\x01",
            "the daughter of a respected family, had been\x01",
            "killed in a traffic accident.\x02\x01",

            "While there is no evidence to prove as much,\x01",
            "it is rumored that the noble may have had a\x01",
            "hand in her death.\x02\x01",

            "Y was only spotted once more at his lover's grave\x01",
            "before forever disappearing from the public eye.\x01",
            "To those who knew his story, he became known as\x01",
            "the truly tragic artist.\x02\x01",

            "Several years later, the noble was murdered.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #193
        (
            "\x07\x00[Thoughts]\x02\x01",

            "The story of Y still has several unsolved mysteries\x01",
            "surrounding it and has invited much speculation,\x01",
            "both of which have likely led to the theory that he\x01",
            "and Phantom Thief B are one and the same.\x02\x01",

            "Those aren't the only reasons, naturally.\x02\x01",

            "Phantom Thief B has been known, at times, to try\x01",
            "and dispose of counterfeits, believing them to be\x01",
            "'false beauty.'\x02\x01",

            "This has led some to believe that Phantom Thief B\x01",
            "may be attempting to rid the world of counterfeits\x01",
            "that he himself created.\x02\x01",

            "Lending further credibility to this is the discovery\x01",
            "that the forgeries disposed of by Phantom Thief B\x01",
            "were indeed the works of Y.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #194
        "\x07\x00[Theory 3 - Skilled Martial Artist Z]\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #195
        (
            "\x07\x00[Z's Personal History]\x02\x01",

            "The story of Z is significantly different from the\x01",
            "other two potential identities we have proposed\x01",
            "here, making this an unusual--but still plausible--\x01",
            "possibility.\x02\x01",

            "Z was born in the far East as the son of a famed\x01",
            "military family.\x02\x01",

            "He was an attractive, delicately-built young man,\x01",
            "but he was far more skilled at martial arts than\x01",
            "his frame would have suggested, being blessed\x01",
            "with great natural talent.\x02\x01",

            "He is also said to possess a keen, sharp mind, and\x01",
            "there was a mild air of arrogance about him, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #196
        (
            "\x07\x00Z was indeed blessed in nearly every way. He came\x01",
            "from an important family, he had skill, he had looks...\x02\x01",

            "and as a result, he came to feel bored with the world\x01",
            "around him.\x02\x01",

            "He hardly kept such thoughts to himself--in fact,\x01",
            "he often voiced his complaints to anyone within\x01",
            "earshot.\x02\x01",

            "These complaints persisted until one day, he simply\x01",
            "disappeared, telling no one where he was going and\x01",
            "leaving nothing to suggest his next destination.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #197
        (
            "\x07\x00[Thoughts]\x02\x01",

            "Much of this theory is based on the idea of geniuses\x01",
            "being eccentric by nature.\x02\x01",

            "There are some who say that the fighting style of Z\x01",
            "has some resemblance to the peculiar skills used by\x01",
            "Phantom Thief B...\x02\x01",

            "but in terms of credibility, this theory is barely a cut\x01",
            "above many other similarly unusual suggestions.\x02\x01",

            "Still, the idea that the man beneath the mask is one\x01",
            "from the East is certainly an interesting and exciting\x01",
            "one, leading many to wish it were true...even if they\x01",
            "find themselves doubting it actually is.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    OP_22(0x12, 0x0, 0x64)
    Sleep(1000)
    OP_C7(0x1, 0x0, 0x0)
    OP_20(0xBB8)
    OP_21()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #198
        (
            "\x07\x00That brings us to the end of outlining three very\x01",
            "different theories.\x02\x01",

            "Could X, Y, or Z be the true identity of our famed\x01",
            "phantom thief?\x02\x01",

            "Or is the truth perhaps something else entirely?\x02\x01",

            "The only way we will know for sure is to hear the\x01",
            "truth from the man himself.\x02\x01",

            "Of course, whether we can trust anything he says\x01",
            "is a discussion for another time.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #199
        (
            "\x07\x00[Postscript]\x02\x01",

            "After this article was first published, we received\x01",
            "a card believed to be from Phantom Thief B himself\x01",
            "at our office.\x02\x01",

            "The contents of the card are as follows:\x02\x01",

            "'The truth of my identity is already within your\x01",
            "grasp. My number reveals all.'\x02\x01",

            "Judging by this, it is believed that one of the three\x01",
            "theories proposed is the true identity of Phantom\x01",
            "Thief B.\x02\x01",

            "That said, uncovering the meaning behind his words\x01",
            "has proven to be a trying task.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #200
        (
            "\x07\x00Will one valued reader be able to step forward and\x01",
            "solve what we cannot? Only time will tell.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_C4(0x1, 0x20000000)
    Sleep(1000)
    OP_F7(0x9, 0xB, 0x0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #201
        "\x07\x00Side Story [Phantom Thief B Report] finished!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_C4(0x1, 0x800)
    OP_C7(0x1, 0xFF, 0x0)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D349")
    Sleep(1000)
    OP_28(0x14, 0x4, 0x10)
    OP_28(0x14, 0x4, 0x20)
    OP_3E(0x12E, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #202
        "\x07\x05Received \x1F\x2E\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    AddMira(10000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #203
        "\x07\x05Received \x07\x0210,000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_D349")

    OP_A2(0x2505)
    NewScene("ED6_DT21/M5610   ._SN", 130, 0, 0)
    IdleLoop()
    Return()

    # Function_17_A74D end

    def Function_18_D356(): pass

    label("Function_18_D356")

    OP_C6(0x1, 0x3, -1, 500, 0)
    OP_C6(0x1, 0x4, 0, 0, 0)
    Sleep(1000)

    label("loc_D379")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D3C1")
    Sleep(200)
    OP_C6(0x1, 0x3, 16777215, 500, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D3A5")
    Jump("loc_D3C1")

    label("loc_D3A5")

    Sleep(200)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(1000)
    Jump("loc_D379")

    label("loc_D3C1")

    Return()

    # Function_18_D356 end

    def Function_19_D3C2(): pass

    label("Function_19_D3C2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D3F6")
    OP_22(0x1A, 0x0, 0x64)
    Sleep(500)
    OP_22(0x1B, 0x0, 0x64)
    Sleep(500)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(500)
    OP_22(0x1C, 0x0, 0x64)
    Sleep(500)
    Jump("Function_19_D3C2")

    label("loc_D3F6")

    Return()

    # Function_19_D3C2 end

    SaveToFile()

Try(main)
