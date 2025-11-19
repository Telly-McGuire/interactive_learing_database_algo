# Chapter 9: Associative Arrays (Dictionaries)
# Topics:
# - Associative arrays
# - Hash table introduction – collisions
# - Hash table introduction – dynamic resizing

default chapter_9_progress = 0

default chapter_9_Associative_Arrays_quiz = 0
default chapter_9_Collisions_quiz = 0
default chapter_9_Dynamic_Resizing_quiz = 0

screen chapter_9_AAIntro:  # Associative Arrays Intro
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 200
        ypadding 60
        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5
            text "Associative Arrays" size 60 color "#FFFFFF" outlines [(5, "#000000", 0, 0)]

label chapter_9_intro:

    call hideall from _call_hideall_10
    play sound "sfx/start.mp3"
    stop music fadeout 1.0

    scene black
    pause 1.0

    show screen chapter_9_AAIntro
    scene room with dissolve
    pause 2.0
    hide screen chapter_9_AAIntro

    show screen menu_btn

    play music "bgm/city-high-life.mp3" fadein 1.0
    show adrian smiling at center:
        smaller
    with dissolve


    if persistent.chapter_9 == True:
        a "Welcome back to Chapter 9"
        a "Are you sure you want to go through this chapter again?"
        menu:
            "Yes":
                a "Pick a topic to review!"
                menu:
                    "Associative Arrays":
                        jump chapter_9_Associative_Arrays
                    "Collisions":
                        jump chapter_9_Collisions
                    "Dynamic Resizing":
                        jump chapter_9_Dynamic_Resizing
            "No":
                jump menu
    else:
        pass 


    show adrian normal
    a "Do you have a partner?"

    menu:
        "Yes":
            a "Aww, that's great!"
        "No":
            show adrian nocomment
            a "Oh..."
            a "Thats kinda sad."
            a "Lmao it's okay though, I'm here with you!"

    show adrian normal
    a "I'm asking you that cuz were talking about partnering"
    a "Connecting things to another"
    a "Like how Associative Arrays connect keys to values!"

    show shrimple onlayer overlay:
        zoom 0.2
        xpos 0.4
        ypos 0.8
    show adrian smiling
    a "As shrimple as that" 

    show adrian smiling
    a "Welcome to Chapter 9: Associative Arrays"

screen chapter_9_dict_display():
    frame:
        xalign 0.5
        yalign 0.6
        xpadding 50
        ypadding 50
        vbox:
            spacing 8
            text "Associative Array — Live Demo" size 32 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
            text "Current entries:" size 20 color "#FFFFFF" outlines [(1, "#000000", 0, 0)]
            # Show the dictionary as a compact, readable list.
            text "[', '.join([f'{k}: {v}' for k, v in demo_dict.items()])]" size 20 color "#FFFFCC" outlines [(1, "#000000", 0, 0)]
            hbox:
                spacing 12
                frame:
                    textbutton "Add entry" action Return("add")
                frame:
                    textbutton "Lookup" action Return("lookup")
                frame:
                    textbutton "Close" action Return("close")

init python:
    try:
        demo_dict
    except NameError:
        demo_dict = {"alice": "Phone: 555-0123", "bob": "Phone: 555-0456"}

label chapter_9_Associative_Arrays:

    a "Let’s explore a powerful data structure: {b}Associative Arrays{/b}, also known as {b}dictionaries{/b}."
    a "Unlike regular arrays that use numeric indices, associative arrays store data as {b}key-value pairs{/b}."

    a "Think of it like a phonebook: you look up a name (the {i}key{/i}) to get the phone number (the {i}value{/i})."
    a "Keys must be {i}unique{/i} — two people can't occupy the same exact phonebook entry."

    a "They're everywhere: configuration maps, caches, game state, and more."

    show screen chapter_9_dict_display

    # Interactive loop: let the player add or lookup entries to see how keys map to values.
    $ _continue_demo = True
    while _continue_demo:
        # Show the demo screen and wait for a button result.
        $ result = ui.interact()  # allow screen to return a value via Return()

        if result == "add":
            $ name = renpy.input("Enter the key (e.g. a name):").strip()
            if name == "":
                a "No key entered — cancelled."
            else:
                $ value = renpy.input("Enter the value for [name]:").strip()
                if value == "":
                    a "No value entered — cancelled."
                else:
                    $ demo_dict[name] = value
                    play sound "sfx/confirm.mp3"
                    a "Added [name] : [value] to the associative array."
                    # Refresh the screen by re-showing it (ui.interact will re-render)
        elif result == "lookup":
            $ key = renpy.input("Lookup which key?").strip()
            if key == "":
                a "No key entered — cancelled."
            else:
                $ found = demo_dict.get(key, None)
                if found is None:
                    play sound "sfx/error.mp3"
                    a "No entry for '[key]' was found."
                else:
                    play sound "sfx/confirm.mp3"
                    a "Found: [key] -> [found]"
        else:
            # close or any other
            $ _continue_demo = False

    hide screen chapter_9_dict_display

    a "You just experimented with inserting and looking up key-value pairs."
    a "Behind the scenes, many associative arrays use {b}hash tables{/b} to convert keys into indices for fast access."
    a "Pretty Cool right?"


    $ chapter_9_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Let's check your understanding with a quick quiz!"
    jump chapter_9_Associative_Arrays_Quiz

init python:
    import random
    chapter_9_Associative_Arrays_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_9_Associative_Arrays_order)

label chapter_9_Associative_Arrays_Quiz:
    #5POINTS
    $ chapter_9_Associative_Arrays_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_9_Associative_Arrays_order:
        $ current_q = chapter_9_Associative_Arrays_order.pop(0)

        if current_q == "q1":
            a "What is an associative array also known as?"
            menu:
                "Dictionary":
                    $ chapter_9_Associative_Arrays_quiz += 1
                    a "Correct! Associative arrays are often called dictionaries in many languages."
                "List":
                    a "Incorrect! Lists use numeric indices, not keys."
                "Stack":
                    a "Incorrect! Stacks follow LIFO order, not key-value mapping."

        elif current_q == "q2":
            a "What does an associative array store?"
            menu:
                "Key-value pairs":
                    $ chapter_9_Associative_Arrays_quiz += 1
                    a "Correct! Each value is accessed using a unique key."
                "Only values":
                    a "Incorrect! Keys are essential for access."
                "Only keys":
                    a "Incorrect! Keys must be paired with values."

        elif current_q == "q3":
            a "Which operation is fastest in a well-implemented associative array?"
            menu:
                "Lookup by key":
                    $ chapter_9_Associative_Arrays_quiz += 1
                    a "Correct! Hashing allows fast access to values using keys."
                "Sorting values":
                    a "Incorrect! Sorting isn’t the primary use."
                "Iterating over values":
                    a "Incorrect! Lookup is typically faster than iteration."

        elif current_q == "q4":
            a "Which data structure is commonly used to implement associative arrays?"
            menu:
                "Hash table":
                    $ chapter_9_Associative_Arrays_quiz += 1
                    a "Correct! Hash tables provide efficient key-based access."
                "Queue":
                    a "Incorrect! Queues don’t support key-value access."
                "Tree":
                    a "Incorrect! Trees can be used, but hash tables are more common."

        elif current_q == "q5":
            a "What happens if two keys hash to the same index?"
            menu:
                "A collision occurs":
                    $ chapter_9_Associative_Arrays_quiz += 1
                    a "Correct! Collisions must be handled to maintain access efficiency."
                "The second key is ignored":
                    a "Incorrect! That would lose data."
                "The array resizes automatically":
                    a "Incorrect! Resizing may happen, but not immediately due to collisions."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_9_Associative_Arrays_quiz] out of 5."
    jump chapter_9_Collisions
init python:
    # Interactive collisions demo globals and helpers defined at init/top-level so the screen can access them.
    try:
        collision_table_size
    except NameError:
        collision_table_size = 8
        collision_method = "chaining"  # or "open"
        # Initialize a chaining table (list of lists). Open-addressing uses list of None.
        collision_table = [[] for _ in range(collision_table_size)]

    def simple_hash(key):
        return sum(ord(c) for c in key) % collision_table_size

    def table_display():
        if collision_method == "chaining":
            return ", ".join([f"{i}: [{' | '.join(collision_table[i])}]" for i in range(collision_table_size)])
        else:
            return ", ".join([f"{i}: {collision_table[i] if collision_table[i] is not None else '-'}" for i in range(collision_table_size)])

screen chapter_9_collision_display():

    frame:
        xalign 0.5
        yalign 0.6
        xpadding 100
        ypadding 100
        vbox:
            spacing 10
            text "Hash Table Collisions — Live Demo" size 32 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
            text "Method: [collision_method]" size 20 color "#FFFFCC" outlines [(1, "#000000", 0, 0)]
            text "Table (slot: contents):" size 20 color "#FFFFFF" outlines [(1, "#000000", 0, 0)]
            text "[table_display()]" size 18 color "#CCFFEE" outlines [(1, "#000000", 0, 0)]
            hbox:
                spacing 10
                frame:
                    textbutton "Insert key" action Return("insert")
                frame:
                    textbutton "Random key" action Return("random")
                frame:
                    textbutton "Switch method" action Return("switch")
                frame:
                    textbutton "Clear table" action Return("clear")
                frame:
                    textbutton "Close" action Return("close")

label chapter_9_Collisions:
    
    a "So, Collisions."
    a "What are they?"
    # Interactive collisions demo: lets the player insert keys and switch between chaining/open addressing.

    a "Collisions happen when two keys map to the same slot." 
    a "Try inserting keys and watch how the table handles them."
    show screen chapter_9_collision_display

    python:

        def collision_demo():
            # Use the globals established at init/top-level.
            global collision_table_size, collision_method, collision_table

            _continue = True
            while _continue:
                # Wait for the screen buttons to Return() a value.
                result = ui.interact()

                if result == "insert":
                    key = renpy.input("Enter a key to insert (e.g. alice):").strip()
                    if not key:
                        renpy.say(None, "Cancelled.")
                    else:
                        h = simple_hash(key)
                        if collision_method == "chaining":
                            if key in collision_table[h]:
                                renpy.sound.play("sfx/error.mp3")
                                renpy.say(None, "Key '{}' already exists in slot {}.".format(key, h))
                            else:
                                collision_table[h].append(key)
                                renpy.sound.play("sfx/ting.mp3")
                                renpy.say(None, "Inserted '{}' into slot {} (chaining).".format(key, h))
                        else:
                            # open addressing (linear probing)
                            placed = False
                            idx = None
                            start = h
                            for i in range(collision_table_size):
                                idx = (start + i) % collision_table_size
                                if collision_table[idx] is None:
                                    collision_table[idx] = key
                                    placed = True
                                    break
                                elif collision_table[idx] == key:
                                    placed = True
                                    break

                            if placed:
                                if collision_table[idx] == key:
                                    renpy.sound.play("sfx/error.mp3")
                                    renpy.say(None, "Key '{}' was already present at slot {}.".format(key, idx))
                                else:
                                    renpy.sound.play("sfx/ting.mp3")
                                    renpy.say(None, "Inserted '{}' at slot {} after probing (open addressing).".format(key, idx))
                            else:
                                renpy.sound.play("sfx/error.mp3")
                                renpy.say(None, "Table is full — insertion failed.")

                elif result == "random":
                    import random, string
                    key = "".join(random.choice(string.ascii_lowercase[:6]) for _ in range(3))
                    h = simple_hash(key)
                    if collision_method == "chaining":
                        collision_table[h].append(key)
                        renpy.sound.play("sfx/confirm.mp3")
                        renpy.say(None, "Random key '{}' inserted into slot {} (chaining).".format(key, h))
                    else:
                        placed = False
                        idx = None
                        start = h
                        for i in range(collision_table_size):
                            idx = (start + i) % collision_table_size
                            if collision_table[idx] is None:
                                collision_table[idx] = key
                                placed = True
                                break
                        if placed:
                            renpy.sound.play("sfx/confirm.mp3")
                            renpy.say(None, "Random key '{}' placed at slot {} after probing.".format(key, idx))
                        else:
                            renpy.sound.play("sfx/error.mp3")
                            renpy.say(None, "Table is full — random insertion failed.")

                elif result == "switch":
                    if collision_method == "chaining":
                        # Convert chaining -> open addressing
                        new_table = [None] * collision_table_size
                        failed = False
                        for i in range(collision_table_size):
                            for k in collision_table[i]:
                                h = simple_hash(k)
                                placed = False
                                for probe in range(collision_table_size):
                                    idx = (h + probe) % collision_table_size
                                    if new_table[idx] is None:
                                        new_table[idx] = k
                                        placed = True
                                        break
                                if not placed:
                                    failed = True
                                    break
                            if failed:
                                break
                        if failed:
                            renpy.sound.play("sfx/error.mp3")
                            renpy.say(None, "Conversion failed: not enough space to place all keys with open addressing.")
                        else:
                            collision_table = new_table
                            collision_method = "open"
                            renpy.sound.play("sfx/confirm.mp3")
                            renpy.say(None, "Switched to open addressing (keys reinserted with probing).")
                    else:
                        # open -> chaining
                        new_table = [[] for _ in range(collision_table_size)]
                        for i in range(collision_table_size):
                            if collision_table[i] is not None:
                                h = simple_hash(collision_table[i])
                                new_table[h].append(collision_table[i])
                        collision_table = new_table
                        collision_method = "chaining"
                        renpy.sound.play("sfx/confirm.mp3")
                        renpy.say(None, "Switched to chaining (each slot is now a list).")

                elif result == "clear":
                    if collision_method == "chaining":
                        collision_table = [[] for _ in range(collision_table_size)]
                    else:
                        collision_table = [None] * collision_table_size
                    renpy.sound.play("sfx/error.mp3")
                    renpy.say(None, "Table cleared.")

                else:
                    # close or any other
                    _continue = False

        # Call the demo function so the interactive loop runs while this label is active.
        collision_demo()

    show adrian explaining
    a "It is intersting to see something like this"
    a "Should we avoid collisions?"
    a "Not necessarily! Collisions are a normal part of hash table operation."
    a "With good hash functions and collision resolution strategies" 
    a "performance remains efficient even with some collisions."
    hide screen chapter_9_collision_display

    a "You explored collision handling interactively."
    a "Chaining keeps multiple items per slot; open addressing probes for an empty slot."
    a "Notice how collisions affect where keys end up and why a good hash function and resizing matter."

    $ chapter_9_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Quiz time: Collisions!"
    jump chapter_9_Collisions_Quiz

init python:
    import random
    chapter_9_Collisions_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_9_Collisions_order)

label chapter_9_Collisions_Quiz:
    #5POINTS
    $ chapter_9_Collisions_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_9_Collisions_order:
        $ current_q = chapter_9_Collisions_order.pop(0)

        if current_q == "q1":
            a "What is a collision in a hash table?"
            menu:
                "Two keys hash to the same index":
                    $ chapter_9_Collisions_quiz += 1
                    a "Correct! Collisions occur when different keys map to the same slot."
                "A key is not found":
                    a "Incorrect! That’s a lookup failure, not a collision."
                "The table runs out of space":
                    a "Incorrect! That’s a capacity issue, not a collision."

        elif current_q == "q2":
            a "Which method handles collisions by storing multiple items at the same index?"
            menu:
                "Chaining":
                    $ chapter_9_Collisions_quiz += 1
                    a "Correct! Chaining uses linked lists or similar structures at each index."
                "Open addressing":
                    a "Incorrect! That probes for the next available slot."
                "Rehashing":
                    a "Incorrect! Rehashing changes the hash function or table size."

        elif current_q == "q3":
            a "What does open addressing do when a collision occurs?"
            menu:
                "Finds another empty slot using a probing strategy":
                    $ chapter_9_Collisions_quiz += 1
                    a "Correct! It searches for the next available index."
                "Creates a new hash table":
                    a "Incorrect! That’s not part of open addressing."
                "Deletes the colliding key":
                    a "Incorrect! Keys are never discarded due to collision."

        elif current_q == "q4":
            a "Which probing strategy checks the next slot in sequence?"
            menu:
                "Linear probing":
                    $ chapter_9_Collisions_quiz += 1
                    a "Correct! It moves one step at a time until a free slot is found."
                "Quadratic probing":
                    a "Incorrect! That uses squared steps."
                "Double hashing":
                    a "Incorrect! That uses a second hash function."

        elif current_q == "q5":
            a "Why is collision handling important in hash tables?"
            menu:
                "To maintain efficient access and storage":
                    $ chapter_9_Collisions_quiz += 1
                    a "Correct! Without it, hash tables lose their performance benefits."
                "To prevent memory leaks":
                    a "Incorrect! That’s a separate concern."
                "To sort the keys":
                    a "Incorrect! Hash tables don’t sort keys."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    a "Your score for this quiz is [chapter_9_Collisions_quiz] out of 5."
    jump chapter_9_Dynamic_Resizing

# --- Screen definition (UI only) ---
screen chapter_9_resizing_display():
    frame:
        xalign 0.1
        yalign 0.1
        xpadding 80
        ypadding 60
        vbox:
            spacing 10
            text "Dynamic Resizing — Demo" size 28 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
            text "[resizing_status()]" size 18 color "#FFFFCC"
            text "[display_table()]" size 16 color "#CCFFEE"
            hbox:
                spacing 8
                frame:
                    textbutton "Insert" action Return("insert")
                frame:
                    textbutton "Random" action Return("random")
                frame:
                    textbutton "Reset" action Return("reset")
                frame:
                    textbutton "Close" action Return("close")
init python:
    def resizing_status():
        return f"Size: {table_size}  Items: {item_count}  Threshold: {int(threshold * 100)}%"

init python:
    import random, string

    table_size = 8
    table = [[] for _ in range(table_size)]
    item_count = 0
    threshold = 0.7

    def hash_key(key):
        return sum(ord(c) for c in key) % table_size

    def display_table():
        return "\n".join([f"{i}: {' | '.join(bucket)}" for i, bucket in enumerate(table)])


label chapter_9_Dynamic_Resizing:

    show adrian happy
    a "Let's see how a hash table can grow to keep lookups fast."
    a "We'll use a tiny table and insert keys. When it gets crowded, we'll double it."

    show screen chapter_9_resizing_display

    python:
        global table_size, table, item_count, threshold

        _continue = True
        while _continue:
            result = renpy.ui.interact()

            if result == "insert":
                key = renpy.input("Enter a key to insert:").strip()
                if not key:
                    renpy.say(None, "Cancelled.")
                    continue
                h = hash_key(key)
                if key in table[h]:
                    renpy.sound.play("sfx/error.mp3")
                    renpy.say(None, f"Key '{key}' already exists in slot {h}.")
                else:
                    table[h].append(key)
                    item_count += 1
                    renpy.sound.play("sfx/ting.mp3")
                    renpy.say(None, f"Inserted '{key}' into slot {h}.")

            elif result == "random":
                key = "".join(random.choice(string.ascii_lowercase) for _ in range(4))
                h = hash_key(key)
                table[h].append(key)
                item_count += 1
                renpy.sound.play("sfx/confirm.mp3")
                renpy.say(None, f"Random key '{key}' inserted into slot {h}.")

            elif result == "reset":
                table_size = 8
                table = [[] for _ in range(table_size)]
                item_count = 0
                renpy.sound.play("sfx/error.mp3")
                renpy.say(None, "Table reset to size 8.")

            else:
                _continue = False

            # Check load factor and resize if needed
            if item_count / float(table_size) > threshold:
                renpy.say(None, "Load factor exceeded — resizing now.")
                old_table = table
                old_size = table_size
                table_size *= 2
                table = [[] for _ in range(table_size)]
                for bucket in old_table:
                    for k in bucket:
                        table[hash_key(k)].append(k)
                renpy.sound.play("sfx/confirm.mp3")
                renpy.say(None, f"Resized table from {old_size} to {table_size}.")

    show adrian explaining
    a "Nice! You watched a tiny hash table double when it got crowded."
    hide screen chapter_9_resizing_display

    a "Doubling and rehashing is a simple strategy to keep lookups fast without complicated logic."
    a "Of course, real-world hash tables have more optimizations, but this captures the core idea."

    $ chapter_9_progress += 1
    show adrian smiling
    play sound "sfx/bell.mp3"
    a "Quiz time: Dynamic resizing!"
    jump chapter_9_Dynamic_Resizing_Quiz


init python:
    import random
    chapter_9_Dynamic_Resizing_order = [
        "q1", "q2", "q3", "q4", "q5"
    ]
    random.shuffle(chapter_9_Dynamic_Resizing_order)

label chapter_9_Dynamic_Resizing_Quiz:
    #5POINTS
    $ chapter_9_Dynamic_Resizing_quiz = 0

    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    while chapter_9_Dynamic_Resizing_order:
        $ current_q = chapter_9_Dynamic_Resizing_order.pop(0)

        if current_q == "q1":
            a "What triggers dynamic resizing in a hash table?"
            menu:
                "When a collision occurs":
                    a "Incorrect! Collisions are handled separately."
                "When the load factor exceeds a threshold":  # Correct (middle)
                    $ chapter_9_Dynamic_Resizing_quiz += 1
                    a "Correct! Resizing helps maintain performance as the table fills."
                "When a key is deleted":
                    a "Incorrect! Deletion doesn’t usually trigger resizing."

        elif current_q == "q2":
            a "What is the load factor in a hash table?"
            menu:
                "Size of each key":
                    a "Incorrect! Key size doesn’t define load factor."
                "Number of collisions":
                    a "Incorrect! That’s a separate metric."
                "Ratio of stored elements to table size":  # Correct (bottom)
                    $ chapter_9_Dynamic_Resizing_quiz += 1
                    a "Correct! It helps measure how full the table is."

        elif current_q == "q3":
            a "What happens during dynamic resizing?"
            menu:
                "A new, larger table is created and all elements are rehashed":  # Correct (top)
                    $ chapter_9_Dynamic_Resizing_quiz += 1
                    a "Correct! Rehashing ensures proper distribution in the new table."
                "The table is sorted":
                    a "Incorrect! Hash tables don’t maintain sorted order."
                "Only new keys are added to a second table":
                    a "Incorrect! All keys must be rehashed."

        elif current_q == "q4":
            a "Why is rehashing necessary during resizing?"
            menu:
                "To sort the keys":
                    a "Incorrect! Sorting isn’t part of rehashing."
                "Because the hash function depends on table size":  # Correct (middle)
                    $ chapter_9_Dynamic_Resizing_quiz += 1
                    a "Correct! Changing the size affects index calculations."
                "To remove duplicate keys":
                    a "Incorrect! Rehashing doesn’t remove duplicates."

        elif current_q == "q5":
            a "What is a common strategy for resizing a hash table?"
            menu:
                "Halving the table size":
                    a "Incorrect! That would increase collisions."
                "Keeping the size fixed":
                    a "Incorrect! Fixed size leads to performance issues as data grows."
                "Doubling the table size":  # Correct (bottom)
                    $ chapter_9_Dynamic_Resizing_quiz += 1
                    a "Correct! This helps reduce future collisions and maintains efficiency."

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

init python:
    import random
    chapter_9_easy_question_order = [
        "q1","q2","q3","q4","q5",
        "q6","q7","q8","q9","q10"
    ]
    random.shuffle(chapter_9_easy_question_order)

label chapter_9_quiz_easy:
    $ chapter_9_score = 0
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    show adrian smiling at center
    a "Welcome to the associative arrays quiz. Let's cover keys, hashing, collisions, and common uses."

    while chapter_9_easy_question_order:
        $ current_q = chapter_9_easy_question_order.pop(0)

        if current_q == "q1":
            a "What is an associative array?"
            menu:
                "A data structure that maps keys to values (also called a map or dictionary)":
                    $ chapter_9_score += 1
                    a "Correct! Associative arrays store key→value pairs for fast lookup."
                "An array that maintains insertion order only":
                    a "Incorrect. That's an ordered list concept, not the mapping behavior."
                "A fixed-size numeric array":
                    a "Incorrect. That's a basic array, not an associative mapping."

        elif current_q == "q2":
            a "Which common implementation gives average-case O(1) lookup time for associative arrays?"
            menu:
                "Binary search tree":
                    a "Incorrect. BSTs give O(log n) lookups, not O(1) average."
                "Hash table (using hashing and buckets)":
                    $ chapter_9_score += 1
                    a "Correct! Hash tables provide average O(1) lookups with a good hash function and load factor."
                "Linked list of all entries":
                    a "Incorrect. Linked lists require O(n) scan for lookup."

        elif current_q == "q3":
            a "What is a collision in the context of hash tables?"
            menu:
                "When a key is missing from the table":
                    a "Incorrect. That's a miss, not a collision."
                "When the hash function returns negative values only":
                    a "Incorrect. Negative outputs can be normalized; collision is about same index."
                "When two distinct keys produce the same hash index and map to the same bucket":
                    $ chapter_9_score += 1
                    a "Correct! Collisions happen when different keys hash to the same slot."

        elif current_q == "q4":
            a "Which strategy resolves collisions by storing multiple items per bucket?"
            menu:
                "Chaining (store a list of entries per bucket)":
                    $ chapter_9_score += 1
                    a "Correct! Chaining keeps a bucket list for all keys hashing to that index."
                "Open addressing with probing":
                    a "Incorrect. Open addressing places entries in other empty slots instead of lists."
                "Sorting the keys globally":
                    a "Incorrect. Sorting is unrelated to collision resolution."

        elif current_q == "q5":
            a "What does load factor (α) measure for a hash table?"
            menu:
                "The maximum key length allowed":
                    a "Incorrect. Load factor is about occupancy, not key size."
                "The ratio of number of stored elements to number of buckets (n / buckets)":
                    $ chapter_9_score += 1
                    a "Correct! Load factor guides when to resize to keep performance."
                "The time to compute the hash function":
                    a "Incorrect. That's hash cost, not load factor."

        elif current_q == "q6":
            a "Which open addressing probe sequence is commonly used for simplicity and clustering avoidance?"
            menu:
                "Quadratic probing or double hashing to reduce clustering":
                    $ chapter_9_score += 1
                    a "Correct! Quadratic probing and double hashing mitigate clustering issues."
                "Linear probing only":
                    a "Incorrect. Linear probing is simple but suffers primary clustering."
                "Storing collisions in external database":
                    a "Incorrect. External DB isn't a typical in-memory probe strategy."

        elif current_q == "q7":
            a "Why do most hash-table implementations resize (grow) when load factor exceeds a threshold?"
            menu:
                "To reorder keys alphabetically":
                    a "Incorrect. Resizing is for performance, not ordering."
                "To free memory permanently":
                    a "Incorrect. Growing expands capacity; shrinking may free memory later."
                "To keep average lookup, insert, and delete operations fast by reducing collisions":
                    $ chapter_9_score += 1
                    a "Correct! Resizing (rehashing) lowers load factor and reduces collision cost."

        elif current_q == "q8":
            a "Which property must keys generally have to be used in a hash-based associative array?"
            menu:
                "They must always be integers":
                    a "Incorrect. Many types can be hashed, not just integers."
                "They must be hashable and comparable for equality":
                    $ chapter_9_score += 1
                    a "Correct! Keys need a deterministic hash and equality test to locate entries."
                "They must be unique strings only":
                    a "Incorrect. Any hashable, unique key type is fine."

        elif current_q == "q9":
            a "Which real-world application commonly uses associative arrays?"
            menu:
                "Implementing symbol tables in compilers, caches, configuration maps, and databases":
                    $ chapter_9_score += 1
                    a "Correct! Maps are used widely for name→value lookups and fast indexing."
                "Rendering 3D meshes exclusively":
                    a "Incorrect. Mesh rendering uses other structures; maps may still appear for resources."
                "Only for sorting large arrays":
                    a "Incorrect. Sorting is not the primary use of associative arrays."

        elif current_q == "q10":
            a "What is an OrderedDict or map that preserves insertion order compared to a plain hash table?"
            menu:
                "A map that forbids deletions":
                    a "Incorrect. Ordered maps still allow deletes; they maintain order of remaining keys."
                "A map that preserves insertion order while offering map semantics (keys → values)":
                    $ chapter_9_score += 1
                    a "Correct! Many languages provide ordered map variants that remember insertion order."
                "A variant that always sorts keys by value":
                    a "Incorrect. Ordered maps preserve insertion order, not sort by value."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Your quiz score is: [chapter_9_score]"
    jump chapter_9_performance

init python:
    import random
    chapter_9_quiz_medium_order = [
        "q1", "q2", "q3", "q4", "q5",
        "q6", "q7", "q8", "q9", "q10",
        "q11", "q12", "q13", "q14", "q15"
    ]
    random.shuffle(chapter_9_quiz_medium_order)

label chapter_9_quiz_medium:
    $ chapter_9_score = 0
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    a "Welocme to the Chapter Quiz!"
    while chapter_9_quiz_medium_order:
        $ current_q = chapter_9_quiz_medium_order.pop(0)

        if current_q == "q1":
            a "Which data structure is commonly used to implement associative arrays?"
            menu:
                "Linked list":
                    a "Incorrect. Linked lists are not efficient for key-based access."
                "Hash table":  # Correct
                    $ chapter_9_score += 1
                    a "Correct! Hash tables provide fast key-value lookups."
                "Binary tree":
                    a "Incorrect. Trees can be used, but hash tables are more common."

        elif current_q == "q2":
            a "What is the primary advantage of associative arrays?"
            menu:
                "They store data sequentially":
                    a "Incorrect. Associative arrays are not about sequence."
                "They allow fast access via keys":  # Correct
                    $ chapter_9_score += 1
                    a "Correct! Keys enable quick retrieval of values."
                "They use less memory than arrays":
                    a "Incorrect. Memory usage depends on implementation."

        elif current_q == "q3":
            a "In associative arrays, what must be unique?"
            menu:
                "Values":
                    a "Incorrect. Values can be duplicated."
                "Keys":  # Correct
                    $ chapter_9_score += 1
                    a "Correct! Each key must be unique to avoid ambiguity."
                "Indexes":
                    a "Incorrect. Indexes are not used in associative arrays."

        elif current_q == "q4":
            a "Which operation is typically fastest in a hash-based associative array?"
            menu:
                "Searching by key":  # Correct
                    $ chapter_9_score += 1
                    a "Correct! Hashing allows near-constant time lookup."
                "Sorting values":
                    a "Incorrect. Sorting is not a primary feature."
                "Iterating through values":
                    a "Incorrect. Iteration is linear and not the fastest operation."

        elif current_q == "q5":
            a "What happens if two keys hash to the same index?"
            menu:
                "The second key is discarded":
                    a "Incorrect. That would cause data loss."
                "A collision occurs and must be resolved":  # Correct
                    $ chapter_9_score += 1
                    a "Correct! Collisions are handled using techniques like chaining or probing."
                "The table resizes immediately":
                    a "Incorrect. Resizing is based on load factor, not collisions."

        elif current_q == "q6":
            a "Which of the following is a valid key in most associative arrays?"
            menu:
                "A list":
                    a "Incorrect. Lists are mutable and usually not hashable."
                "A string":  # Correct
                    $ chapter_9_score += 1
                    a "Correct! Strings are immutable and commonly used as keys."
                "A dictionary":
                    a "Incorrect. Dictionaries are mutable and not hashable."

        elif current_q == "q7":
            a "What is a common method to resolve hash collisions?"
            menu:
                "Binary search":
                    a "Incorrect. Binary search is not used for collisions."
                "Chaining":  # Correct
                    $ chapter_9_score += 1
                    a "Correct! Chaining stores multiple items at the same index."
                "Sorting the table":
                    a "Incorrect. Sorting doesn’t resolve collisions."

        elif current_q == "q8":
            a "Which of these best describes a hash function?"
            menu:
                "A function that sorts keys":
                    a "Incorrect. Sorting is not its purpose."
                "A function that maps keys to indices":  # Correct
                    $ chapter_9_score += 1
                    a "Correct! It determines where to store each key-value pair."
                "A function that encrypts data":
                    a "Incorrect. Hashing is not encryption."

        elif current_q == "q9":
            a "What is the typical time complexity for inserting into a hash table (without collisions)?"
            menu:
                "O(n)":
                    a "Incorrect. That would be inefficient."
                "O(1)":  # Correct
                    $ chapter_9_score += 1
                    a "Correct! Constant time is the goal of hashing."
                "O(log n)":
                    a "Incorrect. That’s typical for balanced trees."

        elif current_q == "q10":
            a "Which scenario might trigger dynamic resizing in a hash table?"
            menu:
                "When the load factor exceeds a threshold":  # Correct
                    $ chapter_9_score += 1
                    a "Correct! Resizing helps maintain performance."
                "When a key is accessed":
                    a "Incorrect. Access doesn’t trigger resizing."
                "When a collision occurs":
                    a "Incorrect. Collisions are handled separately."

        elif current_q == "q11":
            a "What is the load factor in a hash table?"
            menu:
                "Ratio of stored elements to table size":  # Correct
                    $ chapter_9_score += 1
                    a "Correct! It helps measure how full the table is."
                "Size of each key":
                    a "Incorrect. Key size doesn’t define load factor."
                "Number of collisions":
                    a "Incorrect. That’s a separate metric."

        elif current_q == "q12":
            a "Which of the following is NOT a typical use case for associative arrays?"
            menu:
                "Counting word frequencies":
                    a "Incorrect. That’s a common use."
                "Storing pixel data in images":  # Correct
                    $ chapter_9_score += 1
                    a "Correct! Pixel data is usually stored in arrays, not key-value pairs."
                "Mapping usernames to user IDs":
                    a "Incorrect. That’s a classic use case."

        elif current_q == "q13":
            a "Which of these is a disadvantage of hash tables?"
            menu:
                "They are slow to access":
                    a "Incorrect. They are fast for access."
                "They require sorted keys":
                    a "Incorrect. Sorting is not required."
                "They can have poor performance with many collisions":  # Correct
                    $ chapter_9_score += 1
                    a "Correct! Too many collisions can degrade performance."

        elif current_q == "q14":
            a "What does it mean if a key is not found in an associative array?"
            menu:
                "The key maps to a null value":
                    a "Incorrect. It means the key doesn’t exist."
                "The key was deleted":
                    a "Incorrect. Not necessarily—it may never have existed."
                "The key is not present in the structure":  # Correct
                    $ chapter_9_score += 1
                    a "Correct! A missing key simply isn’t stored."

        elif current_q == "q15":
            a "Which of the following languages has built-in support for associative arrays?"
            menu:
                "Python":  # Correct
                    $ chapter_9_score += 1
                    a "Correct! Python’s dictionaries are associative arrays."
                "Assembly":
                    a "Incorrect. Assembly doesn’t have high-level data structures."
                "C without libraries":
                    a "Incorrect. C requires manual implementation."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Your quiz score is: [chapter_9_score]"
    jump chapter_9_performance

init python:
    import random
    chapter_9_quiz_hard_order = [
        "q1", "q2", "q3", "q4", "q5",
        "q6", "q7", "q8", "q9", "q10",
        "q11", "q12", "q13", "q14", "q15",
        "q16", "q17", "q18", "q19", "q20"
    ]
    random.shuffle(chapter_9_quiz_hard_order)

label chapter_9_quiz_hard:
    $ chapter_9_score = 0
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    a "Let's dive into a deeper challenge. These questions will test your understanding of associative arrays from multiple angles. Take your time and think carefully."

    while chapter_9_quiz_hard_order:
        $ current_q = chapter_9_quiz_hard_order.pop(0)

        if current_q == "q1":
            a "Which hashing technique minimizes clustering in open addressing?"
            menu:
                "Quadratic probing":  # Correct (top)
                    $ chapter_9_score += 1
                    a "Correct! Quadratic probing reduces clustering by spreading probes."
                "Linear probing":
                    a "Incorrect. Linear probing can cause primary clustering."
                "Separate chaining":
                    a "Incorrect. Chaining is not an open addressing method."

        elif current_q == "q2":
            a "What is the worst-case time complexity for searching in a hash table with chaining?"
            menu:
                "O(1)":
                    a "Incorrect. That’s the best case."
                "O(n)":  # Correct (middle)
                    $ chapter_9_score += 1
                    a "Correct! In the worst case, all elements may hash to the same bucket."
                "O(log n)":
                    a "Incorrect. That applies to balanced trees, not hash chains."

        elif current_q == "q3":
            a "Which property must a good hash function satisfy?"
            menu:
                "It must be reversible":
                    a "Incorrect. Hash functions are not meant to be reversible."
                "It must sort the keys":
                    a "Incorrect. Sorting is unrelated to hashing."
                "It must distribute keys uniformly":  # Correct (bottom)
                    $ chapter_9_score += 1
                    a "Correct! Uniform distribution reduces collisions."

        elif current_q == "q4":
            a "What does rehashing involve?"
            menu:
                "Recomputing hashes and resizing the table":  # Correct (top)
                    $ chapter_9_score += 1
                    a "Correct! Rehashing redistributes keys in a larger table."
                "Changing the hash function":
                    a "Incorrect. Rehashing usually keeps the same function."
                "Deleting all keys and starting over":
                    a "Incorrect. That would lose data."

        elif current_q == "q5":
            a "Which scenario causes the most performance degradation in hash tables?"
            menu:
                "Low load factor":
                    a "Incorrect. Low load factor improves performance."
                "High collision rate":  # Correct (middle)
                    $ chapter_9_score += 1
                    a "Correct! Collisions slow down access and insertion."
                "Using numeric keys":
                    a "Incorrect. Numeric keys are fine if hashed properly."

        elif current_q == "q6":
            a "Which of the following is true about associative arrays in Python?"
            menu:
                "They automatically sort keys":
                    a "Incorrect. Sorting must be done manually."
                "They require keys to be integers":
                    a "Incorrect. Keys can be any hashable type."
                "They preserve insertion order":  # Correct (bottom)
                    $ chapter_9_score += 1
                    a "Correct! Since Python 3.7, dictionaries preserve order."

        elif current_q == "q7":
            a "What is double hashing?"
            menu:
                "Using two hash functions to resolve collisions":  # Correct (top)
                    $ chapter_9_score += 1
                    a "Correct! Double hashing spreads out probes more effectively."
                "Using two hash tables":
                    a "Incorrect. It’s not about multiple tables."
                "Hashing keys twice for security":
                    a "Incorrect. That’s more relevant to cryptography."

        elif current_q == "q8":
            a "Which of these is a disadvantage of separate chaining?"
            menu:
                "It cannot handle collisions":
                    a "Incorrect. Chaining is designed for collisions."
                "It uses extra memory for linked lists":  # Correct (middle)
                    $ chapter_9_score += 1
                    a "Correct! Each bucket may store a list of entries."
                "It requires keys to be sorted":
                    a "Incorrect. Sorting is not required."

        elif current_q == "q9":
            a "What is the amortized cost of insertion in a dynamic hash table?"
            menu:
                "O(log n)":
                    a "Incorrect. That applies to tree structures."
                "O(n)":
                    a "Incorrect. That’s the worst-case during resizing."
                "O(1)":  # Correct (bottom)
                    $ chapter_9_score += 1
                    a "Correct! Most insertions are constant time."

        elif current_q == "q10":
            a "Which of these key types is invalid in most associative arrays?"
            menu:
                "List":  # Correct (top)
                    $ chapter_9_score += 1
                    a "Correct! Lists are mutable and not hashable."
                "Tuple":
                    a "Incorrect. Tuples are immutable and valid."
                "Integer":
                    a "Incorrect. Integers are commonly used."

        elif current_q == "q11":
            a "Which structure is best for implementing an associative array with ordered keys?"
            menu:
                "Hash table":
                    a "Incorrect. Hash tables don’t maintain order."
                "Binary search tree":  # Correct (middle)
                    $ chapter_9_score += 1
                    a "Correct! BSTs maintain sorted order of keys."
                "Stack":
                    a "Incorrect. Stacks are not key-based."

        elif current_q == "q12":
            a "What does the term 'bucket' refer to in hashing?"
            menu:
                "A backup table for overflow":
                    a "Incorrect. That’s not standard terminology."
                "A temporary storage for deleted keys":
                    a "Incorrect. Buckets store active entries."
                "A slot in the hash table where keys map":  # Correct (bottom)
                    $ chapter_9_score += 1
                    a "Correct! Buckets hold key-value pairs."

        elif current_q == "q13":
            a "Which of these is most likely to cause clustering?"
            menu:
                "Linear probing":  # Correct (top)
                    $ chapter_9_score += 1
                    a "Correct! Linear probing can cause primary clustering."
                "Separate chaining":
                    a "Incorrect. Chaining avoids clustering."
                "Double hashing":
                    a "Incorrect. Double hashing reduces clustering."

        elif current_q == "q14":
            a "What is the purpose of a sentinel value in associative arrays?"
            menu:
                "To store default values":
                    a "Incorrect. Defaults are handled differently."
                "To mark deleted entries":  # Correct (middle)
                    $ chapter_9_score += 1
                    a "Correct! Sentinels help manage deletions in open addressing."
                "To sort the keys":
                    a "Incorrect. Sorting doesn’t use sentinels."

        elif current_q == "q15":
            a "Which of these operations is not typically supported by associative arrays?"
            menu:
                "Key-based lookup":
                    a "Incorrect. That’s the core feature."
                "Key insertion":
                    a "Incorrect. Insertion is supported."
                "Value-based deletion":  # Correct (bottom)
                    $ chapter_9_score += 1
                    a "Correct! Deletion is usually key-based."

        elif current_q == "q16":
            a "What does 'hashable' mean in Python?"
            menu:
                "The object has a fixed hash value":  # Correct (top)
                    $ chapter_9_score += 1
                    a "Correct! Hashable objects must be immutable and consistent."
                "The object can be sorted":
                    a "Incorrect. Sorting is unrelated."
                "The object is encrypted":
                    a "Incorrect. Hashing is not encryption."

        elif current_q == "q17":
            a "Which of these is true about resizing a hash table?"
            menu:
                "It deletes half the keys":
                    a "Incorrect. Keys are preserved."
                "It improves performance by reducing collisions":  # Correct (middle)
                    $ chapter_9_score += 1
                    a "Correct! A larger table lowers the load factor."
                "It sorts the keys":
                    a "Incorrect. Sorting is not involved."

        elif current_q == "q18":
            a "Which of these is a valid reason to use associative arrays?"
            menu:
                "To perform matrix multiplication":
                    a "Incorrect. That’s not their purpose."
                "To store sequential data":
                    a "Incorrect. Arrays are better for that."
                "To map identifiers to values":  # Correct (bottom)
                    $ chapter_9_score += 1
                    a "Correct! Associative arrays excel at key-value mapping."

        elif current_q == "q19":
            a "When using open addressing, what must you do when deleting an entry to keep lookups correct?"
            menu:
                "Mark the slot with a special deleted sentinel":  # Correct (top)
                    $ chapter_9_score += 1
                    a "Correct! A sentinel preserves probe chains for existing keys."
                "Set the slot to empty and stop":
                    a "Incorrect. Clearing it outright breaks probes."
                "Immediately rehash the entire table":
                    a "Incorrect. Rehashing on every delete is unnecessary."

        elif current_q == "q20":
            a "Which metric directly influences when many implementations trigger a resize?"
            menu:
                "The number of buckets":
                    a "Incorrect. Bucket count is a table property, not the trigger."
                "Load factor (ratio of elements to buckets)":  # Correct (middle)
                    $ chapter_9_score += 1
                    a "Correct! Load factor thresholds prompt resizing to maintain performance."
                "Average key length":
                    a "Incorrect. Key length doesn't typically trigger resizing."

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Your quiz score is: [chapter_9_score]"
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
    play sound "sfx/success.mp3"
    play music "bgm/city-high-life.mp3" fadein 1.0
    $ persistent.chapter_9 = True
    a "Would You like to test again?"
    menu:
        "Yes":
            jump chapter_9_restart
        "No":
            pass
    show adrian happy
    a "You have finished chapter 9. You can continue to Chapter 10!"
    jump menu