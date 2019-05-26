#! /usr/bin/env python3
from flask import Flask
app = Flask(__name__)

@app.route('/catalog')
@app.route('/')
def homepage():
  return "Homepage!"


@app.route('/catalog/owner/<int:owner_id>')
def viewAll_owner(owner_id):
  return 'View items by owner {}.'.format(owner_id)


@app.route('/catalog/owner/<int:owner_id>/item/<int:item_id>')
def viewItem_owner(owner_id, item_id):
  return 'This is item {} by owner {}.'.format(item_id, owner_id)


@app.route('/catalog/owner/<int:owner_id>/item/new')
def newItem_owner(owner_id):
  return 'Make a new item by {}'.format(owner_id)


@app.route('/catalog/owner/<int:owner_id>/item/<int:item_id>/edit')
def editItem_owner(owner_id, item_id):
  return 'Edit item {} by owner {}'.format(item_id, owner_id)


@app.route('/catalog/owner/<int:owner_id>/item/<int:item_id>/delete')
def deleteItem_owner(owner_id, item_id):
  return 'Delete item {} by owner {}'.format(item_id, owner_id)


@app.route('/catalog/catagory/<int:catagory_id>')
def viewAll_catagory(catagory_id):
  return 'View items in catagory {}'.format(catagory_id)


@app.route('/catalog/catagory/<int:catagory_id>/item/<int:item_id>')
def viewItem_catagory(catagory_id, item_id):
  return 'This is item {} in catagory {}.'.format(item_id, catagory_id)


@app.route('/catalog/catagory/<int:catagory_id>/item/new')
def newItem_catagory(catagory_id):
  return 'Make a new item in catagory {}.'.format(catagory_id)


@app.route('/catalog/catagory/<int:catagory_id>/item/<int:item_id>/edit')
def editItem_catagory(catagory_id, item_id):
  return 'Edit item {} in catagory {}.'.format(item_id, catagory_id)


@app.route('/catalog/catagory/<int:catagory_id>/item/<int:item_id>/delete')
def deleteItem_catagory(catagory_id, item_id):
  return 'Delete item {} in catagory {}.'.format(item_id, catagory_id)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)