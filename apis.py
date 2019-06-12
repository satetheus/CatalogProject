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
from controls import sqlItemSearch

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


@api.route('/all')
def api_showAll():
    items = session.query(Item).all()
    return jsonify(allItems=[i.serialize for i in items])


@api.route('/owner/<string:owner_name>')
def api_showOwner(owner_name):
    items = sqlItemSearch('owner', owner_name)
    return jsonify(ownerItems=[i.serialize for i in items])


@api.route('/catagory/<string:catagory_name>')
def api_showCatagory(catagory_name):
    items = sqlItemSearch('catagory', catagory_name)
    return jsonify(catagoryItems=[i.serialize for i in items])


@api.route('/item/<string:item_name>')
def api_showItem(item_name):
    item = sqlItemSearch('name', item_name)
    return jsonify(item.serialize)