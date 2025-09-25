

default chapter_1_Data_Structures_quiz = 0
default chapter_1_Characteristics_quiz = 0
default chapter_1_Algorithms_quiz = 0
default chapter_1_Good_Programming_quiz = 0

default chapter_1_progress = 0
label ch1_scoreadd:
    $ chapter_1_score += 1
    return
screen chapter_1_introscreen:
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 60
        ypadding 60
        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5
            text "Chapter 1: Abstract Data Structures" size 60 color "#FFFFFF" outlines [(5, "#000000", 0, 0)]


label chapter_1_intro:
    call hideall
    play sound "sfx/start.mp3"
    stop music fadeout 1.0
    
    scene black
    pause 1.0
    show screen chapter_1_introscreen
    pause 2.0
    scene mt tree with dissolve
    pause 1.0
    hide screen chapter_1_introscreen
    
    play music "bgm/city-high-life.mp3" fadein 1.0
    show adrian smiling at center:
        smaller
    with dissolve
    
    if persistent.chapter_1 == True:
        a "Hey Welcome back to Chapter 1"
        a "What do you want to do again?"
        menu:
            "Start from the beginning":
                jump chapter_1_Data_Structures
            "Take the Quizzes":
                jump chapter_1_Data_Structures_Quiz
            
            "Would you like to review the chapter?":
                menu:
                    "Yes":
                        "Please Pick a topic to review:"
                        menu:
                            "Data Structures":
                                jump chapter_1_Data_Structures
                            "Characteristics of Algorithms":
                                jump chapter_1_Characteristics
                            "Good Programming":
                                jump chapter_1_Algorithms
                    "No":
                        return
    else:
        pass
    show screen menu_btn
    a "Welcome to Chapter 1"
    a "Today, we’re diving into something that forms the backbone of computer science:"
    a "{size=+30}Data Structures and Algorithms."
    a "These are the building blocks of efficient programming, and mastering them can make all the difference in how we handle large amounts of data"
    
    show adrian explaining:
        smaller

    a "In this chapter, we will cover the basi abstract datastructures"
    
    show adrian normal:
        smaller

    show adrian smiling:
        smaller
    a "Let's get started with the first topic."
    a "But before we do that, look at this this"

    window hide dissolve
    stop music
    play sound "sfx/slideleft.mp3"
    show adrian smiling at left with move:
        smaller
    pause(1.5)

    play sound "sfx/slideright.mp3"
    show adrian smiling at right with move:
        smaller
    pause(1.5)

    play sound "sfx/crisscross.mp3"
    show adrian at left with move
    pause (0.2)
    show adrian at right with move
    pause (0.2)

    show adrian at left with move
    pause (0.2)
    show adrian at right with move
    pause (0.2)

    pause(1.0)
    
    play sound "sfx/chacha.mp3"
    show adrian normal at center:
        xzoom -1
    with move
    pause 0.3
    show adrian smiling at center:
        xzoom 1
    pause 0.3
    show adrian normal at center:
        xzoom -1
    pause 0.3
    show adrian smiling at center:
        xzoom 1
    pause 0.3
    show adrian normal at center:
        xzoom -1
    pause 0.3
    show adrian smiling at center:
        xzoom 1
    pause 0.3
    show adrian normal at center:
        xzoom -1
    pause 0.3
    show adrian smiling at center:
        xzoom 1
    pause 0.3
    show adrian normal at center:
        xzoom -1
    pause 0.3
    show adrian smiling at center:
        xzoom 1
    pause 0.3

    pause 2.0   

    window show dissolve
    window auto

    show adrian explaining at left: 
        smaller
    with move

    transform right_centered:
        zoom 1.5
        xalign 0.8   # Aligns to the left
        yalign 0.2

    play music "bgm/city-high-life.mp3" fadein 1.0
    show adrian smiling     
    a "Now I have your attention, let’s talk about data structures and algorithms."
    a "{b}Data Structures{/b} : They are ways to organize and store data in a computer so that it can be used efficiently."
    a "Think of them as containers that hold data in a specific format, making it easier to access and manipulate."
    a "There are three common problems that data structures help us solve: {b}data search, processer speed, multiple requests{/b}"

    # Add more content for Chapter 1 here...

    jump chapter_1_Data_Structures

#data search 
label chapter_1_Data_Structures:
    show adrian explaining at center:
        smaller

    a "Now, let’s talk about {b} Data Search Algorithms. {/b}"

    show adrian at left
    with move

    show maglass at Position(xpos=0.7, ypos=0.8) with dissolve
    pause 0.5

    a "These algorithms help us find specific data within a larger dataset quickly and efficiently."
    
    show adrian normal:
        smaller

    #add visual 
    show maglass at Position(xpos=0.9, ypos=0.7) with move
    pause 0.5
    a "{size=+10}Data search{/size} : is the process of retrieving relevant information from a dataset, 
    database, or the web using methods like keyword search, pattern matching, and ranking algorithms."
    
    show maglass at Position(xpos=0.5, ypos=0.5) with move
    pause 0.5
    show adrian smiling:
        smaller
    a "Efficient search techniques, such as binary search or hash-based lookup, enhance speed and accuracy in locating data."
    show maglass at Position(xpos=0.2, ypos=0.7) with move
    pause 0.5

    hide maglass 
    with dissolve
    #add visual
    show adrian normal
    show clock at Position(xpos=0.7,ypos=0.8) with dissolve
    a "Next, we have {b}Processor Speed{/b}."
    a "{size=+10}Processor speed{/size} : although being very high, falls limited if the data grows to billion records."
    a "In such cases, we need to optimize our algorithms and data structures to ensure that our programs run efficiently."

    hide clock with dissolve

    image mail = "assets/mail.png"
    image mail2 = "assets/mail.png"
    image mail3 = "assets/mail.png"
    image mail4 = "assets/mail.png"
    image mail5 = "assets/mail.png"
    image mail6 = "assets/mail.png"
    image mail7 = "assets/mail.png"
    image mail8 = "assets/mail.png"
    image mail9 = "assets/mail.png"

    play sound "sfx/paper.mp3"
    show mail at Move((0.7, -0.3), (0.7, 0.4), 3.0)
    show mail2 at Move((0.2, -0.3), (0.2, 0.3), 4.0)
    show mail3 at Move((0.5, -0.3), (0.5, 0.5), 2.0)

    show adrian explaining:
        smaller
    a "Last is {b}Multiple Requests.{/b}"

    play sound "sfx/paper.mp3"
    show mail4 at Move((0.3, -0.3), (0.3, 0.6), 2.5)
    show mail5 at Move((0.8, -0.3), (0.8, 0.3), 3.8)
    show mail6 at Move((0.6, -0.3), (0.6, 0.25), 2.2)
    a "When multiple requests are made to access or modify data simultaneously, it can lead to bottlenecks and inefficiencies."
    
    play sound "sfx/paper.mp3"
    show mail7 at Move((0.1, -0.3), (0.1, 0.4), 2.7)
    show mail8 at Move((0.4, -0.3), (0.4, 0.5), 4.5)
    show mail9 at Move((0.9, -0.3), (0.9, 0.3), 2.3)
    a "Data structures like queues and stacks help manage these requests effectively, 
    ensuring that data is processed in the right order and without conflicts."

    hide mail with dissolve
    hide mail2 with dissolve
    hide mail3 with dissolve
    hide mail4 with dissolve
    hide mail5 with dissolve
    hide mail6 with dissolve
    hide mail7 with dissolve
    hide mail8 with dissolve
    hide mail9 with dissolve

    show adrian normal at center:
        smaller
    with move
    a "There are 3 Characteristics of data structures that we need to consider when choosing the right one for our needs."

    screen ch1_data_structure_characteristics_select:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 60
            ypadding 60
            hbox:
                spacing 30
                xalign 0.5
                yalign 0.5
                text "{size=+5}{b}Characteristics of Data Structures{/b}" color "#00FF40" outlines [(4, "#000000", 0, 0)]
                textbutton "Time Complexity" action Show("ch1_time_complexity")
                textbutton "Space Complexity" action Show("ch1_space_complexity")
                textbutton "Correctness" action Show("ch1_correctness")
                textbutton "Close" action Return()

    screen ch1_time_complexity:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 60
            ypadding 60
            vbox:
                spacing 15
                xalign 0.5
                yalign 0.5
                text "{b}Time Complexity{/b}" size 32 color "#00FF00" outlines [(2, "#000000", 0, 0)]
                text "Measures how long an algorithm takes as input size grows" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "Choose structures that minimize time for large datasets" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "Hash tables: jump straight to data using a unique code" size 28 color "#FFD700" outlines [(2, "#000000", 0, 0)]
                textbutton "Back" action Hide("ch1_time_complexity")

    screen ch1_space_complexity:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 60
            ypadding 60
            vbox:
                spacing 15
                xalign 0.5
                yalign 0.5
                text "{b}Space Complexity{/b}" size 32 color "#00FF00" outlines [(2, "#000000", 0, 0)]
                text "Measures memory used as input size grows" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "Important for limited memory or large datasets" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "Linked lists use less memory than arrays, but slower access" size 28 color "#FFD700" outlines [(2, "#000000", 0, 0)]
                textbutton "Back" action Hide("ch1_space_complexity")

    screen ch1_correctness:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 60
            ypadding 60
            vbox:
                spacing 15
                xalign 0.5
                yalign 0.5
                text "{b}Correctness{/b}" size 32 color "#00FF00" outlines [(2, "#000000", 0, 0)]
                text "Accuracy and reliability of algorithm results" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "Right structure ensures correct outcomes" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "Binary search tree: smart guessing game for sorted data" size 28 color "#FFD700" outlines [(2, "#000000", 0, 0)]
                textbutton "Back" action Hide("ch1_correctness")
    
    call screen ch1_data_structure_characteristics_select
    a "Please look over these"
    hide screen ch1_data_structure_characteristics_select
    play sound "sfx/bell.mp3"
    show adrian smiling
    a "You hear that? Its time for some questions. Buckle Up Buckeroo"
    $ chapter_1_progress += 1

    jump chapter_1_Data_Structures_Quiz

init python:
    import random

    chapter_1_DS_question_order = [
        "q1", "q2", "q3", "q4","q5"
    ]
    random.shuffle(chapter_1_DS_question_order)

label chapter_1_Data_Structures_Quiz:

    play music "bgm/better-answer.mp3" fadein 0.5

    show adrian smiling at center:
        smaller

    
    a "Now that we’ve covered the basics, let’s see how well you understand these concepts."
    a "I have a few questions for you to test your knowledge."
    a "Don’t worry, it’s all part of the learning process, and I’m here to help you along the way."
    a "Here’s your first question:"

    while chapter_1_DS_question_order:    
        $ chapter_1_Data_Structures_quiz = 0
        $ current_ds_q = chapter_1_DS_question_order.pop(0)
        if current_ds_q == "q1":
            a "What is the primary purpose of data structures in programming?"
            menu:
                "To organize and store data efficiently":
                    a "Correct! Data structures are essential for organizing and storing data efficiently."
                    $ chapter_1_Data_Structures_quiz += 1
                "To write code faster":
                    a "Incorrect. While data structures can help with code efficiency, their primary purpose is to organize and store data."
                "To create user interfaces":
                    a "Incorrect. Data structures are not primarily used for creating user interfaces."
            a "Next question:"

        elif current_ds_q == "q2":
            a "Which of the following is NOT a characteristic of data structures?"
            menu:
                "Time Complexity":
                    a "Incorrect. Time complexity is a characteristic of data structures."
                "Space Complexity":
                    a "Incorrect. Space complexity is a characteristic of data structures."
                "User Interface Design":
                    a "Correct! User interface design is not a characteristic of data structures."
                    $ chapter_1_Data_Structures_quiz += 1
            a "Next question:"

        elif current_ds_q == "q3":
            a "What is the difference between a stack and a queue?"
            menu:
                "A stack is LIFO (Last In First Out) and a queue is FIFO (First In First Out)":
                    a "Correct! A stack is LIFO and a queue is FIFO."
                    a "Omg You remembered! Good job!"
                    $ chapter_1_Data_Structures_quiz += 1
                "A stack is FIFO and a queue is LIFO":
                    a "Incorrect. A stack is LIFO and a queue is FIFO."
                "There is no difference":
                    a "Incorrect. There is a difference between a stack and a queue."
            a "Next question:"

        elif current_ds_q == "q4":
            a "What is the primary purpose of search algorithms?"
            menu:
                "To find specific data within a larger dataset quickly and efficiently":
                    a "Correct! Search algorithms are designed to find specific data quickly and efficiently."
                    $ chapter_1_Data_Structures_quiz += 1
                "To sort data in a specific order":
                    a "Incorrect. Sorting algorithms are used for arranging data, not searching for it."
                "To delete data from a dataset":
                    a "Incorrect. Deletion algorithms are used for removing data, not searching for it."
        elif current_ds_q == "q5":
            a "Which data structure uses key-value pairs for storing data?"
            menu:
                "Dictionary":
                    a "Correct! Dictionaries store data as key-value pairs, allowing fast access via keys."
                    $ chapter_1_Data_Structures_quiz += 1
                "List":
                    a "Incorrect. Lists store data in ordered sequences, not key-value pairs."
                "Stack":
                    a "Incorrect. Stacks use LIFO ordering, not key-value pairs."
            a "Next question:"
                        
    a "Quiz complete!"
    a "You got [chapter_1_Data_Structures_quiz] out of 5 questions correct."


    stop music fadeout 1.0
   
    play music "bgm/city-high-life.mp3" fadein 0.5        
    play sound "sfx/success.mp3"
    a "Great job! You've completed the quiz."
    if persistent.chapter_1 == True:
        a "Would you like to continue to the next quiz?"
        menu:
            "Yes":
                jump chapter_1_Characteristics_Quiz
            "No":
                pass

#Charactericistican of Algorithms
label chapter_1_Characteristics:

    show adrian explaining at center:
        smaller
    a "Now, let’s dive deeper into the characteristics of data structures."
    show screen ch1_algorithm_categories

    screen ch1_algorithm_categories:
        frame:
            xalign 0.5
            yalign 0.3
            xpadding 60
            ypadding 100
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5
                text "{size=+10}{b}Important Categories of Algorithms{/b}" color "#00FF40" outlines [(4, "#000000", 0, 0)]
                text "{b}1. Search Algorithms:{/b} Find specific data quickly." color "#FFFFFF" size 32 outlines [(2, "#000000", 0, 0)]
                text "{b}2. Sorting Algorithms:{/b} Arrange data in order." color "#FFD700" size 32 outlines [(2, "#000000", 0, 0)]
                text "{b}3. Insertion Algorithms:{/b} Add new data, keep structure." color "#00BFFF" size 32 outlines [(2, "#000000", 0, 0)]
                text "{b}4. Updating Algorithms:{/b} Modify existing data." color "#FF69B4" size 32 outlines [(2, "#000000", 0, 0)]
                text "{b}5. Deletion Algorithms:{/b} Remove data, keep things organized." color "#FF6347" size 32 outlines [(2, "#000000", 0, 0)]
                text "These are the most common algorithms you'll encounter in this chapter." color "#FFFFFF" size 28 outlines [(2, "#000000", 0, 0)]
                textbutton "Close" action Hide("ch1_algorithm_categories")
    a "Here are some important categories of algorithms to know:"

    hide screen ch1_algorithm_categories

    a "There are many more algorithms, but these are the most common ones that we will encounter in this chapter."
    a "Now, let’s take a closer look at some of these algorithms and how they work."
    show adrian smiling
    a "But First, What do you think of algorithms?"
    menu:
        "Theyre kinda cute":
            show adrian blush
            a "Haha, I guess you could say that! Algorithms can be cute in their own way, especially when they solve problems efficiently."
            show adrian smug
            a "Do you think I am cute too?"
        "Theyre boring":
            show adrian normal
            a "I understand, algorithms can seem boring at first, but they are essential for solving complex problems in programming."
        "Theyre hot":
            show adrian smug
            a "Haha, I guess you could say that! Algorithms can be hot when they solve problems efficiently and elegantly."
    
    show adrian explaining at center
    a "Now let's continue to algorithms."
    a "{b}Algorithms{/b} are step-by-step procedures for solving problems or performing tasks."
    a "They are {b}essential{/b} for processing data efficiently and effectively."
    a "Every single procedure that a computer performs is an algorithm."
    a "An algorithm states the actions to be executed and the order in which these actions are to be executed."
    screen algorithm_cases_screen():
        
        
        frame:
            
            xalign 0.5
            yalign 0.3
            xpadding 60
            ypadding 60
            vbox:
                spacing 15
                xalign 0.5
                yalign 0.5

                text "{b}Algorithm Cases{/b}" size 32 color "#00FF00" outlines [(2, "#000000", 0, 0)]

                text "There are 3 Cases for algorithms.\nWhat are cases you ask? Think of cases like different ways something can happen. Imagine you're playing a guessing game." size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]

                text "Well, there are 3 cases for algorithms: {b}Best Case, Average Case, and Worst Case.{/b}" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]

                text "{b}1. Best Case:{/b} This is the scenario where the algorithm performs the least amount of work, resulting in the fastest execution time." size 26 color "#FFD700" outlines [(2, "#000000", 0, 0)]

                text "{b}2. Average Case:{/b} This is the scenario where the algorithm performs a moderate amount of work, resulting in an average execution time." size 26 color "#00BFFF" outlines [(2, "#000000", 0, 0)]

                text "{b}3. Worst Case:{/b} This is the scenario where the algorithm performs the most amount of work, resulting in the slowest execution time." size 26 color "#FF4500" outlines [(2, "#000000", 0, 0)]
        add "assets/neko.png" xpos 0.008 ypos 0.45

    
    show screen algorithm_cases_screen
    a "Please look over these"
    show adrian smug
    a "It's like when you're going to the bathroom, sometimes you get there quickly, sometimes you have to wait in line, and sometimes you have to wait for a long time because someone is taking forever."
    a "Excuse the screen covering me btw :3"
    show adrian smiling
    a "Algorithms are like that too, they can be fast, slow, or somewhere in between depending on the situation."
    hide screen algorithm_cases_screen
    a "Speaking of algorithms, do you have a type?"

    show adrian blush
    a "I like {size=+10}{b}{i}{color=#FF0000}p{/color}{color=#FF7F00}e{/color}{color=#FFFF00}o{/color}{color=#00FF00}p{/color}{color=#0000FF}l{/color}{color=#8B00FF}e{/color}{/i}{/b}{/size} teehee. What about you?"
    menu:
        "I like boys":
            a "Ooooh, very mucho interesting. My friend is a dude, maybe you two can meet up."
        "I like girls":
            a "I like girls too, Teehee. They're so pretty and cute."
        "I prefer not to say":
            a "That's okay, you don't have to say. It's your personal preference and I respect that."

    show adrian normal
    a "So you ask me why the random question about types?"
    a "Well, just like how we have different types of people, there are also different types of algorithms."
    a "And different types have different characteristics and performance."
    a "And there are certain characteristics before we call something an algorithm."

    screen algo_prop_1:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 60
            ypadding 60
            vbox:
                spacing 20
                text "{b}1. Unambiguous{/b}" size 32 color "#FFD700"
                text "An algorithm must be clear and unambiguous. Each step should be precisely defined and easy to understand." size 26
                text "It's like ordering food: 'I want a cheeseburger with no pickles and extra cheese.'" size 24
    
                imagebutton:
                    xalign 1.0
                    yalign 0.0
                    xoffset -30
                    yoffset 30
                    auto "UI/btn_back_%s.png"
                    action Return()
    screen algo_prop_2:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 60
            ypadding 60
            vbox:
                spacing 20
                text "{b}2. Input{/b}" size 32 color "#00BFFF"
                text "An algorithm should have zero or more inputs—the data it will process." size 26
                text "Like giving your order to the restaurant." size 24

                imagebutton:
                    xalign 1.0
                    yalign 0.0
                    xoffset -30
                    yoffset 30
                    auto "UI/btn_back_%s.png"
                    action Return()
    screen algo_prop_3:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 60
            ypadding 60
            vbox:
                spacing 20
                text "{b}3. Output{/b}" size 32 color "#00FF00"
                text "An algorithm should produce one or more outputs—the result of processing." size 26
                text "Like receiving your burger exactly how you ordered it." size 24

                imagebutton:
                    xalign 1.0
                    yalign 0.0
                    xoffset -30
                    yoffset 30
                    auto "UI/btn_back_%s.png"
                    action Return()
    screen algo_prop_4:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 60
            ypadding 60
            vbox:
                spacing 20
                text "{b}4. Finiteness{/b}" size 32 color "#FF4500"
                text "An algorithm must terminate after a finite number of steps." size 26
                text "Like waiting for your food—it eventually arrives." size 24

                imagebutton:
                    xalign 1.0
                    yalign 0.0
                    xoffset -30
                    yoffset 30
                    auto "UI/btn_back_%s.png"
                    action Return()
    screen algo_prop_5:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 60
            ypadding 60
            vbox:
                spacing 20
                text "{b}5. Effectiveness{/b}" size 32 color "#FF69B4"
                text "An algorithm should solve the problem in a reasonable amount of time." size 26
                text "Your burger should be perfect and arrive on time." size 24

                imagebutton:
                    xalign 1.0
                    yalign 0.0
                    xoffset -30
                    yoffset 30
                    auto "UI/btn_back_%s.png"
                    action Return()
    screen algo_prop_6:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 60
            ypadding 60
            vbox:
                spacing 20
                text "{b}6. Feasibility{/b}" size 32 color "#FFFFFF"
                text "An algorithm should be implementable with available resources." size 26
                text "Your burger should always be available on the menu." size 24

                imagebutton:
                    xalign 1.0
                    yalign 0.0
                    xoffset -30
                    yoffset 30
                    auto "UI/btn_back_%s.png"
                    action Return()
    screen algo_prop_7:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 60
            ypadding 60
            vbox:
                spacing 20
                text "{b}7. Independent{/b}" size 32 color "#8A2BE2"
                text "An algorithm should be independent of any programming language or platform." size 26
                text "Your burger should be exactly what you ordered—no surprise sides." size 24

                imagebutton:
                    xalign 1.0
                    yalign 0.0
                    xoffset -30
                    yoffset 30
                    auto "UI/btn_back_%s.png"
                    action Return()
    screen algo_prop_menu:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 60
            ypadding 60
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5
                text "Algorithm Properties" size 60 color "#00ff40" outlines [(5, "#000000", 0, 0)]

                hbox:
                    spacing 40

                    textbutton "Unambiguous":
                        action ShowMenu("algo_prop_1")
                        text_size 40
                        text_color "#FFFFFF"
                        text_hover_color "#FFD700"

                    textbutton "Input":
                        action ShowMenu("algo_prop_2")
                        text_size 40
                        text_color "#FFFFFF"
                        text_hover_color "#FFD700"

                    textbutton "Output":
                        action ShowMenu("algo_prop_3")
                        text_size 40
                        text_color "#FFFFFF"
                        text_hover_color "#FFD700"

                hbox:
                    spacing 40

                    textbutton "Finiteness":
                        action ShowMenu("algo_prop_4")
                        text_size 40
                        text_color "#FFFFFF"
                        text_hover_color "#FFD700"

                    textbutton "Effectiveness":
                        action ShowMenu("algo_prop_5")
                        text_size 40
                        text_color "#FFFFFF"
                        text_hover_color "#FFD700"

                    textbutton "Feasibility":
                        action ShowMenu("algo_prop_6")
                        text_size 40
                        text_color "#FFFFFF"
                        text_hover_color "#FFD700"

                    textbutton "Independent":
                        action ShowMenu("algo_prop_7")
                        text_size 40
                        text_color "#FFFFFF"
                        text_hover_color "#FFD700"
                        
    a "Here are the key properties that define a good algorithm:"   
    a "Please look over these"
    show screen algo_prop_menu
    a "Click on each property to learn more about it."
    a "{size=+20}CLICK IT"
    hide screen algo_prop_menu
    a "Alright, now that you know the characteristics of algorithms, it's time for a quiz!"

    play sound "sfx/bell.mp3"
    a "You hear that? Its time for some questions. Buckle Up Buckeroo"
    $ chapter_1_progress += 1

    jump chapter_1_Characteristics_Quiz

init python:
    import random

    chapter_1_Characteristics_question_order = [
        "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8"
    ]
    random.shuffle(chapter_1_Characteristics_question_order)
    chapter_1_Characteristics_question_order = chapter_1_Characteristics_question_order[:5]

label chapter_1_Characteristics_Quiz:

    $ chapter_1_Characteristics_quiz = 0

    play music "bgm/better-answer.mp3" fadein 0.5

    show adrian smiling at center:
        smaller

    a "Now that we’ve covered the basics, let’s test your understanding of algorithm characteristics."
    a "I’ll ask you a few questions—just answer honestly and we’ll learn together."
    a "Here’s your first question:"

    while chapter_1_Characteristics_question_order:
        $ current_char_q = chapter_1_Characteristics_question_order.pop(0)

        if current_char_q == "q1":
            a "Which of the following is NOT a common category of algorithms?"
            menu:
                "Searching":
                    show adrian sad
                    a "Incorrect. Searching is a common category of algorithms."
                "Sorting":
                    show adrian sad
                    a "Incorrect. Sorting is a common category of algorithms."
                "Extracting":
                    show adrian happy
                    a "Correct! Extracting is not typically listed as a common category of algorithms."
                    $ chapter_1_Characteristics_quiz += 1
                "Deletion":
                    show adrian sad
                    a "Incorrect. Deletion is a common category of algorithms."

        elif current_char_q == "q2":
            a "Which of the following is NOT a characteristic of a good algorithm?"
            menu:
                "Unambiguous":
                    show adrian sad
                    a "Incorrect. Unambiguous is a key characteristic of a good algorithm."
                "Infinite steps":
                    show adrian happy
                    a "Correct! A good algorithm must always terminate after a finite number of steps."
                    $ chapter_1_Characteristics_quiz += 1
                "Effective":
                    show adrian sad
                    a "Incorrect. Effectiveness is a key characteristic of a good algorithm."
                "Feasible":
                    show adrian sad
                    a "Incorrect. Feasibility is a key characteristic of a good algorithm."

        elif current_char_q == "q3":
            a "True or False: Insertion algorithms add new data while maintaining the dataset’s structure."
            menu:
                "True":
                    show adrian happy
                    a "You are Correct. Good JOB!!"
                    $ chapter_1_Characteristics_quiz += 1
                "False":
                    show adrian sad
                    a "Incorrect. Of course you add new data, you insert something."

        elif current_char_q == "q4":
            a "A ____ algorithm modifies existing data in a dataset to reflect updates correctly."
            $ chapter_1_fillin = renpy.input("Fill in the blank").strip()
            if chapter_1_fillin.lower() == "updating":
                show adrian happy
                a "You are Correct. Good Job!!"
                $ chapter_1_Characteristics_quiz += 1
            else:
                show adrian sad
                a "Sorry, wrong answer."

        elif current_char_q == "q5":
            a "Which of the following best describes the 'Worst Case' scenario for an algorithm?"
            menu:
                "The scenario where the algorithm performs the most amount of work and takes the longest time":
                    show adrian happy
                    a "Correct! The worst case is when the algorithm takes the most time to complete."
                    $ chapter_1_Characteristics_quiz += 1
                "The scenario where the algorithm performs the least amount of work":
                    show adrian sad
                    a "Incorrect. That's the best case scenario."
                "The scenario where the algorithm performs an average amount of work":
                    show adrian sad
                    a "Incorrect. That's the average case scenario."
                "The scenario where the algorithm never finishes":
                    show adrian sad
                    a "Incorrect. A good algorithm should always finish in a finite number of steps."

        elif current_char_q == "q6":
            a "Which of the following is NOT a characteristic of a good algorithm?"
            menu:
                "Ambiguity":
                    show adrian happy
                    a "Correct! A good algorithm should be unambiguous, meaning every step is clearly defined."
                    $ chapter_1_Characteristics_quiz += 1
                "Finiteness":
                    show adrian sad
                    a "Incorrect. Finiteness is a key characteristic of a good algorithm."
                "Effectiveness":
                    show adrian sad
                    a "Incorrect. Effectiveness is a key characteristic of a good algorithm."
                "Feasibility":
                    show adrian sad
                    a "Incorrect. Feasibility is a key characteristic of a good algorithm."

        elif current_char_q == "q7":
            a "Which type of algorithm is responsible for maintaining the structure and order of a dataset after new data is added?"
            menu:
                "Insertion Algorithm":
                    show adrian happy
                    a "Correct! Insertion algorithms add new data while keeping the dataset's structure and order intact."
                    $ chapter_1_Characteristics_quiz += 1
                "Sorting Algorithm":
                    show adrian sad
                    a "Not quite. Sorting algorithms arrange data, but insertion algorithms handle adding new data while maintaining order."
                "Deletion Algorithm":
                    show adrian sad
                    a "Incorrect. Deletion algorithms remove data, not add it."
                "Searching Algorithm":
                    show adrian sad
                    a "Incorrect. Searching algorithms help find data, not insert it."

        elif current_char_q == "q8":
            a "Which of the following algorithms is primarily used to arrange data in a specific order, such as ascending or descending?"
            menu:
                "Sorting Algorithm":
                    show adrian happy
                    a "Correct! Sorting algorithms are used to arrange data in a particular order."
                    $ chapter_1_Characteristics_quiz += 1
                "Insertion Algorithm":
                    show adrian sad
                    a "Incorrect. Insertion algorithms add new data, but don't necessarily arrange all data."
                "Searching Algorithm":
                    show adrian sad
                    a "Incorrect. Searching algorithms are for finding data."
                "Updating Algorithm":
                    show adrian sad
                    a "Incorrect. Updating algorithms modify existing data."

    show adrian happy
    stop music fadeout 1.0
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Good job!!! Your Score of [chapter_1_Characteristics_quiz] has been Graded"

    if persistent.chapter_1 == True:
        a "Would you like to continue to the chapter quiz?"
        menu:
            "Yes":
                jump chapter_1_Algorithms_Quiz
            "No":
                pass

    jump chapter_1_Algorithms

#Good Programming
label chapter_1_Algorithms:
    show adrian smiling 
    a "We'll be tackling the last few topics of this chapter, so hang in there! Okay?"
    show adrian explaining
    a "How can one write an algorithm?"
    a "Well, there are several steps to writing an algorithm, and they can vary depending on the problem you're trying to solve."
    a "As we know that all programming languages share basic code constructs like loops (do, for, while), 
        flow-control (if-else), etc. These common constructs can be used to write an algorithm."
    a "We write algorithms in a step-by-step manner, but it is not always the case. 
        Algorithm writing is a process and is executed after the problem domain is well-defined."
    show adrian smiling
    a "Now Good Computer Programming. What is it?"

    screen good_programming_features:
        frame:
            xalign 0.8
            yalign 0.3
            xpadding 60
            ypadding 60
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5
                text "{size=+10}{b}Features of Good Programming{/b}" color "#00FF40" outlines [(4, "#000000", 0, 0)]
                text "• Run Efficiently and Correctly" size 32 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "• Have a user friendly interface" size 32 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "• Be easy to read and Understand" size 32 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "• Be easy to debug" size 32 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "• Be easy to modify" size 32 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "• Be easy to maintain" size 32 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                textbutton "Close" action Return()

    show screen good_programming_features
    show adrian at left
    with move
    a "Please review these features on the screen."
    hide screen good_programming_features

    show adrian explaining at center
    with move
    a "Let's try to learn algorithm-writing using an example."

    a "The problem: We need to design an algorithm to add two numbers and display the result."

    show adrian smiling
    a "Think of it like counting two sets of toys. If you have 5 toys in one pile and 3 in another, 
        you add them together to find the total."

    screen algorithm_example_steps:
        frame:
            xalign 0.9
            yalign 0.3
            xpadding 60
            ypadding 60
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5
                text "{size=+10}{b}Steps to Add Two Numbers{/b}" color "#00FF40" outlines [(4, "#000000", 0, 0)]
                text "Step 1: START—this tells us we are beginning the process." size 32 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "Step 2: Declare three numbers—let's call them a, b, and c." size 32 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "Step 3: Assign values to a and b. Let's say a is 5 and b is 3." size 32 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "Step 4: Add a and b together." size 32 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "Step 5: Store the result in c." size 32 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "Step 6: Print c—the final total." size 32 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "Step 7: STOP—the algorithm is complete!" size 32 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                textbutton "Close" action Return()
    play sound "sfx/cave_sound.mp3"
    pause 0.5
    show adrian explaining at left 
    with dissolve
    a "Just like that, we've built a simple step-by-step process to solve a problem."
    show screen algorithm_example_steps
    a "Algorithms are all about breaking tasks into clear instructions so that computers (or even people!) can follow them easily."
    show adrian normal
    a "Please review these steps on the screen."
    a "{size=+100}{color=#FF0000}{b}{w=0.1}RE{w=0.1}V{w=0.1}I{w=0.1}E{w=0.1}W {w=0.1}I{w=0.1}T!{/b}"
    hide screen algorithm_example_steps

    show adrian smug at center
    with move
    play sound "sfx/bell.mp3"
    a "Uh Oh, Theres that sound again. "
    $ chapter_1_progress += 1
    jump chapter_1_Algorithms_Quiz

init python:
    import random
    chapter_1_Algorithms_question_order = ["q1", "q2", "q3", "q4", "q5"]
    random.shuffle(chapter_1_Algorithms_question_order)

label chapter_1_Algorithms_Quiz:
    $ chapter_1_Algorithms_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 0.5

    show adrian smiling at center

    a "Let's see how well you understand algorithms with a few questions."

    while chapter_1_Algorithms_question_order:
        $ current_alg_q = chapter_1_Algorithms_question_order.pop(0)

        if current_alg_q == "q1":
            a "1. Which of the following is a step-by-step procedure for solving a problem?"
            menu:
                "Algorithm":
                    show adrian happy
                    a "Correct! An algorithm is a step-by-step procedure for solving problems."
                    $ chapter_1_Algorithms_quiz += 1
                "Data Structure":
                    show adrian sad
                    a "Incorrect. Data structures are ways to organize and store data."
                "Variable":
                    show adrian sad
                    a "Incorrect. Variables store data values."
                "Function":
                    show adrian sad
                    a "Incorrect. Functions are blocks of code that perform specific tasks."

        elif current_alg_q == "q2":
            a "2. Which characteristic is essential for a good algorithm?"
            menu:
                "Ambiguity":
                    show adrian sad
                    a "Incorrect. Algorithms should be unambiguous."
                "Finiteness":
                    show adrian happy
                    a "Correct! A good algorithm must terminate after a finite number of steps."
                    $ chapter_1_Algorithms_quiz += 1
                "Infinite loops":
                    show adrian sad
                    a "Incorrect. Infinite loops are not desirable in algorithms."
                "Randomness":
                    show adrian sad
                    a "Incorrect. Randomness is not a required characteristic."

        elif current_alg_q == "q3":
            a "3. What is the output of an algorithm?"
            menu:
                "The result produced after processing the input":
                    show adrian happy
                    a "Correct! The output is the result produced by the algorithm."
                    $ chapter_1_Algorithms_quiz += 1
                "The data given to the algorithm":
                    show adrian sad
                    a "Incorrect. That's the input."
                "The steps of the algorithm":
                    show adrian sad
                    a "Incorrect. Those are the instructions."
                "The programming language used":
                    show adrian sad
                    a "Incorrect. The language is not the output."

        elif current_alg_q == "q4":
            a "4. Which of the following is NOT a type of algorithm case?"
            menu:
                "Best Case":
                    show adrian sad
                    a "Incorrect. Best case is a type of algorithm case."
                "Worst Case":
                    show adrian sad
                    a "Incorrect. Worst case is a type of algorithm case."
                "Average Case":
                    show adrian sad
                    a "Incorrect. Average case is a type of algorithm case."
                "Random Case":
                    show adrian happy
                    a "Correct! Random case is not a standard type of algorithm case."
                    $ chapter_1_Algorithms_quiz += 1

        elif current_alg_q == "q5":
            a "5. Which statement about algorithms is TRUE?"
            menu:
                "Algorithms must have clear and precise steps":
                    show adrian happy
                    a "Correct! Algorithms should be clear and precise."
                    $ chapter_1_Algorithms_quiz += 1
                "Algorithms can run forever without stopping":
                    show adrian sad
                    a "Incorrect. Algorithms should terminate after a finite number of steps."
                "Algorithms do not need any input":
                    show adrian sad
                    a "Incorrect. Algorithms may have zero or more inputs."
                "Algorithms are only used for sorting data":
                    show adrian sad
                    a "Incorrect. Algorithms are used for many tasks, not just sorting."

    show adrian happy
    stop music fadeout 1.0
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    jump chapter_1_restart
label chapter_1_restart:
    $ chapter_1_test = chapter_1_Data_Structures_quiz + chapter_1_Characteristics_quiz + chapter_1_Algorithms_quiz + chapter_1_Good_Programming_quiz
    a "Your score is [chapter_1_test]"
    a "Let's see how well you do in the {size=+20}CHAPTER QUIZ"
    if chapter_1_test <= 8:
        show adrian blush
        jump chapter_1_quiz_easy
    elif chapter_1_test <= 14:
        show adrian smiling
        jump chapter_1_quiz_medium
    else:
        show adrian happy
        jump chapter_1_quiz_hard
    

        
init python:
    import random
    chapter_1_hard_question_order = [
        "mc1", "mc2", "mc3", "mc4", "mc5", "mc6", "mc7",
        "fill1", "fill2", "fill3", "fill4",
        "mc8", "mc9", "mc10", "mc11"
    ]
    random.shuffle(chapter_1_hard_question_order)

label chapter_1_quiz_hard:
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 0.5
    $ chapter_1_score = 0

    show adrian smiling at center
    a "Welcome to the {b}Quiz!{/b} Let's see how much you've learned."

    while chapter_1_hard_question_order:
        $ current_q = chapter_1_hard_question_order.pop(0)

        if current_q == "mc1":
            a "Which data structure allows elements to be added or removed from both ends?"
            menu:
                "Deque":
                    show adrian happy
                    call ch1_scoreadd
                    a "Correct! A deque allows insertion and deletion at both ends."
                "Stack":
                    show adrian sad
                    a "Incorrect. Stack only allows insertion and removal at one end."
                "Queue":
                    show adrian sad
                    a "Incorrect. Queue only allows insertion at one end and removal at the other."
                "Array":
                    show adrian sad
                    a "Incorrect. Array does not have this property."

        elif current_q == "mc2":
            a "Which of the following is NOT a characteristic of data structures?"
            menu:
                "Time Complexity":
                    show adrian sad
                    a "Incorrect. Time complexity is a characteristic of data structures."
                "Space Complexity":
                    show adrian sad
                    a "Incorrect. Space complexity is a characteristic of data structures."
                "User Interface Design":
                    show adrian happy
                    a "Correct! User interface design is not a characteristic of data structures."
                    call ch1_scoreadd

        elif current_q == "mc3":
            a "What is the difference between a stack and a queue?"
            menu:
                "A stack is LIFO (Last In First Out) and a queue is FIFO (First In First Out)":
                    show adrian happy
                    a "Correct! A stack is LIFO and a queue is FIFO."
                    call ch1_scoreadd
                "A stack is FIFO and a queue is LIFO":
                    show adrian sad
                    a "Incorrect. A stack is LIFO and a queue is FIFO."
                "There is no difference":
                    show adrian sad
                    a "Incorrect. There is a difference between a stack and a queue."

        elif current_q == "mc4":
            a "What is the primary purpose of search algorithms?"
            menu:
                "To find specific data within a larger dataset quickly and efficiently":
                    show adrian happy
                    a "Correct! Search algorithms are designed to find specific data quickly and efficiently."
                    call ch1_scoreadd
                "To sort data in a specific order":
                    show adrian sad
                    a "Incorrect. Sorting algorithms are used for arranging data, not searching for it."
                "To delete data from a dataset":
                    show adrian sad
                    a "Incorrect. Deletion algorithms are used for removing data, not searching for it."

        elif current_q == "mc5":
            a "Which of the following is NOT a common category of algorithms?"
            menu:
                "Searching":
                    show adrian sad
                    a "Incorrect. Searching is a common category of algorithms."
                "Sorting":
                    show adrian sad
                    a "Incorrect. Sorting is a common category of algorithms."
                "Extracting":
                    show adrian happy
                    a "Correct! Extracting is not typically listed as a common category of algorithms."
                    call ch1_scoreadd
                "Deletion":
                    show adrian sad
                    a "Incorrect. Deletion is a common category of algorithms."

        elif current_q == "mc6":
            a "Which of the following is NOT a characteristic of a good algorithm?"
            menu:
                "Unambiguous":
                    show adrian sad
                    a "Incorrect. Unambiguous is a key characteristic of a good algorithm."
                "Infinite steps":
                    show adrian happy
                    a "Correct! A good algorithm must always terminate after a finite number of steps."
                    call ch1_scoreadd
                "Effective":
                    show adrian sad
                    a "Incorrect. Effectiveness is a key characteristic of a good algorithm."
                "Feasible":
                    show adrian sad
                    a "Incorrect. Feasibility is a key characteristic of a good algorithm."

        elif current_q == "mc7":
            a "True or False: Insertion algorithms add new data while maintaining the dataset’s structure."
            menu:
                "True":
                    show adrian happy
                    a "You are Correct. Good JOB!!"
                    call ch1_scoreadd
                "False":
                    show adrian sad
                    a "Incorrect. Of course you add new data, you insert something."

        elif current_q == "fill1":
            a "A ____ algorithm modifies existing data in a dataset to reflect updates correctly."
            $ answer = renpy.input("Fill in the blank").strip()
            if answer.lower() == "updating":
                show adrian happy
                a "You are Correct. Good Job!!"
                call ch1_scoreadd
            else:
                show adrian sad
                a "Sorry, wrong answer."

        elif current_q == "fill2":
            a "A ____ is a linear data structure where elements are added and removed from only one end."
            $ answer = renpy.input("Fill in the blank").strip()
            if answer.lower() == "stack":
                show adrian happy
                a "Correct! Stack is the right answer."
                call ch1_scoreadd
            else:
                show adrian sad
                a "Sorry, the correct answer is 'stack'."

        elif current_q == "fill3":
            a "The process of arranging data in a particular order is called ____."
            $ answer = renpy.input("Fill in the blank").strip()
            if answer.lower() == "sorting":
                show adrian happy
                a "Correct! Sorting is the process."
                call ch1_scoreadd
            else:
                show adrian sad
                a "Sorry, the correct answer is 'sorting'."

        elif current_q == "fill4":
            a "In a ____ search, the dataset must be sorted before searching."
            $ answer = renpy.input("Fill in the blank").strip()
            if answer.lower() == "binary":
                show adrian happy
                a "Correct! Binary search requires a sorted dataset."
                call ch1_scoreadd
            else:
                show adrian sad
                a "Sorry, the correct answer is 'binary'."

        elif current_q == "mc8":
            a "Which data structure uses nodes that point to the next node in the sequence?"
            menu:
                "Linked List":
                    show adrian happy
                    a "Correct! Linked lists use nodes that point to the next node."
                    call ch1_scoreadd
                "Array":
                    show adrian sad
                    a "Incorrect. Arrays do not use nodes."
                "Stack":
                    show adrian sad
                    a "Incorrect. Stacks do not use nodes."
                "Queue":
                    show adrian sad
                    a "Incorrect. Queues do not use nodes."

        elif current_q == "mc9":
            a "Which of the following is NOT a linear data structure?"
            menu:
                "Tree":
                    show adrian happy
                    a "Correct! Trees are non-linear data structures."
                    call ch1_scoreadd
                "Queue":
                    show adrian sad
                    a "Incorrect. Queue is linear."
                "Stack":
                    show adrian sad
                    a "Incorrect. Stack is linear."
                "Array":
                    show adrian sad
                    a "Incorrect. Array is linear."

        elif current_q == "mc10":
            a "Which operation is used to remove an element from the end of a stack?"
            menu:
                "Pop":
                    show adrian happy
                    a "Correct! Pop removes the top element from a stack."
                    call ch1_scoreadd
                "Push":
                    show adrian sad
                    a "Incorrect. Push adds an element."
                "Enqueue":
                    show adrian sad
                    a "Incorrect. Enqueue is for queues."
                "Dequeue":
                    show adrian sad
                    a "Incorrect. Dequeue is for queues."

        elif current_q == "mc11":
            a "Which of the following best describes a queue?"
            menu:
                "First In, First Out":
                    show adrian happy
                    a "Correct! Queue is FIFO."
                    call ch1_scoreadd
                "Last In, First Out":
                    show adrian sad
                    a "Incorrect. That's a stack."
                "Random Access":
                    show adrian sad
                    a "Incorrect. That's an array."
                "Hierarchical":
                    show adrian sad
                    a "Incorrect. That's a tree."

    show adrian smiling

    # Matching Type Question 1
    a "Let's try a matching type question! Match the data structure to its description. Type your answers as a comma-separated list (e.g., 1A,2B,3C,4D)."
    a "1. Stack\n2. Queue\n3. Linked List\n4. Tree"
    a "A. Each element points to the next; dynamic size.\nB. Hierarchical structure with parent and child nodes.\nC. First In, First Out (FIFO) structure.\nD. Last In, First Out (LIFO) structure."
    $ matching_answer = renpy.input("Enter your matches (e.g., 1D,2C,3A,4B):").strip().replace(" ", "").lower()
    if matching_answer.startswith("1d,2c,3a,4b"):
        show adrian happy
        a "Excellent! All your matches are correct."
        call ch1_scoreadd
    else:
        show adrian sad
        a "Not quite. The correct matches are: 1D, 2C, 3A, 4B."

    # Matching Type Question 2
    a "Let's do another matching question! Match the algorithm to its description. Type your answers as a comma-separated list (e.g., 1A,2B,3C,4D)."
    a "1. Binary Search\n2. Bubble Sort\n3. Insertion\n4. Deletion"
    a "A. Removes data from a dataset.\nB. Adds new data to a dataset.\nC. Finds data in a sorted list by repeatedly dividing the search interval in half.\nD. Repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order."
    $ matching_answer2 = renpy.input("Enter your matches (e.g., 1C,2D,3B,4A):").strip().replace(" ", "").lower()
    if matching_answer2.startswith("1c,2d,3b,4a"):
        show adrian happy
        a "Excellent! All your matches are correct."
        call ch1_scoreadd
    else:
        show adrian sad
        a "Not quite. The correct matches are: 1C, 2D, 3B, 4A."

    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job! You finished the Hard Quiz. Your total score is [chapter_1_score]."

    jump chapter_1_performance

init python:
    import random
    chapter_1_medium_question_order = ["q1", "q2", "q3", "q4", "q5", "q6", "q7"]
    random.shuffle(chapter_1_medium_question_order)

label chapter_1_quiz_medium:
    $ chapter_1_score = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 0.5

    show adrian smiling at center
    a "Welcome to the {b}Quiz{/b}! Let's see how much you've learned."

    while chapter_1_medium_question_order:
        $ current_q = chapter_1_medium_question_order.pop(0)

        if current_q == "q1":
            a "Which data structure allows elements to be added or removed from both ends?"
            menu:
                "Deque":
                    show adrian happy
                    call ch1_scoreadd
                    a "Correct! A deque allows insertion and deletion at both ends."
                "Stack":
                    show adrian sad
                    a "Incorrect. Stack only allows insertion and removal at one end."
                "Queue":
                    show adrian sad
                    a "Incorrect. Queue only allows insertion at one end and removal at the other."
                "Array":
                    show adrian sad
                    a "Incorrect. Array does not have this property."

        elif current_q == "q2":
            a "Which of the following is NOT a characteristic of data structures?"
            menu:
                "Time Complexity":
                    show adrian sad
                    a "Incorrect. Time complexity is a characteristic of data structures."
                "Space Complexity":
                    show adrian sad
                    a "Incorrect. Space complexity is a characteristic of data structures."
                "User Interface Design":
                    show adrian happy
                    a "Correct! UI design is not a data structure characteristic."
                    call ch1_scoreadd

        elif current_q == "q3":
            a "What is the difference between a stack and a queue?"
            menu:
                "A stack is LIFO and a queue is FIFO":
                    show adrian happy
                    a "Correct! Stack is LIFO and queue is FIFO."
                    call ch1_scoreadd
                "A stack is FIFO and a queue is LIFO":
                    show adrian sad
                    a "Incorrect. You got them reversed."
                "There is no difference":
                    show adrian sad
                    a "Incorrect. They differ in access order."

        elif current_q == "q4":
            a "What is the primary purpose of search algorithms?"
            menu:
                "To find specific data within a larger dataset quickly and efficiently":
                    show adrian happy
                    a "Correct! That’s exactly what search algorithms do."
                    call ch1_scoreadd
                "To sort data in a specific order":
                    show adrian sad
                    a "Incorrect. That’s sorting, not searching."
                "To delete data from a dataset":
                    show adrian sad
                    a "Incorrect. That’s deletion, not searching."

        elif current_q == "q5":
            a "Which of the following is NOT a common category of algorithms?"
            menu:
                "Searching":
                    show adrian sad
                    a "Incorrect. Searching is a standard category."
                "Sorting":
                    show adrian sad
                    a "Incorrect. Sorting is a standard category."
                "Extracting":
                    show adrian happy
                    a "Correct! Extracting isn’t typically listed."
                    call ch1_scoreadd
                "Deletion":
                    show adrian sad
                    a "Incorrect. Deletion is a valid category."

        elif current_q == "q6":
            a "Which of the following is NOT a characteristic of a good algorithm?"
            menu:
                "Unambiguous":
                    show adrian sad
                    a "Incorrect. Clarity is essential."
                "Infinite steps":
                    show adrian happy
                    a "Correct! Algorithms must terminate."
                    call ch1_scoreadd
                "Effective":
                    show adrian sad
                    a "Incorrect. Effectiveness is key."
                "Feasible":
                    show adrian sad
                    a "Incorrect. Feasibility matters."

        elif current_q == "q7":
            a "True or False: Insertion algorithms add new data while maintaining the dataset’s structure."
            menu:
                "True":
                    show adrian happy
                    a "You are Correct. Good JOB!!"
                    call ch1_scoreadd
                "False":
                    show adrian sad
                    a "Incorrect. Insertion preserves structure."

    jump ch1_med1
    label ch1_med1:
        a "A ____ algorithm modifies existing data in a dataset to reflect updates correctly."
        $ answer = renpy.input("Fill in the blank").strip()
        if answer.lower() == "updating":
            show adrian happy
            a "You are Correct. Good Job!!"
            call ch1_scoreadd
        else:
            show adrian sad
            a "Sorry, wrong answer."

        jump ch1_med2

    label ch1_med2:
        a "A ____ is a linear data structure where elements are added and removed from only one end."
        $ answer = renpy.input("Fill in the blank").strip()
        if answer.lower() == "stack":
            show adrian happy
            a "Correct! Stack is the right answer."
            call ch1_scoreadd
        else:
            show adrian sad
            a "Sorry, the correct answer is 'stack'."

        jump ch1_med3

    label ch1_med3:
        a "The process of arranging data in a particular order is called ____."
        $ answer = renpy.input("Fill in the blank").strip()
        if answer.lower() == "sorting":
            show adrian happy
            a "Correct! Sorting is the process."
            call ch1_scoreadd
        else:
            show adrian sad
            a "Sorry, the correct answer is 'sorting'."

        jump ch1_med4

    label ch1_med4:
        a "In a ____ search, the dataset must be sorted before searching."
        $ answer = renpy.input("Fill in the blank").strip()
        if answer.lower() == "binary":
            show adrian happy
            a "Correct! Binary search requires a sorted dataset."
            call ch1_scoreadd
        else:
            show adrian sad
            a "Sorry, the correct answer is 'binary'."

        jump ch1_med5

    label ch1_med5:
        a "Which data structure uses nodes that point to the next node in the sequence?"
        menu:
            "Linked List":
                show adrian happy
                a "Correct! Linked lists use nodes that point to the next node."
                call ch1_scoreadd
            "Array":
                show adrian sad
                a "Incorrect. Arrays do not use nodes."
            "Stack":
                show adrian sad
                a "Incorrect. Stacks do not use nodes."
            "Queue":
                show adrian sad
                a "Incorrect. Queues do not use nodes."

        jump ch1_med6

    label ch1_med6:
        a "Which of the following is NOT a linear data structure?"
        menu:
            "Tree":
                show adrian happy
                a "Correct! Trees are non-linear data structures."
                call ch1_scoreadd
            "Queue":
                show adrian sad
                a "Incorrect. Queue is linear."
            "Stack":
                show adrian sad
                a "Incorrect. Stack is linear."
            "Array":
                show adrian sad
                a "Incorrect. Array is linear."

        jump ch1_med7

    label ch1_med7:
        a "Which operation is used to remove an element from the end of a stack?"
        menu:
            "Pop":
                show adrian happy
                a "Correct! Pop removes the top element from a stack."
                call ch1_scoreadd
            "Push":
                show adrian sad
                a "Incorrect. Push adds an element."
            "Enqueue":
                show adrian sad
                a "Incorrect. Enqueue is for queues."
            "Dequeue":
                show adrian sad
                a "Incorrect. Dequeue is for queues."

        jump ch1_med8

    label ch1_med8:
        a "Which of the following best describes a queue?"
        menu:
            "First In, First Out":
                show adrian happy
                a "Correct! Queue is FIFO."
                call ch1_scoreadd
            "Last In, First Out":
                show adrian sad
                a "Incorrect. That's a stack."
            "Random Access":
                show adrian sad
                a "Incorrect. That's an array."
            "Hierarchical":
                show adrian sad
                a "Incorrect. That's a tree."

        show adrian smiling
        stop music fadeout 0.5
        play music "bgm/city-high-life.mp3" fadein 0.5
        play sound "sfx/success.mp3"
        a "Great job! You finished the Moderate Quiz. Your total score is [chapter_1_score]."
        jump chapter_1_performance


init python:
    import random
    chapter_1_easy_question_order = ["q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10"]
    random.shuffle(chapter_1_easy_question_order)

label chapter_1_quiz_easy:
    $ chapter_1_score = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 0.5

    show adrian smiling at center
    a "Welcome to the {b}Quiz!{/b} Let's see how much you've learned."

    while chapter_1_easy_question_order:
        $ current_q = chapter_1_easy_question_order.pop(0)

        if current_q == "q1":
            a "1. Which of the following is a data structure?"
            menu:
                "Array":
                    show adrian happy
                    a "Correct! An array is a data structure."
                    call ch1_scoreadd
                "Button":
                    show adrian sad
                    a "Incorrect. A button is not a data structure."
                "Window":
                    show adrian sad
                    a "Incorrect. A window is not a data structure."
                "Image":
                    show adrian sad
                    a "Incorrect. An image is not a data structure."

        elif current_q == "q2":
            a "2. True or False: A stack follows the Last In, First Out (LIFO) principle."
            menu:
                "True":
                    show adrian happy
                    a "Correct! Stack is LIFO."
                    call ch1_scoreadd
                "False":
                    show adrian sad
                    a "Incorrect. Stack is LIFO."

        elif current_q == "q3":
            a "3. Which data structure works like a line at a ticket counter?"
            menu:
                "Queue":
                    show adrian happy
                    a "Correct! A queue works like a line."
                    call ch1_scoreadd
                "Stack":
                    show adrian sad
                    a "Incorrect. A stack is not like a line."
                "Array":
                    show adrian sad
                    a "Incorrect. An array is not like a line."
                "Graph":
                    show adrian sad
                    a "Incorrect. A graph is not like a line."

        elif current_q == "q4":
            a "4. True or False: Algorithms are only used in computer programming."
            menu:
                "False":
                    show adrian happy
                    a "Correct! Algorithms can be used in daily life too."
                    call ch1_scoreadd
                "True":
                    show adrian sad
                    a "Incorrect. Algorithms are everywhere!"

        elif current_q == "q5":
            a "5. Which of these is NOT a characteristic of a good algorithm?"
            menu:
                "Ambiguity":
                    show adrian happy
                    a "Correct! Algorithms should not be ambiguous."
                    call ch1_scoreadd
                "Finiteness":
                    show adrian sad
                    a "Incorrect. Finiteness is a good characteristic."
                "Effectiveness":
                    show adrian sad
                    a "Incorrect. Effectiveness is a good characteristic."
                "Input":
                    show adrian sad
                    a "Incorrect. Input is a good characteristic."

        elif current_q == "q6":
            a "6. True or False: A queue is First In, First Out (FIFO)."
            menu:
                "True":
                    show adrian happy
                    a "Correct! Queue is FIFO."
                    call ch1_scoreadd
                "False":
                    show adrian sad
                    a "Incorrect. Queue is FIFO."

        elif current_q == "q7":
            a "7. Which of the following is used to find data quickly?"
            menu:
                "Search Algorithm":
                    show adrian happy
                    a "Correct! Search algorithms help find data."
                    call ch1_scoreadd
                "Sorting Algorithm":
                    show adrian sad
                    a "Incorrect. Sorting arranges data."
                "Insertion Algorithm":
                    show adrian sad
                    a "Incorrect. Insertion adds data."
                "Deletion Algorithm":
                    show adrian sad
                    a "Incorrect. Deletion removes data."

        elif current_q == "q8":
            a "8. True or False: A linked list can grow and shrink in size easily."
            menu:
                "True":
                    show adrian happy
                    a "Correct! Linked lists are dynamic."
                    call ch1_scoreadd
                "False":
                    show adrian sad
                    a "Incorrect. Linked lists are flexible."

        elif current_q == "q9":
            a "9. Which of these is an example of a sorting algorithm?"
            menu:
                "Bubble Sort":
                    show adrian happy
                    a "Correct! Bubble Sort is a sorting algorithm."
                    call ch1_scoreadd
                "Binary Search":
                    show adrian sad
                    a "Incorrect. Binary Search is a search algorithm."
                "Queue":
                    show adrian sad
                    a "Incorrect. Queue is a data structure."
                "Stack":
                    show adrian sad
                    a "Incorrect. Stack is a data structure."

        elif current_q == "q10":
            a "10. True or False: Data structures help organize and store data efficiently."
            menu:
                "True":
                    show adrian happy
                    a "Correct! That's the main purpose of data structures."
                    call ch1_scoreadd
                "False":
                    show adrian sad
                    a "Incorrect. Data structures do help organize data."

    show adrian smiling
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job! You finished the Easy Quiz. Your total score is [chapter_1_score]."

    jump chapter_1_performance

label chapter_1_performance:
    # Data Structures Quiz
    if chapter_1_Data_Structures_quiz < 2:
        a "You need to review the Data Structures section."
        a "Consider revisiting the material to improve your understanding."
    elif chapter_1_Data_Structures_quiz < 4:
        a "You did okay in the Data Structures section, but there's room for improvement."
        a "Reviewing the material could help solidify your knowledge."

    # Characteristics Quiz
    if chapter_1_Characteristics_quiz < 2:
        a "You need to review the Characteristics of Algorithms section."
        a "Focus on understanding the key properties and categories."
    elif chapter_1_Characteristics_quiz < 4:
        a "You did okay in the Characteristics section, but there's room for improvement."
        a "Revisiting the algorithm cases and properties could help reinforce your understanding."

    # Algorithms Quiz
    if chapter_1_Algorithms_quiz < 2:
        a "You need to review the Algorithms section."
        a "Make sure you understand the steps and characteristics of good algorithms."
    elif chapter_1_Algorithms_quiz < 4:
        a "You did okay in the Algorithms section, but there's room for improvement."
        a "Reviewing algorithm-writing and examples could strengthen your grasp."

    jump chapter_1_ending
label chapter_1_ending:    
    $ chapter_1_progress += 1
    $ persistent.chapter_1 = True
    play sound "sfx/success.mp3"
    a "Your Score is [chapter_1_score]!"
    a "Would You like to test again?"
    menu:
        "Yes":
            jump chapter_1_restart
        "No":
            pass
    show adrian happy
    a "You have finished chapter 1. You can continue to Chapter 2!"
    $ renpy.force_autosave()
    stop music fadeout 0.5
    jump menu
    
    
