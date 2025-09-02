label menu_select:
    call hideall
    scene bg_blank
    show screen menu_select_screen
    
    with dissolve
    pause 0.5
    show adrian normal:
        xalign 0.3
        smaller
    play music "bgm/lets-learn.mp3"
    hide window
    while True:
        $ renpy.pause(0.1, hard=True)


    
    return



#Chapter Menu Thingy
label menu:
    call hideall
    scene black
    show screen menu_screen
    show black
    with dissolve
    pause 0.5
    play music "bgm/menu.mp3"
    hide window
    while True:
        $ renpy.pause(0.1, hard=True)

    return


screen menu_select_screen:
    frame:
        xalign 0.85
        yalign 0.2
        xpadding 50
        ypadding 50
        vbox:
            xalign 0.5
            spacing 30
            text "{size=+10}Select":
                xalign 0.5

            frame:
                xalign 0.5
                xpadding 30
                textbutton "{size=+5}Chapter Select":
                    text_color "#00BFFF"
                    text_hover_color "#FFD700"
                    action [Jump("menu"), Hide("menu_select_screen")]
            frame:
                xalign 0.5
                xpadding 110
                textbutton "{size=+5}Scores":
                    text_color "#00BFFF"
                    text_hover_color "#FFD700"
                    action [Hide("menu_select_screen"), ShowMenu("StatsUI")]



screen menu_screen:
    add "bg_menu"
    hbox:
        xalign 1.0
        spacing 20

        imagebutton:

            xoffset -30
            yoffset 30
            auto "UI/stats_%s.png"
            action ShowMenu("StatsUI")

        frame:
            xoffset -30
            yoffset 30
            ypadding 20
            xpadding 20
            textbutton "Main Menu":
                text_color "#00BFFF"
                text_hover_color "#FFD700"
                action [Jump("menu_select"), Hide("menu_screen")]

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 20
        yoffset 30

        imagebutton:
            auto "chapter_0_%s"
            action Jump("chapter_0")
        
        imagebutton:
            auto "chapter_1_%s"
            action Jump("chapter_1_intro")

        
        imagebutton:
            auto "chapter_2_%s"
            action Jump("chapter_2_intro")


        imagebutton:
            auto "chapter_3_%s"
            action Jump("chapter_3_intro")

        imagebutton:
            auto "nextchapter_%s"
            action [Hide("menu_screen"), Show("menu_screen_2")]
            

screen menu_screen_2:
    add "bg_menu"

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/stats_%s.png"
        action ShowMenu("StatsUI")
    
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 20
        yoffset 30

        imagebutton:
            auto "back_%s"
            action [Hide("menu_screen_2"), Show("menu_screen")]

        imagebutton:
            auto "chapter_4_%s"
            action [Hide("menu_screen_2"),Jump("chapter_4_intro")]

        
        imagebutton:
            auto "chapter_5_%s"
            action Jump("chapter_5_intro")

        
        imagebutton:
            auto "chapter_6_%s"
            action Jump("chapter_6_intro")


        imagebutton:
            auto "nextchapter_%s"
            action [Hide("menu_screen"), Show("menu_screen_3")]

screen menu_screen_3:
    add "bg_menu"

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/stats_%s.png"
        action ShowMenu("StatsUI")
    
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 20
        yoffset 30

        imagebutton:
            auto "back_%s"
            action [Hide("menu_screen_3"), Show("menu_screen_2")]

        # imagebutton:
        #     auto "chapter_7_%s"
        #     action Jump("chapter_4_intro")

        
        # imagebutton:
        #     auto "chapter_8_%s"
        #     action Jump("chapter_5_intro")

        
        # imagebutton:
        #     auto "chapter_9_%s"
        #     action Jump("chapter_6_intro")


        imagebutton:
            auto "nextchapter_%s"
            action [Hide("menu_screen_3"), Show("menu_screen_4")]

screen menu_screen_4:

    add "bg_menu"

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/stats_%s.png"
        action ShowMenu("StatsUI")
    
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 20
        yoffset 30

        imagebutton:
            auto "back_%s"
            action [Hide("menu_screen_4"), Show("menu_screen_3")]

        vbox:
            yalign 0.5
            frame:
                yalign 0.5
                ypadding 20
                xpadding 20
                textbutton "Stack Minigame":
                    text_color "#00BFFF"
                    text_hover_color "#FFD700"
                    action Jump("stack_minigame2")
            frame:
                yalign 0.5
                ypadding 20
                xpadding 20
                textbutton "Stack Minigame":
                    text_color "#00BFFF"
                    text_hover_color "#FFD700"
                    action Jump("stack_minigame3")

        # imagebutton:
        #     auto "chapter_10_%s"
        #     action Jump("chapter_4_intro")

        
        # imagebutton:
        #     auto "chapter_11_%s"
        #     action Jump("chapter_5_intro")

        
        # imagebutton:
        #     auto "chapter_12_%s"
        #     action Jump("chapter_6_intro")



        

