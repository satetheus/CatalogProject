#! /usr/bin/env python3
from flask import Blueprint, Flask, request, render_template
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
  return render_template('homepage.html')


@app.route('/catalog/owner/<string:owner>', methods=['GET'])
def viewAll_owner(owner):
    items = session.query(Item).filter_by(owner=owner).all()
    if request.method == 'GET':
        return render_template('viewowner.html', owner=owner, items=items)


@app.route('/catalog/catagory/<int:catagory>', methods=['GET'])
def viewAll_catagory(catagory):
    catagory = session.query(Catagory).filter_by(id=catagory).first().name
    if request.method == 'GET':
        return 'View items in catagory {}'.format(catagory)


@app.route('/catalog/item/<int:item_id>', methods=['GET'])
def viewItem(item_id):
    item = session.query(Item).filter_by(id=item_id).first()
    catagory = session.query(Catagory).filter_by(id=item.catagory).first().name
    if request.method == 'GET':
        return 'This is item {} in catagory {}.'.format(item.name, catagory)


@app.route('/catalog/item/new', methods=['GET', 'POST'])
def newItem():
    if request.method == 'GET':
        return 'Make a new item.'
    if request.method == 'POST':
        return ''


@app.route('/catalog/item/<int:item_id>/edit', methods=['GET', 'PATCH'])
def editItem(item_id):
    item = session.query(Item).filter_by(id=item_id).first()
    catagory = session.query(Catagory).filter_by(id=item.catagory).first().name
    if request.method == 'GET':
        return 'Edit item {} in catagory {}.'.format(item.name, catagory)
    if request.method == 'PATCH':
        return ''


@app.route('/catalog/item/<int:item_id>/delete', methods=['GET', 'DELETE'])
def deleteItem(item_id):
    item = session.query(Item).filter_by(id=item_id).first()
    catagory = session.query(Catagory).filter_by(id=item.catagory).first().name
    if request.method == 'GET':
        return 'Delete item {} in catagory {}.'.format(item.name, catagory)
    if request.method == 'DELETE':
        return ''


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
