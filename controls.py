#! /usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for
from flask import make_response, flash, Blueprint
from flask import session as login_session

# import oauth
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError

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
    Outputs:
        Boolean
      
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


def showAllItems(separate=False):
    """
    Returns the entire Item table. If separate is set to True, the 
    items are returned as a dictionary separated by catagory.
    Inputs:
        separate (optional): Boolean, defualts to False
    Outputs:
        items: List if separate is False,
               Dict if separate is True
    """
    items = session.query(Item).order_by(Item.catagory.desc())
    if separate:
        separate_items = {}
        catagories = session.query(Catagory).all()
        for catagory in catagories:
            separate_items[catagory.name] = []
        for item in items:
            separate_items[item.catagory].append(item)
        items = separate_items
    return items



def crud_create():
    """
    Creates a new item in the Item table based on the form data & 
    the current session.
    Inputs:
        None
    Outputs:
        None
    """
    new_item = Item(
        name=request.form['name'],
        catagory=request.form['catagory'],
        owner=login_session['username'])
    session.add(new_item)
    session.commit()
    flash("{} created.".format(new_item.name))
    return new_item


def crud_edit(item):
    """
    Edits the input item based on the form data.
    Inputs:
        item: a sqlalchemy queried item
    Outputs:
        None
    """
    if request.form['name']:
        item.name = request.form['name']
    if request.form['catagory']:
        item.catagory = request.form['catagory']
    session.add(item)
    session.commit()
    flash("{} successfully edited.".format(item.name))


def crud_delete(item):
    """
    Deletes the input item from the table.
    Inputs:
        item: a sqlalchemy queried item
    Outputs:
        None
    """
    session.delete(item)
    session.commit()
    flash("{} deleted.".format(item.name))


def createUser(login_session):
    """
    Creates a new user based on the current login session.
    Inputs:
        login_session: dict
    Outputs:
        user.id: int
    """
    newUser = User(name=login_session['username'], email=login_session['email'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(name=login_session['username']).first()
    return user.id
