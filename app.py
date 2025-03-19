from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json

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

    return jsonify({"message": "Signup successful"}), 200

if __name__ == "__main__":
    app.run(debug=True)

