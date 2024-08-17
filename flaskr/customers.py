from flask import Blueprint, jsonify, request

from flaskr.models import Customer, Product

customers_bp = Blueprint('customers', __name__, url_prefix='/customers')

@customers_bp.route('/', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([str(customer) for customer in customers])

@customers_bp.route('/', methods=['POST'])
def create_customer():
    name = request.json.get('name')
    customer = Customer(name=name)
    customer.save()
    return jsonify(str(customer))

@customers_bp.route('/<int:id>', methods=['GET'])
def get_customer(id):
    customer = Customer.query.get_or_404(id)
    return jsonify(str(customer))

@customers_bp.route('<int:customer_id>/add-product/<int:product_id>', methods=['GET'])
def add_product(customer_id, product_id):
    customer = Customer.query.get_or_404(customer_id)
    product = Product.query.get_or_404(product_id)
    customer.add_product(product)
    return jsonify(str(customer))

@customers_bp.route('/<int:id>/products', methods=['GET'])
def get_customer_products(id):
    customer = Customer.get_by_id(id)
    products = [str(product) for product in customer.products]
    return products