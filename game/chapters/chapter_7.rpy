# Chapter 7: Binary Search Trees (Red-Black Trees)
# Topics:
# - The logic of Red-Black Trees
# - Operations
# - Re-coloring and Rotation cases

default chapter_7_progress = 0

default chapter_7_RB_Logic_quiz = 0
default chapter_7_RB_Operations_quiz = 0
default chapter_7_Recoloring_Rotation_quiz = 0

label chapter_7_intro:

    call hideall
    play sound "sfx/start.mp3"
    stop music fadeout 1.0
    
    scene black
    pause 1.0

    show screen chapter_
    scene mt tree with dissolve
    pause 2.0
    hide screen chapter_
    
    show screen menu_btn
    
    play music "bgm/city-high-life.mp3" fadein 1.0
    show adrian smiling at center:
        smaller
    with dissolve
    
    show adrian nocomment
    a "Here Have this Honey"
    a "Shhh dont tell anyone I have this"
    a "I took it from a bear"

    show adrian smiling
    a "Welcome to Chapter 7: Red-Black Trees"

label chapter_7_RB_Logic:
    
    a "So what are Red-Black Trees"
    a "Theyre just different"
    a "Red-Black Trees are a type of self-balancing binary search tree"
    a "They ensure that the tree remains approximately balanced during insertions and deletions"
    a "This balance is crucial for maintaining efficient search, insertion, and deletion operations"
    a "Red-Black Trees have the following properties:"
    a "1. Each node is either red or black"
    a "2. The root is always black"
    a "3. All leaves (NIL nodes) are black"
    a "4. If a red node has children, then both children must be black"
    a "5. Every path from a node to its descendant NIL nodes must have the same number of black nodes"

    $ chapter_7_progress =+ 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Alright, let’s see what you’ve learned. Time for a quick quiz!"
    jump chapter_7_RB_Logic_Quiz

label chapter_7_RB_Logic_Quiz:
    #5POINTS
    $ chapter_7_RB_Logic_quiz = 0
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal


    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_7_RB_Logic_quiz] out of 5."
    jump chapter_7_RB_Operations

label chapter_7_RB_Operations:
    a "Red-Black Trees support standard binary search tree operations such as {b}insertion, deletion, and search{/b}"
    a ""

    $ chapter_7_progress =+ 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Alright, let’s see what you’ve learned. Time for a quick quiz!"
    jump chapter_7_RB_Operations_Quiz




label chapter_7_RB_Operations_Quiz:
    #5POINTS
    $ chapter_7_RB_Operations_quiz = 0
    
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal


    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_7_RB_Operations_quiz] out of 5."
    jump chapter_7_Recoloring_Rotation

label chapter_7_Recoloring_Rotation:



    $ chapter_7_progress =+ 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Alright, let’s see what you’ve learned. Time for a quick quiz!"
    jump chapter_7_Recoloring_Rotation_Quiz

label chapter_7_Recoloring_Rotation_Quiz:
    #5POINTS
    $ chapter_7_Recoloring_Rotation_quiz = 0
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal


    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_7_Recoloring_Rotation_quiz] out of 5."

    jump chapter_7_restart

label chapter_7_restart:
    $ chapter_7_test = (
        chapter_7_RB_Logic_quiz +
        chapter_7_RB_Operations_quiz +
        chapter_7_Recoloring_Rotation_quiz
    )

    a "Your score is [chapter_7_test]"
    a "Let's see how well you do in the {size=+20}CHAPTER QUIZ"

    if chapter_6_test <= 10:
        show adrian worried
        jump chapter_7_quiz_easy
    elif chapter_6_test <= 18:
        show adrian neutral
        jump chapter_7_quiz_medium
    else:
        show adrian proud
        jump chapter_7_quiz_hard

label chapter_7_quiz_easy:
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal


    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"

    jump chapter_7_performance
    
label chapter_7_quiz_medium:
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal


    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    
    jump chapter_7_performance

label chapter_7_quiz_hard:
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal


    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    jump chapter_7_performance

label chapter_7_performance:

# Red-Black Logic
    if chapter_7_RB_Logic_quiz < 2:
        a "You need to review the logic behind Red-Black Trees."
        a "Focus on the properties that maintain balance and prevent degeneration."
    elif chapter_7_RB_Logic_quiz < 3:
        a "You did okay in Red-Black Tree logic, but there's room for improvement."
        a "Revisit how the tree maintains height and structure."

# Operations
    if chapter_7_RB_Operations_quiz < 2:
        a "You need to review Red-Black Tree operations."
        a "Pay attention to how insertions and deletions trigger fixes."
    elif chapter_7_RB_Operations_quiz < 3:
        a "You did okay in Operations, but there's room for improvement."
        a "Try tracing how violations are resolved during updates."

# Recoloring & Rotation
    if chapter_7_Recoloring_Rotation_quiz < 2:
        a "You need to review Re-coloring and Rotation cases."
        a "Understand how LL, RR, LR, and RL cases are handled."
    elif chapter_7_Recoloring_Rotation_quiz < 3:
        a "You did okay in Re-coloring and Rotation, but there's room for improvement."
        a "Practice visualizing how color changes and rotations restore balance."

    jump chapter_7_end

label chapter_7_end: