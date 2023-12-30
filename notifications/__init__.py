from flask import Flask, request, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# database location ///- this folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notifications.sqlite'
# create database instance
db = SQLAlchemy()
db.init_app(app)

from notifications import routs


