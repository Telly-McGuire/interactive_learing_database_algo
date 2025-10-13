# Chapter 11: Graph Traversal Algorithms
# Topics:
# - Breadth-first search introduction
# - Introduction to web crawlers
# - Depth-first search introduction
# - Uniform cost search algorithm
# - A* search algorithm
# - Iterative deepening search
# - Memory management: BFS vs DFS

default chapter_11_progress = 0

default chapter_11_BFS_quiz = 0
default chapter_11_Web_Crawlers_quiz = 0
default chapter_11_DFS_quiz = 0
default chapter_11_Uniform_Cost_quiz = 0
default chapter_11_A_Star_quiz = 0
default chapter_11_Iterative_Deepening_quiz = 0
default chapter_11_Memory_Management_quiz = 0

label chapter_11_intro:

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

    a "Welcome to Chapter 11: Graph Traversal Algorithms!"
    show adrian sad
    a "This is the last subject in our journey through Data Structures and Algorithms."
    a "I gotta be honest, I will miss you guys after this."
    show adrian happy
    a "But don't worry, we will have more adventures in the future!"
    a "What does that {b}Quote{/b} say again?"
    a "{cps=24}Don't cry because it's over, smile because it happened."
    show adrian normal
    a "Now, let's dive into graph traversal algorithms!"
    a "We will be tackling quite a few important algorithms in this chapter."
    a "So {b}bear{/b} with me"

    image bear = "assets/bear.png"

    show bear at right
    with moveinright

    show adrian at left
    with move

    "Yo"
    a "..."
    a "Sup?"
    "Nothing much"
    a "..."
    "You got honey?"
    a "Cuz you're a bear? {nw}"
    "No cuz I'm a monkey"
    "{size=+30 }YES BECAUSE I'M A BEAR"
    "Plus my kids are hungry and I'm hungry and I'm very sleepy"
    "And not to mention my wife is mad at me"
    "I still have to pay my mortgage"
    a "Sorry..."
    a "No sorry we run out of honey"
    "Damn"
    a "..."
    "..."
    a "Can you leave...we're in the middle of something here"
    "yeah aight"
    a "Thanks"
    "np"

    hide bear at right
    with moveoutright

    show adrian at center
    with move

    jump chapter_11_BFS

label chapter_11_BFS:

    a "First up, we have {b}Breadth-First Search (BFS){/b}."
    $ chapter_11_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Let's check your understanding with a quick quiz!"
    jump chapter_11_BFS_Quiz

label chapter_11_BFS_Quiz:
    #5POINTS
    $ chapter_11_BFS_quiz = 0
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert quiz questions here)

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_11_BFS_quiz] out of 5."
    jump chapter_11_Web_Crawlers

label chapter_11_Web_Crawlers:

    a "Next, let's look at how BFS powers web crawlers."
    a "Web crawlers use BFS to systematically visit and index web pages."
    $ chapter_11_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Quiz time: Web crawlers!"
    jump chapter_11_Web_Crawlers_Quiz

label chapter_11_Web_Crawlers_Quiz:
    #5POINTS
    $ chapter_11_Web_Crawlers_quiz = 0
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert quiz questions here)

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_11_Web_Crawlers_quiz] out of 5."
    jump chapter_11_DFS

label chapter_11_DFS:

    a "Now, let's explore {b}Depth-First Search (DFS){/b}."
    a "DFS explores as far as possible along each branch before backtracking."
    $ chapter_11_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Quiz time: DFS!"
    jump chapter_11_DFS_Quiz

label chapter_11_DFS_Quiz:
    #5POINTS
    $ chapter_11_DFS_quiz = 0
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert quiz questions here)

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_11_DFS_quiz] out of 5."
    jump chapter_11_Uniform_Cost

label chapter_11_Uniform_Cost:

    a "Uniform Cost Search is a variant of BFS that considers edge costs."
    a "It uses a priority queue to always expand the lowest-cost node."
    $ chapter_11_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Quiz time: Uniform Cost Search!"
    jump chapter_11_Uniform_Cost_Quiz

label chapter_11_Uniform_Cost_Quiz:
    #5POINTS
    $ chapter_11_Uniform_Cost_quiz = 0
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert quiz questions here)

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_11_Uniform_Cost_quiz] out of 5."
    jump chapter_11_A_Star

label chapter_11_A_Star:

    a "A* Search combines Uniform Cost Search with heuristics."
    a "It finds the shortest path efficiently using cost and estimated distance."
    $ chapter_11_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Quiz time: A* Search!"
    jump chapter_11_A_Star_Quiz

label chapter_11_A_Star_Quiz:
    #5POINTS
    $ chapter_11_A_Star_quiz = 0
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert quiz questions here)

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_11_A_Star_quiz] out of 5."
    jump chapter_11_Iterative_Deepening

label chapter_11_Iterative_Deepening:

    a "Iterative Deepening Search combines the space efficiency of DFS with the completeness of BFS."
    a "It repeatedly applies DFS with increasing depth limits."
    $ chapter_11_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Quiz time: Iterative Deepening!"
    jump chapter_11_Iterative_Deepening_Quiz

label chapter_11_Iterative_Deepening_Quiz:
    #5POINTS
    $ chapter_11_Iterative_Deepening_quiz = 0
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert quiz questions here)

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_11_Iterative_Deepening_quiz] out of 5."
    jump chapter_11_Memory_Management

label chapter_11_Memory_Management:

    a "Let's compare memory management in BFS and DFS."
    a "BFS uses more memory but guarantees shortest paths; DFS uses less memory but may get stuck."
    $ chapter_11_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Quiz time: Memory Management!"
    jump chapter_11_Memory_Management_Quiz

label chapter_11_Memory_Management_Quiz:
    #5POINTS
    $ chapter_11_Memory_Management_quiz = 0
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert quiz questions here)

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_11_Memory_Management_quiz] out of 5."
    jump chapter_11_restart

label chapter_11_restart:
    $ chapter_11_test = (
        chapter_11_BFS_quiz +
        chapter_11_Web_Crawlers_quiz +
        chapter_11_DFS_quiz +
        chapter_11_Uniform_Cost_quiz +
        chapter_11_A_Star_quiz +
        chapter_11_Iterative_Deepening_quiz +
        chapter_11_Memory_Management_quiz
    )

    a "Your score is [chapter_11_test]"
    a "Let's see how well you do in the {size=+20}CHAPTER QUIZ"

    if chapter_10_test <= 7:
        show adrian thoughtful
        jump chapter_11_quiz_easy
    elif chapter_10_test <= 12:
        show adrian smiling
        jump chapter_11_quiz_medium
    else:
        show adrian confident
        jump chapter_11_quiz_hard

label chapter_11_quiz_easy:
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert easy quiz questions here)

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    jump chapter_11_performance

label chapter_11_quiz_medium:
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert medium quiz questions here)

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    jump chapter_11_performance

label chapter_11_quiz_hard:
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert hard quiz questions here)

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    jump chapter_11_performance

label chapter_11_performance:

# BFS
    if chapter_11_BFS_quiz < 2:
        a "You need to review Breadth-First Search."
        a "Focus on queue-based traversal and level-order logic."
    elif chapter_11_BFS_quiz < 3:
        a "You did okay in BFS, but there's room for improvement."
        a "Practice tracing BFS on sample graphs."

# Web Crawlers
    if chapter_11_Web_Crawlers_quiz < 2:
        a "You need to review Web Crawlers."
        a "Understand how BFS powers crawling and indexing."
    elif chapter_11_Web_Crawlers_quiz < 3:
        a "You did okay in Web Crawlers, but there's room for improvement."
        a "Explore how traversal depth affects crawl efficiency."

# DFS
    if chapter_11_DFS_quiz < 2:
        a "You need to review Depth-First Search."
        a "Focus on stack-based traversal and recursive logic."
    elif chapter_11_DFS_quiz < 3:
        a "You did okay in DFS, but there's room for improvement."
        a "Try tracing DFS paths and backtracking behavior."

# Uniform Cost Search
    if chapter_11_Uniform_Cost_quiz < 2:
        a "You need to review Uniform Cost Search."
        a "Understand how priority queues guide cost-based traversal."
    elif chapter_11_Uniform_Cost_quiz < 3:
        a "You did okay in Uniform Cost Search, but there's room for improvement."
        a "Compare it with BFS and Dijkstra’s algorithm."

# A* Search
    if chapter_11_A_Star_quiz < 2:
        a "You need to review A* Search."
        a "Focus on heuristics and cost functions."
    elif chapter_11_A_Star_quiz < 3:
        a "You did okay in A* Search, but there's room for improvement."
        a "Practice designing admissible heuristics."

# Iterative Deepening
    if chapter_11_Iterative_Deepening_quiz < 2:
        a "You need to review Iterative Deepening Search."
        a "Understand how it balances DFS depth with BFS completeness."
    elif chapter_11_Iterative_Deepening_quiz < 3:
        a "You did okay in Iterative Deepening, but there's room for improvement."
        a "Explore its use in memory-constrained environments."

# Memory Management
    if chapter_11_Memory_Management_quiz < 2:
        a "You need to review Memory Management in BFS vs DFS."
        a "Focus on space complexity and trade-offs."
    elif chapter_11_Memory_Management_quiz < 3:
        a "You did okay in Memory Management, but there's room for improvement."
        a "Compare stack vs queue usage and scalability."

    jump chapter_11_end

label chapter_11_end: