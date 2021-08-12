
from api import db

class Product(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),unique=True)
    description=db.Column(db.String(500),nullable=False)
    price=db.Column(db.Float,nullable=False)
    quantity=db.Column(db.Integer,nullable=False)


    def __init__(self,name,description,price,quantity):
        self.name=name
        self.description=description
        self.price=price
        self.quantity=quantity

    def __repr__(self):
        return f'{self.name}'



