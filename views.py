#! /usr/bin/env python3
from blueprints.catagories import catagory
from blueprints.owners import owner
from flask import Blueprint, Flask
app = Flask(__name__)

# import database library
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Base, Catagory, Item

# connect to database
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/catalog/')
def homepage():
  return "Homepage!"

app.register_blueprint(owner, url_prefix='/catalog/owner')
app.register_blueprint(catagory, url_prefix='/catalog/catagory')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
