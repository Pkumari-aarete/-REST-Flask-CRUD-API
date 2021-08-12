from api.model.product import Product
from api.schema.productschema import ProductSchema
from api import app
from api import db
from api.controller.authenticate import token_required
from flask import request,jsonify


product_schema=ProductSchema()
products_schema=ProductSchema(many=True)


@app.route("/",methods=['GET'])
@token_required
def get_product():
    all_products=Product.query.all()
    result=products_schema.dump(all_products)
    return jsonify(result)


@app.route("/<int:id>",methods=['GET'])
@token_required
def get_product_by_id(id):
    product=Product.query.get_or_404(id)
    result=product_schema.dump(product)
    return jsonify(result)
    #return product_schema.jsonify(product)


@app.route("/",methods=['POST'])
@token_required
def add_product():
    name=request.json['name']
    description=request.json['description']
    price=request.json['price']
    quantity=request.json['quantity']

    new_product=Product(name,description,price,quantity)
    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product),201


@app.route("/<id>",methods=['PUT'])
@token_required
def update_product(id):
    product=Product.query.get(id)
    product.name=request.json['name']
    product.description=request.json['description']
    product.price=request.json['price']
    product.quantity=request.json['quantity']

    db.session.commit()
    return product_schema.jsonify(product)


@app.route("/<id>",methods=['DELETE'])
@token_required
def delete_product(id):
    product=Product.query.get(id)
    db.session.delete(product)
    db.session.commit()

    return product_schema.jsonify(product)

@app.errorhandler(404)
def not_found(error):
    return jsonify({'message':'record not found'})


