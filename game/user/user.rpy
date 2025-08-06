# List to gather user information outside the label
default user_name = "Adrian"
default user_id = "12345"
default user_info_list = []

label user_info:
    stop music
    scene black
    $ user_name = renpy.input("What is your name?", default=user_name)
    $ user_name = user_name.strip()
    if not user_name:
        $ user_name = "Adrian"

    $ user_id = renpy.input("What is your ID Number?", default=user_id)
    $ user_id = user_id.strip()
    if not user_id:
        $ user_id = "12345"

    $ persistent.user_name = user_name
    $ persistent.user_id = user_id

    # Gather user information in the list
    $ user_info_list.append({"name": user_name, "id": user_id})

    show black
    with dissolve
    pause 0.5

    a "Hi [user_name] (ID: [user_id]), welcome to the Data Structures and Algorithms!"
    a "are you ready?"
    menu:
        "Yes":
            a "Great! Let's get started."
            return
        "No":
            $ renpy.quit()

    pass