#! /usr/bin/env python3
from flask import Blueprint, Flask, request, render_template, url_for, redirect, flash
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
    catagories = session.query(Catagory).all()
    if request.method == 'GET':
        return render_template('newitem.html', catagories=catagories)
    if request.method == 'POST':
        new_item = Item(
            name=request.form['name'], 
            catagory=request.form['catagory'],
            owner='Satetheus') # hard coded until authorization is built in.
        session.add(new_item)
        session.commit()
        flash("{} created.".format(new_item.name))
        return redirect(url_for('viewAll_owner', owner=new_item.owner))


@app.route('/catalog/item/<string:item_name>/edit', methods=['GET', 'POST'])
def editItem(item_name):
    item = session.query(Item).filter_by(name=item_name).first()
    catagories = session.query(Catagory).all()
    if request.method == 'GET':
        return render_template('edititem.html', item=item, catagories=catagories)
    if request.method == 'POST':
        if request.form['name']:
            item.name = request.form['name']
        if request.form['catagory']:
            item.catagory = request.form['catagory']
        session.add(item)
        session.commit()
        flash("{} successfully edited.".format(item.name))
        return redirect(url_for('viewAll_owner', owner=item.owner))


@app.route('/catalog/item/<string:item_name>/delete', methods=['GET', 'POST'])
def deleteItem(item_name):
    item = session.query(Item).filter_by(name=item_name).first()
    if request.method == 'GET':
        return render_template('deleteitem.html', item=item)
    if request.method == 'POST':
        return ''


if __name__ == '__main__':
    app.debug = True
    app.secret_key="african or european?"
    app.run(host='0.0.0.0', port=8000)
