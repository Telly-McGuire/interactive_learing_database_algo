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


screen chapter_11_Algointro:  
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 200
        ypadding 60
        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5
            text "Algorithms" size 60 color "#FFFFFF" outlines [(5, "#000000", 0, 0)]

label chapter_11_intro:

    call hideall from _call_hideall_3
    play sound "sfx/start.mp3"
    stop music fadeout 1.0

    scene black
    pause 1.0

    show screen chapter_11_Algointro
    scene room with dissolve
    pause 2.0
    hide screen chapter_11_Algointro

    show screen menu_btn

    play music "bgm/city-high-life.mp3" fadein 1.0
    show adrian smiling at center:
        smaller
    with dissolve
    if persistent.chapter_11 == True:
        a "Welcome Back to Chapter 11!"
        a "Would you like to go over this chapter again?"
        menu: 
            "Yes":
                a "Pick a topic"
                menu:
                    "Breadth First Search":
                        jump chapter_11_BFS
                    "Web Crawlers":
                        jump chapter_11_Web_Crawlers
                    "Depth First Search":
                        jump chapter_11_DFS
                    "Uniform Cost":
                        jump chapter_11_Uniform_Cost
                    "A* Star Algorithm":
                        jump chapter_11_A_Star
            "No":
                jump menu


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
    "{cps=50}No cuz I'm a monkey{nw}"
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
    image maze1 = "assets/maze_1.png"

    image maze5 = "assets/maze_5.png"
    image maze6 = "assets/maze_6.png"
    image maze7 = "assets/maze_7.png"

    
    a "So..."
    a "Breadth-First Search."
    show adrian explaining at left
    with move

    show maze1 at right:
        matrices
    with dissolve
    a "Imagine you are in a maze."
    
    show adrian confused
    a "How would you find the exit?"
    show adrian explaining
    a "You can come up with many Strategies"
    a "In this case Algorithms"
    hide maze1
    a "{b}{size=+30}Breadth First"
    
    show maze5 at right:
        matrices
    with dissolve 
    a "It visits nodes level by level, always expanding the oldest queued node next."
    a "Notice how the queue contains the frontier and how visited prevents repeats."
    a "It checks all possible way it can go to the end"
    hide maze5
    
    show maze6 at right:
        matrices
    with dissolve

    a "And when it finally reaches the destination"
    a "And when every possible way has been exhausted"
    hide maze6

    show maze7 at right:
        matrices
    with dissolve
    play sound "sfx/explode.mp3"


    a "{b}{cps=3}{size=+50}BAM!"
    show adrian smiling
    a "It shows the path most efficient path"
    a "That is basically what Breadth First Means"
    a "Checking {b}all possible paths{/b} until it finds the most efficient path"
    hide maze7
    with dissolve
    show adrian at center
    with move
    a "Its pretty intersting no?"

    $ chapter_10_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "You hear that? Its time for some questions. Buckle Up Buckeroo"

    $ chapter_11_progress += 1
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
    image website1 = "assets/website_1.png"

    show adrian smiling
    play sound "sfx/ting.mp3"

    a "Next, let’s explore a real-world application of Breadth-First Search: {b}web crawlers{/b}."
    show adrian smiling at left 
    with move
    show website1 at right:
        gmap
    with dissolve
    a "Think of a crawler as a little explorer bot that hops from page to page, collecting what it finds."
    a "Whatever information you want it to collect"

    show adrian explaining
    with dissolve
    a "{cps=30}Instead of wandering randomly, crawlers use strategies, {b}often BFS{/b}, to make sure they discover the most important pages quickly."
    hide website1 
    with dissolve
    show adrian smiling at center 
    with move
    a "for example"
    # Simulate a lively crawl with dynamic feedback
    $ seeds = [
        "https://www.reddit.com",
        "https://twitter.com",
        "https://www.fbi.govservices",
        "https://op-proper.gov.ph"
    ]
    $ discovered = []

    a "{cps=40}Booting crawler..."
    play sound "sfx/start.mp3"
    pause 0.6

    while seeds:
        $ current = seeds.pop(0)
        a "{cps=40}Visiting [current]..."
        play sound "sfx/bell.mp3"
        pause 0.5

        a "{cps=30}Scanning links on [current]..."
        pause 0.4

        # pretend we found a few links (dynamic flavor text)
        $ found = [current + "/about", current + "/products", current + "/contact"]
        $ discovered.extend(found)

        a "Found: [found[0]], [found[1]], [found[2]]"
        pause 0.4

        # show a quick visual flourish
        show adrian shock
        with vpunch
        pause 0.25
        show adrian explaining
        with dissolve

    a "{cps=30}That was a shallow sweep. You discovered [len(discovered)] pages across several domains."

    menu:
        "Keep it shallow — explore broad, many domains (BFS)":
            a "Good call. BFS helps discover widely-linked, high-value pages early."
            $ strategy = "bfs"
            $ bonus = 6
        "Go deep into one site (DFS style)":
            a "You dig deep into one domain to find hidden details — fewer domains but deeper coverage."
            $ strategy = "dfs"
            $ bonus = 2
        "Use a smart hybrid (prioritize popular then deep-dive)":
            a "You mix approaches: breadth first to build an index, then focused depth for detail."
            $ strategy = "hybrid"
            $ bonus = 10

    show adrian smiling
    with dissolve
    play sound "sfx/bell.mp3"
    a "{cps=40}Your crawler strategy: [strategy]. Estimated pages discovered: [len(discovered) + bonus]."
    a "That what web crawlers are basically"

    $ chapter_11_progress += 1
    show adrian happy
    play sound "sfx/bell.mp3"
    a "You hear that? Its time for some questions. Buckle Up Buckeroo"
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

    image maze2 = "assets/maze_2.png"
    image maze4 = "assets/maze_4.png"
    image maze4a = "assets/maze_4a.png"

    show adrian smiling
    a "Now, let’s explore {b}Depth-First Search (DFS){/b}."
    
    show adrian at left
    with move
    show maze1 at right:
        matrices
    with dissolve
    a "Lets go back to the maze"
    a "Unlike BFS, which explores level by level, DFS dives deep into each branch before backtracking."
    hide maze1

    show maze2 at right:
        matrices
    with dissolve
    a "DFS starts at a chosen node and explores as far as it can go along one path, only returning when it hits a dead end."
    a "It uses a {b}stack{/b}—either explicitly or through recursion—to keep track of the path it’s following."
    a "It goes as deep as it can and then ones it finally finds the path"
    hide maze2

    show maze4 at right:
        matrices
    with dissolve
    a "Since it has found the path as deep as it can"
    hide maze4

    show maze4a at right:
        matrices
    with dissolve
    a "It connects!"

    a "DFS is also useful in topological sorting, connected component analysis, and many other graph-based algorithms."
    a "Remember, it dives deep in first, then backtracks until it finds the path"
    hide maze4a
    with dissolve

    show adrian smiling at center
    a "Thats the basic gist of it"
    a "Unlike {b}Breadth First{/b} which checks every path, {b}Depth First{/b} goes as deep as it can"

    $ chapter_11_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "You hear that? Its time for some questions. Buckle Up Buckeroo"
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

    show adrian smiling
    play sound "sfx/ting.mp3"
    a "Let’s take Breadth-First Search one step further with {b}Uniform Cost Search (UCS){/b}."
    a "UCS accounts for {b}edge costs{/b} and always expands the path with the {i}lowest cumulative cost{/i}."
    
    a "Alright, picture this: you're trying to get to school, but there are multiple routes you could take."
    a "One path is {i}short but full of traffic{/i}. Another is {i}longer but smooth and fast{/i}. A third has {i}potholes and slow zones{/i}."
    a "{b}Uniform Cost Search{/b} is like a smart GPS. It doesn’t just look at distance — it looks at the {b}total cost{/b} of each route."
    a "That cost could be {i}time, effort, or even fuel{/i}. UCS always picks the path with the {b}lowest total cost so far{/b}."
    a "Instead of rushing ahead, it carefully expands the {i}cheapest option first{/i} — even if that means taking a longer route that’s easier overall."

    a "To take the most efficient path, you pick the one with the least cost"
    show adrian explaining at center
    with move

    a "Okay — let's try an interactive demo. Pick a start and a goal node and I'll walk you through UCS step-by-step."

    # Choose start and goal
    menu:
        "Start at S":
            $ start_node = "S"
        "Start at A":
            $ start_node = "A"
        "Start at B":
            $ start_node = "B"

    menu:
        "Goal is G":
            $ goal_node = "G"
        "Goal is B":
            $ goal_node = "B"
        "Goal is A":
            $ goal_node = "A"

    # Define a small weighted graph for the demo
    python:
        import heapq

        graph = {
            "S": [("A", 2), ("B", 5)],
            "A": [("B", 2), ("G", 7)],
            "B": [("G", 1)],
            "G": []
        }

        def uniform_cost_search(graph, start, goal):
            # frontier is a min-heap of (cost, node, path)
            frontier = []
            heapq.heappush(frontier, (0, start, [start]))
            explored_cost = {}  # best known cost to each node
            steps = []  # snapshots for interactive stepping

            while frontier:
                # snapshot of frontier before pop
                frontier_snapshot = sorted([(c, n, list(p)) for (c, n, p) in frontier])
                cost, node, path = heapq.heappop(frontier)

                steps.append({
                    "popped": (node, cost, list(path)),
                    "frontier": frontier_snapshot
                })

                if node == goal:
                    return steps, (path, cost)

                # If we've already seen a cheaper path to node, skip
                if node in explored_cost and explored_cost[node] < cost:
                    continue

                explored_cost[node] = cost

                for (neighbor, w) in graph.get(node, []):
                    new_cost = cost + w
                    # If we haven't seen neighbor or found cheaper path, push
                    if neighbor not in explored_cost or new_cost < explored_cost.get(neighbor, float("inf")):
                        heapq.heappush(frontier, (new_cost, neighbor, path + [neighbor]))

            return steps, (None, None)

        demo_steps, result = uniform_cost_search(graph, start_node, goal_node)
        demo_path, demo_cost = result

    # If no path, tell user
    if demo_path is None:
        show adrian sad
        play sound "sfx/fail.mp3"
        a "Hmm — no path was found from [start_node] to [goal_node] in this demo graph."
        a "Try a different start/goal combination."
        jump chapter_11_Uniform_Cost

    # Interactive stepping through computed snapshots
    $ step_index = 0
    while step_index < len(demo_steps):
        $ snapshot = demo_steps[step_index]
        $ popped_node, popped_cost, popped_path = snapshot["popped"]


        a "{cps=30}Step [step_index + 1] — UCS pops node [popped_node] with cumulative cost [popped_cost]."
        a "Current path to that node: [popped_path]"

        # Short visual: show a relevant maze image on the right if available
        # Replace image visuals with a textual info panel on the right (no images).
        python:
            if popped_node == "G":
                status = "GOAL REACHED!\n"
            else:
                status = "EXPANDING NODE\n"

            path_str = " -> ".join(popped_path)
            visual_text = f"{status}Node: {popped_node}\nCost: {popped_cost}\nPath: {path_str}"
    
        show text visual_text:
            xalign 0.8
            yalign 0.4
        menu:
            "Next step":
                $ step_index += 1
            "Inspect priority queue":
                # Show a quick representation of the frontier
                python:
                    items = snapshot["frontier"]
                    # Format lines like "cost: node (path)"
                    frontier_lines = []
                    for c, n, p in items:
                        frontier_lines.append("{:>3} : {} -> {}".format(c, n, "->".join(p)))
                    ui_text = "\\n".join(frontier_lines) if frontier_lines else "Frontier is empty."
                    renpy.call_in_new_context("chapter_11_show_queue", ui_text)
            "Jump to solution":
                $ step_index = len(demo_steps)

    # After stepping, reveal the solution path and cost
    show adrian happy
    play sound "sfx/success.mp3"
    a "{cps=30}Done stepping! UCS found this least-cost path:"
    a "{b}[ ' -> '.join(demo_path) ]{/b} with total cost {b}[demo_cost]{/b}."

    # Offer comparison: show what BFS would pick (by steps) ignoring weights
    menu:
        "Compare with BFS (ignoring weights)":
            python:
                from collections import deque
                def bfs_path(graph, start, goal):
                    q = deque([(start, [start])])
                    visited = set([start])
                    while q:
                        node, path = q.popleft()
                        if node == goal:
                            return path
                        for (nbr, _) in graph.get(node, []):
                            if nbr not in visited:
                                visited.add(nbr)
                                q.append((nbr, path + [nbr]))
                    return None
                bfs_solution = bfs_path(graph, start_node, goal_node)
            if bfs_solution:
                a "BFS (unweighted) would return: [ ' -> '.join(bfs_solution) ]"
            else:
                a "BFS didn't find a path in this demo graph."

        "Skip comparison":
            pass

    # Small interactive question to test understanding
    menu:
        "Why did UCS pick this path?":
            a "Because it minimized cumulative cost across edges, not the number of steps."
            $ ucs_explain = True
        "How does the priority queue affect choices?":
            a "The priority queue orders partial paths by total cost; the cheapest partial path is expanded first."
            $ ucs_explain = True
        "I'm good, continue":
            $ ucs_explain = False

    if ucs_explain:
        show adrian explaining
        with dissolve
        a "Key idea: UCS is optimal with non-negative costs because it always expands the least-cost frontier entry."
        a "If a cheaper path to a node appears later, UCS will still consider it because the queue orders by total path cost."
    

    $ chapter_11_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "You hear that? Its time for some questions. Buckle Up Buckeroo"
    hide text visual_text
    jump chapter_11_Uniform_Cost_Quiz

# A small helper label used above to display queue contents without breaking the step loop.
label chapter_11_show_queue(ui_text):
    show adrian normal
    a "{cps=30}Priority Queue (cost : node -> path):"
    nvl clear
    menu:
        "OK":
            pass
    return

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

    a "Let’s talk about one of the smartest pathfinding algorithms out there: {b}A* Search{/b}."

    a "A* is designed to find the shortest path from a starting point to a goal—quickly and efficiently."

    a "What makes it powerful is how it balances two things:"
    a "• {b}g(n){/b} — the actual cost to reach a point"
    a "• {b}h(n){/b} — a heuristic estimate of the cost to reach the goal from there"

    a "By adding them together, we get {b}f(n) = g(n) + h(n){/b}, which represents the total estimated cost of a path through that point."

    a "A* always chooses the path with the lowest {b}f(n){/b}, meaning it prefers paths that are both cheap so far and promising ahead."

    a "This makes A* both fast and accurate—it often finds the shortest route without wasting time exploring bad options."

    a "It’s widely used in games, robotics, and navigation systems because of its reliability and efficiency."

    $ chapter_11_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Now that you know how A* works, let’s see what you’ve learned!"
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
    jump chapter_11_restart


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
        chapter_11_A_Star_quiz 
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

init python:
    import random
    chapter_11_easy_question_order = [
        "q1","q2","q3","q4","q5",
        "q6","q7","q8","q9","q10"
    ]
    random.shuffle(chapter_11_easy_question_order)

label chapter_11_quiz_easy:

    $ chapter_11_score = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0

    show adrian normal
    a "Welcome to the Chapter Quiz!"

    while chapter_11_easy_question_order:
        $ current_q = chapter_11_easy_question_order.pop(0)

        if current_q == "q1":
            a "Q1: What data structure does Breadth-First Search primarily use?"
            menu:
                "Stack":
                    a "Incorrect — that's DFS."
                "Queue":
                    $ chapter_11_score += 1
                    a "Correct — BFS uses a queue to explore nodes level by level."
                "Priority queue":
                    a "Incorrect — that's for cost-aware searches."

        elif current_q == "q2":
            a "Q2: Why do many web crawlers use a breadth-first (BFS-like) approach?"
            menu:
                "To quickly cover many sites at shallow depth and avoid getting stuck deep in one site":
                    $ chapter_11_score += 1
                    a "Correct — BFS-style crawling improves coverage and fairness."
                "To prioritize the deepest links first":
                    a "Incorrect — that biases the crawler."
                "To guarantee finding the most important pages first":
                    a "Not necessarily — importance requires ranking."

        elif current_q == "q3":
            a "Q3: What traversal explores as far as possible along a branch before backtracking?"
            menu:
                "Breadth-First Search (BFS)":
                    a "Incorrect — BFS explores level by level."
                "Depth-First Search (DFS)":
                    $ chapter_11_score += 1
                    a "Correct — DFS dives deep then backtracks."
                "Uniform Cost Search":
                    a "Incorrect — UCS is cost-driven."

        elif current_q == "q4":
            a "Q4: Uniform Cost Search (UCS) expands nodes in order of:"
            menu:
                "Smallest heuristic estimate h(n)":
                    a "Incorrect — that's greedy best-first."
                "Random order":
                    a "Incorrect — UCS is systematic and cost-based."
                "Lowest path cost so far g(n)":
                    $ chapter_11_score += 1
                    a "Correct — UCS uses accumulated path cost."
                

        elif current_q == "q5":
            a "Q5: In A*, what does f(n) = g(n) + h(n) represent?"
            menu:
                "The heuristic alone":
                    a "Incorrect — that's h(n)."
                "The sum of cost so far and an estimate to the goal":
                    $ chapter_11_score += 1
                    a "Correct — f(n) is the estimated total cost via node n."
                "Number of neighbors of n":
                    a "Incorrect — unrelated."

        elif current_q == "q6":
            a "Q6: When implementing BFS on a graph, when is it best to mark a node as visited to avoid duplicates?"
            menu:
                "When dequeued (after removal)":
                    a "This can work but may allow duplicates to be queued."
                "Never mark visited":
                    a "Incorrect — that risks infinite loops."

                "When enqueued (upon insertion)":
                    $ chapter_11_score += 1
                    a "Correct — marking on enqueue prevents multiple insertions."
                
        elif current_q == "q7":
            a "Q7: Which is a common reason to limit a crawler's depth?"
            menu:
                "To make the crawler find everything on the entire web":
                    a "Incorrect — limiting depth reduces coverage of deep pages."
                "To limit resource use and keep crawls focused":
                    $ chapter_11_score += 1
                    a "Correct — depth limits manage time, bandwidth, and relevance."
                "To always start at the deepest pages":
                    a "Incorrect — counterproductive for broad coverage."

        elif current_q == "q8":
            a "Q8: Which real task is DFS especially suited for?"
            menu:
                "Finding shortest path by edge count in an unweighted graph":
                    a "Incorrect — BFS is better for that."
                "Detecting cycles and performing topological sort":
                    $ chapter_11_score += 1
                    a "Correct — DFS helps detect cycles and build topological order."
                "Always finding the minimum-cost route on weighted graphs":
                    a "Incorrect — use UCS or A* for cost-aware searches."

        elif current_q == "q9":
            a "Q9: If A* uses an admissible heuristic that never overestimates, what is guaranteed?"
            menu:
                "That A* will be faster than any other algorithm":
                    a "Incorrect — speed depends on many factors."
                "That A* will find an optimal (shortest-cost) path":
                    $ chapter_11_score += 1
                    a "Correct — admissible heuristics ensure optimality."
                "That A* will use no memory":
                    a "Incorrect — A* can be memory-intensive."

        elif current_q == "q10":
            a "Q10: On a graph with non-negative edge weights, which algorithm guarantees shortest paths?"
            menu:
                "Breadth-First Search":
                    a "Incorrect — BFS ignores weights."
                "Uniform Cost Search (Dijkstra)":
                    $ chapter_11_score += 1
                    a "Correct — UCS/Dijkstra guarantee shortest paths with non-negative weights."
                "Depth-First Search":
                    a "Incorrect — DFS does not guarantee shortest paths."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Your quiz score is: [chapter_11_score]"

    if chapter_11_score >= 8:
        a "Excellent — you clearly understand the topics."
    elif chapter_11_score >= 5:
        a "Nice work — a bit more practice and you'll be solid."
    else:
        a "Review the chapter topics (BFS, DFS, web crawlers, UCS, A*)."

    jump chapter_11_performance

init python:
    import random
    chapter_11_medium_question_order = [
        "q1", "q2", "q3", "q4", "q5",
        "q6", "q7", "q8", "q9", "q10",
        "q11", "q12", "q13", "q14", "q15"
    ]
    random.shuffle(chapter_11_medium_question_order)

label chapter_11_quiz_medium:
    $ chapter_11_score = 0
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_11_medium_question_order:
        $ current_q = chapter_11_medium_question_order.pop(0)

        if current_q == "q1":
            a " When performing BFS on a graph to find the shortest path in an unweighted graph, which guarantee holds?"
            menu:
                "BFS finds a shortest path in number of edges between the start and goal":
                    $ chapter_11_score += 1
                    a "Correct — BFS explores by increasing distance in edges."
                "BFS always finds the path with the lowest total cost":
                    a "Incorrect — costs matter; BFS assumes equal edge cost."
                "BFS is guaranteed to use less memory than DFS":
                    a "Incorrect — BFS often uses more memory."

        elif current_q == "q2":
            a "Which strategy do polite web crawlers use to avoid overloading a single site?"
            menu:
                "Rate limiting and obeying robots.txt":
                    $ chapter_11_score += 1
                    a "Correct — good crawlers respect robots.txt and throttle requests per site."
                "Recursively crawling everything from a domain without pause":
                    a "Incorrect — that can overload servers."
                "Always using DFS to get to deep pages first":
                    a "Incorrect — DFS can concentrate requests on one site and is impolite."

        elif current_q == "q3":
            a "In DFS, what data structure is typically used to implement the search iteratively?"
            menu:
                "Queue":
                    a "Incorrect — a queue is BFS's structure."
                "Stack":
                    $ chapter_11_score += 1
                    a "Correct — DFS uses a stack (explicit or the call stack in recursion)."
                "Priority queue":
                    a "Incorrect — that's for cost-based searches."

        elif current_q == "q4":
            a "Which of these is a primary weakness of naive breadth-first crawling across the web?"
            menu:
                "It quickly finds deep pages":
                    a "Incorrect — BFS favors shallow pages first."
                "It may spend lots of resources visiting many low-value shallow pages":
                    $ chapter_11_score += 1
                    a "Correct — BFS can fetch many low-value pages before deeper, important ones."
                "It always finds the most relevant pages first":
                    a "Incorrect — relevance requires ranking beyond BFS."

        elif current_q == "q5":
            a "Uniform-Cost Search (UCS) differs from BFS because it expands nodes by:"
            menu:
                "Order of node creation":
                    a "Incorrect — creation order is not the primary difference."
                "Lowest path cost from the start first":
                    $ chapter_11_score += 1
                    a "Correct — UCS uses a priority queue keyed by cumulative cost."
                "Largest heuristic estimate first":
                    a "Incorrect — that describes a greedy approach."

        elif current_q == "q6":
            a "When is DFS preferable to BFS?"
            menu:
                "When you need the shortest path in an unweighted graph":
                    a "Incorrect — BFS is better for shortest unweighted paths."
                "When memory is constrained and you want a solution quickly without guaranteeing shortest path":
                    $ chapter_11_score += 1
                    a "Correct — DFS uses less memory and can find solutions quickly but may not be optimal."
                "When edge costs differ and optimality is required":
                    a "Incorrect — UCS or A* handle costs/optimality better."

        elif current_q == "q7":
            a " A polite crawler uses a URL frontier. Which property should the frontier implement to support BFS-like crawling across many hosts fairly?"
            menu:
                "A single queue that enqueues children immediately, ignoring host":
                    a "Incorrect — that can concentrate requests on one host."
                "A frontier that interleaves or schedules requests per host (politeness policy)":
                    $ chapter_11_score += 1
                    a "Correct — scheduling prevents hitting one host too hard."
                "A LIFO stack that always follows the most recent link":
                    a "Incorrect — that's DFS-like and not fair across hosts."

        elif current_q == "q8":
            a " In A* search, what condition on the heuristic guarantees optimality?"
            menu:
                "The heuristic must be admissible (never overestimates true cost)":
                    $ chapter_11_score += 1
                    a "Correct — admissible heuristics ensure A* finds an optimal path when combined with proper cost handling."
                "The heuristic must be larger than the true cost":
                    a "Incorrect — that makes it inadmissible."
                "The heuristic must be random to avoid loops":
                    a "Incorrect — randomness doesn't guarantee optimality."

        elif current_q == "q9":
            a "Which statement best describes greedy best-first search compared to A*?"
            menu:
                "Greedy uses f(n) = g(n) + h(n) and is always optimal":
                    a "Incorrect — that's A*."
                "Greedy uses only heuristic h(n) to pick nodes and is not guaranteed optimal":
                    $ chapter_11_score += 1
                    a "Correct — greedy prioritizes apparent closeness to goal and can be faster but suboptimal."
                "Greedy performs the same expansions as BFS":
                    a "Incorrect — greedy differs significantly from BFS."

        elif current_q == "q10":
            a " If edges have non-uniform positive costs, which search is required to guarantee an optimal solution without a heuristic?"
            menu:
                "Breadth-first search":
                    a "Incorrect — only for uniform costs."
                "Uniform-Cost Search":
                    $ chapter_11_score += 1
                    a "Correct — UCS expands by lowest cumulative cost and handles varying positive edge costs."
                "Depth-first search":
                    a "Incorrect — DFS doesn't guarantee optimality with varying costs."

        elif current_q == "q11":
            a "For web crawling, what does 'politeness' commonly include besides rate limiting?"
            menu:
                "Ignoring robots.txt to crawl everything":
                    a "Incorrect — ignoring robots.txt is impolite and often disallowed."
                "Respecting crawl-delay directives and avoiding duplicate downloads":
                    $ chapter_11_score += 1
                    a "Correct — obeying robots rules and deduplication reduce load and redundancy."
                "Always using maximum parallel connections to each host":
                    a "Incorrect — that risks overloading hosts."

        elif current_q == "q12":
            a "A* with a heuristic that is admissible but not consistent (monotone) can still be optimal if implemented carefully. What practical issue might arise?"
            menu:
                "No issue; admissibility implies no problems":
                    a "Incorrect — admissibility alone may cause re-expansions."
                "The search may need to re-open nodes and handle path corrections (more bookkeeping)":
                    $ chapter_11_score += 1
                    a "Correct — inconsistent heuristics can force node re-expansion and extra work."
                "It will always run faster than with a consistent heuristic":
                    a "Incorrect — inconsistency typically increases work, not decreases."

        elif current_q == "q13":
            a "Which crawling approach best helps discover new sites broadly across the web quickly?"
            menu:
                "Frontier prioritization by domain-level breadth (wide host sampling)":
                    $ chapter_11_score += 1
                    a "Correct — prioritizing domain-wide breadth finds many different hosts quickly."
                "Deep single-domain DFS until exhaustion":
                    a "Incorrect — that discovers deep pages on one host but not many hosts."
                "Only following links with high PageRank":
                    a "Incorrect — that focuses on 'important' pages but not necessarily new hosts."

        elif current_q == "q14":
            a "When combining cost and heuristic in A*, node priority f(n) is:"
            menu:
                "f(n) = g(n) - h(n)":
                    a "Incorrect — subtraction would be wrong."
                "f(n) = g(n) + h(n)":
                    $ chapter_11_score += 1
                    a "Correct — A* expands nodes by the sum of path cost so far and estimated remaining cost."
                "f(n) = h(n) only":
                    a "Incorrect — that's greedy search."

        elif current_q == "q15":
            a "In practice, what is a common technique to keep a crawler's URL frontier manageable?"
            menu:
                "Never remove duplicates and keep everything":
                    a "Incorrect — that causes massive duplication."
                "Canonicalization, URL filtering, and deduplication":
                    $ chapter_11_score += 1
                    a "Correct — these reduce redundant fetches and keep the frontier useful."
                "Always fetch pages in the order they were discovered without checks":
                    a "Incorrect — naive FIFO without filtering leads to inefficiency."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Your quiz score is: [chapter_11_score]"
    jump chapter_11_performance

init python:
    import random
    chapter_11_hard_question_order = [
        "q1","q2","q3","q4","q5",
        "q6","q7","q8","q9","q10",
        "q11","q12","q13","q14","q15",
        "q16","q17","q18","q19","q20"
    ]
    random.shuffle(chapter_11_hard_question_order)

label chapter_11_quiz_hard:
    $ chapter_11_score = 0
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_11_hard_question_order:
        $ current_q = chapter_11_hard_question_order.pop(0)

        if current_q == "q1":
            a "Prove which search (BFS, DFS, UCS, A*) is complete on finite graphs without negative-cost edges."
            menu:
                "BFS, DFS, UCS, and A* are complete on finite graphs with appropriate implementations":
                    $ chapter_11_score += 1
                    a "Correct — BFS and DFS are complete on finite graphs; UCS and A* are complete with finite branching and positive costs."
                "Only BFS is complete":
                    a "Incorrect — others can be complete under conditions."

        elif current_q == "q2":
            a "For a graph with branching factor b and solution depth d, what is the worst-case time complexity of BFS?"
            menu:
                "O(b^d)":
                    $ chapter_11_score += 1
                    a "Correct — BFS explores level by level, worst-case nodes ~ b^0 + b^1 + ... + b^d."
                "O(d)":
                    a "Incorrect — that's not accounting for branching."

        elif current_q == "q3":
            a "When using UCS, what data structure is required to ensure we always expand the lowest-cost frontier node next?"
            menu:
                "Queue":
                    a "Incorrect — FIFO queue won't pick lowest cost."
                "Priority queue (min-heap) keyed by path cost":
                    $ chapter_11_score += 1
                    a "Correct — UCS needs a priority queue keyed by g(n)."
                "Stack":
                    a "Incorrect — LIFO stack is for DFS."

        elif current_q == "q4":
            a "Which property of heuristics ensures A* never undercuts optimality even with different path representations?"
            menu:
                "Admissibility (never overestimates)":
                    $ chapter_11_score += 1
                    a "Correct — admissible heuristics keep A* optimistic and optimal."
                "Randomness":
                    a "Incorrect — randomness doesn't ensure optimality."

        elif current_q == "q5":
            a "How does heuristic consistency (monotonicity) affect node re-expansions in A*?"
            menu:
                "Consistent heuristics prevent re-opening nodes leading to fewer re-expansions":
                    $ chapter_11_score += 1
                    a "Correct — consistency guarantees f-values along paths do not decrease, avoiding re-openings."
                "Consistency increases re-expansions":
                    a "Incorrect — inconsistency usually increases re-expansions."

        elif current_q == "q6":
            a "For huge web graphs, why is full-graph optimal search impractical and what practical compromise do crawlers use?"
            menu:
                "Full optimal search is always fine":
                    a "Incorrect — impractical at web scale."
                "Crawlers use heuristics, frontier prioritization, sampling, politeness and freshness heuristics":
                    $ chapter_11_score += 1
                    a "Correct — practical crawling balances coverage, freshness, and politeness."
                "They only use DFS to save memory":
                    a "Incorrect — DFS alone isn't sufficient at web scale."

        elif current_q == "q7":
            a "Which of these best describes A*'s f(n) ordering when heuristic equals true remaining cost?"
            menu:
                "A* becomes equivalent to an ideal direct oracle and expands only optimal path nodes":
                    $ chapter_11_score += 1
                    a "Correct — if h(n) equals true cost, A* expands only nodes on an optimal path."
                "A* becomes BFS":
                    a "Incorrect — that only happens if costs are uniform and h=0."
                "A* fails to find a solution":
                    a "Incorrect — it still finds optimal solutions."

        elif current_q == "q8":
            a "In the presence of zero-cost cycles, which search can loop indefinitely unless special handling is used?"
            menu:
                "UCS with naive visited checks can loop; need to track best-cost-to-node":
                    $ chapter_11_score += 1
                    a "Correct — zero-cost cycles require careful cost checks or cycle detection."
                "BFS will never loop":
                    a "Incorrect — BFS can revisit nodes if cycles not tracked."
                "DFS inherently avoids cycles":
                    a "Incorrect — DFS can loop without visited set."

        elif current_q == "q9":
            a "For a crawler that stores billions of URLs, which scalable frontier storage technique is commonly used?"
            menu:
                "In-memory list only":
                    a "Incorrect — memory would be exhausted."
                "Externalized priority queues with sharding (disk-backed queues, leveldb/rocksdb) and host-based partitions":
                    $ chapter_11_score += 1
                    a "Correct — disk-backed, sharded frontiers are practical at scale."
                "Single global priority queue in RAM":
                    a "Incorrect — not scalable for billions of URLs."

        elif current_q == "q10":
            a "Describe a case where greedy best-first search outperforms A* in practice despite being suboptimal."
            menu:
                "When heuristic is informative and search time matters more than optimality (e.g., real-time pathing)":
                    $ chapter_11_score += 1
                    a "Correct — greedy reduces expansions and latency when approximate is acceptable."
                "When you need minimum-cost guarantees":
                    a "Incorrect — greedy won't guarantee that."

        elif current_q == "q11":
            a "You're designing a crawler politeness scheduler. Which metric helps decide when to revisit a host for freshness while balancing budget?"
            menu:
                "Fixed uniform revisit interval for all hosts":
                    a "Incorrect — too rigid; hosts differ in change frequency."
                "Adaptive revisit score combining last-modified, change frequency estimate, and page importance":
                    $ chapter_11_score += 1
                    a "Correct — adaptive scoring balances freshness and cost."
                "Never revisit once fetched":
                    a "Incorrect — staleness increases."

        elif current_q == "q12":
            a "For a navigation mesh pathfinding problem with edge costs varying by time of day, which search extension handles dynamic costs best?"
            menu:
                "Standard A* without modification":
                    a "Incorrect — static costs assumed."
                "Time-expanded A* (state includes time) or re-planning with incremental search (D* / LPA*)":
                    $ chapter_11_score += 1
                    a "Correct — modeling time or using incremental planners handles dynamic costs."
                "DFS with backtracking":
                    a "Incorrect — not suitable for dynamic costs."

        elif current_q == "q13":
            a "Suppose your heuristic is admissible but has wildly varying values causing huge OPEN-set growth. Which practical step reduces memory usage while preserving reasonable solutions?"
            menu:
                "Switch to uninformed search":
                    a "Incorrect — that sacrifices performance."
                "Use weighted A* (f(n)=g(n)+(1+w)h(n)) or increase heuristic smoothing; accept bounded suboptimality":
                    $ chapter_11_score += 1
                    a "Correct — weighted A* trades optimality for fewer expansions and less memory."
                "Use DFS instead":
                    a "Incorrect — DFS doesn't provide good bounded suboptimality guarantees."

        elif current_q == "q14":
            a "In large-scale crawling, what's a concise strategy to reduce duplicate content storage caused by URL variants?"
            menu:
                "Store everything and deduplicate later":
                    a "Incorrect — wastes bandwidth and storage."
                "Canonicalize URLs, normalize query parameters, use checksum-based content dedupe (fingerprinting)":
                    $ chapter_11_score += 1
                    a "Correct — canonicalization plus content fingerprints reduces duplicates early."
                "Ignore robots.txt to fetch canonical versions":
                    a "Incorrect — ignoring robots.txt is not acceptable."

        elif current_q == "q15":
            a "Complexity comparison — under what circumstances does DFS use less memory than BFS?"
            menu:
                "When solution depth is small":
                    a "Incorrect — that doesn't capture memory tradeoffs."
                "When branching factor is large and solution depth is much smaller than breadth, DFS uses O(d) memory vs BFS O(b^d) frontier":
                    $ chapter_11_score += 1
                    a "Correct — DFS stores depth path while BFS stores wide frontiers."
                "DFS always uses more memory":
                    a "Incorrect — not always."

        elif current_q == "q16":
            a "Mini puzzle: Given this shortest-path heuristic ranking for nodes A->E: h(A)=4, h(B)=3, h(C)=2, h(D)=1, h(E)=0. If A* expands nodes in increasing f=g+h and all edge costs are 1, which node is expanded first after A?"
            menu:
                "B":
                    a "Incorrect — depends on g values from A to neighbors."
                "Any neighbor with g=1 and lowest h; so the neighbor with h=1 (D) if it's a direct neighbor":
                    $ chapter_11_score += 1
                    a "Correct — with g=1, f = 1 + h; the lowest h among neighbors is chosen."
                "E":
                    a "Incorrect — E has h=0 but likely farther (higher g)."

        elif current_q == "q17":
            a "Debug challenge: You see a crawler that keeps refetching the same page because URLs differ by trailing slash. What's the minimal change you'd implement?"
            menu:
                "Ignore trailing slashes by canonicalizing URLs before adding to frontier":
                    $ chapter_11_score += 1
                    a "Correct — canonicalization (strip/normalize trailing slash) prevents duplicate frontier entries."
                "Fetch both versions always":
                    a "Incorrect — duplicates the work."
                "Block all URLs with trailing slashes":
                    a "Incorrect — too aggressive and incorrect."

        elif current_q == "q18":
            a "Design prompt: Propose a one-line heuristic for A* on a grid with 4-way movement that is admissible and tight."
            menu:
                "Euclidean distance":
                    a "Incorrect — admissible but for 4-way Manhattan is tighter."
                "Manhattan distance (|dx| + |dy|)":
                    $ chapter_11_score += 1
                    a "Correct — Manhattan is admissible and tight for 4-way grids with unit costs."
                "Squared distance":
                    a "Incorrect — can over/underestimate; not standard."

        elif current_q == "q19":
            a "Creative scenario: You must prioritize crawling for a breaking-news site vs. an archival site with seldom changes. Which scheduling tweak do you apply?"
            menu:
                "Give breaking-news site higher revisit score and more parallel bandwidth; reduce frequency for archival site":
                    $ chapter_11_score += 1
                    a "Correct — prioritize freshness and allocate resources adaptively."
                "Treat both equally":
                    a "Incorrect — wastes resources or misses breaking updates."
                "Never revisit the breaking-news site":
                    a "Incorrect — that misses updates."

        elif current_q == "q20":
            a "Tiny coding logic: Which of these Python snippets correctly prevents re-expansion in A*/UCS by checking if a better cost was found before pushing to OPEN?"
            menu:
                "if neighbor not in closed or new_cost < cost_so_far[neighbor]:\n    cost_so_far[neighbor] = new_cost\n    push neighbor to open":
                    $ chapter_11_score += 1
                    a "Correct — updating when new_cost is better and only then pushing avoids unnecessary re-expansions."
                "Always push neighbor to open without checks":
                    a "Incorrect — causes extra work."
                "Only check closed set and ignore cost improvements":
                    a "Incorrect — misses better paths."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Your quiz score is: [chapter_11_score]"
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

    jump chapter_11_end

label chapter_11_end:    
    play sound "sfx/success.mp3"
    play music "bgm/city-high-life.mp3" fadein 1.0
    $ persistent.chapter_11 = True
    a "Would You like to test again?"
    menu:
        "Yes":
            jump chapter_10_restart
        "No":
            pass
    show adrian happy
    a "You have finished chapter 11. The last chapter!"
    a "I am so proud of you!"
    a "You made it this far!"
    jump menu