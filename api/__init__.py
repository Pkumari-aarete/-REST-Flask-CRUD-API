from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from configparser import ConfigParser

config=ConfigParser()
config.read('config.ini')
SQLALCHEMY_DATABASE_URI=config['DEFAULT']['SQLALCHEMY_DATABASE_URI']

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

from api.controller import home,authenticate