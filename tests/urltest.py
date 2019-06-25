#! /usr/bin/env python3
import pycurl
from io import BytesIO

import os
import sys

# import database library
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from vagrant.models import User, Base, Catagory, Item

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# connect to database
engine = create_engine('sqlite:///../catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


address = input(
    "enter address, if left blank it will be set to 'http://localhost:8000':")
if address == '':
    address = 'http://localhost:8000'


def testUrl(path, output):
    # Updated to use pycurl to address this issue:
    # https://grokbase.com/t/python/python-list/098b58yc9v/httplib-incredibly-slow
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, address+path)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()

    content = buffer.getvalue().decode('iso-8859-1')
    if content == output:
        return True
    return False


def oneVar(path, output, testnum=1, loops=5):
    failcheck = False
    for var1 in range(0, loops-1):
        testpath = path.format(var1)
        testoutput = output.format(var1)
        if not testUrl(testpath, testoutput):
            failcheck = True
    if not failcheck:
        print("Test {} success!".format(testnum))


def twoVar(path, output, testnum=1, loops=5):
    failcheck = False
    for var1 in range(0, loops-1):
        for var2 in range(0, loops-1):
            # Output reverses var order for format of the phrases
            testpath = path.format(var1, var2)
            testoutput = output.format(var2, var1)
            if not testUrl(testpath, testoutput):
                failcheck = True
    if not failcheck:
        print("Test {} success!".format(testnum))


test = [['/catalog/owner/{}', 'View items by owner {}.'],
        ['/catalog/owner/{}/item/{}', 'This is item {} by owner {}.'],
        ['/catalog/owner/{}/item/new', 'Make a new item by {}'],
        ['/catalog/owner/{}/item/{}/edit', 'Edit item {} by owner {}'],
        ['/catalog/owner/{}/item/{}/delete', 'Delete item {} by owner {}'],
        ['/catalog/catagory/{}', 'View items in catagory {}'],
        ['/catalog/catagory/{}/item/{}', 'This is item {} in catagory {}.'],
        ['/catalog/catagory/{}/item/new', 'Make a new item in catagory {}.'],
        ['/catalog/catagory/{}/item/{}/edit', 'Edit item {} in catagory {}.']]

# Run tests for given urls & expected outputs
if testUrl('/catalog/', "Homepage!"):
    print("Test 1 success!")
oneVar(test[0][0], test[0][1], testnum=2)
twoVar(test[1][0], test[1][1], testnum=3)
oneVar(test[2][0], test[2][1], testnum=4)
twoVar(test[3][0], test[3][1], testnum=5)
twoVar(test[4][0], test[4][1], testnum=6)
oneVar(test[5][0], test[5][1], testnum=7)
twoVar(test[6][0], test[6][1], testnum=8)
oneVar(test[7][0], test[7][1], testnum=9)
twoVar(test[8][0], test[8][1], testnum=10)
twoVar(test[9][0], test[9][1], testnum=11)
