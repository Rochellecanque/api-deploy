from flask import Flask
import sqlalchemy
# import os
# from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@127.0.0.1:5432/bookshelf'
engine = sqlalchemy.create_engine('postgresql://postgres:postgres@127.0.0.1:5432/bookshelf')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'thisisthesecretkey'