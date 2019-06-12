#! /usr/bin/env python3
from flask import Flask, render_template, request, jsonify, Blueprint

import json
from controls import sqlItemSearch, showAllItems

api = Blueprint('api', __name__, template_folder='templates')


@api.route('/all')
def api_showAll():
    items = showAllItems()
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