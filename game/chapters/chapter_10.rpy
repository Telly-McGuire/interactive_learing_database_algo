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

    a "Graph Theory studies how objects (nodes) are connected (edges)."
    a "Graphs can be directed or undirected, weighted or unweighted."
    a "They're used in networking, social media, and more."
    $ chapter_10_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Let's check your understanding with a quick quiz!"
    jump chapter_10_Graph_Theory_Quiz

label chapter_10_Graph_Theory_Quiz:
    #5POINTS
    $ chapter_10_Graph_Theory_quiz = 0
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert quiz questions here)

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_10_Graph_Theory_quiz] out of 5."
    jump chapter_10_Adjacency_Representation

label chapter_10_Adjacency_Representation:

    a "Graphs can be represented using adjacency matrices or adjacency lists."
    a "Adjacency matrices use a 2D array to show connections."
    a "Adjacency lists use lists for each node to show its neighbors."
    $ chapter_10_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Let's see how well you understand graph representations!"
    jump chapter_10_Adjacency_Representation_Quiz

label chapter_10_Adjacency_Representation_Quiz:
    #5POINTS
    $ chapter_10_Adjacency_Representation_quiz = 0
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert quiz questions here)

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_10_Adjacency_Representation_quiz] out of 5."
    jump chapter_10_Applications

label chapter_10_Applications:

    a "Graphs are used in routing, social networks, dependency tracking, and more."
    a "Algorithms like BFS and DFS help solve real-world problems."
    $ chapter_10_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Quiz time: Applications of graphs!"
    jump chapter_10_Applications_Quiz

label chapter_10_Applications_Quiz:
    #5POINTS
    $ chapter_10_Applications_quiz = 0
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert quiz questions here)

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