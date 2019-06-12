#! /usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for
from flask import make_response, flash, Blueprint
from flask import session as login_session

# import oauth
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError

import string
import random
import httplib2
import json
import requests

# import db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Base, Catagory, Item

# connect to db
engine = create_engine('sqlite:///catalog.db?check_same_thread=False')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def checkLogin(local=False, crudItem=None):
    """
    If local is set to False (default), then checklogin checks of there is a
    user signed in. If local is set to True, checklogin also checks if the
    current user is the creator of the item 'crudItem'.

    Inputs:
      local: Boolean
      crudItem: SQLAlchemy query
    """
    if 'username' not in login_session:
        return False

    if local:
        try:
            if crudItem.owner != login_session['username']:
                return False
            else:
                return True
        except AttributeError:
            if crudItem[0].owner != login_session['username']:
                return False
            else:
                return True
    else:
        return True


def sqlItemSearch(checkby, checkVar):
    """
    Runs a search of the Item table, filtered by either 'name', 'owner', 
    or 'catagory'.
    Inputs:
        checkby: String
        checkVar: String
    Outputs:
        crudItem: SQLAlchemy query
    """
    assert type(checkby) == str, 'checkby must be a string'
    assert checkby in [
        'name', 'owner', 'catagory'], 'checkby can only be "name", "owner", or "catagory"'
    assert type(checkVar) == str, 'checkVar must be a string'

    search = session.query(Item)
    if checkby.lower() == 'name':
        crudItem = search.filter_by(name=checkVar).first()
    elif checkby.lower() == 'owner':
        crudItem = search.filter_by(owner=checkVar).all()
    elif checkby.lower() == 'catagory':
        crudItem = search.filter_by(catagory=checkVar).all()

    return crudItem
