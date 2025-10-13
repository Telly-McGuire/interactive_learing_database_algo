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

    a "Associative arrays, or dictionaries, let you store data as key-value pairs."
    a "They're great for fast lookups, like a phonebook or a student database."
    a "Keys must be unique, and you can use them to quickly access values."
    $ chapter_9_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Let's check your understanding with a quick quiz!"
    jump chapter_9_Associative_Arrays_Quiz

label chapter_9_Associative_Arrays_Quiz:
    #5POINTS
    $ chapter_9_Associative_Arrays_quiz = 0
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert quiz questions here)

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_9_Associative_Arrays_quiz] out of 5."
    jump chapter_9_Collisions

label chapter_9_Collisions:

    a "Hash tables use a hash function to map keys to indices."
    a "Sometimes, two keys hash to the same index. This is called a collision."
    a "There are different ways to handle collisions, like chaining or open addressing."
    $ chapter_9_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Quiz time: Collisions!"
    jump chapter_9_Collisions_Quiz

label chapter_9_Collisions_Quiz:
    #5POINTS
    $ chapter_9_Collisions_quiz = 0
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert quiz questions here)

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_9_Collisions_quiz] out of 5."
    jump chapter_9_Dynamic_Resizing

label chapter_9_Dynamic_Resizing:

    a "As a hash table fills up, performance can drop."
    a "Dynamic resizing increases the table size and rehashes all keys."
    a "This keeps lookups fast, even as you add more data."
    $ chapter_9_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Quiz time: Dynamic resizing!"
    jump chapter_9_Dynamic_Resizing_Quiz

label chapter_9_Dynamic_Resizing_Quiz:
    #5POINTS
    $ chapter_9_Dynamic_Resizing_quiz = 0
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert quiz questions here)

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