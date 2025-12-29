from flask import Flask, request, jsonify
import auth, products, orders
from jwt_utils import decode_token

app = Flask(__name__)

@app.route("/login")
def login():
    return auth.login()

@app.route("/products")
def products_list():
    return products.list_products()

@app.route("/order")
def order():
    return orders.place_order()

@app.route("/admin/orders")
def admin_orders():
    user = None
    token = request.headers.get("Authorization")
    if token:
        user = decode_token(token)

    if user and user.get("role") == "admin":
        return jsonify({"orders": "ALL ORDERS"})

    return jsonify({"error": "Unauthorized"}), 401


if __name__ == "__main__":
    print("🚀 E-commerce API running on http://127.0.0.1:5000")
    app.run(debug=True)
