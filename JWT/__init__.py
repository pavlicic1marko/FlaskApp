from flask import Flask, request, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# database location ///- this folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite'
app.config['SECRET_KEY']='004f2af45d3a4e161a7dd2d17fdae47f'
# create database instance
db = SQLAlchemy()
db.init_app(app)

from JWT import routs


