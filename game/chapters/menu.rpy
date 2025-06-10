label menu:
    call screen menu_screen

screen menu_screen:
    add "bg_menu"
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
            sensitive persistent.chapter_0 == True
        
        imagebutton:
            auto "chapter_2_%s"
            action Jump("chapter_2_intro")
            sensitive persistent.chapter_1 == True

        imagebutton:
            auto "chapter_3_%s"
            action Jump("chapter_3")
            sensitive persistent.chapter_2 == True
        
        imagebutton:
            auto "nextchapter_%s"
            action Jump("menu_screen_2")


label menu_screen_2:
    call screen menu_screen_2

screen menu_screen_2:
    add "bg_menu"
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 20
        yoffset 30

        imagebutton:
            auto "back_%s"
            action Jump("menu")

        # imagebutton:
        #     auto "chapter_4_%s"
        #     action Jump("chapter_4_intro")
        #     sensitive persistent.chapter_3 == True
        
        # imagebutton:
        #     auto "chapter_5_%s"
        #     action Jump("chapter_5_intro")
        #     sensitive persistent.chapter_4 == True
        
        # imagebutton:
        #     auto "chapter_6_%s"
        #     action Jump("chapter_6_intro")
        #     sensitive persistent.chapter_5 == True

        # imagebutton:
        #     auto "chapter_7_%s"
        #     action Jump("chapter_7_intro")
        #     sensitive persistent.chapter_6 == True
        

