# Flask Strong Password Signup

This is a minimal Flask-based API that validates strong passwords during signup. It checks for:

- A minimum length of 8 characters  
- At least one uppercase letter  
- At least one lowercase letter  
- At least one digit  
- At least one special character  

---

## Project Structure

    .
    ├── app.py
    └── README.md

- **app.py**: Contains the Flask application code.  
- **README.md**: Project documentation (this file).

---

## Prerequisites

- [Python 3](https://www.python.org/downloads/) installed on your system.  
- [pip](https://pip.pypa.io/en/stable/installing/) (usually comes with Python).  

---

## Quick Start

1. **Clone or Download** this repository.
2. **Open a Command Prompt (CMD)** in the project folder.

### 1. Create and Activate a Virtual Environment (Recommended)

It’s best practice to isolate your project’s dependencies using a virtual environment:

    python -m venv venv
    venv\Scripts\activate

If you ever want to deactivate:

    deactivate

*(If you’re on macOS/Linux, use `source venv/bin/activate` instead.)*

### 2. Install Flask

Since we’re not using a `requirements.txt`, install Flask directly:

    pip install flask

### 3. Run the Application

    python app.py

You should see output similar to:

    * Serving Flask app 'app'
    * Debug mode: on
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

By default, Flask listens on port **5000**.

### 4. Test the Endpoint

Use a tool like [Postman](https://www.postman.com/) or [cURL](https://curl.se/) to send a **POST** request to:

    http://127.0.0.1:5000/signup

with JSON data containing a `password` field.

#### Example cURL command:

    curl -X POST -H "Content-Type: application/json" \
         -d "{\"password\": \"StrongPassw0rd!\"}" \
         http://127.0.0.1:5000/signup

A successful request with a strong password returns:

    {
      "message": "Signup successful"
    }

If the password fails any criteria, you’ll receive an error message like:

    {
      "error": "Password must contain at least one uppercase letter"
    }

(With an HTTP status code of `400`.)

---

## Code Explanation

Below is the core `app.py` code:

    from flask import Flask, request, jsonify
    import re

    app = Flask(__name__)

    @app.route('/signup', methods=['POST'])
    def signup():
        data = request.json

        # Check if password is provided
        if not data or 'password' not in data:
            return jsonify({"error": "Password is required"}), 400

        password = data["password"]

        # 1. Length check
        if len(password) < 8:
            return jsonify({"error": "Password must be at least 8 characters long"}), 400

        # 2. Uppercase letter check
        if not re.search(r"[A-Z]", password):
            return jsonify({"error": "Password must contain at least one uppercase letter"}), 400

        # 3. Lowercase letter check
        if not re.search(r"[a-z]", password):
            return jsonify({"error": "Password must contain at least one lowercase letter"}), 400

        # 4. Digit check
        if not re.search(r"\d", password):
            return jsonify({"error": "Password must contain at least one digit"}), 400

        # 5. Special character check
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return jsonify({"error": "Password must contain at least one special character"}), 400

        # If all checks pass
        return jsonify({"message": "Signup successful"}), 200

    if __name__ == "__main__":
        app.run(debug=True)

---

## Contributing

1. **Fork** the repository.  
2. **Create a branch** for your feature or bug fix.  
3. **Commit** your changes.  
4. **Push** to your branch.  
5. **Create a Pull Request**.  


**Happy coding!**


