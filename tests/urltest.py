#! /usr/bin/env python3
from httplib2 import Http
import sys

address = input(
    "Please enter the address of the server you want to access, \n If left blank the connection will be set to 'http://localhost:8000':   ")
if address == '':
    address = 'http://localhost:8000'


def testUrl(path, output):
    # get output
    h = Http()
    url = address + path
    _, content = h.request(url, 'GET')
    content = content.decode('utf-8')

    if content == output:
        return True
    return False


if testUrl('/catalog', "Homepage!"):
    print("Test 1 success!")


failcheck = False
for owner_id in range(5):
    path = '/catalog/owner/{}'.format(owner_id)
    output = 'View items by owner {}.'.format(owner_id)
    if not testUrl(path, output):
        failcheck = True
if not failcheck:
    print("Test 2 success!")


failcheck = False
for owner_id in range(5):
    for item_id in range(5):
        path = '/catalog/owner/{}/item/{}'.format(owner_id, item_id)
        output = 'This is item {} by owner {}.'.format(item_id, owner_id)
        if not testUrl(path, output):
            failcheck = True
if not failcheck:
    print("Test 3 success!")


failcheck = False
for owner_id in range(5):
    path = '/catalog/owner/{}/item/new'.format(owner_id)
    output = 'Make a new item by {}'.format(owner_id)
    if not testUrl(path, output):
        failcheck = True
if not failcheck:
    print("Test 4 success!")


failcheck = False
for owner_id in range(5):
    for item_id in range(5):
        path = '/catalog/owner/{}/item/{}/edit'.format(owner_id, item_id)
        output = 'Edit item {} by owner {}'.format(item_id, owner_id)
        if not testUrl(path, output):
            failcheck = True
if not failcheck:
    print("Test 5 success!")


failcheck = False
for owner_id in range(5):
    for item_id in range(5):
        path = '/catalog/owner/{}/item/{}/delete'.format(owner_id, item_id)
        output = 'Delete item {} by owner {}'.format(item_id, owner_id)
        if not testUrl(path, output):
            failcheck = True
if not failcheck:
    print("Test 6 success!")


failcheck = False
for catagory_id in range(5):
    path = '/catalog/catagory/{}'.format(catagory_id)
    output = 'View items in catagory {}'.format(catagory_id)
    if not testUrl(path, output):
        failcheck = True
if not failcheck:
    print("Test 7 success!")


failcheck = False
for catagory_id in range(5):
    for item_id in range(5):
        path = '/catalog/catagory/{}/item/{}'.format(catagory_id, item_id)
        output = 'This is item {} in catagory {}.'.format(item_id, catagory_id)
        if not testUrl(path, output):
            failcheck = True
if not failcheck:
    print("Test 8 success!")


failcheck = False
for catagory_id in range(5):
    path = '/catalog/catagory/{}/item/new'.format(catagory_id)
    output = 'Make a new item in catagory {}.'.format(catagory_id)
    if not testUrl(path, output):
        failcheck = True
if not failcheck:
    print("Test 9 success!")


failcheck = False
for catagory_id in range(5):
    for item_id in range(5):
        path = '/catalog/catagory/{}/item/{}/edit'.format(catagory_id, item_id)
        output = 'Edit item {} in catagory {}.'.format(item_id, catagory_id)
        if not testUrl(path, output):
            failcheck = True
if not failcheck:
    print("Test 10 success!")


failcheck = False
for catagory_id in range(5):
    for item_id in range(5):
        path = '/catalog/catagory/{}/item/{}/delete'.format(
            catagory_id, item_id)
        output = 'Delete item {} in catagory {}.'.format(item_id, catagory_id)
        if not testUrl(path, output):
            failcheck = True
if not failcheck:
    print("Test 11 success!")
