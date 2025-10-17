# Chapter 10: Graph Algorithms
# Topics:
# - Graph theory overview
# - Adjacency matrix and adjacency list
# - Application

default chapter_10_progress = 0

default chapter_10_Graph_Theory_quiz = 0
default chapter_10_Adjacency_Representation_quiz = 0
default chapter_10_Applications_quiz = 0

label chapter_10_intro:

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
    a "Welcome to Chapter 10: Graph Algorithms"
    a "You like chess? I like chess"
    a "I like chest-{nw}"
    a "I mean graphs, whatever Im tired"
    show adrian explaining
    a "In this chapter, we'll explore the fascinating world of graphs."
    a "What are Graphs? I dont know, ask your mom."
    show adrian smug
    a "Lmao"
    a "Graphs are mathematical structures used to model pairwise relations between objects."
    show adrian normal
    a "So you know chest right?"
    a "Graphs are kinda like that, but with nodes and edges"
    $ chapter_10_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Let's start with Graph Theory!"
    jump chapter_10_Graph_Theory

label chapter_10_Graph_Theory:

    a "Let’s begin our journey into {b}Graph Theory{/b}, a fundamental area of computer science and mathematics."
    a "Graph Theory explores how objects—called {b}nodes{/b} or {b}vertices{/b}—are connected by {b}edges{/b}."

    a "Graphs come in many forms:"
    a "- {b}Directed graphs{/b} have edges with direction, like one-way streets."
    a "- {b}Undirected graphs{/b} have edges that go both ways, like mutual friendships."
    a "- {b}Weighted graphs{/b} assign values to edges, useful for measuring cost, distance, or time."
    a "- {b}Unweighted graphs{/b} treat all connections equally."

    a "These structures are used everywhere—from modeling computer networks and transportation systems to analyzing social media connections and solving puzzles."

    a "Understanding graphs helps us design efficient algorithms for searching, optimizing, and navigating complex systems."

    $ chapter_10_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Let's check your understanding with a quick quiz!"
    jump chapter_10_Graph_Theory_Quiz

init python:
    import random
    chapter_10_Graph_Theory_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_10_Graph_Theory_order)

label chapter_10_Graph_Theory_Quiz:
    #5POINTS
    $ chapter_10_Graph_Theory_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_10_Graph_Theory_order:
        $ current_q = chapter_10_Graph_Theory_order.pop(0)

        if current_q == "q1":
            a "What is a graph in computer science?"
            menu:
                "A collection of nodes and edges":  # Correct (top)
                    $ chapter_10_Graph_Theory_quiz += 1
                    a "Correct! Graphs model relationships between entities."
                "A sorted list of numbers":
                    a "Incorrect! That’s more like an array."
                "A tree with only one root":
                    a "Incorrect! Trees are a type of graph, but not all graphs are trees."

        elif current_q == "q2":
            a "What do edges in a graph represent?"
            menu:
                "The size of each node":
                    a "Incorrect! Edges don’t describe node size."
                "Connections or relationships between nodes":  # Correct (middle)
                    $ chapter_10_Graph_Theory_quiz += 1
                    a "Correct! Edges define how nodes are linked."
                "The color of each node":
                    a "Incorrect! That’s not a standard graph concept."

        elif current_q == "q3":
            a "Which graph type allows multiple edges between the same pair of nodes?"
            menu:
                "Simple graph":
                    a "Incorrect! Simple graphs allow only one edge per pair."
                "Multigraph":  # Correct (middle)
                    $ chapter_10_Graph_Theory_quiz += 1
                    a "Correct! Multigraphs can have parallel edges."
                "Tree":
                    a "Incorrect! Trees don’t allow cycles or multiple edges."

        elif current_q == "q4":
            a "What is a cycle in a graph?"
            menu:
                "A path that starts and ends at the same node":  # Correct (top)
                    $ chapter_10_Graph_Theory_quiz += 1
                    a "Correct! Cycles revisit the starting node."
                "A node with no edges":
                    a "Incorrect! That’s an isolated node."
                "A graph with only one edge":
                    a "Incorrect! That’s just a minimal connection."

        elif current_q == "q5":
            a "Which of the following is true about directed graphs?"
            menu:
                "Edges have a direction from one node to another":  # Correct (bottom)
                    $ chapter_10_Graph_Theory_quiz += 1
                    a "Correct! Direction matters in digraphs."
                "All edges are bidirectional":
                    a "Incorrect! That’s true for undirected graphs."
                "They cannot contain cycles":
                    a "Incorrect! Directed graphs can have cycles."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_10_Graph_Theory_quiz] out of 5."
    jump chapter_10_Adjacency_Representation
label chapter_10_Adjacency_Representation:

    a "Now that you understand what graphs are, let’s explore how they’re represented in code."
    a "There are two common ways to represent graphs: {b}adjacency matrices{/b} and {b}adjacency lists{/b}."

    a "An {b}adjacency matrix{/b} uses a 2D array where each cell indicates whether a connection exists between two nodes."
    a "If the graph has {i}n{/i} nodes, the matrix is {i}n × n{/i}, and each entry at position [i][j] shows whether there’s an edge from node i to node j."
    a "This method is great for dense graphs where most nodes are connected."

    a "An {b}adjacency list{/b}, on the other hand, stores a list for each node that contains its neighbors."
    a "It’s more memory-efficient for sparse graphs, where many node pairs aren’t connected."

    a "Choosing the right representation depends on the graph’s structure and the operations you need—like checking connections or iterating through neighbors."

    a "Understanding both formats is key to building efficient graph algorithms."

    $ chapter_10_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Let's see how well you understand graph representations!"
    jump chapter_10_Adjacency_Representation_Quiz

init python:
    import random
    chapter_10_Adjacency_Representation_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_10_Adjacency_Representation_order)

label chapter_10_Adjacency_Representation_Quiz:
    #5POINTS
    $ chapter_10_Adjacency_Representation_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_10_Adjacency_Representation_order:
        $ current_q = chapter_10_Adjacency_Representation_order.pop(0)

        if current_q == "q1":
            a "What does an adjacency list store for each node?"
            menu:
                "The degree of the node":
                    a "Incorrect! Degree is a count, not a list."
                "A list of connected nodes":  # Correct (middle)
                    $ chapter_10_Adjacency_Representation_quiz += 1
                    a "Correct! Each node stores its neighbors."
                "The coordinates of the node":
                    a "Incorrect! Graphs don’t require spatial data."

        elif current_q == "q2":
            a "Which representation uses a 2D array to show connections?"
            menu:
                "Adjacency matrix":  # Correct (top)
                    $ chapter_10_Adjacency_Representation_quiz += 1
                    a "Correct! It uses rows and columns to show edges."
                "Adjacency list":
                    a "Incorrect! That uses linked lists or arrays."
                "Edge list":
                    a "Incorrect! That stores edges directly, not in a matrix."

        elif current_q == "q3":
            a "What is the space complexity of an adjacency matrix for a graph with n nodes?"
            menu:
                "O(n^2)":  # Correct (top)
                    $ chapter_10_Adjacency_Representation_quiz += 1
                    a "Correct! Every node pair has a slot in the matrix."
                "O(n)":
                    a "Incorrect! That’s too small for a matrix."
                "O(log n)":
                    a "Incorrect! Logarithmic space doesn’t apply here."

        elif current_q == "q4":
            a "Which representation is more efficient for sparse graphs?"
            menu:
                "Adjacency matrix":
                    a "Incorrect! It wastes space for sparse graphs."
                "Adjacency list":  # Correct (middle)
                    $ chapter_10_Adjacency_Representation_quiz += 1
                    a "Correct! It only stores existing connections."
                "Complete graph":
                    a "Incorrect! That’s a type of graph, not a representation."

        elif current_q == "q5":
            a "What does a 1 in an adjacency matrix indicate?"
            menu:
                "That the node is isolated":
                    a "Incorrect! Isolation would be all 0s."
                "That there is an edge between two nodes":  # Correct (bottom)
                    $ chapter_10_Adjacency_Representation_quiz += 1
                    a "Correct! A 1 means a connection exists."
                "That the graph is directed":
                    a "Incorrect! Direction is shown by position, not value."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_10_Adjacency_Representation_quiz] out of 5."
    jump chapter_10_Applications

label chapter_10_Applications:

    a "Now that you understand how graphs work, let’s explore where they’re used in the real world."
    a "Graphs are incredibly versatile—they show up in {b}routing systems{/b}, {b}social networks{/b}, {b}dependency tracking{/b}, and much more."

    a "For example, in navigation apps, graphs represent cities and roads. Algorithms like Dijkstra’s or A* help find the shortest path from one location to another."
    a "In social media platforms, graphs model users as nodes and friendships or follows as edges—making it easy to analyze connections and suggest new friends."

    a "Graphs also help track dependencies in software projects, where tasks or modules rely on others being completed first."

    a "To work with these graphs, we use algorithms like {b}Breadth-First Search (BFS){/b} and {b}Depth-First Search (DFS){/b}."
    a "These algorithms allow us to explore networks, detect cycles, find paths, and even solve puzzles like mazes or word ladders."

    a "Understanding graph applications helps you design smarter systems—from efficient logistics to intelligent recommendation engines."

    $ chapter_10_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Quiz time: Applications of graphs!"
    jump chapter_10_Applications_Quiz
init python:
    import random
    chapter_10_Applications_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_10_Applications_order)

label chapter_10_Applications_Quiz:
    #5POINTS
    $ chapter_10_Applications_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_10_Applications_order:
        $ current_q = chapter_10_Applications_order.pop(0)

        if current_q == "q1":
            a "Which of the following is a common use of graph theory?"
            menu:
                "Modeling relationships in social networks":  # Correct (top)
                    $ chapter_10_Applications_quiz += 1
                    a "Correct! Graphs are perfect for representing connections between users."
                "Sorting numbers in an array":
                    a "Incorrect! That’s a task for sorting algorithms."
                "Calculating factorials":
                    a "Incorrect! That’s a mathematical operation, not graph-related."

        elif current_q == "q2":
            a "How are graphs used in navigation systems?"
            menu:
                "To store user preferences":
                    a "Incorrect! Preferences are stored separately."
                "To represent locations and routes":  # Correct (middle)
                    $ chapter_10_Applications_quiz += 1
                    a "Correct! Nodes represent locations, and edges represent paths."
                "To display weather updates":
                    a "Incorrect! That’s unrelated to graph structures."

        elif current_q == "q3":
            a "Which graph algorithm helps find the shortest path?"
            menu:
                "Dijkstra’s algorithm":  # Correct (top)
                    $ chapter_10_Applications_quiz += 1
                    a "Correct! It’s widely used in routing and maps."
                "Depth-first search":
                    a "Incorrect! DFS explores paths but doesn’t guarantee shortest."
                "Bubble sort":
                    a "Incorrect! That’s a sorting algorithm."

        elif current_q == "q4":
            a "How can graphs help in scheduling tasks?"
            menu:
                "By modeling dependencies between tasks":  # Correct (bottom)
                    $ chapter_10_Applications_quiz += 1
                    a "Correct! Directed graphs show which tasks must come first."
                "By storing task durations":
                    a "Incorrect! Durations are data, not structure."
                "By counting completed tasks":
                    a "Incorrect! That’s a tracking function, not graph-based."

        elif current_q == "q5":
            a "Which field commonly uses graphs to analyze connections?"
            menu:
                "Social media analytics":  # Correct (top)
                    $ chapter_10_Applications_quiz += 1
                    a "Correct! Graphs reveal patterns in user interactions."
                "Image compression":
                    a "Incorrect! That uses different algorithms."
                "Audio mixing":
                    a "Incorrect! Graphs aren’t central to that process."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_10_Applications_quiz] out of 5."
    jump chapter_10_restart

label chapter_10_restart:
    $ chapter_10_test = (
        chapter_10_Graph_Theory_quiz +
        chapter_10_Adjacency_Representation_quiz +
        chapter_10_Applications_quiz
    )

    a "Your score is [chapter_10_test]"
    a "Let's see how well you do in the {size=+20}CHAPTER QUIZ"

    if chapter_9_test <= 7:
        show adrian thoughtful
        jump chapter_10_quiz_easy
    elif chapter_9_test <= 12:
        show adrian smiling
        jump chapter_10_quiz_medium
    else:
        show adrian confident
        jump chapter_10_quiz_hard

label chapter_10_quiz_easy:
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert easy quiz questions here)

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    jump chapter_10_performance

label chapter_10_quiz_medium:
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert medium quiz questions here)

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    jump chapter_10_performance

label chapter_10_quiz_hard:
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert hard quiz questions here)

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    jump chapter_10_performance

label chapter_10_performance:

# Graph Theory
    if chapter_10_Graph_Theory_quiz < 2:
        a "You need to review Graph Theory basics."
        a "Focus on nodes, edges, and types of graphs like directed and undirected."
    elif chapter_10_Graph_Theory_quiz < 3:
        a "You did okay in Graph Theory, but there's room for improvement."
        a "Revisit terminology and graph classifications."

# Adjacency Matrix & List
    if chapter_10_Adjacency_Representation_quiz < 2:
        a "You need to review Adjacency Matrix and List representations."
        a "Understand how each structure stores connections and their trade-offs."
    elif chapter_10_Adjacency_Representation_quiz < 3:
        a "You did okay in Adjacency Representation, but there's room for improvement."
        a "Practice converting between matrix and list formats."

# Applications
    if chapter_10_Applications_quiz < 2:
        a "You need to review Graph Applications."
        a "Explore how graphs are used in routing, social networks, and dependency tracking."
    elif chapter_10_Applications_quiz < 3:
        a "You did okay in Applications, but there's room for improvement."
        a "Look into real-world problems solved using graph algorithms like BFS and DFS."

    jump chapter_10_end

label chapter_10_end: