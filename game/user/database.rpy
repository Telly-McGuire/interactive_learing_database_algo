init python:
    import requests
    import json

    FIREBASE_BASE_URL = "https://datastructhesis-default-rtdb.asia-southeast1.firebasedatabase.app/"

    def send_student_data(name, student_id):
        data = {
            "name": name,
            "student_id": student_id,
            "score": 0   # default score
        }
        try:
            url = f"{FIREBASE_BASE_URL}/{student_id}.json"
            response = requests.put(url, data=json.dumps(data), timeout=10)
            if response.status_code == 200:
                return f"Data saved for ID {student_id}"
            else:
                return f"Firebase Error: {response.status_code} - {response.text}"
        except requests.exceptions.RequestException as e:
            return f"Request failed: {e}"

screen student_input_screen(prompt):
    window:
        yalign 0.5
        background None
        yfill True
        has vbox xalign 0.5 yalign 0.5

        text prompt xalign 0.5
        input id "input"

    use quick_menu

default student_input = ""

init python:
    def get_input(prompt_text):
        global student_input
        student_input = ""
        renpy.call_screen("student_input_screen", prompt=prompt_text)
        return student_input.strip()


screen student_input_screen(prompt):
    window:
        yalign 0.5
        background None
        yfill True
        has vbox xalign 0.5 yalign 0.5
        
        text prompt xalign 0.5
        input id "input" default "" allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ":
            changed student_input

        textbutton "Submit":
            action Return()
    use quick_menu


label database_user_info:
    # Input student info
    $ student_name = renpy.input("Enter your name:").strip()
    $ student_id = renpy.input("Enter your ID number:").strip()

    # Send data directly to Firebase under their ID
    $ result_msg = send_student_data(student_name, student_id)
    "Server response: [result_msg]"

    return