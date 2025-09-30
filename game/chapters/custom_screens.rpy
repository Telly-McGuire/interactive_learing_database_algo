

label call_stats:
    call screen StatsUI
    return

screen StatsUI:
    add "bg_blank"
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 200
        ypadding 200

        vbox:
            spacing 40
            xalign 0.5
            yalign 0.1

            hbox:
                spacing 80

                vbox:
                    spacing 40
                    text "SCORES" size 40
                    text "Chapter 1: Abstract Data Structures" size 40
                    text "Chapter 2: Arrays" size 40
                    text "Chapter 3: Linked List" size 40
                    text "Chapter 4: Stacks & Queues"
                    text "Chapter 5: Trees" size 40
                
                vbox:
                    spacing 45
                    text ""
                    text "[chapter_1_score]" size 40
                    text "[chapter_2_score]" size 40
                    text "[chapter_3_score]" size 40
                    text "[chapter_4_score]" size 40
                    text "[chapter_5_score]" size 40

            frame:
                xalign 0.5
                textbutton "Submit Scores":    
                    text_size 28
                    action[Call("submit_all_chapter_scores")]


    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/btn_back_%s.png"
        action Return()

screen menu_btn:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/btn_menu_%s.png"
        action [Hide("menu_btn"),Call("warn_handler")]

label progress_check:
    call screen progressUI
    return

screen progressUI:
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 200
        ypadding 200
        vbox:
            spacing 40
            xalign 0.5
            yalign 0.1
            text "Chapter Progress" size 40
            text "Chapter 1 Progress: [chapter_1_progress] / 4" size 40
            text "Chapter 2 Progress: [chapter_2_progress] / 2" size 40
            text "Chapter 3 Progress: [chapter_3_progress] / 3" size 40
            text "Chapter 4 Progress: [chapter_4_progress] / 5" size 40
            text "Chapter 5 Progress: [chapter_5_progress] / 4" size 40
            text "Chapter 6 Progress: [chapter_6_progress] / 5" size 40

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/btn_back_%s.png"
        action Return()

label warn_handler:
    call screen warn
    return


screen warn:
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 50
        vbox:
            text "Are you sure you want to go back?"
            spacing 40
            hbox:
                xalign 0.5

                spacing 40
                vbox:
                    textbutton "Yes":
                        text_color "#00BFFF"
                        text_hover_color "#FFD700"
                        action [Hide("warn"), Jump("menu")]
                        text_size 28
                        
                vbox:
                    textbutton "No":
                        text_color "#00BFFF"
                        text_hover_color "#FFD700"
                        action [Return(), Hide("warn")]
                        text_size 28
    



