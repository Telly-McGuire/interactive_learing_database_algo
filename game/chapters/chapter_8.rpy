# Chapter 8: Heaps
# Topics:
# - Introduction to priority queues
# - Heap basics
# - Array representation
# - Remove operation
# - Heap sort
# - Operation complexities
# - Binomial and Fibonacci heaps

default chapter_8_progress = 0

default chapter_8_Priority_Queues_quiz = 0
default chapter_8_Heap_Basics_quiz = 0
default chapter_8_Array_Representation_quiz = 0
default chapter_8_Remove_Operation_quiz = 0
default chapter_8_Heap_Sort_quiz = 0
default chapter_8_Operation_Complexities_quiz = 0
default chapter_8_Binomial_Fibonacci_quiz = 0

label chapter_8_intro:

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
    a "Ready to climb the Heap mountain?"
    a "Let's explore how heaps help us organize data efficiently."
    show adrian smiling
    a "Welcome to Chapter 8: Heaps"

label chapter_8_Priority_Queues:

    a "First, let's talk about Priority Queues."
    a "A priority queue is a data structure where each element has a priority."
    a "Elements are served based on their priority, not just their order in the queue."
    a "They're used in scheduling, pathfinding, and more."
    $ chapter_8_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Let's check your understanding with a quick quiz!"
    jump chapter_8_Priority_Queues_Quiz

label chapter_8_Priority_Queues_Quiz:
    #5POINTS
    $ chapter_8_Priority_Queues_quiz = 0
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert quiz questions here)

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_8_Priority_Queues_quiz] out of 5."
    jump chapter_8_Heap_Basics

label chapter_8_Heap_Basics:

    a "Heaps are special binary trees used to implement priority queues."
    a "There are two main types: min-heaps and max-heaps."
    a "In a min-heap, the smallest element is always at the root."
    a "Heaps are always complete binary trees."
    $ chapter_8_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Time for a quiz on heap basics!"
    jump chapter_8_Heap_Basics_Quiz

label chapter_8_Heap_Basics_Quiz:
    #5POINTS
    $ chapter_8_Heap_Basics_quiz = 0
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert quiz questions here)

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_8_Heap_Basics_quiz] out of 5."
    jump chapter_8_Array_Representation

label chapter_8_Array_Representation:

    a "Heaps are often stored as arrays."
    a "For a node at index i, its children are at 2i+1 and 2i+2."
    a "This makes heaps efficient for storage and access."
    $ chapter_8_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Let's see how well you understand array representation!"
    jump chapter_8_Array_Representation_Quiz

label chapter_8_Array_Representation_Quiz:
    #5POINTS
    $ chapter_8_Array_Representation_quiz = 0
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert quiz questions here)

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_8_Array_Representation_quiz] out of 5."
    jump chapter_8_Remove_Operation

label chapter_8_Remove_Operation:

    a "Removing the root from a heap requires reheapifying."
    a "The last element replaces the root, and the heap property is restored."
    $ chapter_8_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Quiz time: Remove operation!"
    jump chapter_8_Remove_Operation_Quiz

label chapter_8_Remove_Operation_Quiz:
    #5POINTS
    $ chapter_8_Remove_Operation_quiz = 0
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert quiz questions here)

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_8_Remove_Operation_quiz] out of 5."
    jump chapter_8_Heap_Sort

label chapter_8_Heap_Sort:

    a "Heap sort uses the heap structure to sort arrays efficiently."
    a "It repeatedly removes the root and rebuilds the heap."
    $ chapter_8_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Quiz time: Heap sort!"
    jump chapter_8_Heap_Sort_Quiz

label chapter_8_Heap_Sort_Quiz:
    #5POINTS
    $ chapter_8_Heap_Sort_quiz = 0
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert quiz questions here)

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_8_Heap_Sort_quiz] out of 5."
    jump chapter_8_Operation_Complexities

label chapter_8_Operation_Complexities:

    a "Heap operations like insert, delete, and peek have specific time complexities."
    a "Understanding these helps you choose the right data structure."
    $ chapter_8_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Quiz time: Operation complexities!"
    jump chapter_8_Operation_Complexities_Quiz

label chapter_8_Operation_Complexities_Quiz:
    #5POINTS
    $ chapter_8_Operation_Complexities_quiz = 0
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert quiz questions here)

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_8_Operation_Complexities_quiz] out of 5."
    jump chapter_8_Binomial_Fibonacci

label chapter_8_Binomial_Fibonacci:

    a "Binomial and Fibonacci heaps are advanced heap structures."
    a "They're used in algorithms like Dijkstra's for better performance."
    $ chapter_8_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Quiz time: Binomial and Fibonacci heaps!"
    jump chapter_8_Binomial_Fibonacci_Quiz

label chapter_8_Binomial_Fibonacci_Quiz:
    #5POINTS
    $ chapter_8_Binomial_Fibonacci_quiz = 0
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert quiz questions here)

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_8_Binomial_Fibonacci_quiz] out of 5."
    jump chapter_8_restart

label chapter_8_restart:
    $ chapter_8_test = (
        chapter_8_Priority_Queues_quiz +
        chapter_8_Heap_Basics_quiz +
        chapter_8_Array_Representation_quiz +
        chapter_8_Remove_Operation_quiz +
        chapter_8_Heap_Sort_quiz +
        chapter_8_Operation_Complexities_quiz +
        chapter_8_Binomial_Fibonacci_quiz
    )

    a "Your score is [chapter_8_test]"
    a "Let's see how well you do in the {size=+20}CHAPTER QUIZ"

    if chapter_7_test <= 7:
        show adrian concerned
        jump chapter_8_quiz_easy
    elif chapter_7_test <= 12:
        show adrian neutral
        jump chapter_8_quiz_medium
    else:
        show adrian excited
        jump chapter_8_quiz_hard

label chapter_8_quiz_easy:
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert easy quiz questions here)

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    jump chapter_8_performance

label chapter_8_quiz_medium:
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert medium quiz questions here)

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    jump chapter_8_performance

label chapter_8_quiz_hard:
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert hard quiz questions here)

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    jump chapter_8_performance

label chapter_8_performance:

# Priority Queues
    if chapter_8_Priority_Queues_quiz < 2:
        a "You need to review Priority Queues."
        a "Focus on how they differ from regular queues and their role in scheduling."
    elif chapter_8_Priority_Queues_quiz < 3:
        a "You did okay in Priority Queues, but there's room for improvement."
        a "Revisit how priorities affect insertion and removal."

# Heap Basics
    if chapter_8_Heap_Basics_quiz < 2:
        a "You need to review Heap Basics."
        a "Understand min-heaps vs max-heaps and their structural properties."
    elif chapter_8_Heap_Basics_quiz < 3:
        a "You did okay in Heap Basics, but there's room for improvement."
        a "Try visualizing heap trees and their constraints."

# Array Representation
    if chapter_8_Array_Representation_quiz < 2:
        a "You need to review Array Representation of Heaps."
        a "Focus on parent-child index relationships."
    elif chapter_8_Array_Representation_quiz < 3:
        a "You did okay in Array Representation, but there's room for improvement."
        a "Practice mapping tree nodes to array indices."

# Remove Operation
    if chapter_8_Remove_Operation_quiz < 2:
        a "You need to review the Remove Operation."
        a "Understand how the heap property is restored after removal."
    elif chapter_8_Remove_Operation_quiz < 3:
        a "You did okay in Remove Operation, but there's room for improvement."
        a "Trace the reheapify process step-by-step."

# Heap Sort
    if chapter_8_Heap_Sort_quiz < 2:
        a "You need to review Heap Sort."
        a "Focus on how heaps are used to sort arrays efficiently."
    elif chapter_8_Heap_Sort_quiz < 3:
        a "You did okay in Heap Sort, but there's room for improvement."
        a "Compare heap sort with other sorting algorithms."

# Operation Complexities
    if chapter_8_Operation_Complexities_quiz < 2:
        a "You need to review Operation Complexities."
        a "Understand time complexities for insert, delete, and peek."
    elif chapter_8_Operation_Complexities_quiz < 3:
        a "You did okay in Operation Complexities, but there's room for improvement."
        a "Revisit Big-O analysis for heap operations."

# Binomial & Fibonacci Heaps
    if chapter_8_Binomial_Fibonacci_quiz < 2:
        a "You need to review Binomial and Fibonacci Heaps."
        a "Focus on their structure and why they're used in advanced algorithms."
    elif chapter_8_Binomial_Fibonacci_quiz < 3:
        a "You did okay in Binomial and Fibonacci Heaps, but there's room for improvement."
        a "Explore their use in graph algorithms like Dijkstra’s."

    jump chapter_8_end

label chapter_8_end: