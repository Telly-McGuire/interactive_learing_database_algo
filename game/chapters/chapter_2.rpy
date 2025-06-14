screen chapter_2_introscreen:
    vbox:
        spacing 20
        xalign 0.5
        yalign 0.5
        text "Chapter 2: Arrays" size 60 color "#FFFFFF" outlines [(5, "#000000", 0, 0)]

label chapter_2_intro:
    show black
    pause 1.0
    show screen chapter_2_introscreen
    pause 2.0
    scene mt tree with dissolve
    pause 1.0
    hide screen chapter_2_introscreen
    show adrian normal at center:
        smaller
    with dissolve

    if persistent.chapter_2:
        a "Welcome Back"
        a "Would you like skip to the Quizzes?"
        menu:
            "Yes":
                jump chapter_2_quiz1
            "no":
                pass
    else:
        pass

    a "Welcome to Chapter 2"
    a "In this chapter, we will be learning about arrays"
    a "What is an array?"
    menu:
        "A data structure that stores a fixed-size sequence of elements of the same type":
            a "Correct! An array is a data structure that stores a fixed-size sequence of elements of the same type"
        "A type of algorithm":
            a "Incorrect. An array is not an algorithm, but it can be used in algorithms"
        "A programming language":
            a "Incorrect. An array is not a programming language, but it can be implemented in one"
        "{size=+20}{i}puppy":
            show adrian doubt
            a "{size=+20}Puppy?{/size}"
            jump chapter_2_puppy
    jump chapter_2_basics

define d = Character("Dog", color="#FF0000")
label chapter_2_puppy:
    play sound "sfx/puppy.mp3"
    show adrian confused at left
    with move 

    a "a Puppy?"

    show dog at right
    with moveinright
    d "Woof! Woof!"

    show adrian smiling at left
    a "Oh, you meant puppy!"
    a "Whats your name? Speak!" 
    play sound "sfx/hellomario.mp3"
    d "woof woof!"
    pause 3.0
    show adrian nocomment at left
    hide dog
    with moveoutright
    pause 1.0
    a "Okay"

    jump chapter_2_basics

label chapter_2_basics:
    show adrian smiling at center:
        smaller
    with move
    a "An array is a data structure that stores a fixed-size sequence of elements of the same type"
    a "It is a collection of items stored at contiguous memory locations"
    a "The items can be accessed using an index, which is an integer value that represents the position of the item in the array"
    a "Arrays are used to store multiple values in a single variable, instead of declaring separate variables for each value"

    show adrian normal at center
    a "In simple words, think of an array like a row of boxes."
    a "Each box can hold something, and you can find each box by its number."
    a "This helps you keep things organized and easy to find."

    show adrian explaining
    a "an array consists of {b}ELEMENTS{/b} and {b}INDEX{/b}"
    a "The {b}ELEMENTS{/b} are the items stored in the array, and the {b}INDEX{/b} is the position of the item in the array"
    a "For example, if we have an array of numbers, the first number is at index 0, the second number is at index 1, and so on"
    a "The index is used to access the elements of the array"

    a "an array starts at index {b}0{/b}, not index {b}1{/b}"
    show adrian mad
    a "Remember that, {size=+20}INDEXES START AT ZERO!"

    show adrian smiling
    a "Oh yeah, there is also a special type of array called a {b}Dynamic array{/b}"
    a "A dynamic array is an array that can grow or shrink in size as needed"


    a "Let's try creating an array together!"
    menu:
        "Create an array of 3 numbers":
            $ array1 = [0, 0, 0, 0, 0]
            a "Great! Let's fill in the values for your array."
            python:
                for i in range(len(array1)):
                    renpy.say("adrian", f"Enter a value for index {i}:")
                    value = renpy.input(f"Value for index {i}:", length=5)
                    try:
                        array1[i] = int(value)
                    except:
                        array1[i] = value
            a "Here's your array: [%(array1)s]"

        "Skip creating an array":
            a "No problem! Let's continue."


    show adrian explaining    
    a "There are also multidimensional arrays, which are arrays of arrays"
    a "These can be thought of as a table, where each row is an array and each column is an element in that array"
    a "Here's a simpler way to think about it:"
    a "Imagine you have a row of mailboxes, each with a number on it."
    a "You can put a letter in each mailbox, and to find a letter, you just look at the mailbox number."
    a "Arrays work the same way in programming!"
    a "Let's create a 2D array (an array of arrays) together!"
    menu:
        "Create a 2x2 array":
            $ array2d = [[0, 0], [0, 0]]
            a "Let's fill in the values for your 2x2 array."
            python:
                for row in range(2):
                    for col in range(2):
                        renpy.say("adrian", f"Enter a value for row {row}, column {col}:")
                        value = renpy.input(f"Value for [{row}][{col}]:", length=5)
                        try:
                            array2d[row][col] = int(value)
                        except:
                            array2d[row][col] = value
            a "Here's your 2D array:"
            python:
                for row in array2d:
                    renpy.say("adrian", str(row))
        "Skip creating a 2D array":
            a "Alright, let's move on!"
    show black with dissolve
    pause 1.0
    show screen array_advantages
    pause 2.0
    hide screen array_advantages
    hide black with dissolve

    show adrian smiling
    a "Advantages of using arrays include:"
    a "We can use random access because of the keys: getItem(int index) will return the value with the given key very fast "
    a "Very easy to implement and to use"
    a "Very fast data structure for storing and accessing data"
    a "We should use arrays in applications when we want to add items over and over again and we want to take items with given indexes!!! "

    show adrian normal
    a "The Disadvantages of using arrays include:"
    a "We have to know the size of the array at compile-time: so it is not so dynamic data structure"
    a "If it is full: we have to create a bigger array and have to copy the values one by one "
    a "It is not able to store items with different types."


    jump chapter_2_examples

screen array_advantages:
    vbox:        
        spacing 20
        xalign 0.5
        yalign 0.5
        text "Advantages & Disadvantages of Arrays" size 40 color "#FFFFFF" outlines [(5, "#000000", 0, 0)]


label chapter_2_examples:
    
    show adrian normal at center:
        smaller

    a "Let's look at some examples of how arrays can be used in programming"
    a "Arrays can be used to store a list of items, such as a list of numbers, names, or any other type of data"
    
    show adrian explaining
    a "For example, we can use an array to store a list of numbers"
    python:
        numbers1 = [1, 2, 3, 4, 5]
        renpy.say("adrian", f"Here's an array of numbers: {numbers1}")

    a "We can access the elements of the array using their index"
    python:
        for i in range(len(numbers1)):
            renpy.say("adrian", f"Element at index {i} is {numbers1[i]}")
            
    a "We can also use arrays to store a list of names"
    python:
        names1 = ["Alice", "Bob", "Charlie"]
        renpy.say("adrian", f"Here's an array of names: {names1}")

    a "We can access the elements of the array using their index"
    python:
        for i in range(len(names1)):
            renpy.say("adrian", f"Element at index {i} is {names1[i]}")

    a "Arrays can also be used to store a list of objects, such as a list of players in a game"
    python:
        players = ["Player1", "Player2", "Player3"]
        renpy.say("adrian", f"Here's an array of players: {players}")

    a "We can access the elements of the array using their index"
    python:
        for i in range(len(players)):
            renpy.say("adrian", f"Element at index {i} is {players[i]}")

    show adrian smiling
    play sound "sfx/bell.mp3"
    a "You hear that? Its time for some questions. Buckle Up Buckeroo"

    jump chapter_2_quiz1

label chapter_2_quiz1:
    $ chapter_2_questions = 0
    show adrian smug
    a "Lets see if you have learned anything"
    
    show adrian smiling
    a "Question 1: "
    a "What is an index?"
    menu:
        "A type of data stored in an array":
            show adrian doubt
            a "Not quite. The index is the position, not the data itself."
        "A position number used to access elements in an array":
            $ chapter_2_questions += 1
            show adrian happy
            a "Good Job!"
        "A programming language feature":
            show adrian confused
            a "No, an index is not a programming language feature, but a concept used in arrays."
        "A sorting algorithm":
            show adrian mad
            a "No, an index is not a sorting algorithm."
    
    show adrian normal
    a "Question 2: "
    a "What is an array?"
    menu:
        "A programming language":
            show adrian doubt
            a "No, again no, its not a programming language. Stop insisting"
        "A data structure that stores a fixed-size sequence of elements of the same type":
            $ chapter_2_questions += 1
            show adrian happy
            a "Correct! An array stores a fixed-size sequence of elements of the same type."
        "A type of loop":
            show adrian mad
            a "No, an array is not a type of loop. Ill loop your brains off"
        "A function that sorts data":
            show adrian confused
            a "No, an array is not a function or an algorithm."
    
    show adrian normal
    a "Question 3: "
    a "True or False: The first index of an array is always 1."
    menu:
        "True":
            show adrian mad
            a "Incorrect! The first index of an array is 0, not 1. I told you to {b}REMEMBER{/b} that!"
        "False":
            $ chapter_2_questions += 1
            show adrian happy
            a "Correct! Arrays start at index 0."
    
    show adrian normal
    a "Question 4: "
    a "True or False: Arrays can store elements of different types in the same array."
    menu:
        "True":
            show adrian mad
            a "Incorrect! Arrays can only store elements of the same type."
        "False":
            $ chapter_2_questions += 1
            show adrian happy
            a "Correct! Arrays store elements of the same type."

    show adrian normal
    a "Question 5: "
    a "True or False: The size of a static array cannot be changed after it is created."
    menu:
        "True":
            $ chapter_2_questions += 1
            show adrian happy
            a "Correct! The size of a static array is fixed."
        "False":
            show adrian mad
            a "Incorrect! Static arrays cannot change size after creation."

    # Multiple Choice Question 6
    show adrian normal
    a "Question 6: "
    a "Which of the following is a valid way to access the third element in an array called 'numbers'?"
    menu:
        "numbers[[3]":
            show adrian mad
            a "Incorrect! That would be the fourth element."
        "numbers(2)":
            show adrian confused
            a "Incorrect! Arrays use square brackets, not parentheses."
        "numbers[[2]":
            $ chapter_2_questions += 1
            show adrian happy
            a "Correct! Indexing starts at 0, so the third element is at index 2."
        "numbers{{2}":
            show adrian doubt
            a "Incorrect! Arrays use square brackets, not curly braces."

    show adrian normal
    a "Question 7: "
    a "What is a multidimensional array?"
    menu:
        "A variable that stores multiple data types":
            show adrian mad
            a "Incorrect! Arrays store elements of the same type."
        "An array that contains other arrays as its elements":
            $ chapter_2_questions += 1
            show adrian happy
            a "Correct! A multidimensional array is an array of arrays. WOW epic"
        "A function that returns an array":
            show adrian confused
            a "Incorrect! That's not what a multidimensional array is."
        "An array with only one element":
            show adrian doubt
            a "Incorrect! That is just a single-element array."

    a "Your score is : [chapter_2_questions]"

    if persistent.chapter_2:
        a "Would you like to continue with the next quiz?"
        menu: 
            "Yes":
                jump chapter_2_quiz2
            "No":
                pass

    a "Lets move on forward"
    jump chapter_2_add

screen ch2explode:
    vbox:
        spacing 20
        xalign 0.5
        yalign 0.5
        text "Array Operations!!!!" size 150 color "#FFFFFF" outlines [(5, "#000000", 0, 0)]

label chapter_2_add:
    
    show adrian smiling
    a "Ok lets see how arrays work"

    show black 
    show screen ch2explode 
    play sound "sfx/explode.mp3"
    pause 0.8
    hide black
    hide screen ch2explode
    
    a "Array Operations"
    a "Lets see how we can add in an empty array"

    show adrian explaining
    a "Let's create an empty array and add elements to it step by step."

    #adding
    a "Step 1: We start with an empty array. Imagine you have no boxes yet."
    a "Empty array: [[]"

    a "Step 2: Let's add the number 10 to our array."
    a "Now the array looks like this: [[10]"

    a "Step 3: Let's add the number 20."
    a "Now the array is: [[10, 20]"

    a "Step 4: Let's add the number 30."
    a "Now the array is: [[10, 20, 30]"

    show adrian smiling
    a "You can keep adding more elements to the array, just like putting more things into boxes!"

    #INSErt
    show adrian normal
    a "Let's try insert"
    a "Suppose we have our array: [[10, 20, 30]"
    a "Let's insert the number 15 at index {b}1{/b}."
    
    a "To do this, we move the elements after index {b}1{/b} one position to the right."
    a "So, 20 moves to index 2, and 30 moves to index 3."
    a "Now we put 15 at index {b}1{/b}."
    a "After inserting 15 at index 1: [[10, 15, 20, 30]"
    a "We just moved the whole section so that we can insert 15"

    #removing
    show adrian explaining
    a "Let's try removing"
    a "Suppose we have our array: [[10, 15, 20, 30]"
    a "Let's remove the element at index {b}2{/b}."
    a "That means we remove 20."
    a "After removing, the array is: [[10, 15, 30]"    
    
    show adrian smiling
    a "Here are some common functions you can do with arrays:"
    a "{b}append{/b}: Adds an element to the end of the array."
    a "{b}insert{/b}: Inserts an element at a specific index."
    a "{b}remove{/b}: Removes the first occurrence of a value."
    a "For example, if you have array = [[1, 2, 3, 2] and you do array.remove(2), the array becomes [[1, 3, 2]."

    show adrian normal
    a "{b}NOTE:{/b} It removed based off the {size=+20}index{/size} not the value "
    
    show adrian explaining
    a "{b}pop{/b}: Removes and returns the element at a given index."
    a "If no index is specified, pop() removes and returns the last item in the list."
    a "Example: my_list.pop(2) removes and returns the item at index 2."

    a "{b}index{/b}: Returns the index of the first occurrence of a value."
    a "{b}count{/b}: Counts how many times a value appears in the array."
    a "{b}sort{/b}: Sorts the array."
    a "{b}reverse{/b}: Reverses the order of the array."
    show adrian happy
    a "These functions help you manage and work with arrays easily!"

    show adrian normal
    a "did you get all of that?"
    menu:
        "No":
            show adrian smiling
            a "Lmao, do you wanna go back from the start?"
            menu:
                "Yes":
                    show adrian doubt
                    a "Youre really sure about that?"
                    menu:
                        "Positive":
                            show adrian smug
                            a "Your choice Boss"
                            jump chapter_2_add
                        "Nah Im just joking lets continue":
                            show adrian smiling
                            a"Thats the spirit!"
                "Jk nah":
                    a "I knew you were smart"
        "Yes":
            a "Good job!"
       
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "You hear that? Its time for some questions. Buckle Up Buckeroo"

    jump chapter_2_quiz2

label chapter_2_quiz2:
    a "Lets see what you have learned"

    show adrian normal
    a "Question 1: True or False: You can add elements to an array after it is created."
    menu:
        "True":
            $ chapter_2_questions += 1
            show adrian happy
            a "Correct! You can add elements to an array after it is created."
        "False":
            show adrian mad
            a "Incorrect! Arrays can be modified after creation."

    show adrian normal
    a "Question 2: True or False: Removing an element from an array will automatically shift the remaining elements."
    menu:
        "True":
            $ chapter_2_questions += 1
            show adrian happy
            a "Correct! The elements after the removed one shift left."
        "False":
            show adrian mad
            a "Incorrect! The elements do shift after removal."

    show adrian normal
    a "Question 3: True or False: Inserting an element in the middle of an array requires moving other elements."
    menu:
        "True":
            $ chapter_2_questions += 1
            show adrian happy
            a "Correct! Elements after the insertion point must be moved."
        "False":
            show adrian mad
            a "Incorrect! You do need to move elements to insert in the middle."


    show adrian normal
    a "Question 4: What happens if you try to access an index that does not exist in an array?"
    menu:
        "You get an error":
            $ chapter_2_questions += 1
            show adrian happy
            a "Correct! Accessing an invalid index causes an error."
        "It creates a new element":
            show adrian doubt
            a "Incorrect! It does not create a new element."
        "It ignores the request":
            show adrian mad
            a "Incorrect! It will cause an error."
        "It returns 0":
            show adrian confused
            a "Incorrect! It does not return 0."

    show adrian normal
    a "Question 5: Which operation adds an element to the end of an array?"
    menu:
        "insert":
            show adrian confused
            a "Incorrect! Insert adds at a specific index."
        "append":
            $ chapter_2_questions += 1
            show adrian happy
            a "Correct! The append operation adds to the end."
        "remove":
            show adrian mad
            a "Incorrect! Remove deletes an element."
        "pop":
            show adrian doubt
            a "Incorrect! Pop removes and returns an element."

    show adrian normal
    a "Question 6: If you have array = [[5, 10, 15], what will array.pop(1) do?"
    menu:
        "Remove and return 5":
            show adrian confused
            a "Incorrect! 5 is at index 0."       
        "Remove and return 10":
            $ chapter_2_questions += 1
            show adrian happy
            a "Correct! It removes and returns the element at index 1, which is 10."
        "Add a new element":
            show adrian doubt
            a "Incorrect! Pop removes, not adds."
        "Remove and return 15":
            show adrian mad
            a "Incorrect! 15 is at index 2."

    show adrian happy
    a "{b}OMG GREAT WORK!!!"
    a "Your current score is : [chapter_2_questions]"
    if persistent.chapter_2:
        a "Would you like to Continue on to the Chapter Quiz?"
        menu:
            "Yes":
                jump chapter_2_restart
            "No":
                pass

    jump chapter_2_extra

label chapter_2_extra:


## add more flavour text
label chapter_2_restart:

    a "Your score of [chapter_2_questions] will tell how hard your quiz will be"
    if chapter_2_questions >= 8:
        show adrian smiling
        jump chapter_2_quizmed

    elif chapter_1_questions >= 5:
        show adrian blush
        jump chapter_2_quizeasy

    else:
        show adrian happy
        jump chapter_2_quizhard
        

label chapter_2_quizeasy:
    $ chapter_2_score = 0

    show adrian normal
    a "Welcome to The {size=+20}Easy Chapter Quiz{/size}"

    a "Question 1: True or False: An array can store more than one value."
    menu:
        "True":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! Arrays can store multiple values."
        "False":
            show adrian mad
            a "Incorrect! Arrays can store more than one value."

    a "Question 2: True or False: The first index of an array is always 0."
    menu:
        "True":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! Arrays start at index 0."
        "False":
            show adrian mad
            a "Incorrect! Arrays start at index 0."

    a "Question 3: True or False: Arrays can only store numbers."
    menu:
        "True":
            show adrian mad
            a "Incorrect! Arrays can store any data type."
        "False":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! Arrays can store numbers, strings, and more."

    a "Question 4: True or False: You can change the value of an element in an array."
    menu:
        "True":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! You can change values in an array."
        "False":
            show adrian mad
            a "Incorrect! You can change values in an array."

    a "Question 5: True or False: Arrays are useful for storing lists of data."
    menu:
        "False":
            show adrian mad
            a "Incorrect! Arrays are made for storing lists."
        "True":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! Arrays are great for lists of data."

    show adrian normal
    a "Question 6: What is the correct way to access the first element of an array called 'arr'?"
    menu:
        "arr(first)":
            show adrian confused
            a "Incorrect! Use square brackets and index numbers."
        "arr[[0]":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! The first element is at index 0."
        "arr[[1]":
            show adrian mad
            a "Incorrect! That is the second element."
        "arr{0}":
            show adrian doubt
            a "Incorrect! Use square brackets."

    a "Question 7: Which of these is a valid array?"
    menu:
        "1, 2, 3":
            show adrian mad
            a "Incorrect! Arrays use brackets."
       
        "{1, 2, 3}":
            show adrian confused
            a "Incorrect! That's not array syntax."
        "[[1, 2, 3]":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! That's a valid array."
        "(1, 2, 3)":
            show adrian doubt
            a "Incorrect! That's a tuple, not an array."

    a "Question 8: What does arr.append(4) do to the array arr = [[1, 2, 3]?"
    menu:
        "Removes 4":
            show adrian mad
            a "Incorrect! It adds, not removes."
        "Adds 4 to the end":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! 4 is added to the end."
        "Sorts the array":
            show adrian doubt
            a "Incorrect! It does not sort."
        "Replaces the first element with 4":
            show adrian confused
            a "Incorrect! It adds to the end."

    a "Question 9: What is the length of the array [[5, 6, 7, 8]?"
    menu:
        "5":
            show adrian confused
            a "Incorrect! There are 4 elements."
        "4":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! There are 4 elements."
        "8":
            show adrian doubt
            a "Incorrect! That's just a value in the array."
        "3":
            show adrian mad
            a "Incorrect! There are 4 elements."

    a "Question 10: Which operation removes the last element from an array?"
    menu:
        "count()":
            show adrian doubt
            a "Incorrect! count() counts elements."
        "append()":
            show adrian mad
            a "Incorrect! append() adds an element."
        "pop()":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! pop() removes the last element."
        "insert()":
            show adrian confused
            a "Incorrect! insert() adds at a specific index."

        a "Your quiz score is: [chapter_2_score]"
    jump chapter_2_ending
label chapter_2_quizmed:
    
    $ chapter_2_score = 0

    show adrian normal
    a "Welcome to The {size=+20}Medium Chapter Quiz{/size}"

    # True or False Questions (8)
    a "Question 1: True or False: Arrays can store both numbers and strings in the same array."
    menu:
        "True":
            show adrian mad
            a "Incorrect! Arrays should store elements of the same type."
        "False":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! Arrays store elements of the same type."

    a "Question 2: True or False: The length of an array can be found using the len() function."
    menu:
        "True":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! len() gives the number of elements."
        "False":
            show adrian mad
            a "Incorrect! Use len() to get the length."

    a "Question 3: True or False: You can use a for loop to go through all elements in an array."
    menu:
        "True":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! For loops are great for arrays."
        "False":
            show adrian mad
            a "Incorrect! For loops are commonly used with arrays."

    a "Question 4: True or False: The pop() function removes the first element of an array by default."
    menu:
        "True":
            show adrian mad
            a "Incorrect! pop() removes the last element by default."
        "False":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! pop() removes the last element unless you specify an index."

    a "Question 5: True or False: Arrays can be sorted using the sort() function."
    menu:
        "True":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! sort() arranges elements in order."
        "False":
            show adrian mad
            a "Incorrect! Use sort() to sort arrays."

    a "Question 6: True or False: The index of the last element in an array of length 5 is 5."
    menu:
        "True":
            show adrian mad
            a "Incorrect! The last index is length minus one."
        "False":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! The last index is 4."

    a "Question 7: True or False: Arrays can be used to store a list of student names."
    menu:
        "True":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! Arrays are perfect for lists like names."
        "False":
            show adrian mad
            a "Incorrect! Arrays can store names."

    a "Question 8: True or False: The remove() function deletes all occurrences of a value in an array."
    menu:
        "True":
            show adrian mad
            a "Incorrect! remove() deletes only the first occurrence."
        "False":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! Only the first occurrence is removed."

    # Multiple Choice Questions (7)
    a "Question 9: What is the correct way to add an element to the end of an array called arr?"
    menu:
        "arr.add(5)":
            show adrian mad
            a "Incorrect! Use append() to add."
        "arr.append(5)":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! append() adds to the end."
        "arr.insert(5)":
            show adrian confused
            a "Incorrect! insert() needs an index."
        "arr.push(5)":
            show adrian doubt
            a "Incorrect! push() is not used in Python arrays."

    a "Question 10: What is the index of the first element in an array?"
    menu:
        "1":
            show adrian mad
            a "Incorrect! Indexing starts at 0."
        "0":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! The first index is 0."
        "2":
            show adrian confused
            a "Incorrect! That's the third element."
        "-1":
            show adrian doubt
            a "Incorrect! -1 is the last element."

    a "Question 11: Which function returns the number of times a value appears in an array?"
    menu:
        "count()":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! count() counts occurrences."
        "index()":
            show adrian mad
            a "Incorrect! index() gives the position."
        "append()":
            show adrian confused
            a "Incorrect! append() adds elements."
        "sort()":
            show adrian doubt
            a "Incorrect! sort() arranges elements."

    a "Question 12: If arr = [[2, 4, 6], what does arr[[1] return?"
    menu:
        "2":
            show adrian mad
            a "Incorrect! That's arr[0]."
        "4":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! arr[1] is 4."
        "6":
            show adrian confused
            a "Incorrect! That's arr[2]."
        "1":
            show adrian doubt
            a "Incorrect! That's the index, not the value."

    a "Question 13: Which operation reverses the order of elements in an array?"
    menu:

        "sort()":
            show adrian mad
            a "Incorrect! sort() arranges in order."
        "append()":
            show adrian confused
            a "Incorrect! append() adds elements."
        "remove()":
            show adrian doubt
            a "Incorrect! remove() deletes elements."        
        "reverse()":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! reverse() flips the array."

    a "Question 14: What does arr.insert(1, 99) do to arr = [[10, 20, 30]?"
    menu:
        "Adds 99 at the end":
            show adrian mad
            a "Incorrect! It adds at index 1."
        "Adds 99 at index 1":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! 99 goes at index 1."
        "Removes 99":
            show adrian confused
            a "Incorrect! insert() adds, not removes."
        "Replaces value at index 1 with 99":
            show adrian doubt
            a "Incorrect! It inserts, not replaces."

    a "Question 15: Which of the following is a valid 2D array?"
    menu:
        "[[1, 2], [[3, 4]":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! That's a 2D array."
        "[[1, 2, 3, 4]":
            show adrian mad
            a "Incorrect! That's a 1D array."
        "{{1, 2}, {{3, 4}":
            show adrian confused
            a "Incorrect! That's not array syntax."
        "(1, 2), (3, 4)":
            show adrian doubt
            a "Incorrect! That's a tuple, not an array."

    # Identification Questions (5)
    a "Question 16: Identify the function used to find the position of a value in an array."
    $ answer = renpy.input("Your answer:").strip().lower()
    if answer == "index" or answer == "index()":
        $ chapter_2_score += 1
        show adrian happy
        a "Correct! index() finds the position."
    else:
        show adrian mad
        a "Incorrect! The answer is index()."

    a "Question 17: Identify the function that adds an element at a specific position."
    $ answer = renpy.input("Your answer:").strip().lower()
    if answer == "insert" or answer == "insert()":
        $ chapter_2_score += 1
        show adrian happy
        a "Correct! insert() adds at a position."
    else:
        show adrian mad
        a "Incorrect! The answer is insert()."

    a "Question 18: Identify the function that removes and returns the last element."
    $ answer = renpy.input("Your answer:").strip().lower()
    if answer == "pop" or answer == "pop()":
        $ chapter_2_score += 1
        show adrian happy
        a "Correct! pop() removes and returns the last element."
    else:
        show adrian mad
        a "Incorrect! The answer is pop()."

    a "Question 19: Identify the function that arranges elements in ascending order."
    $ answer = renpy.input("Your answer:").strip().lower()
    if answer == "sort" or answer == "sort()":
        $ chapter_2_score += 1
        show adrian happy
        a "Correct! sort() arranges elements."
    else:
        show adrian mad
        a "Incorrect! The answer is sort()."

    a "Question 20: Identify the function that counts how many times a value appears."
    $ answer = renpy.input("Your answer:").strip().lower()
    if answer == "count" or answer == "count()":
        $ chapter_2_score += 1
        show adrian happy
        a "Correct! count() counts occurrences."
    else:
        show adrian mad
        a "Incorrect! The answer is count()."

    a "Your quiz score is: [chapter_2_score]"
    jump chapter_2_ending


label chapter_2_quizhard:
    
    $ chapter_2_score = 0

    show adrian normal
    a "Welcome to The {size=+20}Medium Chapter Quiz{/size}"

    # True or False Questions (8)
    show adrian normal
    a "Question 1: True or False: Arrays can store both numbers and strings in the same array."
    menu:
        "True":
            show adrian mad
            a "Incorrect! Arrays should store elements of the same type."
        "False":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! Arrays store elements of the same type."

    show adrian normal
    a "Question 2: True or False: The length of an array can be found using the len() function."
    menu:
        "True":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! len() gives the number of elements."
        "False":
            show adrian mad
            a "Incorrect! Use len() to get the length."

    show adrian normal
    a "Question 3: True or False: You can use a for loop to go through all elements in an array."
    menu:
        "True":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! For loops are great for arrays."
        "False":
            show adrian mad
            a "Incorrect! For loops are commonly used with arrays."

    show adrian normal
    a "Question 4: True or False: The pop() function removes the first element of an array by default."
    menu:
        "True":
            show adrian mad
            a "Incorrect! pop() removes the last element by default."
        "False":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! pop() removes the last element unless you specify an index."

    show adrian normal
    a "Question 5: True or False: Arrays can be sorted using the sort() function."
    menu:
        "True":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! sort() arranges elements in order."
        "False":
            show adrian mad
            a "Incorrect! Use sort() to sort arrays."

    show adrian normal
    a "Question 6: True or False: The index of the last element in an array of length 5 is 5."
    menu:
        "True":
            show adrian mad
            a "Incorrect! The last index is length minus one."
        "False":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! The last index is 4."

    show adrian normal
    a "Question 7: True or False: Arrays can be used to store a list of student names."
    menu:
        "True":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! Arrays are perfect for lists like names."
        "False":
            show adrian mad
            a "Incorrect! Arrays can store names."

    show adrian normal
    a "Question 8: True or False: The remove() function deletes all occurrences of a value in an array."
    menu:
        "True":
            show adrian mad
            a "Incorrect! remove() deletes only the first occurrence."
        "False":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! Only the first occurrence is removed."
    
    show adrian normal
    a "Question 9: What is the correct way to add an element to the end of an array called arr?"
    menu:
        "arr.add(5)":
            show adrian mad
            a "Incorrect! Use append() to add."
        "arr.append(5)":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! append() adds to the end."
        "arr.insert(5)":
            show adrian confused
            a "Incorrect! insert() needs an index."
        "arr.push(5)":
            show adrian doubt
            a "Incorrect! push() is not used in Python arrays."

    show adrian normal
    a "Question 10: What is the index of the first element in an array?"
    menu:
        "1":
            show adrian mad
            a "Incorrect! Indexing starts at 0."
        "0":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! The first index is 0."
        "2":
            show adrian confused
            a "Incorrect! That's the third element."
        "-1":
            show adrian doubt
            a "Incorrect! -1 is the last element."

    show adrian normal
    a "Question 11: Which function returns the number of times a value appears in an array?"
    menu:
        "count()":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! count() counts occurrences."
        "index()":
            show adrian mad
            a "Incorrect! index() gives the position."
        "append()":
            show adrian confused
            a "Incorrect! append() adds elements."
        "sort()":
            show adrian doubt
            a "Incorrect! sort() arranges elements."

    show adrian normal
    a "Question 12: If arr = [[2, 4, 6], what does arr[[1] return?"
    menu:
        "2":
            show adrian mad
            a "Incorrect! That's arr[[0]."
        "4":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! arr[[1] is 4."
        "6":
            show adrian confused
            a "Incorrect! That's arr[[2]."
        "1":
            show adrian doubt
            a "Incorrect! That's the index, not the value."

    show adrian normal
    a "Question 13: Which operation reverses the order of elements in an array?"
    menu:

        "sort()":
            show adrian mad
            a "Incorrect! sort() arranges in order."
        "append()":
            show adrian confused
            a "Incorrect! append() adds elements."
        "remove()":
            show adrian doubt
            a "Incorrect! remove() deletes elements."        
        "reverse()":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! reverse() flips the array."

    show adrian normal
    a "Question 14: What does arr.insert(1, 99) do to arr = [[10, 20, 30]?"
    menu:
        "Adds 99 at the end":
            show adrian mad
            a "Incorrect! It adds at index 1."
        "Adds 99 at index 1":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! 99 goes at index 1."
        "Removes 99":
            show adrian confused
            a "Incorrect! insert() adds, not removes."
        "Replaces value at index 1 with 99":
            show adrian doubt
            a "Incorrect! It inserts, not replaces."

    show adrian normal
    a "Question 15: Which of the following is a valid 2D array?"
    menu:
        "[[1, 2], [[3, 4]":
            $ chapter_2_score += 1
            show adrian happy
            a "Correct! That's a 2D array."
        "[[1, 2, 3, 4]":
            show adrian mad
            a "Incorrect! That's a 1D array."
        "{{1, 2}, {{3, 4}":
            show adrian confused
            a "Incorrect! That's not array syntax."
        "(1, 2), (3, 4)":
            show adrian doubt
            a "Incorrect! That's a tuple, not an array."

    show adrian normal
    a "Question 16: Identify the function used to find the position of a value in an array."
    $ answer = renpy.input("Your answer:").strip().lower()
    if answer == "index" or answer == "index()":
        $ chapter_2_score += 1
        show adrian happy
        a "Correct! index() finds the position."
    else:
        show adrian mad
        a "Incorrect! The answer is index()."

    show adrian normal
    a "Question 17: Identify the function that adds an element at a specific position."
    $ answer = renpy.input("Your answer:").strip().lower()
    if answer == "insert" or answer == "insert()":
        $ chapter_2_score += 1
        show adrian happy
        a "Correct! insert() adds at a position."
    else:
        show adrian mad
        a "Incorrect! The answer is insert()."

    show adrian normal
    a "Question 18: Identify the function that removes and returns the last element."
    $ answer = renpy.input("Your answer:").strip().lower()
    if answer == "pop" or answer == "pop()":
        $ chapter_2_score += 1
        show adrian happy
        a "Correct! pop() removes and returns the last element."
    else:
        show adrian mad
        a "Incorrect! The answer is pop()."

    show adrian normal
    a "Question 19: Identify the function that arranges elements in ascending order."
    $ answer = renpy.input("Your answer:").strip().lower()
    if answer == "sort" or answer == "sort()":
        $ chapter_2_score += 1
        show adrian happy
        a "Correct! sort() arranges elements."
    else:
        show adrian mad
        a "Incorrect! The answer is sort()."

    show adrian normal
    a "Question 20: Identify the function that counts how many times a value appears."
    $ answer = renpy.input("Your answer:").strip().lower()
    if answer == "count" or answer == "count()":
        $ chapter_2_score += 1
        show adrian happy
        a "Correct! count() counts occurrences."
    else:
        show adrian mad
        a "Incorrect! The answer is count()."

    show adrian normal
    a "Question 21: Identify the function that removes the first occurrence of a value from an array."
    $ answer = renpy.input("Your answer:").strip().lower()
    if answer == "remove" or answer == "remove()":
        $ chapter_2_score += 1
        show adrian happy
        a "Correct! remove() deletes the first occurrence."
    else:
        show adrian mad
        a "Incorrect! The answer is remove()."

    show adrian normal
    a "Question 22: Identify the function that returns the number of elements in an array."
    $ answer = renpy.input("Your answer:").strip().lower()
    if answer == "len" or answer == "len()":
        $ chapter_2_score += 1
        show adrian happy
        a "Correct! len() returns the length."
    else:
        show adrian mad
        a "Incorrect! The answer is len()."

    show adrian normal
    a "Question 23: Identify the function that adds an element to the end of an array."
    $ answer = renpy.input("Your answer:").strip().lower()
    if answer == "append" or answer == "append()":
        $ chapter_2_score += 1
        show adrian happy
        a "Correct! append() adds to the end."
    else:
        show adrian mad
        a "Incorrect! The answer is append()."

    show adrian normal
    a "Question 24: Identify the function that sorts the array in reverse order."
    $ answer = renpy.input("Your answer:").strip().lower()
    if answer == "sort(reverse=true)" or answer == "sort(reverse=true)":
        $ chapter_2_score += 1
        show adrian happy
        a "Correct! sort(reverse=True) sorts in reverse order."
    else:
        show adrian mad
        a "Incorrect! The answer is sort(reverse=True)."

    show adrian normal
    a "Question 25: Identify the function that creates a shallow copy of an array."
    $ answer = renpy.input("Your answer:").strip().lower()
    if answer == "copy" or answer == "copy()":
        $ chapter_2_score += 1
        show adrian happy
        a "Correct! copy() creates a shallow copy."
    else:
        show adrian mad
        a "Incorrect! The answer is copy()."

    a "Question 26: What will be the result of the following code? \narr = [[2, 4, 6] \narr.append(8) \nWhat is arr now?"
    $ answer = renpy.input("Your answer:").strip().replace(" ", "")
    if answer == "[2,4,6,8]" or answer == "2,4,6,8" or answer "2468":
        $ chapter_2_score += 1
        show adrian happy
        a "Correct! arr is now [[2, 4, 6, 8]."
    else:
        show adrian mad
        a "Incorrect! The answer is [[2, 4, 6, 8]."

    a "Question 27: Given arr = [[5, 10, 15, 20], what does arr.pop(2) return?"
    $ answer = renpy.input("Your answer:").strip()
    if answer == "15":
        $ chapter_2_score += 1
        show adrian happy
        a "Correct! arr.pop(2) returns 15."
    else:
        show adrian mad
        a "Incorrect! The answer is 15."

    a "Question 28: If arr = [[1, 2, 3, 4], what is the result of arr.insert(1, 99)?"
    $ answer = renpy.input("Your answer:").strip().replace(" ", "")
    if answer == "[1,99,2,3,4]" or answer == "1,99,2,3,4":
        $ chapter_2_score += 1
        show adrian happy
        a "Correct! arr becomes [[1, 99, 2, 3, 4]."
    else:
        show adrian mad
        a "Incorrect! The answer is [[1, 99, 2, 3, 4]."

    a "Question 29: What is the output of len([[7, 8, 9, 10, 11])?"
    $ answer = renpy.input("Your answer:").strip()
    if answer == "5":
        $ chapter_2_score += 1
        show adrian happy
        a "Correct! The length is 5."
    else:
        show adrian mad
        a "Incorrect! The answer is 5."

    a "Question 30: If arr = [[3, 6, 9, 6], what does arr.count(6) return?"
    $ answer = renpy.input("Your answer:").strip()
    if answer == "2":
        $ chapter_2_score += 1
        show adrian happy
        a "Correct! 6 appears twice."
    else:
        show adrian mad
        a "Incorrect! The answer is 2."


    a "Your quiz score is: [chapter_2_score]"
    a "{size=+20} OMG Yaaaay!!!"

    jump chapter_2_ending
    

label chapter_2_ending:
    a "Your Score is [chapter_2_score]!"
    a "Would You like to test again?"
    menu:
        "Yes":
            jump chapter_2_restart
        "No":
            pass
    show adrian happy
    a "You have finished chapter 2. You can continue to Chapter 3!"
    jump menu
    
    
    $ persistent.chapter_2 = True