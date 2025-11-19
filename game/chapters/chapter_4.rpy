default chapter_4_progress = 0

default chapter_4_stack_operations_quiz = 0
default chapter_4_stack_recursion_quiz = 0

screen chapter_4_introscreen:
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 60
        ypadding 60
        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5
            text "Chapter 4: Stack & Queues" size 60 color "#FFFFFF" outlines [(5, "#000000", 0, 0)]

screen chapter_4_StackIntro:
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 200
        ypadding 60
        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5
            text "Stack" size 60 color "#FFFFFF" outlines [(5, "#000000", 0, 0)]

screen chapter_4_QueueIntro:
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 200
        ypadding 60
        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5
            text "Queues" size 60 color "#FFFFFF" outlines [(5, "#000000", 0, 0)]

screen StackQueues:
    frame:
        xalign 0.5
        yalign 0.3
        xpadding 100
        ypadding 100

        hbox:
            spacing 80
            xalign 0.5
            yalign 0.5
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5
                text "STACKS" size 60 color "#00ff40" outlines [(5, "#000000", 0, 0)]
                text "How Stack Works" size 40 color "#FFFFFF" outlines [(5, "#000000", 0, 0)]
                text "Application, Properties & Heap Memory" size 40 color "#FFFFFF" outlines [(5, "#000000", 0, 0)]                
                text "Stack and Recursion" size 40 color "#FFFFFF" outlines [(5, "#000000", 0, 0)]
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5
                text "QUEUES" size 60 color "#00ff40" outlines [(5, "#000000", 0, 0)]
                text "How Queue Works" size 40 color "#FFFFFF" outlines [(5, "#000000", 0, 0)]


label chapter_4_intro:
    call hideall from _call_hideall_5 #This is a stupid fix but it works I think
    play audio ("sfx/start.mp3")
    play music "bgm/country.mp3" fadein 1.0

    scene black
    pause 1.0
    show screen chapter_4_introscreen
    pause 2.0
    scene cowboy with dissolve
    pause 1.0
    hide screen chapter_4_introscreen

    with dissolve
        
    show screen menu_btn
            
    show adrian smiling at center:
        smaller 

    if persistent.chapter_4 == True:
        a "Hi welcome back to chapter 4"
        a "are you sure you want to go through this chapter again?"
        menu:
            "Yes":
                a "Pick which You Want to Review"
                menu:
                    "Stacks":
                        menu:
                            "How Stack Works":
                                jump chapter_4_how_stack_works
                            "Stack Application, Properties, & Heap Memory":
                                jump chapter_4_stack_operations
                            "Stack and Recursion":
                                jump chapter_4_stack_and_recursion
                    "Queues":
                        menu:
                            "How Queue Works":
                                jump chapter_4_queues

            "No":
                jump menu
    show screen menu_btn
    a "Howdy Yall"
    a "Welcome to my Ranch"
    a "Well My father's Ranch"
    a "Welcome to chapter 4: {size=+20}{b}Stacks & Queues{/b}"
    a "We will be tackling:"

    show screen StackQueues
    a "Stacks and Queues are fundamental data structures that are used to store and manage collections of elements in a specific order."
    hide screen StackQueues

    a "Shall we Start?"
    menu:
        "Yes":
            jump chapter_4_how_stack_works
        "No":
            show adrian smug
            a "Aight bet your lost"
            $ renpy.quit()

label chapter_4_how_stack_works:
    show screen chapter_4_StackIntro
    with dissolve
    pause 2.0
    hide screen chapter_4_StackIntro
    with dissolve
    show adrian smiling at center:
        smaller

    show adrian happy
    a "Nice to see you again!"
    show adrian explaining
    a "So what is a Stack?"

    screen ch4_Stack_Info:
        frame:
            xalign 0.95
            yalign 0.3
            xpadding 70
            ypadding 100

            vbox:
                spacing 25
                xalign 0.5
                yalign 0.5

                text "STACKS" size 60 color "#00ff40" outlines [(5, "#000000", 0, 0)]

                text "1. Abstract data type with pop(), push(), peek()" size 40 color "#FFFFFF" outlines [(3, "#000000", 0, 0)]
                text "2. LIFO: Last In, First Out" size 40 color "#FFFFFF" outlines [(3, "#000000", 0, 0)]
                text "3. Implemented via arrays or linked lists" size 40 color "#FFFFFF" outlines [(3, "#000000", 0, 0)]
                text "4. Used in stack-oriented languages for basic operations" size 40 color "#FFFFFF" outlines [(3, "#000000", 0, 0)]
    
    show adrian explaining at left
    with move
    show screen ch4_Stack_Info
    a "Howdy, partner! Let me give ya a quick rundown on stacks."

    a "Stacks are like a cowboy's saddlebag , the last thing ya toss in is the first thing ya pull out."

    a "They follow the ol' Last In, First Out rule, or LIFO for short."

    a "You push items onto the stack like stackin' hay bales, and pop 'em off in reverse, just like grabbin' the top one first."


    show adrian smiling at center
    with move
    hide screen ch4_Stack_Info
    with dissolve 
    "Here is an example of how stacks work"
    jump chapter_4_stack_operations


image ch_4_st_1 = Movie(play="images/videos/chapter_4_stackpush.webm", loop=False)
image ch_4_st_2 = Movie(play="images/videos/chapter_4_stackpop.webm", loop=False)
image ch_4_st_3 = Movie(play="images/videos/chapter_4_stackpeek.webm", loop=False)  
label ch_4_push:
    hide screen stack_operations
    window hide
    show ch_4_st_1 at truecenter
    pause 9.0
    hide ch_4_st_1
    window auto
    jump chapter_4_stack_operations

label ch_4_pop:
    hide screen stack_operations
    hide screen menu_btn
    window hide
    show ch_4_st_2 at truecenter
    pause 15.0
    hide ch_4_st_2
    show screen menu_btn
    window auto
    jump chapter_4_stack_operations

label ch_4_peek:
    hide screen stack_operations
    hide screen menu_btn
    window hide
    show ch_4_st_3 at truecenter
    pause 9.0
    hide ch_4_st_3
    show screen menu_btn
    window auto
    jump chapter_4_stack_operations


label chapter_4_stack_operations:
    
    show screen stack_operations
    a "Pick an Operation On how stacks work"

    screen stack_operations:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 100
            ypadding 100

            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                hbox:
                    spacing 80
                    xalign 0.5
                    yalign 0.5

                    text "STACK OPERATIONS =>" size 40 color "#e1ff00" outlines [(5, "#000000", 0, 0)]
                    frame:
                        textbutton "Push()":
                            action Call("ch_4_push")
                            text_size 40
                            text_color "#FFFFFF"
                            text_hover_color "#FFD700"
                    frame:
                        textbutton "Pop()":
                            action Call("ch_4_pop")
                            text_size 40
                            text_color "#FFFFFF"
                            text_hover_color "#FFD700"
                    frame:
                        textbutton "Peek()":
                            action Call("ch_4_peek")
                            text_size 40
                            text_color "#FFFFFF"
                            text_hover_color "#FFD700"


    show adrian smiling
    a "Neet isnt it?"
    hide screen stack_operations
    with dissolve
    show adrian explaining
    a "Stacks are used in various applications, such as function calls, expression evaluation, and backtracking algorithms."
    show adrian normal
    a "Lets try a minigame"

    call stack_minigame from _call_stack_minigame
    
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "You hear that? Its time for some questions. Buckle Up Buckeroo"
    $ chapter_4_progress =+ 1
    jump ch4_stack_operations_quiz

init python:
    import random
    chapter_4_stack_operations_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_4_stack_operations_order)

label ch4_stack_operations_quiz:
    $ chapter_4_stack_operations_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_4_stack_operations_order:
        $ current_q = chapter_4_stack_operations_order.pop(0)

        if current_q == "q1":
            a "What is the main principle of a stack data structure?"
            menu:
                "First In, First Out (FIFO)":
                    a "Incorrect! The correct answer is Last In, First Out (LIFO)."
                "Last In, First Out (LIFO)":
                    $ chapter_4_stack_operations_quiz += 1
                    a "Correct! Stacks follow the LIFO principle."
                "Random Access":
                    a "Incorrect! Stacks do not allow random access to elements."

        elif current_q == "q2":
            show adrian doubt
            a "Which operation is used to add an element to the top of a stack?"
            menu:
                "Pop()":
                    a "Incorrect! Pop() removes the top element from the stack."
                "Peek()":
                    a "Incorrect! Peek() retrieves the top element without removing it."
                "Push()":
                    $ chapter_4_stack_operations_quiz += 1
                    a "Correct! Push() adds an element to the top of the stack."

        elif current_q == "q3":
            show adrian happy
            a "What is the time complexity of the push() and pop() operations in a stack?"
            menu:
                "O(1)":
                    $ chapter_4_stack_operations_quiz += 1
                    a "Correct! Both push() and pop() operations have a time complexity of O(1)."
                "O(n)":
                    a "Incorrect! O(n) is not the correct time complexity for these operations."
                "O(log n)":
                    a "Incorrect! O(log n) is not the correct time complexity for these operations."

        elif current_q == "q4":
            show adrian normal
            a "What are the two main operations of a stack?"
            menu:
                "Enqueue() and Dequeue()":
                    a "Incorrect! Enqueue() and Dequeue() are operations of a queue, not a stack."
                "Push() and Pop()":
                    $ chapter_4_stack_operations_quiz += 1
                    a "Correct! Push() adds an element, and Pop() removes the top element."
                "Insert() and Remove()":
                    a "Incorrect! Insert() and Remove() are not specific to stacks."

        elif current_q == "q5":
            show adrian smug
            a "Which of the following is NOT a valid application of stacks?"
            menu:
                "Function call management":
                    a "Incorrect! Stacks are used for managing function calls."
                "Expression evaluation":
                    a "Incorrect! Stacks are used in expression evaluation."
                "Memory allocation":
                    $ chapter_4_stack_operations_quiz += 1
                    a "Correct! Memory allocation is not a typical application of stacks."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/country.mp3" fadein 1.0
    play sound "sfx/success.mp3"

    a "Congratulations!"
    a "Your current score is [chapter_4_stack_operations_quiz]"
    a "Let's continue"

    jump chapter_4_stack_properties

label chapter_4_stack_properties:
    play music "bgm/country.mp3" fadein 1.0
    show adrian mad
    a "As I was sayin', partner..."

    show adrian smiling

    a "Now let's mosey on to the next roundup: {b}Stack Application & Properties{/b}"

    show adrian explaining

    a "Stacks ain't just for show"
    a "they're mighty useful for wranglin' function calls, sortin' out expressions, and trackin' back through tricky algorithms like a trail scout on a lost path."

    screen ch_4_stack_application:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 60
            ypadding 60
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5
                text "Stack Properties" size 60 color "#00ff40" outlines [(5, "#000000", 0, 0)]

                hbox:
                    spacing 60
                    frame:
                        textbutton "Application":
                            action ShowMenu("ch_4_Application")
                            text_size 40
                            text_color "#FFFFFF"
                            text_hover_color "#FFD700"
                    frame:
                        textbutton "Stack":
                            action ShowMenu("ch_4_Stack")
                            text_size 40
                            text_color "#FFFFFF"
                            text_hover_color "#FFD700"
                    frame:
                        textbutton "Heap Memory":
                            action ShowMenu("ch_4_HeapMemory")
                            text_size 40
                            text_color "#FFFFFF"
                            text_hover_color "#FFD700"
    
    screen ch_4_Application:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 60
            ypadding 60
            vbox:
                spacing 20
                text "{size=+20}{b}Application of Stacks{/b}" size 40 color "#FFFFFF" outlines [(3, "#000000", 0, 0)]
                hbox:
                    spacing 80
                    vbox:
                        spacing 15
                        xalign 0.5
                        yalign 0.5
                        text "{b}Stack-Oriented Languages{/b}" size 32 color "#00FF00" outlines [(2, "#000000", 0, 0)]
                        text "Languages like Forth and PostScript use stacks heavily" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "Operations are performed by pushing and popping values" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "Useful for reverse Polish notation and expression evaluation" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                    vbox:
                        spacing 15
                        xalign 0.5
                        yalign 0.5
                        text "{b}Graph Algorithms{/b}" size 32 color "#00FF00" outlines [(2, "#000000", 0, 0)]
                        text "Depth-first search (DFS) uses stacks or recursion" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "Finding Euler cycles involves stack-based traversal" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "Strongly connected components can be found using Kosaraju’s algorithm" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "Stacks help manage traversal state efficiently" size 28 color "#FFD700" outlines [(2, "#000000", 0, 0)]

                imagebutton:
                    xalign 1.0
                    yalign 0.0
                    xoffset -30
                    yoffset 30
                    auto "UI/btn_back_%s.png"
                    action Return()

    screen ch_4_Stack:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 60
            ypadding 60
            vbox:
                spacing 20
                text "{size=+20}{b}Stack Memory{/b}" size 40 color "#FFFFFF" outlines [(3, "#000000", 0, 0)]
                hbox:
                    spacing 80
                    vbox:
                        spacing 15
                        xalign 0.5
                        yalign 0.5
                        text "{b}Core Concept{/b}" size 32 color "#00FF00" outlines [(2, "#000000", 0, 0)]
                        text "Stack memory is a special region in RAM" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "Used to manage active subroutines/functions" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "Call stack stores return points and temporary variables" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "High-level languages handle it automatically" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                    vbox:
                        spacing 15
                        xalign 0.5
                        yalign 0.5
                        text "{b}Why It's Useful{/b}" size 32 color "#00FF00" outlines [(2, "#000000", 0, 0)]
                        text "Tracks where each function should return" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "Stores local variables during execution" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "Variables are pushed when declared, popped when function exits" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "Local variables are lost after function returns" size 28 color "#FFD700" outlines [(2, "#000000", 0, 0)]
                        text "Stack memory is limited—use wisely!" size 28 color "#FF4500" outlines [(2, "#000000", 0, 0)]

                imagebutton:
                    xalign 1.0
                    yalign 0.0
                    xoffset -30
                    yoffset 30
                    auto "UI/btn_back_%s.png"
                    action Return()

    screen ch_4_HeapMemory:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 60
            ypadding 60
            vbox:
                spacing 20
                text "{size=+20}{b}Heap Memory{/b}" size 40 color "#FFFFFF" outlines [(3, "#000000", 0, 0)]
                hbox:
                    spacing 80
                    vbox:
                        spacing 15
                        xalign 0.5
                        yalign 0.5
                        text "{b}Core Concept{/b}" size 32 color "#00FF00" outlines [(2, "#000000", 0, 0)]
                        text "Heap is a large memory region not managed automatically" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "Used for dynamic memory allocation" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "C: uses malloc() and calloc() with pointers" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "Java: objects and reference types live on the heap" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                    vbox:
                        spacing 15
                        xalign 0.5
                        yalign 0.5
                        text "{b}Challenges{/b}" size 32 color "#00FF00" outlines [(2, "#000000", 0, 0)]
                        text "Manual deallocation is required" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "Failure to free memory leads to memory leaks!" size 28 color "#FF4500" outlines [(2, "#000000", 0, 0)]
                        text "Pointer management makes it slower than stack" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "Garbage collection helps in some languages" size 28 color "#FFD700" outlines [(2, "#000000", 0, 0)]

                imagebutton:
                    xalign 1.0
                    yalign 0.0
                    xoffset -30
                    yoffset 30
                    auto "UI/btn_back_%s.png"
                    action Return()

    show adrian happy
    show screen ch_4_stack_application
    a "These here are the core concepts, partner."

    a "Take yer sweet time lookin' 'em over"
    a "no need to rush like a cattle stampede."
    hide screen ch_4_stack_application

    screen ch_4_StackVsHeap:
        frame:
            xalign 0.9
            yalign 0.3
            xpadding 100
            ypadding 100
            vbox:
                spacing 20
                text "{size=+20}{b}Stack vs Heap Memory{/b}" size 40 color "#FFFFFF" outlines [(3, "#000000", 0, 0)]
                hbox:
                    spacing 80
                    vbox:
                        spacing 15
                        xalign 0.5
                        yalign 0.5
                        text "{b}Stack Memory{/b}" size 32 color "#00FF00" outlines [(2, "#000000", 0, 0)]
                        text "Limited in size" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "Fast access" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "Stores local variables" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "Managed efficiently by CPU" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "Variables cannot be resized" size 28 color "#FF4500" outlines [(2, "#000000", 0, 0)]
                    vbox:
                        spacing 15
                        xalign 0.5
                        yalign 0.5
                        text "{b}Heap Memory{/b}" size 32 color "#00FF00" outlines [(2, "#000000", 0, 0)]
                        text "No size limits" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "Slow access" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "Stores objects and reference types" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "Memory may be fragmented" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "Variables can be resized" size 28 color "#FFD700" outlines [(2, "#000000", 0, 0)]

 

    show adrian normal
    a "so what is the difference between stack memory and heap?"
    show adrian explaining at left
    with move
    show screen ch_4_StackVsHeap
    a "Here"
    show adrian happy
    a "Take time to read through it :3"
    hide screen ch_4_StackVsHeap
    $ chapter_4_progress =+ 1
    jump chapter_4_stack_and_recursion


image ch_4_st_4 = Movie(play="images/videos/chapter_4_recursion.webm", loop=False)
label chapter_4_stack_and_recursion:
    show adrian normal
    a "Let's ride on to the next topic, partner: {b}Stack and Recursion{/b}"

    show adrian explaining at center
    with move

    a "Recursion’s a mighty clever trick — it’s when a function calls itself to {i}solve a problem.{/i}"

    a "And just like stackin’ saddles in the barn, each call gets piled on top of the stack till the job’s done."

    a "Yessir, recursion’s like a trail that loops back on itself — each step builds on the last."

    a "For example..."

    show ch_4_st_4 at truecenter
    window hide
    pause 28.0
    hide ch_4_st_4
    window auto

    show adrian happy
    a "This is how recursion works"
    show adrian smiling
    $ chapter_4_progress =+ 1
    play sound "sfx/bell.mp3"
    a "You hear that? Its time for some questions. Buckle Up Buckeroo"
    jump ch4_stack_recursion_quiz

init python:
    import random
    chapter_4_stack_recursion_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_4_stack_recursion_order)

label ch4_stack_recursion_quiz:
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal
    $ chapter_4_stack_recursion_quiz = 0

    while chapter_4_stack_recursion_order:
        $ current_q = chapter_4_stack_recursion_order.pop(0)

        if current_q == "q1":
            a "What is recursion in programming?"
            menu:
                "A technique where a function calls itself":
                    $ chapter_4_stack_recursion_quiz += 1
                    a "Correct! Recursion involves a function calling itself."
                "A method to optimize memory usage":
                    a "Incorrect! Recursion is not primarily about memory optimization."
                "A way to sort data":
                    a "Incorrect! Recursion can be used in sorting algorithms, but it is not its main purpose."

        elif current_q == "q2":
            show adrian doubt
            a "What is the base case in recursion?"
            menu:
                "The condition that stops the recursion":
                    $ chapter_4_stack_recursion_quiz += 1
                    a "Correct! The base case prevents infinite recursion."
                "The maximum depth of recursion":
                    a "Incorrect! The base case is not about depth."
                "The first recursive call":
                    a "Incorrect! The base case is not the first call."

        elif current_q == "q3":
            show adrian happy
            a "What happens if there is no base case in recursion?"
            menu:
                "The program runs indefinitely":
                    $ chapter_4_stack_recursion_quiz += 1
                    a "Correct! Without a base case, recursion leads to infinite loops."
                "The program terminates immediately":
                    a "Incorrect! The program will not terminate without a base case."
                "The program runs faster":
                    a "Incorrect! Lack of base case does not improve performance."

        elif current_q == "q4":
            show adrian normal
            a "Which of the following is an example of recursion?"
            menu:
                "Calculating factorial using iteration":
                    a "Incorrect! This is an iterative approach, not recursive."
                "Calculating Fibonacci numbers using recursion":
                    $ chapter_4_stack_recursion_quiz += 1
                    a "Correct! Fibonacci can be calculated recursively."
                "Sorting an array using bubble sort":
                    a "Incorrect! Bubble sort is an iterative algorithm."

        elif current_q == "q5":
            show adrian smug
            a "What is the time complexity of a recursive function with a base case?"
            menu:
                "O(1)":
                    a "Incorrect! O(1) is constant time complexity."
                "O(n)":
                    $ chapter_4_stack_recursion_quiz += 1
                    a "Correct! The time complexity depends on the number of recursive calls."
                "O(n^2)":
                    a "Incorrect! O(n^2) is not the correct time complexity for recursion."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/country.mp3" fadein 1.0
    play sound "sfx/success.mp3"

    a "Congratulations!"
    a "Your current score is [chapter_4_stack_recursion_quiz]"
    a "Let's continue"
    jump chapter_4_queues

label chapter_4_queues:
    play music "bgm/country.mp3" fadein 1.0

    show screen chapter_4_QueueIntro
    with dissolve
    pause 2.0
    hide screen chapter_4_QueueIntro
    with dissolve

    show adrian smiling

    a "Now, let's move on to the next topic: {b}Queues{/b}"

    screen ch4_Queue_Info:
        frame:
            xalign 0.95
            yalign 0.3
            xpadding 70
            ypadding 100

            vbox:
                spacing 25
                xalign 0.5
                yalign 0.5

                text "QUEUES" size 60 color "#00ff40" outlines [(5, "#000000", 0, 0)]

                text "1. Abstract data type (interface)" size 40 color "#FFFFFF" outlines [(3, "#000000", 0, 0)]
                text "2. Basic operations: enqueue(), dequeue(), peek()" size 40 color "#FFFFFF" outlines [(3, "#000000", 0, 0)]
                text "3. FIFO: First In, First Out" size 40 color "#FFFFFF" outlines [(3, "#000000", 0, 0)]
                text "4. Implemented via dynamic arrays or linked lists" size 40 color "#FFFFFF" outlines [(3, "#000000", 0, 0)]
                text "5. Crucial for BFS in graph algorithms" size 40 color "#FFFFFF" outlines [(3, "#000000", 0, 0)]

    show adrian explaining at left
    with move
    show screen ch4_Queue_Info
    a "{size=+10}{b}Howdy, partner!{/b}{/size}"
    a "{i}Let me tell ya 'bout queues—one o’ the handiest tools in a coder’s saddlebag.{/i}"

    a "{size=+5}They follow the {b}First In, First Out{/b} rule,{/size}"
    a "Kinda like herdin’ cows through a gate. {i}First cow in’s the first one out.{/i}"

    a "You send them cows into the herd from the back—that’s called {b}enqueuein’{/b}—"
    a "and you let ‘em out the front—that’s {b}dequeuein’{/b}—one hoof at a time."

    a "{color=#DAA520}No cuttin’ in line, no stampedin’.{/color} Just good ol’ order, like a proper cattle drive."

    a "{size=+8}{color=#8B0000}That’s a queue, cowboy. Simple, steady, and always fair.{/color}{/size}"

        
    hide screen ch4_Queue_Info
    with dissolve
    show adrian smiling at center
    with move
    "Queues are used in various applications, such as scheduling tasks and managing resources."
    $ chapter_4_progress =+ 1
    jump chapter_4_queues_vid


image ch4_pingpong = Movie( play="images/videos/pingpong.webm", loop=False)    
default ch4_pingpong = False

label ch4_pingpong:
    $ ch4_pingpong = True
    show adrian mad
    a "WAIT NO DONT TOUCH THAT"
    stop music
    show adrian blush
    hide screen ch_4_queues_vid
    hide screen menu_btn
    window hide
    show ch4_pingpong at truecenter
    pause 5.0
    hide ch4_pingpong
    show screen menu_btn
    window auto
    show adrian blush
    a "I told you not to touch that!"
    a "Ignore that its..."
    show adrian nocomment
    a "I have my needs too you know"
    play music "bgm/country.mp3" fadein 1.0
    jump chapter_4_queues_vid

image ch_4_qu_1 = Movie(play="images/videos/chapter_4_queue.webm", loop=False)
image ch_4_qu_2 = Movie(play="images/videos/chapter_4_dequeue.webm", loop=False)
label ch_4_queue:
    hide screen ch_4_queues_vid
    window hide
    show ch_4_qu_1 at truecenter
    pause 16.0
    hide ch_4_qu_1
    window auto
    jump chapter_4_queues_vid
label ch_4_dequeue:
    hide screen ch_4_queues_vid
    window hide
    show ch_4_qu_2 at truecenter
    pause 16.0
    hide ch_4_qu_2
    window auto
    jump chapter_4_queues_vid

label chapter_4_queues_vid:
    
    show screen ch_4_queues_vid
    show adrian smiling
    a "Just press the button to see how queues work"

    screen ch_4_queues_vid:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 100
            ypadding 100

            hbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "QUEUE OPERATIONS =>" size 40 color "#e1ff00" outlines [(5, "#000000", 0, 0)]
                frame:
                    textbutton "Queue()":
                            action Call("ch_4_queue")
                            text_size 40
                            text_color "#FFFFFF"
                            text_hover_color "#FFD700"
                frame:
                    textbutton "Dequeue()":
                            action Call("ch_4_dequeue")
                            text_size 40
                            text_color "#FFFFFF"
                            text_hover_color "#FFD700"
        frame: 
            xalign 0.0
            yalign 0.9
            textbutton "DO NOT TOUCH":
                action Call("ch4_pingpong")
                text_size 10
                text_color "#FFFFFF"
                text_hover_color "#FFD700"
    
    a "Queues are used in various applications, such as scheduling tasks and managing resources."
    a "Queueing how it works is simple"
    a "You can enqueue elements at the back and dequeue them from the front."
    show adrian happy
    a "Dequeuing is the process of removing an element from the front of the queue."
    hide screen ch_4_queues_vid
    


    show adrian normal 
    stop music fadeout 0.5
    play sound "sfx/bell.mp3"
    $ chapter_4_progress =+ 1
    a "You hear that? Its time for some questions. Buckle Up Buckeroo"

label ch4_restart:
    $ chapter_4_test = chapter_4_stack_operations_quiz + chapter_4_stack_recursion_quiz
    a "Your score is [chapter_4_test]"
    a "Let's see how well you do in the {size=+20}CHAPTER QUIZ"
    if chapter_4_test <= 4:
        show adrian blush
        jump chapter_4_quiz_easy
    elif chapter_4_test <= 7:
        show adrian smiling
        jump chapter_4_quiz_medium
    else:
        show adrian happy
        jump chapter_4_quiz_hard
        
init python:
    import random
    chapter_4_easy_question_order = [
        "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10"
    ]
    random.shuffle(chapter_4_easy_question_order)

label chapter_4_quiz_easy:
    $ chapter_4_score = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0

    show adrian smiling at center
    a "Welcome to the {b}Quiz!{/b} Let's see how much you've learned."

    while chapter_4_easy_question_order:
        $ current_q = chapter_4_easy_question_order.pop(0)

        if current_q == "q1":
            a "What is the main principle of a stack data structure?"
            menu:
                "First In, First Out (FIFO)":
                    a "Incorrect! The correct answer is Last In, First Out (LIFO)."
                "Last In, First Out (LIFO)":
                    $ chapter_4_score += 1
                    a "Correct! Stacks follow the LIFO principle."
                "Random Access":
                    a "Incorrect! Stacks do not allow random access to elements."

        elif current_q == "q2":
            show adrian doubt
            a "Which operation is used to add an element to the top of a stack?"
            menu:
                "Pop()":
                    a "Incorrect! Pop() removes the top element from the stack."
                "Peek()":
                    a "Incorrect! Peek() retrieves the top element without removing it."
                "Push()":
                    $ chapter_4_score += 1
                    a "Correct! Push() adds an element to the top of the stack."

        elif current_q == "q3":
            show adrian happy
            a "What is the time complexity of the push() and pop() operations in a stack?"
            menu:
                "O(1)":
                    $ chapter_4_score += 1
                    a "Correct! Both push() and pop() operations have a time complexity of O(1)."
                "O(n)":
                    a "Incorrect! O(n) is not the correct time complexity for these operations."
                "O(log n)":
                    a "Incorrect! O(log n) is not the correct time complexity for these operations."

        elif current_q == "q4":
            show adrian normal
            a "What are the two main operations of a stack?"
            menu:
                "Enqueue() and Dequeue()":
                    a "Incorrect! Enqueue() and Dequeue() are operations of a queue, not a stack."
                "Push() and Pop()":
                    $ chapter_4_score += 1
                    a "Correct! Push() adds an element, and Pop() removes the top element."
                "Insert() and Remove()":
                    a "Incorrect! Insert() and Remove() are not specific to stacks."

        elif current_q == "q5":
            show adrian smug
            a "Which of the following is NOT a valid application of stacks?"
            menu:
                "Function call management":
                    a "Incorrect! Stacks are used for managing function calls."
                "Expression evaluation":
                    a "Incorrect! Stacks are used in expression evaluation."
                "Memory allocation":
                    $ chapter_4_score += 1
                    a "Correct! Memory allocation is not a typical application of stacks."

        elif current_q == "q6":
            show adrian happy
            a "What is recursion in programming?"
            menu:
                "A technique where a function calls itself":
                    $ chapter_4_score += 1
                    a "Correct! Recursion involves a function calling itself."
                "A method to optimize memory usage":
                    a "Incorrect! Recursion is not primarily about memory optimization."
                "A way to sort data":
                    a "Incorrect! Recursion can be used in sorting algorithms, but it is not its main purpose."

        elif current_q == "q7":
            show adrian doubt
            a "What is the base case in recursion?"
            menu:
                "The condition that stops the recursion":
                    $ chapter_4_score += 1
                    a "Correct! The base case prevents infinite recursion."
                "The maximum depth of recursion":
                    a "Incorrect! The base case is not about depth."
                "The first recursive call":
                    a "Incorrect! The base case is not the first call."

        elif current_q == "q8":
            show adrian happy
            a "What happens if there is no base case in recursion?"
            menu:
                "The program runs indefinitely":
                    $ chapter_4_score += 1
                    a "Correct! Without a base case, recursion leads to infinite loops."
                "The program terminates immediately":
                    a "Incorrect! The program will not terminate without a base case."
                "The program runs faster":
                    a "Incorrect! Lack of base case does not improve performance."

        elif current_q == "q9":
            show adrian normal
            a "Which of the following is an example of recursion?"
            menu:
                "Calculating factorial using iteration":
                    a "Incorrect! This is an iterative approach, not recursive."
                "Calculating Fibonacci numbers using recursion":
                    $ chapter_4_score += 1
                    a "Correct! Fibonacci can be calculated recursively."
                "Sorting an array using bubble sort":
                    a "Incorrect! Bubble sort is an iterative algorithm."

        elif current_q == "q10":
            show adrian smug
            a "What is the time complexity of a recursive function with a base case?"
            menu:
                "O(1)":
                    a "Incorrect! O(1) is constant time complexity."
                "O(n)":
                    $ chapter_4_score += 1
                    a "Correct! The time complexity depends on the number of recursive calls."
                "O(n^2)":
                    a "Incorrect! O(n^2) is not the correct time complexity for recursion."

    stop music fadeout 0.5
    play music "bgm/country.mp3" fadein 1.0
    play sound "sfx/success.mp3"
    a "Your quiz score is: [chapter_4_score]"

    jump chapter_4_review

init python:
    import random
    chapter_4_medium_question_order = [
        "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10"
    ]
    random.shuffle(chapter_4_medium_question_order)

label chapter_4_quiz_medium:
    $ chapter_4_score = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0

    show adrian smiling at center
    a "Welcome to the {b}Quiz!{/b} Let's see how much you've learned."

    while chapter_4_medium_question_order:
        $ current_q = chapter_4_medium_question_order.pop(0)

        if current_q == "q1":
            a "What is the main principle of a stack data structure?"
            menu:
                "First In, First Out (FIFO)":
                    a "Incorrect! The correct answer is Last In, First Out (LIFO)."
                "Last In, First Out (LIFO)":
                    $ chapter_4_score += 1
                    a "Correct! Stacks follow the LIFO principle."
                "Random Access":
                    a "Incorrect! Stacks do not allow random access to elements."

        elif current_q == "q2":
            show adrian doubt
            a "Which operation is used to add an element to the top of a stack?"
            menu:
                "Pop()":
                    a "Incorrect! Pop() removes the top element from the stack."
                "Peek()":
                    a "Incorrect! Peek() retrieves the top element without removing it."
                "Push()":
                    $ chapter_4_score += 1
                    a "Correct! Push() adds an element to the top of the stack."

        elif current_q == "q3":
            show adrian happy
            a "What is the time complexity of the push() and pop() operations in a stack?"
            menu:
                "O(1)":
                    $ chapter_4_score += 1
                    a "Correct! Both push() and pop() operations have a time complexity of O(1)."
                "O(n)":
                    a "Incorrect! O(n) is not the correct time complexity for these operations."
                "O(log n)":
                    a "Incorrect! O(log n) is not the correct time complexity for these operations."

        elif current_q == "q4":
            show adrian normal
            a "What are the two main operations of a stack?"
            menu:
                "Enqueue() and Dequeue()":
                    a "Incorrect! Enqueue() and Dequeue() are operations of a queue, not a stack."
                "Push() and Pop()":
                    $ chapter_4_score += 1
                    a "Correct! Push() adds an element, and Pop() removes the top element."
                "Insert() and Remove()":
                    a "Incorrect! Insert() and Remove() are not specific to stacks."

        elif current_q == "q5":
            show adrian smug
            a "Which of the following is NOT a valid application of stacks?"
            menu:
                "Function call management":
                    a "Incorrect! Stacks are used for managing function calls."
                "Expression evaluation":
                    a "Incorrect! Stacks are used in expression evaluation."
                "Memory allocation":
                    $ chapter_4_score += 1
                    a "Correct! Memory allocation is not a typical application of stacks."

        elif current_q == "q6":
            show adrian happy
            a "What is recursion in programming?"
            menu:
                "A technique where a function calls itself":
                    $ chapter_4_score += 1
                    a "Correct! Recursion involves a function calling itself."
                "A method to optimize memory usage":
                    a "Incorrect! Recursion is not primarily about memory optimization."
                "A way to sort data":
                    a "Incorrect! Recursion can be used in sorting algorithms, but it is not its main purpose."

        elif current_q == "q7":
            show adrian doubt
            a "What is the base case in recursion?"
            menu:
                "The condition that stops the recursion":
                    $ chapter_4_score += 1
                    a "Correct! The base case prevents infinite recursion."
                "The maximum depth of recursion":
                    a "Incorrect! The base case is not about depth."
                "The first recursive call":
                    a "Incorrect! The base case is not the first call."

        elif current_q == "q8":
            show adrian happy
            a "What happens if there is no base case in recursion?"
            menu:
                "The program runs indefinitely":
                    $ chapter_4_score += 1
                    a "Correct! Without a base case, recursion leads to infinite loops."
                "The program terminates immediately":
                    a "Incorrect! The program will not terminate without a base case."
                "The program runs faster":
                    a "Incorrect! Lack of base case does not improve performance."

        elif current_q == "q9":
            show adrian normal
            a "Which of the following is an example of recursion?"
            menu:
                "Calculating factorial using iteration":
                    a "Incorrect! This is an iterative approach, not recursive."
                "Calculating Fibonacci numbers using recursion":
                    $ chapter_4_score += 1
                    a "Correct! Fibonacci can be calculated recursively."
                "Sorting an array using bubble sort":
                    a "Incorrect! Bubble sort is an iterative algorithm."

        elif current_q == "q10":
            show adrian smug
            a "What is the time complexity of a recursive function with a base case?"
            menu:
                "O(1)":
                    a "Incorrect! O(1) is constant time complexity."
                "O(n)":
                    $ chapter_4_score += 1
                    a "Correct! The time complexity depends on the number of recursive calls."
                "O(n^2)":
                    a "Incorrect! O(n^2) is not the correct time complexity for recursion."

    screen queue_quiz1:
        frame:
            xalign 0.2
            yalign 0.3
            xpadding 30
            ypadding 30
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Queue Representation" size 40

                hbox:
                    spacing 20
                    vbox:
                        spacing 5
                        text "Front →" size 25 color "#FFD700"
                        text "Task A" size 30 color "#00FF00"
                        text "Task B" size 30 color "#00FF00"
                        text "Task C" size 30 color "#00FF00"
                        text "Task D" size 30 color "#00FF00"
                        text "← Rear" size 25 color "#FFD700"

        frame:
            xalign 0.7
            yalign 0.3
            xpadding 30
            ypadding 30

            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Pick Your Answer" size 40

                hbox:
                    spacing 20
                    vbox:
                        textbutton "Task A" action [SetVariable("ch3_selected_queue1", "Task A"), Return()]
                        textbutton "Task B" action [SetVariable("ch3_selected_queue1", "Task B"), Return()]
                        textbutton "Task C" action [SetVariable("ch3_selected_queue1", "Task C"), Return()]
                        textbutton "Task D" action [SetVariable("ch3_selected_queue1", "Task D"), Return()]

    show screen queue_quiz1
    a "Which task will be processed first in this queue?"
    hide screen queue_quiz1

    if ch3_selected_queue1 is None:
        a "Please select an answer."
        return

    elif ch3_selected_queue1 == "Task A":
        $ chapter_4_score += 1
        a "Correct! Task A is at the front of the queue."
        pass
    else:
        a "Oops! That's not the first task in line."
        pass
    

    screen queue_quiz2:
        frame:
            xalign 0.2
            yalign 0.3
            xpadding 30
            ypadding 30
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Queue Representation" size 40

                hbox:
                    spacing 20
                    vbox:
                        spacing 5
                        text "Front →" size 25 color "#FFD700"
                        text "Task Alpha" size 30 color "#00FF00"
                        text "Task Beta" size 30 color "#00FF00"
                        text "Task Gamma" size 30 color "#00FF00"
                        text "Task Delta" size 30 color "#00FF00"
                        text "← Rear" size 25 color "#FFD700"

        frame:
            xalign 0.7
            yalign 0.3
            xpadding 30
            ypadding 30

            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Pick Your Answer" size 40

                hbox:
                    spacing 20
                    vbox:
                        textbutton "Task Alpha" action [SetVariable("ch4_selected_queue2", "Task Alpha"), Return()]
                        textbutton "Task Beta" action [SetVariable("ch4_selected_queue2", "Task Beta"), Return()]
                        textbutton "Task Gamma" action [SetVariable("ch4_selected_queue2", "Task Gamma"), Return()]
                        textbutton "Task Delta" action [SetVariable("ch4_selected_queue2", "Task Delta"), Return()]

    show screen queue_quiz2
    a "Which task will be processed last in this queue?"
    hide screen queue_quiz2

    if ch4_selected_queue2 is None:
        a "Please select an answer."
        return

    elif ch4_selected_queue2 == "Task Delta":
        $ chapter_4_score += 1
        a "Correct! Task Delta is at the rear of the queue."
        pass
    else:
        a "Oops! That's not the last task in line."
        pass
        
    screen queue_quiz3:
        frame:
            xalign 0.2
            yalign 0.3
            xpadding 30
            ypadding 30
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Queue After One Dequeue" size 40

                hbox:
                    spacing 20
                    vbox:
                        spacing 5
                        text "Front →" size 25 color "#FFD700"
                        text "Task Beta" size 30 color "#00FF00"
                        text "Task Gamma" size 30 color "#00FF00"
                        text "Task Delta" size 30 color "#00FF00"
                        text "← Rear" size 25 color "#FFD700"

        frame:
            xalign 0.7
            yalign 0.3
            xpadding 30
            ypadding 30

            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Which task was removed?" size 40

                hbox:
                    spacing 20
                    vbox:
                        textbutton "Task Alpha" action [SetVariable("ch4_selected_queue3", "Task Alpha"), Return()]
                        textbutton "Task Beta" action [SetVariable("ch4_selected_queue3", "Task Beta"), Return()]
                        textbutton "Task Gamma" action [SetVariable("ch4_selected_queue3", "Task Gamma"), Return()]
                        textbutton "Task Delta" action [SetVariable("ch4_selected_queue3", "Task Delta"), Return()]

    show screen queue_quiz3
    a "One task was dequeued from the front. Which one was it?"
    hide screen queue_quiz3

    if ch4_selected_queue3 is None:
        a "Please select an answer."
        return

    elif ch4_selected_queue3 == "Task Alpha":
        $ chapter_4_score += 1
        a "Correct! Task Alpha was at the front and got removed first."
        pass
    else:
        a "Not quite! Remember, queues remove from the front."
        pass

    screen queue_quiz4:
        frame:
            xalign 0.2
            yalign 0.3
            xpadding 30
            ypadding 30
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Queue After Two Dequeues" size 40

                hbox:
                    spacing 20
                    vbox:
                        spacing 5
                        text "Front →" size 25 color "#FFD700"
                        text "Task Gamma" size 30 color "#00FF00"
                        text "Task Delta" size 30 color "#00FF00"
                        text "← Rear" size 25 color "#FFD700"

        frame:
            xalign 0.7
            yalign 0.3
            xpadding 30
            ypadding 30

            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Which task was removed second?" size 40

                hbox:
                    spacing 20
                    vbox:
                        textbutton "Task Alpha" action [SetVariable("ch4_selected_queue4", "Task Alpha"), Return()]
                        textbutton "Task Beta" action [SetVariable("ch4_selected_queue4", "Task Beta"), Return()]
                        textbutton "Task Gamma" action [SetVariable("ch4_selected_queue4", "Task Gamma"), Return()]
                        textbutton "Task Delta" action [SetVariable("ch4_selected_queue4", "Task Delta"), Return()]

    show screen queue_quiz4
    a "Another task was dequeued. Which one was removed second?"
    hide screen queue_quiz4

    if ch4_selected_queue4 is None:
        a "Please select an answer."
        return

    elif ch4_selected_queue4 == "Task Beta":
        $ chapter_4_score += 1
        a "Correct! Task Beta was next in line and got removed."
        pass
    else:
        a "Not quite! The second dequeue removes the next front task."
        pass

    screen queue_quiz5:
        frame:
            xalign 0.2
            yalign 0.3
            xpadding 30
            ypadding 30
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Queue After One Dequeue" size 40

                hbox:
                    spacing 20
                    vbox:
                        spacing 5
                        text "Front →" size 25 color "#FFD700"
                        text "Compile Code" size 30 color "#00FF00"
                        text "Run Tests" size 30 color "#00FF00"
                        text "Deploy App" size 30 color "#00FF00"
                        text "← Rear" size 25 color "#FFD700"

        frame:
            xalign 0.7
            yalign 0.3
            xpadding 30
            ypadding 30

            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Which task was removed?" size 40

                hbox:
                    spacing 20
                    vbox:
                        textbutton "Upload File" action [SetVariable("ch4_selected_queue5", "Upload File"), Return()]
                        textbutton "Compile Code" action [SetVariable("ch4_selected_queue5", "Compile Code"), Return()]
                        textbutton "Run Tests" action [SetVariable("ch4_selected_queue5", "Run Tests"), Return()]
                        textbutton "Deploy App" action [SetVariable("ch4_selected_queue5", "Deploy App"), Return()]

    show screen queue_quiz5
    a "One task was dequeued from the front. Which one was it?"
    hide screen queue_quiz5

    if ch4_selected_queue5 is None:
        a "Please select an answer."
        return

    elif ch4_selected_queue5 == "Upload File":
        $ chapter_4_score += 1
        a "Correct! 'Upload File' was at the front and got removed first."
        pass
    else:
        a "Not quite! Remember, queues remove from the front—FIFO style."
        pass


    show adrian happy
    play music "bgm/country.mp3" fadein 1.0
    play sound "sfx/success.mp3"
    a "Your quiz score is: [chapter_4_score]"
    jump chapter_4_review
    
init python:
    import random
    chapter_4_hard_question_order = [
        "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10"
    ]
    random.shuffle(chapter_4_hard_question_order)

label chapter_4_quiz_hard:
    $ chapter_4_score = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0

    show adrian smiling at center
    a "Welcome to the {b}Quiz!{/b} Let's see how much you've learned."

    while chapter_4_hard_question_order:
        $ current_q = chapter_4_hard_question_order.pop(0)

        if current_q == "q1":
            a "What is the main principle of a stack data structure?"
            menu:
                "First In, First Out (FIFO)":
                    a "Incorrect! The correct answer is Last In, First Out (LIFO)."
                "Last In, First Out (LIFO)":
                    $ chapter_4_score += 1
                    a "Correct! Stacks follow the LIFO principle."
                "Random Access":
                    a "Incorrect! Stacks do not allow random access to elements."

        elif current_q == "q2":
            show adrian doubt
            a "Which operation is used to add an element to the top of a stack?"
            menu:
                "Pop()":
                    a "Incorrect! Pop() removes the top element from the stack."
                "Peek()":
                    a "Incorrect! Peek() retrieves the top element without removing it."
                "Push()":
                    $ chapter_4_score += 1
                    a "Correct! Push() adds an element to the top of the stack."

        elif current_q == "q3":
            show adrian happy
            a "What is the time complexity of the push() and pop() operations in a stack?"
            menu:
                "O(1)":
                    $ chapter_4_score += 1
                    a "Correct! Both push() and pop() operations have a time complexity of O(1)."
                "O(n)":
                    a "Incorrect! O(n) is not the correct time complexity for these operations."
                "O(log n)":
                    a "Incorrect! O(log n) is not the correct time complexity for these operations."

        elif current_q == "q4":
            show adrian normal
            a "What are the two main operations of a stack?"
            menu:
                "Enqueue() and Dequeue()":
                    a "Incorrect! Enqueue() and Dequeue() are operations of a queue, not a stack."
                "Push() and Pop()":
                    $ chapter_4_score += 1
                    a "Correct! Push() adds an element, and Pop() removes the top element."
                "Insert() and Remove()":
                    a "Incorrect! Insert() and Remove() are not specific to stacks."

        elif current_q == "q5":
            show adrian smug
            a "Which of the following is NOT a valid application of stacks?"
            menu:
                "Function call management":
                    a "Incorrect! Stacks are used for managing function calls."
                "Expression evaluation":
                    a "Incorrect! Stacks are used in expression evaluation."
                "Memory allocation":
                    $ chapter_4_score += 1
                    a "Correct! Memory allocation is not a typical application of stacks."

        elif current_q == "q6":
            show adrian happy
            a "What is recursion in programming?"
            menu:
                "A technique where a function calls itself":
                    $ chapter_4_score += 1
                    a "Correct! Recursion involves a function calling itself."
                "A method to optimize memory usage":
                    a "Incorrect! Recursion is not primarily about memory optimization."
                "A way to sort data":
                    a "Incorrect! Recursion can be used in sorting algorithms, but it is not its main purpose."

        elif current_q == "q7":
            show adrian doubt
            a "What is the base case in recursion?"
            menu:
                "The condition that stops the recursion":
                    $ chapter_4_score += 1
                    a "Correct! The base case prevents infinite recursion."
                "The maximum depth of recursion":
                    a "Incorrect! The base case is not about depth."
                "The first recursive call":
                    a "Incorrect! The base case is not the first call."

        elif current_q == "q8":
            show adrian happy
            a "What happens if there is no base case in recursion?"
            menu:
                "The program runs indefinitely":
                    $ chapter_4_score += 1
                    a "Correct! Without a base case, recursion leads to infinite loops."
                "The program terminates immediately":
                    a "Incorrect! The program will not terminate without a base case."
                "The program runs faster":
                    a "Incorrect! Lack of base case does not improve performance."

        elif current_q == "q9":
            show adrian normal
            a "Which of the following is an example of recursion?"
            menu:
                "Calculating factorial using iteration":
                    a "Incorrect! This is an iterative approach, not recursive."
                "Calculating Fibonacci numbers using recursion":
                    $ chapter_4_score += 1
                    a "Correct! Fibonacci can be calculated recursively."
                "Sorting an array using bubble sort":
                    a "Incorrect! Bubble sort is an iterative algorithm."

        elif current_q == "q10":
            show adrian smug
            a "What is the time complexity of a recursive function with a base case?"
            menu:
                "O(1)":
                    a "Incorrect! O(1) is constant time complexity."
                "O(n)":
                    $ chapter_4_score += 1
                    a "Correct! The time complexity depends on the number of recursive calls."
                "O(n^2)":
                    a "Incorrect! O(n^2) is not the correct time complexity for recursion."
    screen queue_quiz1:
        frame:
            xalign 0.2
            yalign 0.3
            xpadding 30
            ypadding 30
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Queue Representation" size 40

                hbox:
                    spacing 20
                    vbox:
                        spacing 5
                        text "Front →" size 25 color "#FFD700"
                        text "Task A" size 30 color "#00FF00"
                        text "Task B" size 30 color "#00FF00"
                        text "Task C" size 30 color "#00FF00"
                        text "Task D" size 30 color "#00FF00"
                        text "← Rear" size 25 color "#FFD700"

        frame:
            xalign 0.7
            yalign 0.3
            xpadding 30
            ypadding 30

            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Pick Your Answer" size 40

                hbox:
                    spacing 20
                    vbox:
                        textbutton "Task A" action [SetVariable("ch3_selected_queue1", "Task A"), Return()]
                        textbutton "Task B" action [SetVariable("ch3_selected_queue1", "Task B"), Return()]
                        textbutton "Task C" action [SetVariable("ch3_selected_queue1", "Task C"), Return()]
                        textbutton "Task D" action [SetVariable("ch3_selected_queue1", "Task D"), Return()]

    show screen queue_quiz1
    a "Which task will be processed first in this queue?"
    hide screen queue_quiz1

    if ch3_selected_queue1 is None:
        a "Please select an answer."
        return

    elif ch3_selected_queue1 == "Task A":
        $ chapter_4_score += 1
        a "Correct! Task A is at the front of the queue."
        pass
    else:
        a "Oops! That's not the first task in line."
        pass
    

    screen queue_quiz2:
        frame:
            xalign 0.2
            yalign 0.3
            xpadding 30
            ypadding 30
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Queue Representation" size 40

                hbox:
                    spacing 20
                    vbox:
                        spacing 5
                        text "Front →" size 25 color "#FFD700"
                        text "Task Alpha" size 30 color "#00FF00"
                        text "Task Beta" size 30 color "#00FF00"
                        text "Task Gamma" size 30 color "#00FF00"
                        text "Task Delta" size 30 color "#00FF00"
                        text "← Rear" size 25 color "#FFD700"

        frame:
            xalign 0.7
            yalign 0.3
            xpadding 30
            ypadding 30

            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Pick Your Answer" size 40

                hbox:
                    spacing 20
                    vbox:
                        textbutton "Task Alpha" action [SetVariable("ch4_selected_queue2", "Task Alpha"), Return()]
                        textbutton "Task Beta" action [SetVariable("ch4_selected_queue2", "Task Beta"), Return()]
                        textbutton "Task Gamma" action [SetVariable("ch4_selected_queue2", "Task Gamma"), Return()]
                        textbutton "Task Delta" action [SetVariable("ch4_selected_queue2", "Task Delta"), Return()]

    show screen queue_quiz2
    a "Which task will be processed last in this queue?"
    hide screen queue_quiz2

    if ch4_selected_queue2 is None:
        a "Please select an answer."
        return

    elif ch4_selected_queue2 == "Task Delta":
        $ chapter_4_score += 1
        a "Correct! Task Delta is at the rear of the queue."
        pass
    else:
        a "Oops! That's not the last task in line."
        pass
        
    screen queue_quiz3:
        frame:
            xalign 0.2
            yalign 0.3
            xpadding 30
            ypadding 30
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Queue After One Dequeue" size 40

                hbox:
                    spacing 20
                    vbox:
                        spacing 5
                        text "Front →" size 25 color "#FFD700"
                        text "Task Beta" size 30 color "#00FF00"
                        text "Task Gamma" size 30 color "#00FF00"
                        text "Task Delta" size 30 color "#00FF00"
                        text "← Rear" size 25 color "#FFD700"

        frame:
            xalign 0.7
            yalign 0.3
            xpadding 30
            ypadding 30

            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Which task was removed?" size 40

                hbox:
                    spacing 20
                    vbox:
                        textbutton "Task Alpha" action [SetVariable("ch4_selected_queue3", "Task Alpha"), Return()]
                        textbutton "Task Beta" action [SetVariable("ch4_selected_queue3", "Task Beta"), Return()]
                        textbutton "Task Gamma" action [SetVariable("ch4_selected_queue3", "Task Gamma"), Return()]
                        textbutton "Task Delta" action [SetVariable("ch4_selected_queue3", "Task Delta"), Return()]

    show screen queue_quiz3
    a "One task was dequeued from the front. Which one was it?"
    hide screen queue_quiz3

    if ch4_selected_queue3 is None:
        a "Please select an answer."
        return

    elif ch4_selected_queue3 == "Task Alpha":
        $ chapter_4_score += 1
        a "Correct! Task Alpha was at the front and got removed first."
        pass
    else:
        a "Not quite! Remember, queues remove from the front."
        pass

    screen queue_quiz4:
        frame:
            xalign 0.2
            yalign 0.3
            xpadding 30
            ypadding 30
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Queue After Two Dequeues" size 40

                hbox:
                    spacing 20
                    vbox:
                        spacing 5
                        text "Front →" size 25 color "#FFD700"
                        text "Task Gamma" size 30 color "#00FF00"
                        text "Task Delta" size 30 color "#00FF00"
                        text "← Rear" size 25 color "#FFD700"

        frame:
            xalign 0.7
            yalign 0.3
            xpadding 30
            ypadding 30

            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Which task was removed second?" size 40

                hbox:
                    spacing 20
                    vbox:
                        textbutton "Task Alpha" action [SetVariable("ch4_selected_queue4", "Task Alpha"), Return()]
                        textbutton "Task Beta" action [SetVariable("ch4_selected_queue4", "Task Beta"), Return()]
                        textbutton "Task Gamma" action [SetVariable("ch4_selected_queue4", "Task Gamma"), Return()]
                        textbutton "Task Delta" action [SetVariable("ch4_selected_queue4", "Task Delta"), Return()]

    show screen queue_quiz4
    a "Another task was dequeued. Which one was removed second?"
    hide screen queue_quiz4

    if ch4_selected_queue4 is None:
        a "Please select an answer."
        return

    elif ch4_selected_queue4 == "Task Beta":
        $ chapter_4_score += 1
        a "Correct! Task Beta was next in line and got removed."
        pass
    else:
        a "Not quite! The second dequeue removes the next front task."
        pass

    screen queue_quiz5:
        frame:
            xalign 0.2
            yalign 0.3
            xpadding 30
            ypadding 30
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Queue After One Dequeue" size 40

                hbox:
                    spacing 20
                    vbox:
                        spacing 5
                        text "Front →" size 25 color "#FFD700"
                        text "Compile Code" size 30 color "#00FF00"
                        text "Run Tests" size 30 color "#00FF00"
                        text "Deploy App" size 30 color "#00FF00"
                        text "← Rear" size 25 color "#FFD700"

        frame:
            xalign 0.7
            yalign 0.3
            xpadding 30
            ypadding 30

            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Which task was removed?" size 40

                hbox:
                    spacing 20
                    vbox:
                        textbutton "Upload File" action [SetVariable("ch4_selected_queue5", "Upload File"), Return()]
                        textbutton "Compile Code" action [SetVariable("ch4_selected_queue5", "Compile Code"), Return()]
                        textbutton "Run Tests" action [SetVariable("ch4_selected_queue5", "Run Tests"), Return()]
                        textbutton "Deploy App" action [SetVariable("ch4_selected_queue5", "Deploy App"), Return()]

    show screen queue_quiz5
    a "One task was dequeued from the front. Which one was it?"
    hide screen queue_quiz5

    if ch4_selected_queue5 is None:
        a "Please select an answer."
        return

    elif ch4_selected_queue5 == "Upload File":
        $ chapter_4_score += 1
        a "Correct! 'Upload File' was at the front and got removed first."
        pass
    else:
        a "Not quite! Remember, queues remove from the front—FIFO style."
        pass

    screen queue_quiz6:
        frame:
            xalign 0.5
            yalign 0.2
            xpadding 40
            ypadding 40
            vbox:
                spacing 20
                xalign 0.5

                text "Circular Queue State" size 40

                hbox:
                    spacing 10
                    for task in ["", "Task X", "Task Y", "Task Z", "", "Task W"]:
                        vbox:
                            spacing 5
                            frame:
                                xsize 120
                                ysize 80
                                background "#333333"
                                text task size 25 color "#00FFCC" xalign 0.5 yalign 0.5
                            if task == "Task X":
                                text "Front" size 20 color "#FFD700" xalign 0.5
                            elif task == "Task W":
                                text "Rear" size 20 color "#FFD700" xalign 0.5

        frame:
            xalign 0.5
            yalign 0.65
            xpadding 40
            ypadding 40

            vbox:
                spacing 20
                xalign 0.5

                text "Which task was dequeued earlier?" size 40

                hbox:
                    spacing 20
                    vbox:
                        textbutton "Task A" action [SetVariable("ch4_selected_queue6", "Task A"), Return()]
                        textbutton "Task B" action [SetVariable("ch4_selected_queue6", "Task B"), Return()]
                        textbutton "Task V" action [SetVariable("ch4_selected_queue6", "Task V"), Return()]
                        textbutton "Task Q" action [SetVariable("ch4_selected_queue6", "Task Q"), Return()]

    show screen queue_quiz6
    a "This circular queue has wrapped around. Based on the final state, which task was removed earlier?"
    hide screen queue_quiz6

    if ch4_selected_queue6 is None:
        a "Please select an answer."
        return

    elif ch4_selected_queue6 == "Task Q":
        $ chapter_4_score += 1
        a "Correct! Task Q was dequeued before the wraparound occurred."
        pass
    else:
        a "Not quite! Think about how circular queues reuse space and how the front pointer moves."
        pass

    screen queue_quiz7:
        frame:
            xalign 0.5
            yalign 0.2
            xpadding 40
            ypadding 40
            vbox:
                spacing 20
                xalign 0.5

                text "Priority Queue After One Dequeue" size 40

                hbox:
                    spacing 15
                    for task, color, size in [("Feature Update", "#00FF00", 25),
                                            ("Critical Bug Fix", "#FF0000", 35),
                                            ("UI Polish", "#00CED1", 25),
                                            ("Code Refactor", "#FFA500", 30)]:
                        vbox:
                            spacing 5
                            frame:
                                xsize 160
                                ysize 100
                                background "#222222"
                                text task size size color color xalign 0.5 yalign 0.5

        frame:
            xalign 0.5
            yalign 0.65
            xpadding 40
            ypadding 40

            vbox:
                spacing 20
                xalign 0.5

                text "Which task was removed first?" size 40

                hbox:
                    spacing 20
                    vbox:
                        textbutton "Feature Update" action [SetVariable("ch4_selected_queue7", "Feature Update"), Return()]
                        textbutton "Critical Bug Fix" action [SetVariable("ch4_selected_queue7", "Critical Bug Fix"), Return()]
                        textbutton "UI Polish" action [SetVariable("ch4_selected_queue7", "UI Polish"), Return()]
                        textbutton "Code Refactor" action [SetVariable("ch4_selected_queue7", "Code Refactor"), Return()]

    show screen queue_quiz7
    a "This queue prioritizes urgency. Which task was dequeued first?"
    hide screen queue_quiz7

    if ch4_selected_queue7 is None:
        a "Please select an answer."
        return

    elif ch4_selected_queue7 == "Critical Bug Fix":
        $ chapter_4_score += 1
        a "Correct! Priority queues remove the most urgent task first."
        pass
    else:
        a "Not quite! In a priority queue, urgency beats arrival order."
        pass

    screen stack_quiz1:
        frame:
            xalign 0.3
            yalign 0.3
            xpadding 30
            ypadding 30
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Stack After One Pop" size 40

                vbox:
                    spacing 10
                    for item in ["Login Screen", "Settings Panel", "Inventory UI"]:
                        frame:
                            xsize 300
                            ysize 60
                            background "#444444"
                            text item size 30 color "#00FFCC" xalign 0.5 yalign 0.5
                    text "← Top" size 25 color "#FFD700" xalign 0.5

        frame:
            xalign 0.7
            yalign 0.3
            xpadding 30
            ypadding 30

            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Which UI element was popped?" size 40

                hbox:
                    spacing 20
                    vbox:
                        textbutton "Login Screen" action [SetVariable("ch4_selected_stack1", "Login Screen"), Return()]
                        textbutton "Settings Panel" action [SetVariable("ch4_selected_stack1", "Settings Panel"), Return()]
                        textbutton "Inventory UI" action [SetVariable("ch4_selected_stack1", "Inventory UI"), Return()]
                        textbutton "Main Menu" action [SetVariable("ch4_selected_stack1", "Main Menu"), Return()]

    show screen stack_quiz1
    a "One UI element was popped from the top of the stack. Which one was it?"
    hide screen stack_quiz1

    if ch4_selected_stack1 is None:
        a "Please select an answer."
        return

    elif ch4_selected_stack1 == "Main Menu":
        $ chapter_4_score += 1
        a "Correct! 'Main Menu' was the last pushed and the first popped."
        pass
    else:
        a "Not quite! Stacks remove the most recently added item—LIFO style."
        pass

    screen stack_quiz2:
        frame:
            xalign 0.3
            yalign 0.3
            xpadding 30
            ypadding 30
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Call Stack After One Return" size 40

                vbox:
                    spacing 10
                    for func in ["main()", "loadAssets()", "initializeGame()"]:
                        frame:
                            xsize 320
                            ysize 60
                            background "#333333"
                            text func size 30 color "#00FF99" xalign 0.5 yalign 0.5
                    text "← Top" size 25 color "#FFD700" xalign 0.5

        frame:
            xalign 0.7
            yalign 0.3
            xpadding 30
            ypadding 30

            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Which function just returned?" size 40

                hbox:
                    spacing 20
                    vbox:
                        textbutton "main()" action [SetVariable("ch4_selected_stack2", "main()"), Return()]
                        textbutton "loadAssets()" action [SetVariable("ch4_selected_stack2", "loadAssets()"), Return()]
                        textbutton "initializeGame()" action [SetVariable("ch4_selected_stack2", "initializeGame()"), Return()]
                        textbutton "setupUI()" action [SetVariable("ch4_selected_stack2", "setupUI()"), Return()]

    show screen stack_quiz2
    a "One function just returned and was popped off the stack. Which one was it?"
    hide screen stack_quiz2

    if ch4_selected_stack2 is None:
        a "Please select an answer."
        return

    elif ch4_selected_stack2 == "setupUI()":
        $ chapter_4_score += 1
        a "Correct! 'setupUI()' was the last called and returned first."
        pass
    else:
        a "Not quite! The top of the stack holds the most recent function call."
    pass

    screen stack_quiz3:
        frame:
            xalign 0.3
            yalign 0.3
            xpadding 30
            ypadding 30
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Browser History After One 'Back'" size 40

                vbox:
                    spacing 10
                    for page in ["Home Page", "Search Results", "Product Details"]:
                        frame:
                            xsize 320
                            ysize 60
                            background "#2E2E2E"
                            text page size 30 color "#87CEFA" xalign 0.5 yalign 0.5
                    text "← Top" size 25 color "#FFD700" xalign 0.5

        frame:
            xalign 0.7
            yalign 0.3
            xpadding 30
            ypadding 30

            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Which page was popped?" size 40

                hbox:
                    spacing 20
                    vbox:
                        textbutton "Home Page" action [SetVariable("ch4_selected_stack3", "Home Page"), Return()]
                        textbutton "Search Results" action [SetVariable("ch4_selected_stack3", "Search Results"), Return()]
                        textbutton "Product Details" action [SetVariable("ch4_selected_stack3", "Product Details"), Return()]
                        textbutton "Checkout" action [SetVariable("ch4_selected_stack3", "Checkout"), Return()]

    show screen stack_quiz3
    a "You clicked 'Back' once. Which page was removed from the top of the history stack?"
    hide screen stack_quiz3

    if ch4_selected_stack3 is None:
        a "Please select an answer."
        return

    elif ch4_selected_stack3 == "Checkout":
        $ chapter_4_score += 1
        a "Correct! 'Checkout' was the last visited and got popped when you hit back."
        pass
    else:
        a "Not quite! The browser history stack removes the most recent page first."
        pass



    show adrian happy
    play music "bgm/country.mp3" fadein 1.0
    play sound "sfx/success.mp3"
    a "Your quiz score is: [chapter_4_score]"
    jump chapter_4_review
    
label chapter_4_review:
    # Stack Operations
    if chapter_4_stack_operations_quiz < 2:
        a "You need to review the Stack Operations section."
        a "Focus on how elements are pushed, popped, and how the stack behaves in different scenarios."
    elif chapter_4_stack_operations_quiz < 4:
        a "You did okay in the Stack Operations section, but there's room for improvement."
        a "Revisiting the core stack functions could help reinforce your understanding."

    # Stack Recursion
    if chapter_4_stack_recursion_quiz < 2:
        a "You need to review the Stack Recursion section."
        a "Pay attention to how recursive calls use the call stack and how base cases are handled."
    elif chapter_4_stack_recursion_quiz < 4:
        a "You did okay in the Stack Recursion section, but there's room for improvement."
        a "Reviewing recursion flow and stack frames could help clarify the concept."

    jump chapter_4_ending
label chapter_4_ending:
    play sound "sfx/success.mp3"
    play music "bgm/country.mp3" fadein 1.0
    $ persistent.chapter_4 = True
    a "Would You like to test again?"
    menu:
        "Yes":
            jump ch4_restart
        "No":
            pass
    show adrian happy
    a "You have finished chapter 4. You can continue to Chapter 5!"
    jump menu
       

    


        

