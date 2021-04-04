'''
db.py - initializes database and defines schemas for working with `shoes` table
Important: mysql-connector does not support caching_sha2_password auth plugin,
           which is set by default starting from mysql 8.0.
           For mysql-connector to work, you need a user with mysql_native_password
           auth plugin. You can change auth plugin for a given user using this query:

ALTER USER 'username'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';

Variables:
  db
  shoe_schema
  shoes_schema

Functions:
  init

Classes:
  Shoes

'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
ma = Marshmallow()


class Shoes(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, unique=True, nullable=False)
    size = db.Column(db.Integer, nullable=False)
    shoes_type = db.Column(db.Enum('SPORT', 'SUMMER', 'WINTER'), nullable=False)
    manufacturer = db.Column(db.Text, nullable=False)
    model = db.Column(db.Text, nullable=False)

    def __init__(self, size: int, shoes_type: str, manufacturer: str, model: str):
        self.size = size
        self.shoes_type = shoes_type
        self.manufacturer = manufacturer
        self.model = model

    def __str__(self) -> str:
        return f'Shoe({self.size}, {self.shoes_type}, {self.manufacturer})'

    def __repr__(self) -> str:
        return f'<Shoe {self.id}>'


class ShoesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'size', 'shoes_type', 'manufacturer', 'model')


shoe_schema = ShoesSchema()
shoes_schema = ShoesSchema(many=True)


def init(app: Flask, db_user: str, db_pass: str, db_host: str, db_name: str) -> Flask:
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        f'mysql+mysqlconnector://{db_user}:{db_pass}@{db_host}/{db_name}?auth_plugin=mysql_native_password'
    db.init_app(app)
    ma.init_app(app)
    
    # Created table `shoes`, if not exists
    app.app_context().push()
    db.create_all()
    
    return app

