# Chapter 8: Heaps
# Topics:
# - Introduction to priority queues
# - Heap basics
# - Array representation
# - Remove operation
# - Heap sort
# - Operation complexities
# - Binomial and Fibonacci heaps

label chapter_8_intro:

label chapter_8_Priority_Queues:
label chapter_8_Priority_Queues_Quiz:
    #5POINTS
    $ chapter_8_Priority_Queues_quiz = 0

label chapter_8_Heap_Basics:
label chapter_8_Heap_Basics_Quiz:
    #5POINTS
    $ chapter_8_Heap_Basics_quiz = 0

label chapter_8_Array_Representation:
label chapter_8_Array_Representation_Quiz:
    #5POINTS
    $ chapter_8_Array_Representation_quiz = 0

label chapter_8_Remove_Operation:
label chapter_8_Remove_Operation_Quiz:
    #5POINTS
    $ chapter_8_Remove_Operation_quiz = 0

label chapter_8_Heap_Sort:
label chapter_8_Heap_Sort_Quiz:
    #5POINTS
    $ chapter_8_Heap_Sort_quiz = 0

label chapter_8_Operation_Complexities:
label chapter_8_Operation_Complexities_Quiz:
    #5POINTS
    $ chapter_8_Operation_Complexities_quiz = 0

label chapter_8_Binomial_Fibonacci:
label chapter_8_Binomial_Fibonacci_Quiz:
    #5POINTS
    $ chapter_8_Binomial_Fibonacci_quiz = 0

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
label chapter_8_quiz_medium:
label chapter_8_quiz_hard:

label chapter_8_quiz_end:
    a "Your total score is [chapter_8_test] out of 35"
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