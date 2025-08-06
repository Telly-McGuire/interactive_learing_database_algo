
label menu:
    show black 
    with dissolve
    pause 0.5
    play music "bgm/menu.mp3"
    call screen menu_screen
    return

screen menu_screen:
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

        # imagebutton:
        #     auto "chapter_10_%s"
        #     action Jump("chapter_4_intro")

        
        # imagebutton:
        #     auto "chapter_11_%s"
        #     action Jump("chapter_5_intro")

        
        # imagebutton:
        #     auto "chapter_12_%s"
        #     action Jump("chapter_6_intro")



        

