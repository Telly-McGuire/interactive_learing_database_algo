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
                text "Application" size 40 color "#FFFFFF" outlines [(5, "#000000", 0, 0)]                
                text "Stack Properties & Heap Memory" size 40 color "#FFFFFF" outlines [(5, "#000000", 0, 0)]
                text "Stack and Recursion" size 40 color "#FFFFFF" outlines [(5, "#000000", 0, 0)]
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5
                text "QUEUES" size 60 color "#00ff40" outlines [(5, "#000000", 0, 0)]
                text "How Queue Works" size 40 color "#FFFFFF" outlines [(5, "#000000", 0, 0)]
                text "Queue Operation" size 40 color "#FFFFFF" outlines [(5, "#000000", 0, 0)]
                text "Queue Application" size 40 color "#FFFFFF" outlines [(5, "#000000", 0, 0)]


label chapter_4_intro:
    play audio ("sfx/start.mp3")
    play music "bgm/city-high-life.mp3" fadein 1.0

    scene black
    pause 1.0
    show screen chapter_4_introscreen
    pause 2.0
    scene mt tree with dissolve
    pause 1.0
    hide screen chapter_4_introscreen

    with dissolve
    
            
    show adrian smiling at center:
        smaller 

    show screen menu_btn
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
    a "Here is a brief information about stacks"
    a "Stacks are abstract data types that follow the Last In, First Out (LIFO) principle."
    a "They allow you to push elements onto the stack and pop them off in reverse order."
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

                    textbutton "Push()":
                        action Call("ch_4_push")
                        text_size 40
                        text_color "#FFFFFF"
                        text_hover_color "#FFD700"

                    textbutton "Pop()":
                        action Call("ch_4_pop")
                        text_size 40
                        text_color "#FFFFFF"
                        text_hover_color "#FFD700"

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
    a "Now, let's move on to the next topic: Stack Applic-"
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "You hear that? Its time for some questions. Buckle Up Buckeroo"
    jump ch4_quiz1

label ch4_quiz1:
    $ chapter_4_test = 0
    show adrian normal
    a "What is the main principle of a stack data structure?"
    menu:
        "First In, First Out (FIFO)":

            a "Incorrect! The correct answer is Last In, First Out (LIFO)."
        "Last In, First Out (LIFO)":
            $ chapter_4_test += 1
            a "Correct! Stacks follow the LIFO principle."
        "Random Access":
            a "Incorrect! Stacks do not allow random access to elements."
    
    show adrian doubt
    a "Next question!"
    a "Which operation is used to add an element to the top of a stack?"
    menu:
        "Pop()":
            a "Incorrect! Pop() removes the top element from the stack."
        "Peek()":
            a "Incorrect! Peek() retrieves the top element without removing it."
        "Push()":
            $ chapter_4_test += 1
            a "Correct! Push() adds an element to the top of the stack."
    
    show adrian happy
    a "Next question!"
    a "What is the time complexity of the push() and pop() operations in a stack?"
    menu:
        "O(1)":
            $ chapter_4_test += 1
            a "Correct! Both push() and pop() operations have a time complexity of O(1)."
        "O(n)":
            a "Incorrect! O(n) is not the correct time complexity for these operations."
        "O(log n)":
            a "Incorrect! O(log n) is not the correct time complexity for these operations."
    
    show adrian normal
    a "Next question!"
    a "what are the two main operations of a stack?"
    menu:
        
        "Enqueue() and Dequeue()":
            a "Incorrect! Enqueue() and Dequeue() are operations of a queue, not a stack."
        "Push() and Pop()":
            $ chapter_4_test += 1
            a "Correct! Push() adds an element, and Pop() removes the top element."
        "Insert() and Remove()":
            a "Incorrect! Insert() and Remove() are not specific to stacks."
        
    show adrian smug
    a "Next Question"
    a "Which of the following is NOT a valid application of stacks?"
    menu:
        "Function call management":
            a "Incorrect! Stacks are used for managing function calls."
        "Expression evaluation":
            a "Incorrect! Stacks are used in expression evaluation."
        "Memory allocation":
            $ chapter_4_test += 1
            a "Correct! Memory allocation is not a typical application of stacks."
    show adrian happy
    a "Congratulations!"
    a "Your current score is [chapter_4_test]"
    a "Lets continue"

    jump chapter_4_stack_application

label chapter_4_stack_application:
    show adrian mad
    a "As I was saying"
    show adrian smiling
    a "Now, let's move on to the next topic: Stack Application & Properties"
    show adrian explaining
    a "Stacks have various applications, including function call management, expression evaluation, and backtracking algorithms."
    

