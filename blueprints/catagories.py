#! /usr/bin/env python3
from flask import Blueprint
catagory = Blueprint('catagory', __name__)


@catagory.route('/<int:catagory_id>')
def viewAll_catagory(catagory_id):
  return 'View items in catagory {}'.format(catagory_id)


@catagory.route('/<int:catagory_id>/item/<int:item_id>')
def viewItem_catagory(catagory_id, item_id):
  return 'This is item {} in catagory {}.'.format(item_id, catagory_id)


@catagory.route('/<int:catagory_id>/item/new')
def newItem_catagory(catagory_id):
  return 'Make a new item in catagory {}.'.format(catagory_id)


@catagory.route('/<int:catagory_id>/item/<int:item_id>/edit')
def editItem_catagory(catagory_id, item_id):
  return 'Edit item {} in catagory {}.'.format(item_id, catagory_id)


@catagory.route('/<int:catagory_id>/item/<int:item_id>/delete')
def deleteItem_catagory(catagory_id, item_id):
  return 'Delete item {} in catagory {}.'.format(item_id, catagory_id)