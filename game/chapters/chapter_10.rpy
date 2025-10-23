# Chapter 10: Graph Algorithms
# Topics:
# - Graph theory overview
# - Adjacency matrix and adjacency list
# - Application

default chapter_10_progress = 0

default chapter_10_Graph_Theory_quiz = 0
default chapter_10_Adjacency_Representation_quiz = 0
default chapter_10_Applications_quiz = 0


screen chapter_10_GAintro:  
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 200
        ypadding 60
        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5
            text "Graph Algorithms" size 60 color "#FFFFFF" outlines [(5, "#000000", 0, 0)]
label chapter_10_intro:

    call hideall
    play sound "sfx/start.mp3"
    stop music fadeout 1.0

    scene black
    pause 1.0

    show screen chapter_10_GAintro
    scene mt tree with dissolve
    pause 2.0
    hide screen chapter_10_GAintro

    show screen menu_btn

    play music "bgm/city-high-life.mp3" fadein 1.0
    show adrian smiling at center:
        smaller
    with dissolve

    show adrian normal
    a "Welcome to Chapter 10: Graph Algorithms"
    a "You like chess? I like chess"
    show adrian smug
    a "I like chest-{nw}"
    show adrian nocomment
    a "I mean graphs"
    a "Just like the grids in chess, graphs are made up of nodes and edges connecting them."
    show adrian explaining
    a "In this chapter, we'll explore graphs."
    a "What are Graphs?"
    show adrian happy
    a "{cps=5}IDK"
    show adrian smiling
    a "Lmao"
    a "Graphs are mathematical structures used to model pairwise relations between objects."

    $ chapter_10_progress += 1
    show adrian smiling
    jump chapter_10_Graph_Theory


label chapter_10_Graph_Theory:

    image g_example = "assets/g_example.png"

    show adrian explaining 
    a "Let’s begin our journey into {b}Graph Theory{/b}, a fundamental area of computer science and mathematics."
    a "Graph Theory explores how objects—called {b}nodes{/b} or {b}vertices{/b}—are connected by {b}edges{/b}."
    show adrian smiling at left
    with move

    transform graphs:
        zoom 0.4
        yalign 0.5
        xalign 0.75

    show g_example:
        graphs
    with dissolve

    a "Here’s a simple graph example:"
    a "{b}Nodes{/b} are the individual points, while edges are the lines that link them together."
    a "{b}Edges{/b} are the connections between nodes."

    hide g_example

    a "Graphs come in many forms:"

    image directed = "assets/g_directed.png"
    image undirected = "assets/g_undirected.png"
    image weighted = "assets/g_weighted.png"

    show adrian at left
    with move
    show directed:
        graphs
    with dissolve
    a "- {b}Directed graphs{/b} have edges with direction, like one-way streets."
    hide directed

    show undirected:
        graphs
    with dissolve   
    a "- {b}Undirected graphs{/b} have edges that go both ways, like mutual friendships."
    hide undirected

    show weighted:
        graphs
    with dissolve
    a "- {b}Weighted graphs{/b} assign values to edges, useful for measuring cost, distance, or time."
    hide weighted

    show undirected:
        graphs
    with dissolve   
    a "- {b}Unweighted graphs{/b} treat all connections equally."
    hide undirected

    image motherboard = "assets/motherboard.png"
    image social_network = "assets/social_network.png"
    image transport_network = "assets/train_network.png"
    image purble = "assets/purble.png"



    show adrian explaining at center
    with move

    pause 0.5
    show motherboard at top_left:
        smaller
    with dissolve
    pause 0.2

    show social_network at top_right:
        smaller
    with dissolve
    pause 0.2

    show transport_network at bottom_left:
        even_smaller
    with dissolve
    pause 0.2

    show purble at bottom_right
    with dissolve

    a "These structures are used everywhere—from modeling computer networks and transportation systems to analyzing social media connections and solving puzzles."
    a "Understanding graph theory is essential for designing efficient algorithms and data structures."
    show adrian nocomment
    a "..."
    a "Yeah I know that PNG Is too {size=+100}{cps=3}big"
    show adrian smiling
    a "But hey, it looks cool right?"
    hide motherboard
    hide social_network
    hide transport_network
    hide purble


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

    show adrian normal
    a "Now that you understand what graphs are, let’s explore how they’re represented in code."

    show adrian explaining
    a "There are two common ways to represent graphs: {b}adjacency matrices{/b} and {b}adjacency lists{/b}."

    a "An {b}adjacency matrix{/b} uses a 2D array where each cell indicates whether a connection exists between two nodes."
    a "So basically its a grid of relationships"

    show adrian normal
    a "Its as simple as that"
    a "Let us borrow some images from {color=#00aa00}{a=https://www.geeksforgeeks.org/dsa/adjacency-matrix/#1-adjacency-matrix-for-undirected-and-unweighted-graph}GeeksforGeeks{/a}{/color}. Thats an actual Link btw, you can click it"
    
    a "For example"


    image am1 = "assets/am_dud.png"
    image am2 = "assets/am_unuw.png"
    image am3 = "assets/am_dw.png"
    image am4 = "assets/am_unw.png"
    image monke = "assets/le_monke.png"


    show adrian at left
    with move
    show am1 at right:
        matrices
    with dissolve
    a "{b}Adjacency Matrix for Undirected and Unweighted Graph "
    show adrian explaining
    a "An adjacency matrix is a 2D array used to represent a graph." 
    a "Each cell [[i][[j] contains a 1 if there's an edge between node i and node j, and 0 otherwise."
    a "Since the graph is undirected, the matrix is symmetric." 
    a "And because it's unweighted, all edges are represented by 1s instead of weights."
    hide am1

    show am2 at right:
        matrices
    with dissolve
    show adrian normal
    a"{b}Adjacency Matrix for Undirected and Weighted Graph"
    show adrian explaining
    a "In this type of graph, the adjacency matrix stores the weights of the edges between nodes."
    a "If there's an edge between node i and node j, the cell [[i][[j] contains the weight of that edge."
    a "Since the graph is undirected, the matrix is symmetric: [[i][[j] equals [[j][[i]."
    a "If there's no edge between two nodes, the corresponding cell typically contains 0 or a special value like ∞ to indicate no connection."
    hide am2

    show am3 at right:
        matrices
    with dissolve
    show adrian normal
    a "{b}Adjacency Matrix for Directed and Unweighted Graph"
    show adrian explaining
    a "In a directed graph, edges have direction—going from one node to another."
    a "The adjacency matrix uses 1s to indicate the presence of an edge from node i to node j."
    a "Unlike undirected graphs, the matrix is not symmetric: [[i][[j] may be 1 while [[j][[i] is 0."
    a "Since it's unweighted, all edges are represented by 1s, and 0s indicate no edge."
    hide am3

    show monke at right:
        matrices
    with dissolve
    show adrian normal
    a "{b}Adjacency Matrix for Directed-{nw}"
    show adrian shock
    a "{b}{cps=30}{size=+50}MONKE?"
    "Banan"
    show adrian nocomment
    a "..."
    a "We dont...have a banana"
    
    "..."
    "..."
    "..."

    a "Were kinda busy here"

    "Banan"
    play sound "sfx/cave_sound.mp3"
    hide monke
    with dissolve
    a "I...I dont know what that was"
    a "Anyways"

    show am4 at right:
        matrices
    with dissolve
    show adrian normal
    a "As I was saying"
    a "{b}Adjacency Matrix for Directed and Weighted Graph"
    show adrian explaining
    a "In this graph type, edges have direction and carry weights."
    a "The adjacency matrix stores the weight of the edge from node i to node j in cell [[i][[j]."
    a "If there's no edge from {b}{i}i to j{/b}{/i}, the cell typically contains 0 or ∞ to indicate no connection."
    a "Because the graph is directed, [[i][[j] and [[j][[i] can hold different values, making the matrix asymmetric."
    hide am4


    show adrian happy at center
    with move
    a "This method is great for dense graphs where most nodes are connected."

    image al_dg1 = "assets/al_dg1.png"
    image al_dg2 = "assets/al_dg2.png"
    image al_dg3 = "assets/al_dg3.png"
    image al_dg4 = "assets/al_dg4.png"

    show adrian normal
    a "An {b}adjacency list{/b}, on the other hand, stores a list for each node that contains its neighbors."
    a "It’s more memory-efficient for sparse graphs, where many node pairs aren’t connected."

    a "Here is an example of an Adjency List"
    show adrian at left 
    with move
    show al_dg1 at right:
        matrices
    with dissolve
    a "{b}Adjacency List for Directed Graph"
    a "Here is the relationship of it"
    a "An example of the relationship between them"
    hide al_dg1 

    show al_dg2 at right:
        matrices
    with dissolve 
    a "Like since 1 goes to 0 and 2 it reflects that as well"
    hide al_dg2
    
    show al_dg3 at right:
        matrices
    with dissolve
    hide al_dg3

    show al_dg4 at right:
        matrices
    with dissolve
    a "And you can see the relationship with all of it"
    a "Got it?"
    hide al_dg4
    with dissolve

    image al_ug1 = "assets/al_ug1.png"
    image al_ug2 = "assets/al_ug2.png"
    image al_ug3 = "assets/al_ug3.png"  
    image al_ug4 = "assets/al_ug4.png"

    a "How would Undirected Graphs would act?"
    show al_ug1 at right:
        matrices
    with dissolve
    a "{b}Adjacency List for Undirected Graph"
    a "Since there is no direct connection to it, it has a wider range for relationships"
    hide al_ug1

    show al_ug2 at right:
        matrices
    with dissolve 
    a "Like 1 goes to 0 and 1 goes to 0 as well"
    hide al_ug2
    
    show al_ug3 at right:
        matrices
    with dissolve
    hide al_ug3

    show al_ug4 at right:
        matrices
    with dissolve
    a "And you can see the relationship with all of it"
    a "Pretty Intersting if you dive deeper into it"
    hide al_ug4
    with dissolve


    show adrian at center
    with move
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
    image gmap = "assets/g_map.png"
    image dependency = "assets/dependency.png"


    a "Now that you understand how graphs work, let’s explore where they’re used in the real world."
    a "Graphs are incredibly versatile—they show up in {b}routing systems{/b}, {b}social networks{/b}, {b}dependency tracking{/b}, and much more."

    show adrian at left
    with move
    show gmap at right:
        gmap

    with dissolve
    a "For example, in navigation apps, graphs represent cities and roads. Algorithms like Dijkstra’s or A* help find the shortest path from one location to another."
    hide gmap

    show social_network at right:
        matrices
    with dissolve
    a "In social media platforms, graphs model users as nodes and friendships or follows as edges—making it easy to analyze connections and suggest new friends."
    hide social_network
    
    show dependency at right:
        matrices
    with dissolve
    a "Graphs also help track dependencies in software projects, where tasks or modules rely on others being completed first."


    a "To work with these graphs, we use algorithms like {b}Breadth-First Search (BFS){/b} and {b}Depth-First Search (DFS){/b}."
    a "These algorithms allow us to explore networks, detect cycles, find paths, and even solve puzzles like mazes or word ladders."
    hide dependency
    with dissolve

    show adrian at center
    with move
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