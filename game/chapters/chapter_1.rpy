define a = Character("Adrian") 
screen chapter_1_introscreen:
    vbox:
        spacing 20
        xalign 0.5
        yalign 0.5
        text "Chapter 1: Abstract Data Structures" size 60 color "#FFFFFF" outlines [(5, "#000000", 0, 0)]
label chapter_1_intro:
    
    show black
    pause 1.0
    show screen chapter_1_introscreen
    pause 2.0
    scene mt tree with dissolve
    pause 1.0
    hide screen chapter_1_introscreen
    show adrian smiling at center:
        smaller
    with dissolve
    
    if persistent.chapter_1 == True:
        a "Hey Welcome back to Chapter 1"
        a "Would you like to take the quizzes again?"
        menu :
            "Yes":
                jump chapter_1_quiz1
            "No":
                pass
    else:
        pass
    a "Welcome to Chapter 1"
    a "Today, we’re diving into something that forms the backbone of computer science—data structures and algorithms."
    a "These are the building blocks of efficient programming, and mastering them can make all the difference in how we handle large amounts of data"
    
    show adrian explaining:
        smaller

    a "In this chapter, we will cover the basi abstract datastructures"
    
    show adrian normal:
        smaller

    show adrian smiling:
        smaller
    a "Let's get started with the first topic."
    a "But before we do that, look at this this"

    play sound "sfx/slideleft.mp3"
    show adrian smiling at left with move:
        smaller
    a "Slide to the left"

    play sound "sfx/slideright.mp3"
    show adrian smiling at right with move:
        smaller

    
    a "Slide to the right"

    show adrian explaining at left with move:
        smaller

    transform right_centered:
        zoom 1.5
        xalign 0.8   # Aligns to the left
        yalign 0.5

    show adrian smiling     
    a "Now I have your attention, let’s talk about data structures and algorithms."

    show tree at right_centered
    a "Data Structures : They are ways to organize and store data in a computer so that it can be used efficiently."
    hide tree

    show graph at right_centered
    a "Think of them as containers that hold data in a specific format, making it easier to access and manipulate."
    hide graph

    show linklist at right_centered
    a "Imagine you’re looking for a book in a massive library with no organization." 
    hide linklist

    show stack at right_centered
    a "Finding what you need would take forever, right? That’s exactly what happens when we don’t structure our data efficiently in programming."
    hide stack

    show adrian smiling at center with move
    a "There are three common problems that data structures help us solve: data search, processer speed, multiple requests"

    # Add more content for Chapter 1 here...

    jump chapter_1_explanation1

label chapter_1_explanation1:
    show adrian explaining at center:
        smaller

    a "Now, let’s talk about data search algorithms."
    a "These algorithms help us find specific data within a larger dataset quickly and efficiently."
    
    show adrian normal:
        smaller

    #add visual 

    a "Data search : is the process of retrieving relevant information from a dataset, 
    database, or the web using methods like keyword search, pattern matching, and ranking algorithms."
    
    show adrian smiling:
        smaller

    a "Efficient search techniques, such as binary search or hash-based lookup, enhance speed and accuracy in locating data."
     
    #add visual
    show adrian normal
    a "Next, we have Processor Speed."
    a "Processor speed although being very high, falls limited if the data grows to billion records."
    a "In such cases, we need to optimize our algorithms and data structures to ensure that our programs run efficiently."

    show adrian explaining:
        smaller
    a "Last is Multiple Requests."
    a "When multiple requests are made to access or modify data simultaneously, it can lead to bottlenecks and inefficiencies."
    a "Data structures like queues and stacks help manage these requests effectively, 
    ensuring that data is processed in the right order and without conflicts."

    show adrian normal:
        smaller
    a "There are 3 Characteristics of data structures that we need to consider when choosing the right one for our needs."
    a "These characteristics are: Time Complexity, Space Complexity, and Correctness."

    show adrian explaining:
        smaller
    a "Time Complexity: refers to the amount of time an algorithm takes to complete as the size of the input data increases."
    a "It’s crucial to choose data structures that minimize time complexity, especially for large datasets."
    a "For example, A hash table is like a magic shortcut for finding things. Instead of checking every item one by one, 
    it uses a unique code to jump straight to the right spot—kind of like knowing exactly where your keys are instead of searching the whole house."

    show adrian normal:
        smaller
    a "Space Complexity: refers to the amount of memory an algorithm uses as the size of the input data increases."
    a "It’s important to consider space complexity when working with limited memory resources or large datasets."
    a "For example, a linked list uses less memory than an array for storing data, but it may take longer to access specific elements."

    show adrian explaining:
        smaller
    a "Correctness: refers to the accuracy and reliability of an algorithm in producing the expected results."
    a "Choosing the right data structure ensures that our algorithms are correct and produce the desired outcomes."
    a "Imagine you have a big list of words written on cards, all neatly arranged from A to Z. 
    Instead of flipping through one card at a time, a binary search tree works like a smart guessing game." 
    a "You start in the middle—if your word is earlier in the alphabet, you look in the left half; if it's later, you check the right"

    jump chapter_1_quiz1

label chapter_1_quiz1:
    $ chapter_1_questions = 0
    show adrian smiling at center:
        smaller

    a "Now that we’ve covered the basics, let’s see how well you understand these concepts."
    a "I have a few questions for you to test your knowledge."
    a "Don’t worry, it’s all part of the learning process, and I’m here to help you along the way."
    a "Here’s your first question:"

    a "What is the primary purpose of data structures in programming?"
    menu:
        "To organize and store data efficiently":
            a "Correct! Data structures are essential for organizing and storing data efficiently."
            $ chapter_1_questions += 1
            
        "To write code faster":
            a "Incorrect. While data structures can help with code efficiency, their primary purpose is to organize and store data."
        "To create user interfaces":
            a "Incorrect. Data structures are not primarily used for creating user interfaces."
    a "Next question:"

    a "Which of the following is NOT a characteristic of data structures?"
    menu:   
        "Time Complexity":
            a "Incorrect. Time complexity is a characteristic of data structures."
        "Space Complexity":
            a "Incorrect. Space complexity is a characteristic of data structures."
        "User Interface Design":
            a "Correct! User interface design is not a characteristic of data structures."
            $ chapter_1_questions += 1
    a "Next question:"

    a "What is the difference between a stack and a queue?"
    menu:
        "A stack is LIFO (Last In First Out) and a queue is FIFO (First In First Out)":
            a "Correct! A stack is LIFO and a queue is FIFO."
            a "Omg You remembered! Good job!"
            $ chapter_1_questions += 1
        "A stack is FIFO and a queue is LIFO":
            a "Incorrect. A stack is LIFO and a queue is FIFO."
        "There is no difference":
            a "Incorrect. There is a difference between a stack and a queue."
    a "Next question:"

    a "What is the primary purpose of search algorithms?"
    menu:
        "To find specific data within a larger dataset quickly and efficiently":
            a "Correct! Search algorithms are designed to find specific data quickly and efficiently."
            $ chapter_1_questions += 1
        "To sort data in a specific order":
            a "Incorrect. Sorting algorithms are used for arranging data, not searching for it."
        "To delete data from a dataset":
            a "Incorrect. Deletion algorithms are used for removing data, not searching for it."
        
            

    a "Your Current Score is [chapter_1_questions] out of 4"
    if persistent.chapter_1 == True:
        a "Would you like to continue to the next quiz?"
        menu:
            "Yes":
                jump chapter_1_quiz2
            "No":
                pass


label chapter_1_explanation2:
    show adrian explaining at center:
        smaller
    
    a "Now, let’s dive deeper into the characteristics of data structures."
    a "From the data structure point of view, following are some important categories of algorithms "
    a "1. Search or Searching Algorithms: These algorithms help us find specific data within a larger dataset quickly and efficiently."
    a "2. Sort or Sorting Algorithms: These algorithms arrange data in a specific order, such as ascending or descending, to make it easier to analyze and retrieve."
    a "3. Insert or Insertion Algorithms: These algorithms add new data to an existing dataset while maintaining its structure and order."
    a "4. Update or Updating Algorithms: These algorithms modify existing data in a dataset, ensuring that the changes are reflected accurately."
    a "5. Delete or Deletion Algorithms: These algorithms remove specific data from a dataset, ensuring that the remaining data remains organized and accessible."

    a "There are many more algorithms, but these are the most common ones that we will encounter in this chapter."
    a "Now, let’s take a closer look at some of these algorithms and how they work."

    show adrian smiling
    a "But First, What do you think of algorithmns?"
    menu:
        "Theyre kinda cute":
            show adrian blush
            a "Haha, I guess you could say that! Algorithms can be cute in their own way, especially when they solve problems efficiently." 
            show adrian smug
            a "do you think I am cute too?"
        "Theyre boring":
            show adrian normal
            a "I understand, algorithms can seem boring at first, but they are essential for solving complex problems in programming."
        "Theyre hot":
            show adrian smug
            a "Haha, I guess you could say that! Algorithms can be hot when they solve problems efficiently and elegantly."
    
    show adrian explaining at center
    a "Now Lets continue to algorithms"
    a "Algorithms are step-by-step procedures for solving problems or performing tasks."
    a "They are essential for processing data efficiently and effectively."
    a "Every single procedure that a computer performs is an algorithm"
    a "An algorithm states the actions to be executed and the order in which these actions are to be executed."

    show adrian normal
    a "There are 3 Cases for algorithms. What are cases you ask?  Think of cases like different ways something can happen. Imagine you're playing a guessing game"

    a "Well, there are 3 cases for algorithms: Best Case, Average Case, and Worst Case."
    a "1. Best Case: This is the scenario where the algorithm performs the least amount of work, resulting in the fastest execution time."
    a "2. Average Case: This is the scenario where the algorithm performs a moderate amount of work, resulting in an average execution time."
    a "3. Worst Case: This is the scenario where the algorithm performs the most amount of work, resulting in the slowest execution time."

    show adrian smug
    a "Its like when youre going to the bathroom, sometimes you get there quickly, sometimes you have to wait in line,
        and sometimes you have to wait for a long time because someone is taking forever."
    show adrian smiling
    a "algorithms are like that too, they can be fast, slow, or somewhere in between depending on the situation."

    a "Speaking of algorithms, do you have a type?"

    show adrian blush
    a "I like girls teehee. What about you?"
    menu:
        "I like boys":
            a "Ooooh Very mucho intresting. My friend is a dude, maybe you two can meet up"
        "I like girls":
            a "I like girks too, Teehee. Theyre so Pretty and cute"
        "I prefer not to say":
            a "Thats okay, you dont have to say. Its your personal preference and I respect that"

    show adrian normal
    a "So you ask me why the random question about types?"
    a "Well, just like how we have different types of people, there are also different types of algorithms."
    a "and different types have different characteristics and performance."
    a "and there are certain characteristics before we call something an algorithm."

    a "1. Unambiguous: An algorithm must be clear and unambiguous, meaning that each step should be precisely defined and easy to understand."
    show adrian smiling
    a "Its like you have to be clear about what you want, like when you order food at a restaurant."
    a "like you have to say exactly what you want, like 'I want a cheeseburger with no pickles and extra cheese.'"

    show adrian explaining
    a "2. Input: An algorithm should have zero or more inputs, which are the data that the algorithm will process."
    a "Its like when you order food, you have to give them your order, like 'I want a cheeseburger with no pickles and extra cheese.'"

    show adrian normal
    a "3. Output: An algorithm should produce one or more outputs, which are the results of the algorithm's processing."
    a "Its like when you order food, you get your food as the output, like 'Here is your cheeseburger with no pickles and extra cheese.'"

    show adrian explaining
    a "4. Finiteness: An algorithm must terminate after a finite number of steps, meaning it should not run indefinitely."
    a "Its like when you order food, you have to wait for your food to be ready, and then you can eat it."
    a "1, 2, 3. Start to Finish"

    show adrian smiling
    a "5. Effectiveness: An algorithm should be effective, meaning that it should be able to solve the problem it was designed for in a reasonable amount of time."
    a "Your Burger should be perfect and should get what you want within the time you order it"

    show adrian normal
    a "6. Feasibility: An algorithm should be feasible, meaning that it should be able to be implemented with the available resources and technology."
    a "Your burger should always be available"

    show adrian smiling
    a "7. Indipendent: An algorithm should be independent of any programming language or platform, meaning that it can be implemented in any programming language or platform."
    a "and the burger you get should be only that and nothing more. If you get extra burgers or side orders it would be good for you but bad for business"
    a "So your algorithmn should stand alone on its two feet"

    play sound "sfx/bell.mp3"
    a "You hear that? Its time for some questions. Buckle Up Buckeroo"

    jump chapter_1_quiz2

label chapter_1_quiz2:
    
    show adrian smiling at center
    a "Lets start with a few questions"

    show adrian normal
    a "Which of the following is NOT a common category of algorithmns?"
    menu:
        "Searching":
            show adrian sad
            a "Incorrect. Searching is a common category of algorithms."
        "Sorting":
            show adrian sad
            a "Incorrect. Sorting is a common category of algorithms."
        "Exctracting":
            show adrian happy
            a "Correct! Extracting is not typically listed as a common category of algorithms."
            $ chapter_1_questions += 1
        "deletion":
            show adrian sad
            a "Incorrect. Deletion is a common category of algorithms."
    a "Next question:"

    show adrian normal
    a "Which of the following is NOT a characteristic of a good algorithm?"
    menu:
        "Unambiguous":
            show adrian sad
            a "Incorrect. Unambiguous is a key characteristic of a good algorithm."
        "Infinite steps":
            show adrian happy
            a "Correct! A good algorithm must always terminate after a finite number of steps."
            $ chapter_1_questions += 1
        "Effective":
            show adrian sad
            a "Incorrect. Effectiveness is a key characteristic of a good algorithm."
        "Feasible":
            show adrian sad
            a "Incorrect. Feasibility is a key characteristic of a good algorithm."
    a "Next Question: "

    show adrian normal
    a "True or False: Insertion algorithms add new data while maintaining the dataset’s structure."
    menu:
        "True":
            show adrian happy
            a "You are Correct. Good JOB!!"
            $ chapter_1_questions += 1
        "False":
            show adrian sad
            a "Incorrect. Of course you add new data, you insert something."
    a "Next Question: "

    show adrian normal
    a "A ____ algorithm modifies existing data in a dataset to reflect updates correctly."

    $ chapter_1_fillin = renpy.input("Fill in the blank").strip()

    if chapter_1_fillin.lower() == "updating":
        show adrian happy
        a "You are Correct. Good Job!!"
        $ chapter_1_questions += 1
        jump chapter_1_continue
    else:
        show adrian sad
        a "Sorry, wrong answer."
        jump chapter_1_continue

label chapter_1_continue:
    a "Next Question:"
    show adrian normal
    a "Which of the following best describes the 'Worst Case' scenario for an algorithm?"
    menu:
        "The scenario where the algorithm performs the most amount of work and takes the longest time":
            show adrian happy
            a "Correct! The worst case is when the algorithm takes the most time to complete."
            $ chapter_1_questions += 1
        "The scenario where the algorithm performs the least amount of work":
            show adrian sad
            a "Incorrect. That's the best case scenario."
        "The scenario where the algorithm performs an average amount of work":
            show adrian sad
            a "Incorrect. That's the average case scenario."
        "The scenario where the algorithm never finishes":
            show adrian sad
            a "Incorrect. A good algorithm should always finish in a finite number of steps."
    a "Next Question"

    show adrian normal
    a "Which of the following is NOT a characteristic of a good algorithm?"
    menu:
        "Ambiguity":
            show adrian happy
            a "Correct! A good algorithm should be unambiguous, meaning every step is clearly defined."
            $ chapter_1_questions += 1
        "Finiteness":
            show adrian sad
            a "Incorrect. Finiteness is a key characteristic of a good algorithm."
        "Effectiveness":
            show adrian sad
            a "Incorrect. Effectiveness is a key characteristic of a good algorithm."
        "Feasibility":
            show adrian sad
            a "Incorrect. Feasibility is a key characteristic of a good algorithm."
    a "Next Question"

    show adrian normal
    a "Here's a tricky one: Which type of algorithm is responsible for maintaining the structure and order of a dataset after new data is added?"
    menu:
        "Insertion Algorithm":
            show adrian happy
            a "Correct! Insertion algorithms add new data while keeping the dataset's structure and order intact."
            $ chapter_1_questions += 1
        "Sorting Algorithm":
            show adrian sad
            a "Not quite. Sorting algorithms arrange data, but insertion algorithms handle adding new data while maintaining order."
        "Deletion Algorithm":
            show adrian sad
            a "Incorrect. Deletion algorithms remove data, not add it."
        "Searching Algorithm":
            show adrian sad
            a "Incorrect. Searching algorithms help find data, not insert it."

    show adrian normal
    a "Which of the following algorithms is primarily used to arrange data in a specific order, such as ascending or descending?"
    menu:
        "Sorting Algorithm":
            show adrian happy
            a "Correct! Sorting algorithms are used to arrange data in a particular order."
            $ chapter_1_questions += 1
        "Insertion Algorithm":
            show adrian sad
            a "Incorrect. Insertion algorithms add new data, but don't necessarily arrange all data."
        "Searching Algorithm":
            show adrian sad
            a "Incorrect. Searching algorithms are for finding data."
        "Updating Algorithm":
            show adrian sad
            a "Incorrect. Updating algorithms modify existing data."
    show adrian happy
    a "Good job!!! Your Score of [chapter_1_questions] has been Graded"

    if persistent.chapter_1 == True:
        a "Would you like to continue to the chapter quiz?"
        menu:
            "yes":
                jump chapter_1_restart
            "no":
                pass

    jump chapter_1_explanation3


label chapter_1_explanation3:
    show adrian smiling 
    a "We'll be tackling the last few topics of this chapter, so hang in there! Okay?"
    show adrian explaining
    a "How can one write an algorithm?"
    a "Well, there are several steps to writing an algorithm, and they can vary depending on the problem you're trying to solve."
    a "As we know that all programming languages share basic code constructs like loops (do, for, while), 
        flow-control (if-else), etc. These common constructs can be used to write an algorithm."
    a "We write algorithms in a step-by-step manner, but it is not always the case. 
        Algorithm writing is a process and is executed after the problem domain is well-defined."
    show adrian smiling
    a "Now Good Computer Programming. What is it?"

    show adrian explaining
    a "Programs consists of two things: Algorithms and data structures."
    a "Algorithms are the step-by-step procedures for solving problems, while data structures are the ways to organize and store data."
    a "A data structure represents the logical relationship that exists between individual elements of data to carry out certain tasks"
    show adrian smiling
    a "Imagine you have a big toy box, but instead of tossing all your toys in randomly, you organize them in different ways to make finding them easier."
    show adrian explaining
    a "A data structure defines a way of organizing all data items that consider not only the elements 
        stored but also stores the relationship between the elements"
    show adrian normal
    a "For example, if you have a box for action figures, a shelf for books, and a bin for building blocks,
        you can quickly find what you want without digging through a jumbled mess."

    show adrian normal
    a "These are a number of Features for a good program"
    a "Run Efficiently and Correctly"
    a "Have a user friendly interface"
    a "Be easy to read and Understand"
    a "Be easy to debug"
    a "Be easy to modify"
    a "Be easy to maintin"

    show adrian explaining
    a "Let's try to learn algorithm-writing using an example."

    a "The problem: We need to design an algorithm to add two numbers and display the result."

    show adrian smiling
    a "Think of it like counting two sets of toys. If you have 5 toys in one pile and 3 in another, 
        you add them together to find the total."

    show adrian explaining
    a "Step 1: START—this tells us we are beginning the process."
    a "Step 2: Declare three numbers—let's call them a, b, and c."
    a "Step 3: Assign values to a and b. Let's say a is 5 and b is 3."
    a "Step 4: Add a and b together."
    a "Step 5: Store the result in c."
    a "Step 6: Print c—the final total."
    a "Step 7: STOP—the algorithm is complete!"

    show adrian normal
    a "Just like that, we've built a simple step-by-step process to solve a problem."
    a "Algorithms are all about breaking tasks into clear instructions so that computers (or even people!) can follow them easily."
    
    show adrian smug
    play sound "sfx/bell.mp3"
    a "Uh Oh, Theres that sound again. Its time for your chapter quiz!"
    a "Since you got [chapter_1_questions] you will be taking the"

    if chapter_1_questions < 9:
        show adrian happy
        a "You will be getting the Hard Quiz"
        jump chapter_1_quizhard
    
    if chapter_1_questions >= 8:
        show adrian smiling
        a "You will be getting the Moderate Quiz"
        jump chapter_1_quiz_medium
    
    if chapter_1_questions >=4:
        show adriab blush
        a "You will be getting the Easy Quiz"
        jump chapter_1_quizeasy

label chapter_1_restart:    
    a "Your score of [chapter_1_questions] will tell how hard your quiz will be"
    if chapter_1_questions >= 8:
        show adrian smiling
        jump chapter_1_quiz_medium
    elif chapter_1_questions >= 4:
        show adrian blush
        jump chapter_1_quiz_easy
    else:
        show adrian happy
        jump chapter_1_quiz_hard
    

        
label chapter_1_quiz_hard:
    $ chapter_1_score = 0

    show adrian smiling at center
    a "Welcome to the Moderate Quiz! Let's test your knowledge with some medium-difficulty questions."

    # Question 1 - Multiple Choice
    a "1. Which data structure allows elements to be added or removed from both ends?"
    menu:
        "Deque":
            show adrian happy
            $ chapter_1_score += 1
            a "Correct! A deque allows insertion and deletion at both ends."
        "Stack":
            show adrian sad
            a "Incorrect. Stack only allows insertion and removal at one end."
        "Queue":
            show adrian sad
            a "Incorrect. Queue only allows insertion at one end and removal at the other."
        "Array":
            show adrian sad
            a "Incorrect. Array does not have this property."

    # Question 2
    a "2. Which of the following is NOT a characteristic of data structures?"
    menu:
        "Time Complexity":
            show adrian sad
            a "Incorrect. Time complexity is a characteristic of data structures."
        "Space Complexity":
            show adrian sad
            a "Incorrect. Space complexity is a characteristic of data structures."
        "User Interface Design":
            show adrian happy
            a "Correct! User interface design is not a characteristic of data structures."
            $ chapter_1_score += 1

    # Question 3
    a "3. What is the difference between a stack and a queue?"
    menu:
        "A stack is LIFO (Last In First Out) and a queue is FIFO (First In First Out)":
            show adrian happy
            a "Correct! A stack is LIFO and a queue is FIFO."
            $ chapter_1_score += 1
        "A stack is FIFO and a queue is LIFO":
            show adrian sad
            a "Incorrect. A stack is LIFO and a queue is FIFO."
        "There is no difference":
            show adrian sad
            a "Incorrect. There is a difference between a stack and a queue."

    # Question 4
    a "4. What is the primary purpose of search algorithms?"
    menu:
        "To find specific data within a larger dataset quickly and efficiently":
            show adrian happy
            a "Correct! Search algorithms are designed to find specific data quickly and efficiently."
            $ chapter_1_score += 1
        "To sort data in a specific order":
            show adrian sad
            a "Incorrect. Sorting algorithms are used for arranging data, not searching for it."
        "To delete data from a dataset":
            show adrian sad
            a "Incorrect. Deletion algorithms are used for removing data, not searching for it."

    # Question 5
    a "5. Which of the following is NOT a common category of algorithms?"
    menu:
        "Searching":
            show adrian sad
            a "Incorrect. Searching is a common category of algorithms."
        "Sorting":
            show adrian sad
            a "Incorrect. Sorting is a common category of algorithms."
        "Extracting":
            show adrian happy
            a "Correct! Extracting is not typically listed as a common category of algorithms."
            $ chapter_1_score += 1
        "Deletion":
            show adrian sad
            a "Incorrect. Deletion is a common category of algorithms."

    # Question 6
    a "6. Which of the following is NOT a characteristic of a good algorithm?"
    menu:
        "Unambiguous":
            show adrian sad
            a "Incorrect. Unambiguous is a key characteristic of a good algorithm."
        "Infinite steps":
            show adrian happy
            a "Correct! A good algorithm must always terminate after a finite number of steps."
            $ chapter_1_score += 1
        "Effective":
            show adrian sad
            a "Incorrect. Effectiveness is a key characteristic of a good algorithm."
        "Feasible":
            show adrian sad
            a "Incorrect. Feasibility is a key characteristic of a good algorithm."

    # Question 7
    a "7. True or False: Insertion algorithms add new data while maintaining the dataset’s structure."
    menu:
        "True":
            show adrian happy
            a "You are Correct. Good JOB!!"
            $ chapter_1_score += 1
        "False":
            show adrian sad
            a "Incorrect. Of course you add new data, you insert something."

    # Question 8
    a "8. A ____ algorithm modifies existing data in a dataset to reflect updates correctly."
    $ answer = renpy.input("Fill in the blank").strip()
    if answer.lower() == "updating":
        show adrian happy
        a "You are Correct. Good Job!!"
        $ chapter_1_score += 1
        jump ch1_hard1
    else:
        show adrian sad
        a "Sorry, wrong answer."
        jump ch1_hard1

    
    # Question 9
    label ch1_hard1:
    a "9. A ____ is a linear data structure where elements are added and removed from only one end."
    $ answer = renpy.input("Fill in the blank").strip()
    if answer.lower() == "stack":
        show adrian happy
        a "Correct! Stack is the right answer."
        $ chapter_1_score += 1
        jump ch1_hard2

    else:
        show adrian sad
        a "Sorry, the correct answer is 'stack'."
        jump ch1_hard2
    # Question 10
    label ch1_hard2:# Fill in the Blank 2
    a "10. The process of arranging data in a particular order is called ____."
    $ answer = renpy.input("Fill in the blank").strip()
    if answer.lower() == "sorting":
        show adrian happy
        a "Correct! Sorting is the process."
        $ chapter_1_score += 1
        jump ch1_hard3
    else:
        show adrian sad
        a "Sorry, the correct answer is 'sorting'."
        jump ch1_hard3
    # Question 11
    label ch1_hard3:
    # Fill in the Blank 3
    a "11. In a ____ search, the dataset must be sorted before searching."
    $ answer = renpy.input("Fill in the blank").strip()
    if answer.lower() == "binary":
        show adrian happy
        a "Correct! Binary search requires a sorted dataset."
        $ chapter_1_score += 1
        jump ch1_hard4
    else:
        show adrian sad
        a "Sorry, the correct answer is 'binary'."
        jump ch1_hard4
    # Question 12
    label ch1_hard4:
    # Multiple Choice 1
    a "12. Which data structure uses nodes that point to the next node in the sequence?"
    menu:
        "Linked List":
            show adrian happy
            a "Correct! Linked lists use nodes that point to the next node."
            $ chapter_1_score += 1
        "Array":
            show adrian sad
            a "Incorrect. Arrays do not use nodes."
        "Stack":
            show adrian sad
            a "Incorrect. Stacks do not use nodes."
        "Queue":
            show adrian sad
            a "Incorrect. Queues do not use nodes."
    # Question 14
    # Multiple Choice 2
    a "13. Which of the following is NOT a linear data structure?"
    menu:
        "Tree":
            show adrian happy
            a "Correct! Trees are non-linear data structures."
            $ chapter_1_score += 1
        "Queue":
            show adrian sad
            a "Incorrect. Queue is linear."
        "Stack":
            show adrian sad
            a "Incorrect. Stack is linear."
        "Array":
            show adrian sad
            a "Incorrect. Array is linear."
    # Question 15
    # Multiple Choice 3
    a "14. Which operation is used to remove an element from the end of a stack?"
    menu:
        "Pop":
            show adrian happy
            a "Correct! Pop removes the top element from a stack."
            $ chapter_1_score += 1
        "Push":
            show adrian sad
            a "Incorrect. Push adds an element."
        "Enqueue":
            show adrian sad
            a "Incorrect. Enqueue is for queues."
        "Dequeue":
            show adrian sad
            a "Incorrect. Dequeue is for queues."
    # Question 16
    # Multiple Choice 4
    a "15. Which of the following best describes a queue?"
    menu:
        "First In, First Out":
            show adrian happy
            a "Correct! Queue is FIFO."
            $ chapter_1_score += 1
        "Last In, First Out":
            show adrian sad
            a "Incorrect. That's a stack."
        "Random Access":
            show adrian sad
            a "Incorrect. That's an array."
        "Hierarchical":
            show adrian sad
            a "Incorrect. That's a tree."

    show adrian smiling
    a "Great job! You finished the Moderate Quiz. Your total score is [chapter_1_score]."

    #ADD MATCHING TYPE
    # Matching Type Question
    a "Let's try a matching type question! Match the data structure to its description. Type your answers as a comma-separated list (e.g., 1A,2B,3C,4D)."

    a "1. Stack\n2. Queue\n3. Linked List\n4. Tree"
    a "A. Each element points to the next; dynamic size.\nB. Hierarchical structure with parent and child nodes.\nC. First In, First Out (FIFO) structure.\nD. Last In, First Out (LIFO) structure."

    $ matching_answer = renpy.input("Enter your matches (e.g., 1D,2C,3A,4B):").strip().replace(" ", "").lower()

    # Accept both "1d,2c,3a,4b" and "1d,2c,3a,4b," etc.
    if matching_answer.startswith("1d,2c,3a,4b"):
        show adrian happy
        a "Excellent! All your matches are correct."
        $ chapter_1_score += 1
    else:
        show adrian sad
        a "Not quite. The correct matches are: 1D, 2C, 3A, 4B."
    
    # Another Matching Type Question
    a "Let's do another matching question! Match the algorithm to its description. Type your answers as a comma-separated list (e.g., 1A,2B,3C,4D)."

    a "1. Binary Search\n2. Bubble Sort\n3. Insertion\n4. Deletion"
    a "A. Removes data from a dataset.\nB. Adds new data to a dataset.\nC. Finds data in a sorted list by repeatedly dividing the search interval in half.\nD. Repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order."

    $ matching_answer2 = renpy.input("Enter your matches (e.g., 1C,2D,3B,4A):").strip().replace(" ", "").lower()

    if matching_answer2.startswith("1c,2d,3b,4a"):
        show adrian happy
        a "Excellent! All your matches are correct."
        $ chapter_1_score += 1
    else:
        show adrian sad
        a "Not quite. The correct matches are: 1C, 2D, 3B, 4A."

    jump chapter_1_ending

label chapter_1_quiz_medium:
    $ chapter_1_score = 0

    show adrian smiling at center
    a "Welcome to the Moderate Quiz! Let's test your knowledge with some medium-difficulty questions."

    # Question 1 - Multiple Choice
    a "1. Which data structure allows elements to be added or removed from both ends?"
    menu:
        "Deque":
            show adrian happy
            $ chapter_1_score += 1
            a "Correct! A deque allows insertion and deletion at both ends."
        "Stack":
            show adrian sad
            a "Incorrect. Stack only allows insertion and removal at one end."
        "Queue":
            show adrian sad
            a "Incorrect. Queue only allows insertion at one end and removal at the other."
        "Array":
            show adrian sad
            a "Incorrect. Array does not have this property."

    # Question 2
    a "2. Which of the following is NOT a characteristic of data structures?"
    menu:
        "Time Complexity":
            show adrian sad
            a "Incorrect. Time complexity is a characteristic of data structures."
        "Space Complexity":
            show adrian sad
            a "Incorrect. Space complexity is a characteristic of data structures."
        "User Interface Design":
            show adrian happy
            a "Correct! User interface design is not a characteristic of data structures."
            $ chapter_1_score += 1

    # Question 3
    a "3. What is the difference between a stack and a queue?"
    menu:
        "A stack is LIFO (Last In First Out) and a queue is FIFO (First In First Out)":
            show adrian happy
            a "Correct! A stack is LIFO and a queue is FIFO."
            $ chapter_1_score += 1
        "A stack is FIFO and a queue is LIFO":
            show adrian sad
            a "Incorrect. A stack is LIFO and a queue is FIFO."
        "There is no difference":
            show adrian sad
            a "Incorrect. There is a difference between a stack and a queue."

    # Question 4
    a "4. What is the primary purpose of search algorithms?"
    menu:
        "To find specific data within a larger dataset quickly and efficiently":
            show adrian happy
            a "Correct! Search algorithms are designed to find specific data quickly and efficiently."
            $ chapter_1_score += 1
        "To sort data in a specific order":
            show adrian sad
            a "Incorrect. Sorting algorithms are used for arranging data, not searching for it."
        "To delete data from a dataset":
            show adrian sad
            a "Incorrect. Deletion algorithms are used for removing data, not searching for it."

    # Question 5
    a "5. Which of the following is NOT a common category of algorithms?"
    menu:
        "Searching":
            show adrian sad
            a "Incorrect. Searching is a common category of algorithms."
        "Sorting":
            show adrian sad
            a "Incorrect. Sorting is a common category of algorithms."
        "Extracting":
            show adrian happy
            a "Correct! Extracting is not typically listed as a common category of algorithms."
            $ chapter_1_score += 1
        "Deletion":
            show adrian sad
            a "Incorrect. Deletion is a common category of algorithms."

    # Question 6
    a "6. Which of the following is NOT a characteristic of a good algorithm?"
    menu:
        "Unambiguous":
            show adrian sad
            a "Incorrect. Unambiguous is a key characteristic of a good algorithm."
        "Infinite steps":
            show adrian happy
            a "Correct! A good algorithm must always terminate after a finite number of steps."
            $ chapter_1_score += 1
        "Effective":
            show adrian sad
            a "Incorrect. Effectiveness is a key characteristic of a good algorithm."
        "Feasible":
            show adrian sad
            a "Incorrect. Feasibility is a key characteristic of a good algorithm."

    # Question 7
    a "7. True or False: Insertion algorithms add new data while maintaining the dataset’s structure."
    menu:
        "True":
            show adrian happy
            a "You are Correct. Good JOB!!"
            $ chapter_1_score += 1
        "False":
            show adrian sad
            a "Incorrect. Of course you add new data, you insert something."

    # Question 8
    a "8. A ____ algorithm modifies existing data in a dataset to reflect updates correctly."
    $ answer = renpy.input("Fill in the blank").strip()
    if answer.lower() == "updating":
        show adrian happy
        a "You are Correct. Good Job!!"
        $ chapter_1_score += 1
        jump ch1_med1
    else:
        show adrian sad
        a "Sorry, wrong answer."
        jump ch1_med1

    
    label ch1_med1:# Fill in the Blank 1
    a "9. A ____ is a linear data structure where elements are added and removed from only one end."
    $ answer = renpy.input("Fill in the blank").strip()
    if answer.lower() == "stack":
        show adrian happy
        a "Correct! Stack is the right answer."
        $ chapter_1_score += 1
        jump ch1_med2

    else:
        show adrian sad
        a "Sorry, the correct answer is 'stack'."
        jump ch1_med2

    label ch1_med2:# Fill in the Blank 2
    a "10. The process of arranging data in a particular order is called ____."
    $ answer = renpy.input("Fill in the blank").strip()
    if answer.lower() == "sorting":
        show adrian happy
        a "Correct! Sorting is the process."
        $ chapter_1_score += 1
        jump ch1_med3
    else:
        show adrian sad
        a "Sorry, the correct answer is 'sorting'."
        jump ch1_med3

    label ch1_med3:
    # Fill in the Blank 3
    a "11. In a ____ search, the dataset must be sorted before searching."
    $ answer = renpy.input("Fill in the blank").strip()
    if answer.lower() == "binary":
        show adrian happy
        a "Correct! Binary search requires a sorted dataset."
        $ chapter_1_score += 1
        jump ch1_med4
    else:
        show adrian sad
        a "Sorry, the correct answer is 'binary'."
        jump ch1_med4

    label ch1_med4:
    # Multiple Choice 1
    a "12. Which data structure uses nodes that point to the next node in the sequence?"
    menu:
        "Linked List":
            show adrian happy
            a "Correct! Linked lists use nodes that point to the next node."
            $ chapter_1_score += 1
        "Array":
            show adrian sad
            a "Incorrect. Arrays do not use nodes."
        "Stack":
            show adrian sad
            a "Incorrect. Stacks do not use nodes."
        "Queue":
            show adrian sad
            a "Incorrect. Queues do not use nodes."

    # Multiple Choice 2
    a "13. Which of the following is NOT a linear data structure?"
    menu:
        "Tree":
            show adrian happy
            a "Correct! Trees are non-linear data structures."
            $ chapter_1_score += 1
        "Queue":
            show adrian sad
            a "Incorrect. Queue is linear."
        "Stack":
            show adrian sad
            a "Incorrect. Stack is linear."
        "Array":
            show adrian sad
            a "Incorrect. Array is linear."

    # Multiple Choice 3
    a "14. Which operation is used to remove an element from the end of a stack?"
    menu:
        "Pop":
            show adrian happy
            a "Correct! Pop removes the top element from a stack."
            $ chapter_1_score += 1
        "Push":
            show adrian sad
            a "Incorrect. Push adds an element."
        "Enqueue":
            show adrian sad
            a "Incorrect. Enqueue is for queues."
        "Dequeue":
            show adrian sad
            a "Incorrect. Dequeue is for queues."

    # Multiple Choice 4
    a "15. Which of the following best describes a queue?"
    menu:
        "First In, First Out":
            show adrian happy
            a "Correct! Queue is FIFO."
            $ chapter_1_score += 1
        "Last In, First Out":
            show adrian sad
            a "Incorrect. That's a stack."
        "Random Access":
            show adrian sad
            a "Incorrect. That's an array."
        "Hierarchical":
            show adrian sad
            a "Incorrect. That's a tree."

    show adrian smiling
    a "Great job! You finished the Moderate Quiz. Your total score is [chapter_1_score]."
    jump chapter_1_ending


label chapter_1_quiz_easy:
    $ chapter_1_score = 0
    show adrian smiling at center
    a "Welcome to the Easy Quiz! Let's see how much you've learned."

    # Question 1
    a "1. Which of the following is a data structure?"
    menu:
        "Array":
            show adrian happy
            a "Correct! An array is a data structure."
            $ chapter_1_score += 1
        "Button":
            show adrian sad
            a "Incorrect. A button is not a data structure."
        "Window":
            show adrian sad
            a "Incorrect. A window is not a data structure."
        "Image":
            show adrian sad
            a "Incorrect. An image is not a data structure."

    # Question 2
    a "2. True or False: A stack follows the Last In, First Out (LIFO) principle."
    menu:
        "True":
            show adrian happy
            a "Correct! Stack is LIFO."
            $ chapter_1_score += 1
        "False":
            show adrian sad
            a "Incorrect. Stack is LIFO."

    # Question 3
    a "3. Which data structure works like a line at a ticket counter?"
    menu:
        "Queue":
            show adrian happy
            a "Correct! A queue works like a line."
            $ chapter_1_score += 1
        "Stack":
            show adrian sad
            a "Incorrect. A stack is not like a line."
        "Array":
            show adrian sad
            a "Incorrect. An array is not like a line."
        "Graph":
            show adrian sad
            a "Incorrect. A graph is not like a line."

    # Question 4
    a "4. True or False: Algorithms are only used in computer programming."
    menu:
        "False":
            show adrian happy
            a "Correct! Algorithms can be used in daily life too."
            $ chapter_1_score += 1
        "True":
            show adrian sad
            a "Incorrect. Algorithms are everywhere!"

    # Question 5
    a "5. Which of these is NOT a characteristic of a good algorithm?"
    menu:
        "Ambiguity":
            show adrian happy
            a "Correct! Algorithms should not be ambiguous."
            $ chapter_1_score += 1
        "Finiteness":
            show adrian sad
            a "Incorrect. Finiteness is a good characteristic."
        "Effectiveness":
            show adrian sad
            a "Incorrect. Effectiveness is a good characteristic."
        "Input":
            show adrian sad
            a "Incorrect. Input is a good characteristic."

    # Question 6
    a "6. True or False: A queue is First In, First Out (FIFO)."
    menu:
        "True":
            show adrian happy
            a "Correct! Queue is FIFO."
            $ chapter_1_score += 1
        "False":
            show adrian sad
            a "Incorrect. Queue is FIFO."

    # Question 7
    a "7. Which of the following is used to find data quickly?"
    menu:
        "Search Algorithm":
            show adrian happy
            a "Correct! Search algorithms help find data."
            $ chapter_1_score += 1
        "Sorting Algorithm":
            show adrian sad
            a "Incorrect. Sorting arranges data."
        "Insertion Algorithm":
            show adrian sad
            a "Incorrect. Insertion adds data."
        "Deletion Algorithm":
            show adrian sad
            a "Incorrect. Deletion removes data."

    # Question 8
    a "8. True or False: A linked list can grow and shrink in size easily."
    menu:
        "True":
            show adrian happy
            a "Correct! Linked lists are dynamic."
            $ chapter_1_score += 1
        "False":
            show adrian sad
            a "Incorrect. Linked lists are flexible."

    # Question 9
    a "9. Which of these is an example of a sorting algorithm?"
    menu:
        "Bubble Sort":
            show adrian happy
            a "Correct! Bubble Sort is a sorting algorithm."
            $ chapter_1_score += 1
        "Binary Search":
            show adrian sad
            a "Incorrect. Binary Search is a search algorithm."
        "Queue":
            show adrian sad
            a "Incorrect. Queue is a data structure."
        "Stack":
            show adrian sad
            a "Incorrect. Stack is a data structure."

    # Question 10
    a "10. True or False: Data structures help organize and store data efficiently."
    menu:
        "True":
            show adrian happy
            a "Correct! That's the main purpose of data structures."
            $ chapter_1_score += 1
        "False":
            show adrian sad
            a "Incorrect. Data structures do help organize data."

    show adrian smiling
    a "Great job! You finished the Easy Quiz. Your total score is [chapter_1_score]."

    
    jump chapter_1_ending
label chapter_1_ending:
    a "Your Score is [chapter_1_score]!"
    a "Would You like to test again?"
    menu:
        "Yes":
            jump chapter_1_restart
        "No":
            pass
    show adrian happy
    a "You have finished chapter 1. You can continue to Chapter 2!"
    jump menu
    
    
    $ persistent.chapter_1 = True