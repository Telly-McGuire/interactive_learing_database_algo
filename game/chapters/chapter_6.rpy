
# Chapter 6: AVL TREES
# Properties of AVL Trees
# operations on AVL Trees
# Balanced Trees
# Rotation I, II, III, IV
# Operations
# Application

label chapter_6_intro:


label chapter_6_AVL_Properties:
label chapter_6_AVL_Properties_Quiz:
    #5POINTS
    $ chapter_6_AVL_Properties_quiz = 0


label chapter_6_AVL_Operations:
label chapter_6_AVL_Operations_Quiz:
    #5POINTS
    $ chapter_6_AVL_Operations_quiz = 0


label chapter_6_Balanced_Trees:
label chapter_6_Balanced_Trees_Quiz:
    #5POINTS
    $ chapter_6_Balanced_Trees_quiz = 0


label chapter_6_Rotations:
    # Rotation I, II, III, IV
label chapter_6_Rotations_Quiz:
    #5POINTS
    $ chapter_6_Rotations_quiz = 0


label chapter_6_Applications:
label chapter_6_Applications_Quiz:
    #5POINTS
    $ chapter_6_Applications_quiz = 0

label chapter_6_restart:
    $ chapter_6_test = (
        chapter_6_AVL_Properties_quiz +
        chapter_6_AVL_Operations_quiz +
        chapter_6_Balanced_Trees_quiz +
        chapter_6_Rotations_quiz +
        chapter_6_Applications_quiz
    )

    a "Your score is [chapter_6_test]"
    a "Let's see how well you do in the {size=+20}CHAPTER QUIZ"

    if chapter_5_test <= 8:
        show adrian concerned
        jump chapter_6_quiz_easy
    elif chapter_5_test <= 14:
        show adrian smiling
        jump chapter_6_quiz_medium
    else:
        show adrian confident
        jump chapter_6_quiz_hard


label chapter_6_quiz_easy:
label chapter_6_quiz_medium:
label chapter_6_quiz_hard:

label chapter_6_quiz_end:
    a "Your total score is [chapter_6_test] out of 25"
    jump chapter_6_performance

label chapter_6_performance:

# Properties
    if chapter_6_AVL_Properties_quiz < 2:
        a "You need to review the Properties of AVL Trees section."
        a "Focus on height balance and node structure."
    elif chapter_6_AVL_Properties_quiz < 3:
        a "You did okay in Properties, but there's room for improvement."
        a "Revisiting balance factor logic could help."

# Operations
    if chapter_6_AVL_Operations_quiz < 2:
        a "You need to review AVL Tree Operations."
        a "Pay attention to insertions and deletions with rebalancing."
    elif chapter_6_AVL_Operations_quiz < 3:
        a "You did okay in Operations, but there's room for improvement."
        a "Try tracing how rotations are triggered during insert/delete."

# Balanced Trees
    if chapter_6_Balanced_Trees_quiz < 2:
        a "You need to review Balanced Trees."
        a "Understand why balance matters for performance."
    elif chapter_6_Balanced_Trees_quiz < 3:
        a "You did okay in Balanced Trees, but there's room for improvement."
        a "Compare AVL with other balanced trees like Red-Black."

# Rotations
    if chapter_6_Rotations_quiz < 2:
        a "You need to review Rotations."
        a "Focus on LL, RR, LR, and RL cases."
    elif chapter_6_Rotations_quiz < 3:
        a "You did okay in Rotations, but there's room for improvement."
        a "Practice visualizing rotation steps."

# Applications
    if chapter_6_Applications_quiz < 2:
        a "You need to review Applications of AVL Trees."
        a "Think about real-world use cases like databases and indexing."
    elif chapter_6_Applications_quiz < 3:
        a "You did okay in Applications, but there's room for improvement."
        a "Explore how AVL Trees compare with other data structures in practice."

    jump chapter_6_end

label chapter_6_end:
