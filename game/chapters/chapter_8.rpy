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

    a "Let’s dive into a new data structure: the {b}Priority Queue{/b}."
    a "Unlike a regular queue where elements are processed in the order they arrive, a priority queue serves elements based on their {b}priority{/b}."

    a "Each element in a priority queue is assigned a priority value. The element with the highest priority is served first—even if it was added later than others."
    a "This makes priority queues incredibly useful in situations where urgency matters more than arrival time."

    a "You’ll find them in real-world applications like task scheduling in operating systems, managing print jobs, and even in algorithms like Dijkstra’s shortest path for navigation and pathfinding."

    a "Internally, priority queues are often implemented using {b}heaps{/b}, which allow efficient insertion and removal of the highest-priority element."

    a "Understanding how priority queues work is key to mastering more advanced algorithmic strategies."

    $ chapter_8_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Let’s check your understanding with a quick quiz!"
    jump chapter_8_Priority_Queues_Quiz

init python:
    import random
    chapter_8_Priority_Queues_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_8_Priority_Queues_order)

label chapter_8_Priority_Queues_Quiz:
    #5POINTS
    $ chapter_8_Priority_Queues_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_8_Priority_Queues_order:
        $ current_q = chapter_8_Priority_Queues_order.pop(0)

        if current_q == "q1":
            a "What is the main purpose of a priority queue?"
            menu:
                "To access elements based on priority":
                    $ chapter_8_Priority_Queues_quiz += 1
                    a "Correct! Priority queues always return the highest or lowest priority item first."
                "To store elements in sorted order":
                    a "Incorrect! Sorting is not guaranteed—only priority-based access."
                "To remove duplicates from a list":
                    a "Incorrect! That’s not a function of priority queues."

        elif current_q == "q2":
            a "Which data structure is commonly used to implement a priority queue?"
            menu:
                "Heap":
                    $ chapter_8_Priority_Queues_quiz += 1
                    a "Correct! Heaps are ideal for efficiently managing priorities."
                "Stack":
                    a "Incorrect! Stacks follow LIFO, not priority."
                "Linked List":
                    a "Incorrect! Linked lists don’t offer efficient priority access."

        elif current_q == "q3":
            a "In a min-heap priority queue, which element is removed first?"
            menu:
                "The smallest element":
                    $ chapter_8_Priority_Queues_quiz += 1
                    a "Correct! Min-heaps always remove the smallest item first."
                "The largest element":
                    a "Incorrect! That’s true for max-heaps."
                "The most recently added element":
                    a "Incorrect! That’s how stacks behave."

        elif current_q == "q4":
            a "What operation maintains the heap property after insertion?"
            menu:
                "Heapify-up":
                    $ chapter_8_Priority_Queues_quiz += 1
                    a "Correct! Heapify-up restores order after adding a new element."
                "Heapify-down":
                    a "Incorrect! That’s used after removal."
                "Sort":
                    a "Incorrect! Sorting isn’t part of heap maintenance."

        elif current_q == "q5":
            a "Which of the following is true about priority queues?"
            menu:
                "They allow fast access to the highest-priority item":
                    $ chapter_8_Priority_Queues_quiz += 1
                    a "Correct! That’s their core feature."
                "They always keep elements in alphabetical order":
                    a "Incorrect! Priority is based on values, not names."
                "They use FIFO ordering":
                    a "Incorrect! That’s how queues behave, not priority queues."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_8_Priority_Queues_quiz] out of 5."
    jump chapter_8_Heap_Basics
label chapter_8_Heap_Basics:

    a "Let’s take a closer look at {b}heaps{/b}, a special kind of binary tree often used to implement priority queues."
    a "Heaps are designed to efficiently support operations like inserting elements and retrieving the highest or lowest priority item."

    a "There are two main types of heaps: {b}min-heaps{/b} and {b}max-heaps{/b}."
    a "In a min-heap, the smallest element is always at the root. In a max-heap, it’s the largest element that sits at the top."

    a "This structure ensures that we can quickly access the most important element—whether that means the smallest or the largest—depending on the use case."

    a "One key property of heaps is that they are always {b}complete binary trees{/b}."
    a "That means every level of the tree is fully filled, except possibly the last, which is filled from left to right."

    a "This completeness allows heaps to be efficiently stored in arrays, making them ideal for use in algorithms like heapsort or in systems that need fast scheduling."

    a "Understanding how heaps maintain their structure is essential for mastering priority queues and many optimization algorithms."

    $ chapter_8_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Time for a quiz on heap basics!"
    jump chapter_8_Heap_Basics_Quiz

init python:
    import random
    chapter_8_Heap_Basics_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_8_Heap_Basics_order)

label chapter_8_Heap_Basics_Quiz:
    #5POINTS
    $ chapter_8_Heap_Basics_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_8_Heap_Basics_order:
        $ current_q = chapter_8_Heap_Basics_order.pop(0)

        if current_q == "q1":
            a "What type of heap always has the smallest element at the root?"
            menu:
                "Min-heap":
                    $ chapter_8_Heap_Basics_quiz += 1
                    a "Correct! Min-heaps keep the smallest element at the top."
                "Max-heap":
                    a "Incorrect! Max-heaps store the largest element at the root."
                "Binary search tree":
                    a "Incorrect! BSTs don’t guarantee root value."

        elif current_q == "q2":
            a "Which property must a heap always satisfy?"
            menu:

                "It must be balanced":
                    a "Incorrect! Heaps don’t require strict balancing."
                "It must be sorted":
                    a "Incorrect! Only the heap property matters, not full sorting."
                "It must be a complete binary tree":
                    $ chapter_8_Heap_Basics_quiz += 1
                    a "Correct! Heaps are always complete binary trees."
        elif current_q == "q3":
            a "What is the main use of heaps in computer science?"
            menu:

                "Storing sorted arrays":
                    a "Incorrect! Heaps don’t maintain full sorted order."
                "Searching for elements":
                    a "Incorrect! Heaps aren’t optimized for search operations."
                "Implementing priority queues":
                    $ chapter_8_Heap_Basics_quiz += 1
                    a "Correct! Heaps are ideal for managing priorities efficiently."
        elif current_q == "q4":
            a "Which of the following is true about max-heaps?"
            menu:

                "The smallest element is at the root":
                    a "Incorrect! That’s true for min-heaps."
                "All elements are sorted":
                    a "Incorrect! Heaps only maintain partial order."
                "The largest element is at the root":
                    $ chapter_8_Heap_Basics_quiz += 1
                    a "Correct! That’s the defining feature of a max-heap."
        elif current_q == "q5":
            a "Why are heaps efficient for priority queues?"
            menu:                
                "They use recursion to store values":
                    a "Incorrect! Heaps are typically stored in arrays."
                "They allow fast access to the highest or lowest priority item":
                    $ chapter_8_Heap_Basics_quiz += 1
                    a "Correct! The root always holds the top-priority element."

                "They sort all elements automatically":
                    a "Incorrect! Heaps maintain structure, not full sorting."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_8_Heap_Basics_quiz] out of 5."
    jump chapter_8_Array_Representation

label chapter_8_Array_Representation:

    a "Let’s talk about how heaps are stored in memory."
    a "Instead of using pointers like a typical binary tree, heaps are often stored as {b}arrays{/b}."

    a "This works because heaps are always {i}complete binary trees{/i}, meaning every level is filled left to right without gaps."
    a "That structure makes it easy to map tree positions directly to array indices."

    a "Here’s how it works:"
    a "- For a node at index {b}i{/b}, its left child is at index {b}2i + 1{/b}."
    a "- Its right child is at index {b}2i + 2{/b}."
    a "- And its parent? That’s at index {b}(i - 1) // 2{/b}."

    a "This mapping allows heaps to be stored compactly and accessed efficiently—no need for extra memory to store pointers."

    a "It’s one of the reasons heaps are so useful in performance-critical applications like priority queues and sorting algorithms."

    $ chapter_8_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Let's see how well you understand array representation!"
    jump chapter_8_Array_Representation_Quiz

init python:
    import random
    chapter_8_Array_Representation_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_8_Array_Representation_order)

label chapter_8_Array_Representation_Quiz:
    #5POINTS
    $ chapter_8_Array_Representation_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_8_Array_Representation_order:
        $ current_q = chapter_8_Array_Representation_order.pop(0)

        if current_q == "q1":
            a "How are heaps typically stored in memory?"
            menu:
                "As arrays":
                    $ chapter_8_Array_Representation_quiz += 1
                    a "Correct! Heaps are stored as arrays for efficient access."
                "As linked lists":
                    a "Incorrect! Linked lists don’t support fast index-based access."
                "As hash tables":
                    a "Incorrect! Hash tables are used for key-value storage, not heaps."

        elif current_q == "q2":
            a "In a heap stored as an array, where is the left child of node at index i?"
            menu:
                "2i + 1":
                    $ chapter_8_Array_Representation_quiz += 1
                    a "Correct! That’s the formula for the left child."
                "2i":
                    a "Incorrect! That’s not the correct index."
                "i + 1":
                    a "Incorrect! That’s just the next element, not necessarily a child."

        elif current_q == "q3":
            a "What is the index of the parent of a node at index i?"
            menu:                
                "i // 2":
                    a "Incorrect! That’s used in some contexts but not for heap parents."
                "(i - 1) // 2":
                    $ chapter_8_Array_Representation_quiz += 1
                    a "Correct! That formula gives the parent’s index."

                "2i - 1":
                    a "Incorrect! That’s not a valid parent index formula."

        elif current_q == "q4":
            a "Why is array representation efficient for heaps?"
            menu:

                "It automatically sorts the elements":
                    a "Incorrect! Heaps maintain partial order, not full sorting."
                "It uses less memory than arrays":
                    a "Incorrect! Heaps are stored in arrays."
                "It avoids using pointers and supports fast indexing":
                    $ chapter_8_Array_Representation_quiz += 1
                    a "Correct! Arrays make heap operations fast and memory-efficient."
        elif current_q == "q5":
            a "What kind of binary tree must a heap be to use array representation?"
            menu:

                "Balanced binary tree":
                    a "Incorrect! Balance isn’t required for heaps."
                "Full binary tree":
                    a "Incorrect! Heaps don’t need every node to have two children."
                "Complete binary tree":
                    $ chapter_8_Array_Representation_quiz += 1
                    a "Correct! Completeness ensures no gaps in the array."
    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_8_Array_Representation_quiz] out of 5."
    jump chapter_8_Remove_Operation

label chapter_8_Remove_Operation:

    a "Let’s talk about what happens when you remove the root from a heap."
    a "Since the root holds the highest or lowest priority element—depending on whether it’s a max-heap or min-heap—removing it must be handled carefully to preserve the heap’s structure."

    a "Here’s how it works:"
    a "- First, the root is removed."
    a "- Then, the last element in the heap is moved to the root position."
    a "- Finally, the heap is {b}reheapified{/b} to restore the heap property."

    a "Reheapification involves comparing the new root with its children and swapping it down the tree until the correct order is restored."
    a "This process is also called {i}heapify-down{/i}, and it ensures that the heap remains a complete binary tree with the correct priority ordering."

    a "Efficient reheapification is what makes heaps so powerful for priority queues and sorting algorithms like heapsort."

    $ chapter_8_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Quiz time: Remove operation!"
    jump chapter_8_Remove_Operation_Quiz
init python:
    import random
    chapter_8_Remove_Operation_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_8_Remove_Operation_order)

label chapter_8_Remove_Operation_Quiz:
    #5POINTS
    $ chapter_8_Remove_Operation_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_8_Remove_Operation_order:
        $ current_q = chapter_8_Remove_Operation_order.pop(0)

        if current_q == "q1":
            a "What happens first when removing the root from a heap?"
            menu:
                
                "The heap is sorted":
                    a "Incorrect! Sorting isn’t part of the removal process."
                "The root is deleted and left empty":
                    a "Incorrect! The root must be replaced."
                "The last element replaces the root":
                    $ chapter_8_Remove_Operation_quiz += 1
                    a "Correct! This maintains the complete tree structure."

        elif current_q == "q2":
            a "What operation restores the heap property after removal?"
            menu:
                "Heapify-down":
                    $ chapter_8_Remove_Operation_quiz += 1
                    a "Correct! Heapify-down ensures the new root is correctly positioned."
                "Heapify-up":
                    a "Incorrect! That’s used after insertion."
                "Rebalancing":
                    a "Incorrect! That term applies more to AVL or Red-Black Trees."

        elif current_q == "q3":
            a "Why is the last element used to replace the root?"
            menu:                
                "To avoid reheapifying":
                    a "Incorrect! Reheapifying is still required."
                "To maintain the complete binary tree structure":
                    $ chapter_8_Remove_Operation_quiz += 1
                    a "Correct! This keeps the array-based heap compact and valid."
                "To reduce the number of rotations":
                    a "Incorrect! Heaps don’t use rotations."


        elif current_q == "q4":
            a "Which direction does heapify-down move the new root?"
            menu:                
                "Upward to the top":
                    a "Incorrect! That’s heapify-up."
                "Downward toward its correct position":
                    $ chapter_8_Remove_Operation_quiz += 1
                    a "Correct! It swaps with children until the heap property is restored."

                "Sideways across the tree":
                    a "Incorrect! Heapify-down moves vertically."

        elif current_q == "q5":
            a "What is the time complexity of removing the root from a heap?"
            menu:
               
                "O(n)":
                    a "Incorrect! That would be too slow for a heap."
                "O(1)":
                    a "Incorrect! Removal requires restructuring."
                "O(log n)":
                    $ chapter_8_Remove_Operation_quiz += 1
                    a "Correct! Because heapify-down traverses the height of the tree."
    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_8_Remove_Operation_quiz] out of 5."
    jump chapter_8_Heap_Sort

label chapter_8_Heap_Sort:

    a "Let’s wrap up this chapter with a powerful sorting algorithm: {b}Heap Sort{/b}."
    a "Heap sort takes advantage of the heap data structure to sort arrays efficiently and reliably."

    a "Here’s how it works:"
    a "- First, the array is turned into a {b}max-heap{/b} (or min-heap, depending on the desired order)."
    a "- Then, the root—the largest or smallest element—is removed and placed at the end of the array."
    a "- The heap is rebuilt, and the process repeats until the entire array is sorted."

    a "This method ensures that each step places the next correct element in its final position, all while maintaining the heap structure."

    a "Heap sort has a time complexity of {i}O(n log n){/i}, and unlike quicksort, it doesn’t rely on recursion or random pivots."

    a "It’s especially useful when memory usage needs to be predictable, since it sorts in place without requiring extra space."

    $ chapter_8_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Quiz time: Heap sort!"
    jump chapter_8_Heap_Sort_Quiz
init python:
    import random
    chapter_8_Heap_Sort_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_8_Heap_Sort_order)

label chapter_8_Heap_Sort_Quiz:
    #5POINTS
    $ chapter_8_Heap_Sort_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_8_Heap_Sort_order:
        $ current_q = chapter_8_Heap_Sort_order.pop(0)

        if current_q == "q1":
            a "What is the first step in heap sort?"
            menu:                
                "Reverse the array":
                    a "Incorrect! Reversing isn’t part of heap sort."
                "Build a heap from the input array":
                    $ chapter_8_Heap_Sort_quiz += 1
                    a "Correct! You start by building a max-heap or min-heap."
                "Sort the array directly":
                    a "Incorrect! Heap sort begins with heap construction."


        elif current_q == "q2":
            a "Which heap is typically used for sorting in ascending order?"
            menu:
                
                "Min-heap":
                    a "Incorrect! Min-heaps are used for descending order."
                "Binary search tree":
                    a "Incorrect! BSTs aren’t used in heap sort."
                "Max-heap":
                    $ chapter_8_Heap_Sort_quiz += 1
                    a "Correct! Max-heaps allow repeated removal of the largest element."

        elif current_q == "q3":
            a "What happens after removing the root during heap sort?"
            menu:                
                "Rebuild the entire heap":
                    a "Incorrect! Only heapify-down is needed."
                "Place it at the end of the array and heapify-down":
                    $ chapter_8_Heap_Sort_quiz += 1
                    a "Correct! This maintains the heap and builds the sorted array."
                "Delete it permanently":
                    a "Incorrect! The root is stored in the sorted portion."


        elif current_q == "q4":
            a "What is the time complexity of heap sort?"
            menu:                
                "O(n^2)":
                    a "Incorrect! That’s too slow for heap sort."
                "O(n log n)":
                    $ chapter_8_Heap_Sort_quiz += 1
                    a "Correct! Heap sort is efficient and consistent."

                "O(log n)":
                    a "Incorrect! That’s the complexity of individual heap operations."

        elif current_q == "q5":
            a "Why is heap sort considered an in-place algorithm?"
            menu:
                "It uses recursion":
                    a "Incorrect! Recursion doesn’t define in-place behavior."
                "It doesn’t require extra memory beyond the input array":
                    $ chapter_8_Heap_Sort_quiz += 1
                    a "Correct! Heap sort rearranges elements within the array."
                
                "It stores elements in a separate heap":
                    a "Incorrect! The heap is built within the array itself."

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
    jump chapter_8_Binomial_Fibonacci

label chapter_8_Binomial_Fibonacci:

    a "Now let’s explore two advanced types of heaps: {b}Binomial Heaps{/b} and {b}Fibonacci Heaps{/b}."
    a "These structures are designed for scenarios where we need to perform a large number of priority queue operations efficiently."

    a "A {b}Binomial Heap{/b} is made up of a collection of binomial trees, which are defined recursively and follow a specific structure."
    a "They allow fast merging of two heaps, which is useful in applications like network optimization and job scheduling."

    a "On the other hand, {b}Fibonacci Heaps{/b} are even more flexible."
    a "They support very fast {i}decrease-key{/i} and {i}merge{/i} operations, making them ideal for algorithms like {b}Dijkstra’s shortest path{/b} and {b}Prim’s minimum spanning tree{/b}."

    a "While they’re more complex than binary heaps, their performance benefits are significant in large-scale or graph-based computations."

    a "Understanding these heaps isn’t just about memorizing structure—it’s about recognizing when their strengths make them the right tool for the job."

    $ chapter_8_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Quiz time: Binomial and Fibonacci heaps!"
    jump chapter_8_Binomial_Fibonacci_Quiz

init python:
    import random
    chapter_8_Binomial_Fibonacci_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_8_Binomial_Fibonacci_order)

label chapter_8_Binomial_Fibonacci_Quiz:
    #5POINTS
    $ chapter_8_Binomial_Fibonacci_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_8_Binomial_Fibonacci_order:
        $ current_q = chapter_8_Binomial_Fibonacci_order.pop(0)

        if current_q == "q1":
            a "What is the time complexity of inserting into a Binomial Heap?"
            menu:
                "O(log n)":
                    $ chapter_8_Binomial_Fibonacci_quiz += 1
                    a "Correct! Binomial Heaps support logarithmic-time insertion."
                "O(n)":
                    a "Incorrect! That’s too slow for heap insertion."
                "O(1)":
                    a "Incorrect! That’s true for Fibonacci Heaps, not Binomial."

        elif current_q == "q2":
            a "Which heap supports constant-time insertion?"
            menu:                
                "Binomial Heap":
                    a "Incorrect! Binomial Heaps take O(log n) time."
                "Fibonacci Heap":
                    $ chapter_8_Binomial_Fibonacci_quiz += 1
                    a "Correct! Fibonacci Heaps allow O(1) insertion."

                "Binary Heap":
                    a "Incorrect! Binary Heaps also take O(log n)."

        elif current_q == "q3":
            a "What is the structure of a Binomial Heap?"
            menu:
                
                "A single binary tree":
                    a "Incorrect! That’s not how Binomial Heaps are organized."
                "A linked list of values":
                    a "Incorrect! Binomial Heaps use tree structures."
                "A forest of binomial trees":
                    $ chapter_8_Binomial_Fibonacci_quiz += 1
                    a "Correct! Binomial Heaps are made of binomial trees."
        elif current_q == "q4":
            a "Which operation is faster in Fibonacci Heaps compared to Binomial Heaps?"
            menu:  
                "Extract-min":
                    a "Incorrect! Extract-min is O(log n) in both."
                "Decrease-key":
                    $ chapter_8_Binomial_Fibonacci_quiz += 1
                    a "Correct! Fibonacci Heaps support O(1) decrease-key."
              
                "Merge":
                    a "Incorrect! Both support efficient merging."

        elif current_q == "q5":
            a "Why are Fibonacci Heaps preferred in some graph algorithms?"
            menu:

                "They use less memory":
                    a "Incorrect! Memory usage isn’t the main advantage."
                "They sort elements automatically":
                    a "Incorrect! Heaps don’t fully sort elements."
                "They offer better amortized time for decrease-key":
                    $ chapter_8_Binomial_Fibonacci_quiz += 1
                    a "Correct! This makes them ideal for Dijkstra’s and Prim’s algorithms."
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

# Binomial & Fibonacci Heaps
    if chapter_8_Binomial_Fibonacci_quiz < 2:
        a "You need to review Binomial and Fibonacci Heaps."
        a "Focus on their structure and why they're used in advanced algorithms."
    elif chapter_8_Binomial_Fibonacci_quiz < 3:
        a "You did okay in Binomial and Fibonacci Heaps, but there's room for improvement."
        a "Explore their use in graph algorithms like Dijkstra’s."

    jump chapter_8_end

label chapter_8_end: