# Chapter 9: Associative Arrays (Dictionaries)
# Topics:
# - Associative arrays
# - Hash table introduction – collisions
# - Hash table introduction – dynamic resizing

label chapter_9_intro:

label chapter_9_Associative_Arrays:
label chapter_9_Associative_Arrays_Quiz:
    #5POINTS
    $ chapter_9_Associative_Arrays_quiz = 0

label chapter_9_Collisions:
label chapter_9_Collisions_Quiz:
    #5POINTS
    $ chapter_9_Collisions_quiz = 0

label chapter_9_Dynamic_Resizing:
label chapter_9_Dynamic_Resizing_Quiz:
    #5POINTS
    $ chapter_9_Dynamic_Resizing_quiz = 0

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
label chapter_9_quiz_medium:
label chapter_9_quiz_hard:

label chapter_9_quiz_end:
    a "Your total score is [chapter_9_test] out of 15"
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