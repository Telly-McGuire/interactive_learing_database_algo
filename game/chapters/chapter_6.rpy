
# Chapter 6: AVL TREES
# Properties of AVL Trees
# operations on AVL Trees
# Balanced Trees
# Rotation I, II, III, IV
# Operations
# Application


default chapter_6_progress = 0

default chapter_6_AVL_Properties_quiz = 0
default chapter_6_AVL_Operations_quiz = 0
default chapter_6_Balanced_Trees_quiz = 0
default chapter_6_Rotations_quiz = 0
screen chapter_6_AVLIntro:
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 200
        ypadding 60
        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5
            text "AVL Trees" size 60 color "#FFFFFF" outlines [(5, "#000000", 0, 0)]
label chapter_6_intro:
    call hideall from _call_hideall_7 #This is a stupid fix but it works I think
    play audio ("sfx/start.mp3")
    play music "bgm/city-high-life.mp3" fadein 1.0

    scene black
    pause 1.0
    show screen chapter_6_AVLIntro
    pause 2.0
    scene room with dissolve
    pause 1.0
    hide screen chapter_6_AVLIntro

    with dissolve
        
    show screen menu_btn

    show adrian normal at center:
        smaller
    
    if persistent.chapter_6 == False:
        a "Hi welcome back to chapter 6!"
        a "are you sure you want to go through this chapter again?"
        menu:
            "Yes":
                a "Pick a topic"
                menu:
                    "AVL Tree Properties":
                        jump chapter_6_AVL_Properties
                    "AVL Tree Operations":
                        jump chapter_6_AVL_Operations
                    "Balanced Trees":
                        jump chapter_6_Balanced_Trees
                    "Rotations":
                        jump chapter_6_Rotations 

            "No":
                jump menu
    else:
        pass

    a "Aight no more monke business"
    a "Welcome back to my room"
    a "Welcome to Chapter 6: AVL Trees."
    show adrian nocomment
    a "..."
    a "What you expected an aligator to pop out or something?"
    a "Nah"


    jump chapter_6_AVL_Properties
label chapter_6_AVL_Properties:
    
    
    a "Let’s talk about AVL Trees."

    show adrian explaining:
        smaller
    a "AVL Trees are a type of self-balancing Binary Search Tree."
    a "They have to be Balanced to be called AVL Trees."

    screen ch6_AVL_Info:
        frame:
            xalign 0.95
            yalign 0.3
            xpadding 70
            ypadding 100

            vbox:
                spacing 25
                xalign 0.5
                yalign 0.5

                text "AVL TREE PROPERTIES" size 60 color "#00ccff" outlines [(5, "#000000", 0, 0)]

                text "1. Height-balanced BST" size 40 color "#FFFFFF" outlines [(3, "#000000", 0, 0)]
                text "2. Balance factor ∈ -1, 0, +1" size 40 color "#FFFFFF" outlines [(3, "#000000", 0, 0)]
                text "3. Rotations restore balance after insert/delete" size 40 color "#FFFFFF" outlines [(3, "#000000", 0, 0)]
                text "4. Guarantees O(log n) search, insert, delete" size 40 color "#FFFFFF" outlines [(3, "#000000", 0, 0)]
                

    show adrian explaining at left
    with move
    show screen ch6_AVL_Info
    a "{size=+10}{b}Okay, so AVL Trees are a computer science concept.{/b}{/size}"
    a "{i}That means they’re not real trees—they live in your computer’s brain!{/i}"

    a "{color=#4682B4}They’re part of something called data structures,{/color} which are like invisible ways to organize stuff so computers can work faster."

    show adrian explaining
    a "{b}AVL Trees are special because they stay balanced.{/b}"
    a "That means they don’t let one side get too tall or too short."

    a "They check the height difference—called the {color=#DAA520}balance factor{/color}—and if it’s off, they do a little twist to fix it."

    a "{i}These twists are called rotations.{/i} There are four kinds: {b}Left, Right, Left-Right, and Right-Left.{/b}"

    show adrian normal
    a "{color=#2E8B57}It’s all pretend,{/color} but it helps computers keep things neat so they can {b}find, add, or remove stuff quickly.{/b}"

    show adrian smiling
    a "Think of it like {i}sorting your toy box{/i}. You don’t see the sorting rules, but they help you find your favorite toy fast."

    a "{size=+8}{color=#6A5ACD}AVL Trees do that for computers. It’s all in their imagination—but it works!{/color}{/size}"

    show adrian smiling at center
    with move
    hide screen ch6_AVL_Info
    with dissolve
    $ chapter_6_progress =+ 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Alright, let’s see what you’ve learned. Time for a quick quiz!"
    jump chapter_6_AVL_Properties_Quiz
init python:
    import random
    chapter_6_AVL_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_6_AVL_order)

label chapter_6_AVL_Properties_Quiz:
    $ chapter_6_AVL_Properties_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_6_AVL_order:
        $ current_q = chapter_6_AVL_order.pop(0)

        if current_q == "q1":
            a "What does AVL stand for in AVL Tree?"
            menu:
                "Adelson-Velsky and Landis":
                    $ chapter_6_AVL_Properties_quiz += 1
                    a "Correct! AVL trees are named after their inventors."
                "Automatic Variable Lookup":
                    a "Incorrect! That’s not related to tree structures."
                "Advanced Vector Logic":
                    a "Incorrect! That’s a different computing concept."

        elif current_q == "q2":
            show adrian doubt
            a "What is the balance factor of a node in an AVL tree?"
            menu:
                "Height difference between left and right subtrees":
                    $ chapter_6_AVL_Properties_quiz += 1
                    a "Correct! Balance factor is left height minus right height."
                "Number of children nodes":
                    a "Incorrect! That’s not how balance is measured."
                "Depth of the deepest leaf":
                    a "Incorrect! That’s more related to tree height."

        elif current_q == "q3":
            a "Which operation may be required to maintain AVL balance after insertion?"
            menu:
                "Rotation":
                    $ chapter_6_AVL_Properties_quiz += 1
                    a "Correct! Rotations help restore balance."
                "Traversal":
                    a "Incorrect! Traversal doesn’t affect balance."
                "Deletion":
                    a "Incorrect! Deletion may trigger rebalancing, but isn’t the operation itself."

        elif current_q == "q4":
            a "What is the maximum allowed balance factor in an AVL tree?"
            menu:
                "1":
                    $ chapter_6_AVL_Properties_quiz += 1
                    a "Correct! Balance factors must be -1, 0, or 1."
                "2":
                    a "Incorrect! A balance factor of 2 means rebalancing is needed."
                "0":
                    a "Incorrect! 0 is balanced, but not the maximum allowed."

        elif current_q == "q5":
            show adrian happy
            a "Which of these is a valid AVL tree property?"
            menu:
                "Self-balancing after insertions and deletions":
                    $ chapter_6_AVL_Properties_quiz += 1
                    a "Correct! AVL trees maintain balance automatically."
                "Always perfectly balanced":
                    a "Incorrect! AVL trees allow slight imbalance."
                "Only allows sorted data":
                    a "Incorrect! Sorting is a result of traversal, not a restriction."

    
    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_6_AVL_Properties_quiz] out of 5."
    jump chapter_6_AVL_Operations



label chapter_6_AVL_Operations:


    show adrian 
    a "Alright, now that we know what AVL Trees are, let’s dive into how they operate."

    show adrian explaining
    a "AVL Trees adjust themselves after insertions and deletions to stay balanced."

    show screen ch6_AVLOps_Menu

    screen ch6_AVLOps_Menu():
        frame:
            xalign 0.8
            yalign 0.3
            xpadding 80
            ypadding 80

            vbox:
                spacing 30
                xalign 0.5
                yalign 0.5

                text "AVL OPERATIONS" size 60 color "#00ccff" outlines [(5, "#000000", 0, 0)]

                textbutton "Insert" action Show("ch6_AVLOps_Insert") text_size 40
                textbutton "Delete" action Show("ch6_AVLOps_Delete") text_size 40
                textbutton "Rotations" action Show("ch6_AVLOps_Rotations") text_size 40
                textbutton "Search" action Show("ch6_AVLOps_Search") text_size 40
            
    screen ch6_AVLOps_Insert():
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 60
            ypadding 60

            vbox:
                spacing 20
                text "INSERT OPERATION" size 50 color "#00ccff"
                text "• Add node like in BST" size 40
                text "• Check balance factor after insert" size 40
                text "• Perform rotation if needed" size 40
                textbutton "Back" action Hide("ch6_AVLOps_Insert") text_size 30

    screen ch6_AVLOps_Delete():
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 60
            ypadding 60

            vbox:
                spacing 20
                text "DELETE OPERATION" size 50 color "#00ccff"
                text "• Remove node like in BST" size 40
                text "• Recalculate balance factor" size 40
                text "• Apply rotation if imbalance occurs" size 40
                textbutton "Back" action Hide("ch6_AVLOps_Delete") text_size 30

    screen ch6_AVLOps_Rotations():
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 60
            ypadding 60

            vbox:
                spacing 20
                text "ROTATIONS" size 50 color "#00ccff"
                text "• LL: Right rotation" size 40
                text "• RR: Left rotation" size 40
                text "• LR: Left then right" size 40
                text "• RL: Right then left" size 40
                textbutton "Back" action Hide("ch6_AVLOps_Rotations") text_size 30

    screen ch6_AVLOps_Search():
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 60
            ypadding 60

            vbox:
                spacing 20
                text "SEARCH OPERATION" size 50 color "#00ccff"
                text "• Same as BST search" size 40
                text "• Balanced height ensures fast lookup" size 40
                textbutton "Back" action Hide("ch6_AVLOps_Search") text_size 30

    show adrian normal at left
    with move
    a "These rotations are lightweight and localized—they don’t rebuild the whole tree, just tweak the structure where needed."

    show adrian smiling
    a "Thanks to these operations, AVL Trees keep their height logarithmic, which means fast search, insert, and delete."

    hide screen ch6_AVLOps_Menu
   
    show adrian smiling at center
    with move

    $ chapter_6_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "You hear that? Its time for some questions. Buckle Up Buckeroo"
    jump chapter_6_AVL_Operations_Quiz
init python:
    import random
    chapter_6_AVL_operations_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_6_AVL_operations_order)

label chapter_6_AVL_Operations_Quiz:
    #5POINTS
    $ chapter_6_AVL_Operations_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_6_AVL_operations_order:
        $ current_q = chapter_6_AVL_operations_order.pop(0)

        if current_q == "q1":
            a "Which rotation is used when a node is inserted into the left subtree of the left child?"
            menu:
                "Right Rotation":
                    $ chapter_6_AVL_Operations_quiz += 1
                    a "Correct! That's a Left-Left case, resolved with a right rotation."
                "Left Rotation":
                    a "Incorrect! Left rotation is used for Right-Right cases."
                "Left-Right Rotation":
                    a "Incorrect! That's used for Left-Right imbalance."

        elif current_q == "q2":
            show adrian doubt
            a "What triggers a double rotation in an AVL tree?"
            menu:
                "Insertion into the inner subtree of a child":
                    $ chapter_6_AVL_Operations_quiz += 1
                    a "Correct! Double rotations fix Left-Right or Right-Left imbalances."
                "Insertion into the outer subtree of a child":
                    a "Incorrect! That only needs a single rotation."
                "Any insertion":
                    a "Incorrect! Not all insertions require rebalancing."

        elif current_q == "q3":
            a "Which of these is a valid AVL rebalancing operation?"
            menu:
                "Left-Right Rotation":
                    $ chapter_6_AVL_Operations_quiz += 1
                    a "Correct! It's a combination of left then right rotation."
                "Top-Down Rotation":
                    a "Incorrect! That’s not a standard AVL operation."
                "Root Swap":
                    a "Incorrect! AVL trees don’t swap roots arbitrarily."

        elif current_q == "q4":
            a "What happens after deleting a node in an AVL tree?"
            menu:
                "Tree may need rebalancing":
                    $ chapter_6_AVL_Operations_quiz += 1
                    a "Correct! Deletion can cause imbalance that must be fixed."
                "Tree becomes a binary search tree":
                    a "Incorrect! AVL trees are already BSTs with balance."
                "Tree height always increases":
                    a "Incorrect! Deletion usually reduces height."

        elif current_q == "q5":
            show adrian happy
            a "Which case requires a Left-Right rotation?"
            menu:
                "Insertion into left subtree of right child":
                    a "Incorrect! That’s a Right-Left case."
                "Insertion into right subtree of left child":
                    $ chapter_6_AVL_Operations_quiz += 1
                    a "Correct! That’s a Left-Right imbalance."
                "Insertion into left subtree of left child":
                    a "Incorrect! That’s a Left-Left case."


    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_6_AVL_Operations_quiz] out of 5."
    jump chapter_6_Balanced_Trees



label chapter_6_Balanced_Trees:
 
    show adrian 
    a "Let’s zoom out for a moment. Not all trees are created equal."

    show adrian explaining
    a "Balanced trees are the backbone of efficient data structures. They keep operations fast even if as data {b}grows."

    show adrian happy at right
    with move
    a "Tap on a concept to explore how balance is maintained."

    show screen ch6_BalancedTree_Menu
    screen ch6_BalancedTree_Menu():
        frame:
            xalign 0.1
            yalign 0.3
            xpadding 40
            ypadding 150

            vbox:
                spacing 30
                xalign 0.5
                yalign 0.5

                text "BALANCED TREE CONCEPTS" size 60 color "#00ccff" outlines [(5, "#000000", 0, 0)]

                textbutton "Why Balance Matters" action Show("ch6_BalancedTree_Why") text_size 40
                textbutton "Types of Balanced Trees" action Show("ch6_BalancedTree_Types") text_size 40
                textbutton "Balance Factor & Height" action Show("ch6_BalancedTree_Factor") text_size 40
                
    screen ch6_BalancedTree_Why():
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 60
            ypadding 60

            vbox:
                spacing 20
                text "WHY BALANCE MATTERS" size 50 color "#00ccff"
                text "• Balanced trees keep operations O(log n)" size 40
                text "• Unbalanced trees can degrade to O(n)" size 40
                text "• Balance ensures predictable performance" size 40
                textbutton "Back" action Hide("ch6_BalancedTree_Why") text_size 30

    screen ch6_BalancedTree_Types():
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 60
            ypadding 60

            vbox:
                spacing 20
                text "TYPES OF BALANCED TREES" size 50 color "#00ccff"
                text "• AVL Trees: strict balance via rotations" size 40
                text "• Red-Black Trees: looser balance, faster inserts" size 40
                text "• B-Trees: used in databases and file systems" size 40
                textbutton "Back" action Hide("ch6_BalancedTree_Types") text_size 30

    screen ch6_BalancedTree_Factor():
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 60
            ypadding 60

            vbox:
                spacing 20
                text "BALANCE FACTOR & HEIGHT" size 50 color "#00ccff"
                text "• Balance Factor = Left Height - Right Height" size 40
                text "• Acceptable range: -1 to +1 (AVL)" size 40
                text "• Height affects traversal and efficiency" size 40
                textbutton "Back" action Hide("ch6_BalancedTree_Factor") text_size 30
    image shocker = "assets/shocker.png"

    show adrian normal
    a "Balanced trees are essential for maintaining performance as data scales."
    a "Oooh scaling, scaling what? Yo mom?"
    hide screen ch6_BalancedTree_Menu
    a "yo mama joke in this century, shocker"

    show shocker at right
    with moveinright
    show adrian at left 
    with move

    a "Who are you?"
    "Shocker, you called me"
    show adrian nocomment
    a "..."
    a "no"
    a "get out of here"
    "waste of my time" 

    show shocker at right
    with moveoutright
    hide shocker
    show adrian at center
    with move
    a "{cps=20}I...I dont know what that was"
    
    $ chapter_6_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "You hear that? Its time for some questions. Buckle Up Buckeroo"
    jump chapter_6_Balanced_Trees_Quiz
init python:
    import random
    chapter_6_balanced_trees_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_6_balanced_trees_order)

label chapter_6_Balanced_Trees_Quiz:
    #5POINTS
    $ chapter_6_Balanced_Trees_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_6_balanced_trees_order:
        $ current_q = chapter_6_balanced_trees_order.pop(0)

        if current_q == "q1":
            a "What defines a balanced binary tree?"
            menu:
                "The height difference between left and right subtrees is at most one":
                    $ chapter_6_Balanced_Trees_quiz += 1
                    a "Correct! That’s the standard definition of balance."
                "Each node has exactly two children":
                    a "Incorrect! That’s a full binary tree, not necessarily balanced."
                "All leaves are at the same depth":
                    a "Incorrect! That describes a perfect binary tree."

        elif current_q == "q2":
            show adrian doubt
            a "Which of these is a type of balanced tree?"
            menu:
                "AVL Tree":
                    $ chapter_6_Balanced_Trees_quiz += 1
                    a "Correct! AVL trees maintain balance through rotations."
                "Linked List":
                    a "Incorrect! Linked lists aren’t trees and aren’t balanced."
                "Heap":
                    a "Incorrect! Heaps have a different structure and balance criteria."

        elif current_q == "q3":
            a "Why are balanced trees important in data structures?"
            menu:
                "They ensure efficient search, insert, and delete operations":
                    $ chapter_6_Balanced_Trees_quiz += 1
                    a "Correct! Balanced trees keep operations close to O(log n)."
                "They store more data than unbalanced trees":
                    a "Incorrect! Capacity isn’t the key benefit."
                "They are easier to draw":
                    a "Incorrect! Visual simplicity isn’t a technical advantage."

        elif current_q == "q4":
            a "Which tree is always balanced by design?"
            menu:
                "Red-Black Tree":
                    $ chapter_6_Balanced_Trees_quiz += 1
                    a "Correct! Red-Black trees enforce balance through color rules."
                "Binary Search Tree":
                    a "Incorrect! BSTs can become unbalanced without rotations."
                "Trie":
                    a "Incorrect! Tries are prefix trees, not necessarily balanced."

        elif current_q == "q5":
            show adrian happy
            a "What happens if a binary tree becomes unbalanced?"
            menu:
                "Search operations may become inefficient":
                    $ chapter_6_Balanced_Trees_quiz += 1
                    a "Correct! Unbalanced trees can degrade to linear time."
                "It automatically converts to a balanced tree":
                    a "Incorrect! Rebalancing must be implemented."
                "It loses all its nodes":
                    a "Incorrect! Imbalance doesn’t erase data."
    

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_6_Balanced_Trees_quiz] out of 5."
    jump chapter_6_Rotations


label chapter_6_Rotations:
    # Rotation I, II, III, IV
                                # VISUALS NEEDED
    show adrian
    a "Now, let’s get into the nitty-gritty of rotations in AVL Trees."

    show adrian explaining
    a "Rotations are the key operations that restore balance in AVL Trees after insertions or deletions."

    #add visuals for each rotation type
        
    $ chapter_6_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "You hear that? Its time for some questions. Buckle Up Buckeroo"
    jump chapter_6_Rotations_Quiz
    
init python:
    import random
    chapter_6_rotations_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_6_rotations_order)

label chapter_6_Rotations_Quiz:

    #5POINTS
    $ chapter_6_Rotations_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_6_rotations_order:
        $ current_q = chapter_6_rotations_order.pop(0)

        if current_q == "q1":
            a "Which rotation fixes a Left-Left imbalance in an AVL tree?"
            menu:
                "Right Rotation":
                    $ chapter_6_Rotations_quiz += 1
                    a "Correct! A Left-Left case is resolved with a right rotation."
                "Left Rotation":
                    a "Incorrect! That’s used for Right-Right cases."
                "Left-Right Rotation":
                    a "Incorrect! That’s for Left-Right imbalances."

        elif current_q == "q2":
            show adrian doubt
            a "What is the sequence of operations in a Left-Right rotation?"
            menu:
                "Left rotation on left child, then right rotation on root":
                    $ chapter_6_Rotations_quiz += 1
                    a "Correct! That’s the proper sequence for Left-Right cases."
                "Right rotation on left child, then left rotation on root":
                    a "Incorrect! That’s the Right-Left rotation sequence."
                "Single right rotation on root":
                    a "Incorrect! Left-Right requires a double rotation."

        elif current_q == "q3":
            a "Which rotation is used for a Right-Left imbalance?"
            menu:
                "Right-Left Rotation":
                    $ chapter_6_Rotations_quiz += 1
                    a "Correct! It’s a combination of right then left rotation."
                "Left Rotation":
                    a "Incorrect! That’s for Right-Right cases."
                "Left-Right Rotation":
                    a "Incorrect! That’s for Left-Right cases."

        elif current_q == "q4":
            a "When is a single rotation sufficient to restore AVL balance?"
            menu:
                "When imbalance is in the outer subtree":
                    $ chapter_6_Rotations_quiz += 1
                    a "Correct! Outer subtree insertions need only one rotation."
                "When imbalance is in the inner subtree":
                    a "Incorrect! Inner subtree cases require double rotation."
                "Always":
                    a "Incorrect! Some cases need double rotations."

        elif current_q == "q5":
            show adrian happy
            a "Which of the following is true about AVL rotations?"
            menu:
                "They preserve the binary search tree property":
                    $ chapter_6_Rotations_quiz += 1
                    a "Correct! Rotations maintain BST order while restoring balance."
                "They randomly rearrange nodes":
                    a "Incorrect! Rotations are structured and purposeful."
                "They only occur during deletions":
                    a "Incorrect! Rotations can occur after insertions too."

    
    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_6_Balanced_Trees_quiz] out of 5."
    jump chapter_6_restart




label chapter_6_restart:
    $ chapter_6_test = (
        chapter_6_AVL_Properties_quiz +
        chapter_6_AVL_Operations_quiz +
        chapter_6_Balanced_Trees_quiz +
        chapter_6_Rotations_quiz)

    a "Your score is [chapter_6_test]"
    a "Let's see how well you do in the {size=+20}CHAPTER QUIZ"

    if chapter_5_test <= 8:
        show adrian concerned
        jump chapter_6_quiz_easy
    elif chapter_5_test <= 14:
        show adrian smiling
        jump chapter_6_quiz_medium
    else:
        show adrian confident
        jump chapter_6_quiz_hard


init python:
    import random
    chapter_6_easy_question_order = [
        "q1","q2","q3","q4","q5",
        "q6","q7","q8","q9","q10"
    ]
    random.shuffle(chapter_6_easy_question_order)

label chapter_6_quiz_easy:
    $ chapter_6_score = 0
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    show adrian smiling at center
    a "Welcome to the {b}AVL Trees Quiz{/b}! Let's test your basic understanding."

    while chapter_6_easy_question_order:
        $ current_q = chapter_6_easy_question_order.pop(0)

        if current_q == "q1":
            a "What property defines an AVL tree?"
            menu:
                "Every node's left and right subtree heights differ by at most 1":
                    $ chapter_6_score += 1
                    a "Correct! AVL trees maintain balance by keeping height differences ≤ 1."
                "Every node has at most two children":
                    a "Incorrect. That's true for all binary trees, not specific to AVL."
                "All leaves are at the same depth":
                    a "Incorrect. That's a perfect tree, stricter than AVL."

        elif current_q == "q2":
            a "What is the balance factor of a node in an AVL tree?"
            menu:
                "Height(left subtree) − Height(right subtree)":
                    $ chapter_6_score += 1
                    a "Correct! Balance factor is typically left height minus right height."
                "Number of nodes in left subtree":
                    a "Incorrect. That's subtree size, not balance factor."
                "Depth of the node from the root":
                    a "Incorrect. Depth is different from balance factor."

        elif current_q == "q3":
            a "Which rotation fixes a Right-Right (RR) imbalance after insertion?"
            menu:
                "Left rotation at the unbalanced node":
                    $ chapter_6_score += 1
                    a "Correct! An RR case is fixed with a single left rotation."
                "Right rotation at the unbalanced node":
                    a "Incorrect. Right rotation fixes a Left-Left case."
                "Double rotation (left then right)":
                    a "Incorrect. Double rotation is for LR or RL cases."

        elif current_q == "q4":
            a "Which sequence of rotations fixes a Left-Right (LR) imbalance?"
            menu:
                "Right rotation on left child, then left rotation on node":
                    $ chapter_6_score += 1
                    a "Correct! LR is fixed by right-then-left (double) rotation."
                "Single left rotation on node":
                    a "Incorrect. Single rotation doesn't resolve LR correctly."
                "Right rotation on node only":
                    a "Incorrect. That handles LL, not LR."

        elif current_q == "q5":
            a "What is the worst-case time complexity for search, insert, or delete in an AVL tree with n nodes?"
            menu:
                "O(n)":
                    a "Incorrect. AVL guarantees logarithmic height, not linear."
                "O(log n)":
                    $ chapter_6_score += 1
                    a "Correct! AVL trees guarantee O(log n) operations."
                "O(1)":
                    a "Incorrect. Tree operations are not constant time."

        elif current_q == "q6":
            a "When inserting into an AVL tree, when do you need to perform rotations?"
            menu:
                "Only when a node's balance factor becomes +2 or −2 after insertion":
                    $ chapter_6_score += 1
                    a "Correct! Rotations restore balance when factor magnitude reaches 2."
                "When the tree becomes empty":
                    a "Incorrect. Empty tree doesn't require rotation."
                "Always after every insertion":
                    a "Incorrect. Rotations are only sometimes necessary."

        elif current_q == "q7":
            a "How does AVL compare to a Red-Black tree in terms of height guarantees?"
            menu:
                "AVL has stronger (tighter) balance, so typically smaller height than RB for same n":
                    $ chapter_6_score += 1
                    a "Correct! AVL is more strictly balanced, often shorter than RB trees."
                "Red-Black trees are always shorter than AVL trees":
                    a "Incorrect. RB trees have weaker balance guarantees, so often taller."
                "They have identical height bounds":
                    a "Incorrect. Their worst-case height constants differ."

        elif current_q == "q8":
            a "Which scenario makes AVL trees a particularly good choice?"
            menu:
                "Workloads with many more searches than insertions/deletions":
                    $ chapter_6_score += 1
                    a "Correct! AVL's stricter balance favors faster searches when updates are fewer."
                "Workloads that require minimal memory overhead only":
                    a "Incorrect. AVL stores heights or balance factors, a small overhead."
                "When every operation must be amortized O(1)":
                    a "Incorrect. AVL operations are O(log n), not O(1)."

        elif current_q == "q9":
            a "What must be updated when you perform a rotation in an AVL tree?"
            menu:
                "Only child pointers; heights/balance factors are unchanged":
                    a "Incorrect. Heights/balance factors usually change and must be updated."
                "Child pointers and the heights or balance factors of affected nodes":
                    $ chapter_6_score += 1
                    a "Correct! Rotations change pointers and affected nodes' heights/factors."
                "Only the root pointer of the entire tree":
                    a "Incorrect. Rotations are local and may not involve the root."

        elif current_q == "q10":
            a "Which of these is a correct statement about AVL deletions?"
            menu:
                "Deleting a node never requires rebalancing":
                    a "Incorrect. Deletions can unbalance ancestors and require rotations."
                "Deletion can trigger rotations up the path to the root until balance restored":
                    $ chapter_6_score += 1
                    a "Correct! After delete, you may need to rebalance upward along ancestors."
                "Deleting always increases tree height":
                    a "Incorrect. Deletion typically reduces or keeps height, not increases."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Your quiz score is: [chapter_6_score]"
    jump chapter_6_performance
init python:
    import random
    chapter_6_medium_question_order = [
        "q1","q2","q3","q4","q5",
        "q6","q7","q8","q9","q10",
        "q11","q12","q13","q14","q15"
    ]
    random.shuffle(chapter_6_medium_question_order)

label chapter_6_quiz_medium:
    $ chapter_6_score = 0
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    show adrian smiling at center
    a "Welcome to the {b}AVL Trees Quiz{/b}! Let's tackle some interesting AVL topics."

    while chapter_6_medium_question_order:
        $ current_q = chapter_6_medium_question_order.pop(0)

        if current_q == "q1":
            a "What is the allowed range of a node's balance factor in a valid AVL tree?"
            menu:
                "-1..+1":
                    $ chapter_6_score += 1
                    a "Correct! AVL balance factors are -1, 0, or +1."
                "-2..+2":
                    a "Incorrect. That's too permissive for AVL."
                "-3..+3":
                    a "Incorrect. That's not the AVL constraint."

        elif current_q == "q2":
            a "Which rotation sequence fixes a Right-Left (RL) imbalance?"
            menu:
                "Left rotation on right child, then right rotation on node":
                    a "Incorrect. That describes LR; check the child/parent sides carefully."
                "Left rotation on right child, then right rotation on node":
                    $ chapter_6_score += 1
                    a "Correct! RL is fixed by left-then-right (double) rotation."
                "Single left rotation on node":
                    a "Incorrect. Single rotations don't resolve RL correctly."

        elif current_q == "q3":
            a "When inserting keys in increasing order into an empty AVL tree, what behavior keeps the tree balanced compared to an ordinary BST?"
            menu:
                "AVL will perform rotations during insertion to avoid becoming a chain":
                    a "Incorrect. (Positioned for alternation)"
                "AVL will perform rotations during insertion to avoid becoming a chain":
                    a "Incorrect. (Positioned for alternation)"
                "AVL will perform rotations during insertion to avoid becoming a chain":
                    $ chapter_6_score += 1
                    a "Correct! AVL rotations prevent the skewed chain that a plain BST would get."

        elif current_q == "q4":
            a "Which piece of information is typically stored per node to maintain AVL balance efficiently?"
            menu:
                "Height or balance factor (height difference)":
                    $ chapter_6_score += 1
                    a "Correct! Nodes store height or balance factor to decide rotations."
                "Subtree sum of values":
                    a "Incorrect. That's for augmented sums, not balance."
                "In-order index only":
                    a "Incorrect. In-order index doesn't help balancing."

        elif current_q == "q5":
            a "After performing a single rotation, which nodes' heights must you update?"
            menu:
                "In-order index only":
                    a "Incorrect. (Positioned for alternation)"
                "The two nodes involved in the rotation (the pivot and its child)":
                    $ chapter_6_score += 1
                    a "Correct! Update heights for the rotated node and its child (and possibly parent references)."
                "Only the rotated child subtree's leaves":
                    a "Incorrect. Leaves alone are not sufficient to update."

        elif current_q == "q6":
            a "Which insertion pattern causes a Left-Left (LL) imbalance at node X?"
            menu:
                "Insertion into right subtree of right child":
                    a "Incorrect. That creates RR."
                "Insertion into left subtree of left child":
                    a "Incorrect. (Positioned for alternation)"
                "Insertion into left subtree of left child":
                    $ chapter_6_score += 1
                    a "Correct! Left insertion on left child causes LL at X."

        elif current_q == "q7":
            a "Which statement about AVL deletions is true?"
            menu:
                "Deletion may require rebalancing at multiple ancestors up to the root":
                    $ chapter_6_score += 1
                    a "Correct! Deleting can cascade rebalances upward."
                "A single rotation always fixes any imbalance after deletion":
                    a "Incorrect. Multiple rotations up the tree may be needed."
                "Deletion never changes node heights":
                    a "Incorrect. Deletion can decrease heights and change balance factors."

        elif current_q == "q8":
            a "What is the amortized cost difference between AVL and Red-Black trees for insert/delete in practice?"
            menu:
                "AVL may have slightly higher update cost but typically faster searches due to smaller heights":
                    $ chapter_6_score += 1
                    a "Correct! AVL often yields faster searches but can cost more during updates."
                "AVL always much faster for updates due to stricter balance":
                    a "Incorrect. AVL has more rotations on updates; it's not always faster."
                "Red-Black trees use O(n) updates while AVL uses O(log n)":
                    a "Incorrect. Both use O(log n) updates."

        elif current_q == "q9":
            a "Which test can detect whether a tree is AVL balanced in one traversal?"
            menu:
                "Post-order traversal that returns height and a boolean balanced flag for each node":
                    a "Incorrect. (Positioned for alternation)"
                "Level-order traversal counting nodes per level only":
                    a "Incorrect. Level counts don't verify local balance factors."
                "Post-order traversal that returns height and a boolean balanced flag for each node":
                    $ chapter_6_score += 1
                    a "Correct! Post-order can check balance and compute heights in O(n)."

        elif current_q == "q10":
            a "When implementing AVL rotations, which pointer adjustments are essential besides child links?"
            menu:
                "Child pointers and parent pointers (if present), plus updating node heights":
                    $ chapter_6_score += 1
                    a "Correct! Parent links and heights must be updated too when used."
                "Only left/right child pointers; parent pointers must not be updated":
                    a "Incorrect. Parent pointers (if stored) must also be updated correctly."
                "No pointer changes are necessary; only height values swap":
                    a "Incorrect. Rotations change structure, not just heights."

        elif current_q == "q11":
            a "Which condition distinguishes between doing a single rotation versus a double rotation to fix imbalance after insertion?"
            menu:
                "Always prefer single rotations; double rotations are optional":
                    a "Incorrect. Single rotation won't fix LR/RL properly."
                "Choose double rotation if the child subtree's heavy side is opposite to the parent's imbalance direction":
                    $ chapter_6_score += 1
                    a "Correct! If child is heavy opposite to parent (LR or RL), perform double rotation."
                "Use double rotation only when tree height is even":
                    a "Incorrect. Height parity is irrelevant."

        elif current_q == "q12":
            a "Which augmented value can be maintained in AVL nodes cheaply and still be updated during rotations?"
            menu:
                "Full sorted list of subtree elements":
                    a "Incorrect. That would be expensive to maintain."
                "Subtree minimum and maximum values":
                    a "Incorrect. (Positioned for alternation)"
                "Subtree minimum and maximum values":
                    $ chapter_6_score += 1
                    a "Correct! Min/max or subtree sizes can be maintained and updated with local info during rotations."

        elif current_q == "q13":
            a "Why might one choose AVL over a Treap for deterministic worst-case guarantees?"
            menu:
                "AVL provides strict worst-case height bounds deterministically, while Treap gives expected bounds using randomness":
                    $ chapter_6_score += 1
                    a "Correct! AVL yields deterministic worst-case guarantees; treaps are randomized with expected bounds."
                "Treaps never require rotations":
                    a "Incorrect. Treaps also use rotations to maintain heap property."
                "AVL uses randomness to balance":
                    a "Incorrect. AVL is deterministic."

        elif current_q == "q14":
            a "Which optimization reduces rotations when inserting many keys but still keeps a balanced tree?"
            menu:
                "Insert and immediately delete each key":
                    a "Incorrect. That simply wastes operations."
                "Batch insert keys then rebuild tree from sorted array":
                    $ chapter_6_score += 1
                    a "Correct! Bulk-building from sorted data (or balanced build) can avoid repeated rotations and yield a balanced tree."
                "Always rotate at root after each insertion":
                    a "Incorrect. Arbitrary rotations at root don't guarantee correctness."

        elif current_q == "q15":
            a "If you maintain heights at each node, what is the cost to update heights up the insertion path before checking balance?"
            menu:
                "O(n) where n is total nodes":
                    a "Incorrect. Only nodes on the insertion path are updated."
                "O(1) constant time":
                    a "Incorrect. Multiple ancestor nodes may need height updates."
                "O(h) where h is the height of the tree":
                    $ chapter_6_score += 1
                    a "Correct! You update heights along the path from inserted node up to root, costing O(h) = O(log n)."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Your quiz score is: [chapter_6_score]"
    jump chapter_6_performance
init python:
    import random
    chapter_6_hard_question_order = [
        "q1","q2","q3","q4","q5",
        "q6","q7","q8","q9","q10",
        "q11","q12","q13","q14","q15",
        "q16","q17","q18","q19","q20"
    ]
    random.shuffle(chapter_6_hard_question_order)

label chapter_6_quiz_hard:
    $ chapter_6_score = 0
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    show adrian smiling at center
    a "Welcome to the {b}AVL Trees Quiz{/b}! These are challenging — think through rotations, invariants, and edge cases."

    while chapter_6_hard_question_order:
        $ current_q = chapter_6_hard_question_order.pop(0)

        if current_q == "q1":
            a "What is the maximum possible imbalance (difference in heights) between left and right subtrees for any node in a valid AVL tree?"
            menu:
                "-2":
                    a "Incorrect. That's beyond AVL's allowed range."
                "-1..+1":
                    $ chapter_6_score += 1
                    a "Correct! AVL requires balance factor ∈ {-1,0,1}."
                "-3..+3":
                    a "Incorrect. That's not allowed for AVL."

        elif current_q == "q2":
            a "During insertion, you encounter an LR imbalance at node X. Which rotation sequence fixes it?"
            menu:
                "Left rotation at X, then right rotation at X":
                    a "Incorrect. That sequence is for other patterns."
                "Right rotation on left child, then left rotation on X":
                    a "Incorrect. That's RL pattern; check sides."
                "Left rotation on left child, then right rotation on X":
                    $ chapter_6_score += 1
                    a "Correct! LR is fixed by left-then-right on the left subtree then X."

        elif current_q == "q3":
            a "When an AVL deletion reduces the height of a subtree, how far can rebalancing propagate?"
            menu:
                "It never propagates past the parent":
                    a "Incorrect. It can propagate further."
                "It can propagate all the way up to the root":
                    $ chapter_6_score += 1
                    a "Correct! Deletion may trigger rotations up the path to the root until balance restored."
                "It only affects the deleted node":
                    a "Incorrect. Ancestors can become unbalanced."

        elif current_q == "q4":
            a "Which invariant must hold for heights when performing a single rotation (e.g., left rotation at node A)?"
            menu:
                "Only child pointers change; heights remain unchanged":
                    a "Incorrect. Heights must be recomputed for affected nodes."
                "Heights of rotated nodes must be updated using their children's heights after pointer changes":
                    $ chapter_6_score += 1
                    a "Correct! Update heights of the two main nodes involved using their new child heights."
                "Heights are globally recomputed from root each rotation":
                    a "Incorrect. Global recompute is unnecessary and expensive."

        elif current_q == "q5":
            a "Which of these statements about AVL vs Red-Black trees is correct in practice?"
            menu:
                "AVL has stricter balance, so searches are often faster but updates (rotations) can be more frequent":
                    $ chapter_6_score += 1
                    a "Correct! AVL tends to be shallower; RB trades slightly taller trees for fewer rotations on updates."
                "Red-Black trees are always faster for search due to color bits":
                    a "Incorrect. RB are often slightly slower for searches due to looser balance."
                "AVL never requires rotations while RB always does":
                    a "Incorrect. Both require rotations; frequency differs."

        elif current_q == "q6":
            a "Suppose you store only a node's balance factor (−1,0,+1) instead of full height. After a rotation, how do you update balance factors efficiently?"
            menu:
                "Recompute the entire subtree heights to derive balance factors":
                    a "Incorrect. That is inefficient."
                "Use local formulas based on previous balance factors and rotation type to update in O(1) for affected nodes":
                    $ chapter_6_score += 1
                    a "Correct! Balance factors can be updated locally with case formulas for single/double rotations."
                "Balance factors cannot be kept without full heights":
                    a "Incorrect. Balance factors suffice with correct local updates."

        elif current_q == "q7":
            a "When performing a double rotation (LR or RL), how many pointer reassignments are strictly necessary among the three main nodes involved?"
            menu:
                "Zero; only heights change":
                    a "Incorrect. Pointers must be reattached."
                "A constant small number (O(1)), typically several pointer updates among three nodes and their subtrees":
                    $ chapter_6_score += 1
                    a "Correct! Rotations are O(1) pointer reassignments affecting a few nodes and subtrees."
                "O(h) pointer reassignments where h is tree height":
                    a "Incorrect. Rotations are local, not proportional to height."

        elif current_q == "q8":
            a "Which insertion order will produce the maximum number of rotations in AVL when inserting 1..n sequentially into an initially empty tree?"
            menu:
                "Random order produces the worst-case number of rotations":
                    a "Incorrect. Random tends to average-case behavior."
                "Strictly increasing order (1..n) causes many rotations but AVL rebalances, not worst-case exponential rotations":
                    $ chapter_6_score += 1
                    a "Correct! Sequential insertions force rotations regularly but total per-insert cost remains O(log n)."
                "Inserting all even keys then odd keys causes no rotations":
                    a "Incorrect. Specific patterns still cause rotations."

        elif current_q == "q9":
            a "If you augment AVL nodes with subtree sizes, can you maintain sizes across rotations without traversing the subtree?"
            menu:
                "No; maintaining sizes requires full subtree scan after rotation":
                    a "Incorrect. That's unnecessary."
                "Yes; sizes are local aggregates and can be updated for affected nodes using children's stored sizes in O(1) during rotations":
                    $ chapter_6_score += 1
                    a "Correct! Subtree sizes update from children sizes during rotations in constant time for affected nodes."
                "Only if you recompute from leaves upward":
                    a "Incorrect. Local updates suffice."

        elif current_q == "q10":
            a "Which of the following is a correct worst-case bound on the height h of an AVL tree with n nodes?"
            menu:
                "h ≤ 1.44 * log2(n + 2) − 0.328 (approx)":
                    $ chapter_6_score += 1
                    a "Correct! Height of AVL is O(log n) with a known constant ≈ 1.44."
                "h ≤ n/2":
                    a "Incorrect. That's far too large for AVL."
                "h ≤ log2(log2 n)":
                    a "Incorrect. That's far too small."

        elif current_q == "q11":
            a "When rebalancing after deletion, you perform a rotation that makes an ancestor's balance factor zero. What is the effect on further upward rebalancing?"
            menu:
                "You must always stop; no further ancestors can be unbalanced":
                    a "Incorrect. It depends on previous state; sometimes you stop, sometimes continue."
                "If the ancestor becomes balanced (0), rebalancing may stop; if it becomes ±1, you stop; if it becomes ±2, continue upward after rotations":
                    $ chapter_6_score += 1
                    a "Correct! The exact updated balance determines whether rebalancing continues."
                "You always continue up to the root regardless":
                    a "Incorrect. Some rotations restore heights so you can stop."

        elif current_q == "q12":
            a "Which sequence of checks is necessary when inserting to decide which rotation to apply at the lowest unbalanced ancestor?"
            menu:
                "Check the sign of the ancestor's balance only":
                    a "Incorrect. You must examine the child's balance to choose single vs double rotation."
                "Check ancestor's balance sign and the sign of the heavier child's balance to determine single vs double rotation":
                    $ chapter_6_score += 1
                    a "Correct! Child's heavy side decides LL/RR vs LR/RL and whether double rotation needed."
                "Always perform double rotation to be safe":
                    a "Incorrect. Unnecessary double rotations waste operations."

        elif current_q == "q13":
            a "What is the effect of maintaining parent pointers on rotation implementations and complexity?"
            menu:
                "Parent pointers eliminate the need to update child pointers":
                    a "Incorrect. Child pointers still change; parent pointers must be updated too."
                "They increase constant work during rotations since parent links must be updated, but rotations remain O(1)":
                    $ chapter_6_score += 1
                    a "Correct! Parent pointers add constant updates but don't change asymptotic cost."
                "Parent pointers make rotations O(log n)":
                    a "Incorrect. Rotations remain local O(1) operations."

        elif current_q == "q14":
            a "Consider building an AVL tree by inserting n keys drawn uniformly at random. What is the expected height and why?"
            menu:
                "Expected height is Θ(n) because randomness creates chains":
                    a "Incorrect. Random inserts into AVL remain balanced."
                "Expected height is Θ(log n) because AVL maintains logarithmic height guarantees and randomness doesn't worsen it":
                    $ chapter_6_score += 1
                    a "Correct! AVL invariants keep height logarithmic; random keys produce typical logarithmic height."
                "Expected height is Θ(log log n) due to randomization":
                    a "Incorrect. That's not the correct bound for AVL."

        elif current_q == "q15":
            a "Which of these is a subtle bug to watch for when implementing rotations in a language with manual memory management?"
            menu:
                "Failing to update parent pointers leading to cycles or dangling references":
                    $ chapter_6_score += 1
                    a "Correct! Incorrect parent updates can create corrupted structure or leaks."
                "Using recursion for traversal":
                    a "Incorrect. Recursion is not the rotation-specific bug described."
                "Choosing wrong comparison operator (< vs <=) in keys only":
                    a "Incorrect. Key comparison bugs are serious but not memory-management specific."

        elif current_q == "q16":
            a "Which technique allows rebuilding an AVL tree in linear time given all keys sorted?"
            menu:
                "Insert keys one by one into AVL using standard insert":
                    a "Incorrect. That costs O(n log n) in general."
                "Construct a perfectly balanced BST by recursive middle selection then compute balance/heights":
                    $ chapter_6_score += 1
                    a "Correct! Building from sorted array by midpoint recursion yields O(n) if heights computed bottom-up."
                "Use random shuffling before insertions to get expected linear time":
                    a "Incorrect. Shuffling doesn't give deterministic linear build for AVL."

        elif current_q == "q17":
            a "When combining AVL with additional augmentation (e.g., sum of subtree), which property ensures rotations maintain augmentation correctness locally?"
            menu:
                "Augmentations must be computable from children's augmentations and node's own value":
                    $ chapter_6_score += 1
                    a "Correct! If augmentation is a function of children and node, rotations can update it locally."
                "Augmentations must depend on global tree shape":
                    a "Incorrect. Global dependencies break local updates."
                "Augmentations must be stored in external arrays only":
                    a "Incorrect. External storage is unnecessary and complicates updates."

        elif current_q == "q18":
            a "Suppose you implement iterative insertion without recursion. What additional bookkeeping do you most likely need to perform rebalancing?"
            menu:
                "A stack or parent pointers to trace back the insertion path so you can update heights and rebalance upward":
                    $ chapter_6_score += 1
                    a "Correct! Iterative insertion needs a way to walk back up to update and rebalance."
                "Nothing; iterative insertion auto-updates ancestors":
                    a "Incorrect. You must explicitly update ancestors' heights/balance."
                "Only a queue of siblings":
                    a "Incorrect. A queue of siblings doesn't help trace parent path."

        elif current_q == "q19":
            a "Which complexity statement about sequences of m mixed AVL operations (inserts/deletes/searches) on n-sized trees is accurate?"
            menu:
                "Each operation worst-case O(log n), so the sequence is O(m log n)":
                    $ chapter_6_score += 1
                    a "Correct! Each op is O(log n) worst-case, so m ops cost O(m log n)."
                "Amortized cost per operation becomes O(1) due to rotations balancing out":
                    a "Incorrect. There is no O(1) amortized guarantee for AVL operations."
                "Search is O(n) but insert/delete are O(log n)":
                    a "Incorrect. Search is O(log n) as well."

        elif current_q == "q20":
            a "Which approach is safest to test a new AVL implementation for correctness?"
            menu:
                "Compare behavior against a simple unbalanced BST on random inputs only":
                    a "Incorrect. Unbalanced BST won't reveal balance invariants easily."
                "Automated randomized testing against a reference (e.g., rebuild from sorted keys) plus invariants checks (balance factors, heights, in-order correctness)":
                    $ chapter_6_score += 1
                    a "Correct! Randomized tests plus invariant checks and reference rebuilds expose many bugs."
                "Manual inspection of tree diagrams only":
                    a "Incorrect. Manual inspection is error-prone and slow."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Your quiz score is: [chapter_6_score]"
    jump chapter_6_performance
label chapter_6_performance:

# Properties
    if chapter_6_AVL_Properties_quiz < 2:
        a "You need to review the Properties of AVL Trees section."
        a "Focus on height balance and node structure."
    elif chapter_6_AVL_Properties_quiz < 3:
        a "You did okay in Properties, but there's room for improvement."
        a "Revisiting balance factor logic could help."

# Operations
    if chapter_6_AVL_Operations_quiz < 2:
        a "You need to review AVL Tree Operations."
        a "Pay attention to insertions and deletions with rebalancing."
    elif chapter_6_AVL_Operations_quiz < 3:
        a "You did okay in Operations, but there's room for improvement."
        a "Try tracing how rotations are triggered during insert/delete."

# Balanced Trees
    if chapter_6_Balanced_Trees_quiz < 2:
        a "You need to review Balanced Trees."
        a "Understand why balance matters for performance."
    elif chapter_6_Balanced_Trees_quiz < 3:
        a "You did okay in Balanced Trees, but there's room for improvement."
        a "Compare AVL with other balanced trees like Red-Black."

# Rotations
    if chapter_6_Rotations_quiz < 2:
        a "You need to review Rotations."
        a "Focus on LL, RR, LR, and RL cases."
    elif chapter_6_Rotations_quiz < 3:
        a "You did okay in Rotations, but there's room for improvement."
        a "Practice visualizing rotation steps."

    jump chapter_6_end

label chapter_6_end:
    play sound "sfx/success.mp3"
    play music "bgm/city-high-life.mp3" fadein 1.0
    $ persistent.chapter_6 = True
    a "Would You like to test again?"
    menu:
        "Yes":
            jump chapter_6_restart
        "No":
            pass
    show adrian happy
    a "You have finished chapter 6. You can continue to Chapter 7!"
    jump menu
       