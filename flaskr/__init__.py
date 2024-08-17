from flask import Flask
from flaskr.db import db
from flaskr.products import products_bp
from flaskr.customers import customers_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


with app.app_context():
    db.create_all()

app.register_blueprint(products_bp)
app.register_blueprint(customers_bp)

if __name__ == '__main__':
    app.run()
