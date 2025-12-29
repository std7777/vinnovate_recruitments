from flask import jsonify

products = [
    {"id": 1, "name": "Laptop", "price": 1000},
    {"id": 2, "name": "Phone", "price": 500},
]

def list_products():
    return jsonify(products)
