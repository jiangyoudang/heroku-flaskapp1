from flask.ext.restless import APIManager
from sqlalchemy import Column, INTEGER, TEXT

from init import app
from init import db


class Users(db.Model):
    id = Column(INTEGER, primary_key=True)
    name = Column(TEXT, unique=False)
    email = Column(TEXT, unique=True)




###########################

db.create_all()

api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(Users, methods = ['GET', 'POST', 'PUT','DELETE'])
