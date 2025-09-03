init python:
    import requests
    import json

    FIREBASE_BASE_URL = "https://datastructhesis-default-rtdb.asia-southeast1.firebasedatabase.app/Students/"

    def send_student_data(name, student_id):
        data = {
            "Name": name,
            "Student ID": student_id,
            "chapter_scores": {
                "Chapter 1: Abstract Data Structures": 0,
                "Chapter 2: Arrays": 0,
                "Chapter 3: Linked List": 0,
                "Chapter 4: Stack & Queues": 0
            }
        }
        try:
            url = f"{FIREBASE_BASE_URL}/{student_id}.json"
            response = requests.put(url, data=json.dumps(data), timeout=10)
            if response.status_code == 200:
                return f"Data saved for {name} (ID: {student_id})"
            else:
                return f"Firebase Error: {response.status_code} - {response.text}"
        except requests.exceptions.RequestException as e:
            return f"Request failed: {e}"

    def submit_scores(student_id):
        """Submit all chapter scores to Firebase"""
        try:
            url = f"{FIREBASE_BASE_URL}/{student_id}.json"
            
            clean_data = {
                "Name": current_student_name,
                "Student ID": student_id,
                "chapter_scores": {
                    "Chapter 1: Abstract Data Structures": chapter_1_score,
                    "Chapter 2: Arrays": chapter_2_score,
                    "Chapter 3: Linked List": chapter_3_score,
                    "Chapter 4: Stack & Queues": chapter_4_score
                }
            }
            
            
            put_response = requests.put(url, data=json.dumps(clean_data), timeout=10)
            if put_response.status_code == 200:
                return f"Scores submitted successfully!"
            else:
                return f"Failed to submit: {put_response.status_code}"
        except requests.exceptions.RequestException as e:
            return f"Submit failed: {e}"


default student_input = ""
default current_student_id = ""
default current_student_name = ""

screen student_input_screen(prompt):
    window:
        yalign 0.5
        background None
        yfill True
        has vbox xalign 0.5 yalign 0.5
        
        text prompt xalign 0.5
        input id "input" default "" allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ":
            value VariableInputValue("student_input")

        textbutton "Submit":
            action Return()
    
    use quick_menu

label database_user_info:
    # Get student name
    $ student_input = ""
    call screen student_input_screen("Enter your name:")
    $ student_name = student_input.strip()
    
    # Check if name is empty
    if student_name == "":
        "Name cannot be empty. Please try again."
        jump database_user_info
    
    # Get student ID
    $ student_input = ""
    call screen student_input_screen("Enter your ID number:")
    $ student_id = student_input.strip()
    
    # Check if ID is empty
    if student_id == "":
        "ID cannot be empty. Please try again."
        jump database_user_info
    
    # Store for later use
    $ current_student_id = student_id
    $ current_student_name = student_name

    # Send data directly to Firebase under their ID
    $ result_msg = send_student_data(student_name, student_id)
    "Server response: [result_msg]"

    return

label submit_all_chapter_scores:
    if current_student_id == "":
        "You need to register first!"
        call database_user_info
    
    $ result = submit_scores(current_student_id)
    "[result]"
    
    return
