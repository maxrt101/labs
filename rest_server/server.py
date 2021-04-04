'''
server.py - endpoints for rest api calls

Defines '/shoe'       [GET, POST]
        '/shoe/<id>'  [GET, PUT, DELETE]

Variables:
  app

Functions:
  init

'''

from flask import Flask, request, redirect, abort, jsonify, url_for

from .db import init as db_init
from .db import db, Shoes, shoe_schema, shoes_schema


app = Flask('rest-sample')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Server init
def init(db_user: str, db_pass: str, db_host: str, db_name: str):
    global app
    app = db_init(app, db_user, db_pass, db_host, db_name)


@app.route('/')
def index():
    return redirect(url_for('get_shoes'), code=302)


@app.errorhandler(404)
def shoe_not_found(e):
    return '<h1>404 Not Found<h1>\n<p>Resource you requested does not exist.</p>', 404


# Endpoints

# Create shoe
@app.route('/shoe', methods=['POST'])
def add_shoe():
    new_shoe = Shoes(
        int(request.json['size']),
        request.json['shoes_type'],
        request.json['manufacturer'],
        request.json['model']
    )

    db.session.add(new_shoe)
    db.session.commit()

    return shoe_schema.jsonify(new_shoe)


# Get all shoes
@app.route('/shoe', methods=['GET'])
def get_shoes():
    shoes = Shoes.query.all()
    result = shoes_schema.dump(shoes)
    return jsonify(result)


# Get shoe
@app.route('/shoe/<id>', methods=['GET'])
def get_shoe(id):
    shoe = Shoes.query.get(id)
    if shoe is None:
        abort(404)
    return shoe_schema.jsonify(shoe)


# Update shoe
@app.route('/shoe/<id>', methods=['PUT'])
def update_shoe(id):
    shoe = Shoes.query.get(id)
    if shoe is None:
        abort(404)

    shoe.size         = int(request.json['size'])    if 'size' in request.json else shoe.size
    shoe.shoes_type   = request.json['shoes_type']   if 'shoes_type' in request.json else shoe.shoes_type
    shoe.manufacturer = request.json['manufacturer'] if 'manufacturer' in request.json else shoe.manufacturer
    shoe.model        = request.json['model']        if 'model' in request.json else shoe.model

    db.session.commit()
    return shoe_schema.jsonify(shoe)


# Delete shoe
@app.route('/shoe/<id>', methods=['DELETE'])
def delete_shoe(id):
    shoe = Shoes.query.get(id)
    if shoe is None:
        abort(404)
    db.session.delete(shoe)
    db.session.commit()

    return shoe_schema.jsonify(shoe)

