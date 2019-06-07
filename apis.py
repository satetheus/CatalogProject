#! /usr/bin/env python3
from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask import make_response, flash, Blueprint
from flask import session as login_session

#import oauth
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError

import httplib2
import json
import requests

# import database library
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Base, Catagory, Item

# connect to database
engine = create_engine('sqlite:///catalog.db?check_same_thread=False')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

api = Blueprint('api', __name__, template_folder='templates')


#/api/all
@api.route('/all')
def api_showAll():
    items = session.query(Item).all()
    return jsonify(allItems=[i.serialize for i in items])


#/api/owner/<string:owner_name>
@api.route('/owner/<string:owner_name>')
def api_showOwner(owner_name):
    items = session.query(Item).filter_by(owner=owner_name).all()
    return jsonify(ownerItems=[i.serialize for i in items])


#/api/catagory/<string:catagory_name>
@api.route('/catagory/<string:catagory_name>')
def api_showCatagory(catagory_name):
    items = session.query(Item).filter_by(catagory=catagory_name).all()
    return jsonify(catagoryItems=[i.serialize for i in items])


#/api/item/<string:item_name>
@api.route('/item/<string:item_name>')
def api_showItem(item_name):
    item = session.query(Item).filter_by(name=item_name).first()
    return jsonify(item.serialize)