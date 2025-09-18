# Chapter 7: Binary Search Trees (Red-Black Trees)
# Topics:
# - The logic of Red-Black Trees
# - Operations
# - Re-coloring and Rotation cases

label chapter_7_intro:

label chapter_7_RB_Logic:
label chapter_7_RB_Logic_Quiz:
    #5POINTS
    $ chapter_7_RB_Logic_quiz = 0

label chapter_7_RB_Operations:
label chapter_7_RB_Operations_Quiz:
    #5POINTS
    $ chapter_7_RB_Operations_quiz = 0

label chapter_7_Recoloring_Rotation:
label chapter_7_Recoloring_Rotation_Quiz:
    #5POINTS
    $ chapter_7_Recoloring_Rotation_quiz = 0

label chapter_7_restart:
    $ chapter_7_test = (
        chapter_7_RB_Logic_quiz +
        chapter_7_RB_Operations_quiz +
        chapter_7_Recoloring_Rotation_quiz
    )

    a "Your score is [chapter_7_test]"
    a "Let's see how well you do in the {size=+20}CHAPTER QUIZ"

    if chapter_6_test <= 10:
        show adrian worried
        jump chapter_7_quiz_easy
    elif chapter_6_test <= 18:
        show adrian neutral
        jump chapter_7_quiz_medium
    else:
        show adrian proud
        jump chapter_7_quiz_hard

label chapter_7_quiz_easy:
label chapter_7_quiz_medium:
label chapter_7_quiz_hard:

label chapter_7_quiz_end:
    a "Your total score is [chapter_7_test] out of 15"
    jump chapter_7_performance

label chapter_7_performance:

# Red-Black Logic
    if chapter_7_RB_Logic_quiz < 2:
        a "You need to review the logic behind Red-Black Trees."
        a "Focus on the properties that maintain balance and prevent degeneration."
    elif chapter_7_RB_Logic_quiz < 3:
        a "You did okay in Red-Black Tree logic, but there's room for improvement."
        a "Revisit how the tree maintains height and structure."

# Operations
    if chapter_7_RB_Operations_quiz < 2:
        a "You need to review Red-Black Tree operations."
        a "Pay attention to how insertions and deletions trigger fixes."
    elif chapter_7_RB_Operations_quiz < 3:
        a "You did okay in Operations, but there's room for improvement."
        a "Try tracing how violations are resolved during updates."

# Recoloring & Rotation
    if chapter_7_Recoloring_Rotation_quiz < 2:
        a "You need to review Re-coloring and Rotation cases."
        a "Understand how LL, RR, LR, and RL cases are handled."
    elif chapter_7_Recoloring_Rotation_quiz < 3:
        a "You did okay in Re-coloring and Rotation, but there's room for improvement."
        a "Practice visualizing how color changes and rotations restore balance."

    jump chapter_7_end

label chapter_7_end: