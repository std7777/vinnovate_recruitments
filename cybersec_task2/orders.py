from flask import request
from database import get_db

def place_order():
    user = request.args.get("user")
    product = request.args.get("product")

    db = get_db()
    cursor = db.cursor()

    # ❌ No validation / auth
    cursor.execute(
        f"INSERT INTO orders(user, product) VALUES('{user}', '{product}')"
    )
    db.commit()

    return {"status": "order placed"}
