from flask import Blueprint, request, jsonify

from flaskr.models import Product

products_bp = Blueprint('products', __name__, url_prefix='/products')

@products_bp.route('/', methods=['GET'])
def get_all_products():
    products = Product.query.all()
    return jsonify([str(product) for product in products])

@products_bp.route('/', methods=['POST'])
def create_product():
    try:
        name = request.json.get('name')
        if not name:
            return jsonify({"error": "Name is required"}), 400

        price = request.json.get('price')
        try:
            price = float(price)
        except (TypeError, ValueError):
            return jsonify({"error": "Invalid price value"}), 400

        product = Product(name=name, price=price)
        product.save()
        return jsonify(str(product)), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@products_bp.route('/<int:id>', methods=['GET'])
def get_product_by_id(id):
    product = Product.get_by_id(id)
    return jsonify(str(product))

@products_bp.route('/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.get_by_id(id)
    product.delete()
    return jsonify({'message': f'Product {id} deleted'})
