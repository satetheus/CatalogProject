#! /usr/bin/env python3
from flask import Blueprint
owner = Blueprint('owner', __name__)


@owner.route('/<int:owner_id>')
def viewAll_owner(owner_id):
  return 'View items by owner {}.'.format(owner_id)


@owner.route('/<int:owner_id>/item/<int:item_id>')
def viewItem_owner(owner_id, item_id):
  return 'This is item {} by owner {}.'.format(item_id, owner_id)


@owner.route('/<int:owner_id>/item/new')
def newItem_owner(owner_id):
  return 'Make a new item by {}'.format(owner_id)


@owner.route('/<int:owner_id>/item/<int:item_id>/edit')
def editItem_owner(owner_id, item_id):
  return 'Edit item {} by owner {}'.format(item_id, owner_id)


@owner.route('/<int:owner_id>/item/<int:item_id>/delete')
def deleteItem_owner(owner_id, item_id):
  return 'Delete item {} by owner {}'.format(item_id, owner_id)