# Chapter 10: Graph Algorithms
# Topics:
# - Graph theory overview
# - Adjacency matrix and adjacency list
# - Application

label chapter_10_intro:

label chapter_10_Graph_Theory:
label chapter_10_Graph_Theory_Quiz:
    #5POINTS
    $ chapter_10_Graph_Theory_quiz = 0

label chapter_10_Adjacency_Representation:
label chapter_10_Adjacency_Representation_Quiz:
    #5POINTS
    $ chapter_10_Adjacency_Representation_quiz = 0

label chapter_10_Applications:
label chapter_10_Applications_Quiz:
    #5POINTS
    $ chapter_10_Applications_quiz = 0

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
label chapter_10_quiz_medium:
label chapter_10_quiz_hard:

label chapter_10_quiz_end:
    a "Your total score is [chapter_10_test] out of 15"
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