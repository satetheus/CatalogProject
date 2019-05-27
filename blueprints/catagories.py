#! /usr/bin/env python3
from flask import Blueprint, request
catagory = Blueprint('catagory', __name__)


@catagory.route('/<int:catagory_id>', methods=['GET'])
def viewAll_catagory(catagory_id):
  if request.method == 'GET':
      return 'View items in catagory {}'.format(catagory_id)


@catagory.route('/<int:catagory_id>/item/<int:item_id>', methods=['GET'])
def viewItem_catagory(catagory_id, item_id):
  if request.method == 'GET':
      return 'This is item {} in catagory {}.'.format(item_id, catagory_id)


@catagory.route('/<int:catagory_id>/item/new', methods=['GET','POST'])
def newItem_catagory(catagory_id):
  if request.method == 'GET':
      return 'Make a new item in catagory {}.'.format(catagory_id)
  if request.method == 'POST':
      return ''


@catagory.route('/<int:catagory_id>/item/<int:item_id>/edit', methods=['GET','PATCH'])
def editItem_catagory(catagory_id, item_id):
  if request.method == 'GET':
      return 'Edit item {} in catagory {}.'.format(item_id, catagory_id)
  if request.method == 'PATCH':
      return ''


@catagory.route('/<int:catagory_id>/item/<int:item_id>/delete', methods=['GET','DELETE'])
def deleteItem_catagory(catagory_id, item_id):
  if request.method == 'GET':
      return 'Delete item {} in catagory {}.'.format(item_id, catagory_id)
  if request.method == 'DELETE':
      return ''