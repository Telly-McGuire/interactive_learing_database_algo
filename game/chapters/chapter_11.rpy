# Chapter 11: Graph Traversal Algorithms
# Topics:
# - Breadth-first search introduction
# - Introduction to web crawlers
# - Depth-first search introduction
# - Uniform cost search algorithm
# - A* search algorithm
# - Iterative deepening search
# - Memory management: BFS vs DFS

label chapter_11_intro:

label chapter_11_BFS:
label chapter_11_BFS_Quiz:
    #5POINTS
    $ chapter_11_BFS_quiz = 0

label chapter_11_Web_Crawlers:
label chapter_11_Web_Crawlers_Quiz:
    #5POINTS
    $ chapter_11_Web_Crawlers_quiz = 0

label chapter_11_DFS:
label chapter_11_DFS_Quiz:
    #5POINTS
    $ chapter_11_DFS_quiz = 0

label chapter_11_Uniform_Cost:
label chapter_11_Uniform_Cost_Quiz:
    #5POINTS
    $ chapter_11_Uniform_Cost_quiz = 0

label chapter_11_A_Star:
label chapter_11_A_Star_Quiz:
    #5POINTS
    $ chapter_11_A_Star_quiz = 0

label chapter_11_Iterative_Deepening:
label chapter_11_Iterative_Deepening_Quiz:
    #5POINTS
    $ chapter_11_Iterative_Deepening_quiz = 0

label chapter_11_Memory_Management:
label chapter_11_Memory_Management_Quiz:
    #5POINTS
    $ chapter_11_Memory_Management_quiz = 0

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
label chapter_11_quiz_medium:
label chapter_11_quiz_hard:

label chapter_11_quiz_end:
    a "Your total score is [chapter_11_test] out of 35"
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