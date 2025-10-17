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
    a "Red-Black Trees support standard binary search tree operations such as {b}insertion, deletion, and search{/b}."
    a "But what makes them special is how they maintain balance through color properties and rotations."
    a "This ensures operations stay efficient—typically in {i}O(log n){/i} time."

    a "Each node is either red or black, and the tree follows strict rules to preserve balance:"
    a "- The root is always black."
    a "- Red nodes can't have red children."
    a "- Every path from a node to its descendant leaves must have the same number of black nodes."

    a "These rules might seem rigid, but they’re what give Red-Black Trees their power in real-time systems and databases."

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

    a "Now that you’ve got a handle on the basic operations of Red-Black Trees, let’s explore how they stay balanced after insertions and deletions."
    a "Unlike regular binary search trees, Red-Black Trees maintain their structure using a smart mix of {b}recoloring{/b} and {b}rotations{/b}."

    a "Let’s begin with recoloring. This technique involves changing the color of certain nodes—either from red to black or vice versa—to fix violations of the tree’s rules."
    a "For instance, if inserting a red node results in two red nodes appearing consecutively, recoloring might be enough to restore balance without altering the tree’s shape."

    a "However, recoloring isn’t always sufficient. That’s when rotations come into play."

    a "Rotations are structural adjustments that reposition nodes while keeping the binary search tree order intact."
    a "There are two types of rotations: {b}left rotation{/b} and {b}right rotation{/b}."
    a "A left rotation moves a node down to the left and promotes its right child. A right rotation does the opposite—it lowers a node to the right and raises its left child."

    a "These rotations are especially useful when recoloring alone can’t fix deeper structural issues, such as a red node having a red child."

    a "By combining recoloring and rotations, Red-Black Trees maintain their balance, ensuring that operations like search, insert, and delete remain efficient—usually in {i}O(log n){/i} time."

    a "It might sound a bit tricky at first, but once you see these operations in action, the logic becomes much easier to grasp."

    $ chapter_7_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Alright, let’s see what you’ve learned. Time for a quick quiz!"
    jump chapter_7_Recoloring_Rotation_Quiz

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