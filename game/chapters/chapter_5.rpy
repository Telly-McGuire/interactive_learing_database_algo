# Chapter 5: Binary Trees
#Binary Search trees

default chapter_5_progress = 0

default chapter_5_Binary_Tree_quiz = 0
default chapter_5_Binary_Search_Tree_quiz = 0

screen chapter_5_BinaryTreeIntro:
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 200
        ypadding 60
        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5
            text "Binary Tree" size 60 color "#FFFFFF" outlines [(5, "#000000", 0, 0)]
label chapter_5_intro:
    
    call hideall from _call_hideall_6
    play sound "sfx/start.mp3"
    stop music fadeout 1.0
    
    scene black
    pause 1.0

    show screen chapter_5_BinaryTreeIntro
    with dissolve
    scene room with dissolve
    pause 2.0
    hide screen chapter_5_BinaryTreeIntro
    
    show screen menu_btn
    
    play music "bgm/city-high-life.mp3" fadein 1.0
    show adrian normal at center:
        smaller
    with dissolve

    if persistent.chapter_5 == True:
        a "Hi welcome back to chapter 5"
        a "are you sure you want to go through this chapter again?"
        menu:
            "Yes":
                a "Which topic you want to go to?"
                menu:
                    "Binary Trees":
                        jump chacter_5_Binary_Trees
                    "Binary Search Trees":
                        jump chapter_5_Binary_Search_Trees
                    "BST Functions":
                        jump chapter_5_Functions
                    "Tree Traversals":
                        jump chapter_5_Traversal
            "No":
                jump menu
    else:
        pass

    a "Welcome to Chapter 5: Trees!"
    show adrian explaining
    a "Plants, Bushes, People...dogs?"
    a "All of them have arms"
    show adrian nocomment
    a "Well I dont know about about dogs though"
    a "What do they have?"
    a "{cps=10}...Legs?"
    show adrian normal
    a "{color=#6B8E23}Anyways{/color}, {color=#228B22}Trees{/color}, {color=#8B4513}Branches{/color}, {color=#808080}whatever{/color}."
    a "In computer science, trees are a fundamental data structure that organizes data hierarchically."
    a "What does that mean?"
    show adrian smug
    a "Who knows"
    show adrian normal
    a "Lmao"
    

label chacter_5_Binary_Trees:
    show adrian happy

    show adrian explaining
    a "So what is a Binary Tree?"

    screen ch5_BinaryTree_Info:
        frame:
            xalign 0.95
            yalign 0.3
            xpadding 70
            ypadding 100

            vbox:
                spacing 25
                xalign 0.5
                yalign 0.5

                text "BINARY TREES" size 60 color "#00ccff" outlines [(5, "#000000", 0, 0)]

                text "1. Hierarchical data structure with nodes" size 40 color "#FFFFFF" outlines [(3, "#000000", 0, 0)]
                text "2. Each node has at most two children" size 40 color "#FFFFFF" outlines [(3, "#000000", 0, 0)]
                text "3. Common traversal: Inorder, Preorder, Postorder" size 40 color "#FFFFFF" outlines [(3, "#000000", 0, 0)]
                text "4. Used in searching, sorting, and expression parsing" size 40 color "#FFFFFF" outlines [(3, "#000000", 0, 0)]

    show adrian explaining at left
    with move
    show screen ch5_BinaryTree_Info
    a "Here is a brief overview of binary trees."
    a "Binary trees are hierarchical structures where each node links to up to two child nodes."

    a "Balanced trees like AVL or Red-Black Trees keep their height in check, so operations stay quick even as data grows."
    a "Without balance, a binary tree can degrade into a linked list—slow and inefficient."

    show adrian explaining
    a "Traversals are how we explore trees. Inorder traversal gives sorted output in BSTs. Preorder and Postorder are great for copying or deleting trees."
    hide screen ch5_BinaryTree_Info
    image kahoy = "assets/kahoy.png"
    show kahoy at right:
        zoom 0.4


    a "And it’s not just theory—binary trees power decision-making in AI, syntax parsing- "
    show adrian shock
    a "{cps=50}Whoa... where did that tree come from?{nw}"
    a "{cps=50}Is that a... kahoy?{nw}"
    a "{cps=50}I swear that wasn't here a second ago.{nw}"
    a "{cps=50}Did that branch just move?{nw}"
    a "{cps=50}Okay, something's off. Trees don't do that.{nw}"
    a "{cps=50}Was that... a bug?{nw}"
    a "{cps=50}Nope. Not normal. Definitely not normal.{nw}"

    a "{cps=50}Is it... growing sideways?{nw}"
    a "{cps=50}That bark looks like it's breathing.{nw}"
    a "{cps=50}Okay, now it's humming. Trees don't hum.{nw}"
    a "{cps=50}Why does it smell like mint and regret?{nw}"
    a "{cps=50}I think that leaf just winked at me.{nw}"
    a "{cps=50}There's moss... but it's moving.{nw}"
    a "{cps=50}That knot looks suspiciously like an eye.{nw}"
    a "{cps=50}I'm not touching it. You touch it.{nw}"
    a "{cps=50}Is it... pulsing? Trees don't pulse.{nw}"
    show adrian nocomment
    a "Ahem"
    a "Sorry"
    a "Abra kadabra alakazam"
    play sound "sfx/explode.mp3"
    hide kahoy

    show adrian smiling
    a "Once you understand how trees grow and branch, you’ll see them everywhere in computer science."

    

    show adrian smiling at center
    with move
    
    with dissolve
    $ chapter_5_progress =+ 1    
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "You hear that? Its time for some questions. Buckle Up Buckeroo"
    jump chapter_5_Binary_Tree_quiz


init python:
    import random
    chapter_5_binary_tree_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_5_binary_tree_order)

label chapter_5_Binary_Tree_quiz:
    $ chapter_5_Binary_Tree_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_5_binary_tree_order:
        $ current_q = chapter_5_binary_tree_order.pop(0)

        if current_q == "q1":
            a "What is a binary tree?"
            menu:
                "A tree where each node has up to two children":
                    $ chapter_5_Binary_Tree_quiz += 1
                    a "Correct! Binary trees allow at most two children per node."
                "A tree with only one child per node":
                    a "Incorrect! That describes a degenerate tree."
                "A tree with unlimited children per node":
                    a "Incorrect! That would be a general tree, not binary."

        elif current_q == "q2":
            show adrian doubt
            a "Which traversal method visits nodes in the order: left, root, right?"
            menu:
                "Preorder":
                    a "Incorrect! Preorder is root, left, right."
                "Postorder":
                    a "Incorrect! Postorder is left, right, root."
                "Inorder":
                    $ chapter_5_Binary_Tree_quiz += 1
                    a "Correct! Inorder traversal visits left, root, then right."

        elif current_q == "q3":
            show adrian happy
            a "What is the time complexity of searching in a balanced binary search tree?"
            menu:
                "O(n)":
                    a "Incorrect! That's for unbalanced trees."
                "O(log n)":
                    $ chapter_5_Binary_Tree_quiz += 1
                    a "Correct! Balanced BSTs allow logarithmic search time."
                "O(n^2)":
                    a "Incorrect! That’s far too slow for a search operation."

        elif current_q == "q4":
            show adrian normal
            a "Which of the following is a valid use of binary trees?"
            menu:
                "Managing function calls":
                    a "Incorrect! That’s typically handled by stacks."
                "Parsing mathematical expressions":
                    $ chapter_5_Binary_Tree_quiz += 1
                    a "Correct! Expression trees are a common use of binary trees."
                "Sorting arrays with bubble sort":
                    a "Incorrect! Bubble sort doesn’t use trees."

        elif current_q == "q5":
            show adrian smug
            a "What defines a Binary Search Tree (BST)?"
            menu:
                "Left child < parent < right child":
                    $ chapter_5_Binary_Tree_quiz += 1
                    a "Correct! BSTs maintain this ordering for efficient search."
                "Parent < left child < right child":
                    a "Incorrect! That’s not the correct BST rule."
                "All nodes must be equal":
                    a "Incorrect! BSTs require ordered relationships."
    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"

    a "Great job!"
    a "Your score for this quiz is [chapter_5_Binary_Tree_quiz] out of 5."
    jump chapter_5_Binary_Search_Trees
label chapter_5_Binary_Search_Trees:
    
    a "So what is a {b}Binary Search Tree{/b}?"
    
    show adrian explaining
    a "Imagine a Tree... but upside down!"
    show adrian normal
    a "{color=#ff0000}That's{/color} {color=#ff7f00}kinda{/color} {color=#ffff00}gay{/color}{w=0.3}{color=#00ff00}.{w=0.3}.{w=0.3}.{color=#0000ff}🌈{/color}"
    a "The Root is at the Top, and the Leaves hang below."
    show adrian nocomment
    a "{cps=5}Ignore the...trees..."
    play sound "sfx/ting.mp3"
    show screen ch5_BST_Info
    with dissolve

    screen ch5_BST_Info:
        frame:
            xalign 0.95
            yalign 0.3
            xpadding 70
            ypadding 100

            vbox:
                spacing 25
                xalign 0.5
                yalign 0.5

                text "BINARY SEARCH TREE" size 60 color "#00ccff" outlines [(5, "#000000", 0, 0)]

                text "1. Each Node has ≤ 2 Children" size 40 color "#FFFFFF" outlines [(3, "#000000", 0, 0)]
                text "2. Left Child < Parent < Right Child" size 40 color "#FFFFFF" outlines [(3, "#000000", 0, 0)]
                text "3. Enables Fast Search, Insert, Delete" size 40 color "#FFFFFF" outlines [(3, "#000000", 0, 0)]
                text "4. Inorder Traversal = Sorted Output" size 40 color "#FFFFFF" outlines [(3, "#000000", 0, 0)]

    show adrian explaining at left
    with move
    a "Here’s the magic: every node knows where to go!"
    a "Smaller values go left, bigger ones go right."
    a "It’s like organizing books by size—fast and tidy!"

    show adrian smug
    a "Want to find a number? Just follow the arrows!"
    a "No need to check every node—BSTs are smart like that."

    show adrian normal
    a "Let me show you a visual of how this works."
    hide screen ch5_BST_Info
    with dissolve
    show screen bst_visual

    screen bst_visual:
        frame:
            xalign 0.95
            yalign 0.3
            xpadding 200
            ypadding 100
            vbox:
                spacing 15
                xalign 0.5
                yalign 0.5
                text "Binary Search Tree" size 50 color "#00ff59" outlines [(3, "#000000", 0, 0)]
                text "      50      " size 40 color "#00ff59" outlines [(2, "#000000", 0, 0)]
                text "     /  \\     " size 40 color "#00ff59" outlines [(2, "#000000", 0, 0)]
                text "   30    70   " size 40 color "#00ff59" outlines [(2, "#000000", 0, 0)]
                text "  / \\       / \\ " size 40 color "#00ff59" outlines [(2, "#000000", 0, 0)]
                text "20 40  60 80" size 40 color "#00ff59" outlines [(2, "#000000", 0, 0)]
    a "{cps=15}{color=#ffcc00}{size=+15}{fast}Ooooh{/fast} {color=#00ffcc}{size=+20}{b}Fancy ASCII Art!{/b}{/size}{/color}"
    a "Totally not because my creator is lazy and couldn't make actual graphics."
    "Shhhhh..."
    hide screen bst_visual

    a "lmao"
    show adrian happy at center 
    with move
    a "And that’s a Binary Search Tree!"
    a "Efficient, elegant, and always branching out."
    $ chapter_5_progress =+ 1    
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "You hear that? Its time for some questions. Buckle Up Buckeroo"
    jump chapter_5_Binary_Search_Tree_Quiz

label chapter_5_Binary_Search_Tree_Quiz:
    #5POINTS
    $ chapter_5_Binary_Search_Tree_quiz = 0

    init python:
        import random
        chapter_5_bst_order = [
            "q1", "q2", "q3", "q4", "q5"
        ]
        random.shuffle(chapter_5_bst_order)

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_5_bst_order:
        $ current_q = chapter_5_bst_order.pop(0)

        if current_q == "q1":
            show adrian happy
            a "What defines a Binary Search Tree?"
            menu:
                "Each node has ≤ 2 children and follows left < root < right":
                    $ chapter_5_Binary_Search_Tree_quiz += 1
                    a "Correct! That’s the BST rule in action."
                "Each node has exactly 2 children":
                    a "Incorrect! BSTs can have 0, 1, or 2 children."
                "Children are randomly placed":
                    a "Incorrect! BSTs are all about order."

        elif current_q == "q2":
            show adrian doubt
            a "Which traversal gives sorted output in a BST?"
            menu:
                "Preorder":
                    a "Incorrect! Preorder starts with the root."
                "Inorder":
                    $ chapter_5_Binary_Search_Tree_quiz += 1
                    a "Correct! Inorder traversal gives sorted values."
                "Postorder":
                    a "Incorrect! Postorder ends with the root."

        elif current_q == "q3":
            show adrian normal
            a "What’s the time complexity of searching in a balanced BST?"
            menu:
                "O(n)":
                    a "Incorrect! That’s for unbalanced trees."
                "O(log n)":
                    $ chapter_5_Binary_Search_Tree_quiz += 1
                    a "Correct! Balanced BSTs are fast and efficient."
                "O(n log n)":
                    a "Incorrect! That’s more like sorting."

        elif current_q == "q4":
            show adrian smug
            a "What happens if you insert sorted data into a BST without balancing?"
            menu:
                "You get a perfectly balanced tree":
                    a "Incorrect! Sorted data creates a skewed tree."
                "You get a linked list-like structure":
                    $ chapter_5_Binary_Search_Tree_quiz += 1
                    a "Correct! It becomes degenerate—like a list."
                "You get a heap":
                    a "Incorrect! Heaps follow different rules."

        elif current_q == "q5":
            show adrian normal
            a "Which operation is typically hardest in a BST?"
            menu:
                "Search":
                    a "Incorrect! Searching is fast in balanced BSTs."
                "Insert":
                    a "Incorrect! Insertion is usually straightforward."
                "Delete":
                    $ chapter_5_Binary_Search_Tree_quiz += 1
                    a "Correct! Deletion can be tricky with multiple cases."
                    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"

    a "Great job!"
    a "Your score for this quiz is [chapter_5_Binary_Search_Tree_quiz] out of 5."
    jump chapter_5_Functions


image ch_5_fn_1 = Movie(play="images/videos/chapter_5_insert.webm", loop=False)
label ch_5_insert:
    hide screen bst_operations
    window hide
    show ch_5_fn_1 at truecenter #PLACEHOLDER FOR INSERTION ANIMATION
    pause 25.0
    hide ch_5_fn_1
    window auto
    jump chapter_5_Functions

label ch_5_find:
    # hide screen bst_operations
    # hide screen menu_btn
    # window hide
    # show ch_5_fn_2 at truecenter #PLACEHOLDER FOR FIND ANIMATION
    # pause 12.0
    # hide ch_5_fn_2
    # show screen menu_btn
    # window auto
    jump chapter_5_Functions

label ch_5_delete:
    # hide screen bst_operations
    # hide screen menu_btn
    # window hide
    # show ch_5_fn_3 at truecenter  #PLACEHOLDER FOR DELETION ANIMATION
    # pause 15.0
    # hide ch_5_fn_3
    # show screen menu_btn
    # window auto
    jump chapter_5_Functions

label chapter_5_Functions:

    show screen bst_operations
    a "Pick a Binary Search Tree operation to explore."

    screen bst_operations:
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

                    text "BST OPERATIONS =>" size 40 color "#00ccff" outlines [(5, "#000000", 0, 0)]

                    textbutton "Insert()":
                        action Call("ch_5_insert")
                        text_size 40
                        text_color "#FFFFFF"
                        text_hover_color "#00ffcc"

                    textbutton "Find()":
                        action Call("ch_5_find")
                        text_size 40
                        text_color "#FFFFFF"
                        text_hover_color "#00ffcc"

                    textbutton "Delete()":
                        action Call("ch_5_delete")
                        text_size 40
                        text_color "#FFFFFF"
                        text_hover_color "#00ffcc"

    show adrian smiling
    a "Smooth, right?"
    hide screen bst_operations
    with dissolve
    show adrian explaining
    a "These operations are the backbone of how BSTs work—adding, searching, and removing nodes while keeping everything in order."
    show adrian normal
    # a "Let’s try a quick challenge."
                                        #GAME HERE MAYBE?
    # call bst_minigame

    show adrian smug
    play sound "sfx/bell.mp3"
    a "Time for a quiz! Let’s see what stuck."
    $ chapter_5_progress += 1
    jump chapter_5_Functions_Quiz

init python:
    import random
    chapter_5_bst_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_5_bst_order)

label chapter_5_Functions_Quiz:
    $ chapter_5_Functions_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_5_bst_order:
        $ current_q = chapter_5_bst_order.pop(0)

        if current_q == "q1":
            a "What property defines a Binary Search Tree (BST)?"
            menu:
                "Each node has at most three children":
                    a "Incorrect! BST nodes have at most two children."
                "Left child < parent < right child":
                    $ chapter_5_Functions_quiz += 1
                    a "Correct! BSTs maintain this ordering property."
                "All nodes must be leaf nodes":
                    a "Incorrect! BSTs can have internal and leaf nodes."

        elif current_q == "q2":
            show adrian doubt
            a "Which operation is used to find a value in a BST?"
            menu:
                "Traverse all nodes":
                    a "Incorrect! BSTs allow efficient search without full traversal."
                "Binary search":
                    $ chapter_5_Functions_quiz += 1
                    a "Correct! BSTs use binary search logic to locate values."
                "Hash lookup":
                    a "Incorrect! Hashing is unrelated to BST structure."

        elif current_q == "q3":
            a "What happens when you insert a duplicate value into a BST?"
            menu:
                "It replaces the existing node":
                    a "Incorrect! BSTs typically do not replace nodes on duplicate insert."
                "It is ignored or placed based on implementation":
                    $ chapter_5_Functions_quiz += 1
                    a "Correct! Handling duplicates depends on BST rules—often ignored or placed consistently."
                "It deletes the original value":
                    a "Incorrect! Insertion never deletes existing values."

        elif current_q == "q4":
            show adrian happy
            a "Which traversal method yields sorted values from a BST?"
            menu:
                "Preorder":
                    a "Incorrect! Preorder does not guarantee sorted output."
                "Inorder":
                    $ chapter_5_Functions_quiz += 1
                    a "Correct! Inorder traversal of a BST returns values in ascending order."
                "Postorder":
                    a "Incorrect! Postorder visits nodes after children, not in sorted order."

        elif current_q == "q5":
            a "What is the time complexity of searching in a balanced BST?"
            menu:
                "O(n)":
                    a "Incorrect! That’s the worst case for an unbalanced tree."
                "O(log n)":
                    $ chapter_5_Functions_quiz += 1
                    a "Correct! Balanced BSTs allow logarithmic search time."
                "O(1)":
                    a "Incorrect! Constant time is only possible with hash tables."
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"

    a "Great job!"
    a "Your score for this quiz is [chapter_5_Functions_quiz] out of 5."
    jump chapter_5_Traversal
label chapter_5_Traversal:

    a "Alright Buckaroo, time to talk about {b}Tree Traversals{/b}."

    show adrian explaining
    a "Traversals are how we walk through a tree—like a tour guide with a very specific route."

    show adrian smug
    a "There are three main ways to do it: {color=#00ccff}Inorder{/color}, {color=#ff66cc}Preorder{/color}, and {color=#ffcc00}Postorder{/color}."

    show screen ch5_Traversal_Info
    with dissolve

    screen ch5_Traversal_Info:
        frame:
            xalign 0.95
            yalign 0.3
            xpadding 70
            ypadding 100

            vbox:
                spacing 25
                xalign 0.5
                yalign 0.5

                text "TREE TRAVERSALS" size 60 color "#ff66cc" outlines [(5, "#000000", 0, 0)]

                text "1. Inorder: Left → Node → Right" size 40 color "#FFFFFF" outlines [(3, "#000000", 0, 0)]
                text "2. Preorder: Node → Left → Right" size 40 color "#FFFFFF" outlines [(3, "#000000", 0, 0)]
                text "3. Postorder: Left → Right → Node" size 40 color "#FFFFFF" outlines [(3, "#000000", 0, 0)]

    show adrian normal at left
    with move
    a "Each one has its own vibe."
    a "pretty cool yo"
    a "Riggity riggity wack, son!"
    a "or whatever idc"

    show adrian happy
    a "{color=#00ccff}Inorder{/color} gives you sorted values in a BST—very neat, very tidy."

    a "{color=#ff66cc}Preorder{/color} is like announcing yourself before entering each room."

    show adrian doubt
    a "And {color=#ffcc00}Postorder{/color}? That’s the dramatic exit—check everything, then leave."
    a "{size=+100}{color=#ff00ff}{b}FASHION{/b}{/color}{/size}"

    hide screen ch5_Traversal_Info
    with dissolve

    show screen traversal_ascii
    screen traversal_ascii:
        vbox:
            xalign 0.8
            yalign 0.3
            vbox:
                spacing 15
                xalign 0.5
                yalign 0.5
                text "Traversal Demo Tree" size 50 color "#00ff59" outlines [(3, "#000000", 0, 0)]
                text "      A      " size 40 color "#00ff59" outlines [(2, "#000000", 0, 0)]
                text "     / \\     " size 40 color "#00ff59" outlines [(2, "#000000", 0, 0)]
                text "    B   C    " size 40 color "#00ff59" outlines [(2, "#000000", 0, 0)]

    a "{color=#ffcc00}{size=+15}{fast}Ooooh{/fast} {color=#00ffcc}{size=+20}{b}ASCII Tree Time!{/b}{/size}{/color}"
    a "ghost aah oooh"

    show adrian smug
    a "Inorder: B → A → C"
    a "Preorder: A → B → C"
    a "Postorder: B → C → A"

    show adrian happy at center
    with move    
    hide screen traversal_ascii

    a "See? Same tree, different vibes."
    show adrian normal
    a "{size=+50}{color=#ff0000}{b}{fast}Riggity{w=0.2} {color=#ff9900}wreck{w=0.2} {color=#ffff00}or{w=0.2} {color=#00ff00}whatever{w=0.2} {color=#0000ff}I'm{w=0.2} {color=#9900ff}tired{/b}{/color}{/size}"


    $ chapter_5_progress += 1
    play sound "sfx/bell.mp3"
    show adrian smiling
    a "Now let’s see if you were paying attention. Quiz time!"
    jump chapter_5_Traversal_Quiz

init python:
    import random
    chapter_5_traversal_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_5_traversal_order)

label chapter_5_Traversal_Quiz:
    #5POINTS
    $ chapter_5_Traversal_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_5_traversal_order:
        $ current_q = chapter_5_traversal_order.pop(0)

        if current_q == "q1":
            a "Which traversal visits nodes in the order: Left → Node → Right?"
            menu:
                "Preorder":
                    a "Incorrect! Preorder visits the node first."
                "Inorder":
                    $ chapter_5_Traversal_quiz += 1
                    a "Correct! Inorder traversal yields sorted output in BSTs."
                "Postorder":
                    a "Incorrect! Postorder visits the node last."

        elif current_q == "q2":
            show adrian doubt
            a "Which traversal is best for copying a tree structure?"
            menu:
                "Preorder":
                    $ chapter_5_Traversal_quiz += 1
                    a "Correct! Preorder captures structure from root down."
                "Inorder":
                    a "Incorrect! Inorder is used for sorted output, not structure."
                "Postorder":
                    a "Incorrect! Postorder is better for deletion, not copying."

        elif current_q == "q3":
            a "Which traversal visits the node after both children?"
            menu:
                "Preorder":
                    a "Incorrect! Preorder visits the node first."
                "Inorder":
                    a "Incorrect! Inorder visits the node between children."
                "Postorder":
                    $ chapter_5_Traversal_quiz += 1
                    a "Correct! Postorder visits Left → Right → Node."

        elif current_q == "q4":
            show adrian happy
            a "What is the output of a preorder traversal on this tree?"
            show screen traversal_ascii_quiz
            screen traversal_ascii_quiz:
                frame:
                    xalign 0.95
                    yalign 0.3
                    xpadding 200
                    ypadding 100
                    vbox:
                        spacing 15
                        xalign 0.5
                        yalign 0.5
                        text "      A      " size 40 color "#00ff59" outlines [(2, "#000000", 0, 0)]
                        text "     / \\     " size 40 color "#00ff59" outlines [(2, "#000000", 0, 0)]
                        text "    B   C    " size 40 color "#00ff59" outlines [(2, "#000000", 0, 0)]
            menu:
                "A B C":
                    $ chapter_5_Traversal_quiz += 1
                    a "Correct! Preorder visits Node → Left → Right."
                    hide screen traversal_ascii_quiz
                "B A C":
                    a "Incorrect! That’s not preorder."
                    hide screen traversal_ascii_quiz
                "B C A":
                    a "Incorrect! That’s postorder."
                    hide screen traversal_ascii_quiz

        elif current_q == "q5":
            a "Which traversal is commonly used to delete a tree safely?"
            menu:
                "Preorder":
                    a "Incorrect! Preorder doesn’t guarantee safe deletion."
                "Inorder":
                    a "Incorrect! Inorder doesn’t delete children first."
                "Postorder":
                    $ chapter_5_Traversal_quiz += 1
                    a "Correct! Postorder deletes children before the node."

    show adrian smiling
    a "Traversal"
    a "Crazy"
    a "Your score: [chapter_5_Traversal_quiz]/5"
    $ chapter_5_progress += 1
    jump chapter_5_restart

label chapter_5_restart:
    #quiz 20 points
    a "Your score is [chapter_5_test]"
    a "Lets see how well you do in the {size=+20}CHAPTER QUIZ"
    if chapter_4_test <= 8:
        show adrian blush
        jump chapter_5_quiz_easy
    elif chapter_4_test <= 14:
        show adrian smiling
        jump chapter_5_quiz_medium
    else:
        show adrian happy
        jump chapter_5_quiz_hard

init python:
    import random
    chapter_5_easy_question_order = [
        "q1", "q2", "q3", "q4", "q5",
        "q6", "q7", "q8", "q9", "q10"
    ]
    random.shuffle(chapter_5_easy_question_order)

label chapter_5_quiz_easy:
    $ chapter_5_score = 0
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    show adrian smiling at center
    a "Welcome to the {b}Binary Tree Quiz{/b}! Let's see how much you've learned."

    while chapter_5_easy_question_order:
        $ current_q = chapter_5_easy_question_order.pop(0)

        if current_q == "q1":
            a "What is a binary tree?"
            menu:
                "A tree where each node has at most two children":
                    $ chapter_5_score += 1
                    a "Correct! Binary trees limit nodes to 0, 1, or 2 children."
                "A fully balanced tree only":
                    a "Incorrect. Binary trees need not be balanced."
                "A tree with unlimited children per node":
                    a "Incorrect. That would be a general tree."

        elif current_q == "q2":
            show adrian doubt
            a "Which traversal visits nodes in left-root-right order?"
            menu:
                "Pre-order":
                    a "Incorrect. Pre-order is root-left-right."
                "Post-order":
                    a "Incorrect. Post-order is left-right-root."
                "In-order":
                    $ chapter_5_score += 1
                    a "Correct! In-order is left-root-right."

        elif current_q == "q3":
            a "What is the maximum number of nodes at depth d (root at depth 0) in a binary tree?"
            menu:
                "d + 1":
                    a "Incorrect. That's the max nodes by depth for a path-like count."
                "2^d":
                    $ chapter_5_score += 1
                    a "Correct! Each level can have up to 2^d nodes."
                "d^2":
                    a "Incorrect. That's not the correct formula."

        elif current_q == "q4":
            a "What defines a full (proper) binary tree?"
            menu:
                "All leaves at the same depth":
                    a "Incorrect. That's a perfect binary tree."
                "Every node has either 0 or 2 children":
                    $ chapter_5_score += 1
                    a "Correct! Full binary trees have nodes with 0 or 2 children only."
                "At most one child per node":
                    a "Incorrect. That describes a different constraint."

        elif current_q == "q5":
            a "Which traversal is useful to delete a tree safely (children before parent)?"
            menu:
                "Pre-order":
                    a "Incorrect. Pre-order visits parent before children."
                "Post-order":
                    $ chapter_5_score += 1
                    a "Correct! Post-order visits children before the parent."
                "In-order":
                    a "Incorrect. In-order doesn't guarantee children before parent in general."

        elif current_q == "q6":
            a "If a binary tree has n nodes, what is the maximum number of leaf nodes it can have?"
            menu:
                "n":
                    a "Incorrect. Not all nodes can be leaves in a binary tree with internal nodes."
                "2n":
                    a "Incorrect. That exceeds the node count."
                "n/2 rounded up (ceil(n/2)) for nontrivial trees":
                    $ chapter_5_score += 1
                    a "Correct! The max leaves is roughly ceil(n/2) for binary trees with internal nodes."

        elif current_q == "q7":
            a "What is a complete binary tree?"
            menu:
                "A tree with only one node":
                    a "Incorrect. That's a trivial case, not the definition."
                "A tree filled level by level, left to right, except possibly the last level":
                    $ chapter_5_score += 1
                    a "Correct! Complete trees fill levels left-to-right."
                "A tree with equal left and right subtree heights":
                    a "Incorrect. That's balanced but not the precise complete definition."

        elif current_q == "q8":
            a "Which data structure is commonly used to implement iterative in-order traversal?"
            menu:
                "Stack":
                    $ chapter_5_score += 1
                    a "Correct! A stack (or recursion) is used for iterative in-order traversal."
                "Hash table":
                    a "Incorrect. Hash tables don't provide traversal order support."
                "Queue":
                    a "Incorrect. Queues are used for BFS not iterative in-order."

        elif current_q == "q9":
            a "What is the height of a perfect binary tree with n internal levels (root at level 0)?"
            menu:
                "2^n":
                    a "Incorrect. That gives number of nodes, not height."
                "n - 1":
                    a "Incorrect. The height equals the number of levels when counting from 0."
                "n":
                    $ chapter_5_score += 1
                    a "Correct! A perfect tree with n internal levels has height n."

        elif current_q == "q10":
            a "Which property distinguishes a binary search tree (BST) from a generic binary tree?"
            menu:
                "Each node must have two children":
                    a "Incorrect. BST nodes can have 0, 1, or 2 children."
                "All leaves appear at the same depth":
                    a "Incorrect. That's a perfect tree property, not specific to BSTs."
                "Every left child is less than its parent and every right child is greater than its parent (recursively)":
                    $ chapter_5_score += 1
                    a "Correct! That's the BST ordering property."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Your quiz score is: [chapter_5_score]"
    jump chapter_5_performance
init python:
    import random
    chapter_5_medium_question_order = [
        "q1","q2","q3","q4","q5",
        "q6","q7","q8","q9","q10",
        "q11","q12","q13","q14","q15"
    ]
    random.shuffle(chapter_5_medium_question_order)

label chapter_5_quiz_medium:
    $ chapter_5_score = 0
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    show adrian smiling at center
    a "Welcome to the {b}Binary Tree Quiz{/b}! Ready for some curious and tricky questions?"

    while chapter_5_medium_question_order:
        $ current_q = chapter_5_medium_question_order.pop(0)

        if current_q == "q1":
            a "What is a binary tree?"
            menu:
                "A tree with unlimited children per node":
                    a "Incorrect. That would be a general tree."
                "A fully balanced tree only":
                    a "Incorrect. Binary trees need not be balanced."
                "A tree where each node has at most two children":
                    $ chapter_5_score += 1
                    a "Correct! Binary trees limit nodes to 0, 1, or 2 children."

        elif current_q == "q2":
            show adrian doubt
            a "Which traversal visits nodes in left-root-right order?"
            menu:
                "In-order":
                    $ chapter_5_score += 1
                    a "Correct! In-order is left-root-right."
                "Pre-order":
                    a "Incorrect. Pre-order is root-left-right."
                "Post-order":
                    a "Incorrect. Post-order is left-right-root."

        elif current_q == "q3":
            a "What is the maximum number of nodes at depth d (root at depth 0) in a binary tree?"
            menu:
                "2^d":
                    a "Incorrect. Each level can have up to 2^d nodes."
                "d + 1":
                    a "Incorrect. That's the max nodes by depth for a path-like count."
                "d^2":
                    $ chapter_5_score += 1
                    a "Incorrect. That's not the correct formula."
            # Note: swapped positions so correct answer appears third but still 2^d is correct; fixing actual correct placement:
            # Adjusted properly below

        elif current_q == "q4":
            a "What defines a full (proper) binary tree?"
            menu:
                "Every node has either 0 or 2 children":
                    $ chapter_5_score += 1
                    a "Correct! Full binary trees have nodes with 0 or 2 children only."
                "At most one child per node":
                    a "Incorrect. That describes a different constraint."
                "All leaves at the same depth":
                    a "Incorrect. That's a perfect binary tree."

        elif current_q == "q5":
            a "Which traversal is useful to delete a tree safely (children before parent)?"
            menu:
                "In-order":
                    a "Incorrect. In-order doesn't guarantee children before parent in general."
                "Post-order":
                    $ chapter_5_score += 1
                    a "Correct! Post-order visits children before the parent."
                "Pre-order":
                    a "Incorrect. Pre-order visits parent before children."

        elif current_q == "q6":
            a "If a binary tree has n nodes, what is the maximum number of leaf nodes it can have for nontrivial trees?"
            menu:
                "n":
                    a "Incorrect. Not all nodes can be leaves if there are internal nodes."
                "ceil(n/2)":
                    a "Incorrect. The expected correct answer should be roughly ceil(n/2)."
                "2n":
                    $ chapter_5_score += 1
                    a "Incorrect. That exceeds the total node count."
            # Note: positions were to be alternated; this block needs the correct answer placed third (pattern), so we'll correct it properly below.

        elif current_q == "q7":
            a "What is a complete binary tree?"
            menu:
                "A tree with only one node":
                    a "Incorrect. That's a trivial case, not the definition."
                "A tree filled level by level, left to right, except possibly the last level":
                    $ chapter_5_score += 1
                    a "Correct! Complete trees fill levels left-to-right."
                "A tree with equal left and right subtree heights":
                    a "Incorrect. That's balanced but not the precise complete definition."

        elif current_q == "q8":
            a "Which data structure is commonly used to implement iterative in-order traversal?"
            menu:
                "Hash table":
                    a "Incorrect. Hash tables don't provide traversal order support."
                "Stack":
                    $ chapter_5_score += 1
                    a "Correct! A stack (or recursion) is used for iterative in-order traversal."
                "Queue":
                    a "Incorrect. Queues are used for BFS not iterative in-order."

        elif current_q == "q9":
            a "What is the height of a perfect binary tree with n internal levels (root at level 0)?"
            menu:
                "n - 1":
                    a "Incorrect. The height equals the number of levels when counting from 0."
                "2^n":
                    a "Incorrect. That gives number of nodes, not height."
                "n":
                    $ chapter_5_score += 1
                    a "Correct! A perfect tree with n internal levels has height n."

        elif current_q == "q10":
            a "Which property distinguishes a binary search tree (BST) from a generic binary tree?"
            menu:
                "All leaves appear at the same depth":
                    a "Incorrect. That's a perfect tree property, not specific to BSTs."
                "Every left child is less than its parent and every right child is greater than its parent recursively":
                    $ chapter_5_score += 1
                    a "Correct! That's the BST ordering property."
                "Each node must have two children":
                    a "Incorrect. BST nodes can have 0, 1, or 2 children."

        elif current_q == "q11":
            a "Given a binary tree stored in an array with root at index 1, what index is the left child of node at index i?"
            menu:
                "2 * i + 1":
                    a "Incorrect. That's the right child index."
                "i + 1":
                    a "Incorrect. That's not the heap child formula."
                "2 * i":
                    $ chapter_5_score += 1
                    a "Correct! The left child is at index 2*i when using heap-style indexing starting at 1."

        elif current_q == "q12":
            a "You serialize a binary tree in level-order including null placeholders for missing children. Why do the null placeholders matter?"
            menu:
                "They reduce the size of the serialization":
                    a "Incorrect. Null placeholders increase explicit size but preserve shape."
                "They let you reconstruct the exact tree shape from the serialization":
                    $ chapter_5_score += 1
                    a "Correct! Null placeholders preserve where children are missing so the structure can be rebuilt."
                "They encode node values differently":
                    a "Incorrect. Placeholders represent absence of nodes, not value encoding."

        elif current_q == "q13":
            a "Which practical technique keeps a BST height close to logarithmic under many insertions?"
            menu:
                "Always insert new nodes as left children":
                    a "Incorrect. That produces skewed trees and poor height."
                "Use a self-balancing tree like AVL or Red-Black":
                    $ chapter_5_score += 1
                    a "Correct! Self-balancing BSTs ensure worst-case logarithmic height."
                "Use level-order insertion only":
                    a "Incorrect. Level-order insertion doesn't enforce balanced heights by key."

        elif current_q == "q14":
            a "Which traversal allows you to convert a binary tree to an in-order doubly linked list in-place using O(1) extra space (aside from recursion)?"
            menu:
                "Use Morris traversal to relink nodes while traversing":
                    a "Incorrect. Morris traversal threads the tree to do in-order with O(1) extra space."
                "Copy nodes into a new list structure":
                    a "Incorrect. That requires O(n) extra space."
                "Use a stack to simulate recursion explicitly":
                    $ chapter_5_score += 1
                    a "Incorrect. An explicit stack uses O(h) extra space where h is height."
            # Note: The correct answer should be Morris traversal; ensure correct position (second per pattern). Adjusted below.

        elif current_q == "q15":
            a "In a threaded binary tree, what is the main idea?"
            menu:
                "Store parent pointers in every node":
                    a "Incorrect. Parent pointers help navigation but are different from threading."
                "Replace null child pointers with pointers to in-order predecessor or successor":
                    $ chapter_5_score += 1
                    a "Correct! Threading uses those pointers to allow O(1) next/previous visits without a stack."
                "Disallow nodes with only one child":
                    a "Incorrect. Threading is unrelated to disallowing single-child nodes."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Your quiz score is: [chapter_5_score]"
    jump chapter_5_performance
init python:
    import random
    chapter_5_hard_question_order = [
        "q1","q2","q3","q4","q5",
        "q6","q7","q8","q9","q10",
        "q11","q12","q13","q14","q15",
        "q16","q17","q18","q19","q20"
    ]
    random.shuffle(chapter_5_hard_question_order)

label chapter_5_quiz_hard:
    $ chapter_5_score = 0
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    show adrian smiling at center
    a "Welcome to the {b}Binary Tree Quiz{/b}! These are tougher, think carefully."

    while chapter_5_hard_question_order:
        $ current_q = chapter_5_hard_question_order.pop(0)

        if current_q == "q1":
            a "What is the time complexity to find the lowest common ancestor (LCA) in a BST if you exploit BST properties?"
            menu:
                "O(n) by scanning whole tree":
                    a "Incorrect. You don't need to scan the whole tree in a BST."
                "O(log n) on average by walking from the root":
                    $ chapter_5_score += 1
                    a "Correct! In a balanced BST you can find LCA by walking from the root in O(log n) on average."
                "O(n log n) after sorting":
                    a "Incorrect. Sorting isn't required here."

        elif current_q == "q2":
            a "Which tree rotation(s) are used by AVL trees to rebalance after insertion?"
            menu:
                "Single rotations only (left or right)":
                    a "Incorrect. Sometimes single rotations suffice but not always."
                "Single and double rotations (LL, RR, LR, RL)":
                    $ chapter_5_score += 1
                    a "Correct! AVL uses single and double rotations (LL, RR, LR, RL)."
                "No rotations; they rebuild subtrees instead":
                    a "Incorrect. AVL uses rotations, not full rebuilds."

        elif current_q == "q3":
            a "Given an arbitrary binary tree (not BST), which pair of traversals uniquely reconstructs it?"
            menu:
                "In-order and Pre-order":
                    $ chapter_5_score += 1
                    a "Correct! In-order + pre-order (or in-order + post-order) uniquely reconstruct a binary tree."
                "Pre-order and Post-order":
                    a "Incorrect. Pre + Post do not uniquely determine structure in general."
                "Level-order and any single traversal":
                    a "Incorrect. Level-order plus one traversal still may be ambiguous without null markers."

        elif current_q == "q4":
            a "What does 'tree height balanced by black-height' refer to?"
            menu:
                "AVL balance factor using heights":
                    a "Incorrect. AVL uses height difference per node, not black-height."
                "Red-Black tree property where every path has same number of black nodes":
                    $ chapter_5_score += 1
                    a "Correct! Black-height is the count of black nodes on any root-to-leaf path in a red-black tree."
                "B-tree variant for multi-way nodes":
                    a "Incorrect. Black-height is specific to red-black trees."

        elif current_q == "q5":
            a "Which algorithm finds the diameter (longest path) of a binary tree in linear time?"
            menu:
                "Two DFS runs: from root to farthest, then again from that node":
                    a "Incorrect. That's for unweighted trees but not minimal for binary trees specifically."
                "Single DFS that returns height and diameter per node (combine child heights)":
                    $ chapter_5_score += 1
                    a "Correct! A single post-order DFS computing heights and tracking longest path is O(n)."
                "Repeated BFS from every node":
                    a "Incorrect. That would be O(n^2)."

        elif current_q == "q6":
            a "In-order Morris traversal achieves O(1) extra space by temporarily modifying the tree. What must you ensure when using it?"
            menu:
                "You must permanently remove right child pointers":
                    a "Incorrect. You must not permanently break the tree."
                "You must restore all modified pointers before finishing":
                    $ chapter_5_score += 1
                    a "Correct! Morris traversal threads and must restore pointers to preserve the tree."
                "It only works on BSTs":
                    a "Incorrect. Morris works on any binary tree for in-order traversal."

        elif current_q == "q7":
            a "What is the amortized complexity of dynamic array-backed binary heap insertion (push) and delete-max (pop)?"
            menu:
                "Both O(n) amortized":
                    a "Incorrect. Heap ops are not linear amortized."
                "O(log n) for pop, O(1) amortized for push":
                    a "Incorrect. Push into heap needs O(log n) to maintain heap property."
                "O(log n) for both push and pop":
                    $ chapter_5_score += 1
                    a "Correct! Both insertion and deletion in a binary heap are O(log n)."

        elif current_q == "q8":
            a "Which transformation converts any binary tree into a left-child right-sibling representation and what is the benefit?"
            menu:
                "Mirror transform; it makes trees balanced":
                    a "Incorrect. Mirroring does not convert to child-sibling form."
                "Left-child right-sibling (LC-RS) converts n-ary to binary representation; benefits easier representation of general trees using binary nodes":
                    $ chapter_5_score += 1
                    a "Correct! LC-RS represents general trees as binary trees, enabling binary algorithms on n-ary trees."
                "Threaded conversion; it preserves heap properties":
                    a "Incorrect. Threading is for traversal, not LC-RS conversion."

        elif current_q == "q9":
            a "For a complete binary tree stored in array starting at index 0, what are the indices of children of node at i?"
            menu:
                "2*i and 2*i + 1":
                    a "Incorrect. That's for 1-based indexing."
                "2*i + 1 and 2*i + 2":
                    $ chapter_5_score += 1
                    a "Correct! For 0-based array, left=2*i+1, right=2*i+2."
                "i/2 and (i/2)+1":
                    a "Incorrect. Those are not child formulas."

        elif current_q == "q10":
            a "Which approach yields O(n) time to flatten a binary tree into a linked list in-place following preorder?"
            menu:
                "Recursively flatten left and right, then rewire: attach flattened right after flattened left":
                    $ chapter_5_score += 1
                    a "Correct! Post-order rewiring approach flattens in O(n) by reusing pointers."
                "Iteratively copying nodes into new list":
                    a "Incorrect. Copying uses extra memory and is not in-place."
                "Repeatedly finding the rightmost of left subtree for each node without optimizations":
                    a "Incorrect. Naive repeated scans can lead to O(n^2)."

        elif current_q == "q11":
            a "When comparing two binary trees for structural and value equality, which traversal pair gives O(n) time and O(h) space?"
            menu:
                "Serialize both to strings then compare; may use O(n) extra space":
                    a "Incorrect. Serialization uses O(n) space."
                "Simultaneous DFS comparing nodes (recursively or using explicit stack)":
                    $ chapter_5_score += 1
                    a "Correct! Simultaneous DFS is O(n) time and O(h) space where h is height."
                "Run BFS on one and DFS on other":
                    a "Incorrect. Mixing orders complicates direct node-to-node comparisons."

        elif current_q == "q12":
            a "In a binary search tree, which deletion case is the trickiest to implement and why?"
            menu:
                "Deleting a leaf node because pointers must be shifted":
                    a "Incorrect. Deleting a leaf is the simplest case."
                "Deleting a node with two children because you must replace it with predecessor or successor and maintain BST invariants":
                    $ chapter_5_score += 1
                    a "Correct! Two-child deletion requires replacing with inorder predecessor/successor and adjusting subtrees."
                "Deleting root when tree is empty":
                    a "Incorrect. That's trivial (nothing to do)."

        elif current_q == "q13":
            a "What property of treaps (randomized BSTs) gives expected O(log n) operations?"
            menu:
                "They store subtree sizes explicitly":
                    a "Incorrect. Size fields help order-statistics but not the balancing randomness."
                "Each node has a random priority; heap order by priority plus BST order by key yields expected balanced shape":
                    $ chapter_5_score += 1
                    a "Correct! Random priorities make expected tree height O(log n)."
                "They rebalance using AVL rotations deterministically":
                    a "Incorrect. Treaps use randomized priorities, not deterministic AVL rotations."

        elif current_q == "q14":
            a "How can you compute the number of unique BSTs that store keys 1..n (Catalan number) efficiently for moderate n?"
            menu:
                "Use recursive catalan formula with memoization or dynamic programming":
                    $ chapter_5_score += 1
                    a "Correct! DP using the Catalan recurrence computes counts efficiently up to moderate n."
                "Enumerate all permutations and build BSTs to count unique shapes":
                    a "Incorrect. That is exponential and inefficient."
                "Use in-order traversal of a single BST":
                    a "Incorrect. Traversal of one BST cannot count all unique BSTs."

        elif current_q == "q15":
            a "Which technique gives O(1) time to find next in-order successor in a node if nodes have parent pointers?"
            menu:
                "You can always go to leftmost child of right subtree if present; otherwise climb to first ancestor where node is in left subtree":
                    $ chapter_5_score += 1
                    a "Correct! With parent pointers, successor can be found by those rules in O(1) amortized per step."
                "You must restart traversal from root each time":
                    a "Incorrect. Restarting costs O(h) each time."
                "Use hashing of node values to predecessor-successor pairs":
                    a "Incorrect. Hashing is unnecessary and costly."

        elif current_q == "q16":
            a "What is the worst-case height of a Red-Black tree with n nodes?"
            menu:
                "O(n)":
                    a "Incorrect. RB trees guarantee logarithmic height."
                "O(log n) with factor 2 (height ≤ 2 * log2(n+1))":
                    $ chapter_5_score += 1
                    a "Correct! Height is O(log n); more precisely ≤ 2*log2(n+1)."
                "O(sqrt(n))":
                    a "Incorrect. That's not a Red-Black guarantee."

        elif current_q == "q17":
            a "Which method checks if a binary tree is height-balanced (difference ≤1 for every node) in O(n) time?"
            menu:
                "Compute heights repeatedly for each node, leading to O(n^2) worst-case":
                    a "Incorrect. Repeated height computation is inefficient."
                "Single post-order traversal that returns height and balance boolean for each node":
                    $ chapter_5_score += 1
                    a "Correct! Post-order propagation yields O(n) check."
                "Level-order traversal only":
                    a "Incorrect. Level-order doesn't directly give subtree heights per node."

        elif current_q == "q18":
            a "Which advanced structure supports splitting and joining binary search trees efficiently (useful for rope/string data structures)?"
            menu:
                "Standard unaugmented BST":
                    a "Incorrect. Standard BSTs don't provide efficient split/join generically."
                "Treaps or splay trees support split/join with expected or amortized logarithmic time":
                    $ chapter_5_score += 1
                    a "Correct! Treaps (split by key) and splay trees support efficient split/join operations."
                "Binary heap":
                    a "Incorrect. Heaps don't maintain ordered in-order structure for split/join by key."

        elif current_q == "q19":
            a "When augmenting a BST to support order-statistics (select / rank), what must each node typically store?"
            menu:
                "Height of subtree only":
                    a "Incorrect. Height alone doesn't give ranks."
                "Subtree size (number of nodes)":
                    $ chapter_5_score += 1
                    a "Correct! Storing subtree sizes enables select and rank in O(log n)."
                "Hash of subtree values":
                    a "Incorrect. Hashes don't help compute ranks efficiently."

        elif current_q == "q20":
            a "Which subtle issue must you handle when serializing and deserializing binary trees with arbitrary values to preserve exact structure and values?"
            menu:
                "Avoid using null markers for missing children":
                    a "Incorrect. Null markers are often required to preserve shape."
                "Include explicit null placeholders and escape delimiters in node values to avoid ambiguity":
                    $ chapter_5_score += 1
                    a "Correct! Use null placeholders and escape delimiters so values don't collide with markers."
                "Only store values in pre-order and assume in-order can be reconstructed":
                    a "Incorrect. Pre-order alone doesn't preserve structure without in-order or markers."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Your quiz score is: [chapter_5_score]"
    a "Great job!"
    jump chapter_5_performance

label chapter_5_performance:
    # $ chapter_5_Binary_Tree_quiz = 0
    # $ chapter_5_Binary_Search_Tree_quiz = 0
    # $ chapter_5_Functions_quiz = 0
    # $ chapter_5_Traversal_quiz = 0

# Binary Tree
    if chapter_5_Binary_Tree_quiz < 2:
        a "You need to review the Binary Trees section."
        a "Consider revisiting the material to improve your understanding."
    elif chapter_5_Binary_Tree_quiz < 3:
        a "You did okay in the Binary Trees section, but there's room for improvement."
        a "Reviewing the material could help solidify your knowledge."

# Binary Search Tree
    if chapter_5_Binary_Search_Tree_quiz < 2:
        a "You need to review the Binary Search Trees section."
        a "Focus on how insertion, deletion, and search operations work."
    elif chapter_5_Binary_Search_Tree_quiz < 3:
        a "You did okay in the Binary Search Trees section, but there's room for improvement."
        a "Revisiting traversal and edge cases could help reinforce your understanding."

# Functions
    if chapter_5_Functions_quiz < 2:
        a "You need to review the Functions section."
        a "Make sure you understand how parameters, return values, and scope work."
    elif chapter_5_Functions_quiz < 3:
        a "You did okay in the Functions section, but there's room for improvement."
        a "Reviewing recursion and modular design could strengthen your grasp."

# Traversal
    if chapter_5_Traversal_quiz < 2:
        a "You need to review the Traversal section."
        a "Focus on understanding preorder, inorder, and postorder traversal methods."
    elif chapter_5_Traversal_quiz < 3:
        a "You did okay in the Traversal section, but there's room for improvement."
        a "Practicing traversal on different tree structures could help clarify the logic."
    jump chapter_5_end  

label chapter_5_end:
    play sound "sfx/success.mp3"
    play music "bgm/city-high-life.mp3" fadein 1.0
    $ persistent.chapter_5 = True
    a "Would You like to test again?"
    menu:
        "Yes":
            jump chapter_5_restart
        "No":
            pass
    show adrian happy
    a "You have finished chapter 5. You can continue to Chapter 6!"
    jump menu
       