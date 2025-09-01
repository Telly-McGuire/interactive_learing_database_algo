init python:
    store.stack_items     = []
    store.correct_pattern = ["21", "19", "12"]
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
            text "Status: [store.stack_status]" color "#fff"

        frame:
            xsize 350 ysize 80
            xpadding 15 ypadding 15
            text "Pattern: [', '.join(store.correct_pattern)]" color "#fff"

        hbox:
            spacing 30

            textbutton "Reset":
                background "#444"
                action Function(reset_stack)
                
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

        # Draggable “21”
        drag:
            xpos 0.4 ypos 0.2
            drag_name "21"
            draggable True
            dragged handle_stack_drag
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
            dragged handle_stack_drag
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
            dragged handle_stack_drag
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
            drag_name "pop_zone"
            frame:
                xsize 250 ysize 200
                xpadding 30 ypadding 30

                vbox:
                    spacing 5
                    text "Pop() Zone" color "#fff"
                    if store.stack_items:
                        text "Top: [store.stack_items[-1]]" color "#fff"

label stack_minigame:

    a "Form the stack 21 → 19 → 12 by pushing, and pop from the right."
    
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0

    window hide
    show screen stack_demo
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

    
label after_stack_demo:
    $ persistent.stack_completed = True
    window show
    show adrian smiling
    play sound "sfx/success.mp3"
    play music "bgm/city-high-life.mp3" fadein 1.0
    a "Great job! You've completed the stack exercise."
    show adrian normal
    a "Let's continue our adventure."
    return
