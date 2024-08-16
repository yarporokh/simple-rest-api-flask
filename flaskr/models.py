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