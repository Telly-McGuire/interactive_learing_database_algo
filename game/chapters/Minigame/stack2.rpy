init python:
    store.stack_items     = []
    store.correct_pattern = ["18", "30", "3", "17", "45"]
    store.stack_status    = "Waiting..."

    def handle_stack_drag(drags, drop):
        if not drop or not drags or len(drags) != 1:
            return True  # Prevent screen exit

        drag = drags[0]

        if not drop.droppable or not drag.draggable:
            return True  # Prevent screen exit

        if drag == drop:
            return True  # Prevent screen exit

        if drag.drag_name is None or drop.drag_name is None:
            return True  # Prevent screen exit

        # Ignore non-stack zones
        if drop.drag_name not in ["stack_zone", "pop_zone"]:
            return fals

        # Pushing
        if drop.drag_name == "stack_zone":
            push_to_stack([drag], drop)
            return True

        # Popping
        if drop.drag_name == "pop_zone":
            pop_from_stack([drag], drop)
            return True

        return True  # Fallback to prevent screen exit  # Fallback to prevent screen exit


    def push_to_stack(drags, drop):
        if not drop or drop.drag_name != "stack_zone":
            return False

        idx      = len(store.stack_items)
        expected = store.correct_pattern[idx] if idx < len(store.correct_pattern) else None
        item     = drags[0].drag_name

        if item == expected:
            store.stack_items.append(item)
            _update_stack_status()
            return True
        else:
            store.stack_status = "❌ Incorrect"
            return False

    def pop_from_stack(drags, drop):
        if not drop or drop.drag_name != "pop_zone" or not store.stack_items:
            return False

        item = drags[0].drag_name
        if store.stack_items[-1] == item:
            store.stack_items.pop()
            _update_stack_status()
            return True
        else:
            store.stack_status = "❌ Incorrect"
            return False

    def _update_stack_status():
        if store.stack_items == store.correct_pattern:
            store.stack_status = "✅ Correct!"
        elif store.correct_pattern[:len(store.stack_items)] == store.stack_items:
            store.stack_status = "⏳ Incomplete"
        else:
            store.stack_status = "❌ Incorrect"

    def reset_stack():
        store.stack_items.clear()
        store.stack_status = "Waiting..."

screen stack_demo2():
    add "bg_blank"
    modal True
    tag stack_demo

    #── Info Panel ────────────────────────────────────────────────────
    vbox:
        spacing 20
        xalign 0.06 yalign 0.09

        frame:
            xsize 500 ysize 150
            xpadding 40 ypadding 40
            text "Status: [store.stack_status]" color "#fff"

        frame:
            xsize 500 ysize 80
            xpadding 15 ypadding 15
            text "Pattern: [', '.join(store.correct_pattern)]" color "#fff"

        hbox:
            spacing 30

            textbutton "Reset":
                background "#444"
                action Function(reset_stack)
                
            textbutton "Done":
                xalign 0.5 yalign 0.95
                action [Hide("stack_demo2"), Jump("after_stack_demo2")]



    #── Drag & Drop Area ───────────────────────────────────────────────
    draggroup:

        # Push Zone (left)
        drag:
            xpos 0.05 ypos 0.4
            draggable False
            droppable True
            drag_name "stack_zone"
            frame:
                xsize 500 ysize 300
                xpadding 20 ypadding 10

                # show current stack
                vbox:
                    spacing 5
                    text "Push Zone" color "#fff"
                    text "Drag here in order:" color "#ddd"
                    for item in reversed(store.stack_items):
                        text item color "#fff"

        drag:
            xpos 0.57 ypos 0.2
            drag_name "18"
            draggable True
            dragged handle_stack_drag
            frame:
                xsize 200 ysize 150
                xpadding 10 ypadding 10
                text "{size=+20}18":
                    xalign 0.5
                    yalign 0.5

        drag:
            xpos 0.4 ypos 0.45
            drag_name "30"
            draggable True
            dragged handle_stack_drag
            frame:
                xsize 200 ysize 150
                xpadding 10 ypadding 10
                text "{size=+20}30":
                    xalign 0.5
                    yalign 0.5

        drag:
            xpos 0.8 ypos 0.4
            drag_name "3"
            draggable True
            dragged handle_stack_drag
            frame:
                xsize 200 ysize 150
                xpadding 10 ypadding 10
                text "{size=+20}3":
                    xalign 0.5
                    yalign 0.5

        drag:
            xpos 0.4 ypos 0.2
            drag_name "7"
            draggable True
            dragged handle_stack_drag
            frame:
                xsize 200 ysize 150
                xpadding 10 ypadding 10
                text "{size=+20}7":
                    xalign 0.5
                    yalign 0.5

        drag:
            xpos 0.7 ypos 0.2
            drag_name "17"
            draggable True
            dragged handle_stack_drag
            frame:
                xsize 200 ysize 150
                xpadding 10 ypadding 10
                text "{size=+20}17":
                    xalign 0.5
                    yalign 0.5


        drag:
            xpos 0.65 ypos 0.4
            drag_name "45"
            draggable True
            dragged handle_stack_drag
            frame:
                xsize 200 ysize 150
                xpadding 10 ypadding 10
                text "{size=+20}45":
                    xalign 0.5
                    yalign 0.5

        # Pop Zone (right)
        drag:
            xpos 0.85 ypos 0.05
            draggable False
            droppable True
            drag_name "pop_zone"
            frame:
                xsize 250 ysize 200
                xpadding 30 ypadding 30

                vbox:
                    spacing 5
                    text "Pop() Zone" color "#fff"
                    if store.stack_items:
                        text "Top: [store.stack_items[-1]]" color "#fff"

label stack_minigame2:
    window hide
    show screen stack_demo2
    a "Form the stack 18 → 30 → 3 → 17 → 45  by pushing, and pop from the right."
    
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0

    
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


label after_stack_demo2:
    window show
    show adrian smiling
    play sound "sfx/success.mp3"
    play music "bgm/city-high-life.mp3" fadein 1.0
    a "Great job! You've completed the stack exercise."
    show adrian normal
    jump menu
