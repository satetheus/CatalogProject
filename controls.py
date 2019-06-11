#! /usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for
from flask import make_response, flash, Blueprint
from flask import session as login_session

#import oauth
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


def checkLogin(local=False, checkby=None, checkVar=None):
    """Checks that user is logged in. If local is set to true, 
    this will check that the session username is the same as 
    the owner of the db item.
    Inputs:
      local: Boolean
      checkby: String
      checkVar: String
    """
    if 'username' not in login_session:
        return False

    if local:
        assert (checkby in [
            'name', 'owner', 'catagory']), "checkby must be 'name', 'owner', or 'catagory'"
        assert (checkVar != None), 'checkVar must not be None'
        print(type(checkVar))
        assert (type(checkVar) == str), 'checkVar must be a string'

        search = session.query(Item)
        if checkby.lower() == 'name':
            crudItem = search.filter_by(name=checkVar).first()
        elif checkby.lower() == 'owner':
            crudItem = search.filter_by(owner=checkVar).all()
        elif checkby.lower() == 'catagory':
            crudItem = search.filter_by(catagory=checkVar).all()

        try:
            if crudItem.owner != login_session['username']:
                return False
            else:
                return crudItem
        except AttributeError:
            if crudItem[0].owner != login_session['username']:
                return False
            else:
                return crudItem
