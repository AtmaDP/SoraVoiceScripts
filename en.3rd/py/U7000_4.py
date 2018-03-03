from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U7000_4 ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U7000.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60210",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/U7000   ._SN',
            '',
            '',
            '',
            '',
            '',
            'ED6_DT21/SUB000  ._SN',
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
        "Function_3_1035",         # 03, 3
        "Function_4_52AC",         # 04, 4
        "Function_5_52C6",         # 05, 5
        "Function_6_52E0",         # 06, 6
        "Function_7_52FA",         # 07, 7
        "Function_8_5314",         # 08, 8
        "Function_9_532E",         # 09, 9
        "Function_10_5348",        # 0A, 10
        "Function_11_5362",        # 0B, 11
        "Function_12_537C",        # 0C, 12
        "Function_13_5669",        # 0D, 13
        "Function_14_5994",        # 0E, 14
        "Function_15_5C9C",        # 0F, 15
        "Function_16_6182",        # 10, 16
        "Function_17_B36D",        # 11, 17
        "Function_18_B3AA",        # 12, 18
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    Return()

    # Function_1_AB end

    def Function_2_AC(): pass

    label("Function_2_AC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS450._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS451._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS452._CH")
    OP_C5(0x3, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS453._CH")
    OP_C5(0x4, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS454._CH")
    OP_C5(0x5, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS455._CH")
    Sleep(2000)
    OP_22(0xC3, 0x1, 0x64)
    Sleep(2000)
    OP_23(0xC3)
    OP_22(0x83, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0xAE)
    OP_C6(0x0, 0x3, -1, 2000, 0)
    Sleep(3000)
    SetMessageWindowPos(60, 240, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #0
        (
            "\x07\x0C#30WYou've reached the Emerose City church.\x01",
            "How may I help you?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(360, 120, -1, -1)
    SetChrName("Female Voice")

    AnonymousTalk(    #1
        (
            "\x07\x0C#30WOh, is that you, Kevin?\x02\x03",

            "I didn't think you'd be there already, so I was\x01",
            "just going to leave a message with the priest.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(60, 240, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #2
        (
            "\x07\x0C#30WOh. Hey, Rufina.\x02\x03",

            "Yeah, I got here late this morning.\x02\x03",

            "How about you? When do you think\x01",
            "you'll be getting here?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(360, 120, -1, -1)
    SetChrName("Rufina's Voice")

    AnonymousTalk(    #3
        (
            "\x07\x0C#30WI'm going to be a little late, I'm afraid...\x01",
            "There's been an accident or something,\x01",
            "so the train's been delayed.\x02\x03",

            "I probably won't be getting there until\x01",
            "this evening now.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(60, 240, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #4
        (
            "\x07\x0C#30WGot'cha. I'll wait here till you arrive.\x02\x03",

            "I think Ries and the kids would get all\x01",
            "bent outta shape if I showed up without\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(360, 120, -1, -1)
    SetChrName("Rufina's Voice")

    AnonymousTalk(    #5
        (
            "\x07\x0C#30WOh, please. I'm sure you're just exaggerating.\x02\x03",

            "Although speaking of Ries, I hope you've\x01",
            "been thinking about how you're going to\x01",
            "cheer her up.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(60, 240, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #6
        (
            "\x07\x0C#30WHaha. I've got it all planned out.\x02\x03",

            "I've been stocking up on souvenirs from\x01",
            "every mission I've been going on.\x02\x03",

            "Should be enough to snap her out of\x01",
            "her funk.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(360, 120, -1, -1)
    SetChrName("Rufina's Voice")

    AnonymousTalk(    #7
        (
            "\x07\x0C#30WHmm... I wouldn't be so sure if I were you...\x02\x03",

            "Girls her age are more complex than you\x01",
            "think.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(60, 240, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #8
        (
            "\x07\x0C#30WYeah?\x02\x03",

            "I guess she's not really a kid anymore\x01",
            "now that she's 13, but still...\x02\x03",

            "Actually, that's about how old you were\x01",
            "when we first met, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(360, 120, -1, -1)
    SetChrName("Rufina's Voice")

    AnonymousTalk(    #9
        (
            "\x07\x0C#30WHeehee. Now that you mention it, it was.\x01",
            "How time flies!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    OP_22(0x17D, 0x1, 0x64)
    Sleep(1600)
    SetMessageWindowPos(360, 120, -1, -1)
    SetChrName("Rufina's Voice")

    AnonymousTalk(    #10
        (
            "\x07\x0C#30WSorry! It looks like the train's about ready\x01",
            "to leave. I'm going to have to go.\x02\x03",

            "I'll see you later, then, all right?\x02\x03",

            "If you get bored of waiting, you're welcome\x01",
            "to go on home ahead of me, of course.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(60, 240, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #11
        "\x07\x0C#30WGot it. See you later.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    OP_23(0x17D)
    OP_22(0x83, 0x0, 0x64)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    Sleep(1500)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(60, 240, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #12
        (
            "\x07\x0C#30WMan, 'how time flies' is right. Have I really not\x01",
            "been home in two years?\x02\x03",

            "And I guess that makes...nine since I met Rufina.\x02\x03",

            "*sigh* I hope Ries isn't TOO grumpy when we\x01",
            "finally get there.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(360, 180, -1, -1)
    SetChrName("Male Voice")

    AnonymousTalk(    #13
        "\x07\x0C#30WK-Kevin!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x2, 0x3, -1, 1000, 0)
    Sleep(1500)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(60, 240, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #14
        (
            "\x07\x0C#30WWhat is it, Father?\x02\x03",

            "Has something bad happened?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(360, 180, -1, -1)
    SetChrName("Priest")

    AnonymousTalk(    #15
        (
            "\x07\x0C#30WW-Well...\x02\x03",

            "I've just received word that someone spotted\x01",
            "a group of men dressed in all black at the edge\x01",
            "of town.\x02\x03",

            "What's worse is, they were supposedly heading\x01",
            "for the mountain path...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x3, 0x3, -1, 500, 0)
    Sleep(1000)
    OP_C6(0x2, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(60, 240, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #16
        (
            "\x07\x0C#30W...?!\x02\x03",

            "Y-You don't think...?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(360, 180, -1, -1)
    SetChrName("Priest")

    AnonymousTalk(    #17
        (
            "\x07\x0C#30WIf they were, Aster House must be their target,\x01",
            "I fear...\x02\x03",

            "Do you have any idea what could be going on?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(60, 240, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #18
        (
            "\x07\x0C#30WI wish I did... I doubt it's anything to do with\x01",
            "the Gralsritter, at least.\x02\x03",

            "I think I should go and check it out just in case.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(360, 180, -1, -1)
    SetChrName("Priest")

    AnonymousTalk(    #19
        (
            "\x07\x0C#30WPlease do.\x02\x03",

            "Oh... Do you know when Rufina's going to be \x01",
            "arriving, by the way?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(60, 240, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #20
        (
            "\x07\x0C#30WThis evening, by the sound of it. She said her\x01",
            "train's been delayed.\x02\x03",

            "When she arrives, can you let her know what\x01",
            "happened?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x3, 0x3, 16777215, 1500, 0)
    Sleep(2500)
    OP_C6(0x4, 0x3, -1, 2000, 0)
    Sleep(3000)
    SetMessageWindowPos(340, 280, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #21
        (
            "\x07\x0C#30WDamn it... Jaegers?\x02\x03",

            "Seems like there's anywhere between five and\x01",
            "ten of them...\x02\x03",

            "But what could they want with a gospel facility\x01",
            "to begin with?\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0xD5, 0x0, 0x64)
    OP_C6(0x5, 0x3, -1, 500, 0)
    Sleep(1000)
    OP_C6(0x4, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(340, 280, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #22
        (
            "\x07\x0C#30W...The longer they're allowed to be in there,\x01",
            "the more danger the kids are in.\x02\x03",

            "I'm gonna have to try and handle this alone.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x5, 0x3, 16777215, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #23
        "\x07\x0C#40WIt's time to put my combat skills to good use!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x5, 0x3, 16777215, 1500, 0)
    Sleep(2000)
    OP_20(0x1388)
    OP_21()
    Sleep(1000)
    OP_AD(0x2400E8, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    OP_A2(0x2505)
    OP_A2(0x250A)
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_2_AC end

    def Function_3_1035(): pass

    label("Function_3_1035")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x26033B, 0x260340, 0x13)
    OP_D2(0x270080, 0x270084, 0x14)
    OP_D2(0x70598, 0x7059D, 0x15)
    LoadEffect(0x0, "map\\mp259_01.eff")
    ClearChrFlags(0x10F, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x22, 0, 4500, 1000, 180)
    SetChrChipByIndex(0x22, 21)
    SetChrSubChip(0x22, 0)
    SetChrFlags(0x22, 0x4)

    def lambda_10A7():

        label("loc_10A7")

        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        OP_48()
        Jump("loc_10A7")

    QueueWorkItem2(0x22, 3, lambda_10A7)
    OP_9F(0x22, 0xFF, 0xFF, 0xFF, 0xB4, 0x0)
    PlayEffect(0x0, 0x7, 0x22, 0, 800, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x10F, -100, 4000, -1600, 0)
    SetChrPos(0x101, -100, 4000, -3000, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x15, -1100, 4000, -3200, 0)
    SetChrPos(0x1F, 1300, 4000, -3100, 0)
    SetChrPos(0x11, 2400, 4000, -3170, 315)
    SetChrPos(0x12, 1300, 4000, -6500, 0)
    SetChrPos(0x13, 100, 4000, -6500, 0)
    SetChrPos(0x14, 2800, 4000, -5870, 0)
    SetChrPos(0x16, 800, 4000, -4300, 0)
    SetChrPos(0x18, -500, 4000, -4700, 0)
    SetChrPos(0x1E, -1520, 4000, -4800, 0)
    SetChrPos(0x1A, 2200, 4000, -4570, 0)
    SetChrPos(0x1B, 1450, 4000, -5600, 0)
    SetChrPos(0x1C, 3500, 4000, -4960, 315)
    SetChrPos(0x19, -1400, 4000, -6200, 0)
    SetChrFlags(0xF0, 0x80)
    SetChrFlags(0xF1, 0x80)
    OP_6D(-1100, 4000, -600, 0)
    OP_67(0, 4800, -10000, 0)
    OP_6B(2550, 0)
    OP_6C(315000, 0)
    OP_6E(350, 0)
    OP_E5(0x2, 0xFF, 0x13, 500)
    OP_1D(0xD2)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #24
        0x101,
        (
            "#1004F#6PCeleste?\x02\x03",

            "W-Wasn't that the name we saw in those data\x01",
            "crystals?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x15,
        (
            "#1505F#6PThat's right. According to those, she was the\x01",
            "de facto leader of the group of ancients who\x01",
            "sealed away the Aureole.\x02\x03",

            "#1500FShe was also the founder of Liberl's current\x01",
            "royal family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x22,
        (
            "\x07\x0C#1616F#11PHeehee...\x02\x03",

            "#1611FI'm glad to see the information I left behind\x01",
            "ended up proving useful to someone.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        "#1008F#6PI-It really did...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x16,
        (
            "#1163F#6PSo then you're really the founder of Liberl's\x01",
            "royal family?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x22,
        (
            "\x07\x0C#1616F#11PNot technically.\x02\x03",

            "#1610FI'm not the real Celeste D. Auslese; think of\x01",
            "me as something of a shadow.\x02\x03",

            "Or a partial copy her personality created in\x01",
            "order to influence Phantasma from within.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x16,
        "#1164F#6PHow can you only be a partial copy...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10F,
        (
            "#1446F#6PThe truth behind you is apparently more\x01",
            "complicated than we thought.\x02\x03",

            "#1448FYou don't appear to be a spirit of some kind,\x01",
            "though. I see that now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x22,
        (
            "\x07\x0C#1615F#11PThat is correct.\x02\x03",

            "#1610FBefore I try to explain just what I am...\x02\x03",

            "...I should probably tell you more about\x01",
            "what the world we are in is first.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x11,
        "#560F#6PYou can do that?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x1F,
        "#261F#6PHeehee. This should be interesting.\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_21()
    OP_1D(0xB7)
    OP_AD(0x24015C, 0x0, 0x0, 0xC8)
    Sleep(3000)
    SetMessageWindowPos(220, 50, -1, -1)
    SetChrName("Celeste")

    AnonymousTalk(    #35
        (
            "\x07\x0C#1615FAs you are aware, the land in which you stand is\x01",
            "called Phantasma.\x02\x03",

            "This is a world belonging to a higher plane of\x01",
            "existence, created several thousands of years ago\x01",
            "by the Aureole.\x02\x03",

            "#1612FIts purpose was to act as a subsystem for the \x01",
            "Aureole in order to incorporate and process the\x01",
            "will of the Liber Ark's populace.\x02\x03",

            "One might call it a self-organized world designed\x01",
            "to realize countless possible others as necessary.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 100, -1, -1)
    SetChrName("Ries")

    AnonymousTalk(    #36
        "\x07\x00#1444FErm... Pardon?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 150, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #37
        "\x07\x00#1019FYou've lost me.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 280, -1, -1)
    SetChrName("Anelace")

    AnonymousTalk(    #38
        (
            "\x07\x00#1317FY-Yeah... Isn't there a simpler way to explain\x01",
            "this?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(250, 50, -1, -1)
    SetChrName("Celeste")

    AnonymousTalk(    #39
        (
            "\x07\x0C#1615FHmm...\x02\x03",

            "#1610FWell, while not technically correct, perhaps you\x01",
            "could think of it this way.\x02\x03",

            "Phantasma is like a fictitious realm created by \x01",
            "the Aureole in order to fulfill humanity's every\x01",
            "wish and desire.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 150, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #40
        "\x07\x00#1016FThaaat's better...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Julia")

    AnonymousTalk(    #41
        (
            "\x07\x00#172FWhat, exactly, qualifies Phantasma as 'fictitious'?\x02\x03",

            "I can't help but think it far too real to be a land\x01",
            "of pure fantasy.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(250, 50, -1, -1)
    SetChrName("Celeste")

    AnonymousTalk(    #42
        (
            "\x07\x0C#1610FWhen I say a fictitious world, I don't mean to\x01",
            "suggest that Phantasma is a complete lie.\x02\x03",

            "#1616FIt's more like a shadowgraph or kaleidoscope.\x01",
            "It has its own laws and can change to reflect\x01",
            "countless different possibilities.\x02\x03",

            "#1611FDoes this make the concept any easier for you\x01",
            "to understand?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Julia")

    AnonymousTalk(    #43
        "\x07\x00#170FSomewhat, yes.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 250, -1, -1)
    SetChrName("Mueller")

    AnonymousTalk(    #44
        (
            "\x07\x00#278FAnd suddenly the name Phantasma seems that\x01",
            "much more appropriate.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(1500)

    ChrTalk(    #45
        0x22,
        (
            "\x07\x0C#1610F#11PAs I stated previously, it was a subsystem of the\x01",
            "Aureole rather than being the Aureole itself, and\x01",
            "it helped to grant people's desires.\x02\x03",

            "#1615FThey were separate entities, but effectively like\x01",
            "two sides of the same coin.\x02\x03",

            "#1612FThe relationship caught our eye as we were\x01",
            "devising the sealing mechanism.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x16,
        (
            "#1162F#6PYou mean the mechanism used to seal away the\x01",
            "Aureole?\x02\x03",

            "That was also in those data crystals left behind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x22,
        (
            "\x07\x0C#1615F#11PExactly.\x02\x03",

            "#1612FAt first, we thought our plan would be impossible\x01",
            "to execute.\x02\x03",

            "After all, the Aureole had absolute control over \x01",
            "space itself and was able to influence mankind's\x01",
            "every action.\x02\x03",

            "#1613FEven after coming upon the idea of temporally\x01",
            "freezing it and imprisoning it with a gravity\x01",
            "barrier, we had no way to implement our plans.\x02\x03",

            "Without that, they were simply ideas with no real\x01",
            "meaning.\x02\x03",

            "#1615FWe were effectively at a total loss.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x18,
        (
            "#1545F#6PYou had discovered your foe's weakness,\x01",
            "but had no way to take advantage of it.\x02\x03",

            "#1540FThat must have been quite the frustrating\x01",
            "predicament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x22,
        (
            "\x07\x0C#1616F#11PIndeed...\x02\x03",

            "#1610FAnd yet our perseverance rewarded us with\x01",
            "the development of something that could take\x01",
            "advantage of that weakness: the Recluse Cube.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x19, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Sleep(300)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 19)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #50
        0x10F,
        "#1443F#6PIs that what this is known as, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x22,
        (
            "\x07\x0C#1610F#11PYes. That is the only object in existence able to\x01",
            "interact with Phantasma without relying on the\x01",
            "Aureole as an intermediary.\x02\x03",

            "Celeste used that to create a partial copy of her\x01",
            "personality--that is, me--inside Phantasma.\x02\x03",

            "And once inside, I began working to sabotage\x01",
            "Phantasma's functionality by using this garden\x01",
            "as my base of operations.\x02\x03",

            "#1615FAs a result of my efforts, the Aureole's processing\x01",
            "ability was hindered just long enough for the plan\x01",
            "to be executed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x1F,
        "#263F#6PHmm...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #53
        0x19,
        (
            "#573F#6PHe who catches his foe off guard wins the battle.\x02\x01",

            "#070FThe same principle applies to martial arts, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x11,
        (
            "#560F#6PIt sounds like you really put a lot of thought\x01",
            "into planning everything...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x22,
        (
            "\x07\x0C#1611F#11PHeehee. Maybe, but I can't deny that luck\x01",
            "played a part in the end.\x02\x03",

            "#1616FOnce the Aureole was sealed away, my work\x01",
            "was done, and I fell into a deep sleep here.\x02\x03",

            "My reason being that if the Aureole were ever\x01",
            "unsealed, I might be able to provide assistance\x01",
            "to the people of that time.\x02\x03",

            "#1610FI'm pleased you've been able to handle it just\x01",
            "fine without my help, however.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        (
            "#1016F#6PA-Ahaha...\x02\x03",

            "#1008FLuck's played a huge part for us, too, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x15,
        (
            "#1505F#6PWe're not even sure where the Aureole is now.\x02\x03",

            "#1503FAs far as we're aware, it disappeared during all\x01",
            "that happened at the Liber Ark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x22,
        (
            "\x07\x0C#1613F#11PI thought as much...\x02\x03",

            "#1615FI was able to confirm the Aureole's disappearance\x01",
            "from here within Phantasma, too.\x02\x03",

            "When I did so, I thought my purpose for existing\x01",
            "was finally over...\x02\x03",

            "...and that all that was left for me and this land\x01",
            "was to embrace a slow and peaceful destruction.\x02\x03",

            "#1612FBut that was not to be.\x02\x03",

            "Soon, the Lord of Phantasma appeared.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x19, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #59
        0x16,
        "#1163F#6PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x10F,
        "#1443F#6PSo that's when it happened...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x1F,
        "#1306F#6PHeehee. Quite a recent development, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x22,
        (
            "\x07\x0C#1615F#11PThe Lord of Phantasma appeared out of nowhere,\x01",
            "stealing all of my power before I was even aware\x01",
            "what happened.\x02\x03",

            "After doing so, they began to remake Phantasma\x01",
            "in accordance to their own designs.\x02\x03",

            "#1612FBoth this world's current structure and the planes\x01",
            "that make it up...\x02\x03",

            "...were all the Lord of Phantasma's creations.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x1E,
        (
            "#115F#6PLooks like your theory was correct, Renne.\x02\x03",

            "#112FStill, that makes it sound like...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x1C,
        (
            "#055F#6PY-Yeah...\x02\x03",

            "So you don't know who that masked bastard is,\x01",
            "either, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x22,
        (
            "\x07\x0C#1615F#11PI'm afraid not.\x02\x03",

            "#1613FTheir every action thus far has been a mystery.\x02\x03",

            "Ordinarily, they should not have been able to gain\x01",
            "access to this world in the first place.\x02\x03",

            "#1612F...And I'm afraid I have no idea what they are trying\x01",
            "to achieve by bringing all of you in here and testing\x01",
            "you.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x1B,
        "#1525F#6PWell, that's a shame...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x14,
        (
            "#413F#6PYeah... That's the part we want to know\x01",
            "most of all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x22,
        (
            "\x07\x0C#1615F#11PI only wish I could be of more help.\x02\x03",

            "#1612FThe only other thing I can say about them\x01",
            "is that I suspect the Lord of Phantasma is\x01",
            "currently in the seventh plane.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x19, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #69
        0x10F,
        "#1444F#6PThere's a seventh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        "#1004F#6PWh-What makes you think that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x22,
        (
            "\x07\x0C#1612F#11PThat was the first plane they created after\x01",
            "appearing in this world.\x02\x03",

            "Just what kind of a place that plane is,\x01",
            "I don't know...\x02\x03",

            "#1615F...but I can sense dark, inhuman thoughts\x01",
            "from there, and they're spreading out across\x01",
            "the whole of Phantasma.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        "#1026F#6PThat doesn't sound good...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x11,
        (
            "#062F#6PThen we'll be seeing them after the next one,\x01",
            "won't we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x15,
        (
            "#1505F#6PYeah. We'd just finished the fifth when we came\x01",
            "back here.\x02\x03",

            "#1502FPresuming they're waiting for us on the seventh,\x01",
            "the time to fight them head on may not be that\x01",
            "far off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x1C,
        "#051F#6PHeh. I was gettin' tired of waiting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x18,
        (
            "#1545F#6PAs was I. It seems the end may finally be in sight.\x02\x03",

            "#1540FNow, if only we had some sort of inkling as to\x01",
            "what the Lord of Phantasma is trying to achieve...\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, 320, 4100, -14250, 0)
    SetChrChipByIndex(0x21, 20)
    SetChrSubChip(0x21, 0)

    NpcTalk(    #77
        0x21,
        "Young Man's Voice",
        "#2PActually, I just might.\x02",
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x19, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_3760():

        label("loc_3760")

        TurnDirection(0xFE, 0x21, 400)
        OP_48()
        Jump("loc_3760")

    QueueWorkItem2(0x10F, 3, lambda_3760)

    def lambda_3771():

        label("loc_3771")

        TurnDirection(0xFE, 0x21, 400)
        OP_48()
        Jump("loc_3771")

    QueueWorkItem2(0x101, 3, lambda_3771)

    def lambda_3782():

        label("loc_3782")

        TurnDirection(0xFE, 0x21, 400)
        OP_48()
        Jump("loc_3782")

    QueueWorkItem2(0x15, 3, lambda_3782)

    def lambda_3793():

        label("loc_3793")

        TurnDirection(0xFE, 0x21, 400)
        OP_48()
        Jump("loc_3793")

    QueueWorkItem2(0x11, 3, lambda_3793)

    def lambda_37A4():

        label("loc_37A4")

        TurnDirection(0xFE, 0x21, 400)
        OP_48()
        Jump("loc_37A4")

    QueueWorkItem2(0x19, 3, lambda_37A4)

    def lambda_37B5():

        label("loc_37B5")

        TurnDirection(0xFE, 0x21, 400)
        OP_48()
        Jump("loc_37B5")

    QueueWorkItem2(0x12, 3, lambda_37B5)

    def lambda_37C6():

        label("loc_37C6")

        TurnDirection(0xFE, 0x21, 400)
        OP_48()
        Jump("loc_37C6")

    QueueWorkItem2(0x16, 3, lambda_37C6)

    def lambda_37D7():

        label("loc_37D7")

        TurnDirection(0xFE, 0x21, 400)
        OP_48()
        Jump("loc_37D7")

    QueueWorkItem2(0x13, 3, lambda_37D7)

    def lambda_37E8():

        label("loc_37E8")

        TurnDirection(0xFE, 0x21, 400)
        OP_48()
        Jump("loc_37E8")

    QueueWorkItem2(0x18, 3, lambda_37E8)

    def lambda_37F9():

        label("loc_37F9")

        TurnDirection(0xFE, 0x21, 400)
        OP_48()
        Jump("loc_37F9")

    QueueWorkItem2(0x14, 3, lambda_37F9)

    def lambda_380A():

        label("loc_380A")

        TurnDirection(0xFE, 0x21, 400)
        OP_48()
        Jump("loc_380A")

    QueueWorkItem2(0x1C, 3, lambda_380A)

    def lambda_381B():

        label("loc_381B")

        TurnDirection(0xFE, 0x21, 400)
        OP_48()
        Jump("loc_381B")

    QueueWorkItem2(0x1A, 3, lambda_381B)

    def lambda_382C():

        label("loc_382C")

        TurnDirection(0xFE, 0x21, 400)
        OP_48()
        Jump("loc_382C")

    QueueWorkItem2(0x1B, 3, lambda_382C)

    def lambda_383D():

        label("loc_383D")

        TurnDirection(0xFE, 0x21, 400)
        OP_48()
        Jump("loc_383D")

    QueueWorkItem2(0x1F, 3, lambda_383D)

    def lambda_384E():

        label("loc_384E")

        TurnDirection(0xFE, 0x21, 400)
        OP_48()
        Jump("loc_384E")

    QueueWorkItem2(0x1E, 3, lambda_384E)
    Fade(500)
    OP_6D(-770, 4100, -12910, 0)
    OP_67(0, 5310, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(222000, 0)
    OP_6E(398, 0)
    SetChrPos(0x22, 500, 4500, 500, 180)
    SetChrPos(0x10F, -530, 4000, -1900, 180)
    SetChrPos(0x101, -520, 4000, -3300, 180)
    SetChrPos(0x15, -1900, 4000, -3140, 180)
    SetChrPos(0x1F, 910, 4000, -3240, 180)
    SetChrPos(0x11, 2400, 4000, -2870, 225)
    SetChrPos(0x12, 370, 4000, -6430, 180)
    SetChrPos(0x13, -980, 4000, -6350, 180)
    SetChrPos(0x14, 2000, 4000, -6250, 225)
    SetChrPos(0x16, -270, 4000, -4590, 180)
    SetChrPos(0x18, -1600, 4000, -4850, 180)
    SetChrPos(0x1E, -3030, 4000, -5200, 135)
    SetChrPos(0x1A, 2600, 4000, -4350, 225)
    SetChrPos(0x1B, 1170, 4000, -4730, 180)
    SetChrPos(0x1C, 3600, 4000, -5020, 225)
    SetChrPos(0x19, -2790, 4000, -6770, 135)
    OP_1D(0xAD)

    def lambda_39B3():
        OP_6D(-1000, 4000, -8000, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_39B3)

    def lambda_39CB():
        OP_8E(0xFE, 0x64, 0xFA0, 0xFFFFD936, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_39CB)
    WaitChrThread(0x21, 0x0)
    WaitChrThread(0x10F, 0x0)

    ChrTalk(    #78
        0x10F,
        "#1444F#11PKevin?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        "#1018F#11PYou're up!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x1E,
        "#111F#11PIt's good to see you again, Father.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x21,
        (
            "#1075F#5PYou, too. Wasn't expecting you of all people\x01",
            "to get an invitation here.\x02\x03",

            "#1840FOr you, for that matter, little lady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x1F,
        (
            "#263F#6P...I'm sure you weren't.\x02\x03",

            "#1305FI've got something I want to ask you...\x02\x03",

            "...but I suppose that can wait until later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x21,
        "#1066F#5PHaha. For sure.\x02",
    )

    CloseMessageWindow()

    def lambda_3B75():
        OP_6D(-820, 4000, -4440, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_3B75)
    SetChrFlags(0x21, 0x40)

    def lambda_3B92():
        OP_8E(0xFE, 0x514, 0xFA0, 0xFFFFF894, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_3B92)
    OP_43(0x12, 0x0, 0x4, 0x4)
    OP_43(0x13, 0x0, 0x4, 0x5)
    OP_43(0x1B, 0x0, 0x4, 0x6)
    OP_43(0x1A, 0x0, 0x4, 0x7)
    OP_43(0x16, 0x0, 0x4, 0x8)
    OP_43(0x18, 0x0, 0x4, 0x9)
    OP_43(0x1F, 0x0, 0x4, 0xA)
    OP_43(0x11, 0x0, 0x4, 0xB)
    WaitChrThread(0x21, 0x0)
    OP_44(0x10F, 0x3)
    OP_44(0x101, 0x3)
    OP_44(0x15, 0x3)
    OP_44(0x11, 0x3)
    OP_44(0x19, 0x3)
    OP_44(0x12, 0x3)
    OP_44(0x16, 0x3)
    OP_44(0x13, 0x3)
    OP_44(0x18, 0x3)
    OP_44(0x14, 0x3)
    OP_44(0x1C, 0x3)
    OP_44(0x1A, 0x3)
    OP_44(0x1B, 0x3)
    OP_44(0x1F, 0x3)
    OP_44(0x1E, 0x3)
    WaitChrThread(0x10F, 0x0)
    Fade(500)
    OP_6D(-1000, 4000, -510, 0)
    OP_67(0, 5340, -10000, 0)
    OP_6B(1950, 0)
    OP_6C(318000, 0)
    OP_6E(466, 0)
    SetChrPos(0x22, 0, 4500, 1000, 180)
    SetChrPos(0x21, 800, 4000, -1600, 0)
    SetChrPos(0x10F, -500, 4000, -1700, 90)
    SetChrPos(0x101, -100, 4000, -3000, 0)
    SetChrPos(0x15, -1100, 4000, -3200, 0)
    SetChrPos(0x1F, 1300, 4000, -3100, 0)
    SetChrPos(0x11, 2400, 4000, -3170, 315)
    SetChrPos(0x12, 1300, 4000, -6500, 0)
    SetChrPos(0x13, 100, 4000, -6500, 0)
    SetChrPos(0x14, 2800, 4000, -5870, 0)
    SetChrPos(0x16, 800, 4000, -4300, 0)
    SetChrPos(0x18, -500, 4000, -4700, 0)
    SetChrPos(0x1E, -1520, 4000, -4800, 0)
    SetChrPos(0x1A, 2200, 4000, -4570, 0)
    SetChrPos(0x1B, 1500, 4000, -5600, 0)
    SetChrPos(0x1C, 3500, 4000, -4960, 315)
    SetChrPos(0x19, -1400, 4000, -6200, 0)
    OP_0D()
    ClearChrFlags(0x21, 0x40)
    OP_8C(0x21, 270, 400)
    Sleep(500)

    ChrTalk(    #84
        0x10F,
        "#1802F#5PAre... Are you sure you're feeling all right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x21,
        (
            "#1071F#12PRight as rain! I'm feeling just great. All that\x01",
            "sleep must've done me a lot of good.\x02\x03",

            "#1840FAnd I see you guys made a whole lot of\x01",
            "progress while I was out cold, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x10F,
        "#1806F#5PYeah...\x02",
    )

    CloseMessageWindow()

    def lambda_3EA8():
        OP_6D(-800, 4000, 0, 1000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_3EA8)

    def lambda_3EC0():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_3EC0)
    Sleep(100)
    OP_8C(0x10F, 0, 400)
    WaitChrThread(0x10F, 0x0)
    Sleep(300)

    ChrTalk(    #87
        0x21,
        (
            "#1075F#6PHey. I'm Kevin Graham.\x02\x03",

            "#1078FOr maybe I don't need to introduce myself\x01",
            "since you seem to know a thing or two\x01",
            "about everyone who's come in here so far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x22,
        (
            "\x07\x0C#1616F#11PTrue. I was able to tell what was happening at\x01",
            "the Liber Ark from the garden.\x02\x03",

            "#1610FAnd out of all of the people here, you are the\x01",
            "one closest to the truth of what is happening\x01",
            "here... Am I wrong?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x10F,
        "#1444F#6P...What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x21,
        (
            "#1075F#6PNo, I don't think you are.\x02\x03",

            "#1840FI can't pretend to be much of an expert on\x01",
            "what Phantasma itself is...\x02\x03",

            "...but I've got a pretty good idea as to who's \x01",
            "responsible for all of this.\x02\x03",

            "I can only think of one person twisted enough\x01",
            "to put us through all we've been through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x10F,
        "#1802F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        "#1020F#6PWait! Is it someone you know?!\x02",
    )

    CloseMessageWindow()

    def lambda_41D7():
        OP_6D(-500, 4000, -1000, 1000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_41D7)

    def lambda_41EF():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_41EF)
    Sleep(50)

    def lambda_4202():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4202)
    Sleep(50)

    def lambda_4215():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_4215)
    Sleep(50)
    OP_8C(0x10F, 135, 400)
    WaitChrThread(0x10F, 0x0)

    ChrTalk(    #93
        0x21,
        (
            "#1075F#11PHaha... You could say that, yeah.\x02\x03",

            "#1067FThe short version is: they're a real piece of work.\x02\x03",

            "A cunning, arrogant, coldhearted son of a bitch\x01",
            "who doesn't even see people as people.\x02\x03",

            "#1840FThat about sums up who we're dealing with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x14,
        "#212F#6PS-Sounds like a real awful guy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x18,
        (
            "#1542F#6PHmm... And who, may I ask, is it that you're\x01",
            "talking about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x21,
        (
            "#1841F#11PWell, about that...\x02\x03",

            "Would you be willing to wait just a bit longer for\x01",
            "the answer to that one?\x02\x03",

            "#1840FI'm pretty sure I'm right, but I'm still missing one\x01",
            "last thing that'll let me be completely certain.\x02\x03",

            "And I think we'll find out just what that is in the\x01",
            "sixth plane.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x18,
        (
            "#1545F#6PHaha... And here I thought we were finally\x01",
            "going to get an answer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x13,
        (
            "#276FIs there a reason you can't share your\x01",
            "theory as is?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x21,
        (
            "#1065F#11PYeah... I realize I'm asking a lot after\x01",
            "we've come so far.\x02\x03",

            "#1063FBut I promise that as soon as I know\x01",
            "for sure, I'll talk.\x02\x03",

            "I swear on the Goddess' name and on\x01",
            "the church's emblem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x12,
        "#170F#6PHmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x1C,
        "#051F#6PWell, I don't see any reason to say no.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x1B,
        "#1534F#6PLikewise. He's clearly got his reasons.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x1A,
        (
            "#819F#6PIt's not often you ask us for favors,\x01",
            "so I can let it slide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x14,
        "#210F#6PNo problem here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        "#1016F#6PAhaha... If he says wait, I'll wait.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x15,
        (
            "#1513F#6PI feel as though we can trust your judgment,\x01",
            "Kevin, so I have no objections, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x11,
        "#560F#6PM-Me, neither!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x1F,
        (
            "#261F#6PI don't really care as long as I get to have\x01",
            "my fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x16,
        "#1168F#6PHeehee. I believe we're all in agreement, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x19,
        "#573F#6PYep. Consider this one settled.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x10F,
        "#1806F#5PThank you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x21,
        (
            "#1075F#11P...Thanks, guys.\x02\x03",

            "#1840FAnyway, now that I'm up, I'm also down to\x01",
            "take lead again.\x02\x03",

            "And I'd appreciate it if you backed me up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        "#1018F#6PNo problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x22,
        "\x07\x0C#1616F#11PIt seems like you're all ready to move on.\x07\x00\x02",
    )

    CloseMessageWindow()

    def lambda_495E():
        OP_6D(-800, 4000, 0, 1000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_495E)

    def lambda_4976():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_4976)
    Sleep(100)
    OP_8C(0x10F, 0, 400)
    WaitChrThread(0x10F, 0x0)
    Sleep(300)

    ChrTalk(    #115
        0x22,
        (
            "\x07\x0C#1610F#11PWhile you're advancing through the sixth plane,\x01",
            "I'll do all that I can on my end to find out more\x01",
            "about the seventh.\x02\x03",

            "Of course, if you need my support, I'll be happy\x01",
            "to provide it through the cube and the monuments\x01",
            "as I always have.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x21,
        (
            "#1079F#6PNow that you mention it, we haven't really\x01",
            "thanked you for all the help you've given us\x01",
            "since we got here, have we?\x02\x03",

            "#1075FThanks, Celeste. We couldn't have done this\x01",
            "without you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x16,
        "#1382F#6PWe truly are in your debt.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x22,
        (
            "\x07\x0C#1616FPlease, think nothing of it.\x02\x03",

            "#1611FI am but a shadow, placed here with a duty\x01",
            "to fulfill.\x02\x03",

            "I believe helping you to be part of that duty.\x02\x03",

            "If I may, allow me to help you however I can.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x21,
        "#1840F#6PWill do.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(1440, 4000, -520, 0)
    OP_67(0, 5280, -10000, 0)
    OP_6B(2150, 0)
    OP_6C(36000, 0)
    OP_6E(376, 0)
    SetChrPos(0x21, 1200, 4000, -1500, 0)
    SetChrPos(0x10F, -190, 4000, -1900, 0)
    SetChrPos(0x101, -110, 4000, -4240, 0)
    SetChrPos(0x15, -1200, 4000, -4050, 45)
    SetChrPos(0x1F, 1400, 4000, -3680, 0)
    SetChrPos(0x11, 2800, 4000, -3060, 315)
    SetChrPos(0x12, 1500, 4000, -6600, 0)
    SetChrPos(0x13, 100, 4000, -6940, 0)
    SetChrPos(0x14, 3250, 4000, -5870, 0)
    SetChrPos(0x16, 1160, 4000, -5170, 0)
    SetChrPos(0x18, -120, 4000, -5740, 0)
    SetChrPos(0x1E, -1550, 4000, -5800, 45)
    SetChrPos(0x1A, 3700, 4000, -3600, 315)
    SetChrPos(0x1B, 2200, 4000, -5440, 0)
    SetChrPos(0x1C, 4300, 4000, -4400, 315)
    SetChrPos(0x19, -1500, 4000, -7310, 45)
    OP_0D()
    OP_8C(0x21, 270, 400)
    Sleep(50)
    OP_8C(0x10F, 90, 400)
    Sleep(300)

    ChrTalk(    #120
        0x21,
        (
            "#1065F#11PSorry for worrying you, too, Ries.\x02\x03",

            "#1063FBut I'm just fine now.\x02\x03",

            "So please, just leave everything to me.\x01",
            "I'm begging you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x10F,
        (
            "#1802F#6P...\x02\x03",

            "#1445FOnly if you promise me one thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x21,
        "#1079F#11PWh-What is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x10F,
        (
            "#1446F#6PI won't make you promise not to put yourself in\x01",
            "danger, or to overdo it...\x02\x03",

            "#1806F...but don't do anything that would make Rufina\x01",
            "sad.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x21, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #124
        0x21,
        (
            "#1063F#11P...\x02\x03",

            "#1068FAaagh... You really know how to hit a guy\x01",
            "where it hurts, don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x10F,
        "#1806F#6P...So? Will you promise?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x21,
        (
            "#1067F#11P...\x02\x03",

            "#1075FYeah. I promise.\x02\x03",

            "#1840FI swear on her name, I won't.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_503C():
        OP_6B(3000, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_503C)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    Sleep(1000)
    OP_1D(0xD2)
    OP_44(0x10F, 0x0)
    OP_A2(0x2B00)
    OP_28(0x36, 0x1, 0x100)
    OP_28(0x35, 0x4, 0x10)
    OP_28(0x35, 0x4, 0x20)
    OP_28(0x36, 0x4, 0x10)
    OP_28(0x36, 0x4, 0x20)
    OP_28(0x37, 0x4, 0x4)
    OP_28(0x37, 0x4, 0x8)
    OP_28(0x37, 0x1, 0x1)
    OP_3F(0x360, 1)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x21, 0x80)
    ClearChrFlags(0xF0, 0x80)
    ClearChrFlags(0xF1, 0x80)
    OP_DB(0x0, 0x8)
    ClearParty()
    AddParty(0x8, 0xEE, 0xFF)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_DD(0x1, 0x0, 0x0, 256, 0, 0, 0)
    FadeToDark(0, 0, -1)
    OP_C0(0x20, 0x1, 0x100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    OP_6D(390, 4000, -1290, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(450, 0)
    SetChrPos(0x0, 390, 4000, -1290, 180)
    SetChrPos(0x1, 390, 4000, -1290, 180)
    SetChrPos(0x2, 390, 4000, -1290, 180)
    SetChrPos(0x3, 390, 4000, -1290, 180)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_E5(0x2, 0xFF, 0x13, 700)
    Call(0, 5)
    SetChrChipByIndex(0x22, 0)
    SetChrSubChip(0x22, 0)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x22, -2100, 4500, 3610, 135)
    SetChrFlags(0x22, 0x4)

    def lambda_524E():

        label("loc_524E")

        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        OP_48()
        Jump("loc_524E")

    QueueWorkItem2(0x22, 3, lambda_524E)
    OP_9F(0x22, 0xFF, 0xFF, 0xFF, 0xB4, 0x0)
    PlayEffect(0x0, 0x7, 0x22, 0, 800, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_3_1035 end

    def Function_4_52AC(): pass

    label("Function_4_52AC")

    Sleep(500)
    OP_8F(0xFE, 0xFFFFFE34, 0xFA0, 0xFFFFE822, 0x3E8, 0x0)
    Return()

    # Function_4_52AC end

    def Function_5_52C6(): pass

    label("Function_5_52C6")

    Sleep(600)
    OP_8F(0xFE, 0xFFFFF984, 0xFA0, 0xFFFFE48A, 0x3E8, 0x0)
    Return()

    # Function_5_52C6 end

    def Function_6_52E0(): pass

    label("Function_6_52E0")

    Sleep(900)
    OP_8F(0xFE, 0x76C, 0xFA0, 0xFFFFEDFE, 0x3E8, 0x0)
    Return()

    # Function_6_52E0 end

    def Function_7_52FA(): pass

    label("Function_7_52FA")

    Sleep(1000)
    OP_8F(0xFE, 0xCD0, 0xFA0, 0xFFFFF09C, 0x3E8, 0x0)
    Return()

    # Function_7_52FA end

    def Function_8_5314(): pass

    label("Function_8_5314")

    Sleep(1000)
    OP_8F(0xFE, 0xFFFFFC54, 0xFA0, 0xFFFFED7C, 0x3E8, 0x0)
    Return()

    # Function_8_5314 end

    def Function_9_532E(): pass

    label("Function_9_532E")

    Sleep(1100)
    OP_8F(0xFE, 0xFFFFF89E, 0xFA0, 0xFFFFECA0, 0x3E8, 0x0)
    Return()

    # Function_9_532E end

    def Function_10_5348(): pass

    label("Function_10_5348")

    Sleep(1300)
    OP_8F(0xFE, 0x852, 0xFA0, 0xFFFFF448, 0x3E8, 0x0)
    Return()

    # Function_10_5348 end

    def Function_11_5362(): pass

    label("Function_11_5362")

    Sleep(1400)
    OP_8F(0xFE, 0xBE0, 0xFA0, 0xFFFFF6F0, 0x3E8, 0x0)
    Return()

    # Function_11_5362 end

    def Function_12_537C(): pass

    label("Function_12_537C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_6D(-790, 4000, 1200, 0)
    OP_67(0, 7010, -10000, 0)
    OP_6B(1830, 0)
    OP_6C(315000, 0)
    OP_6E(444, 0)
    SetChrPos(0x109, 150, 4000, -810, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_541B")
    SetChrPos(0xEF, 270, 4000, 1220, 180)
    SetChrPos(0xF0, -370, 4000, -2190, 0)
    SetChrPos(0xF1, 1180, 4000, -2270, 0)
    Jump("loc_54A0")

    label("loc_541B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_545F")
    SetChrPos(0xF0, 270, 4000, 1220, 180)
    SetChrPos(0xEF, -370, 4000, -2190, 0)
    SetChrPos(0xF1, 1180, 4000, -2270, 0)
    Jump("loc_54A0")

    label("loc_545F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54A0")
    SetChrPos(0xF1, 270, 4000, 1220, 180)
    SetChrPos(0xEF, -370, 4000, -2190, 0)
    SetChrPos(0xF0, 1180, 4000, -2270, 0)

    label("loc_54A0")

    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #127
        0x105,
        (
            "#1382F#11PHi, everyone. Celeste kindly explained the\x01",
            "situation to me while you were away.\x02\x03",

            "You need my help in order to keep going,\x01",
            "don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x109,
        (
            "#1066F#6POh, you've been filled in already? Great!\x01",
            "Saves us the time explaining.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x105,
        (
            "#1383F#11PI'm ready to leave as soon as you are.\x02\x03",

            "#1160FSo just say the word when you're ready\x01",
            "to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x109,
        (
            "#1075F#6PGot it.\x02\x03",

            "#1078FWe'll head on out as soon as we're\x01",
            "done prepping, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2B04)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_12_537C end

    def Function_13_5669(): pass

    label("Function_13_5669")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_6D(-790, 4000, 1200, 0)
    OP_67(0, 7010, -10000, 0)
    OP_6B(1830, 0)
    OP_6C(315000, 0)
    OP_6E(444, 0)
    SetChrPos(0x109, 150, 4000, -810, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5708")
    SetChrPos(0xEF, 270, 4000, 1220, 180)
    SetChrPos(0xF0, -370, 4000, -2190, 0)
    SetChrPos(0xF1, 1180, 4000, -2270, 0)
    Jump("loc_578D")

    label("loc_5708")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_574C")
    SetChrPos(0xF0, 270, 4000, 1220, 180)
    SetChrPos(0xEF, -370, 4000, -2190, 0)
    SetChrPos(0xF1, 1180, 4000, -2270, 0)
    Jump("loc_578D")

    label("loc_574C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_578D")
    SetChrPos(0xF1, 270, 4000, 1220, 180)
    SetChrPos(0xEF, -370, 4000, -2190, 0)
    SetChrPos(0xF0, 1180, 4000, -2270, 0)

    label("loc_578D")

    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #131
        (
            "\x07\x05Kevin explained to Anelace that they thought she was the person the amberl\x01",
            "monument's inscription was asking for.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #132
        0x10A,
        (
            "#1317F#11PMe? The 'sword-wielding dame'?\x02\x03",

            "#819FI dunnooo... I mean, it's a cool-sounding title\x01",
            "and all, but does it really fit me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x109,
        (
            "#1077F#6PIt does if you ask me. But hey, even if you're\x01",
            "not sure, it's worth a try, right?\x02\x03",

            "#1078FDo you mind coming with us and giving it a go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x10A,
        (
            "#810F#11PYou got it.\x02\x03",

            "#1310FOff we go, then!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2B0B)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_13_5669 end

    def Function_14_5994(): pass

    label("Function_14_5994")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_6D(-790, 4000, 1200, 0)
    OP_67(0, 7010, -10000, 0)
    OP_6B(1830, 0)
    OP_6C(315000, 0)
    OP_6E(444, 0)
    SetChrPos(0x109, 150, 4000, -810, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A33")
    SetChrPos(0xEF, 270, 4000, 1220, 180)
    SetChrPos(0xF0, -370, 4000, -2190, 0)
    SetChrPos(0xF1, 1180, 4000, -2270, 0)
    Jump("loc_5AB8")

    label("loc_5A33")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A77")
    SetChrPos(0xF0, 270, 4000, 1220, 180)
    SetChrPos(0xEF, -370, 4000, -2190, 0)
    SetChrPos(0xF1, 1180, 4000, -2270, 0)
    Jump("loc_5AB8")

    label("loc_5A77")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AB8")
    SetChrPos(0xF1, 270, 4000, 1220, 180)
    SetChrPos(0xEF, -370, 4000, -2190, 0)
    SetChrPos(0xF0, 1180, 4000, -2270, 0)

    label("loc_5AB8")

    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #135
        (
            "\x07\x05Kevin explained to Richard that they thought he was the person the carnelia\x01",
            "monument's inscription was asking for.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #136
        0x10C,
        (
            "#113F#11PMe? The 'Divine Blade's successor'?\x02\x03",

            "#116FB-But...\x02\x03",

            "#115F...I suppose there's no point in debating if I am\x01",
            "fit to be called his successor. No one else seems\x01",
            "to match the description, after all.\x02\x03",

            "#110FI'd be happy to accompany you when you return\x01",
            "to that monument.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x109,
        "#1060F#6PThanks.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2B17)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_14_5994 end

    def Function_15_5C9C(): pass

    label("Function_15_5C9C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_6D(-790, 4000, 1200, 0)
    OP_67(0, 7010, -10000, 0)
    OP_6B(1830, 0)
    OP_6C(315000, 0)
    OP_6E(444, 0)
    SetChrPos(0x109, 150, 4000, -810, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D3B")
    SetChrPos(0xEF, 270, 4000, 1220, 180)
    SetChrPos(0xF0, -370, 4000, -2190, 0)
    SetChrPos(0xF1, 1180, 4000, -2270, 0)
    Jump("loc_5DC0")

    label("loc_5D3B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D7F")
    SetChrPos(0xF0, 270, 4000, 1220, 180)
    SetChrPos(0xEF, -370, 4000, -2190, 0)
    SetChrPos(0xF1, 1180, 4000, -2270, 0)
    Jump("loc_5DC0")

    label("loc_5D7F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DC0")
    SetChrPos(0xF1, 270, 4000, 1220, 180)
    SetChrPos(0xEF, -370, 4000, -2190, 0)
    SetChrPos(0xF0, 1180, 4000, -2270, 0)

    label("loc_5DC0")

    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #138
        (
            "\x07\x05Kevin explained to Joshua that they thought he was the person the nohval\x01",
            "monument's inscription was asking for.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #139
        0x102,
        (
            "#1503F#11P...\x02\x03",

            "#1513FSounds like the final area is where that\x01",
            "Schwarzritter's waiting for us, then.\x02\x03",

            "#1514FI wonder why he would want me to go,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x109,
        (
            "#1065F#6PAll we know is, he does.\x02\x03",

            "#1063FWhat's the verdict? Up for it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x102,
        (
            "#1505F#11PNaturally, I'll be accepting his invitation.\x02\x03",

            "#1500FWe should head back as soon as we've made\x01",
            "preparations. Just let me know when you're\x01",
            "ready.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_601B")

    ChrTalk(    #142
        0x101,
        "#1026F#6PJoshua...\x02",
    )

    CloseMessageWindow()

    label("loc_601B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_603F")

    ChrTalk(    #143
        0x10B,
        "#215F#6PU-Umm...\x02",
    )

    CloseMessageWindow()

    label("loc_603F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6065")

    ChrTalk(    #144
        0x105,
        "#1163F#6PJoshua...\x02",
    )

    CloseMessageWindow()

    label("loc_6065")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_608C")

    ChrTalk(    #145
        0x107,
        "#063F#6PJ-Joshua...\x02",
    )

    CloseMessageWindow()

    label("loc_608C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_60B5")

    ChrTalk(    #146
        0x110,
        "#1307F#6PYou're sure?\x02",
    )

    CloseMessageWindow()

    label("loc_60B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6177")

    ChrTalk(    #147
        0x102,
        (
            "#1513F#11P...I am. No matter what happens, I'll be fine.\x02\x03",

            "#1500FAll we can do now is keep going, and I don't\x01",
            "intend to fight that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6177")

    OP_A2(0x2B22)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_15_5C9C end

    def Function_16_6182(): pass

    label("Function_16_6182")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_82(0x7, 0x0)
    OP_E5(0x2, 0xFF, 0x13, 500)
    LoadEffect(0x0, "map\\mp263_05.eff")
    LoadEffect(0x1, "map\\mp259_01.eff")
    OP_D2(0x260350, 0x260355, 0x13)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x22, -1890, 4500, 1230, 135)
    OP_9F(0x22, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x22, 0x4)
    SetChrFlags(0x22, 0x4)

    def lambda_61FA():

        label("loc_61FA")

        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        OP_48()
        Jump("loc_61FA")

    QueueWorkItem2(0x22, 3, lambda_61FA)
    SetChrPos(0x109, 690, 4000, 250, 180)
    SetChrPos(0x10F, 1580, 4000, 960, 180)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1D, 850, 4000, -2160, 0)
    SetChrPos(0x15, -350, 4000, -2200, 0)
    SetChrPos(0x1F, 2100, 4000, -2050, 0)
    SetChrPos(0x11, 2610, 4000, -3630, 0)
    SetChrPos(0x12, 1950, 4000, -4980, 0)
    SetChrPos(0x13, 630, 4000, -5130, 0)
    SetChrPos(0x14, 4400, 4000, -4590, 315)
    SetChrPos(0x16, 1220, 4000, -3520, 0)
    SetChrPos(0x18, -10, 4000, -3630, 0)
    SetChrPos(0x19, -920, 4000, -4200, 0)
    SetChrPos(0x1A, 3590, 4000, -1950, 315)
    SetChrPos(0x1B, 5170, 4000, -3440, 315)
    SetChrPos(0x1C, 3920, 4000, -3280, 315)
    SetChrPos(0x1E, 3340, 4000, -5090, 0)
    OP_6D(250, 4000, -500, 0)
    OP_67(0, 5280, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(315000, 0)
    OP_6E(362, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #148
        "\x07\x00That's about the long and short of it.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_1D(0xC8)

    def lambda_63E9():
        OP_6B(2430, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_63E9)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Sleep(300)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Everyone")

    AnonymousTalk(    #149
        "\x07\x00...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #150
        0x109,
        (
            "#1067F#11PIn other words, all of this--everything that's\x01",
            "happened--is my fault.\x02\x03",

            "All of you are victims who had the misfortune\x01",
            "of knowing me and getting dragged into this.\x02\x03",

            "#1065FNo apology is sincere enough, but I'm so sorry\x01",
            "for what you've been put through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x1D,
        (
            "#1007F#6PI'm not following...\x02\x03",

            "#1008FWhy? I heard all you said, but I don't think\x01",
            "you've got any reason to be THAT sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x109,
        "#1079F#11PCome again, Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x13,
        (
            "#278F#6PBased on what we've learned, Phantasma choosing\x01",
            "a new master was an inevitability, and something it\x01",
            "would have done whether you were there or not.\x02\x03",

            "#277FAs such, after it lost the Aureole, something like this\x01",
            "would have happened no matter the circumstances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x18,
        (
            "#1545F#6PI agree.\x02\x03",

            "#1540FPhantasma would simply have chosen someone\x01",
            "else and created a different world as a result\x01",
            "of the trauma that lay within.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x13,
        (
            "#276F#6P...The thought that you might have been chosen\x01",
            "is nothing short of terrifying, too.\x02\x03",

            "Everything that has happened to us in here so\x01",
            "far is nothing compared to what we would have\x01",
            "endured had that come to pass.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6863():
        OP_6D(-250, 4000, -1000, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_6863)
    OP_8C(0x18, 135, 400)
    WaitChrThread(0xEE, 0x0)

    ChrTalk(    #156
        0x18,
        (
            "#1544F#5POh, Mueller! Your words are like the sweetest kiss\x01",
            "turned frozen upon parting. Do you have that little\x01",
            "faith in me, your one and only?\x02\x03",

            "#1547FPerhaps everyone here would have been drawn\x01",
            "into the most ravenous feast the world has ever\x01",
            "seen, but nothing more than that.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x19, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x1D, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x11, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1E, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x1F, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x13, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    def lambda_6B09():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6B09)

    def lambda_6B17():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_6B17)
    Sleep(50)

    def lambda_6B2A():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_6B2A)

    def lambda_6B38():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6B38)
    Sleep(50)

    def lambda_6B4B():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_6B4B)

    def lambda_6B59():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6B59)
    Sleep(50)

    def lambda_6B6C():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_6B6C)

    def lambda_6B7A():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6B7A)
    Sleep(50)

    def lambda_6B8D():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_6B8D)

    def lambda_6B9B():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_6B9B)
    Sleep(50)

    def lambda_6BAE():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_6BAE)
    OP_8C(0x1F, 225, 400)

    ChrTalk(    #157
        0x13,
        "#274F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x11,
        "#065F#12PI-I'm scared...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x1C,
        "#057F#12PI'm just disgusted.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x1D,
        (
            "#1019F#11PYou're a special degree of creep,\x01",
            "you know that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x14,
        (
            "#214F#12PI-I want no part of any 'feast' that comes\x01",
            "from outta your brain!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x1B,
        "#1525F#12P*sigh* Count me out of this one...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x109,
        (
            "#1840F#11PUmm... I can't help but feel you guys are kinda\x01",
            "missing the point...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1F, 0, 400)
    Sleep(300)

    ChrTalk(    #164
        0x1F,
        (
            "#263F#6PWell, don't take this as me trying to defend\x01",
            "you or anything...\x02\x03",

            "#1305F...but in a sense, it might have been a good\x01",
            "thing you were chosen over anyone else.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_6E17():
        OP_6D(250, 4000, -500, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_6E17)

    def lambda_6E2F():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6E2F)
    Sleep(50)

    def lambda_6E42():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6E42)

    def lambda_6E50():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_6E50)
    Sleep(50)

    def lambda_6E63():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_6E63)

    def lambda_6E71():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6E71)
    Sleep(50)

    def lambda_6E84():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_6E84)

    def lambda_6E92():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6E92)
    Sleep(50)

    def lambda_6EA5():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_6EA5)

    def lambda_6EB3():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6EB3)
    Sleep(50)

    def lambda_6EC6():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_6EC6)

    def lambda_6ED4():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_6ED4)
    Sleep(50)

    def lambda_6EE7():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_6EE7)

    def lambda_6EF5():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_6EF5)
    Sleep(50)
    Sleep(500)
    WaitChrThread(0xEE, 0x0)

    ChrTalk(    #165
        0x109,
        "#1079F#5PHow do you figure?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x10F,
        "#1934F#11PI'm lost as well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x1F,
        (
            "#263F#6PYour Stigma's obviously very powerful, and it's\x01",
            "capable of exerting a lot of control over things.\x02\x03",

            "Enough so that Phantasma as it is now exists in\x01",
            "a state of order.\x02\x03",

            "#1306FBut what if it had chosen someone else? Would\x01",
            "the world have been able to maintain order then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x109,
        "#1063F#5PHmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x15,
        (
            "#1505F#5PIt's possible that Phantasma would have been\x01",
            "unable to contain the chaos that ensued and\x01",
            "gone out of control under someone else...\x02\x03",

            "#1500F...is what you're essentially getting at, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1F, 270, 400)
    Sleep(300)

    ChrTalk(    #170
        0x1F,
        (
            "#269F#12PTeehee. I knew you'd understand, Joshua.\x02\x03",

            "If that had happened, a whole lot more people\x01",
            "might have been caught up in this.\x02\x03",

            "#261FNot that I've got a problem with lots of guests\x01",
            "at a tea party. The more, the merrier! ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x11,
        "#067F#6PC-C'mon, Renne...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x1D,
        (
            "#1016F#5PI think you're the only one who'd\x01",
            "be having fun...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x19,
        "#573F#5PHeh...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x19, 0, 400)
    Sleep(300)

    ChrTalk(    #174
        0x19,
        (
            "#070F#6PShe's right. I don't think you've got any reason to\x01",
            "beat yourself up over this.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_731E():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_731E)
    Sleep(50)

    def lambda_7331():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_7331)
    Sleep(50)

    def lambda_7344():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_7344)
    Sleep(50)

    def lambda_7357():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_7357)
    Sleep(50)

    def lambda_736A():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_736A)
    Sleep(50)

    def lambda_737D():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_737D)
    Sleep(50)

    def lambda_7390():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_7390)
    Sleep(500)

    ChrTalk(    #175
        0x1E,
        (
            "#119F#6PWe're all very different people from different walks\x01",
            "of life...\x02\x03",

            "#111F...but right now, we're all here, sharing a common\x01",
            "destiny.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x1A,
        (
            "#816F#6PYeah. In times like these, we've gotta help\x01",
            "each other out, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x16,
        (
            "#1383F#6PBesides, this place relates to the Aureole,\x01",
            "which is Liberl's problem.\x02\x03",

            "#1382FFrom my perspective, you're a victim.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x12,
        (
            "#179F#6PI couldn't agree more.\x02\x03",

            "#170FAs such, Kevin, we would appreciate you continuing\x01",
            "to lead us as you have done so far.\x02\x03",

            "It's time to truly bring an end to what was started\x01",
            "half a year ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x10F,
        "#1932F#11PWhat can I even say...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x109,
        (
            "#1846F#11P#40WHaha...\x02\x03",

            "#1844FFirst I'm stupid, then Ries pulls off the dumbest\x01",
            "thing I've ever seen...and now you guys. This must\x01",
            "be the biggest group of idiots in all of Zemuria.\x02\x03",

            "I swear, you wouldn't find a more gullible, naive\x01",
            "bunch anywhere on the continent...\x02\x03",

            "#1845FI was happy to use each and every one of you for\x01",
            "my own devices right to the very end...\x02\x03",

            "...so how can you be so...so...?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x109, 19)
    SetChrSubChip(0x109, 0)
    OP_0D()
    OP_9E(0x109, 0xF, 0x0, 0x12C, 0x7D0)
    Sleep(500)

    ChrTalk(    #181
        0x10F,
        "#1946F#11PIt's all right, Kevin...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x15,
        "#1500F#6PKevin...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x1D,
        (
            "#1016F#6PAhaha. Sometimes, you just have to know when\x01",
            "to give in.\x02\x03",

            "#1006F...And you're at that point right now. Your luck\x01",
            "ran out the second you got stuck with us.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7898():
        OP_6D(900, 4000, -1500, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_7898)
    OP_44(0x109, 0x0)
    WaitChrThread(0xEE, 0x1)

    ChrTalk(    #184
        0x14,
        (
            "#210F#6PHeehee. Got stuck with YOU, you mean.\x02\x03",

            "#211FSpending too much time with pushy, meddling\x01",
            "do-gooders who don't know when to quit like\x01",
            "you is bad for anyone.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1D, 135, 600)
    Sleep(200)

    ChrTalk(    #185
        0x1D,
        "#1019F#5PY-You wanna say that again?\x02",
    )

    CloseMessageWindow()

    def lambda_7997():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_7997)
    Sleep(50)

    def lambda_79AA():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_79AA)
    Sleep(50)

    def lambda_79BD():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_79BD)
    Sleep(50)

    def lambda_79D0():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_79D0)
    Sleep(50)

    def lambda_79E3():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_79E3)
    Sleep(50)

    def lambda_79F6():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_79F6)
    Sleep(50)

    def lambda_7A09():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_7A09)
    Sleep(50)

    def lambda_7A1C():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_7A1C)
    Sleep(400)

    ChrTalk(    #186
        0x15,
        "#1514F#5P...Haha.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x1B,
        (
            "#1521F#12PWell, all of those things describe you to a T,\x01",
            "that much is true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x1F,
        "#268F#12P*sigh* They certainly do.\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #189
        0x11,
        (
            "#560F#6PUmm... I...\x02\x03",

            "#067FI think they're your good points, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x1A,
        (
            "#811F#12PYeah! So do I!\x02\x03",

            "#1310FI think Estelle's rubbed off on all of us at this\x01",
            "point...and that's not a bad thing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x1D,
        "#1007F#5PTh-Thanks, guys...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x1C,
        (
            "#051F#12PGroup of idiots is right.\x02\x03",

            "We're smack dab in the middle of a shitty situation\x01",
            "here, but you wouldn't know it by lookin' at us.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x18, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #193
        0x18,
        (
            "#1540F#5PWith a team this spectacular, what do we have\x01",
            "to fear?\x02\x03",

            "#1541FThere's a chance we could even overthrow the\x01",
            "Erebonian government if we put our minds to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x13,
        (
            "#274F#6PNeed I remind you that that's not something an\x01",
            "Erebonian prince should be saying out loud?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7D78():
        OP_6D(250, 4000, -500, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_7D78)
    WaitChrThread(0xEE, 0x0)
    Fade(250)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #195
        0x109,
        "#1846F#11PHaha... All right, all right! I know when I'm beat.\x02",
    )

    CloseMessageWindow()

    def lambda_7DED():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_7DED)

    def lambda_7DFB():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_7DFB)
    Sleep(50)

    def lambda_7E0E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_7E0E)
    Sleep(50)

    def lambda_7E21():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_7E21)

    def lambda_7E2F():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7E2F)
    Sleep(50)

    def lambda_7E42():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_7E42)

    def lambda_7E50():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7E50)
    Sleep(50)

    def lambda_7E63():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_7E63)

    def lambda_7E71():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_7E71)
    Sleep(50)

    def lambda_7E84():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_7E84)

    def lambda_7E92():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_7E92)
    Sleep(50)

    def lambda_7EA5():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_7EA5)

    def lambda_7EB3():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_7EB3)
    Sleep(500)

    ChrTalk(    #196
        0x109,
        (
            "#1065F#11PWe're in this. Together.\x02\x03",

            "#1840FAnd this time, I actually mean that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x1D,
        "#1017F#6PGot it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x15,
        "#1513F#6PWe're happy to have you with us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x109,
        (
            "#1065F#11PAnyway...at least now, we know exactly what we\x01",
            "need to do here.\x02\x03",

            "#1063FWe need to defeat Rufina, the Lord of Phantasma.\x01",
            "There's no getting around that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x10F,
        "#1935F#11P...Unfortunately not.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x12,
        "#176F#6PIndeed...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x18,
        (
            "#1551F#6PWith that said...just where is she?\x02\x03",

            "#1542FYou didn't encounter her in Gehenna, did you?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80FC")

    ChrTalk(    #203
        0x1D,
        (
            "#1007F#6PShe disappeared right after the two of you fell\x01",
            "down there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8529")

    label("loc_80FC")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8155")

    ChrTalk(    #204
        0x15,
        (
            "#1503F#6PShe disappeared right after the two of you fell\x01",
            "down there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8529")

    label("loc_8155")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81AD")

    ChrTalk(    #205
        0x14,
        (
            "#413F#6PShe disappeared right after the two of you fell\x01",
            "down there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8529")

    label("loc_81AD")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8205")

    ChrTalk(    #206
        0x1F,
        (
            "#268F#6PShe disappeared right after the two of you fell\x01",
            "down there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8529")

    label("loc_8205")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_825D")

    ChrTalk(    #207
        0x11,
        (
            "#561F#6PShe disappeared right after the two of you fell\x01",
            "down there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8529")

    label("loc_825D")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82B6")

    ChrTalk(    #208
        0x1A,
        (
            "#1316F#6PShe disappeared right after the two of you fell\x01",
            "down there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8529")

    label("loc_82B6")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_830F")

    ChrTalk(    #209
        0x16,
        (
            "#1163F#6PShe disappeared right after the two of you fell\x01",
            "down there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8529")

    label("loc_830F")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8368")

    ChrTalk(    #210
        0x1B,
        (
            "#1532F#6PShe disappeared right after the two of you fell\x01",
            "down there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8529")

    label("loc_8368")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83BA")

    ChrTalk(    #211
        0x1C,
        (
            "#552F#6PShe just vanished after you'd both fallen down\x01",
            "there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8529")

    label("loc_83BA")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8412")

    ChrTalk(    #212
        0x19,
        (
            "#572F#6PShe disappeared right after the two of you fell\x01",
            "down there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8529")

    label("loc_8412")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8470")

    ChrTalk(    #213
        0x12,
        (
            "#175F#6PShe disappeared immediately after the two of you\x01",
            "fell down there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8529")

    label("loc_8470")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84CE")

    ChrTalk(    #214
        0x13,
        (
            "#276F#6PShe disappeared immediately after the two of you\x01",
            "fell down there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8529")

    label("loc_84CE")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8529")

    ChrTalk(    #215
        0x1E,
        (
            "#116F#6PShe disappeared immediately after the two of you\x01",
            "fell down there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8529")


    ChrTalk(    #216
        0x109,
        "#1065F#11PThat's a good question...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x10F,
        (
            "#1935F#11PI think it's safe to say she wasn't down\x01",
            "in Gehenna with us.\x02\x03",

            "#1942FIf she had been, she would have shown\x01",
            "herself at some point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x109,
        (
            "#1840F#5PYeah...\x02\x03",

            "#1841FBut then where IS she?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 100, -1, -1)

    AnonymousTalk(    #219
        "\x07\x0CI believe I can answer that.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x19, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_8803():
        OP_6D(-1620, 4000, 1500, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_8803)

    def lambda_881B():
        OP_67(0, 3610, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_881B)

    def lambda_8833():
        OP_6B(2800, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_8833)

    def lambda_8843():
        OP_6E(373, 2000)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_8843)

    def lambda_8853():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8853)
    Sleep(100)

    def lambda_8866():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_8866)
    Sleep(100)

    def lambda_8879():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8879)
    Sleep(100)
    OP_8C(0x1F, 315, 400)
    WaitChrThread(0xEE, 0x0)
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0x22, 0, 800, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_22(0x99, 0x0, 0x64)

    def lambda_88DC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xB4, 0x320)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_88DC)
    PlayEffect(0x1, 0x7, 0x22, 0, 900, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x22, 0x1)
    OP_82(0x0, 0x2)
    Sleep(1000)

    ChrTalk(    #220
        0x16,
        "#1164F#6PCeleste?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x109,
        (
            "#1840F#6PDidn't realize you were here.\x02\x03",

            "#1065FI can't thank you enough for saving our hides\x01",
            "earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x10F,
        (
            "#1937F#12PTruly, I doubt we would have been able to get\x01",
            "out unharmed if not for your assistance.\x02\x03",

            "#1946FWe're both grateful beyond words.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x22,
        (
            "\x07\x0C#1616F#5PHeehee. I was more than happy to help.\x02\x03",

            "All of us here are in the same predicament,\x01",
            "myself included.\x02\x03",

            "#1611FYou can even think of me as another one of\x01",
            "your companions if you'd like.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x109,
        (
            "#1075F#6PHeh... Naturally.\x02\x03",

            "#1063FWhat kinda answer are you thinking you\x01",
            "can give?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x22,
        (
            "\x07\x0C#1615F#5PAhh, yes...\x02\x03",

            "#1610FIt took some time, but I was able to\x01",
            "ascertain her current location.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x19, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #226
        0x109,
        "#1064F#6PWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x10F,
        "#1934F#12PR-Really?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x16,
        (
            "#1382F#6PIs that what you've been working on all this\x01",
            "time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x22,
        (
            "\x07\x0C#1616F#5PYes, it is.\x02\x03",

            "#1612FDuring my investigation of the seventh plane, \x01",
            "I was able to gain an understanding of the \x01",
            "layout and contents of Phantasma as a whole.\x02\x03",

            "I also discovered that the Lord of Phantasma\x01",
            "isn't in any of the planes. Rather, she is outside\x01",
            "of them.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x10F,
        "#1942F#12PPhantasma consists of more than just the planes?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x11,
        "#065F#6PWh-What's it like outside of them?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x22,
        (
            "\x07\x0C#1612F#5PThink of the planes you've been exploring like\x01",
            "a giant, multi-layered structure in the center of\x01",
            "Phantasma.\x02\x03",

            "They're all you have known up until this point,\x01",
            "but this world consists of more than them.\x02\x03",

            "#1615FThat said, the rest of Phantasma is just a vast,\x01",
            "barren wasteland at this point, abandoned and\x01",
            "and devoid of life.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x1B,
        "#1522F#6PHard to picture without seeing it for myself...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x1C,
        (
            "#551F#6PDo you know where in this big abandoned\x01",
            "wasteland she is?\x02\x03",

            "#555FBecause if it's that vast, just knowing she's\x01",
            "there probably isn't gonna help us much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x22,
        (
            "\x07\x0C#1615F#5PI have a relatively good idea where in it she is,\x01",
            "thankfully.\x02\x03",

            "#1612FAlthough, that doesn't solve the core problem...\x02\x03",

            "I fear the word 'vast' doesn't do the scale of\x01",
            "the wasteland itself justice.\x02\x03",

            "I believe it's roughly the size of the continent\x01",
            "where you live.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x19, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #236
        0x1D,
        "#1005F#6PIt's the size of ZEMURIA?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x15,
        (
            "#1502F#6PThat IS going to pose a problem...\x02\x03",

            "#1503FCrossing an area that massive on foot would\x01",
            "take months. Maybe even longer...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x1E,
        (
            "#112F#6PDo we not have any other means of transport\x01",
            "that we could use?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x22,
        (
            "\x07\x0C#1615F#5PHmm...\x02\x03",

            "#1613FI'm not sure my power would be of any use to you\x01",
            "here.\x02\x03",

            "I can't place monuments too far from this garden,\x01",
            "for one thing...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x109,
        (
            "#1841F#6PEven if we did commit ourselves to trekking across\x01",
            "the whole thing on foot, without the cube's power,\x01",
            "we couldn't come back and resupply.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x10F,
        (
            "#1935F#12PTrying to take several months worth of food\x01",
            "hardly seems realistic...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x19,
        (
            "#075F#6PWell, this is a tough one...\x02\x03",

            "#072FI can only think of waiting for her\x01",
            "to come to us.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_62(0x1C, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_972D():
        OP_6D(-670, 4000, 450, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_972D)

    def lambda_9745():
        OP_67(0, 3960, -10000, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_9745)
    OP_8C(0x1C, 270, 400)
    WaitChrThread(0xEE, 0x0)
    Sleep(300)

    ChrTalk(    #243
        0x1C,
        (
            "#052FWhat's up with you, shortstuff?#12P\x01",
            "Got something on your mind?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11)
    Sleep(300)
    OP_8C(0x11, 90, 400)
    Sleep(300)

    ChrTalk(    #244
        0x11,
        (
            "#067F#5PWell...I was just thinking...\x02\x03",

            "#560FWhy not use the Arseille?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x22, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x19, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_999B():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_999B)

    def lambda_99A9():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_99A9)
    Sleep(50)

    def lambda_99BC():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_99BC)

    def lambda_99CA():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_99CA)
    Sleep(50)

    def lambda_99DD():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_99DD)
    Sleep(50)

    def lambda_99F0():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_99F0)

    def lambda_99FE():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_99FE)
    Sleep(50)

    def lambda_9A11():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_9A11)

    def lambda_9A1F():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_9A1F)
    Sleep(50)

    def lambda_9A32():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9A32)

    def lambda_9A40():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_9A40)
    Sleep(400)

    ChrTalk(    #245
        0x1C,
        "#055F#12PErr, what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x12,
        "#173F#6PThe replica we encountered on the first plane?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 180, 400)
    Sleep(300)

    ChrTalk(    #247
        0x11,
        (
            "#563F#11PYeah.\x02\x03",

            "#560FThis world is supposed to react to the desires\x01",
            "of people in it, right?\x02\x03",

            "So while that Arseille might not be the real one,\x01",
            "it looks just like it.\x02\x03",

            "Everyone here's pretty familiar with the real\x01",
            "thing and how it looks, so it seems like a ship\x01",
            "we could all picture flying easily.\x02\x03",

            "Maybe if we all wished for it to fly together,\x01",
            "it might actually happen...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x1D, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x15, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x22, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x19, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x16, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x18, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x1C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x1A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x1B, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x1F, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x1E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_62(0x11, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x11, 0, 400)
    Sleep(300)
    OP_8C(0x11, 90, 400)
    OP_63(0x109)
    OP_63(0x10F)
    OP_63(0x1D)
    OP_63(0x15)
    OP_63(0x22)
    OP_63(0x19)
    OP_63(0x12)
    OP_63(0x16)
    OP_63(0x13)
    OP_63(0x18)
    OP_63(0x14)
    OP_63(0x1C)
    OP_63(0x1A)
    OP_63(0x1B)
    OP_63(0x1F)
    OP_63(0x1E)
    Sleep(300)

    ChrTalk(    #248
        0x11,
        (
            "#065F#5PS-Sorry! Aha...ha... I'm being silly, aren't I?\x02\x03",

            "#562FI don't know what's gotten into me... This isn't\x01",
            "something an engineer should be saying...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x1F,
        (
            "#263F#11PI don't think you're silly at all, Tita.\x02\x03",

            "#265FIn fact, I think that's a fantastic idea.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x11, 0, 400)

    ChrTalk(    #250
        0x11,
        "#064F#6PYou do?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x109,
        (
            "#1060F#11PIt does seem like the easier something is to imagine,\x01",
            "the easier it is to have it realized in Phantasma.\x02\x03",

            "And both you and Julia are familiar with the exact\x01",
            "structure of the Arseille, while most of us here have\x01",
            "seen and been on board it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x15,
        (
            "#1513F#5P...This might actually work.\x02\x03",

            "#1501FThere's clearly no rule saying airships can't\x01",
            "exist here, either, given that we've already\x01",
            "been on the Black Ark.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A0AF():
        OP_6D(-1620, 4000, 1500, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_A0AF)

    def lambda_A0C7():
        OP_67(0, 3610, -10000, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_A0C7)
    OP_8C(0x1D, 0, 400)
    WaitChrThread(0xEE, 0x0)

    ChrTalk(    #253
        0x1D,
        "#1018F#6PWell, Celeste? Do you think it would work?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x22,
        (
            "\x07\x0C#1615F#5P...\x02\x03",

            "#1612FThe Arseille was the ship you used to board\x01",
            "the Liber Ark, I believe?\x02\x03",

            "Then if I were to feed the image of it flying\x01",
            "then back into the system...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x22, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    def lambda_A1E5():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A1E5)

    def lambda_A1F3():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_A1F3)
    Sleep(50)

    def lambda_A206():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_A206)

    def lambda_A214():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_A214)
    Sleep(50)

    def lambda_A227():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_A227)

    def lambda_A235():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_A235)
    Sleep(50)

    def lambda_A248():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_A248)

    def lambda_A256():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_A256)
    Sleep(50)

    def lambda_A269():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_A269)

    def lambda_A277():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_A277)
    Sleep(50)

    def lambda_A28A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_A28A)

    def lambda_A298():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_A298)
    Sleep(1700)
    OP_63(0x22)
    Sleep(500)

    ChrTalk(    #255
        0x22,
        (
            "\x07\x0C#1616F#5P...I think this may actually be possible.\x02\x03",

            "#1611FIf all of you are on board, the white wings\x01",
            "will take to the skies once more.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x19, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #256
        0x109,
        "#1078F#6PWe can really make this happen?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x11,
        "#067F#6PI-I can't believe it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x1F,
        "#261F#5PHeehee. Well done, Tita.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x1D,
        "#1001F#5PTotally! You really outdid yourself this time.\x02",
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #260
        0x14,
        (
            "#415F#6PW-Wait a second...\x02\x03",

            "Does this mean we might be able to make\x01",
            "the Bobcat fly? There's a copy of that here,\x01",
            "too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x15,
        "#1500F#5POh, you're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x22,
        (
            "\x07\x0C#1615F#5PHmm...\x02\x03",

            "#1610FHow many of you are familiar with that?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x14,
        "#216F#6PCrap... Forgot about that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x15,
        (
            "#1503F#6PI think Josette and I are the only ones who\x01",
            "have actually flown in it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x1D,
        (
            "#1015F#6PSchera, Olivier, and I have technically been in it,\x01",
            "but that was just as stowaways...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x1B,
        (
            "#1527F#6PYeah. That was back when we were investigating\x01",
            "that airship hijacking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x18,
        (
            "#1541F#6PHeh. What a fond memory that adventure made\x01",
            "now that I look back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x22,
        (
            "\x07\x0C#1613F#5PI'm not sure what the odds of success would be,\x01",
            "then... That's a rather small number of people.\x02\x03",

            "#1610FI think it would be wise to focus on trying to\x01",
            "revive the Arseille first.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x14,
        "#413F#6PAww... Okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x12,
        (
            "#179F#6PStill, this sounds like a much better plan than\x01",
            "trying to walk there on foot.\x02\x03",

            "#170FWe should prepare for departure at once, then\x01",
            "make our way to the Arseille!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x1C,
        "#051F#6PDon't gotta tell me twice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x1E,
        (
            "#111F#6PWe'll have a lot in store for us if we're able\x01",
            "to make this work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x22,
        (
            "\x07\x0C#1615F#5PHowever, I should warn you all of one thing:\x02\x03",

            "#1613FOnce you have flown the Arseille to the area\x01",
            "where the Lord of Phantasma awaits, that will\x01",
            "be it.\x02\x03",

            "#1612FYou will be unable to return to this garden ever\x01",
            "again. Please be mindful of that.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x10F,
        "#1942F#12PNever? Not even once?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x16,
        (
            "#1163F#6PBecause we won't be able to use the cube's\x01",
            "warp functionality anymore?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x22,
        (
            "\x07\x0C#1612F#5PCorrect. Using it to warp is only possible when\x01",
            "you are within a certain range of the garden;\x01",
            "go outside of that, and it is no longer possible.\x02\x03",

            "#1615FSo before you depart, I would ask that you make\x01",
            "absolutely sure you have everything you need\x01",
            "and are ready for whatever you may find there.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x1D,
        "#1025F#6PGood to know...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x19,
        (
            "#573F#6PIt wouldn't hurt to do some extra training,\x01",
            "then. I don't doubt we're all gonna have to\x01",
            "play our part in the things to come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x1A,
        (
            "#819F#6PY-Yeah, you're right.\x02\x03",

            "#1310FI wouldn't mind getting in some exercise, myself.\x01",
            "Wouldn't want to wind up being the one to drag\x01",
            "the group down!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x18,
        (
            "#1545F#6PThis will be our last opportunity to open the \x01",
            "doors scattered throughout the planes and\x01",
            "take anything we find, too.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AE7C():
        OP_6D(-150, 4000, 480, 1200)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_AE7C)

    def lambda_AE94():
        OP_67(0, 4450, -10000, 1200)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_AE94)

    def lambda_AEAC():
        OP_6B(2620, 1200)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_AEAC)

    def lambda_AEBC():
        OP_6E(346, 1200)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_AEBC)

    def lambda_AECC():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AECC)
    Sleep(100)
    OP_8C(0x10F, 180, 400)
    WaitChrThread(0xEE, 0x0)
    Sleep(300)

    ChrTalk(    #281
        0x109,
        (
            "#1075F#11PIt's probably best I step down as leader for the\x01",
            "time being, then. If you're just door hunting or\x01",
            "trying to get some extra practice in, I'd only get\x01",
            "in the way.\x02\x03",

            "#1060FIf anyone else wants to learn how to use the\x01",
            "cube or fill out my notebook, I'd be happy to\x01",
            "teach you. Just let me know.\x02\x03",

            "#1078FLet's just be sure that when the time comes,\x01",
            "we leave with no regrets!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Everyone")

    AnonymousTalk(    #282
        "\x07\x00#5SRight!\x02",
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    def lambda_B0B0():
        OP_6B(3300, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_B0B0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0xEE, 0x0)
    OP_20(0x7D0)
    Sleep(2000)
    OP_AD(0x2400EA, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    OP_1D(0xD5)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xD5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_84(0x0)
    OP_A2(0x2C20)
    OP_E5(0x2, 0xFF, 0x13, 700)
    OP_28(0x3D, 0x1, 0x10)
    OP_28(0x3D, 0x1, 0x20)
    OP_28(0x3D, 0x1, 0x40)
    OP_28(0x3D, 0x1, 0x80)
    OP_28(0x3D, 0x4, 0x10)
    OP_28(0x3D, 0x4, 0x20)
    OP_28(0x3E, 0x4, 0x4)
    OP_28(0x3E, 0x4, 0x8)
    OP_28(0x3E, 0x1, 0x1)
    OP_28(0x3E, 0x1, 0x2)
    OP_28(0x3E, 0x1, 0x4)
    OP_28(0x3E, 0x1, 0x8)
    OP_28(0x3E, 0x1, 0x10)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_DB(0x0, 0x8)
    ClearParty()
    OP_DD(0x1, 0x0, 0x0, 0, 0, 0, 0)
    FadeToDark(0, 0, -1)
    OP_C0(0x20, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    OP_6D(250, 4000, -3050, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(450, 0)
    SetChrPos(0x0, 250, 4000, -3050, 180)
    SetChrPos(0x1, 250, 4000, -3050, 180)
    SetChrPos(0x2, 250, 4000, -3050, 180)
    SetChrPos(0x3, 250, 4000, -3050, 180)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    Call(0, 5)
    SetChrChipByIndex(0x22, 0)
    SetChrSubChip(0x22, 0)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x22, -2100, 4500, 3610, 135)

    def lambda_B2F7():

        label("loc_B2F7")

        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        OP_48()
        Jump("loc_B2F7")

    QueueWorkItem2(0x22, 3, lambda_B2F7)
    OP_9F(0x22, 0xFF, 0xFF, 0xFF, 0xB4, 0x0)
    LoadEffect(0x7, "map\\mp259_01.eff")
    PlayEffect(0x7, 0x7, 0x22, 0, 800, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_16_6182 end

    def Function_17_B36D(): pass

    label("Function_17_B36D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B3A9")
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0x7D0)
    Sleep(1000)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0x7D0)
    Sleep(1500)
    Jump("Function_17_B36D")

    label("loc_B3A9")

    Return()

    # Function_17_B36D end

    def Function_18_B3AA(): pass

    label("Function_18_B3AA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x27003D, 0x270042, 0x13)
    OP_D2(0x27051E, 0x27052B, 0x14)
    LoadEffect(0x3, "map\\mp253_04.eff")
    LoadEffect(0x4, "map\\mp253_03.eff")
    SetChrPos(0x109, 560, 4000, -1440, 0)
    SetChrPos(0x10F, -320, 4000, -2690, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x11, 2600, 4000, -2960, 0)
    SetChrPos(0x12, 2190, 4000, -4480, 0)
    SetChrPos(0x13, 550, 4000, -4510, 0)
    SetChrPos(0x14, 1370, 4000, -3090, 0)
    SetChrFlags(0xF0, 0x80)
    SetChrFlags(0xF1, 0x80)
    OP_6D(-2230, 5000, 4310, 0)
    OP_67(0, 3880, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(315000, 0)
    OP_6E(365, 0)
    ClearChrFlags(0x15, 0x80)
    OP_9F(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x15, 390, 8000, 2150, 180)
    SetChrFlags(0x15, 0x800)
    SetChrChipByIndex(0x15, 19)
    SetChrSubChip(0x15, 0)
    SetChrFlags(0x15, 0x4)
    PlayEffect(0x3, 0x0, 0x15, 0, 600, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    OP_E5(0x2, 0xFF, 0x13, 500)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_B538():
        OP_6D(-1210, 4000, 1510, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B538)

    def lambda_B550():
        OP_67(0, 4850, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B550)

    def lambda_B568():
        OP_6B(3200, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B568)

    def lambda_B578():
        OP_6E(327, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_B578)

    def lambda_B588():
        OP_8F(0xFE, 0x186, 0xFA0, 0x866, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_B588)
    WaitChrThread(0x15, 0x0)
    SetChrSubChip(0x15, 0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Fade(1000)
    OP_82(0x2, 0x2)
    PlayEffect(0x3, 0x1, 0x15, 0, 600, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)

    def lambda_B5F4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x7D0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_B5F4)
    OP_22(0x99, 0x0, 0x64)
    OP_82(0x0, 0x0)
    OP_0D()
    Sleep(1000)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #283
        0x14,
        "#213F#6POh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0x11,
        "#560F#6PTh-That looks like...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x13,
        "#278F#6PHeh. So even he ended up in here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0x12,
        (
            "#170F#6PSo one of the stars of the show makes\x01",
            "his grand appearance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x10F,
        "#1803F#6PThis is someone you know, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x109,
        (
            "#1075F#5PHaha. 'Know' is an understatement.\x02\x03",

            "#1840FHe's everyone's favorite black-haired prince.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x10F,
        "#1444F#6P???\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    PlayEffect(0x4, 0x4, 0x15, 0, 600, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_22(0x138, 0x0, 0x64)
    OP_23(0x146)

    def lambda_B841():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_B841)
    OP_82(0x2, 0x2)
    WaitChrThread(0x15, 0x0)
    Fade(500)
    OP_82(0x1, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #290
        0x15,
        "#1503F#5PUgh...\x02",
    )

    CloseMessageWindow()
    OP_9E(0x15, 0x14, 0x0, 0x12C, 0xBB8)

    def lambda_B891():
        OP_6D(-1210, 4000, 2510, 500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_B891)
    OP_22(0xA3, 0x0, 0x64)
    OP_22(0xD5, 0x0, 0x64)
    ClearChrFlags(0x15, 0x800)
    SetChrChipByIndex(0x15, 20)
    SetChrSubChip(0x15, 0)

    def lambda_B8C2():
        OP_96(0xFE, 0x186, 0xFA0, 0xD98, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_B8C2)
    WaitChrThread(0x15, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    ChrTalk(    #291
        0x15,
        "#1506F#11P#3SEstelle, get down!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #292
        0x15,
        "#1504F#11P...What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x14,
        "#415F#6PJ-Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x11,
        "#061F#6PJoshuaaa!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x15,
        (
            "#1504F#11PJosette? Tita?\x02\x03",

            "#1503FIs this a dream? Or some kind of illusory\x01",
            "tactic meant to disorient me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x109,
        (
            "#1075F#6PTrust you to get right to the theorizing.\x02\x03",

            "#1840FSorry, but this ain't no dream. Or illusion,\x01",
            "for that matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x15,
        "#1504F#11PI'm surprised to find so many of you here.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x15, 7)
    SetChrSubChip(0x15, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #298
        0x15,
        (
            "#1502F#11PMind telling me exactly what this situation\x01",
            "we've found ourselves in is?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrPos(0x109, 270, 4000, -2029, 0)
    SetChrPos(0x10F, -870, 4000, -2950, 0)
    SetChrPos(0x11, 1900, 4000, -3200, 0)
    SetChrPos(0x12, 1410, 4000, -4720, 0)
    SetChrPos(0x13, -320, 4000, -4620, 0)
    SetChrPos(0x14, 650, 4000, -3400, 0)
    SetChrPos(0x15, 290, 4000, -190, 180)
    OP_6D(-1180, 4000, -360, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(315000, 0)
    OP_6E(381, 0)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #299
        0x15,
        "#1503F#11P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x109,
        (
            "#1840F#6PUmm...\x02\x03",

            "Guess that wasn't enough to convince\x01",
            "you this is all actually happening, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0x15,
        (
            "#1505F#11POh, not at all. Consider me convinced.\x02\x03",

            "#1500FWhile the idea of this being an illusion seemed\x01",
            "initially plausible, the existence of your\x01",
            "companion over there made it quite unlikely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x10F,
        "#1444F#6PMe?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0x15,
        (
            "#1505F#11PCorrect.\x02\x03",

            "#1500FAm I right in assuming that you're a member\x01",
            "of the Gralsritter?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #304
        0x10F,
        "#1440F#6PYou can tell?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0x15,
        (
            "#1513F#11PWell, you're with Kevin and use a templar sword to\x01",
            "fight. It's a safe enough assumption on my part.\x02\x03",

            "#1500FMy name is Joshua, incidentally. Joshua Bright.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0x10F,
        (
            "#1447F#6PRies Argent. I'm a squire.\x02\x03",

            "#1448FSince we're on the subject, I'm curious how you\x01",
            "came to be familiar with us and our organization.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0x14,
        (
            "#214F#6PW-Wait a second, Joshua!\x02\x03",

            "Why does HER being there prove this isn't\x01",
            "an illusion?\x02\x03",

            "Is me being here not proof enough for you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x15,
        (
            "#1504F#11POh, you know, I don't think I've ever seen you\x01",
            "with that visor on before, have I?\x02\x03",

            "#1501FDoes that have to do with that delivery company\x01",
            "you mentioned running a while back? It suits you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0x14,
        (
            "#210F#6PYeah, that's it. We're doing awesome for \x01",
            "ourselves these days, too!\x02\x03",

            "#413F...But you didn't answer my question!\x02\x01",

            "#214FSurely you can tell just by looking at me that\x01",
            "I'm the real thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0x15,
        (
            "#1505F#11PGenerally when you're an illusion, the other people who\x01",
            "appear in it are people you're familiar with.\x02\x03",

            "That reason being is, they draw on and utilize knowledge\x01",
            "the victim has within in order to create the world.\x02\x03",

            "#1500FI've met the rest of you, but Ries is a complete stranger.\x02\x03",

            "And not any complete stranger--an unusual one, too.\x02\x03",

            "So she may not prove for certain this isn't an illusion,\x01",
            "but she does make it seem rather unlikely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0x14,
        (
            "#413F#6PI... I think I get what you're saying... Maybe...\x02\x03",

            "#212FBasically, the reason I don't prove this isn't an\x01",
            "illusion is because we're so close?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0x15,
        "#1504F#11PWell, you could put it that way, I guess...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x14,
        "#415F#6PHaha... Okay! That's fine by me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x11,
        (
            "#067F#6PHeehee...\x02\x03",

            "#560FAnyway, it's so good to see you again,\x01",
            "Joshua!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x15,
        (
            "#1501F#11PI'm glad to see you're looking well, too.\x02\x03",

            "You've grown a bit in this past half year,\x01",
            "haven't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x11,
        "#067F#6PAww. You noticed!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x15,
        (
            "#1512F#11PI'm surprised to see you got caught up in all\x01",
            "of this, though...\x02\x03",

            "#1514FIt must've been a real surprise to find yourself\x01",
            "here all of a sudden.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0x11,
        (
            "#563F#6PYeah... It still doesn't feel completely real to\x01",
            "me even after all this time, to be honest.\x02\x03",

            "#064FOh, right...\x02\x03",

            "#063FUmm... You don't know where Estelle could be,\x01",
            "do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0x15,
        (
            "#1503F#11P...I wish I did.\x02\x03",

            "#1505FThat said, I'm sure she was surrounded\x01",
            "by the same white light that I was.\x02\x03",

            "#1502FI'd say the odds are fairly high that she's\x01",
            "somewhere in Phantasma like us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0x11,
        (
            "#561F#6PO-Oh...\x02\x03",

            "#064FActually...where were you before you ended up\x01",
            "here, anyway?\x02\x03",

            "Your last letter said that you were in Erebonia.\x01",
            "Were you still there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x15,
        (
            "#1500F#11POh, no. Not anymore.\x02\x03",

            "We're over in Crossbell at the moment...\x01",
            "or were, with the situation as it is now.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #322
        0x14,
        (
            "#213F#6PReally?!\x02\x03",

            "We were flying over there before I ended up\x01",
            "here, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0x15,
        (
            "#1504F#11PYou were?\x02\x03",

            "#1503FHmm... I wonder if there's anything to that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0x13,
        (
            "#272F#6PIt's relatively close to Liberl, so that may have\x01",
            "something to do with it.\x02\x03",

            "#270FI myself was in Erebonia, but I was in the town\x01",
            "closest to the border with Liberl...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0x15,
        "#1500F#11POh, right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0x12,
        (
            "#176F#6P...I've a question for you, Father Graham.\x02\x03",

            "#178FSupposing that we assume all of this was caused\x01",
            "by an incredibly powerful artifact...\x02\x03",

            "...do you think such a thing would be able to exert\x01",
            "its influence as far as Crossbell or Parm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0x109,
        (
            "#1065F#5PI seriously, seriously doubt it.\x02\x03",

            "#1063FThe only thing I can think of that was\x01",
            "able to affect that wide an area was the\x01",
            "Aureole's Orbal Shutdown Phenomenon.\x02\x03",

            "That actually DID reach the southern edge\x01",
            "of Erebonia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x12,
        (
            "#176F#6PI see...\x02\x03",

            "#175FSo it would need to be something as powerful\x01",
            "as one of the Sept-Terrions, then.\x02\x03",

            "Although speaking of which...is the Aureole \x01",
            "itself still unaccounted for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x11,
        "#065F#6PYou can't mean this is the work of the Aureole!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0x109,
        (
            "#1065F#5PI don't think we should rule out the possibility,\x01",
            "Tita.\x02\x03",

            "#1063FBut even if we assume the Aureole is involved\x01",
            "in some way, that wouldn't answer most of the\x01",
            "questions we want answers to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0x13,
        (
            "#270F#6PIndeed... Such as who our enemies are or how\x01",
            "Grancel ended up filled with fiends and magic\x01",
            "barriers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0x10F,
        (
            "#1446F#5POr how we ended up facing actual embodiments\x01",
            "of devils from church scripture or the presence\x01",
            "of the higher elements...\x02\x03",

            "#1443FUntil we have a theory that can explain all of\x01",
            "those mysteries, we should probably refrain\x01",
            "from jumping to conclusions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0x12,
        "#176F#6PI would have to agree.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0x15,
        (
            "#1505F#11PStill, that being the case...\x02\x03",

            "#1502F...I'd like to propose we focus on working out\x01",
            "what happened to Grancel first and foremost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x109,
        (
            "#1065F#6PMy thoughts exactly.\x02\x03",

            "#1063FI know you're probably worried about Estelle\x01",
            "right now, but would you be up for helping us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0x15,
        (
            "#1513F#11PThat was my intention from the beginning.\x02\x03",

            "#1514FI can't very well turn my back on friends in need,\x01",
            "for one thing.\x02\x03",

            "Besides, I think I'll find her a lot faster by helping\x01",
            "out rather than sitting in here worrying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x11,
        "#560F#6PI hope we do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x14,
        (
            "#413F#6P*sigh* Well, I'll be glad to have you with us,\x01",
            "at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0x109,
        "#1078F#6PThat's what I wanted to hear! Cheers, man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0x10F,
        (
            "#1448F#6PWell, as soon as we're ready, we should make\x01",
            "our way back to the capital.\x02\x03",

            "I expect something will have changed there as\x01",
            "a result of us releasing Joshua from his stone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0x15,
        "#1500F#11PRight.\x02",
    )

    CloseMessageWindow()

    def lambda_D217():
        OP_6B(2600, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D217)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_A2(0x2714)
    OP_28(0x2D, 0x4, 0x4)
    OP_28(0x2D, 0x4, 0x8)
    OP_28(0x2D, 0x1, 0x1)
    OP_28(0x2D, 0x1, 0x2)
    OP_3F(0x356, 1)
    OP_DB(0x0, 0x1)
    OP_A2(0x25C7)
    Call(6, 11)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    ClearChrFlags(0xF0, 0x80)
    ClearChrFlags(0xF1, 0x80)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_DD(0x1, 0x0, 0x0, 16640, 0, 0, 0)
    FadeToDark(0, 0, -1)
    OP_C0(0x20, 0x1, 0x4100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_6D(390, 4000, -1290, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(450, 0)
    SetChrPos(0x0, 390, 4000, -1290, 180)
    SetChrPos(0x1, 390, 4000, -1290, 180)
    SetChrPos(0x2, 390, 4000, -1290, 180)
    SetChrPos(0x3, 390, 4000, -1290, 180)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_E5(0x2, 0xFF, 0x13, 700)
    Call(0, 5)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_18_B3AA end

    SaveToFile()

Try(main)
