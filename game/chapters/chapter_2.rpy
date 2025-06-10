screen chapter_2_introscreen:
    vbox:
        spacing 20
        xalign 0.5
        yalign 0.5
        text "Chapter 2: Arrays" size 60 color "#FFFFFF" outlines [(5, "#000000", 0, 0)]

label chapter_2_intro:
    show black
    pause 1.0
    show screen chapter_2_introscreen
    pause 2.0
    scene mt tree with dissolve
    pause 1.0
    hide screen chapter_2_introscreen
    show adrian normal:
        smaller
    with dissolve

    a "Welcome to Chapter 2"
    a "In this chapter, we will be learning about arrays"
    a "What is an array?"
    menu:
        "A data structure that stores a fixed-size sequence of elements of the same type":
            a "Correct! An array is a data structure that stores a fixed-size sequence of elements of the same type"
        "A type of algorithm":
            a "Incorrect. An array is not an algorithm, but it can be used in algorithms"
        "A programming language":
            a "Incorrect. An array is not a programming language, but it can be implemented in one"
    jump chapter_2_basics