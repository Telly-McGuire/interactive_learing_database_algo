
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
    call hideall #This is a stupid fix but it works I think
    play audio ("sfx/start.mp3")
    play music "bgm/city-high-life.mp3" fadein 1.0

    scene black
    pause 1.0
    show screen chapter_6_AVLIntro
    pause 2.0
    scene mt tree with dissolve
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


    a "Hey there! Whats up aligator."
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
    a "AVL Trees maintain balance by keeping the height difference between left and right subtrees within one."

    a "This difference is called the balance factor. If it strays outside -1 to +1, the tree performs rotations to fix itself."

    a "There are four types of rotations: Left, Right, Left-Right, and Right-Left. They’re surgical—just enough to restore order."

    show adrian explaining
    a "Why does this matter? Because balanced trees mean fast operations. Searching, inserting, and deleting all stay efficient."

    a "AVL Trees are great when you need consistent performance and can’t afford the worst-case slowness of unbalanced trees."

    show adrian smiling
    a "They’re like disciplined librarians—always keeping things neat so you can find what you need in no time."

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


label chapter_6_quiz_easy:
label chapter_6_quiz_medium:
label chapter_6_quiz_hard:

label chapter_6_quiz_end:
    a "Your total score is [chapter_6_test] out of 25"
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
       