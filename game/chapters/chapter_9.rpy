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

    call hideall
    play sound "sfx/start.mp3"
    stop music fadeout 1.0

    scene black
    pause 1.0

    show screen chapter_9_AAIntro
    scene mt tree with dissolve
    pause 2.0
    hide screen chapter_9_AAIntro

    show screen menu_btn

    play music "bgm/city-high-life.mp3" fadein 1.0
    show adrian smiling at center:
        smaller
    with dissolve

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
                textbutton "Add entry" action Return("add")
                textbutton "Lookup" action Return("lookup")
                textbutton "Close" action Return("close")

init python:
    # Demo dictionary for the interactive screen. Kept simple so players can experiment.
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
                textbutton "Insert key" action Return("insert")
                textbutton "Random key" action Return("random")
                textbutton "Switch method" action Return("switch")
                textbutton "Clear table" action Return("clear")
                textbutton "Close" action Return("close")

label chapter_9_Collisions:
    
    a "So, Collisions."
    a "What are they?"
    # Interactive collisions demo: lets the player insert keys and switch between chaining/open addressing.

    a "Collisions happen when two keys map to the same slot." 
    a "Try inserting keys and watch how the table handles them."
    show screen chapter_9_collision_display

    python:
        import ui

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
                textbutton "Insert" action Return("insert")
                textbutton "Random" action Return("random")
                textbutton "Reset" action Return("reset")
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

label chapter_9_quiz_easy:
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert easy quiz questions here)

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    jump chapter_9_performance

label chapter_9_quiz_medium:
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert medium quiz questions here)

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
    jump chapter_9_performance

label chapter_9_quiz_hard:
    stop music fadeout 0.5
    play music "bgm/better-answer.mp3" fadein 1.0
    show adrian normal

    # (Insert hard quiz questions here)

    show adrian happy
    stop music fadeout 0.5
    play music "bgm/city-high-life.mp3" fadein 0.5
    play sound "sfx/success.mp3"
    a "Great job!"
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