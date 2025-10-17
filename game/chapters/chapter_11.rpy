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

    a "First up in graph traversal algorithms is {b}Breadth-First Search (BFS){/b}."
    a "BFS explores a graph level by level, starting from a chosen node and visiting all its neighbors before moving deeper."

    a "It uses a {b}queue{/b} to keep track of which nodes to visit next, ensuring that the closest nodes are processed first."
    a "This makes BFS ideal for finding the shortest path in unweighted graphs, or for exploring all reachable nodes from a starting point."

    a "BFS is commonly used in social networks, recommendation systems, and even puzzle solvers like mazes or word ladders."

    a "Understanding how BFS works helps you design algorithms that are both efficient and predictable in their exploration."

    $ chapter_11_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Let's check your understanding with a quick quiz!"
    jump chapter_11_BFS_Quiz

init python:
    import random
    chapter_11_BFS_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_11_BFS_order)

label chapter_11_BFS_Quiz:
    #5POINTS
    $ chapter_11_BFS_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_11_BFS_order:
        $ current_q = chapter_11_BFS_order.pop(0)

        if current_q == "q1":
            a "What data structure is used in Breadth-First Search?"
            menu:
                "Stack":
                    a "Incorrect! Stacks are used in DFS."
                "Queue":  # Correct (middle)
                    $ chapter_11_BFS_quiz += 1
                    a "Correct! BFS uses a queue to explore nodes level by level."
                "Heap":
                    a "Incorrect! Heaps are used in priority-based algorithms."

        elif current_q == "q2":
            a "Which graph traversal explores all neighbors before going deeper?"
            menu:
                "Depth-First Search":
                    a "Incorrect! DFS dives deep before exploring siblings."
                "Breadth-First Search":  # Correct (middle)
                    $ chapter_11_BFS_quiz += 1
                    a "Correct! BFS visits all neighbors first."
                "Binary Search":
                    a "Incorrect! That’s used for sorted arrays, not graphs."

        elif current_q == "q3":
            a "What is the time complexity of BFS for a graph with V vertices and E edges?"
            menu:
                "O(V + E)":  # Correct (top)
                    $ chapter_11_BFS_quiz += 1
                    a "Correct! BFS visits each vertex and edge once."
                "O(V^2)":
                    a "Incorrect! That’s typical of adjacency matrices in dense graphs."
                "O(log V)":
                    a "Incorrect! BFS doesn’t use logarithmic time."

        elif current_q == "q4":
            a "Which of the following is a typical application of BFS?"
            menu:
                "Finding shortest path in unweighted graphs":  # Correct (bottom)
                    $ chapter_11_BFS_quiz += 1
                    a "Correct! BFS guarantees shortest paths in unweighted graphs."
                "Sorting elements":
                    a "Incorrect! Sorting is unrelated to BFS."
                "Detecting prime numbers":
                    a "Incorrect! That’s a number theory task."

        elif current_q == "q5":
            a "How does BFS avoid revisiting nodes?"
            menu:
                "By using a visited set or array":  # Correct (top)
                    $ chapter_11_BFS_quiz += 1
                    a "Correct! This prevents cycles and redundant work."
                "By skipping leaf nodes":
                    a "Incorrect! Leaf nodes may still be valid targets."
                "By using recursion":
                    a "Incorrect! BFS is typically iterative."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_11_BFS_quiz] out of 5."
    jump chapter_11_Web_Crawlers

label chapter_11_Web_Crawlers:

    a "Next, let’s explore a real-world application of Breadth-First Search: {b}web crawlers{/b}."
    a "Web crawlers are automated programs that browse the internet to collect and index information from websites."

    a "They use BFS to systematically explore web pages—starting from a seed URL, then visiting all the links on that page before moving deeper into the web."
    a "This level-by-level approach ensures that the crawler doesn’t get stuck going too deep into one site while ignoring others."

    a "Search engines like Google use web crawlers to build massive indexes of the internet, making it possible to retrieve relevant results in milliseconds."

    a "BFS helps ensure that the most accessible and widely linked pages are discovered early, which is crucial for keeping search results fresh and comprehensive."

    $ chapter_11_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Quiz time: Web crawlers!"
    jump chapter_11_Web_Crawlers_Quiz

init python:
    import random
    chapter_11_Web_Crawlers_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_11_Web_Crawlers_order)

label chapter_11_Web_Crawlers_Quiz:
    #5POINTS
    $ chapter_11_Web_Crawlers_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_11_Web_Crawlers_order:
        $ current_q = chapter_11_Web_Crawlers_order.pop(0)

        if current_q == "q1":
            a "What is the main purpose of a web crawler?"
            menu:
                "To download and index web pages":  # Correct (top)
                    $ chapter_11_Web_Crawlers_quiz += 1
                    a "Correct! Crawlers help search engines discover and organize content."
                "To display ads on websites":
                    a "Incorrect! That’s handled by ad networks."
                "To encrypt website data":
                    a "Incorrect! Encryption is a security function, not crawling."

        elif current_q == "q2":
            a "Which algorithm is commonly used by web crawlers to explore pages?"
            menu:
                "Depth-First Search":
                    a "Incorrect! DFS can miss closer or more relevant pages early."
                "Breadth-First Search":  # Correct (middle)
                    $ chapter_11_Web_Crawlers_quiz += 1
                    a "Correct! BFS ensures pages are explored level by level."
                "Binary Search":
                    a "Incorrect! Binary search is for sorted data, not graphs."

        elif current_q == "q3":
            a "How does a crawler avoid visiting the same page multiple times?"
            menu:
                "By using a visited set or URL tracker":  # Correct (top)
                    $ chapter_11_Web_Crawlers_quiz += 1
                    a "Correct! This prevents loops and redundant work."
                "By skipping all external links":
                    a "Incorrect! External links may still be valid targets."
                "By deleting old pages":
                    a "Incorrect! Deletion isn’t part of crawling logic."

        elif current_q == "q4":
            a "What kind of structure does a web crawler treat the internet as?"
            menu:
                "A sorted list":
                    a "Incorrect! The web isn’t sorted."
                "A graph of interconnected pages":  # Correct (middle)
                    $ chapter_11_Web_Crawlers_quiz += 1
                    a "Correct! Each page is a node, and links are edges."
                "A stack of documents":
                    a "Incorrect! That’s not how crawling is modeled."

        elif current_q == "q5":
            a "Why is BFS useful for web crawling?"
            menu:
                "It finds the shortest path between pages":
                    a "Incorrect! That’s not the goal of crawling."
                "It prioritizes deeper pages first":
                    a "Incorrect! That’s DFS behavior."
                "It explores pages in layers, starting from the root":  # Correct (bottom)
                    $ chapter_11_Web_Crawlers_quiz += 1
                    a "Correct! BFS helps discover nearby pages before going deeper."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_11_Web_Crawlers_quiz] out of 5."
    jump chapter_11_DFS

label chapter_11_DFS:

    a "Now, let’s explore another powerful graph traversal algorithm: {b}Depth-First Search (DFS){/b}."
    a "Unlike BFS, which explores level by level, DFS dives deep into each branch before backtracking."

    a "DFS starts at a chosen node and explores as far as it can go along one path, only returning when it hits a dead end."
    a "It uses a {b}stack{/b}—either explicitly or through recursion—to keep track of the path it’s following."

    a "This makes DFS ideal for tasks like detecting cycles, solving puzzles, and exploring all possible paths in a maze or game tree."

    a "DFS is also useful in topological sorting, connected component analysis, and many other graph-based algorithms."

    a "Understanding how DFS works helps you build algorithms that are thorough and flexible in their exploration."

    $ chapter_11_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Quiz time: DFS!"
    jump chapter_11_DFS_Quiz

init python:
    import random
    chapter_11_DFS_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_11_DFS_order)

label chapter_11_DFS_Quiz:
    #5POINTS
    $ chapter_11_DFS_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_11_DFS_order:
        $ current_q = chapter_11_DFS_order.pop(0)

        if current_q == "q1":
            a "What data structure is typically used in Depth-First Search?"
            menu:
                "Queue":
                    a "Incorrect! Queues are used in BFS."
                "Stack":  # Correct (middle)
                    $ chapter_11_DFS_quiz += 1
                    a "Correct! DFS uses a stack to backtrack through nodes."
                "Heap":
                    a "Incorrect! Heaps are used in priority-based algorithms."

        elif current_q == "q2":
            a "Which traversal method explores as far as possible along each branch before backtracking?"
            menu:
                "Breadth-First Search":
                    a "Incorrect! BFS explores level by level."
                "Depth-First Search":  # Correct (middle)
                    $ chapter_11_DFS_quiz += 1
                    a "Correct! DFS dives deep before backtracking."
                "Binary Search":
                    a "Incorrect! That’s for sorted arrays, not graphs."

        elif current_q == "q3":
            a "What is the time complexity of DFS for a graph with V vertices and E edges?"
            menu:
                "O(V + E)":  # Correct (top)
                    $ chapter_11_DFS_quiz += 1
                    a "Correct! DFS visits each vertex and edge once."
                "O(V^2)":
                    a "Incorrect! That’s typical of dense adjacency matrices."
                "O(log V)":
                    a "Incorrect! DFS doesn’t run in logarithmic time."

        elif current_q == "q4":
            a "Which of the following is a common use of DFS?"
            menu:
                "Finding shortest paths in unweighted graphs":
                    a "Incorrect! That’s BFS’s strength."
                "Detecting cycles in a graph":  # Correct (middle)
                    $ chapter_11_DFS_quiz += 1
                    a "Correct! DFS is great for cycle detection."
                "Sorting numbers":
                    a "Incorrect! That’s unrelated to graph traversal."

        elif current_q == "q5":
            a "How does DFS avoid revisiting nodes?"
            menu:
                "By skipping leaf nodes":
                    a "Incorrect! Leaf nodes may still be valid."
                "By using a visited set or array":  # Correct (bottom)
                    $ chapter_11_DFS_quiz += 1
                    a "Correct! This prevents infinite loops and redundancy."
                "By using a queue":
                    a "Incorrect! Queues are used in BFS."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_11_DFS_quiz] out of 5."
    jump chapter_11_Uniform_Cost
label chapter_11_Uniform_Cost:

    a "Let’s take Breadth-First Search one step further with {b}Uniform Cost Search (UCS){/b}."
    a "UCS is a variant of BFS that takes {b}edge costs{/b} into account, making it ideal for weighted graphs."

    a "Instead of exploring nodes in simple layers, UCS uses a {b}priority queue{/b} to always expand the node with the {i}lowest total cost{/i} from the starting point."
    a "This means it doesn’t just look for the shortest path in terms of steps—it looks for the {b}cheapest path{/b} based on actual weights."

    a "UCS guarantees finding the optimal path as long as all edge costs are non-negative."
    a "It’s commonly used in routing systems, logistics planning, and any scenario where cost matters more than distance."

    a "Understanding UCS helps you design smarter algorithms for real-world problems that involve trade-offs and weighted decisions."

    $ chapter_11_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Quiz time: Uniform Cost Search!"
    jump chapter_11_Uniform_Cost_Quiz
init python:
    import random
    chapter_11_Uniform_Cost_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_11_Uniform_Cost_order)

label chapter_11_Uniform_Cost_Quiz:
    #5POINTS
    $ chapter_11_Uniform_Cost_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_11_Uniform_Cost_order:
        $ current_q = chapter_11_Uniform_Cost_order.pop(0)

        if current_q == "q1":
            a "What is the main goal of Uniform Cost Search?"
            menu:
                "To explore all nodes in a graph":
                    a "Incorrect! UCS focuses on cost efficiency."
                "To find the least-cost path to a goal":  # Correct (middle)
                    $ chapter_11_Uniform_Cost_quiz += 1
                    a "Correct! UCS expands paths based on cumulative cost."
                "To find the shortest path in terms of steps":
                    a "Incorrect! That’s BFS’s strength in unweighted graphs."

        elif current_q == "q2":
            a "Which data structure does UCS use to manage paths?"
            menu:
                "Stack":
                    a "Incorrect! That’s used in DFS."
                "Priority queue":  # Correct (bottom)
                    $ chapter_11_Uniform_Cost_quiz += 1
                    a "Correct! UCS uses a priority queue to expand the lowest-cost path first."
                "Hash table":
                    a "Incorrect! That’s used for fast lookups, not path management."

        elif current_q == "q3":
            a "How does UCS differ from BFS?"
            menu:
                "UCS considers path cost, while BFS does not":  # Correct (top)
                    $ chapter_11_Uniform_Cost_quiz += 1
                    a "Correct! UCS expands based on cost, not depth."
                "UCS uses a stack":
                    a "Incorrect! UCS uses a priority queue."
                "BFS is slower than UCS":
                    a "Incorrect! BFS can be faster in unweighted graphs."

        elif current_q == "q4":
            a "What happens when UCS finds a goal node?"
            menu:
                "It continues searching for cheaper paths":
                    a "Incorrect! UCS stops once the least-cost goal is found."
                "It returns the path with the lowest total cost":  # Correct (middle)
                    $ chapter_11_Uniform_Cost_quiz += 1
                    a "Correct! UCS guarantees optimality if costs are non-negative."
                "It resets the search":
                    a "Incorrect! UCS doesn’t restart once a goal is found."

        elif current_q == "q5":
            a "Which of the following is true about UCS?"
            menu:
                "It always finds the fastest route":
                    a "Incorrect! UCS finds the cheapest, not necessarily fastest."
                "It guarantees the optimal path if costs are non-negative":  # Correct (bottom)
                    $ chapter_11_Uniform_Cost_quiz += 1
                    a "Correct! That’s UCS’s key strength."
                "It ignores edge weights":
                    a "Incorrect! UCS is built around edge weights."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_11_Uniform_Cost_quiz] out of 5."
    jump chapter_11_A_Star

label chapter_11_A_Star:

    a "Let’s wrap up our graph traversal toolkit with one of the most powerful algorithms: {b}A* Search{/b}."
    a "A* combines the strengths of {b}Uniform Cost Search{/b} and {b}heuristics{/b} to find the shortest path efficiently."

    a "It uses a priority queue to explore paths based on two factors:"
    a "- The actual cost from the start node to the current node."
    a "- An estimated cost from the current node to the goal, provided by a heuristic function."

    a "This combination allows A* to make smart decisions about which paths to explore, often reaching the goal faster than other algorithms."

    a "A* is widely used in navigation systems, game AI, robotics, and any application where finding an optimal path matters."

    a "Its success depends on choosing a good heuristic—one that’s {i}admissible{/i} (never overestimates) and {i}consistent{/i} (respects triangle inequality)."

    a "Understanding A* helps you design intelligent systems that balance speed and accuracy in decision-making."

    $ chapter_11_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Quiz time: A* Search!"
    jump chapter_11_A_Star_Quiz
init python:
    import random
    chapter_11_A_Star_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_11_A_Star_order)

label chapter_11_A_Star_Quiz:
    #5POINTS
    $ chapter_11_A_Star_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_11_A_Star_order:
        $ current_q = chapter_11_A_Star_order.pop(0)

        if current_q == "q1":
            a "What does A* Search combine to make decisions?"
            menu:
                "Depth and breadth":
                    a "Incorrect! That describes traversal style, not cost."
                "Actual cost and heuristic estimate":  # Correct (middle)
                    $ chapter_11_A_Star_quiz += 1
                    a "Correct! A* uses both g(n) and h(n) to guide its search."
                "Random sampling and backtracking":
                    a "Incorrect! A* is deterministic and goal-directed."

        elif current_q == "q2":
            a "What is the role of the heuristic function in A*?"
            menu:
                "To estimate the cost from a node to the goal":  # Correct (top)
                    $ chapter_11_A_Star_quiz += 1
                    a "Correct! The heuristic helps prioritize promising paths."
                "To store visited nodes":
                    a "Incorrect! That’s handled by a separate structure."
                "To track the shortest path":
                    a "Incorrect! The heuristic guides, but doesn’t track paths."

        elif current_q == "q3":
            a "What makes A* optimal?"
            menu:
                "It always expands the deepest node":
                    a "Incorrect! That’s DFS behavior."
                "It uses a priority queue":
                    a "Incorrect! That’s necessary but not sufficient."
                "It finds the least-cost path if the heuristic is admissible":  # Correct (bottom)
                    $ chapter_11_A_Star_quiz += 1
                    a "Correct! Admissible heuristics ensure optimality."

        elif current_q == "q4":
            a "Which of the following is true about admissible heuristics?"
            menu:
                "They never overestimate the true cost":  # Correct (top)
                    $ chapter_11_A_Star_quiz += 1
                    a "Correct! That’s the key property of admissibility."
                "They always underestimate the cost":
                    a "Incorrect! They may match the true cost."
                "They ignore the goal node":
                    a "Incorrect! Heuristics are goal-focused."

        elif current_q == "q5":
            a "Why is A* more efficient than Uniform Cost Search in many cases?"
            menu:
                "It uses a heuristic to guide the search":  # Correct (bottom)
                    $ chapter_11_A_Star_quiz += 1
                    a "Correct! The heuristic helps A* avoid unnecessary paths."
                "It skips all visited nodes":
                    a "Incorrect! A* may revisit nodes if a cheaper path is found."
                "It uses depth-first logic":
                    a "Incorrect! A* is not depth-first."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_11_A_Star_quiz] out of 5."
    jump chapter_11_Iterative_Deepening

label chapter_11_Iterative_Deepening:

    a "Let’s wrap up our exploration of search strategies with {b}Iterative Deepening Search (IDS){/b}."
    a "IDS cleverly combines the {b}space efficiency{/b} of Depth-First Search with the {b}completeness{/b} of Breadth-First Search."

    a "Here’s how it works:"
    a "- It performs DFS repeatedly, but with a depth limit that increases each time."
    a "- On each iteration, it explores the graph up to a certain depth, then starts over with a deeper limit."

    a "This approach ensures that the algorithm doesn’t miss shallow solutions like DFS might, and it doesn’t consume as much memory as BFS."

    a "Although it may seem repetitive, IDS is surprisingly efficient—especially when the branching factor is low and the solution is not too deep."

    a "It’s often used in scenarios like game trees, puzzle solvers, and AI planning systems where memory is limited but completeness is essential."

    $ chapter_11_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Quiz time: Iterative Deepening!"
    jump chapter_11_Iterative_Deepening_Quiz

init python:
    import random
    chapter_11_Iterative_Deepening_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_11_Iterative_Deepening_order)

label chapter_11_Iterative_Deepening_Quiz:
    #5POINTS
    $ chapter_11_Iterative_Deepening_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_11_Iterative_Deepening_order:
        $ current_q = chapter_11_Iterative_Deepening_order.pop(0)

        if current_q == "q1":
            a "What does Iterative Deepening Search combine?"
            menu:
                "Depth-first and breadth-first strategies":  # Correct (top)
                    $ chapter_11_Iterative_Deepening_quiz += 1
                    a "Correct! IDS performs DFS repeatedly with increasing depth limits."
                "Binary and linear search":
                    a "Incorrect! Those are array-based search methods."
                "Uniform cost and greedy search":
                    a "Incorrect! Those are cost-based algorithms."

        elif current_q == "q2":
            a "Why is IDS memory-efficient?"
            menu:
                "It uses a queue to store all paths":
                    a "Incorrect! That’s BFS behavior."
                "It only stores a single path at a time":  # Correct (middle)
                    $ chapter_11_Iterative_Deepening_quiz += 1
                    a "Correct! Like DFS, it uses minimal memory."
                "It compresses the graph before searching":
                    a "Incorrect! IDS doesn’t alter the graph structure."

        elif current_q == "q3":
            a "What is the main drawback of IDS?"
            menu:
                "It uses too much memory":
                    a "Incorrect! IDS is memory-efficient."
                "It repeats searches at each depth level":  # Correct (middle)
                    $ chapter_11_Iterative_Deepening_quiz += 1
                    a "Correct! This redundancy increases runtime."
                "It ignores goal nodes":
                    a "Incorrect! IDS still checks for goals."

        elif current_q == "q4":
            a "What does IDS do when the depth limit is reached?"
            menu:
                "It switches to BFS":
                    a "Incorrect! IDS continues with deeper DFS."
                "It increases the limit and restarts the search":  # Correct (bottom)
                    $ chapter_11_Iterative_Deepening_quiz += 1
                    a "Correct! Each iteration explores one level deeper."
                "It stops and returns failure":
                    a "Incorrect! IDS is designed to retry with deeper limits."

        elif current_q == "q5":
            a "Which scenario is ideal for using IDS?"
            menu:
                "When memory is limited but completeness is required":  # Correct (top)
                    $ chapter_11_Iterative_Deepening_quiz += 1
                    a "Correct! IDS balances low memory use with guaranteed goal discovery."
                "When the graph is weighted":
                    a "Incorrect! IDS doesn’t handle weights."
                "When the goal is always at the deepest level":
                    a "Incorrect! IDS performs best when goal depth is unknown."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_11_Iterative_Deepening_quiz] out of 5."
    jump chapter_11_Memory_Management
label chapter_11_Memory_Management:

    a "Let’s compare how {b}Breadth-First Search (BFS){/b} and {b}Depth-First Search (DFS){/b} manage memory during graph traversal."

    a "BFS explores nodes level by level and uses a {b}queue{/b} to keep track of all frontier nodes."
    a "This means it can consume a lot of memory—especially in wide graphs—because it stores every node at the current depth before moving on."

    a "However, BFS guarantees the {b}shortest path{/b} in unweighted graphs, making it ideal when accuracy is more important than memory usage."

    a "DFS, on the other hand, dives deep into one path using a {b}stack{/b} or recursion."
    a "It uses much less memory since it only needs to remember the current path, but it can get stuck exploring long or irrelevant branches."

    a "Choosing between BFS and DFS often depends on the problem’s structure and constraints—whether you need optimal paths or minimal memory usage."

    $ chapter_11_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Quiz time: Memory Management!"
    jump chapter_11_Memory_Management_Quiz

init python:
    import random
    chapter_11_Memory_Management_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_11_Memory_Management_order)

label chapter_11_Memory_Management_Quiz:
    #5POINTS
    $ chapter_11_Memory_Management_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_11_Memory_Management_order:
        $ current_q = chapter_11_Memory_Management_order.pop(0)

        if current_q == "q1":
            a "Which search algorithm typically uses the most memory?"
            menu:
                "Depth-First Search":
                    a "Incorrect! DFS is memory-efficient."
                "Breadth-First Search":  # Correct (middle)
                    $ chapter_11_Memory_Management_quiz += 1
                    a "Correct! BFS stores all nodes at each level."
                "Iterative Deepening Search":
                    a "Incorrect! IDS uses minimal memory."

        elif current_q == "q2":
            a "Why is DFS considered memory-efficient?"
            menu:
                "It stores all paths in a queue":
                    a "Incorrect! That’s BFS behavior."
                "It only tracks the current path and backtracks":  # Correct (middle)
                    $ chapter_11_Memory_Management_quiz += 1
                    a "Correct! DFS uses a stack and avoids storing entire levels."
                "It compresses the graph before searching":
                    a "Incorrect! DFS doesn’t modify the graph."

        elif current_q == "q3":
            a "What does a priority queue store in UCS and A*?"
            menu:
                "Only visited nodes":
                    a "Incorrect! It stores paths based on cost."
                "Paths ordered by cost or estimated cost":  # Correct (bottom)
                    $ chapter_11_Memory_Management_quiz += 1
                    a "Correct! This helps expand the most promising paths first."
                "All possible graph edges":
                    a "Incorrect! Edges are part of the graph, not the queue."

        elif current_q == "q4":
            a "Which algorithm is best when memory is limited but completeness is required?"
            menu:
                "Breadth-First Search":
                    a "Incorrect! BFS uses a lot of memory."
                "Iterative Deepening Search":  # Correct (middle)
                    $ chapter_11_Memory_Management_quiz += 1
                    a "Correct! IDS balances low memory use with full coverage."
                "Uniform Cost Search":
                    a "Incorrect! UCS can consume more memory due to path tracking."

        elif current_q == "q5":
            a "How can memory usage be reduced in search algorithms?"
            menu:
                "By using depth limits and pruning":  # Correct (top)
                    $ chapter_11_Memory_Management_quiz += 1
                    a "Correct! These techniques help control memory growth."
                "By skipping goal nodes":
                    a "Incorrect! That defeats the purpose of searching."
                "By storing all paths in advance":
                    a "Incorrect! That increases memory usage."

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