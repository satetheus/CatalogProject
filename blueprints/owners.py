#! /usr/bin/env python3
from flask import Blueprint, request
owner = Blueprint('owner', __name__)

# import database library
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Base, Catagory, Item

# connect to database
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@owner.route('/<int:owner_id>', methods=['GET'])
def viewAll_owner(owner_id):
    owner = session.query(User).filter_by(id=owner_id).first().name
    if request.method == 'GET':
        return 'View items by owner {}.'.format(owner)


@owner.route('/<int:owner_id>/item/<int:item_id>', methods=['GET'])
def viewItem_owner(owner_id, item_id):
    owner = session.query(User).filter_by(id=owner_id).one().name
    item = session.query(Item).filter_by(id=item_id).one().name
    if request.method == 'GET':
        return 'This is item {} by owner {}.'.format(item, owner)


@owner.route('/<int:owner_id>/item/new', methods=['GET','POST'])
def newItem_owner(owner_id):
    owner = session.query(User).filter_by(id=owner_id).one().name
    if request.method == 'GET':
        return 'Make a new item by {}'.format(owner)
    if request.method == 'POST':
        return ''


@owner.route('/<int:owner_id>/item/<int:item_id>/edit', methods=['GET','PATCH'])
def editItem_owner(owner_id, item_id):
    owner = session.query(User).filter_by(id=owner_id).one().name
    item = session.query(Item).filter_by(id=item_id).one().name
    if request.method == 'GET':
        return 'Edit item {} by owner {}'.format(item, owner)
    if request.method == 'PATCH':
        return ''


@owner.route('/<int:owner_id>/item/<int:item_id>/delete', methods=['GET', 'DELETE'])
def deleteItem_owner(owner_id, item_id):
    owner = session.query(User).filter_by(id=owner_id).one().name
    item = session.query(Item).filter_by(id=item_id).one().name
    if request.method == 'GET':
        return 'Delete item {} by owner {}'.format(item, owner)
    if request.method == 'DELETE':
        return ''