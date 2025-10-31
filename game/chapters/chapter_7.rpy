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

    if persistent.chapter_7 == True:
        a "Hi welcome back to chapter 7"
        a "are you sure you want to go through this chapter again?"
        menu:
            "Yes":
                a "Pick a topic"
                menu:
                    "The Logic of Red-Black Trees":
                        jump chapter_7_RB_Logic
                    "Operations":
                        jump chapter_7_RB_Operations
                    "Re-coloring and Rotation Cases":
                        jump chapter_7_Recoloring_Rotation
            "No":
                jump menu
    else:
        pass
    
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

init python:
    import random
    chapter_7_easy_question_order = [
        "q1","q2","q3","q4","q5",
        "q6","q7","q8","q9","q10"
    ]
    random.shuffle(chapter_7_easy_question_order)

label chapter_7_quiz_easy:
    $ chapter_7_score = 0
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    show adrian smiling at center
    a "Welcome to the {b}Binary Search Tree Quiz{/b}! Let's test your BST knowledge."

    while chapter_7_easy_question_order:
        $ current_q = chapter_7_easy_question_order.pop(0)

        if current_q == "q1":
            a "What is the defining property of a Binary Search Tree (BST)?"
            menu:
                "All left subtree keys are less than the node's key; all right subtree keys are greater":
                    $ chapter_7_score += 1
                    a "Correct! BSTs maintain that left < node < right recursively."
                "All nodes have either 0 or 2 children":
                    a "Incorrect. That's a full binary tree property."
                "Nodes are arranged by insertion order only":
                    a "Incorrect. BST order depends on key comparisons."

        elif current_q == "q2":
            a "Which traversal of a BST yields the stored keys in sorted (increasing) order?"
            menu:
                "Post-order":
                    a "Incorrect. Post-order is left-right-root."
                "In-order":
                    $ chapter_7_score += 1
                    a "Correct! In-order traversal of a BST produces sorted keys."
                "Pre-order":
                    a "Incorrect. Pre-order is root-left-right."

        elif current_q == "q3":
            a "What is the average-case time complexity for search in a BST with n nodes (assuming random insertions)?"
            menu:
                "O(1)":
                    a "Incorrect. Average search isn't constant for BSTs."
                "O(log n)":
                    $ chapter_7_score += 1
                    a "Correct! Average-case search is O(log n) for reasonably balanced BSTs."
                "O(n^2)":
                    a "Incorrect. That's not a correct complexity for a single search."

        elif current_q == "q4":
            a "When inserting keys 1..n in increasing order into an initially empty BST, what shape does the tree take?"
            menu:
                "A balanced tree with height O(log n)":
                    a "Incorrect. Plain BST insertion without rebalancing won't balance."
                "A degenerate chain (linked-list shape) with height O(n)":
                    $ chapter_7_score += 1
                    a "Correct! Inserting sorted keys into a plain BST produces a skewed chain."
                "A perfect binary tree":
                    a "Incorrect. Perfect requires specific ordering."

        elif current_q == "q5":
            a "Which case when deleting a node from a BST is the simplest to handle?"
            menu:
                "Deleting a node with two children":
                    a "Incorrect. That requires finding successor/predecessor and rewiring."
                "Deleting a leaf node (no children)":
                    $ chapter_7_score += 1
                    a "Correct! Removing a leaf just clears its parent's pointer."
                "Deleting the root always":
                    a "Incorrect. Root deletion may be simple or complex depending on children."

        elif current_q == "q6":
            a "To delete a node with two children in a BST while preserving order, a common approach is to replace it with:"
            menu:
                "Its in-order predecessor (maximum in left subtree) or in-order successor (minimum in right subtree)":
                    $ chapter_7_score += 1
                    a "Correct! Replace with predecessor/successor then delete that node recursively."
                "The root of the whole tree always":
                    a "Incorrect. Replacing with global root breaks BST structure."
                "A random leaf from the tree":
                    a "Incorrect. Random replacement won't preserve BST ordering."

        elif current_q == "q7":
            a "Which data structure trick speeds up successive next (in-order successor) operations on nodes if parent pointers are not available?"
            menu:
                "Use a stack to perform iterative in-order traversal and remember the path":
                    $ chapter_7_score += 1
                    a "Correct! An explicit stack simulates recursion and yields successors efficiently."
                "Always restart in-order traversal from the root":
                    a "Incorrect. Restarting is inefficient."
                "Use a hash table of successor values":
                    a "Incorrect. Hashing needs precomputation and uses extra space."

        elif current_q == "q8":
            a "What is the worst-case time complexity for search in a plain BST with n nodes?"
            menu:
                "O(log n)":
                    a "Incorrect. That's average/balanced case."
                "O(n)":
                    $ chapter_7_score += 1
                    a "Correct! Worst-case (skewed tree) search is O(n)."
                "O(n log n)":
                    a "Incorrect. That's not a single-search complexity."

        elif current_q == "q9":
            a "Which augmented value stored at each node can support order-statistics (select/rank) queries efficiently?"
            menu:
                "Subtree size (number of nodes in subtree)":
                    $ chapter_7_score += 1
                    a "Correct! Storing subtree sizes enables select and rank in O(height) time."
                "Height of subtree only":
                    a "Incorrect. Height helps balancing but not rank/select directly."
                "Hash of subtree values":
                    a "Incorrect. Hashes don't help compute ranks."

        elif current_q == "q10":
            a "Which tree is a BST variant that guarantees O(log n) worst-case operations by automatically rebalancing?"
            menu:
                "Binary Heap":
                    a "Incorrect. Heaps don't provide ordered in-order traversal by key."
                "AVL tree or Red-Black tree (self-balancing BSTs)":
                    $ chapter_7_score += 1
                    a "Correct! AVL and Red-Black trees are self-balancing BSTs with O(log n) worst-case ops."
                "Trie":
                    a "Incorrect. Tries are prefix trees, not BSTs."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Your quiz score is: [chapter_7_score]"

    jump chapter_7_performance
    
init python:
    import random
    chapter_7_medium_question_order = [
        "q1","q2","q3","q4","q5",
        "q6","q7","q8","q9","q10",
        "q11","q12","q13","q14","q15"
    ]
    random.shuffle(chapter_7_medium_question_order)

label chapter_7_quiz_medium:
    $ chapter_7_score = 0
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    show adrian smiling at center
    a "Welcome to the {b}Binary Search Tree Quiz{/b}! Ready for 15 questions?"

    while chapter_7_medium_question_order:
        $ current_q = chapter_7_medium_question_order.pop(0)

        if current_q == "q1":
            a "Which traversal produces keys in ascending order for a BST?"
            menu:
                "Pre-order":
                    a "Incorrect. Pre-order visits root before subtrees."
                "In-order":
                    $ chapter_7_score += 1
                    a "Correct! In-order yields sorted keys for a BST."
                "Post-order":
                    a "Incorrect. Post-order visits children before parent."

        elif current_q == "q2":
            a "What is the worst-case height of a BST built by inserting n increasing keys?"
            menu:
                "O(log n)":
                    a "Incorrect. That's for balanced trees."
                "O(n)":
                    $ chapter_7_score += 1
                    a "Correct! Inserting sorted data into an unbalanced BST gives a chain of height O(n)."
                "O(1)":
                    a "Incorrect. Height can't be constant for arbitrary n."

        elif current_q == "q3":
            a "When deleting a node with two children in a BST, a common step is to replace it with:"
            menu:
                "The node's leftmost descendant in the right subtree (in-order successor) or rightmost in left subtree (predecessor)":
                    $ chapter_7_score += 1
                    a "Correct! Replace and then remove that successor/predecessor node."
                "A random leaf from the tree":
                    a "Incorrect. Random replacement won't preserve order."
                "The tree's root always":
                    a "Incorrect. Replacing with root breaks BST properties."

        elif current_q == "q4":
            a "What additional field stored at each node supports order-statistic (kth smallest) queries efficiently?"
            menu:
                "Subtree size (number of nodes in subtree)":
                    $ chapter_7_score += 1
                    a "Correct! Subtree sizes let you compute ranks/select in O(height)."
                "Hash of subtree values":
                    a "Incorrect. Hashes don't give rank information."
                "Depth from root only":
                    a "Incorrect. Depth doesn't help find kth element directly."

        elif current_q == "q5":
            a "Which data structure is most appropriate to get O(1) average-time membership checks but does not maintain order?"
            menu:
                "Binary Search Tree":
                    a "Incorrect. BSTs maintain order but not O(1) average membership."
                "Hash table":
                    $ chapter_7_score += 1
                    a "Correct! Hash tables give average O(1) membership but don't preserve sorted order."
                "Binary heap":
                    a "Incorrect. Heaps don't guarantee O(1) membership and don't maintain sorted order."

        elif current_q == "q6":
            a "If you want guaranteed O(log n) worst-case operations, which structure should you use instead of a plain BST?"
            menu:
                "Balanced BST like AVL or Red-Black tree":
                    $ chapter_7_score += 1
                    a "Correct! Self-balancing BSTs provide worst-case logarithmic bounds."
                "Unbalanced BST with random keys":
                    a "Incorrect. Random keys give expected behavior but not guaranteed worst-case."
                "Linked list":
                    a "Incorrect. Linked lists have linear-time search."

        elif current_q == "q7":
            a "Which traversal pair can uniquely reconstruct a binary tree (values distinct)?"
            menu:
                "Pre-order and Post-order":
                    a "Incorrect. Pre+Post alone don't uniquely reconstruct in general."
                "In-order and Pre-order":
                    $ chapter_7_score += 1
                    a "Correct! In-order plus pre-order (or in-order plus post-order) uniquely define the tree."
                "Level-order alone":
                    a "Incorrect. Level-order by itself doesn't capture full structure without markers."

        elif current_q == "q8":
            a "What is the time complexity to find the in-order successor of a node in a BST if nodes have parent pointers?"
            menu:
                "O(1) worst-case always":
                    a "Incorrect. Some cases need climbing ancestors."
                "O(h) where h is tree height":
                    $ chapter_7_score += 1
                    a "Correct! Successor can be found in O(h) by checking right subtree or climbing to ancestor."
                "O(n^2)":
                    a "Incorrect. That's not applicable for a single successor lookup."

        elif current_q == "q9":
            a "Which insertion strategy yields a perfectly balanced BST for a known sorted array of keys?"
            menu:
                "Insert keys in sorted order 1..n into an empty BST":
                    a "Incorrect. That creates a skewed tree."
                "Recursively insert the middle element then build left and right halves":
                    $ chapter_7_score += 1
                    a "Correct! Building from middle produces a balanced BST (perfect if sizes match)."
                "Insert keys in reverse sorted order only":
                    a "Incorrect. Reverse sorted also produces a chain."

        elif current_q == "q10":
            a "Which of these operations is NOT naturally supported by a BST in O(height) time?"
            menu:
                "Search for a key":
                    a "Incorrect. Search is O(height)."
                "Find minimum or maximum":
                    a "Incorrect. Min/max are O(height) by following left/right chains."
                "Get median in O(1) without augmentation":
                    $ chapter_7_score += 1
                    a "Correct! Finding median in O(1) requires extra augmentation like order-statistic trees."

        elif current_q == "q11":
            a "What happens to BST search complexity if the tree is balanced versus skewed?"
            menu:
                "Balanced: O(log n); Skewed: O(n)":
                    $ chapter_7_score += 1
                    a "Correct! Balance dramatically affects search complexity."
                "Balanced: O(n); Skewed: O(log n)":
                    a "Incorrect. That reverses the truth."
                "Both always O(n) regardless of shape":
                    a "Incorrect. Shape matters."

        elif current_q == "q12":
            a "Which technique helps keep a BST roughly balanced without strict invariants and with good practical performance?"
            menu:
                "Randomized insertion order (shuffle keys before inserting)":
                    $ chapter_7_score += 1
                    a "Correct! Random insertion order yields good expected height in practice."
                "Always insert larger keys to the left":
                    a "Incorrect. That deterministically skews the tree."
                "Never rebalance even if skewed":
                    a "Incorrect. That gives worst-case linear operations."

        elif current_q == "q13":
            a "When merging two BSTs where all keys in A are less than all keys in B, what is an efficient approach?"
            menu:
                "Insert every node of A into B one by one":
                    a "Incorrect. That's O(|A| log |B|) and may be suboptimal."
                "Convert both to sorted lists and merge, then build balanced BST from merged list":
                    $ chapter_7_score += 1
                    a "Correct! Merging sorted lists then building balanced BST is efficient (linear in total size)."
                "Append B as right subtree of A's root without changes":
                    a "Incorrect. That likely breaks BST invariants and balance."

        elif current_q == "q14":
            a "Which augmented BST supports fast split and join operations by key (useful in rope/string implementations)?"
            menu:
                "Binary heap":
                    a "Incorrect. Heaps don't support ordered split/join by key."
                "Treap (randomized BST) or splay tree":
                    $ chapter_7_score += 1
                    a "Correct! Treaps and splay trees support efficient split/join operations."
                "Simple unbalanced BST":
                    a "Incorrect. Unbalanced BSTs lack guaranteed performance for split/join."

        elif current_q == "q15":
            a "Which serialization strategy preserves both structure and values of a BST unambiguously?"
            menu:
                "Store pre-order traversal only without null markers":
                    a "Incorrect. Pre-order without nulls loses shape information."
                "Store pre-order with explicit null markers for missing children, or store pre-order + in-order":
                    $ chapter_7_score += 1
                    a "Correct! Null markers or a pair of traversals preserve exact structure and values."
                "Store keys in arbitrary order":
                    a "Incorrect. Arbitrary order can't reconstruct the tree."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Your quiz score is: [chapter_7_score]"

    jump chapter_7_performance
init python:
    import random
    chapter_7_hard_question_order = [
        "q1","q2","q3","q4","q5",
        "q6","q7","q8","q9","q10",
        "q11","q12","q13","q14","q15",
        "q16","q17","q18","q19","q20"
    ]
    random.shuffle(chapter_7_hard_question_order)

label chapter_7_quiz_hard:
    $ chapter_7_score = 0
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    show adrian smiling at center
    a "Welcome to the Binary Search Tree challenge. These questions focus on deeper properties, edge cases, and augmented BST techniques."

    while chapter_7_hard_question_order:
        $ current_q = chapter_7_hard_question_order.pop(0)

        if current_q == "q1":
            a "Which pair of traversals uniquely identifies a binary tree (given all node values distinct)?"
            menu:
                "Pre-order and Post-order":
                    a "Incorrect. Pre + Post alone can be ambiguous without extra info."
                "In-order and Pre-order":
                    $ chapter_7_score += 1
                    a "Correct! In-order combined with pre-order (or post-order) uniquely reconstructs the tree."
                "Level-order and any single traversal":
                    a "Incorrect. Level-order plus one traversal may still be ambiguous."

        elif current_q == "q2":
            a "What is an efficient way to check whether a binary tree is a valid BST in O(n) time and O(h) space?"
            menu:
                "Verify for each node that all left descendants are less and all right descendants are greater by scanning subtrees each time":
                    a "Incorrect. That leads to O(n^2) worst-case."
                "Perform in-order traversal and ensure sequence is strictly increasing":
                    $ chapter_7_score += 1
                    a "Correct! In-order of a BST yields sorted order; check monotonicity using O(h) stack space."
                "Compare every pair of nodes":
                    a "Incorrect. Pairwise comparisons are inefficient."

        elif current_q == "q3":
            a "When deleting a node with two children, why might you prefer replacing it with its in-order successor rather than predecessor (or vice versa)?"
            menu:
                "It doesn't matter; both choices produce identical subtree shapes always":
                    a "Incorrect. Choice affects specific shapes and subsequent balancing."
                "Choice can affect subsequent balancing or locality; pick successor or predecessor based on implementation convenience":
                    $ chapter_7_score += 1
                    a "Correct! Either maintains BST invariants; implementation details and balancing heuristics can guide the choice."
                "Using successor is required by BST definition":
                    a "Incorrect. BST definition permits either replacement strategy."

        elif current_q == "q4":
            a "How can you augment a BST to support O(log n) time predecessor and successor queries while keeping standard operations efficient?"
            menu:
                "Store parent pointers and update them during rotations/insert/delete":
                    $ chapter_7_score += 1
                    a "Correct! Parent pointers let you climb to find predecessor/successor quickly; maintain them during updates."
                "Store a global array of successors for all nodes":
                    a "Incorrect. Global arrays are costly to maintain on updates."
                "Nothing; predecessor/successor are always O(1) without augmentation":
                    a "Incorrect. Without augmentation you may need O(h) time."

        elif current_q == "q5":
            a "What invariant must hold when using subtree sizes to implement order-statistic operations (select/rank) in a BST?"
            menu:
                "Subtree size at a node equals 1 plus sizes of left and right children":
                    $ chapter_7_score += 1
                    a "Correct! That recurrence lets you compute ranks/selects by walking the tree."
                "Subtree size equals height of subtree":
                    a "Incorrect. Size counts nodes, height counts levels."
                "Subtree size must be prime":
                    a "Incorrect. That's unrelated."

        elif current_q == "q6":
            a "Which data structure choice gives deterministic O(log n) worst-case guarantees for ordered maps?"
            menu:
                "Plain unbalanced BST with random inserts":
                    a "Incorrect. Random inserts give expected behavior, not deterministic worst-case."
                "Self-balancing BSTs like AVL or Red-Black trees":
                    $ chapter_7_score += 1
                    a "Correct! AVL and RB guarantee O(log n) worst-case."
                "Van Emde Boas tree":
                    a "Incorrect. vEB trees have other constraints and are not a standard BST replacement for arbitrary keys."

        elif current_q == "q7":
            a "What is the standard trick to merge two BSTs A and B where all keys in A are less than all keys in B, producing a balanced BST in O(|A| + |B|)?"
            menu:
                "Insert every key from A into B one-by-one":
                    a "Incorrect. That is O(|A| log |B|) typically."
                "Convert both to sorted lists, merge the lists, then build balanced BST from merged list":
                    $ chapter_7_score += 1
                    a "Correct! Merging sorted lists and building a balanced BST is linear time overall."
                "Attach B as right subtree of A's maximum node without rebalancing":
                    a "Incorrect. That likely breaks balance and may violate performance guarantees."

        elif current_q == "q8":
            a "How do you detect and avoid integer overflow when using subtree sizes or augmented counters in languages with fixed-width integers?"
            menu:
                "Ignore it; overflow cannot happen for practical n":
                    a "Incorrect. Large inputs or adversarial tests can cause overflow."
                "Use a larger integer type, check for overflow on updates, or saturate and detect exceptional cases":
                    $ chapter_7_score += 1
                    a "Correct! Use safe integer types or checks to avoid undefined behavior on overflow."
                "Reset counters randomly when they get large":
                    a "Incorrect. Random resets break correctness."

        elif current_q == "q9":
            a "Which approach gives O(1) amortized time to find next in-order element repeatedly over n elements (i.e., iterate) without parent pointers?"
            menu:
                "Use recursion repeatedly starting from root each time":
                    a "Incorrect. That is costly and not amortized O(1)."
                "Use an explicit stack to perform iterative in-order traversal, pushing left path once and popping as you go":
                    $ chapter_7_score += 1
                    a "Correct! An explicit stack yields amortized O(1) per next over the whole traversal."
                "Use breadth-first traversal":
                    a "Incorrect. BFS doesn't produce in-order sequence."

        elif current_q == "q10":
            a "What is the key idea behind using 'implicit keys' (indices) in a BST to represent sequences (e.g., ropes)?"
            menu:
                "Treat subtree sizes as implicit keys so position-based operations (split/join/select) can be implemented using rank-based navigation":
                    $ chapter_7_score += 1
                    a "Correct! Implicit keys let you operate by index using subtree sizes for navigation."
                "Store each element's global index and update all on each insert":
                    a "Incorrect. Updating all indices is expensive."
                "Use hashing of indices for quick lookup":
                    a "Incorrect. Hashing doesn't preserve order for split/join."

        elif current_q == "q11":
            a "Which randomized BST variant supports efficient split and join by key while keeping expected O(log n) height?"
            menu:
                "Treap (priority BST)":
                    $ chapter_7_score += 1
                    a "Correct! Treaps use random priorities and support split/join efficiently."
                "Binary heap":
                    a "Incorrect. Heaps are not ordered for in-order operations."
                "Naive unbalanced BST":
                    a "Incorrect. Unbalanced BSTs lack guarantees."

        elif current_q == "q12":
            a "Which subtle bug can occur when serializing BSTs by pre-order without null markers and deserializing assuming unique keys?"
            menu:
                "No bug; pre-order always suffices to rebuild the same BST":
                    a "Incorrect. Pre-order without nulls loses structural information for general trees."
                "Different tree shapes can produce the same pre-order sequence unless additional information (like null markers or inorder) is stored":
                    $ chapter_7_score += 1
                    a "Correct! You need null markers or an additional traversal to reconstruct structure uniquely."
                "Pre-order will reverse child order on deserialization":
                    a "Incorrect. That is not the standard failure mode."

        elif current_q == "q13":
            a "How can you implement split(T, key) for a treap quickly?"
            menu:
                "Traverse to find key, then rebuild whole tree from scratch":
                    a "Incorrect. Rebuilding is too costly."
                "Recursively split by comparing key with root and recombine appropriate subtrees, using priorities to maintain heap property":
                    $ chapter_7_score += 1
                    a "Correct! Treap split is recursive and runs in expected O(log n)."
                "Use level-order traversal to partition nodes":
                    a "Incorrect. Level-order doesn't respect BST ordering for split."

        elif current_q == "q14":
            a "Which augmentation lets you answer 'how many keys lie in range [a,b]' in O(log n) time on average in a BST?"
            menu:
                "Maintain subtree sizes and implement rank(x) = count ≤ x; answer is rank(b) − rank(a − 1)":
                    $ chapter_7_score += 1
                    a "Correct! Combining subtree sizes with rank queries yields range counts efficiently."
                "Store cumulative sums across an in-order list only":
                    a "Incorrect. Cumulative sums on a list can help but require rebuilding or extra structure for dynamic updates."
                "Store a global sorted array and binary search it each time":
                    a "Incorrect. Keeping it updated dynamically is costly."

        elif current_q == "q15":
            a "When implementing delete in an augmented BST (stores subtree sizes), what must you remember to update during rotations and removals?"
            menu:
                "Only the sizes of the nodes that are directly removed":
                    a "Incorrect. Rotations change local subtree composition; affected nodes' sizes must be updated."
                "Update subtree sizes for all nodes in entire tree after each operation":
                    a "Incorrect. That's wasteful; updates can be done locally."
                "Update subtree sizes for affected nodes using children's stored sizes during rotations and deletions":
                    $ chapter_7_score += 1
                    a "Correct! Local updates using children's sizes keep augmentation correct."

        elif current_q == "q16":
            a "What is an advantage of splay trees compared to classical balanced BSTs in certain workloads?"
            menu:
                "They provide strict worst-case O(log n) per operation":
                    a "Incorrect. Splay trees give amortized guarantees, not strict worst-case."
                "They adapt to access patterns, offering good amortized bounds and potential locality benefits for nonuniform accesses":
                    $ chapter_7_score += 1
                    a "Correct! Splay trees adapt to sequential/locality patterns with good amortized performance."
                "They never perform rotations":
                    a "Incorrect. Splaying uses rotations extensively."

        elif current_q == "q17":
            a "Which method helps avoid degenerate behavior when inserting adversarial sequences into some BST variants?"
            menu:
                "Use deterministic insertion order exactly as input":
                    a "Incorrect. Deterministic worst-case sequences can degenerate trees."
                "Use randomized priorities (treap) or randomize insertion order to provide expected balance":
                    $ chapter_7_score += 1
                    a "Correct! Randomization thwarts adversarial worst-case sequences in expectation."
                "Use only integer keys":
                    a "Incorrect. Key type doesn't prevent degeneracy."

        elif current_q == "q18":
            a "Which approach yields an in-order traversal without recursion and using O(1) extra space (excluding output), and what caveat does it have?"
            menu:
                "Morris traversal; it modifies tree temporarily by threading and must restore pointers before finishing":
                    $ chapter_7_score += 1
                    a "Correct! Morris traversal uses temporary threads and requires careful restoration to preserve the tree."
                "Simple iterative approach with a global visited flag on nodes":
                    a "Incorrect. Visited flags modify node state and require O(n) extra storage or mutation."
                "Use parent pointers and no stack; no caveats":
                    a "Incorrect. Parent pointers need to be maintained and not always available; also may require careful updates."

        elif current_q == "q19":
            a "Which technique can be used to maintain order-statistics and also support fast split/join operations?"
            menu:
                "Maintain subtree sizes and use a balanced BST variant that supports split/join, e.g., treap or splay with size augmentation":
                    $ chapter_7_score += 1
                    a "Correct! Size augmentation plus a split/join-capable BST yields versatile sequence operations."
                "Use only recursion for each split":
                    a "Incorrect. Naive recursion without split logic is inefficient."
                "Convert tree to array each time you need split/join":
                    a "Incorrect. Conversion costs O(n) each time."

        elif current_q == "q20":
            a "What is a robust testing strategy for validating a complex BST implementation with augmentations and rotations?"
            menu:
                "Manual eyeballing of a few hand-crafted trees":
                    a "Incorrect. Manual tests miss many edge and random cases."
                "Property-based randomized testing: generate random sequences of inserts/deletes/queries, compare against a trusted reference (e.g., sorted array or library map), and assert invariants (BST order, subtree sizes, heights) after each operation":
                    $ chapter_7_score += 1
                    a "Correct! Randomized testing plus invariant checks and reference comparisons is effective for catching subtle bugs."
                "Only run unit tests for trivial cases":
                    a "Incorrect. Trivial cases are insufficient."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Your quiz score is: [chapter_7_score]"
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
    play sound "sfx/success.mp3"
    play music "bgm/city-high-life.mp3" fadein 1.0
    $ persistent.chapter_7 = True
    a "Would You like to test again?"
    menu:
        "Yes":
            jump chapter_7_restart
        "No":
            pass
    show adrian happy
    a "You have finished chapter 7. You can continue to Chapter 8!"
    jump menu
       