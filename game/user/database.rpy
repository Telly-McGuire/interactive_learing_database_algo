init python:
    import requests
    import json

    
    API_KEY = "AIzaSyDRbPXgDcNxqPOalvOLim2YMeg5PRTj39k"

    
    FIREBASE_BASE_URL = "https://datastructhesis-default-rtdb.asia-southeast1.firebasedatabase.app/Students/"

    # Auth state
    ID_TOKEN = None
    CURRENT_UID = None

    def ensure_auth():
        """
        Anonymous sign-in to Firebase Auth.
        Sets ID_TOKEN and CURRENT_UID for use in database requests.
        """
        global ID_TOKEN, CURRENT_UID
        if ID_TOKEN and CURRENT_UID:
            return True, "ok"

        url = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={API_KEY}"
        try:
            r = requests.post(url, json={}, timeout=10)
            if r.status_code != 200:
                return False, f"Auth failed: {r.status_code} - {r.text}"
            data = r.json()
            ID_TOKEN = data.get("idToken")
            CURRENT_UID = data.get("localId")
            if not ID_TOKEN or not CURRENT_UID:
                return False, "Auth failed: missing idToken/localId"
            return True, "ok"
        except requests.exceptions.RequestException as e:
            return False, f"Auth request error: {e}"

    def _student_url_uid():
        # Path for the current user: Students/<uid>.json
        return f"{FIREBASE_BASE_URL}{CURRENT_UID}.json"

    def _auth_params():
        # Pass idToken to Realtime Database using ?auth=
        return {"auth": ID_TOKEN} if ID_TOKEN else None

    def send_student_data(name, student_id):
        """
        Create or overwrite the current user's node with zeroed scores.
        'student_id' is a field; the node key is the Firebase uid.
        """
        ok, msg = ensure_auth()
        if not ok:
            return f"Auth error: {msg}"

        data = {
            "Name": name,
            "Student ID": student_id,
            "chapter_scores": {
                "Chapter 1: Abstract Data Structures": 0,
                "Chapter 2: Arrays": 0,
                "Chapter 3: Linked List": 0,
                "Chapter 4: Stack & Queues": 0,
                "Chapter 5: Trees": 0,
                "Chapter 6: AVL Trees": 0,
                "Chapter 7: Binary Search Trees": 0,
                "Chapter 8: Heaps": 0,
                "Chapter 9: Associative Arrays": 0,
                "Chapter 10: Graph Algorithms": 0,
                "Chapter 11: Graph Traversal Algorithms": 0
            }
        }
        try:
            response = requests.put(
                _student_url_uid(),
                params=_auth_params(),
                json=data,
                timeout=10
            )
            if response.status_code == 200:
                return f"Data saved for {name} (ID: {student_id})"
            else:
                # Escape curly braces by doubling them
                error_text = response.text.replace("{", "{{").replace("}", "}}")
                return f"Firebase Error: {response.status_code} - {error_text}"
        except requests.exceptions.RequestException as e:
            return f"Request failed: {e}"

    def submit_scores(student_id, scores_dict, student_name):
        """
        Overwrite the user's node with the latest name/id and all scores.
        """
        ok, msg = ensure_auth()
        if not ok:
            return f"Auth error: {msg}"

        clean_data = {
            "Name": student_name,
            "Student ID": student_id,
            "chapter_scores": scores_dict
        }
        try:
            put_response = requests.put(
                _student_url_uid(),
                params=_auth_params(),
                json=clean_data,
                timeout=10
            )
            if put_response.status_code == 200:
                return "Scores submitted successfully!"
            else:
                # Escape curly braces by doubling them
                error_text = put_response.text.replace("{", "{{").replace("}", "}}")
                return f"Failed to submit: {put_response.status_code} - {error_text}"
        except requests.exceptions.RequestException as e:
            return f"Submit failed: {e}"

    def patch_chapter_scores(scores_dict):
        """
        Optional: update only chapter_scores instead of overwriting the entire node.
        """
        ok, msg = ensure_auth()
        if not ok:
            return f"Auth error: {msg}"

        try:
            patch_url = f"{FIREBASE_BASE_URL}{CURRENT_UID}/chapter_scores.json"
            r = requests.patch(
                patch_url,
                params=_auth_params(),
                json=scores_dict,
                timeout=10
            )
            if r.status_code == 200:
                return "Scores updated (partial)!"
            else:
                # Escape curly braces by doubling them
                error_text = r.text.replace("{", "{{").replace("}", "}}")
                return f"Failed to patch scores: {r.status_code} - {error_text}"
        except requests.exceptions.RequestException as e:
            return f"Patch failed: {e}"

# These defaults don't duplicate your chapter_* defaults from script.rpy.
# Keep chapter_* defaults only in one file (you already have them in script.rpy).
default student_input = ""
default current_student_id = ""
default current_student_name = ""

screen student_input_screen(prompt):
    window:
        yalign 0.5
        background None
        yfill True

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 10

            text prompt xalign 0.5

            input:
                default ""
                allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789- "
                value VariableInputValue("student_input")
                length 40

            textbutton "Submit":
                action Return()

label database_user_info:
    # Get student name
    $ student_input = ""
    call screen student_input_screen("Enter your name:")
    $ student_name = student_input.strip()

    if student_name == "":
        "Name cannot be empty. Please try again."
        jump database_user_info

    # Get student ID
    $ student_input = ""
    call screen student_input_screen("Enter your ID number:")
    $ student_id = student_input.strip()

    if student_id == "":
        "ID cannot be empty. Please try again."
        jump database_user_info

    # Store for later use
    $ current_student_id = student_id
    $ current_student_name = student_name

    # Send data directly to Firebase under their user (per-uid)
    $ result_msg = send_student_data(student_name, student_id)
    "[result_msg!q]"

    return

label submit_all_chapter_scores:
    if current_student_id == "":
        "You need to register first!"
        call database_user_info

    $ scores_dict = {
        "Chapter 1: Abstract Data Structures": chapter_1_score,
        "Chapter 2: Arrays": chapter_2_score,
        "Chapter 3: Linked List": chapter_3_score,
        "Chapter 4: Stack & Queues": chapter_4_score,
        "Chapter 5: Trees": chapter_5_score,
        "Chapter 6: AVL Trees": chapter_6_score,
        "Chapter 7: Binary Search Trees": chapter_7_score,
        "Chapter 8: Heaps": chapter_8_score,
        "Chapter 9: Associative Arrays": chapter_9_score,
        "Chapter 10: Graph Algorithms": chapter_10_score,
        "Chapter 11: Graph Traversal Algorithms": chapter_11_score,
    }

    $ result = submit_scores(current_student_id, scores_dict, current_student_name)
    "[result!q]"

    # Or to partially update only chapter_scores:
    # $ result = patch_chapter_scores(scores_dict)
    # "[result!q]"

    return