# label splashscreen:
#     scene black
#     pause 1.0
#     show text "{size=100}{color=#938CE6}TMC Entertainment \n Presents{/color}{/size}" at truecenter 
#     with dissolve
#     pause 2.0
#     hide text 
#     with dissolve
#     pause 1.0

#     pause 1.0 
#     show image "assets/logo.png" at Position(xalign=0.5, yalign=0.3):
#         zoom 0.8
#     show text "{size=100}{color=#938CE6}Interactive Learning :{/color}\n{size=60}{color=#ffd700}Data Structures & Algorithms{/color}" at Position(xalign=0.5, yalign=0.8) 
#     with dissolve
#     pause 2.0
#     hide text with dissolve
#     hide image "assets/logo.png" with dissolve
    
#     pause 1.0
#     show image "assets/cpu_logo.png" at truecenter:
#         zoom 1.2
#     with dissolve
#     show text "In association with \n {color=#ffd700}{size=100}Central Philippine University{/color}{/size}" at Position(xalign=0.5, yalign=0.8)
#     with dissolve
#     pause 2.0

#     hide image "assets/logo.png" 
#     with dissolve
#     hide text with dissolve

#     pause 1.0
#     hide scene 
#     with dissolve
#     return



init python:
    def player_speak(event, interact=True, **kwargs):
        beeps = 0
        while beeps < 50:
            randosound = renpy.random.randint(0,2) 
            if event == "show":
                if randosound == 0:
                    renpy.sound.queue("audio/beep/huh.mp3", channel="sound")
                elif randosound == 1:
                    renpy.sound.queue("audio/beep/ra.mp3", channel="sound")
                elif randosound == 2:
                    renpy.sound.queue("audio/beep/be.mp3", channel="sound")
                spause = renpy.music.get_duration(channel = "sound")
            elif event == "slow_done" or event == "end":
                renpy.sound.stop(channel="sound")
            beeps += 1

define a = Character("Adrian", callback=player_speak )
define silent = Character(None, window=False)

transform smaller:
    zoom 0.5


default chapter_1_score = 0
default chapter_2_score = 0
default chapter_3_score = 0
default chapter_4_score = 0
default chapter_5_score = 0

label start:
    $ persistent.menu = False
    if persistent.menu == False:
        call database_user_info
    else:
        pass

    stop music fadeout 1.0
    scene mt tree
    with dissolve
    show adrian smiling at center:
        smaller

    if persistent.menu:
        a "Welcome Back!"
        a "Nice to see you again"
        jump menu_select
        
    else:
        pass

    a "Hello"

    show adrian explaining:
        smaller

    a "Welcome To Interactive Learning : Datastructures & Algorithm"

    show adrian smiling:
        smaller

   
    a "I am Adrian, I will be helping to teach you today"

    show adrian normal:
        smaller

    a "Nice to meet you"

    $ persistent.menu = True
    
    jump menu_select

    return
