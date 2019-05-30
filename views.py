#! /usr/bin/env python3
from flask import Blueprint, Flask, request, render_template, url_for
app = Flask(__name__)

# import database library
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Base, Catagory, Item

# connect to database
engine = create_engine('sqlite:///catalog.db?check_same_thread=False')
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


@app.route('/catalog/catagory/<string:catagory>', methods=['GET'])
def viewAll_catagory(catagory):
    items = session.query(Item).filter_by(catagory=catagory).all()
    if request.method == 'GET':
        return render_template('viewcatagory.html', catagory=catagory, items=items)


@app.route('/catalog/item/<string:item_name>', methods=['GET'])
def viewItem(item_name):
    item = session.query(Item).filter_by(name=item_name).first()
    if request.method == 'GET':
        return render_template('viewitem.html', item=item)


@app.route('/catalog/item/new', methods=['GET', 'POST'])
def newItem():
    if request.method == 'GET':
        return 'Make a new item.'
    if request.method == 'POST':
        return ''


@app.route('/catalog/item/<string:item_name>/edit', methods=['GET', 'PATCH'])
def editItem(item_name):
    item = session.query(Item).filter_by(name=item_name).first()
    if request.method == 'GET':
        return 'Edit item {}.'.format(item.name)
    if request.method == 'PATCH':
        return ''


@app.route('/catalog/item/<string:item_name>/delete', methods=['GET', 'DELETE'])
def deleteItem(item_name):
    item = session.query(Item).filter_by(name=item_name).first()
    if request.method == 'GET':
        return 'Delete item {}.'.format(item.name)
    if request.method == 'DELETE':
        return ''


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
