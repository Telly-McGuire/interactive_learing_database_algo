# Chapter 9: Associative Arrays (Dictionaries)
# Topics:
# - Associative arrays
# - Hash table introduction – collisions
# - Hash table introduction – dynamic resizing

default chapter_9_progress = 0

default chapter_9_Associative_Arrays_quiz = 0
default chapter_9_Collisions_quiz = 0
default chapter_9_Dynamic_Resizing_quiz = 0

label chapter_9_intro:

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
    a "Ready to unlock the power of key-value pairs?"
    a "Let's dive into associative arrays and hash tables."
    show adrian smiling
    a "Welcome to Chapter 9: Associative Arrays"

label chapter_9_Associative_Arrays:

    a "Let’s explore a powerful data structure: {b}Associative Arrays{/b}, also known as {b}dictionaries{/b}."
    a "Unlike regular arrays that use numeric indices, associative arrays store data as {b}key-value pairs{/b}."

    a "This means you can access a value directly by its key—like looking up a contact by name in a phonebook, or retrieving a student’s grade using their ID."

    a "Keys in a dictionary must be {i}unique{/i}, and they act as labels that point to specific values."
    a "This structure allows for extremely fast lookups, insertions, and deletions—often in constant time."

    a "Associative arrays are widely used in real-world applications, from databases and configuration files to caching systems and game state management."

    a "They’re especially useful when you need to organize data in a way that’s easy to search and update."

    $ chapter_9_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Let's check your understanding with a quick quiz!"
    jump chapter_9_Associative_Arrays_Quiz

init python:
    import random
    chapter_9_Associative_Arrays_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_9_Associative_Arrays_order)

label chapter_9_Associative_Arrays_Quiz:
    #5POINTS
    $ chapter_9_Associative_Arrays_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_9_Associative_Arrays_order:
        $ current_q = chapter_9_Associative_Arrays_order.pop(0)

        if current_q == "q1":
            a "What is an associative array also known as?"
            menu:
                "Dictionary":
                    $ chapter_9_Associative_Arrays_quiz += 1
                    a "Correct! Associative arrays are often called dictionaries in many languages."
                "List":
                    a "Incorrect! Lists use numeric indices, not keys."
                "Stack":
                    a "Incorrect! Stacks follow LIFO order, not key-value mapping."

        elif current_q == "q2":
            a "What does an associative array store?"
            menu:
                "Key-value pairs":
                    $ chapter_9_Associative_Arrays_quiz += 1
                    a "Correct! Each value is accessed using a unique key."
                "Only values":
                    a "Incorrect! Keys are essential for access."
                "Only keys":
                    a "Incorrect! Keys must be paired with values."

        elif current_q == "q3":
            a "Which operation is fastest in a well-implemented associative array?"
            menu:
                "Lookup by key":
                    $ chapter_9_Associative_Arrays_quiz += 1
                    a "Correct! Hashing allows fast access to values using keys."
                "Sorting values":
                    a "Incorrect! Sorting isn’t the primary use."
                "Iterating over values":
                    a "Incorrect! Lookup is typically faster than iteration."

        elif current_q == "q4":
            a "Which data structure is commonly used to implement associative arrays?"
            menu:
                "Hash table":
                    $ chapter_9_Associative_Arrays_quiz += 1
                    a "Correct! Hash tables provide efficient key-based access."
                "Queue":
                    a "Incorrect! Queues don’t support key-value access."
                "Tree":
                    a "Incorrect! Trees can be used, but hash tables are more common."

        elif current_q == "q5":
            a "What happens if two keys hash to the same index?"
            menu:
                "A collision occurs":
                    $ chapter_9_Associative_Arrays_quiz += 1
                    a "Correct! Collisions must be handled to maintain access efficiency."
                "The second key is ignored":
                    a "Incorrect! That would lose data."
                "The array resizes automatically":
                    a "Incorrect! Resizing may happen, but not immediately due to collisions."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_9_Associative_Arrays_quiz] out of 5."
    jump chapter_9_Collisions
label chapter_9_Collisions:

    a "Let’s talk about one of the key challenges in hash tables: {b}collisions{/b}."
    a "Hash tables use a {b}hash function{/b} to convert keys into array indices, allowing for fast data access."

    a "But sometimes, two different keys produce the same index. This situation is called a {b}collision{/b}."
    a "Collisions are inevitable, especially when the number of keys grows or the hash function isn’t perfectly uniform."

    a "To handle collisions, we use strategies that preserve access speed and data integrity."

    a "One common method is {b}chaining{/b}, where each index holds a list of entries. If multiple keys hash to the same index, they’re stored in that list."
    a "Another approach is {b}open addressing{/b}, where the algorithm searches for the next available slot in the array using techniques like linear probing or quadratic probing."

    a "Each method has its trade-offs in terms of speed, memory usage, and complexity, but both are designed to keep hash tables efficient even when collisions occur."

    a "Understanding how collisions are handled is essential for designing robust and scalable data systems."

    $ chapter_9_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Quiz time: Collisions!"
    jump chapter_9_Collisions_Quiz

init python:
    import random
    chapter_9_Collisions_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_9_Collisions_order)

label chapter_9_Collisions_Quiz:
    #5POINTS
    $ chapter_9_Collisions_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_9_Collisions_order:
        $ current_q = chapter_9_Collisions_order.pop(0)

        if current_q == "q1":
            a "What is a collision in a hash table?"
            menu:
                "Two keys hash to the same index":
                    $ chapter_9_Collisions_quiz += 1
                    a "Correct! Collisions occur when different keys map to the same slot."
                "A key is not found":
                    a "Incorrect! That’s a lookup failure, not a collision."
                "The table runs out of space":
                    a "Incorrect! That’s a capacity issue, not a collision."

        elif current_q == "q2":
            a "Which method handles collisions by storing multiple items at the same index?"
            menu:
                "Chaining":
                    $ chapter_9_Collisions_quiz += 1
                    a "Correct! Chaining uses linked lists or similar structures at each index."
                "Open addressing":
                    a "Incorrect! That probes for the next available slot."
                "Rehashing":
                    a "Incorrect! Rehashing changes the hash function or table size."

        elif current_q == "q3":
            a "What does open addressing do when a collision occurs?"
            menu:
                "Finds another empty slot using a probing strategy":
                    $ chapter_9_Collisions_quiz += 1
                    a "Correct! It searches for the next available index."
                "Creates a new hash table":
                    a "Incorrect! That’s not part of open addressing."
                "Deletes the colliding key":
                    a "Incorrect! Keys are never discarded due to collision."

        elif current_q == "q4":
            a "Which probing strategy checks the next slot in sequence?"
            menu:
                "Linear probing":
                    $ chapter_9_Collisions_quiz += 1
                    a "Correct! It moves one step at a time until a free slot is found."
                "Quadratic probing":
                    a "Incorrect! That uses squared steps."
                "Double hashing":
                    a "Incorrect! That uses a second hash function."

        elif current_q == "q5":
            a "Why is collision handling important in hash tables?"
            menu:
                "To maintain efficient access and storage":
                    $ chapter_9_Collisions_quiz += 1
                    a "Correct! Without it, hash tables lose their performance benefits."
                "To prevent memory leaks":
                    a "Incorrect! That’s a separate concern."
                "To sort the keys":
                    a "Incorrect! Hash tables don’t sort keys."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_9_Collisions_quiz] out of 5."
    jump chapter_9_Dynamic_Resizing
label chapter_9_Dynamic_Resizing:

    a "Let’s talk about how hash tables stay efficient as they grow."
    a "As you add more key-value pairs, the table can start to fill up—and when that happens, performance may drop."

    a "Why? Because more collisions occur, and resolving them takes extra time."

    a "To fix this, hash tables use a technique called {b}dynamic resizing{/b}."
    a "When the load factor—the ratio of stored elements to table size—gets too high, the table automatically increases its size."

    a "But resizing isn’t just about making room. It also involves {b}rehashing{/b} every key."
    a "That means recalculating each key’s position based on the new table size, so the data stays evenly distributed."

    a "This process helps maintain fast lookup, insertion, and deletion times—even as the dataset grows."

    a "Dynamic resizing is a key reason why hash tables are so powerful in real-world systems like databases, caches, and compilers."

    $ chapter_9_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Quiz time: Dynamic resizing!"
    jump chapter_9_Dynamic_Resizing_Quiz
init python:
    import random
    chapter_9_Dynamic_Resizing_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_9_Dynamic_Resizing_order)

label chapter_9_Dynamic_Resizing_Quiz:
    #5POINTS
    $ chapter_9_Dynamic_Resizing_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_9_Dynamic_Resizing_order:
        $ current_q = chapter_9_Dynamic_Resizing_order.pop(0)

        if current_q == "q1":
            a "What triggers dynamic resizing in a hash table?"
            menu:
                "When a collision occurs":
                    a "Incorrect! Collisions are handled separately."
                "When the load factor exceeds a threshold":  # Correct (middle)
                    $ chapter_9_Dynamic_Resizing_quiz += 1
                    a "Correct! Resizing helps maintain performance as the table fills."
                "When a key is deleted":
                    a "Incorrect! Deletion doesn’t usually trigger resizing."

        elif current_q == "q2":
            a "What is the load factor in a hash table?"
            menu:
                "Size of each key":
                    a "Incorrect! Key size doesn’t define load factor."
                "Number of collisions":
                    a "Incorrect! That’s a separate metric."
                "Ratio of stored elements to table size":  # Correct (bottom)
                    $ chapter_9_Dynamic_Resizing_quiz += 1
                    a "Correct! It helps measure how full the table is."

        elif current_q == "q3":
            a "What happens during dynamic resizing?"
            menu:
                "A new, larger table is created and all elements are rehashed":  # Correct (top)
                    $ chapter_9_Dynamic_Resizing_quiz += 1
                    a "Correct! Rehashing ensures proper distribution in the new table."
                "The table is sorted":
                    a "Incorrect! Hash tables don’t maintain sorted order."
                "Only new keys are added to a second table":
                    a "Incorrect! All keys must be rehashed."

        elif current_q == "q4":
            a "Why is rehashing necessary during resizing?"
            menu:
                "To sort the keys":
                    a "Incorrect! Sorting isn’t part of rehashing."
                "Because the hash function depends on table size":  # Correct (middle)
                    $ chapter_9_Dynamic_Resizing_quiz += 1
                    a "Correct! Changing the size affects index calculations."
                "To remove duplicate keys":
                    a "Incorrect! Rehashing doesn’t remove duplicates."

        elif current_q == "q5":
            a "What is a common strategy for resizing a hash table?"
            menu:
                "Halving the table size":
                    a "Incorrect! That would increase collisions."
                "Keeping the size fixed":
                    a "Incorrect! Fixed size leads to performance issues as data grows."
                "Doubling the table size":  # Correct (bottom)
                    $ chapter_9_Dynamic_Resizing_quiz += 1
                    a "Correct! This helps reduce future collisions and maintains efficiency."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_9_Dynamic_Resizing_quiz] out of 5."
    jump chapter_9_restart

label chapter_9_restart:
    $ chapter_9_test = (
        chapter_9_Associative_Arrays_quiz +
        chapter_9_Collisions_quiz +
        chapter_9_Dynamic_Resizing_quiz
    )

    a "Your score is [chapter_9_test]"
    a "Let's see how well you do in the {size=+20}CHAPTER QUIZ"

    if chapter_8_test <= 14:
        show adrian thoughtful
        jump chapter_9_quiz_easy
    elif chapter_8_test <= 25:
        show adrian smiling
        jump chapter_9_quiz_medium
    else:
        show adrian confident
        jump chapter_9_quiz_hard

label chapter_9_quiz_easy:
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert easy quiz questions here)

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    jump chapter_9_performance

label chapter_9_quiz_medium:
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert medium quiz questions here)

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    jump chapter_9_performance

label chapter_9_quiz_hard:
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert hard quiz questions here)

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    jump chapter_9_performance

label chapter_9_performance:

# Associative Arrays
    if chapter_9_Associative_Arrays_quiz < 2:
        a "You need to review Associative Arrays."
        a "Focus on how key-value pairs work and why they're useful."
    elif chapter_9_Associative_Arrays_quiz < 3:
        a "You did okay in Associative Arrays, but there's room for improvement."
        a "Revisit how dictionaries differ from lists and arrays."

# Collisions
    if chapter_9_Collisions_quiz < 2:
        a "You need to review Hash Table Collisions."
        a "Understand what causes collisions and how they're resolved."
    elif chapter_9_Collisions_quiz < 3:
        a "You did okay in Collisions, but there's room for improvement."
        a "Explore chaining and open addressing techniques."

# Dynamic Resizing
    if chapter_9_Dynamic_Resizing_quiz < 2:
        a "You need to review Dynamic Resizing in Hash Tables."
        a "Focus on load factor and when resizing is triggered."
    elif chapter_9_Dynamic_Resizing_quiz < 3:
        a "You did okay in Dynamic Resizing, but there's room for improvement."
        a "Practice tracing how rehashing affects performance."

    jump chapter_9_end

label chapter_9_end: