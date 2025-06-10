
define a = Character("Adrian")

transform smaller:
    zoom 0.5

label start:
    stop music fadeout 1.0
    scene mt tree
    with dissolve
    show adrian smiling at left:
        smaller

    voice "menu/menu1.mp3"
    a "Hello"

    show adrian explaining:
        smaller

    voice "menu/menu2.mp3"
    a "Welcome To Interactive Learning : Datastructures & Algorithm"

    show adrian smiling:
        smaller

    voice "menu/menu3.mp3"    
    a "I am Adrian, I will be helping to teach you today"

    show adrian normal:
        smaller
    voice "menu/menu4.mp3"
    a "Nice to meet you"

    jump menu

    return
