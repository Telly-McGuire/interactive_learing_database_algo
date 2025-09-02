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


label database_user_info:
    # Input student info
    $ student_name = renpy.input("Enter your name:").strip()
    $ student_id = renpy.input("Enter your ID number:").strip()

    # Send data directly to Firebase under their ID
    $ result_msg = send_student_data(student_name, student_id)
    "Server response: [result_msg]"

    return