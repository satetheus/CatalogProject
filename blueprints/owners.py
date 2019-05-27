#! /usr/bin/env python3
from flask import Blueprint, request
owner = Blueprint('owner', __name__)


@owner.route('/<int:owner_id>', methods=['GET'])
def viewAll_owner(owner_id):
  if request.method == 'GET':
      return 'View items by owner {}.'.format(owner_id)


@owner.route('/<int:owner_id>/item/<int:item_id>', methods=['GET'])
def viewItem_owner(owner_id, item_id):
  if request.method == 'GET':
      return 'This is item {} by owner {}.'.format(item_id, owner_id)


@owner.route('/<int:owner_id>/item/new', methods=['GET','POST'])
def newItem_owner(owner_id):
  if request.method == 'GET':
      return 'Make a new item by {}'.format(owner_id)


@owner.route('/<int:owner_id>/item/<int:item_id>/edit', methods=['GET','PATCH'])
def editItem_owner(owner_id, item_id):
  if request.method == 'GET':
      return 'Edit item {} by owner {}'.format(item_id, owner_id)


@owner.route('/<int:owner_id>/item/<int:item_id>/delete', methods=['GET', 'DELETE'])
def deleteItem_owner(owner_id, item_id):
  if request.method == 'GET':
      return 'Delete item {} by owner {}'.format(item_id, owner_id)