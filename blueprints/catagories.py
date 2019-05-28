#! /usr/bin/env python3
from flask import Blueprint, request
catagory = Blueprint('catagory', __name__)

# import database library
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Base, Catagory, Item

# connect to database
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@catagory.route('/<int:catagory_id>', methods=['GET'])
def viewAll_catagory(catagory_id):
    catagory = session.query(Catagory).filter_by(id=catagory_id).first().name
    if request.method == 'GET':
        return 'View items in catagory {}'.format(catagory)


@catagory.route('/<int:catagory_id>/item/<int:item_id>', methods=['GET'])
def viewItem_catagory(catagory_id, item_id):
    catagory = session.query(Catagory).filter_by(id=catagory_id).first().name
    item = session.query(Item).filter_by(id=item_id).first().name
    if request.method == 'GET':
        return 'This is item {} in catagory {}.'.format(item, catagory)


@catagory.route('/<int:catagory_id>/item/new', methods=['GET', 'POST'])
def newItem_catagory(catagory_id):
    catagory = session.query(Catagory).filter_by(id=catagory_id).first().name
    if request.method == 'GET':
        return 'Make a new item in catagory {}.'.format(catagory)
    if request.method == 'POST':
        return ''


@catagory.route('/<int:catagory_id>/item/<int:item_id>/edit', methods=['GET', 'PATCH'])
def editItem_catagory(catagory_id, item_id):
    catagory = session.query(Catagory).filter_by(id=catagory_id).first().name
    item = session.query(Item).filter_by(id=item_id).first().name
    if request.method == 'GET':
        return 'Edit item {} in catagory {}.'.format(item, catagory)
    if request.method == 'PATCH':
        return ''


@catagory.route('/<int:catagory_id>/item/<int:item_id>/delete', methods=['GET', 'DELETE'])
def deleteItem_catagory(catagory_id, item_id):
    catagory = session.query(Catagory).filter_by(id=catagory_id).first().name
    item = session.query(Item).filter_by(id=item_id).first().name
    if request.method == 'GET':
        return 'Delete item {} in catagory {}.'.format(item, catagory)
    if request.method == 'DELETE':
        return ''
