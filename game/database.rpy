init python:
    import requests

    FLASK_URL = "https://renpy-flask-db.onrender.com/add_student"

    def send_student_data(name, student_id):
        data = {
            "name": name,
            "student_id": student_id
        }
        try:
            response = requests.post(FLASK_URL, json=data, timeout=10)
            if response.status_code == 200:
                result = response.json()
                return result.get("message", "No message from server")
            else:
                return f"Error: {response.status_code}"
        except requests.exceptions.RequestException as e:
            return f"Request failed: {e}"


label database_user_info:
    # Input student info
    $ student_name = renpy.input("Enter your name:").strip()
    $ student_id = renpy.input("Enter your ID number:").strip()

    # Send data to Flask + Firebase
    $ result_msg = send_student_data(student_name, student_id)
    "Server response: [result_msg]"

    return