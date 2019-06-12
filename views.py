#! /usr/bin/env python3
from flask import Blueprint, Flask, request, render_template, url_for, redirect, flash
from flask import session as login_session

# import other project files
from models import User, Base, Catagory, Item
from controls import checkLogin, sqlItemSearch, crud_create, crud_edit, crud_delete
from auth import auth
from apis import api

app = Flask(__name__)
app.register_blueprint(auth)
app.register_blueprint(api, url_prefix='/api')

# import database library
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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
    items = sqlItemSearch('owner', owner)
    if request.method == 'GET' and checkLogin():
        return render_template('viewowner.html', owner=owner, items=items)
    else:
        return redirect(url_for('homepage'))


@app.route('/catalog/catagory/<string:catagory>', methods=['GET'])
def viewAll_catagory(catagory):
    items = sqlItemSearch('catagory', catagory)
    if request.method == 'GET':
        return render_template('viewcatagory.html', catagory=catagory, items=items)


@app.route('/catalog/item/<string:item_name>', methods=['GET'])
def viewItem(item_name):
    item = sqlItemSearch('name', item_name)
    if request.method == 'GET':
        return render_template('viewitem.html', item=item)


@app.route('/catalog/item/new', methods=['GET', 'POST'])
def newItem():
    if checkLogin():
        catagories = session.query(Catagory).all()
        if request.method == 'GET':
            return render_template('newitem.html', catagories=catagories)
        if request.method == 'POST':
            crud_create()
            return redirect(url_for('viewAll_owner', owner=new_item.owner))
    else:
        return redirect(url_for('auth.login'))


@app.route('/catalog/item/<string:item_name>/edit', methods=['GET', 'POST'])
def editItem(item_name):
    item = sqlItemSearch('name', item_name)
    if checkLogin(True, item):
        catagories = session.query(Catagory).all()
        if request.method == 'GET':
            return render_template('edititem.html', item=item, catagories=catagories)
        if request.method == 'POST':
            crud_edit(item)
            return redirect(url_for('viewAll_owner', owner=item.owner))
    else:
        return redirect(url_for('viewAll_owner', owner=item.owner))


@app.route('/catalog/item/<string:item_name>/delete', methods=['GET', 'POST'])
def deleteItem(item_name):
    item = sqlItemSearch('name', item_name)
    if checkLogin(True, item):
        if request.method == 'GET':
            return render_template('deleteitem.html', item=item)
        if request.method == 'POST':
            crud_delete(item)
            return redirect(url_for('viewAll_catagory', catagory=item.catagory))
    else:
        return redirect(url_for('viewAll_catagory', catagory=item.catagory))


if __name__ == '__main__':
    app.debug = True
    app.secret_key = "african or european?"
    app.run(host='0.0.0.0', port=8000)
