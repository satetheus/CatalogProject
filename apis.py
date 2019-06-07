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
  return 'all items'


#/api/owner/<string:owner_name>
@api.route('/owner/<string:owner_name>')
def api_showOwner(owner_name):
  return 'all items by {}'.format(owner_name)


#/api/catagory/<string:catagory_name>
@api.route('/owner/<string:catagory_name>')
def api_showOwner(catagory_name):
  return 'all items in {}'.format(catagory_name)



#/api/item/<string:item_name>
@api.route('/item/<string:item_name>')
def api_showOwner(item_name):
  return '{}'.format(item_name)


