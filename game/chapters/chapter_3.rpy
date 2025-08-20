screen chapter_3_introscreen:
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 60
        ypadding 60
        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5
            text "Chapter 3: Linked List" size 60 color "#FFFFFF" outlines [(5, "#000000", 0, 0)]

screen chapter_3_Properties:
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 60
        ypadding 60
        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5
            text "Linked Lists Properties" size 60 color "#FFFFFF" outlines [(5, "#000000", 0, 0)]

screen chapter_3_Operations:
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 60
        ypadding 60
        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5
            text "Linked Lists Operation" size 60 color "#FFFFFF" outlines [(5, "#000000", 0, 0)]

screen chapter_3_Operations_Building:
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 60
        ypadding 60
        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5
            text "Building Linked Lists" size 60 color "#FFFFFF" outlines [(5, "#000000", 0, 0)]

screen chapter_3_Problems:
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 60
        ypadding 60

        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5
            text "Problems With Linked Lists" size 60 color "#FFFFFF" outlines [(5, "#000000", 0, 0)]

screen LinkedListList:
    frame:
        xalign 0.5
        yalign 0.3
        xpadding 100
        ypadding 100

        hbox:
            spacing 80
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5
                text "Linked Lists Properties" size 40 color "#FFFFFF" outlines [(5, "#000000", 0, 0)]
                text "Linked Lists Operations" size 40 color "#FFFFFF" outlines [(5, "#000000", 0, 0)]
                text "Building Linked Lists" size 40 color "#FFFFFF" outlines [(5, "#000000", 0, 0)]
                text "Problems With Linked Lists" size 40 color "#FFFFFF" outlines [(5, "#000000", 0, 0)]

screen LinkListAdvantages:
    frame:
        xalign 0.5
        yalign 0.3
        xpadding 100
        ypadding 100

        hbox:
            spacing 50
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5
                text "ADVANTAGES" size 50 color "#FFFFFF" outlines [(5, "#000000", 0, 0)] 
                text "1. Dynamic" size 40 color "#FFFFFF" outlines [(5, "#000000", 0, 0)] 
                text "2. Can Allocate" size 40 color "#FFFFFF" outlines [(5, "#000000", 0, 0)] 
                text "3. Efficient" size 40 color "#FFFFFF" outlines [(5, "#000000", 0, 0)] 
                text "4. Easy Implementation" size 40 color "#FFFFFF" outlines [(5, "#000000", 0, 0)] 
                text "5. Can Store Any Size of Items" size 40 color "#FFFFFF" outlines [(5, "#000000", 0, 0)] 
                text "6. It Grows Organically" size 40 color "#FFFFFF" outlines [(5, "#000000", 0, 0)]

            imagebutton:
                xalign 1.0
                yalign 0.0
                xoffset -30
                yoffset 30
                auto "UI/btn_back_%s.png"
                action Return()


screen LinkListDisadvantages:
    frame:
        xalign 0.5
        yalign 0.3
        xpadding 100
        ypadding 100

        hbox:
            spacing 50
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5
                text "DISADVANTAGES" size 50 color "#FFFFFF" outlines [(5, "#000000", 0, 0)] 
                text "1. Waste Memomy" size 40 color "#FFFFFF" outlines [(5, "#000000", 0, 0)] 
                text "2. Must Be Read In Order" size 40 color "#FFFFFF" outlines [(5, "#000000", 0, 0)] 
                text "3. Hard to Reverse Traverse" size 40 color "#FFFFFF" outlines [(5, "#000000", 0, 0)]
            
            imagebutton:
                xalign 1.0
                yalign 0.0
                xoffset -30
                yoffset 30
                auto "UI/btn_back_%s.png"
                action Return()

screen adv_dis_choice:
    imagebutton:
        xalign 0.3
        yalign 0.5
        xoffset -30
        yoffset 30
        auto "UI/LLAdvatages_%s.png"
        action ShowMenu("LinkListAdvantages")

    imagebutton:
        xalign 0.8
        yalign 0.5
        xoffset -30
        yoffset 30
        auto "UI/LLDisdvatages_%s.png"
        action ShowMenu("LinkListDisadvantages")
 



label chapter_3_intro:
    play audio ("sfx/start.mp3")
    play music "bgm/city-high-life.mp3" fadein 1.0
    show black
    pause 1.0
    show screen chapter_3_introscreen
    pause 2.0
    scene mt tree with dissolve
    pause 1.0
    hide screen chapter_3_introscreen
    with dissolve
    
    show screen menu_btn
    if persistent.chapter_3 == True:
        show adrian smiling at center:
            smaller
        a "Hi welcome back to chapter 3"
        a "Do you want to go through this chapter again?"
        menu:
            "Yes":
                a "Which part do you want to go through again?"

                menu:
                    "Properties":
                        jump chapter_3_linked_list_properties
                    "Operations":
                        jump chapter_3_linked_list_operation
                    "Insertion":
                        jump chapter_3_linked_list_insertion1
                    "Deletion":
                        jump chapter_3_linked_list_remove
                    "Problems":
                        jump chapter_3_problems_with_linked_list
                    "Quizzes":
                        jump ch3_quiz1
            "No":
                jump menu
    else:
        pass

        
    show adrian smiling at center:
        smaller 

    show screen menu_btn
    a "Welcome to chapter 3: {size=+20}{b}Linked Lists{/b}"
    a "We will be tackling:"

    show screen LinkedListList

    "Wow thats a lot of topics to cover"

    hide screen LinkedListList
    "Lets Start"
    jump chapter_3_linked_list_properties

label chapter_3_linked_list_properties:


    show screen chapter_3_Properties
    with fade
    pause 1.0
    hide screen chapter_3_Properties
    #nodes ADD VISUALS

    a "So Nodes, Not Noses, But Nodes"
    a "What is a {b}Node{/b}?"

    show adrian explaining
    a "It is Basically a {i}Container for Data{/i}"
    a "Just know that it Contains {size=+20 }{b}Data{/b} and {size=+20}{b}Pointer{/b}"
    a "A {b}Pointer{/b} is a Reference to the Next Node in the List, and remember an {b}Index{/b} is the position of the Node in the List"

    show adrian smug
    a "THAT IS BASICALLY IT"

    show adrian normal
    a "A Linked List is a Collection of {b}Nodes and Pointers{/b} Connected Together"

    show screen node_visual
    with fade
    screen node_visual:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 40
            ypadding 40
            vbox:
                spacing 15
                xalign 0.5
                yalign 0.5
                text "Node" size 50 color "#FFFFFF" outlines [(3, "#000000", 0, 0)]
                text "Data | Pointer → Index: 0" size 40 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
    pause 3.0
    hide screen node_visual

    a "You Got that?"
    menu:
        "Yes":
            a "Good"
            pass
        "No":
            a "Well, I guess you will have to read it again"
            show screen node_visual
            pause 0.5
            hide screen node_visual
            show adrian smug
            a "Is that clear now?"
            menu: 
                "Yes":
                    a "Good"
                "No":
                    show adrian smiling
                    a "Maybe One More Time"
                    show screen node_visual
                    pause 0.3
                    hide screen node_visual
                    show adrian smug
                    a "better?"
                    menu:
                        "Yes":
                            a "Good"
                        "No":
                            show adrian smiling
                            a "LETS TRY AGAIN"
                            show screen node_visual
                            pause 0.5
                            hide screen node_visual
                            a "Is that clear now?"
                            menu: 
                                "Yeah Im good":
                                    a "Good"
                                "No":
                                    a "Maybe One More Time"
                                    show screen node_visual
                                    pause 1.0
                                    hide screen node_visual
                                    a "better?"
                                    menu:
                                        "Behave":
                                            a "Haha, lets go back to the lesson"
                                        "No":
                                            show adrian nocomment
                                            a "Youre threading on bad grounds here"
                                            a "are you sure you want to continue?"
                                            menu:
                                                "Yes":
                                                    a "Your choice, You should have known to Save your Game"
                                                    $ renpy.quit()
                                                "No":
                                                    a "Then lets go back to the lesson"
                                                    pass

    a "Now let's Continue with {b}Advantages and Disadvantages{/b}"

    show screen adv_dis_choice

    a "You can choose to view the Advantages or Disadvantages of Linked Lists"

    hide screen adv_dis_choice

    show adrian smiling
    play sound "sfx/bell.mp3"
    a "You hear that? Its time for some questions. Buckle Up Buckeroo"
    jump ch3_quiz1

label ch3_quiz1:
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    
    $ chapter_3_test = 0

    show adrian explaining
    a "What is a Node?"
    menu:
        "A Type of Linked List":
            a "Incorrect, A Node is not a type of Linked List"
        "A Container for Data":
            a "Correct"
            $ chapter_3_test += 1
        "A Type of Algorithm":
            a "Incorrect, A Node is not an Algorithm"
        "A Type of Data Structure":
            a "Incorrect, A Node is not a type of Data Structure"

    a "Next Question"
    show adrian smiling
    a "What is the purpose of a Pointer in a Linked List?"
    menu:
        "To Store Data":
            a "Incorrect, A Pointer does not store data"
        "To Reference the Next Node":
            a "Correct"
            $ chapter_3_test += 1
        "To Store the Previous Node":
            a "Incorrect, A Pointer does not store the Previous Node"
        "To Store the Index":
            a "Incorrect, A Pointer does not store the Index"
    
    a "Next Question"
    a "What is the main advantage of using a Linked List over an array?"
    menu:
        "Dynamic Size":
            a "Correct! Linked Lists can grow and shrink dynamically."
            $ chapter_3_test += 1
        "Simpler Structure":
            a "Incorrect, Linked Lists are more complex than arrays."
        "Less Memory Usage":
            a "Incorrect, Linked Lists often use more memory due to pointers."
        "Faster Access":
            a "Incorrect, Linked Lists do not have faster access than arrays."

    show adrian explaining
    a "Next Question"
    a "Which of the following is a disadvantage of Linked Lists?"
    menu:
        "Easy to Reverse Traverse":
            a "Incorrect, singly Linked Lists are hard to reverse traverse."
        "Waste Memory":
            a "Correct! Linked Lists use extra memory for pointers."
            $ chapter_3_test += 1
        "Fixed Size":
            a "Incorrect, Linked Lists are not fixed in size."
        "Fast Random Access":
            a "Incorrect, Linked Lists do not support fast random access."

    show adrian smug
    a "Next Question"
    a "What does each node in a Linked List contain?"

    menu:
        "Only Data":
            a "Incorrect, nodes also contain a pointer."
        "Data and Pointer":
            a "Correct! Each node contains data and a pointer to the next node."
            $ chapter_3_test += 1
        "Index and Data":
            a "Incorrect, nodes do not store their index."
        "Only Pointer":
            a "Incorrect, nodes also contain data."
    
    if persistent.chapter_3 == True:
        a "Would you like to continue with the next quiz?"
        menu:
            "Yes":
                jump ch3_quiz2
            "No":
                pass


    jump chapter_3_linked_list_operation

label chapter_3_linked_list_operation:
    play music "bgm/city-high-life.mp3" fadein 1.0
    show screen chapter_3_Operations
    with fade
    pause 1.0
    hide screen chapter_3_Operations

    show adrian explaining
    a "{size=+10}{b}Linked List Operations{/b}{/size}"
    a "Let's talk about how we perform operations on a Linked List."
    show adrian normal
    jump chapter_3_linked_list_insertion1

label chapter_3_linked_list_insertion1:

    a "{color=#00FF00}Inserting items at the beginning{/color} of the linked list is very simple!"
    a "We just need to update the references."
    show screen ch3_operation_visual
    screen ch3_operation_visual:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 40
            ypadding 40
            vbox:
                spacing 15
                xalign 0.5
                yalign 0.5
                text "Insert at Beginning" size 45 color "#FFFFFF" outlines [(3, "#000000", 0, 0)]
                text "New Node → Head → Next Node" size 35 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "Time Complexity: O(1)" size 30 color "#FFD700" outlines [(2, "#000000", 0, 0)]
    pause 2.0
    hide screen ch3_operation_visual
    a "Lets Visualize how this works"

    image ch_3_in_1 = Movie(play="images/videos/chapter_3_Insertion_1.webm", loop=False)

    window hide
    show ch_3_in_1 at truecenter
    pause 15.0
    hide ch_3_in_1
    window auto

    $ ch3_repeat_count1 = 0
    while True:

        show adrian explaining
        a "Would you like to see it again?"

        if ch3_repeat_count1 >= 3:
            a "You watched the animation [ch3_repeat_count1] time(s) already."
            a "You ok bud?"
        if ch3_repeat_count1 >= 6:
            a "You really like this animation huh?"
            a "I mean, I do too, but you should take a break"
            a "You can always come back to this chapter later"
            image horse = Movie(play="images/videos/horse.webm", loop=False)

            window hide
            show horse at truecenter
            pause 16.0
            hide horse 
            window auto

            $ renpy.force_autosave()
            jump menu
        else:
            pass

        menu:
            "Yes":
                $ ch3_repeat_count1 += 1
                show ch_3_in_1 at truecenter
                pause 15.0
                hide ch_3_in_1
            "No":  
                show adrian smiling
                a "BadMUstard showed me how to do this, {size=+10}he might be a {b}1d10t{/b}{/size}."
                jump chapter_3_linked_list_insertion2

    
label chapter_3_linked_list_insertion2:
    a "Now lets talk about {color=#00FF00}Inserting items at the end{/color} of the linked list."
    a "This is a bit more complex, but still manageable."

    image ch_3_in_2 = Movie(play="images/videos/chapter_3_Insertion_2.webm", loop=False)
    window hide
    show ch_3_in_2 at truecenter
    with fade
    pause 13.0
    hide ch_3_in_2
    window auto

    a "That was how we insert at the end of the linked list."

label chapter_3_linked_list_remove:
    a "Now lets talk about {color=#FF0000}Removing items{/color} from the linked list."
    a "It is quite simple"

    image ch_3_del = Movie(play="images/videos/chapter_3_deletion.webm", loop=False)

    window hide
    show ch_3_del at truecenter
    with fade
    pause 13.0
    hide ch_3_del
    window auto

    a "And that is how we remove items from the linked list."
    jump ch3_quiz2

label ch3_quiz2:
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0

    a "Now lets test your knowledge"
 

    show adrian explaining
    a "Question 1: What is the time complexity of inserting an item at the beginning of a singly linked list?"
    menu:
        "O(n)":
            a "Incorrect. Inserting at the beginning does not require traversal."
        "O(log n)":
            a "Incorrect. Linked lists do not have logarithmic operations."
        "O(1)":
            a "Correct! Inserting at the beginning is a constant time operation."
            $ chapter_3_test += 1
        "O(n^2)":
            a "Incorrect. That's way too slow!"

        a "Question 2: What must you update when removing the first node in a singly linked list?"
    menu:
        "The tail pointer":
            a "Incorrect. The tail pointer is only updated if the list becomes empty."
        "No pointers":
            a "Incorrect. You must update the head pointer."
        "All pointers":
            a "Incorrect. Only the head pointer needs updating."
        "The head pointer":
            a "Correct! The head pointer must point to the next node."
            $ chapter_3_test += 1

        a "Question 3: What is the time complexity of inserting an item at the end of a singly linked list if you do NOT have a tail pointer?"
    menu:
        "O(n^2)":
            a "Incorrect. That's much too slow."
        "O(1)":
            a "Incorrect. You need to traverse the list."
        "O(log n)":
            a "Incorrect. Linked lists do not have logarithmic operations."
        "O(n)":
            a "Correct! You need to traverse the list to find the end."
            $ chapter_3_test += 1

        a "Question 4: What happens if you remove a node from the middle of a singly linked list?"
    menu:
        "No updates needed":
            a "Incorrect. You must update the previous node's pointer."
        "You must update the previous node's pointer":
            a "Correct! The previous node's pointer must skip the removed node."
            $ chapter_3_test += 1
        "You must update all nodes":
            a "Incorrect. Only the previous node's pointer needs updating."
        "You must update the tail pointer":
            a "Incorrect, unless you remove the last node."

        a "Question 5: Which operation is generally faster in a singly linked list: insertion at the beginning or at the end (without a tail pointer)?"
    menu:
        "Insertion at the end":
            a "Incorrect. Insertion at the end is slower without a tail pointer."
        "Both are the same":
            a "Incorrect. They have different time complexities."
        "Insertion at the beginning":
            a "Correct! Insertion at the beginning is O(1), while at the end is O(n) without a tail pointer."
            $ chapter_3_test += 1
        "Neither":
            a "Incorrect. One is faster than the other."

    show adrian smiling
    if persistent.chapter_3 == True:
        a "Would you like to continue with the next quiz?"
        menu:
            "Yes":
                jump ch3_restart
            "No":
                pass
    jump chapter_3_problems_with_linked_list



label chapter_3_problems_with_linked_list:
    play music "bgm/city-high-life.mp3" fadein 1.0
    show screen chapter_3_Problems
    with fade
    pause 1.0
    hide screen chapter_3_Problems

    a "Now lets talk about {b}Problems with Linked Lists{/b}"
    show adrian explaining
    a "In a singly linked list, each node points only to the next one."
    a "For example, you can easily move from node 4 to node 25 by following the pointers."
    a "But you can't go from node 25 back to node 4, because the references only go forward!"
    a "{color=#FFD700}Traversal is one-way: forward only!{/color}"
    a "To go backwards, you'd need a different structure, like a doubly linked list."

    show screen linked_list_representation
    screen linked_list_representation:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 40
            ypadding 40
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5
                text "Linked List Representation" size 50 color "#FFFFFF" outlines [(3, "#000000", 0, 0)]
                hbox:
                    spacing 30
                    for i in range(1, 5):
                        vbox:
                            spacing 5
                            text "Node [i]" size 35 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                            text "Data" size 25 color "#00FF00" outlines [(1, "#000000", 0, 0)]
                            text "→" size 30 color "#FFD700" outlines [(1, "#000000", 0, 0)]
                text "Each node points to the next, forming a chain." size 30 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
    pause 3.0
    hide screen linked_list_representation

    show adrian normal
    a "This means you can't easily access the previous node."
    a "Which Takes us to the next problem: {b}Memory Usage{/b}"

    a "Here are the Difference between an Array and a Linked List"

    screen array_vs_linked_list:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 40
            ypadding 40
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5
                textbutton "Search":
                    text_color "#00BFFF"
                    text_hover_color "#FFD700"
                    action ShowMenu("search_info")
                    text_size 28
                    xalign 0.5
                textbutton "Deletion":
                    text_color "#00BFFF"
                    text_hover_color "#FFD700"
                    action ShowMenu("deletion_info")
                    text_size 28
                    xalign 0.5
                textbutton "Memory Management":
                    text_color "#00BFFF"
                    text_hover_color "#FFD700"
                    action ShowMenu("memory_info")
                    text_size 28
                    xalign 0.5

    screen search_info:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 40
            ypadding 40
            vbox:
                spacing 20
                text "Search" size 40 color "#FFFFFF" outlines [(3, "#000000", 0, 0)]
                hbox:
                    spacing 80
                    vbox:
                        spacing 15
                        xalign 0.5
                        yalign 0.5
                        text "{b}ArrayList{/b}" size 32 color "#00FF00" outlines [(2, "#000000", 0, 0)]
                        text "Search is fast (O(1))" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "Uses index-based system" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "Allows random access" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "Better for search operations" size 28 color "#FFD700" outlines [(2, "#000000", 0, 0)]
                    vbox:
                        spacing 15
                        xalign 0.5
                        yalign 0.5
                        text "{b}LinkedList{/b}" size 32 color "#00FF00" outlines [(2, "#000000", 0, 0)]
                        text "Search is slow (O(N))" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "Requires traversal" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "No random access" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "Slower for search operations" size 28 color "#FFD700" outlines [(2, "#000000", 0, 0)]
                        
        imagebutton:
            xalign 1.0
            yalign 0.0
            xoffset -30
            yoffset 30
            auto "UI/btn_back_%s.png"
            action Return()


    screen deletion_info:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 80
            ypadding 50
            vbox:
                spacing 20
                text "{size=+20}{b}Deletion" size 40 color "#FFFFFF" outlines [(3, "#000000", 0, 0)]
                hbox:
                    spacing 80
                    vbox:
                        spacing 15
                        xalign 0.5
                        yalign 0.5
                        text "{b}ArrayList{/b}" size 32 color "#00FF00" outlines [(2, "#000000", 0, 0)]
                        text "Removing first element: O(N)" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "Removing last element: O(1)" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "Often requires reconstructing array" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "LinkedList is better for removal at beginning" size 28 color "#FFD700" outlines [(2, "#000000", 0, 0)]
                    vbox:
                        spacing 15
                        xalign 0.5
                        yalign 0.5
                        text "{b}LinkedList{/b}" size 32 color "#00FF00" outlines [(2, "#000000", 0, 0)]
                        text "Remove at beginning: O(1)" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "Operates with pointers" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "Removal only requires pointer change" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                        text "Very fast for this operation" size 28 color "#FFD700" outlines [(2, "#000000", 0, 0)]

                    imagebutton:
                        xalign 1.0
                        yalign 0.0
                        xoffset -30
                        yoffset 30
                        auto "UI/btn_back_%s.png"
                        action Return()

    screen memory_info:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 80
            ypadding 50
            vbox:
                spacing 20
                text "{size=+20}{b}Memory Management" size 40 color "#FFFFFF" outlines [(3, "#000000", 0, 0)]
                hbox:
                    spacing 80
                    vbox:
                        spacing 15

                        hbox:
                            spacing 80
                            vbox:
                                spacing 10
                                xalign 0.5
                                yalign 0.5
                                text "{b}ArrayList{/b}" size 32 color "#00FF00" outlines [(2, "#000000", 0, 0)]
                                text "No extra memory needed" size 24 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                                text "Memory is contiguous" size 24 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                                text "Arrays are memory friendly" size 24 color "#FFD700" outlines [(2, "#000000", 0, 0)]
                            vbox:
                                spacing 10
                                xalign 0.5
                                yalign 0.5
                                text "{b}LinkedList{/b}" size 32 color "#00FF00" outlines [(2, "#000000", 0, 0)]
                                text "Needs extra memory for pointers" size 24 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                                text "Memory is scattered" size 24 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                                text "Uses more memory" size 24 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                                text "Less memory friendly" size 24 color "#FFD700" outlines [(2, "#000000", 0, 0)]

                    imagebutton:
                        xalign 1.0
                        yalign 0.0
                        xoffset -30
                        yoffset -30
                        auto "UI/btn_back_%s.png"
                        action Return()


    show screen array_vs_linked_list
    a "Just press the button to see the differences"
    a "Please take your time to read the differences"
    hide screen array_vs_linked_list
    $ renpy.force_autosave()
    show adrian smiling
    a "Now that you know the problems with Linked Lists, lets move on to the-"

    play sound "sfx/bell.mp3"
    a "You hear that? Its time for some questions. Buckle Up Buckeroo"
    jump ch3_restart

label ch3_restart:    
    a "Your score is [chapter_3_test]"
    a "Lets see how well you do in the {size=+20}CHAPTER QUIZ"
    if chapter_3_test <= 4:
        show adrian blush
        jump chapter_3_quiz_easy
    elif chapter_3_test <= 7:
        show adrian smiling
        jump chapter_3_quiz_medium
    else:
        show adrian happy
        jump chapter_3_quiz_hard

label chapter_3_quiz_easy:
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 0.5
    $ chapter_3_score = 0

    show adrian smiling at center
    a "Welcome to the {b}Quiz!{/b}Let's see how much you've learned."

    a "What is a Node?"
    menu:
        "A Type of Linked List":
            a "Incorrect, A Node is not a type of Linked List"
        "A Container for Data":
            a "Correct"
            $ chapter_3_score += 1
        "A Type of Algorithm":
            a "Incorrect, A Node is not an Algorithm"
        "A Type of Data Structure":
            a "Incorrect, A Node is not a type of Data Structure"

    a "Next Question"
    show adrian smiling
    a "What is the purpose of a Pointer in a Linked List?"
    menu:
        "To Store Data":
            a "Incorrect, A Pointer does not store data"
        "To Reference the Next Node":
            a "Correct"
            $ chapter_3_score += 1
        "To Store the Previous Node":
            a "Incorrect, A Pointer does not store the Previous Node"
        "To Store the Index":
            a "Incorrect, A Pointer does not store the Index"
    
    a "Next Question"
    a "What is the main advantage of using a Linked List over an array?"
    menu:
        "Dynamic Size":
            a "Correct! Linked Lists can grow and shrink dynamically."
            $ chapter_3_score += 1
        "Simpler Structure":
            a "Incorrect, Linked Lists are more complex than arrays."
        "Less Memory Usage":
            a "Incorrect, Linked Lists often use more memory due to pointers."
        "Faster Access":
            a "Incorrect, Linked Lists do not have faster access than arrays."

    show adrian explaining
    a "Next Question"
    a "Which of the following is a disadvantage of Linked Lists?"
    menu:
        "Easy to Reverse Traverse":
            a "Incorrect, singly Linked Lists are hard to reverse traverse."
        "Waste Memory":
            a "Correct! Linked Lists use extra memory for pointers."
            $ chapter_3_score += 1
        "Fixed Size":
            a "Incorrect, Linked Lists are not fixed in size."
        "Fast Random Access":
            a "Incorrect, Linked Lists do not support fast random access."

    show adrian smug
    a "Next Question"
    a "What does each node in a Linked List contain?"

    menu:
        "Only Data":
            show adrian confused
            a "Incorrect, nodes also contain a pointer."
        "Data and Pointer":
            show adrian happy
            a "Correct! Each node contains data and a pointer to the next node."
            $ chapter_3_score += 1
        "Index and Data":
            show adrian thinking
            a "Incorrect, nodes do not store their index."
        "Only Pointer":
            show adrian confused
            a "Incorrect, nodes also contain data."

    show adrian explaining
    a "Question: What is the time complexity of inserting an item at the beginning of a singly linked list?"
    menu:
        "O(n)":
            show adrian normal
            a "Incorrect. Inserting at the beginning does not require traversal."
        "O(log n)":
            show adrian normal
            a "Incorrect. Linked lists do not have logarithmic operations."
        "O(1)":
            show adrian happy
            a "Correct! Inserting at the beginning is a constant time operation."
            $ chapter_3_score += 1
        "O(n^2)":
            show adrian surprised
            a "Incorrect. That's way too slow!"

    show adrian explaining
    a "Question : What must you update when removing the first node in a singly linked list?"
    menu:
        "The tail pointer":
            show adrian normal
            a "Incorrect. The tail pointer is only updated if the list becomes empty."
        "No pointers":
            show adrian confused
            a "Incorrect. You must update the head pointer."
        "All pointers":
            show adrian thinking
            a "Incorrect. Only the head pointer needs updating."
        "The head pointer":
            show adrian happy
            a "Correct! The head pointer must point to the next node."
            $ chapter_3_score += 1

    show adrian explaining
    a "Question : What is the time complexity of inserting an item at the end of a singly linked list if you do NOT have a tail pointer?"
    menu:
        "O(n^2)":
            show adrian surprised
            a "Incorrect. That's much too slow."
        "O(1)":
            show adrian confused
            a "Incorrect. You need to traverse the list."
        "O(log n)":
            show adrian normal
            a "Incorrect. Linked lists do not have logarithmic operations."
        "O(n)":
            show adrian happy
            a "Correct! You need to traverse the list to find the end."
            $ chapter_3_score += 1

    show adrian explaining
    a "Question : What happens if you remove a node from the middle of a singly linked list?"
    menu:
        "No updates needed":
            show adrian confused
            a "Incorrect. You must update the previous node's pointer."
        "You must update the previous node's pointer":
            show adrian happy
            a "Correct! The previous node's pointer must skip the removed node."
            $ chapter_3_score += 1
        "You must update all nodes":
            show adrian thinking
            a "Incorrect. Only the previous node's pointer needs updating."
        "You must update the tail pointer":
            show adrian normal
            a "Incorrect, unless you remove the last node."

    show adrian explaining
    a "Question : Which operation is generally faster in a singly linked list: insertion at the beginning or at the end (without a tail pointer)?"
    menu:
        "Insertion at the end":
            show adrian normal
            a "Incorrect. Insertion at the end is slower without a tail pointer."
        "Both are the same":
            show adrian confused
            a "Incorrect. They have different time complexities."
        "Insertion at the beginning":
            show adrian happy
            a "Correct! Insertion at the beginning is O(1), while at the end is O(n) without a tail pointer."
            $ chapter_3_score += 1
        "Neither":
            show adrian thinking
            a "Incorrect. One is faster than the other."
    
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Your quiz score is: [chapter_3_score]"


label chapter_3_quiz_medium:
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 0.5
    $ chapter_3_score = 0

    show adrian smiling at center
    a "Welcome to the {b}Quiz!{/b}Let's see how much you've learned."

    a "What is a Node?"
    menu:
        "A Type of Linked List":
            a "Incorrect, A Node is not a type of Linked List"
        "A Container for Data":
            a "Correct"
            $ chapter_3_score += 1
        "A Type of Algorithm":
            a "Incorrect, A Node is not an Algorithm"
        "A Type of Data Structure":
            a "Incorrect, A Node is not a type of Data Structure"

    a "Next Question"
    show adrian smiling
    a "What is the purpose of a Pointer in a Linked List?"
    menu:
        "To Store Data":
            a "Incorrect, A Pointer does not store data"
        "To Reference the Next Node":
            a "Correct"
            $ chapter_3_score += 1
        "To Store the Previous Node":
            a "Incorrect, A Pointer does not store the Previous Node"
        "To Store the Index":
            a "Incorrect, A Pointer does not store the Index"
    
    a "Next Question"
    a "What is the main advantage of using a Linked List over an array?"
    menu:
        "Dynamic Size":
            a "Correct! Linked Lists can grow and shrink dynamically."
            $ chapter_3_score += 1
        "Simpler Structure":
            a "Incorrect, Linked Lists are more complex than arrays."
        "Less Memory Usage":
            a "Incorrect, Linked Lists often use more memory due to pointers."
        "Faster Access":
            a "Incorrect, Linked Lists do not have faster access than arrays."

    show adrian explaining
    a "Next Question"
    a "Which of the following is a disadvantage of Linked Lists?"
    menu:
        "Easy to Reverse Traverse":
            a "Incorrect, singly Linked Lists are hard to reverse traverse."
        "Waste Memory":
            a "Correct! Linked Lists use extra memory for pointers."
            $ chapter_3_score += 1
        "Fixed Size":
            a "Incorrect, Linked Lists are not fixed in size."
        "Fast Random Access":
            a "Incorrect, Linked Lists do not support fast random access."

    show adrian smug
    a "Next Question"
    a "What does each node in a Linked List contain?"

    menu:
        "Only Data":
            show adrian confused
            a "Incorrect, nodes also contain a pointer."
        "Data and Pointer":
            show adrian happy
            a "Correct! Each node contains data and a pointer to the next node."
            $ chapter_3_score += 1
        "Index and Data":
            show adrian thinking
            a "Incorrect, nodes do not store their index."
        "Only Pointer":
            show adrian confused
            a "Incorrect, nodes also contain data."

    show adrian explaining
    a "Question: What is the time complexity of inserting an item at the beginning of a singly linked list?"
    menu:
        "O(n)":
            show adrian normal
            a "Incorrect. Inserting at the beginning does not require traversal."
        "O(log n)":
            show adrian normal
            a "Incorrect. Linked lists do not have logarithmic operations."
        "O(1)":
            show adrian happy
            a "Correct! Inserting at the beginning is a constant time operation."
            $ chapter_3_score += 1
        "O(n^2)":
            show adrian surprised
            a "Incorrect. That's way too slow!"

    show adrian explaining
    a "Question : What must you update when removing the first node in a singly linked list?"
    menu:
        "The tail pointer":
            show adrian normal
            a "Incorrect. The tail pointer is only updated if the list becomes empty."
        "No pointers":
            show adrian confused
            a "Incorrect. You must update the head pointer."
        "All pointers":
            show adrian thinking
            a "Incorrect. Only the head pointer needs updating."
        "The head pointer":
            show adrian happy
            a "Correct! The head pointer must point to the next node."
            $ chapter_3_score += 1

    show adrian explaining
    a "Question : What is the time complexity of inserting an item at the end of a singly linked list if you do NOT have a tail pointer?"
    menu:
        "O(n^2)":
            show adrian surprised
            a "Incorrect. That's much too slow."
        "O(1)":
            show adrian confused
            a "Incorrect. You need to traverse the list."
        "O(log n)":
            show adrian normal
            a "Incorrect. Linked lists do not have logarithmic operations."
        "O(n)":
            show adrian happy
            a "Correct! You need to traverse the list to find the end."
            $ chapter_3_score += 1

    show adrian explaining
    a "Question : What happens if you remove a node from the middle of a singly linked list?"
    menu:
        "No updates needed":
            show adrian confused
            a "Incorrect. You must update the previous node's pointer."
        "You must update the previous node's pointer":
            show adrian happy
            a "Correct! The previous node's pointer must skip the removed node."
            $ chapter_3_score += 1
        "You must update all nodes":
            show adrian thinking
            a "Incorrect. Only the previous node's pointer needs updating."
        "You must update the tail pointer":
            show adrian normal
            a "Incorrect, unless you remove the last node."

    show adrian explaining
    a "Question : Which operation is generally faster in a singly linked list: insertion at the beginning or at the end (without a tail pointer)?"
    menu:
        "Insertion at the end":
            show adrian normal
            a "Incorrect. Insertion at the end is slower without a tail pointer."
        "Both are the same":
            show adrian confused
            a "Incorrect. They have different time complexities."
        "Insertion at the beginning":
            show adrian happy
            a "Correct! Insertion at the beginning is O(1), while at the end is O(n) without a tail pointer."
            $ chapter_3_score += 1
        "Neither":
            show adrian thinking
            a "Incorrect. One is faster than the other."



        
    screen linked_list_quiz1:
        frame:
            xalign 0.2
            yalign 0.3
            xpadding 30
            ypadding 30
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Linked List Representation" size 40

                hbox:
                    spacing 20
                    vbox:
                        spacing 5
                        text "Node 1" size 30
                        text "Data 20" size 20 color "#00FF00"
                        text "→" size 25 color "#FFD700"

                        text "Node 2" size 30
                        text "Data 40" size 20 color "#00FF00"
                        text "→" size 25 color "#FFD700"

                        text "Node 3" size 30
                        text "Data 30" size 20 color "#00FF00"
                        text "→" size 25 color "#FFD700"

                        text "Node 4" size 30
                        text "Data -10" size 20 color "#00FF00"
                        text "→" size 25 color "#FFD700"

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
                        textbutton "Node 1" action [SetVariable("ch3_selected_node1", "Node 1"), Return()]
                        textbutton "Node 2" action [SetVariable("ch3_selected_node1", "Node 2"), Return()]
                        textbutton "Node 3" action [SetVariable("ch3_selected_node1", "Node 3"), Return()]
                        textbutton "Node 4" action [SetVariable("ch3_selected_node1", "Node 4"), Return()]

            
    show screen linked_list_quiz1
    a "Which node you have to go through last before arriving at Value -10?"
    hide screen linked_list_quiz1
    if ch3_selected_node1 is None:
        a "Please Select an Answer"
        return

    elif ch3_selected_node1 == "Node 3":
        $ chapter_3_score += 1
        a "Correct! Node 3 contains the value 30."
        pass
    else:
        a "Oops! That's not the right node."
        pass

    screen linked_list_quiz2:
        frame:
            xalign 0.2
            yalign 0.3
            xpadding 30
            ypadding 30
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Linked List Representation" size 40

                hbox:
                    spacing 20
                    vbox:
                        spacing 5
                        text "Node A" size 30
                        text "Data 10" size 20 color "#00FF00"
                        text "→" size 25 color "#FFD700"

                        text "Node B" size 30
                        text "Data 99" size 20 color "#00FF00"
                        text "→" size 25 color "#FFD700"

                        text "Node C" size 30
                        text "Data 45" size 20 color "#00FF00"
                        text "→" size 25 color "#FFD700"

                        text "Node D" size 30
                        text "Data 0" size 20 color "#00FF00"
                        text "→" size 25 color "#FFD700"

        frame:
            xalign 0.2
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
                        textbutton "Node A" action [
                            SetVariable("ch3_selected_node2", "Node A"),
                            Return()
                        ]

                        textbutton "Node B" action [
                            SetVariable("ch3_selected_node2", "Node B"),
                            Return()
                        ]

                        textbutton "Node C" action [
                            SetVariable("ch3_selected_node2", "Node C"),
                            Return()
                        ]

                        textbutton "Node D" action [
                            SetVariable("ch3_selected_node2", "Node D"),
                            Return()
                        ]


    show screen linked_list_quiz2
    a "Which node contains the value 99?"
    hide screen linked_list_quiz2

    if ch3_selected_node2 is None:
        a "Please Select an Answer"
        return
    elif ch3_selected_node2 == "Node B":
        $ chapter_3_score += 1
        a "Correct! Node B contains the value 99."
        pass
    else:
        a "Oops! That's not the right node."
    
    
    screen linked_list_quiz3:
        frame:
            xalign 0.2
            yalign 0.3
            xpadding 30
            ypadding 30
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Linked List Representation" size 40

                hbox:
                    spacing 20
                    vbox:
                        spacing 5
                        text "Node W" size 30
                        text "Data 5" size 20 color "#00FF00"
                        text "→" size 25 color "#FFD700"

                        text "Node X" size 30
                        text "Data 15" size 20 color "#00FF00"
                        text "→" size 25 color "#FFD700"

                        text "Node Y" size 30
                        text "Data 25" size 20 color "#00FF00"
                        text "→" size 25 color "#FFD700"

                        text "Node Z" size 30
                        text "Data 35" size 20 color "#00FF00"
                        text "→" size 25 color "#FFD700"

        frame:
            xalign 0.2
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
                        spacing 10

                        textbutton "Node W" action [
                            SetVariable("ch3_selected_node3", "Node W"),
                            Return()
                        ]

                        textbutton "Node X" action [
                            SetVariable("ch3_selected_node3", "Node X"),
                            Return()
                        ]

                        textbutton "Node Y" action [
                            SetVariable("ch3_selected_node3", "Node Y"),
                            Return()
                        ]

                        textbutton "Node Z" action [
                            SetVariable("ch3_selected_node3", "Node Z"),
                            Return()
                        ]


    show screen linked_list_quiz3
    a "Which node comes immediately after Node X?"
    hide screen linked_list_quiz3


    if ch3_selected_node3 is None:
        a "Please Select an Answer"
        return
    elif ch3_selected_node3 == "Node Y":
        $ chapter_3_score += 1
        a "Correct! Node Y follows Node X."
        pass
    else:
        a "Oops! That's not the right node."
        pass


    screen linked_list_quiz4:
        frame:
            xalign 0.2
            yalign 0.3
            xpadding 30
            ypadding 30
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Linked List Representation" size 40

                hbox:
                    spacing 20
                    vbox:
                        spacing 5
                        text "Node M" size 30
                        text "Data 88" size 20 color "#00FF00"
                        text "→" size 25 color "#FFD700"

                        text "Node N" size 30
                        text "Data 42" size 20 color "#00FF00"
                        text "→" size 25 color "#FFD700"

                        text "Node O" size 30
                        text "Data 17" size 20 color "#00FF00"
                        text "→" size 25 color "#FFD700"

                        text "Node P" size 30
                        text "Data 3" size 20 color "#00FF00"
                        text "→" size 25 color "#FFD700"

        frame:
            xalign 0.2
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
                        spacing 10

                        textbutton "Node M" action [
                            SetVariable("ch3_selected_node4", "Node M"),
                            Return()
                        ]

                        textbutton "Node N" action [
                            SetVariable("ch3_selected_node4", "Node N"),
                            Return()
                        ]

                        textbutton "Node O" action [
                            SetVariable("ch3_selected_node4", "Node O"),
                            Return()
                        ]

                        textbutton "Node P" action [
                            SetVariable("ch3_selected_node4", "Node P"),
                            Return()
                        ]

    show screen linked_list_quiz4
    a "Which node contains the smallest value?"
    hide screen linked_list_quiz4


    if ch3_selected_node4 is None:
        a "Please Select an Answer"
        return
    elif ch3_selected_node4 == "Node P":
        $ chapter_3_score += 1
        a "Correct! Node P has the smallest value."
        pass
    else:
        a "Oops! That's not the right node."
        pass


    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Your quiz score is: [chapter_3_score]"
label chapter_3_quiz_hard:
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 0.5
    $ chapter_3_score = 0

    show adrian smiling at center
    a "Welcome to the {b}Quiz!{/b}Let's see how much you've learned."

    a "What is a Node?"
    menu:
        "A Type of Linked List":
            a "Incorrect, A Node is not a type of Linked List"
        "A Container for Data":
            a "Correct"
            $ chapter_3_score += 1
        "A Type of Algorithm":
            a "Incorrect, A Node is not an Algorithm"
        "A Type of Data Structure":
            a "Incorrect, A Node is not a type of Data Structure"

    a "Next Question"
    show adrian smiling
    a "What is the purpose of a Pointer in a Linked List?"
    menu:
        "To Store Data":
            a "Incorrect, A Pointer does not store data"
        "To Reference the Next Node":
            a "Correct"
            $ chapter_3_score += 1
        "To Store the Previous Node":
            a "Incorrect, A Pointer does not store the Previous Node"
        "To Store the Index":
            a "Incorrect, A Pointer does not store the Index"
    
    a "Next Question"
    a "What is the main advantage of using a Linked List over an array?"
    menu:
        "Dynamic Size":
            a "Correct! Linked Lists can grow and shrink dynamically."
            $ chapter_3_score += 1
        "Simpler Structure":
            a "Incorrect, Linked Lists are more complex than arrays."
        "Less Memory Usage":
            a "Incorrect, Linked Lists often use more memory due to pointers."
        "Faster Access":
            a "Incorrect, Linked Lists do not have faster access than arrays."

    show adrian explaining
    a "Next Question"
    a "Which of the following is a disadvantage of Linked Lists?"
    menu:
        "Easy to Reverse Traverse":
            a "Incorrect, singly Linked Lists are hard to reverse traverse."
        "Waste Memory":
            a "Correct! Linked Lists use extra memory for pointers."
            $ chapter_3_score += 1
        "Fixed Size":
            a "Incorrect, Linked Lists are not fixed in size."
        "Fast Random Access":
            a "Incorrect, Linked Lists do not support fast random access."

    show adrian smug
    a "Next Question"
    a "What does each node in a Linked List contain?"

    menu:
        "Only Data":
            show adrian confused
            a "Incorrect, nodes also contain a pointer."
        "Data and Pointer":
            show adrian happy
            a "Correct! Each node contains data and a pointer to the next node."
            $ chapter_3_score += 1
        "Index and Data":
            show adrian thinking
            a "Incorrect, nodes do not store their index."
        "Only Pointer":
            show adrian confused
            a "Incorrect, nodes also contain data."

    show adrian explaining
    a "Question: What is the time complexity of inserting an item at the beginning of a singly linked list?"
    menu:
        "O(n)":
            show adrian normal
            a "Incorrect. Inserting at the beginning does not require traversal."
        "O(log n)":
            show adrian normal
            a "Incorrect. Linked lists do not have logarithmic operations."
        "O(1)":
            show adrian happy
            a "Correct! Inserting at the beginning is a constant time operation."
            $ chapter_3_score += 1
        "O(n^2)":
            show adrian surprised
            a "Incorrect. That's way too slow!"

    show adrian explaining
    a "Question : What must you update when removing the first node in a singly linked list?"
    menu:
        "The tail pointer":
            show adrian normal
            a "Incorrect. The tail pointer is only updated if the list becomes empty."
        "No pointers":
            show adrian confused
            a "Incorrect. You must update the head pointer."
        "All pointers":
            show adrian thinking
            a "Incorrect. Only the head pointer needs updating."
        "The head pointer":
            show adrian happy
            a "Correct! The head pointer must point to the next node."
            $ chapter_3_score += 1

    show adrian explaining
    a "Question : What is the time complexity of inserting an item at the end of a singly linked list if you do NOT have a tail pointer?"
    menu:
        "O(n^2)":
            show adrian surprised
            a "Incorrect. That's much too slow."
        "O(1)":
            show adrian confused
            a "Incorrect. You need to traverse the list."
        "O(log n)":
            show adrian normal
            a "Incorrect. Linked lists do not have logarithmic operations."
        "O(n)":
            show adrian happy
            a "Correct! You need to traverse the list to find the end."
            $ chapter_3_score += 1

    show adrian explaining
    a "Question : What happens if you remove a node from the middle of a singly linked list?"
    menu:
        "No updates needed":
            show adrian confused
            a "Incorrect. You must update the previous node's pointer."
        "You must update the previous node's pointer":
            show adrian happy
            a "Correct! The previous node's pointer must skip the removed node."
            $ chapter_3_score += 1
        "You must update all nodes":
            show adrian thinking
            a "Incorrect. Only the previous node's pointer needs updating."
        "You must update the tail pointer":
            show adrian normal
            a "Incorrect, unless you remove the last node."

    show adrian explaining
    a "Question : Which operation is generally faster in a singly linked list: insertion at the beginning or at the end (without a tail pointer)?"
    menu:
        "Insertion at the end":
            show adrian normal
            a "Incorrect. Insertion at the end is slower without a tail pointer."
        "Both are the same":
            show adrian confused
            a "Incorrect. They have different time complexities."
        "Insertion at the beginning":
            show adrian happy
            a "Correct! Insertion at the beginning is O(1), while at the end is O(n) without a tail pointer."
            $ chapter_3_score += 1
        "Neither":
            show adrian thinking
            a "Incorrect. One is faster than the other."



        
    screen linked_list_quiz1:
        frame:
            xalign 0.2
            yalign 0.3
            xpadding 30
            ypadding 30
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Linked List Representation" size 40

                hbox:
                    spacing 20
                    vbox:
                        spacing 5
                        text "Node 1" size 30
                        text "Data 20" size 20 color "#00FF00"
                        text "→" size 25 color "#FFD700"

                        text "Node 2" size 30
                        text "Data 40" size 20 color "#00FF00"
                        text "→" size 25 color "#FFD700"

                        text "Node 3" size 30
                        text "Data 30" size 20 color "#00FF00"
                        text "→" size 25 color "#FFD700"

                        text "Node 4" size 30
                        text "Data -10" size 20 color "#00FF00"
                        text "→" size 25 color "#FFD700"

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
                        textbutton "Node 1" action [SetVariable("ch3_selected_node1", "Node 1"), Return()]
                        textbutton "Node 2" action [SetVariable("ch3_selected_node1", "Node 2"), Return()]
                        textbutton "Node 3" action [SetVariable("ch3_selected_node1", "Node 3"), Return()]
                        textbutton "Node 4" action [SetVariable("ch3_selected_node1", "Node 4"), Return()]

            
    show screen linked_list_quiz1
    a "Which node you have to go through last before arriving at Value -10?"
    hide screen linked_list_quiz1

    if ch3_selected_node1 is None:
        a "Please Select an Answer"
        return
    elif ch3_selected_node1 == "Node 3":
        $ chapter_3_score += 1
        show adrian happy
        a "Correct! Node 3 contains the value 30."
        pass
    else:
        a "Oops! That's not the right node."
        pass

    screen linked_list_quiz2:
        frame:
            xalign 0.2
            yalign 0.3
            xpadding 30
            ypadding 30
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Linked List Representation" size 40

                hbox:
                    spacing 20
                    vbox:
                        spacing 5
                        text "Node A" size 30
                        text "Data 10" size 20 color "#00FF00"
                        text "→" size 25 color "#FFD700"

                        text "Node B" size 30
                        text "Data 99" size 20 color "#00FF00"
                        text "→" size 25 color "#FFD700"

                        text "Node C" size 30
                        text "Data 45" size 20 color "#00FF00"
                        text "→" size 25 color "#FFD700"

                        text "Node D" size 30
                        text "Data 0" size 20 color "#00FF00"
                        text "→" size 25 color "#FFD700"

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
                        textbutton "Node A" action [
                            SetVariable("ch3_selected_node2", "Node A"),
                            Return()
                        ]

                        textbutton "Node B" action [
                            SetVariable("ch3_selected_node2", "Node B"),
                            Return()
                        ]

                        textbutton "Node C" action [
                            SetVariable("ch3_selected_node2", "Node C"),
                            Return()
                        ]

                        textbutton "Node D" action [
                            SetVariable("ch3_selected_node2", "Node D"),
                            Return()
                        ]


    show screen linked_list_quiz2
    a "Which node contains the value 99?"
    hide screen linked_list_quiz2

    if ch3_selected_node2 is None:
        a "Please Select an Answer"
        return
    elif ch3_selected_node2 == "Node B":
        $ chapter_3_score += 1
        a "Correct! Node B contains the value 99."
        pass
    else:
        a "Oops! That's not the right node."
    
    
    screen linked_list_quiz3:
        frame:
            xalign 0.2
            yalign 0.3
            xpadding 30
            ypadding 30
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Linked List Representation" size 40

                hbox:
                    spacing 20
                    vbox:
                        spacing 5
                        text "Node W" size 30
                        text "Data 5" size 20 color "#00FF00"
                        text "→" size 25 color "#FFD700"

                        text "Node X" size 30
                        text "Data 15" size 20 color "#00FF00"
                        text "→" size 25 color "#FFD700"

                        text "Node Y" size 30
                        text "Data 25" size 20 color "#00FF00"
                        text "→" size 25 color "#FFD700"

                        text "Node Z" size 30
                        text "Data 35" size 20 color "#00FF00"
                        text "→" size 25 color "#FFD700"

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
                        spacing 10

                        textbutton "Node W" action [
                            SetVariable("ch3_selected_node3", "Node W"),
                            Return()
                        ]

                        textbutton "Node X" action [
                            SetVariable("ch3_selected_node3", "Node X"),
                            Return()
                        ]

                        textbutton "Node Y" action [
                            SetVariable("ch3_selected_node3", "Node Y"),
                            Return()
                        ]

                        textbutton "Node Z" action [
                            SetVariable("ch3_selected_node3", "Node Z"),
                            Return()
                        ]


    show screen linked_list_quiz3
    a "Which node comes immediately after Node X?"
    hide screen linked_list_quiz3

    if ch3_selected_node3 is None:
        a "Please Select an Answer"
        return
    elif ch3_selected_node3 == "Node Y":
        $ chapter_3_score += 1
        a "Correct! Node Y follows Node X."
        pass
    else:
        a "Oops! That's not the right node."
        pass


    screen linked_list_quiz4:
        frame:
            xalign 0.2
            yalign 0.3
            xpadding 30
            ypadding 30
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Linked List Representation" size 40

                hbox:
                    spacing 20
                    vbox:
                        spacing 5
                        text "Node M" size 30
                        text "Data 88" size 20 color "#00FF00"
                        text "→" size 25 color "#FFD700"

                        text "Node N" size 30
                        text "Data 42" size 20 color "#00FF00"
                        text "→" size 25 color "#FFD700"

                        text "Node O" size 30
                        text "Data 17" size 20 color "#00FF00"
                        text "→" size 25 color "#FFD700"

                        text "Node P" size 30
                        text "Data 3" size 20 color "#00FF00"
                        text "→" size 25 color "#FFD700"

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
                        spacing 10

                        textbutton "Node M" action [
                            SetVariable("ch3_selected_node4", "Node M"),
                            Return()
                        ]

                        textbutton "Node N" action [
                            SetVariable("ch3_selected_node4", "Node N"),
                            Return()
                        ]

                        textbutton "Node O" action [
                            SetVariable("ch3_selected_node4", "Node O"),
                            Return()
                        ]

                        textbutton "Node P" action [
                            SetVariable("ch3_selected_node4", "Node P"),
                            Return()
                        ]

    show screen linked_list_quiz4
    a "Which node contains the smallest value?"
    hide screen linked_list_quiz4

    if ch3_selected_node4 is None:
        a "Please Select an Answer"
        return
    elif ch3_selected_node4 == "Node P":
        $ chapter_3_score += 1
        a "Correct! Node P has the smallest value."
        pass
    else:
        a "Oops! That's not the right node."
        pass

    screen linked_list_quiz5:
        frame:
            xalign 0.2
            yalign 0.3
            xpadding 30
            ypadding 30
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Linked List Representation" size 40

                hbox:
                    spacing 20
                    vbox:
                        spacing 5

                        text "Node A" size 30
                        text "Data 105" size 20 color "#00FF00"
                        text "→" size 25 color "#FFD700"

                        text "Node B" size 30
                        text "Data 12" size 20 color "#00FF00"
                        text "→" size 25 color "#FFD700"

                        text "Node C" size 30
                        text "Data 67" size 20 color "#00FF00"
                        text "→" size 25 color "#FFD700"

                        text "Node D" size 30
                        text "Data 88" size 20 color "#00FF00"
                        text "→" size 25 color "#FFD700"

                        text "Node E" size 30
                        text "Data 33" size 20 color "#00FF00"
                        text "→" size 25 color "#FFD700"

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
                        spacing 10
                        textbutton "Node A" action [SetVariable("ch3_selected_node5", "Node A"), Return()]
                        textbutton "Node B" action [SetVariable("ch3_selected_node5", "Node B"), Return()]
                        textbutton "Node C" action [SetVariable("ch3_selected_node5", "Node C"), Return()]
                        textbutton "Node D" action [SetVariable("ch3_selected_node5", "Node D"), Return()]
                        textbutton "Node E" action [SetVariable("ch3_selected_node5", "Node E"), Return()]


    show screen linked_list_quiz5
    a "Which node contains the **second smallest** value?"
    hide screen linked_list_quiz5


    if ch3_selected_node5 is None:
        a "Please Select an Answer"
        return
    elif ch3_selected_node5 == "Node E":
        $ chapter_3_score += 1
        a "Correct! Node E has the second smallest value after Node B."
    else:
        a "Not quite. Remember to compare all values carefully."

        pass

    screen linked_list_quiz6:
        frame:
            xalign 0.2
            yalign 0.3
            xpadding 30
            ypadding 30
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Linked List Representation" size 40

                hbox:
                    spacing 20
                    vbox:
                        spacing 5
                        text "Node A" size 30
                        text "→" size 25
                        text "Node B" size 30
                        text "→" size 25
                        text "Node C" size 30
                        text "→" size 25
                        text "Node D" size 30
                        text "→" size 25
                        text "Node E" size 30

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
                        spacing 10
                        textbutton "Node A" action [SetVariable("ch3_selected_node6", "Node A"), Return()]
                        textbutton "Node B" action [SetVariable("ch3_selected_node6", "Node B"), Return()]
                        textbutton "Node D" action [SetVariable("ch3_selected_node6", "Node D"), Return()]
                        textbutton "Node E" action [SetVariable("ch3_selected_node6", "Node E"), Return()]

    show screen linked_list_quiz6
    a "Which node comes directly after Node C?"
    hide screen linked_list_quiz6

    if ch3_selected_node6 is None:
        a "Please Select an Answer"
        return
    elif ch3_selected_node6 == "Node D":
        $ chapter_3_score += 1
        a "Correct! Node D follows Node C."
    else:
        a "Incorrect. Trace the arrows carefully."

    screen linked_list_quiz7:
        frame:
            xalign 0.2
            yalign 0.3
            xpadding 30
            ypadding 30
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Linked List Representation" size 40

                hbox:
                    spacing 20
                    vbox:
                        spacing 5
                        text "Node F" size 30
                        text "Data 23" size 20
                        text "→" size 25
                        text "Node G" size 30
                        text "Data 91" size 20
                        text "→" size 25
                        text "Node H" size 30
                        text "Data 45" size 20
                        text "→" size 25
                        text "Node I" size 30
                        text "Data 67" size 20

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
                        spacing 10
                        textbutton "Node F" action [SetVariable("ch3_selected_node7", "Node F"), Return()]
                        textbutton "Node G" action [SetVariable("ch3_selected_node7", "Node G"), Return()]
                        textbutton "Node H" action [SetVariable("ch3_selected_node7", "Node H"), Return()]
                        textbutton "Node I" action [SetVariable("ch3_selected_node7", "Node I"), Return()]

    show screen linked_list_quiz7
    a "Which node contains the highest value?"
    hide screen linked_list_quiz7

    if ch3_selected_node7 is None:
        a "Please Select an Answer"
        return
    elif ch3_selected_node7 == "Node G":
        $ chapter_3_score += 1
        a "Correct! Node G has the highest value: 91."
    else:
        a "Not quite. Scan the data values carefully."

    screen linked_list_quiz8:
        frame:
            xalign 0.2
            yalign 0.3
            xpadding 30
            ypadding 30
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Linked List Representation" size 40

                hbox:
                    spacing 20
                    vbox:
                        spacing 5
                        text "Node F → Node G → Node H → Node I"

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
                        spacing 10
                        textbutton "Node F" action [SetVariable("ch3_selected_node8", "Node F"), Return()]
                        textbutton "Node G" action [SetVariable("ch3_selected_node8", "Node G"), Return()]
                        textbutton "Node H" action [SetVariable("ch3_selected_node8", "Node H"), Return()]
                        textbutton "Node I" action [SetVariable("ch3_selected_node8", "Node I"), Return()]

    show screen linked_list_quiz8
    a "If Node G points directly to Node I, which node is skipped?"
    hide screen linked_list_quiz8

    if ch3_selected_node8 is None:
        a "Please Select an Answer"
        return
    elif ch3_selected_node8 == "Node H":
        $ chapter_3_score += 1
        a "Correct! Node H is skipped in the new pointer structure."
    else:
        a "Incorrect. Think about the pointer redirection."

    screen linked_list_quiz9:
        frame:
            xalign 0.2
            yalign 0.3
            xpadding 30
            ypadding 30
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Linked List Representation" size 40

                hbox:
                    spacing 20
                    vbox:
                        spacing 5
                        text "Node J → Node K → Node L → Node M → Node N"

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
                        spacing 10
                        textbutton "Node J" action [SetVariable("ch3_selected_node9", "Node J"), Return()]
                        textbutton "Node K" action [SetVariable("ch3_selected_node9", "Node K"), Return()]
                        textbutton "Node L" action [SetVariable("ch3_selected_node9", "Node L"), Return()]
                        textbutton "Node M" action [SetVariable("ch3_selected_node9", "Node M"), Return()]
                        textbutton "Node N" action [SetVariable("ch3_selected_node9", "Node N"), Return()]

    show screen linked_list_quiz9
    a "Which node is the third in the sequence?"
    hide screen linked_list_quiz9

    if ch3_selected_node9 is None:
        a "Please Select an Answer"
        return
    elif ch3_selected_node9 == "Node L":
        $ chapter_3_score += 1
        a "Correct! Node L is third in the linked list."
    else:
        a "Nope. Count the arrows carefully."

    screen linked_list_quiz10:
        frame:
            xalign 0.2
            yalign 0.3
            xpadding 30
            ypadding 30
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5

                text "Linked List Representation" size 40

                hbox:
                    spacing 20
                    vbox:
                        spacing 5
                        text "Node A → Node B → Node C → Node D → Node E"

                        text "Pointer override: Node A → Node C → Node E"

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
                        spacing 10
                        textbutton "Node B" action [SetVariable("ch3_selected_node10", "Node B"), Return()]
                        textbutton "Node C" action [SetVariable("ch3_selected_node10", "Node C"), Return()]
                        textbutton "Node D" action [SetVariable("ch3_selected_node10", "Node D"), Return()]
                        textbutton "Node E" action [SetVariable("ch3_selected_node10", "Node E"), Return()]

    show screen linked_list_quiz10
    a "If Node A points to Node C and Node C points to Node E, which node becomes unreachable?"
    hide screen linked_list_quiz10

    if ch3_selected_node10 is None:
        a "Please Select an Answer"
        return
    elif ch3_selected_node10 == "Node B":
        $ chapter_3_score += 1
        a "Correct! Node B is skipped entirely in the new structure."
    else:
        a "Incorrect. Consider which node is no longer part of the traversal."

    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Your quiz score is: [chapter_3_score]"

label chapter_3_ending:
    play music "bgm/city-high-life.mp3" fadein 1.0
    $ persistent.chapter_3 = True
    a "Would You like to test again?"
    menu:
        "Yes":
            jump ch3_restart
        "No":
            pass
    show adrian happy
    a "You have finished chapter 3. You can continue to Chapter 4!"
    jump menu
    





    




    


    
    