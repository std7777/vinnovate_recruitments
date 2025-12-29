from flask import request, jsonify
from database import get_db
from jwt_utils import generate_token

#insecure handling of credentials. URL is visible everywhere on the logs
def login():
    username = request.args.get("username")
    password = request.args.get("password")

    db = get_db()
    cursor = db.cursor()

    # ❌ SQL Injection
    query = f"SELECT username, role FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)

    user = cursor.fetchone()

    if user:
        token = generate_token(user[0], user[1])
        return jsonify({"token": token})

    return jsonify({"error": "Invalid credentials"})

# Very important audit note (you can write this)
#
# Credentials sent via GET parameters
#
# Vulnerable to SQL Injection
#
# No password hashing
#
# No rate limiting