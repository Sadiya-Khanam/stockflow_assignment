from flask import request, jsonify
from sqlalchemy.exc import IntegrityError
from decimal import Decimal
from app import app, db
from models import Product, Inventory

@app.route('/api/products', methods=['POST'])
def create_product():
    data = request.get_json()

    # Required fields
    required = ['name', 'sku', 'price', 'warehouse_id', 'initial_quantity']
    missing = [f for f in required if f not in data]
    if missing:
        return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400

    # Check if SKU already exists
    if Product.query.filter_by(sku=data['sku']).first():
        return jsonify({"error": "SKU already exists"}), 400

    try:
        # Add product
        product = Product(
            name=data['name'],
            sku=data['sku'],
            price=Decimal(str(data['price']))
        )
        db.session.add(product)
        db.session.flush()  # get product.id

        # Add inventory for that product
        inventory = Inventory(
            product_id=product.id,
            warehouse_id=data['warehouse_id'],
            quantity=data['initial_quantity']
        )
        db.session.add(inventory)
        db.session.commit()

        return jsonify({"message": "Product created", "product_id": product.id}), 201

    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Something went wrong", "details": str(e)}), 500
