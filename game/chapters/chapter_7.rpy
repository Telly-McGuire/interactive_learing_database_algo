# Chapter 7: Binary Search Trees (Red-Black Trees)
# Topics:
# - The logic of Red-Black Trees
# - Operations
# - Re-coloring and Rotation cases

default chapter_7_progress = 0

default chapter_7_RB_Logic_quiz = 0
default chapter_7_RB_Operations_quiz = 0
default chapter_7_Recoloring_Rotation_quiz = 0

screen chapter_7_RBIntro:
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 200
        ypadding 60
        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5
            text "Red & Black Trees" size 60 color "#FFFFFF" outlines [(5, "#000000", 0, 0)]

label chapter_7_intro:

    call hideall
    play sound "sfx/start.mp3"
    stop music fadeout 1.0
    
    scene black
    pause 1.0

    show screen chapter_7_RBIntro
    scene mt tree with dissolve
    pause 2.0
    hide screen chapter_7_RBIntro
    
    show screen menu_btn
    
    play music "bgm/city-high-life.mp3" fadein 1.0
    show adrian smiling at center:
        smaller
    with dissolve
    
    image honey = "assets/honey.png"

    show adrian nocomment at left
    with move

    show honey at right
    with move
    a "Here Have this Honey"
    a "Shhh dont tell anyone I have this"
    a "I took it from a bear"
    play sound "sfx/success.mp3"
    hide honey
    show adrian at center
    with move


    show adrian smiling
    a "Welcome to Chapter 7: Red-Black Trees"

label chapter_7_RB_Logic:
    
    a "So what are Red-Black Trees"
    a "Theyre just different"
    a "Red-Black Trees are a type of self-balancing binary search tree"

    show screen ch_7_RedBlackTrees
    a "This is where-{nw}"
    a "{cps=100}Omg why is this so {size=+20}{b}}obnoxious"
    a "Ugh, just read it over"
    a "In a Red-Black Tree, each node has an extra bit for denoting the color of the node, either red or black"

    a "They ensure that the tree remains approximately balanced during insertions and deletions"
    a "This balance is crucial for maintaining efficient search, insertion, and deletion operations"
    a "Red-Black Trees follow specific properties to maintain their balance:"
    a "When will he remove this screen"
    hide screen ch_7_RedBlackTrees
    a "There we go"
    a "Thank you-{nw}"
    show screen ch_7_RedBlackTrees
    a "{size=+30}{b}OMG"
    a "{cps=100}Ugh fine, just read it{nw}"
    a "Are you done yet?"

    menu:
        "Yes":
            hide screen ch_7_RedBlackTrees
        "No":
            a "{cps=100}Ugh fine, just read it"
    hide screen ch_7_RedBlackTrees
    a "Wait OMG"
    a "{size=+100}YES!"


    screen ch_7_RedBlackTrees:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 60
            ypadding 60
            vbox:
                spacing 20
                text "{size=+20}{b}Red-Black Trees{/b}" size 50 color "#FF0000" outlines [(4, "#000000", 0, 0)]

                hbox:
                    spacing 50
                    vbox:
                        spacing 15
                        xalign 0.5
                        yalign 0.5
                        text "{b}Overview{/b}" size 32 color "#00FF00" outlines [(2, "#000000", 0, 0)]
                        text "Red-Black Trees are a type of self-balancing binary search tree" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "They ensure the tree remains approximately balanced during insertions and deletions" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "This balance is crucial for efficient search, insertion, and deletion operations" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]

                    vbox:
                        spacing 15
                        xalign 0.5
                        yalign 0.5
                        text "{b}Properties{/b}" size 32 color "#00FF00" outlines [(2, "#000000", 0, 0)]
                        text "1. Each node is either red or black" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "2. The root is always black" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "3. All leaves (NIL nodes) are black" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "4. If a red node has children, both must be black" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "5. Every path from a node to its descendant NIL nodes must have the same number of black nodes" size 28 color "#FFD700" outlines [(2, "#000000", 0, 0)]

                imagebutton:
                    xalign 1.0
                    yalign 0.0
                    xoffset -30
                    yoffset 30
                    auto "UI/btn_back_%s.png"
                    action Return()

    show adrian explaining
    a "So why is it {color=#FF0000}Red{/color} and {color=#000000}Black{/color}?"   
    a "Red in the tree represents nodes that can be temporarily unbalanced" 
    a "While Black nodes help maintain overall balance" 

    image shrimple = "assets/shrimple.png"

    show shrimple onlayer overlay:
        zoom 0.2
        xpos 0.4
        ypos 0.8
    show adrian smiling
    a "As shrimple as that"    
    $ chapter_7_progress =+ 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Alright, let’s see what you’ve learned. Time for a quick quiz!"
    jump chapter_7_RB_Logic_Quiz

init python:
    import random
    chapter_7_RB_logic_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_7_RB_logic_order)

label chapter_7_RB_Logic_Quiz:
    #5POINTS
    $ chapter_7_RB_Logic_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_7_RB_logic_order:
        $ current_q = chapter_7_RB_logic_order.pop(0)

        if current_q == "q1":
            a "What color is the root node in a valid Red-Black Tree?"
            menu:
                
                "Red":
                    a "Incorrect! Red roots violate Red-Black Tree rules."
                "Black":
                    $ chapter_7_RB_Logic_quiz += 1
                    a "Correct! The root must always be black."
                "Either":
                    a "Incorrect! The root must be black for balance."

        elif current_q == "q2":
            a "Which property helps ensure balance in a Red-Black Tree?"
            menu:
                
                "All leaves must be red":
                    a "Incorrect! Leaves are always black."
                "Every node must have two children":
                    a "Incorrect! That’s not a Red-Black Tree requirement."
                "No two red nodes can be adjacent":
                    $ chapter_7_RB_Logic_quiz += 1
                    a "Correct! This prevents long chains of red nodes."

        elif current_q == "q3":
            a "What happens during insertion in a Red-Black Tree?"
            menu:
                "Only rotations are used":
                    a "Incorrect! Recoloring is also essential."

                "Recoloring and rotations may occur":
                    $ chapter_7_RB_Logic_quiz += 1
                    a "Correct! These maintain Red-Black properties."
                
                "No balancing is needed":
                    a "Incorrect! Red-Black Trees self-balance after insertions."

        elif current_q == "q4":
            a "What is the color of all leaf (NIL) nodes in a Red-Black Tree?"
            menu:
               
                "Red":
                    a "Incorrect! Red leaves would violate tree properties." 
                "Black":
                    $ chapter_7_RB_Logic_quiz += 1
                    a "Correct! All NIL leaves are black by definition."
                "Depends on the parent":
                    a "Incorrect! Leaf color is always black."

        elif current_q == "q5":
            a "Which of the following is true about Red-Black Trees?"
            menu:
                "They guarantee logarithmic height":
                    $ chapter_7_RB_Logic_quiz += 1
                    a "Correct! That’s why they’re efficient for search operations."
                "They are always perfectly balanced":
                    a "Incorrect! They’re approximately balanced, not perfect."
                "They use AVL rotations":
                    a "Incorrect! Red-Black Trees have their own rotation logic."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_7_RB_Logic_quiz] out of 5."
    jump chapter_7_RB_Operations

label chapter_7_RB_Operations:

    show adrian smiling
    a "{size=+30}{b}OPERTIONS"
    a "as in Ope, and Rations"
    show adrian nocomment
    a "..."
    show adrian smug
    a "Teehee"
    show adrian explaining
    show screen ch_7_RB_Operations
    a "Red-Black Trees support standard binary search tree operations such as {b}insertion, deletion, and search{/b}."
    a "But what makes them special is how they maintain balance through color properties and rotations."
    a "This ensures operations stay efficient—typically in {i}O(log n){/i} time."
    a "It's important to understand how these operations work in the context of Red-Black Trees."
    hide screen ch_7_RB_Operations


    screen ch_7_RB_Operations:
        frame:
            xalign 0.01
            yalign 0.01
            xpadding 20
            ypadding 30
            vbox:
                spacing 20
                text "{size=+20}{b}Red-Black Tree Operations{/b}" size 30 color "#FF0000" outlines [(4, "#000000", 0, 0)]
        frame: 
            xalign 0.95
            yalign 0.5
            xpadding 30
            ypadding 100
            vbox:
                spacing 15
                xalign 0.5
                yalign 0.5
                text "{b}Supported Operations{/b}" size 32 color "#00FF00" outlines [(2, "#000000", 0, 0)]
                text "Insetion" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "Deletion" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "Search" size 28 color "#FFD700" outlines [(2, "#000000", 0, 0)]
        frame:
            xalign 0.01
            yalign 0.5 
            xpadding 20
            ypadding 100
            vbox:
                spacing 15
                xalign 0.5
                yalign 0.5
                text "{b}Balancing Rules{/b}" size 32 color "#00FF00" outlines [(2, "#000000", 0, 0)]
                text "- The root is always black" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "- Red nodes can't have red children" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "- Every path to leaves must have the same\nnumber of black nodes" size 28 color "#FFD700" outlines [(2, "#000000", 0, 0)]


    a "But I feel like its better with visuals"
    
    
    #{{ADD VISUALS HERE}}
    
    show adrian happy
    a "Did you get all that?"
    a "Great!"


    $ chapter_7_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Alright, let’s see what you’ve learned. Time for a quick quiz!"
    jump chapter_7_RB_Operations_Quiz




init python:
    import random
    chapter_7_RB_operations_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_7_RB_operations_order)

label chapter_7_RB_Operations_Quiz:
    #5POINTS
    $ chapter_7_RB_Operations_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_7_RB_operations_order:
        $ current_q = chapter_7_RB_operations_order.pop(0)

        if current_q == "q1":
            a "What operation is used when a red node is inserted and its parent is also red?"
            menu:
                
                "Only rotation":
                    a "Incorrect! Recoloring is often needed to fix red-red violations."
                "No operation needed":
                    a "Incorrect! Red-Black Tree properties must be restored."
                "Recoloring and possibly rotation":
                    $ chapter_7_RB_Operations_quiz += 1
                    a "Correct! This violates the red-red rule and may require both recoloring and rotation."

        elif current_q == "q2":
            a "Which rotation is used in a Left-Right imbalance during insertion?"
            menu:
                "Right Rotation only":
                    a "Incorrect! That works for Left-Left cases."
                "Left Rotation followed by Right Rotation":
                    $ chapter_7_RB_Operations_quiz += 1
                    a "Correct! That’s a double rotation to restore balance."
                
                "Left Rotation only":
                    a "Incorrect! That’s used for Right-Right cases."

        elif current_q == "q3":
            a "What is the goal of rotations in Red-Black Trees?"
            menu:
                "To restore balance and maintain properties":
                    $ chapter_7_RB_Operations_quiz += 1
                    a "Correct! Rotations help preserve the tree’s structure and rules."
                "To remove red nodes":
                    a "Incorrect! Red nodes are allowed—just not adjacent."
                "To increase tree height":
                    a "Incorrect! Rotations aim to keep the tree shallow."

        elif current_q == "q4":
            a "When does a single rotation suffice during insertion?"
            menu:
                
                "When the imbalance is Left-Right":
                    a "Incorrect! That requires a double rotation."
                "When the root is red":
                    a "Incorrect! The root must be black, but fixing it may need more than rotation."
                "When the imbalance is Left-Left or Right-Right":
                    $ chapter_7_RB_Operations_quiz += 1
                    a "Correct! These cases only need one rotation to fix."

        elif current_q == "q5":
            a "What happens after a rotation in a Red-Black Tree?"
            menu:
                "Recoloring may be needed to restore properties":
                    $ chapter_7_RB_Operations_quiz += 1
                    a "Correct! Rotations alone don’t always fix color violations."
                "The tree is guaranteed balanced":
                    a "Incorrect! Further adjustments may be needed."
                "All nodes become black":
                    a "Incorrect! Red nodes are still allowed."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_7_RB_Operations_quiz] out of 5."
    jump chapter_7_Recoloring_Rotation

label chapter_7_Recoloring_Rotation:

    show adrian explaining
    a "Now that you’ve got a handle on the basic operations of Red-Black Trees, let’s explore how they stay balanced after insertions and deletions."
    a "Unlike regular binary search trees, Red-Black Trees maintain their structure using a smart mix of {b}recoloring{/b} and {b}rotations{/b}."

    show screen ch_7_Recoloring_Rotation
    show adrian at left
    with move
    a "Recoloring is the simpler of the two techniques."
    a "Look at this black-board here"

    show adrian happy
    a "LOOK at me I look like i have {b}one{/b} {size=+20}eye"
    show adrian smug
    a "Cyclops :3"
    show adrian explaining
    a "Recoloring involves changing the colors of nodes to fix violations of Red-Black properties without altering the tree's shape."
    a "On the other hand, rotations are structural changes that adjust the tree's shape while preserving the in-order sequence of nodes."
    a "There are two types of rotations: left and right."
    a "Together, recoloring and rotations ensure that Red-Black Trees remain balanced, keeping operations efficient."

    hide screen ch_7_Recoloring_Rotation
    show adrian at center
    with move
    a "Nice, that was a quick visual tour. Recoloring and rotations together keep things balanced."
    $ chapter_7_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Alright, let’s see what you’ve learned. Time for a quick quiz!"
    jump chapter_7_Recoloring_Rotation_Quiz


    screen ch_7_Recoloring_Rotation:
        frame:
            xalign 0.9
            yalign 0.2
            xminimum 900
            ymaximum 520
            xpadding 40
            ypadding 100
            has vbox

            spacing 14

            # Header
            hbox:
                spacing 12
                text "{size=+24}{b}Recoloring & Rotations{/b}{/size}" color "#FFD56B" outlines [(2, "#000000", 0, 0)]
                null
                text "Chapter 7" color "#A0A9B8" xalign 1.0

            # Divider
            add Solid("#2a2f36", xysize=(1,2)) xalign 0.0

            # Body: two columns - left explains recoloring, right shows rotations
            hbox:
                spacing 24

                vbox:
                    spacing 10
                    xmaximum 520

                    frame:
                        background Solid("#262b31")
                        xpadding 12
                        ypadding 12
                        has vbox

                        text "{b}Recoloring (concept){/b}" color "#9FE6A0" outlines [(1, "#000000", 0, 0)] size 20
                        text "Change node colors to fix red-red violations without changing tree shape." color "#dfe6ea" size 18
                        text "When the uncle is red, recoloring the parent and uncle black and the grandparent red often resolves the issue." color "#c9d1d9" size 16


                    frame:
                        background Solid("#262b31")
                        xpadding 12
                        ypadding 12
                        has vbox

                        text "{b}When to recolor{/b}" color "#9FE6A0" size 18
                        text "- Inserted node is red and uncle is red." color "#c9d1d9" size 16
                        text "- Fixes color violations without rotations." color "#c9d1d9" size 16

                vbox:
                    spacing 10
                    xmaximum 340

                    frame:
                        background Solid("#262b31")
                        xpadding 12
                        ypadding 12
                        has vbox

                        text "{b}Rotations (structure){/b}" color "#9FD6FF" outlines [(1, "#000000", 0, 0)] size 20
                        text "Use rotations to change the tree shape while preserving in-order ordering." color "#dfe6ea" size 16
                        text "Left rotation: promotes the right child. Right rotation: promotes the left child." color "#c9d1d9" size 16

                        hbox:
                            spacing 8
                            # example images (optional)
                            add "assets/rotation_left.png" xalign 0.0 zoom 0.3 
                            add "assets/rotation_right.png" xalign 0.0 zoom 0.3 



                    frame:
                        background Solid("#262b31")
                        xpadding 12
                        ypadding 12
                        has vbox

                        text "{b}When rotations are needed{/b}" color "#9FD6FF" size 18
                        text "- Parent is red and uncle is black (red-red violation)." color "#c9d1d9" size 16
                        text "- Single rotation for LL/RR, double rotation for LR/RL." color "#c9d1d9" size 16

            # Footer: actions and quick tips
            hbox:
                spacing 14
                text "Tip: Recolor first when possible; rotate when structure must change." color "#9fb0c6" xalign 0.0
                # null
                # textbutton "Continue" action Return() xminimum 160 yminimum 42 align (0.5, 0.5):
                #     background Frame("UI/btn_frame.png", 8) if renpy.exists("UI/btn_frame.png") else "#3b4750"
                #     foreground "#ffffff"
                #     insensitive_background "#2b3338"
                #     xpadding 12
                #     ypadding 6

init python:
    import random
    chapter_7_Recoloring_rotation_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_7_Recoloring_rotation_order)

label chapter_7_Recoloring_Rotation_Quiz:
    #5POINTS
    $ chapter_7_Recoloring_Rotation_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_7_Recoloring_rotation_order:
        $ current_q = chapter_7_Recoloring_rotation_order.pop(0)

        if current_q == "q1":
            a "What is the purpose of recoloring in Red-Black Trees?"
            menu:
                "To fix color violations without changing structure":
                    $ chapter_7_Recoloring_Rotation_quiz += 1
                    a "Correct! Recoloring helps restore Red-Black properties without rotations."
                "To remove red nodes":
                    a "Incorrect! Red nodes are allowed—just not adjacent."
                "To balance the tree height":
                    a "Incorrect! That’s the role of rotations."

        elif current_q == "q2":
            a "When is recoloring alone sufficient during insertion?"
            menu:

                "When the parent is black":
                    a "Incorrect! No fix is needed in that case."
                "When the root is red":
                    a "Incorrect! The root must always be black."
                "When the uncle of the inserted node is red":
                    $ chapter_7_Recoloring_Rotation_quiz += 1
                    a "Correct! This triggers recoloring without rotation."
        elif current_q == "q3":
            a "Which case requires both recoloring and rotation?"
            menu:                
                "When both parent and uncle are black":
                    a "Incorrect! No violation occurs."
                "When the parent is red and the uncle is black":
                    $ chapter_7_Recoloring_Rotation_quiz += 1
                    a "Correct! This violates the red-red rule and needs structural adjustment."

                "When the inserted node is black":
                    a "Incorrect! Black insertions rarely cause violations."

        elif current_q == "q4":
            a "What happens after a rotation in a Red-Black Tree?"
            menu:
                "Recoloring may be needed to maintain properties":
                    $ chapter_7_Recoloring_Rotation_quiz += 1
                    a "Correct! Rotations fix structure, but colors may still need adjustment."
                "All nodes become black":
                    a "Incorrect! Red nodes are still allowed."
                "The tree becomes perfectly balanced":
                    a "Incorrect! Red-Black Trees are approximately balanced."

        elif current_q == "q5":
            a "Which of the following is true about Red-Black Tree maintenance?"
            menu:

                "Only recoloring is used after deletion":
                    a "Incorrect! Deletion may require rotations too."
                "Rotation is never needed if recoloring is done":
                    a "Incorrect! Some cases require both."                
                "Recoloring and rotation work together to restore balance":
                    $ chapter_7_Recoloring_Rotation_quiz += 1
                    a "Correct! Both are essential for preserving Red-Black properties."

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

    if chapter_7_test <= 10:
        show adrian worried
        jump chapter_7_quiz_easy
    elif chapter_7_test <= 18:
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