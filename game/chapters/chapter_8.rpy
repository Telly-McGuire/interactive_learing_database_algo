# Chapter 8: Heaps
# Topics:
# - Introduction to priority queues
# - Heap basics
# - Array representation
# - Remove operation
# - Heap sort
# - Operation complexities
# - Binomial and Fibonacci heaps

default chapter_8_progress = 0

default chapter_8_Priority_Queues_quiz = 0
default chapter_8_Heap_Basics_quiz = 0
default chapter_8_Array_Representation_quiz = 0
default chapter_8_Remove_Operation_quiz = 0
default chapter_8_Heap_Sort_quiz = 0



screen chapter_8_HeapsIntro:
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 200
        ypadding 60
        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5
            text "Heaps" size 60 color "#FFFFFF" outlines [(5, "#000000", 0, 0)]


label chapter_8_intro:

    call hideall
    play sound "sfx/start.mp3"
    stop music fadeout 1.0

    scene black
    pause 1.0

    show screen chapter_8_HeapsIntro
    scene mt tree with dissolve
    pause 2.0
    hide screen chapter_8_HeapsIntro

    show screen menu_btn

    play music "bgm/city-high-life.mp3" fadein 1.0
    show adrian smiling at center:
        smaller
    with dissolve

    if persistent.chapter_8 == True:
        a "Welcome Back to Chapter 8 : Heaps"
        a "Would you like to go throught the chapter again?"
        menu:
            "Yes":
                a "Pick a topic"
                menu:
                    "Priority Queues":
                        jump chapter_8_Priority_Queues
                    "Heap Basics":
                        jump chapter_8_Heap_Basics
                    "Array Representation":
                        jump chapter_8_Array_Representation
                    "Remove Operation":
                        jump chapter_8_Remove_Operation
                    "Heap Sorting":
                        jump chapter_8_Heap_Sort                    
            "No":
                pass

    show adrian normal
    a "Ready to climb a mountain?"
    menu:
        "Yes":
            a "Ew. Ok"
        "No"
            show adrian smiling
            a "Yeah me too, its exhausting" 

    show adrian smug
    a "But you know... "
    show adrian smiling
    a "Nevermind"
    a "Teehee"


    a "Let's explore how heaps works."
    show adrian smiling
    a "Welcome to Chapter 8: Heaps"

label chapter_8_Priority_Queues:

    show adrian happy
    play sound "sfx/notification.mp3"
    a "So what are Heaps?"
    a "But first you need to understand"
    a "{b}Priority Queue{/b}."

    a "Unlike a regular queue, this one serves items by {b}priority{/b} — not arrival order. Ready for a mini scheduler simulation?"

    screen chapter_8_scheduler():
        frame:
            xalign 0.7
            yalign 0.1
            xpadding 40
            ypadding 30
            vbox:
                spacing 12
                xalign 0.5

                text "Scheduler — Pending Tasks" size 40 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]

                vbox:
                    spacing 6
                    text "1) Clean windows — priority 2" size 26
                    text "2) Emergency fix — priority 9" size 26
                    text "3) Auto-save — priority 5" size 26

    show screen chapter_8_scheduler
    show adrian explaining at left 
    with move
    a "Take this list of tasks for example"
    a "WHich you think goes first?"

    menu:
        "Run Emergency fix (priority 9)":
            $ chapter_8_demo_correct = True
            show adrian happy
            play sound "sfx/ting.mp3"
            a "Good call! The highest-priority task runs first."
        "Run Auto-save (priority 5)":
            $ chapter_8_demo_correct = False
            show adrian double
            play sound "sfx/ting.mp3"
            a "Not ideal — auto-save is important, but the emergency fix outranks it."
        "Run Clean windows (priority 2)":
            $ chapter_8_demo_correct = False
            show adrian doubt
            play sound "sfx/ting.mp3"
            a "That’s low priority — it wouldn’t run before the emergency."

    if chapter_8_demo_correct:
        play sound "sfx/success.mp3"
        show adrian smiling
        a "Exactly. A priority queue always picks the item with the top priority (here, 9)."
    else:
        show adrian normal
        a "In a priority queue, priorities decide order — arrival time doesn’t override a higher priority."

    a "Under the hood, heaps power most priority queues. They let us insert and remove the top item efficiently (about O(log n))."

    menu:
        "Add 'Security patch' (priority 7) and show order":
            play sound "sfx/ting.mp3"
            show adrian smiling
            a "After inserting priority 7, the scheduler order becomes: 9 → 7 → 5 → 2 (highest to lowest)."
            a "Heaps keep this order with simple index math and swaps."
        "Skip the insertion demo":
            play sound "sfx/ting.mp3"
            show adrian normal
            a "Okay — we’ll move on to the quiz."

    hide screen chapter_8_scheduler
    show adrian normal at center
    with move
    a "Thats how Priority Works in Heaps basiacally"
    show adrian smiling
    a "The more you know"

    $ chapter_8_progress += 1
    play sound "sfx/bell.mp3"
    show adrian smiling
    a "Nice! Let’s test this with a quick quiz."
    jump chapter_8_Priority_Queues_Quiz

init python:
    import random
    chapter_8_Priority_Queues_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_8_Priority_Queues_order)

label chapter_8_Priority_Queues_Quiz:
    #5POINTS
    $ chapter_8_Priority_Queues_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_8_Priority_Queues_order:
        $ current_q = chapter_8_Priority_Queues_order.pop(0)

        if current_q == "q1":
            a "What is the main purpose of a priority queue?"
            menu:
                "To access elements based on priority":
                    $ chapter_8_Priority_Queues_quiz += 1
                    a "Correct! Priority queues always return the highest or lowest priority item first."
                "To store elements in sorted order":
                    a "Incorrect! Sorting is not guaranteed—only priority-based access."
                "To remove duplicates from a list":
                    a "Incorrect! That’s not a function of priority queues."

        elif current_q == "q2":
            a "Which data structure is commonly used to implement a priority queue?"
            menu:
                "Heap":
                    $ chapter_8_Priority_Queues_quiz += 1
                    a "Correct! Heaps are ideal for efficiently managing priorities."
                "Stack":
                    a "Incorrect! Stacks follow LIFO, not priority."
                "Linked List":
                    a "Incorrect! Linked lists don’t offer efficient priority access."

        elif current_q == "q3":
            a "In a min-heap priority queue, which element is removed first?"
            menu:
                "The smallest element":
                    $ chapter_8_Priority_Queues_quiz += 1
                    a "Correct! Min-heaps always remove the smallest item first."
                "The largest element":
                    a "Incorrect! That’s true for max-heaps."
                "The most recently added element":
                    a "Incorrect! That’s how stacks behave."

        elif current_q == "q4":
            a "What operation maintains the heap property after insertion?"
            menu:
                "Heapify-up":
                    $ chapter_8_Priority_Queues_quiz += 1
                    a "Correct! Heapify-up restores order after adding a new element."
                "Heapify-down":
                    a "Incorrect! That’s used after removal."
                "Sort":
                    a "Incorrect! Sorting isn’t part of heap maintenance."

        elif current_q == "q5":
            a "Which of the following is true about priority queues?"
            menu:
                "They allow fast access to the highest-priority item":
                    $ chapter_8_Priority_Queues_quiz += 1
                    a "Correct! That’s their core feature."
                "They always keep elements in alphabetical order":
                    a "Incorrect! Priority is based on values, not names."
                "They use FIFO ordering":
                    a "Incorrect! That’s how queues behave, not priority queues."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_8_Priority_Queues_quiz] out of 5."
    jump chapter_8_Heap_Basics
label chapter_8_Heap_Basics:

    show adrian normal at left
    play sound "sfx/notification.mp3"
    a "Heaps are a compact binary tree used to keep the top item easy to access."
    a "Two flavors: {b}min-heap{/b} (smallest at root) and {b}max-heap{/b} (largest at root)."
    a "They’re always {b}complete binary trees{/b}, so we store them neatly in arrays."
    a "Let’s walk through how a max-heap is built step-by-step."

    # Separate screens for each step. Each returns "prev", "next", or "close".
    screen chapter_8_heap_demo_0():
        modal True
        tag chapter_8_heap_demo
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 40
            ypadding 30
            vbox:
                spacing 20
                text "Max-Heap Demo" size 50 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "Let’s build a max-heap from this array:\n[3, 1, 6, 5, 2, 4]" size 32

                hbox:
                    spacing 12
                    textbutton "Next" action [Play("sound", "sfx/ting.mp3"), Return("next")]

    screen chapter_8_heap_demo_1():
        modal True
        tag chapter_8_heap_demo
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 40
            ypadding 30
            vbox:
                spacing 20
                text "Max-Heap Demo" size 50 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "Step 1 — Treat as tree level-by-level (no swaps yet):\n[3, 1, 6, 5, 2, 4]" size 30

                hbox:
                    spacing 12
                    textbutton "Prev" action Return("prev")
                    textbutton "Next" action [Play("sound", "sfx/ting.mp3"), Return("next")]

    screen chapter_8_heap_demo_2():
        modal True
        tag chapter_8_heap_demo
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 40
            ypadding 30
            vbox:
                spacing 20
                text "Max-Heap Demo" size 50 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "Step 2 — Compare node 6 with parent 3 → swap to make parent larger:\n[6, 1, 3, 5, 2, 4]" size 30

                hbox:
                    spacing 12
                    textbutton "Prev" action Return("prev")
                    textbutton "Next" action [Play("sound", "sfx/ting.mp3"), Return("next")]

    screen chapter_8_heap_demo_3():
        modal True
        tag chapter_8_heap_demo
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 40
            ypadding 30
            vbox:
                spacing 20
                text "Max-Heap Demo" size 50 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "Step 3 — Check node 5 and 1 → swap if needed:\n[6, 5, 3, 1, 2, 4]" size 30

                hbox:
                    spacing 12
                    textbutton "Prev" action Return("prev")
                    textbutton "Next" action [Play("sound", "sfx/ting.mp3"), Return("next")]

    screen chapter_8_heap_demo_4():
        modal False
        tag chapter_8_heap_demo
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 40
            ypadding 30
            vbox:
                spacing 20
                text "Max-Heap Demo" size 50 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "Result: Root is 6 (largest).\nAccessing max is now O(1);\nInserting/removing is O(log n)." size 30

                hbox:
                    spacing 12
                    textbutton "Prev" action Return("prev")
                    textbutton "Close" action [Play("sound", "sfx/success.mp3"), Return("close")]

    a "We’ll start with an unsorted array and build the heap from it."
    call screen chapter_8_heap_demo_0

    a "This is how the array looks when visualized as a binary tree—level by level."
    call screen chapter_8_heap_demo_1

    a "Now we compare node 6 with its parent 3. Since 6 is larger, we swap them."
    call screen chapter_8_heap_demo_2

    a "Next, we compare node 5 with its parent 1. Again, 5 is larger, so we swap."
    call screen chapter_8_heap_demo_3

    a "Now the largest value, 6, is at the root. This is a valid max-heap!"
    call screen chapter_8_heap_demo_4

    a "Take a moment to review the heap structure."
    a "Why this matters: heaps give predictable performance for priority tasks and in-place sorting (heapsort)."

    show adrian smiling at center 
    with move
    $ chapter_8_progress += 1
    play sound "sfx/bell.mp3"
    show adrian smiling
    a "Short and sweet. Time for a quiz on heap basics!"
    jump chapter_8_Heap_Basics_Quiz

init python:
    import random
    chapter_8_Heap_Basics_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_8_Heap_Basics_order)

label chapter_8_Heap_Basics_Quiz:
    #5POINTS
    $ chapter_8_Heap_Basics_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_8_Heap_Basics_order:
        $ current_q = chapter_8_Heap_Basics_order.pop(0)

        if current_q == "q1":
            a "What type of heap always has the smallest element at the root?"
            menu:
                "Min-heap":
                    $ chapter_8_Heap_Basics_quiz += 1
                    a "Correct! Min-heaps keep the smallest element at the top."
                "Max-heap":
                    a "Incorrect! Max-heaps store the largest element at the root."
                "Binary search tree":
                    a "Incorrect! BSTs don’t guarantee root value."

        elif current_q == "q2":
            a "Which property must a heap always satisfy?"
            menu:

                "It must be balanced":
                    a "Incorrect! Heaps don’t require strict balancing."
                "It must be sorted":
                    a "Incorrect! Only the heap property matters, not full sorting."
                "It must be a complete binary tree":
                    $ chapter_8_Heap_Basics_quiz += 1
                    a "Correct! Heaps are always complete binary trees."
        elif current_q == "q3":
            a "What is the main use of heaps in computer science?"
            menu:

                "Storing sorted arrays":
                    a "Incorrect! Heaps don’t maintain full sorted order."
                "Searching for elements":
                    a "Incorrect! Heaps aren’t optimized for search operations."
                "Implementing priority queues":
                    $ chapter_8_Heap_Basics_quiz += 1
                    a "Correct! Heaps are ideal for managing priorities efficiently."
        elif current_q == "q4":
            a "Which of the following is true about max-heaps?"
            menu:

                "The smallest element is at the root":
                    a "Incorrect! That’s true for min-heaps."
                "All elements are sorted":
                    a "Incorrect! Heaps only maintain partial order."
                "The largest element is at the root":
                    $ chapter_8_Heap_Basics_quiz += 1
                    a "Correct! That’s the defining feature of a max-heap."
        elif current_q == "q5":
            a "Why are heaps efficient for priority queues?"
            menu:                
                "They use recursion to store values":
                    a "Incorrect! Heaps are typically stored in arrays."
                "They allow fast access to the highest or lowest priority item":
                    $ chapter_8_Heap_Basics_quiz += 1
                    a "Correct! The root always holds the top-priority element."

                "They sort all elements automatically":
                    a "Incorrect! Heaps maintain structure, not full sorting."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_8_Heap_Basics_quiz] out of 5."
    jump chapter_8_Array_Representation

label chapter_8_Array_Representation:

    # A prettier, more dynamic presentation of array-backed heaps.

    show adrian normal at center with dissolve
    play sound "sfx/bell.mp3"

    a "{size=+10}{color=#89CFF0}Array Representation — Heaps Made Compact{/color}{/size}"
    a "Heaps are nearly perfect for arrays because they are {b}complete binary trees{/b} — filled left to right with no gaps."

    show adrian smiling
    a "Instead of pointers, we map tree positions straight to indices. That keeps memory usage tidy and access fast."

    pause 0.5

    # A small interactive reveal to make it feel dynamic.

    a "Quick visual demo"
    play sound "sfx/ting.mp3"
    a "{size=+6}{color=#FFD27F}Index mapping (0-based):{/color}{/size}"

    screen chapter_8_array_demo():
        tag chapter_8_array_demo
        frame:
            xalign 0.75
            yalign 0.4
            xpadding 80
            ypadding 80
            vbox:
                spacing 12
                text "Array Representation — Visual" size 40 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "Index:   [[0]   [[1]   [[2]   [[3]   [[4]   [[5]   [[6]\nValue:   50    30    40    10    20    35    45\n\nInterpretation:\n - Root at index {b}0{/b}\n - Left child of i → {b}2*i + 1{/b}\n - Right child of i → {b}2*i + 2{/b}\n - Parent of i → {b}(i - 1) // 2{/b}" size 26

    show screen chapter_8_array_demo
    show adrian at left
    with move
    pause 0.6
    a "Example: Node at index {b}1{/b} (value 30) has children at indices {b}3{/b} and {b}4{/b} (values 10 and 20)."
    a "So it goes like this and that"
    pause 0.4
    play sound "sfx/ting.mp3"
    a "Neat, right? No pointers"
    a "This structure makes heaps super efficient: you can jump between parent and child nodes instantly using simple math."
    a "That’s why heaps are often implemented as arrays — it’s compact, fast, and memory-friendly."
    a "And since heaps are complete binary trees, there are no gaps — every level is filled left to right, which keeps the array tight and predictable."
    a "This layout is what makes operations like insertions and deletions run in {b}O(log n){/b} time — perfect for priority queues and heapsort!"

    hide screen chapter_8_array_demo
    show adrian explaining at center
    with move
    a "Why this is useful:"
    a "- Arrays avoid pointer overhead and make parent/child moves constant-time index math."
    a "- Great for in-place algorithms like {b}heapsort{/b} and efficient priority queues."

    $ chapter_8_progress += 1
    play sound "sfx/bell.mp3"
    show adrian smiling
    a "Ready for a quick quiz to cement this? Let’s go!"
    jump chapter_8_Array_Representation_Quiz

init python:
    import random
    chapter_8_Array_Representation_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_8_Array_Representation_order)

label chapter_8_Array_Representation_Quiz:
    #5POINTS
    $ chapter_8_Array_Representation_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_8_Array_Representation_order:
        $ current_q = chapter_8_Array_Representation_order.pop(0)

        if current_q == "q1":
            a "How are heaps typically stored in memory?"
            menu:
                "As arrays":
                    $ chapter_8_Array_Representation_quiz += 1
                    a "Correct! Heaps are stored as arrays for efficient access."
                "As linked lists":
                    a "Incorrect! Linked lists don’t support fast index-based access."
                "As hash tables":
                    a "Incorrect! Hash tables are used for key-value storage, not heaps."

        elif current_q == "q2":
            a "In a heap stored as an array, where is the left child of node at index i?"
            menu:
                "2i + 1":
                    $ chapter_8_Array_Representation_quiz += 1
                    a "Correct! That’s the formula for the left child."
                "2i":
                    a "Incorrect! That’s not the correct index."
                "i + 1":
                    a "Incorrect! That’s just the next element, not necessarily a child."

        elif current_q == "q3":
            a "What is the index of the parent of a node at index i?"
            menu:                
                "i // 2":
                    a "Incorrect! That’s used in some contexts but not for heap parents."
                "(i - 1) // 2":
                    $ chapter_8_Array_Representation_quiz += 1
                    a "Correct! That formula gives the parent’s index."

                "2i - 1":
                    a "Incorrect! That’s not a valid parent index formula."

        elif current_q == "q4":
            a "Why is array representation efficient for heaps?"
            menu:

                "It automatically sorts the elements":
                    a "Incorrect! Heaps maintain partial order, not full sorting."
                "It uses less memory than arrays":
                    a "Incorrect! Heaps are stored in arrays."
                "It avoids using pointers and supports fast indexing":
                    $ chapter_8_Array_Representation_quiz += 1
                    a "Correct! Arrays make heap operations fast and memory-efficient."
        elif current_q == "q5":
            a "What kind of binary tree must a heap be to use array representation?"
            menu:

                "Balanced binary tree":
                    a "Incorrect! Balance isn’t required for heaps."
                "Full binary tree":
                    a "Incorrect! Heaps don’t need every node to have two children."
                "Complete binary tree":
                    $ chapter_8_Array_Representation_quiz += 1
                    a "Correct! Completeness ensures no gaps in the array."
    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_8_Array_Representation_quiz] out of 5."
    jump chapter_8_Remove_Operation

label chapter_8_Remove_Operation:

    show adrian explaining at left
    play sound "sfx/notification.mp3"
    a "Let’s make removing the root from a heap feel like a tiny action movie — step-by-step and visual."

    a "We’ll remove the root from this max-heap and watch how the structure repairs itself to keep the largest value at the top."

    screen chapter_8_remove_demo_0():

        tag chapter_8_remove_demo
        frame:
            xalign 0.8
            yalign 0.5
            xpadding 60
            ypadding 80
            vbox:
                spacing 14
                text "Remove — Step 0: Current Heap" size 46 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "Array (level order): [60, 40, 50, 20, 30, 10, 5]\nRoot = 60 (max)" size 28
                text "Action: Remove root (60). To keep completeness, move the last element to the root, then rebuild." size 22


    screen chapter_8_remove_demo_1():

        tag chapter_8_remove_demo
        frame:
            xalign 0.8
            yalign 0.5
            xpadding 60
            ypadding 80
            vbox:
                spacing 14
                text "Remove — Step 1: Replace Root" size 46 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "After removing 60, last element 5 moves to root:\n[5, 40, 50, 20, 30, 10]\nNow the heap property may be broken." size 26
                text "We will heapify-down: compare 5 with its children (40 and 50) and swap with the larger child." size 20


    screen chapter_8_remove_demo_2():

        tag chapter_8_remove_demo
        frame:
            xalign 0.8
            yalign 0.5
            xpadding 60
            ypadding 80
            vbox:
                spacing 14
                text "Remove — Step 2: First Heapify-Down Swap" size 46 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "Compare 5 with children 40 and 50 → swap with larger child 50:\n[50, 40, 5, 20, 30, 10]" size 26
                text "5 is now at index 2. Continue heapify-down until both children are smaller than 5." size 20


    screen chapter_8_remove_demo_3():

        tag chapter_8_remove_demo
        frame:
            xalign 0.8
            yalign 0.5
            xpadding 60
            ypadding 80
            vbox:
                spacing 14
                text "Remove — Step 3: Finalize Heapify-Down" size 46 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "At index 2, children are [10] (only left child here). Swap 5 with 10 → [50, 40, 10, 20, 30, 5]" size 26
                text "Now 5 has no larger children — heap property restored. Root is 50 (max)." size 20


    # Run the demo sequence
    show adrian explaining at left
    with move
    show screen chapter_8_remove_demo_0
    a "Let’s make removing the root from a heap feel like a tiny action movie — step-by-step and visual."
    a "We’ll remove the root from this max-heap and watch how the structure repairs itself to keep the largest value at the top."

    a "Step 0 — Here’s our starting heap. The root is 60, the largest value."
    a "We’ll remove it and prepare to rebuild the heap."
    hide screen chapter_8_remove_demo_0
    
    show screen chapter_8_remove_demo_1
    a "Step 1 — To maintain the complete binary tree structure, we move the last element (5) to the root."
    a "But now the heap property is broken — the root is no longer the largest."
    hide screen chapter_8_remove_demo_1

    show screen chapter_8_remove_demo_2
    a "Step 2 — We begin heapify-down. Compare the new root (5) with its children: 40 and 50."
    a "Since 50 is the largest, we swap 5 with 50 to restore order at the top."
    hide screen chapter_8_remove_demo_2

    show screen chapter_8_remove_demo_3
    a "Step 3 — 5 is now at index 2. It still has a child: 10."
    a "We compare and swap again, placing 5 where it belongs. Now the heap is fixed!"
    hide screen chapter_8_remove_demo_3
    with dissolve

    show adrian smiling at center
    with move
    a "Summary: remove root → move last element to root → heapify-down (swap with larger child) until the heap property is restored."

    $ chapter_8_progress += 1
    play sound "sfx/bell.mp3"
    a "Ready for a quiz on Remove operations?"
    jump chapter_8_Remove_Operation_Quiz
init python:
    import random
    chapter_8_Remove_Operation_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_8_Remove_Operation_order)

label chapter_8_Remove_Operation_Quiz:
    #5POINTS
    $ chapter_8_Remove_Operation_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_8_Remove_Operation_order:
        $ current_q = chapter_8_Remove_Operation_order.pop(0)

        if current_q == "q1":
            a "What happens first when removing the root from a heap?"
            menu:
                
                "The heap is sorted":
                    a "Incorrect! Sorting isn’t part of the removal process."
                "The root is deleted and left empty":
                    a "Incorrect! The root must be replaced."
                "The last element replaces the root":
                    $ chapter_8_Remove_Operation_quiz += 1
                    a "Correct! This maintains the complete tree structure."

        elif current_q == "q2":
            a "What operation restores the heap property after removal?"
            menu:
                "Heapify-down":
                    $ chapter_8_Remove_Operation_quiz += 1
                    a "Correct! Heapify-down ensures the new root is correctly positioned."
                "Heapify-up":
                    a "Incorrect! That’s used after insertion."
                "Rebalancing":
                    a "Incorrect! That term applies more to AVL or Red-Black Trees."

        elif current_q == "q3":
            a "Why is the last element used to replace the root?"
            menu:                
                "To avoid reheapifying":
                    a "Incorrect! Reheapifying is still required."
                "To maintain the complete binary tree structure":
                    $ chapter_8_Remove_Operation_quiz += 1
                    a "Correct! This keeps the array-based heap compact and valid."
                "To reduce the number of rotations":
                    a "Incorrect! Heaps don’t use rotations."


        elif current_q == "q4":
            a "Which direction does heapify-down move the new root?"
            menu:                
                "Upward to the top":
                    a "Incorrect! That’s heapify-up."
                "Downward toward its correct position":
                    $ chapter_8_Remove_Operation_quiz += 1
                    a "Correct! It swaps with children until the heap property is restored."

                "Sideways across the tree":
                    a "Incorrect! Heapify-down moves vertically."

        elif current_q == "q5":
            a "What is the time complexity of removing the root from a heap?"
            menu:
               
                "O(n)":
                    a "Incorrect! That would be too slow for a heap."
                "O(1)":
                    a "Incorrect! Removal requires restructuring."
                "O(log n)":
                    $ chapter_8_Remove_Operation_quiz += 1
                    a "Correct! Because heapify-down traverses the height of the tree."
    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_8_Remove_Operation_quiz] out of 5."
    jump chapter_8_Heap_Sort

label chapter_8_Heap_Sort:

    show adrian normal
    play sound "sfx/notification.mp3"
    a "Let’s wrap up this chapter with a powerful sorting algorithm: {b}Heap Sort{/b}."
    a "I’ll walk you through a short step-by-step demo using the array: [3, 1, 6, 5, 2, 4]."

    # Screens for each step. Each returns "prev", "next", or "close".
    screen chapter_8_heapsort_step_0():
        modal True
        tag chapter_8_heapsort
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 40
            ypadding 30
            vbox:
                spacing 18
                text "Heap Sort — Step 0" size 44 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "Start: input array (level order):\n[3, 1, 6, 5, 2, 4]" size 28
                text "Goal: build a max-heap, then repeatedly remove the max to form a sorted array." size 22
                hbox:
                    spacing 12
                    textbutton "Next" action [Play("sound", "sfx/ting.mp3"), Return("next")]

    screen chapter_8_heapsort_step_1():
        modal True
        tag chapter_8_heapsort
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 40
            ypadding 30
            vbox:
                spacing 18
                text "Heap Sort — Step 1: Build max-heap (heapify)" size 44 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "Start heapify from last parent index. Compare children and swap where needed.\nAfter first swaps we get:\n[6, 1, 4, 5, 2, 3]" size 28
                hbox:
                    spacing 12
                    textbutton "Prev" action Return("prev")
                    textbutton "Next" action [Play("sound", "sfx/ting.mp3"), Return("next")]

    screen chapter_8_heapsort_step_2():
        modal True
        tag chapter_8_heapsort
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 40
            ypadding 30
            vbox:
                spacing 18
                text "Heap Sort — Step 2: Max-heap ready" size 44 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "Final max-heap representation (root is max):\n[6, 5, 4, 1, 2, 3]\nRoot (6) is now the largest element." size 28
                hbox:
                    spacing 12
                    textbutton "Prev" action Return("prev")
                    textbutton "Next" action [Play("sound", "sfx/ting.mp3"), Return("next")]

    screen chapter_8_heapsort_step_3():
        modal True
        tag chapter_8_heapsort
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 40
            ypadding 30
            vbox:
                spacing 18
                text "Heap Sort — Step 3: Remove max and place at end" size 44 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "Swap root (6) with last element (3), then heapify-down the new root:\nAfter swap: [3, 5, 4, 1, 2, 6]\nHeapify → [5, 3, 4, 1, 2, 6]" size 28
                hbox:
                    spacing 12
                    textbutton "Prev" action Return("prev")
                    textbutton "Next" action [Play("sound", "sfx/ting.mp3"), Return("next")]

    screen chapter_8_heapsort_step_4():
        modal True
        tag chapter_8_heapsort
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 40
            ypadding 30
            vbox:
                spacing 18
                text "Heap Sort — Step 4: Repeat removal" size 44 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "Swap new root (5) with element at index 3 (2), then heapify:\nAfter swap: [2, 3, 4, 1, 5, 6]\nHeapify → [4, 3, 2, 1, 5, 6]" size 28
                hbox:
                    spacing 12
                    textbutton "Prev" action Return("prev")
                    textbutton "Next" action [Play("sound", "sfx/ting.mp3"), Return("next")]

    screen chapter_8_heapsort_step_5():
        modal False
        tag chapter_8_heapsort
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 40
            ypadding 30
            vbox:
                spacing 18
                text "Heap Sort — Final" size 44 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "Continue these steps until the heap is empty. Final sorted array (ascending):\n[1, 2, 3, 4, 5, 6]" size 28
                hbox:
                    spacing 12
                    textbutton "Prev" action Return("prev")
                    textbutton "Close" action [Play("sound", "sfx/success.mp3"), Return("close")]

    # Sequentially call each step screen (mirrors the heap demo style)
    call screen chapter_8_heapsort_step_0
    call screen chapter_8_heapsort_step_1
    call screen chapter_8_heapsort_step_2
    call screen chapter_8_heapsort_step_3
    call screen chapter_8_heapsort_step_4
    call screen chapter_8_heapsort_step_5
    a "Let’s recap: we first built a max-heap, then repeatedly removed the root (the largest element), placing it at the end of the array."
    a "Each removal was followed by a heapify-down to restore the heap property, shrinking the heap size each time."
    a "This gives us a sorted array in ascending order — and it’s all done in-place, with no extra memory needed!"
    a "Heap Sort runs in {b}O(n log n){/b} time and is great when memory efficiency matters."
    a "Now let’s test your understanding with a quick quiz!"



    $ chapter_8_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Nice! That was the heap sort demo. Now let’s test your understanding with a quiz."
    jump chapter_8_Heap_Sort_Quiz

init python:
    import random
    chapter_8_Heap_Sort_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_8_Heap_Sort_order)

label chapter_8_Heap_Sort_Quiz:
    #5POINTS
    $ chapter_8_Heap_Sort_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_8_Heap_Sort_order:
        $ current_q = chapter_8_Heap_Sort_order.pop(0)

        if current_q == "q1":
            a "What is the first step in heap sort?"
            menu:                
                "Reverse the array":
                    a "Incorrect! Reversing isn’t part of heap sort."
                "Build a heap from the input array":
                    $ chapter_8_Heap_Sort_quiz += 1
                    a "Correct! You start by building a max-heap or min-heap."
                "Sort the array directly":
                    a "Incorrect! Heap sort begins with heap construction."


        elif current_q == "q2":
            a "Which heap is typically used for sorting in ascending order?"
            menu:
                
                "Min-heap":
                    a "Incorrect! Min-heaps are used for descending order."
                "Binary search tree":
                    a "Incorrect! BSTs aren’t used in heap sort."
                "Max-heap":
                    $ chapter_8_Heap_Sort_quiz += 1
                    a "Correct! Max-heaps allow repeated removal of the largest element."

        elif current_q == "q3":
            a "What happens after removing the root during heap sort?"
            menu:                
                "Rebuild the entire heap":
                    a "Incorrect! Only heapify-down is needed."
                "Place it at the end of the array and heapify-down":
                    $ chapter_8_Heap_Sort_quiz += 1
                    a "Correct! This maintains the heap and builds the sorted array."
                "Delete it permanently":
                    a "Incorrect! The root is stored in the sorted portion."


        elif current_q == "q4":
            a "What is the time complexity of heap sort?"
            menu:                
                "O(n^2)":
                    a "Incorrect! That’s too slow for heap sort."
                "O(n log n)":
                    $ chapter_8_Heap_Sort_quiz += 1
                    a "Correct! Heap sort is efficient and consistent."

                "O(log n)":
                    a "Incorrect! That’s the complexity of individual heap operations."

        elif current_q == "q5":
            a "Why is heap sort considered an in-place algorithm?"
            menu:
                "It uses recursion":
                    a "Incorrect! Recursion doesn’t define in-place behavior."
                "It doesn’t require extra memory beyond the input array":
                    $ chapter_8_Heap_Sort_quiz += 1
                    a "Correct! Heap sort rearranges elements within the array."
                
                "It stores elements in a separate heap":
                    a "Incorrect! The heap is built within the array itself."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_8_Heap_Sort_quiz] out of 5."


    jump chapter_8_restart

label chapter_8_restart:
    $ chapter_8_test = (
        chapter_8_Priority_Queues_quiz +
        chapter_8_Heap_Basics_quiz +
        chapter_8_Array_Representation_quiz +
        chapter_8_Remove_Operation_quiz +
        chapter_8_Heap_Sort_quiz 
    )

    a "Your score is [chapter_8_test]"
    a "Let's see how well you do in the {size=+20}CHAPTER QUIZ"

    if chapter_7_test <= 7:
        show adrian concerned
        jump chapter_8_quiz_easy
    elif chapter_7_test <= 12:
        show adrian neutral
        jump chapter_8_quiz_medium
    else:
        show adrian excited
        jump chapter_8_quiz_hard

label chapter_8_quiz_easy:
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert easy quiz questions here)

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    jump chapter_8_performance

label chapter_8_quiz_medium:
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert medium quiz questions here)

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    jump chapter_8_performance

label chapter_8_quiz_hard:
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert hard quiz questions here)

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    jump chapter_8_performance

label chapter_8_performance:

# Priority Queues
    if chapter_8_Priority_Queues_quiz < 2:
        a "You need to review Priority Queues."
        a "Focus on how they differ from regular queues and their role in scheduling."
    elif chapter_8_Priority_Queues_quiz < 3:
        a "You did okay in Priority Queues, but there's room for improvement."
        a "Revisit how priorities affect insertion and removal."

# Heap Basics
    if chapter_8_Heap_Basics_quiz < 2:
        a "You need to review Heap Basics."
        a "Understand min-heaps vs max-heaps and their structural properties."
    elif chapter_8_Heap_Basics_quiz < 3:
        a "You did okay in Heap Basics, but there's room for improvement."
        a "Try visualizing heap trees and their constraints."

# Array Representation
    if chapter_8_Array_Representation_quiz < 2:
        a "You need to review Array Representation of Heaps."
        a "Focus on parent-child index relationships."
    elif chapter_8_Array_Representation_quiz < 3:
        a "You did okay in Array Representation, but there's room for improvement."
        a "Practice mapping tree nodes to array indices."

# Remove Operation
    if chapter_8_Remove_Operation_quiz < 2:
        a "You need to review the Remove Operation."
        a "Understand how the heap property is restored after removal."
    elif chapter_8_Remove_Operation_quiz < 3:
        a "You did okay in Remove Operation, but there's room for improvement."
        a "Trace the reheapify process step-by-step."

# Heap Sort
    if chapter_8_Heap_Sort_quiz < 2:
        a "You need to review Heap Sort."
        a "Focus on how heaps are used to sort arrays efficiently."
    elif chapter_8_Heap_Sort_quiz < 3:
        a "You did okay in Heap Sort, but there's room for improvement."
        a "Compare heap sort with other sorting algorithms."

    jump chapter_8_end

label chapter_8_end:
    play sound "sfx/success.mp3"
    play music "bgm/city-high-life.mp3" fadein 1.0
    $ persistent.chapter_8 = True
    a "Would You like to test again?"
    menu:
        "Yes":
            jump chapter_8_restart
        "No":
            pass
    show adrian happy
    a "You have finished chapter 8. You can continue to Chapter 9!"
    jump menu