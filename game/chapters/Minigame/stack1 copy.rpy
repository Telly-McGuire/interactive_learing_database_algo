init python:
    store.stack_items1     = []
    store.correct_pattern1 = ["21", "19", "12"]
    store.stack_status1    = "Waiting..."

    def handle_stack_drag1(drags, drop):
        if not drop or not drags or len(drags) != 1:
            return True

        drag = drags[0]

        if not drop.droppable or not drag.draggable:
            return True

        if drag == drop:
            return True

        if drag.drag_name is None or drop.drag_name is None:
            return True

        if drop.drag_name not in ["stack_zone1", "pop_zone1"]:
            return False

        if drop.drag_name == "stack_zone1":
            push_to_stack1([drag], drop)
            return True

        if drop.drag_name == "pop_zone1":
            pop_from_stack1([drag], drop)
            return True

        return True

    def push_to_stack1(drags, drop):
        if not drop or drop.drag_name != "stack_zone1":
            return False

        idx      = len(store.stack_items1)
        expected = store.correct_pattern1[idx] if idx < len(store.correct_pattern1) else None
        item     = drags[0].drag_name

        if item == expected:
            store.stack_items1.append(item)
            _update_stack_status1()
            return True
        else:
            store.stack_status1 = "❌ Incorrect"
            return False

    def pop_from_stack1(drags, drop):
        if not drop or drop.drag_name != "pop_zone1" or not store.stack_items1:
            return False

        item = drags[0].drag_name
        if store.stack_items1[-1] == item:
            store.stack_items1.pop()
            _update_stack_status1()
            return True
        else:
            store.stack_status1 = "❌ Incorrect"
            return False

    def _update_stack_status1():
        if store.stack_items1 == store.correct_pattern1:
            store.stack_status1 = "✅ Correct!"
        elif store.correct_pattern1[:len(store.stack_items1)] == store.stack_items1:
            store.stack_status1 = "⏳ Incomplete"
        else:
            store.stack_status1 = "❌ Incorrect"

    def reset_stack1():
        store.stack_items1.clear()
        store.stack_status1 = "Waiting..."

screen stack_demo():
    add "bg_blank"
    modal True
    tag stack_demo

    #── Info Panel ────────────────────────────────────────────────────
    vbox:
        spacing 20
        xalign 0.06 yalign 0.09

        frame:
            xsize 350 ysize 150
            xpadding 40 ypadding 40
            text "Status: [store.stack_status1]" color "#fff"

        frame:
            xsize 350 ysize 80
            xpadding 15 ypadding 15
            text "Pattern: [', '.join(store.correct_pattern1)]" color "#fff"

        hbox:
            spacing 30

            textbutton "Reset":
                background "#444"
                action Function(reset_stack1)
                
            textbutton "Done":
                xalign 0.5 yalign 0.95
                action [Hide("stack_demo"), Jump("after_stack_demo")]



    #── Drag & Drop Area ───────────────────────────────────────────────
    draggroup:

        # Push Zone (left)
        drag:
            xpos 0.05 ypos 0.4
            draggable False
            droppable True
            drag_name "stack_zone1"
            frame:
                xsize 500 ysize 300
                xpadding 20 ypadding 10

                # show current stack
                vbox:
                    spacing 5
                    text "Push Zone" color "#fff"
                    text "Drag here in order:" color "#ddd"
                    for item in reversed(store.stack_items1):
                        text item color "#fff"

        # Draggable “21”
        drag:
            xpos 0.4 ypos 0.2
            drag_name "21"
            draggable True
            dragged handle_stack_drag1
            frame:
                xsize 200 ysize 150
                xpadding 10 ypadding 10
                text "{size=+20}21":
                    xalign 0.5
                    yalign 0.5

        # Draggable “19”
        drag:
            xpos 0.4 ypos 0.45
            drag_name "19"
            draggable True
            dragged handle_stack_drag1
            frame:
                xsize 200 ysize 150
                xpadding 10 ypadding 10
                text "{size=+20}19":
                    xalign 0.5
                    yalign 0.5

        # Draggable “12”
        drag:
            xpos 0.7 ypos 0.5
            drag_name "12"
            draggable True
            dragged handle_stack_drag1
            frame:
                xsize 200 ysize 150
                xpadding 10 ypadding 10
                text "{size=+20}12":
                    xalign 0.5
                    yalign 0.5


        # Pop Zone (right)
        drag:
            xpos 0.85 ypos 0.05
            draggable False
            droppable True
            drag_name "pop_zone1"
            frame:
                xsize 250 ysize 200
                xpadding 30 ypadding 30

                vbox:
                    spacing 5
                    text "Pop() Zone" color "#fff"
                    if store.stack_items1:
                        text "Top: [store.stack_items1[-1]]" color "#fff"

label stack_minigame:

    a "Form the stack 21 → 19 → 12 by pushing, and pop from the right."
    
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0

    window hide
    show screen stack_demo
    window hide
    a "Now, let's switch gears and explore how stacks work."
    a "A stack processes items in reverse order — last in, first out."
    a "Imagine a stack of plates; the last one placed on top is the first one you take off."
    a "When you push an item, it goes to the top of the stack."
    a "When you pop, you remove the item from the top."
    a "Stacks are perfect for tasks that need to be undone or reversed."
    a "Think of the undo feature in a drawing app — the last action is undone first."
    a "In games, stacks can manage layered effects or nested decisions."
    a "We'll practice adding and removing items from a stack next."
    a "By the end, you'll see how stacks help manage control flow and memory cleanly."

    a "Stacks are also used in programming languages to manage function calls."
    a "When a function is called, it's pushed onto the call stack."
    a "Once the function finishes, it's popped off, returning control to the previous one."
    a "This is how recursion works — stacking calls until a base case is reached."
    a "Ever seen a 'stack overflow' error? That happens when too many calls are pushed without popping."
    a "Stacks are memory-efficient when used correctly, but they can crash your program if mismanaged."
    a "They're also handy for parsing expressions, like converting infix to postfix notation."
    a "In compilers, stacks help track nested scopes and variable lifetimes."
    a "Even your browser uses a stack to manage navigation — back and forward buttons rely on it."
    a "Undo-redo systems, like in Photoshop or VS Code, are classic stack use cases."
    a "Stacks are simple, but powerful — they enforce discipline in how data is accessed."
    a "You can only interact with the top item, which keeps things predictable."
    a "This constraint is what makes stacks ideal for managing temporary states."
    a "In games, stacks can control turn order, spell layering, or even dialogue branching."
    a "Imagine a card game where effects resolve in reverse — that's stack logic in action."
    a "Stacks also appear in AI decision trees, especially when backtracking is needed."
    a "They're used in depth-first search algorithms to explore paths deeply before retreating."
    a "Stacks can even model emotional states — the last feeling triggered is the first to be resolved."
    a "In storytelling, stacks help manage nested flashbacks or layered plot reveals."
    a "So whether you're coding, designing, or narrating, stacks offer a clean way to manage complexity."


label after_stack_demo:
    $ persistent.stack_completed = True
    window show
    show adrian smiling
    hide screen stack_demo
    play sound "sfx/success.mp3"
    play music "bgm/city-high-life.mp3" fadein 1.0
    a "Great job! You've completed the stack exercise."
    show adrian normal
    a "Let's continue our adventure."
    return
