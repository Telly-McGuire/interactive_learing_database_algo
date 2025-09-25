# Chapter 5: Binary Trees
#Binary Search trees

default chapter_5_progress = 0
label chapter_5_intro:

label chacter_5_Binary_Trees:
label chapter_5_Binary_Tree_quiz:
    #5POINTS
    $ chapter_5_Binary_Tree_quiz = 0
label chapter_5_Binary_Search_Trees:
label chapter_5_Binary_Search_Tree_Quiz:
    #5POINTS
    $ chapter_5_Binary_Search_Tree_quiz = 0
label chapter_5_Functions:
    #insert
    #find
    #delete

label chapter_5_Functions_Quiz:
    #5POINTS
    $ chapter_5_Functions_quiz = 0

label chapter_5_Traversal:
    #inorder
    #preorder
    #postorder
label chapter_5_Traversal_Quiz:
    #5POINTS
    $ chapter_5_Traversal_quiz = 0

label chapter_5_restart:
    #quiz 20 points
    a "Your score is [chapter_5_test]"
    a "Lets see how well you do in the {size=+20}CHAPTER QUIZ"
    if chapter_4_test <= 8:
        show adrian blush
        jump chapter_5_quiz_easy
    elif chapter_4_test <= 14:
        show adrian smiling
        jump chapter_5_quiz_medium
    else:
        show adrian happy
        jump chapter_5_quiz_hard

label chapter_5_quiz_easy:
label chapter_5_quiz_medium:
label chapter_5_quiz_hard:

label chapter_5_quiz_end:
    a "Your total score is [chapter_5_test] out of 20"
    jump chapter_5_performance
label chapter_5_performance:
    # $ chapter_5_Binary_Tree_quiz = 0
    # $ chapter_5_Binary_Search_Tree_quiz = 0
    # $ chapter_5_Functions_quiz = 0
    # $ chapter_5_Traversal_quiz = 0

# Binary Tree
    if chapter_5_Binary_Tree_quiz < 2:
        a "You need to review the Binary Trees section."
        a "Consider revisiting the material to improve your understanding."
    elif chapter_5_Binary_Tree_quiz < 3:
        a "You did okay in the Binary Trees section, but there's room for improvement."
        a "Reviewing the material could help solidify your knowledge."

# Binary Search Tree
    if chapter_5_Binary_Search_Tree_quiz < 2:
        a "You need to review the Binary Search Trees section."
        a "Focus on how insertion, deletion, and search operations work."
    elif chapter_5_Binary_Search_Tree_quiz < 3:
        a "You did okay in the Binary Search Trees section, but there's room for improvement."
        a "Revisiting traversal and edge cases could help reinforce your understanding."

# Functions
    if chapter_5_Functions_quiz < 2:
        a "You need to review the Functions section."
        a "Make sure you understand how parameters, return values, and scope work."
    elif chapter_5_Functions_quiz < 3:
        a "You did okay in the Functions section, but there's room for improvement."
        a "Reviewing recursion and modular design could strengthen your grasp."

# Traversal
    if chapter_5_Traversal_quiz < 2:
        a "You need to review the Traversal section."
        a "Focus on understanding preorder, inorder, and postorder traversal methods."
    elif chapter_5_Traversal_quiz < 3:
        a "You did okay in the Traversal section, but there's room for improvement."
        a "Practicing traversal on different tree structures could help clarify the logic."
    jump chapter_5_end  

label chapter_5_end: