define a = Character("Adrian")


transform smaller:
    zoom 0.5

label chapter_0:

    scene mt tree

    show adrian smiling :
        smaller
        
    voice "chapter 0/ch_0_1.mp3"
    a "Hello"
    
    show adrian explaining:
        smaller
    voice "chapter 0/ch_0_2.mp3"
    a "This is Interactive Learning : datastructures and algoritmns"
    voice "chapter 0/ch_0_3.mp3"
    a "This is a tool to help you learn the course without the need of a teacher"
    voice "chapter 0/ch_0_4.mp3"
    a "You will be thought the syllabus that is based off Central Philippine University's Curriculum"
    voice "chapter 0/ch_0_5.mp3"
    a "You will be quizzed, given puzzles, and problems to solve"
    voice "chapter 0/ch_0_6.mp3"
    a "Your difficulty of such activties will be based off your performance and knowledge of the subject"
    show adrian smiling:
        smaller
    voice "chapter 0/ch_0_7.mp3"
    a "Wanna give it a try?"
    menu:
        "Yes":
            voice "chapter 0/ch_0_8.mp3"
            a "Great! Let's get started"
            jump chapter_0_test

default chapter_0_test= 0
label chapter_0_test:
    a "Before we start I just have to mention that I have recorded alot of Voice Lines into this"
    a "So I hope you wont get tired of hearing my voice"

    a "Let's start with a simple test to gauge your current knowledge"
    a "Answer the following questions to the best of your ability"  
    a "You can skip questions if you don't know the answer"
    a "You can also review the questions later if you want to"
    a "Let's begin with the first question"

    a "What is a data structure?"
    menu:
        "A way to organize and store data":
            $chapter_0_test += 1
            a "Correct! A data structure is a way to organize and store data"
        "A type of algorithm":
            a "Incorrect. A data structure is not an algorithm, but it can be used in algorithms"
        "A programming language":
            a "Incorrect. A data structure is not a programming language, but it can be implemented in one"

    a "Next question"
    a "What is an algorithm?"
    menu:
        "A step-by-step procedure for solving a problem":
            $chapter_0_test += 1
            a "Correct! An algorithm is a step-by-step procedure for solving a problem"
        "A type of data structure":
            a "Incorrect. An algorithm is not a data structure, but it can use data structures"
        "A programming language":
            a "Incorrect. An algorithm is not a programming language, but it can be implemented in one"

    a "Next question"
    a "What is the difference between a stack and a queue?"
    menu:
        "A stack is LIFO (Last In First Out) and a queue is FIFO (First In First Out)":
            $chapter_0_test += 1
            a "Correct! A stack is LIFO and a queue is FIFO"
        "A stack is FIFO and a queue is LIFO":
            a "Incorrect. A stack is LIFO and a queue is FIFO"
        "There is no difference":
            a "Incorrect. There is a difference between a stack and a queue"
    
    a "Congratulations! You have completed the test"
    a "You scored [chapter_0_test] out of 3"

    if chapter_0_test == 1:
        a "You got 1 out of 3 questions correct"
        a "You can review the questions and answers if you want"
        a "Let's move on to easy the chapter problem"
        jump chapter_0_problem_easy
    
    if chapter_0_test == 2:
        a "You got 2 out of 3 questions correct"
        a "You can review the questions and answers if you want"
        a "Let's move on to the moderate chapter problem"
        jump chapter_0_problem_moderate
    
    if chapter_0_test == 3:
        a "You got all 3 questions correct"
        a "You can review the questions and answers if you want"
        a "Let's move on to the hard chapter problem"
        jump chapter_0_problem_hard

label chapter_0_problem_easy:
    a "How do you reverse a string in Python?"
    menu:
        "Using the reversed() function":
            a "Correct! You can use the reversed() function to reverse a string"
        "Using the slice notation":
            a "Correct! You can use the slice notation to reverse a string"
        "Using the join() method":
            a "Incorrect. The join() method is used to join strings, not reverse them"
    a "Great job! You have completed the easy problem"
    jump chapter_0_ending

label chapter_0_problem_moderate:
    a "How do you find the maximum value in a list in Python?"
    menu:
        "Using the max() function":
            a "Correct! You can use the max() function to find the maximum value in a list"
        "Using the sorted() function":
            a "Incorrect. The sorted() function is used to sort a list, not find the maximum value"
        "Using the min() function":
            a "Incorrect. The min() function is used to find the minimum value in a list, not the maximum value"
    a "Great job! You have completed the moderate problem"
    jump chapter_0_ending

label chapter_0_problem_hard:
    a "How do you implement a binary search algorithm in Python?"
    menu:
        "Using a list comprehension":
            a "Incorrect. A list comprehension is not used to implement a binary search algorithm"
        "Using a recursive function":
            a "Correct! You can implement a binary search algorithm using a recursive function"
        "Using a lambda function":
            a "Incorrect. A lambda function is not used to implement a binary search algorithm"
        "Using a generator":
            a "Incorrect. A generator is not used to implement a binary search algorithm"
        "using a decorator":
            a "Incorrect. A decorator is not used to implement a binary search algorithm"
    a "Great job! You have completed the hard problem"
    jump chapter_0_ending
    

label chapter_0_ending:
    a "You have completed Chapter 0"
    a "You can now move on to Chapter 1"
    a "You can also review the questions and answers if you want"
    $persistent.chapter_0 = True
    jump menu
