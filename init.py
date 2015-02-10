from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy



app = Flask(__name__, static_url_path='')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/data.db'

db = SQLAlchemy(app)

# db.create_all()
