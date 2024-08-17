from sqlalchemy.dialects.sqlite import JSON
from sqlalchemy.ext.mutable import MutableList

from flaskr.db import db


class BaseModel(db.Model):
    __abstract__ = True

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)


class Customer(BaseModel):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    product_ids = db.Column(MutableList.as_mutable(JSON), nullable=True, default=[])

    def __str__(self):
        return f'Customer: id - {self.id}, name - {self.name}, product_ids - {self.product_ids}'

    @property
    def products(self):
        if self.product_ids:
            return Product.query.filter(Product.id.in_(self.product_ids)).all()
        return []

    def add_product(self, product):
        print(product.id)
        self.product_ids.append(product.id)
        print(self.product_ids)
        self.save()


class Product(BaseModel):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False, default=0)

    __table_args__ = (
        db.CheckConstraint('price >= 0.0'),
    )

    def __str__(self):
        return f'Product: id - {self.id}, name - {self.name}, price - {self.price}'