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


def oneVar(path, output, testnum=1, loops=5):
    failcheck = False
    for var1 in range(loops):
        testpath = path.format(var1)
        testoutput = output.format(var1)
        if not testUrl(testpath, testoutput):
            failcheck = True
    if not failcheck:
        print("Test {} success!".format(testnum))


def twoVar(path, output, testnum=1, loops=5):
    failcheck = False
    for var1 in range(loops):
        for var2 in range(loops):
            # Output reverses var order for format of the phrases
            testpath = path.format(var1, var2)
            testoutput = output.format(var2, var1)
            if not testUrl(testpath, testoutput):
                failcheck = True
    if not failcheck:
        print("Test {} success!".format(testnum))


# Run tests for given urls & expected outputs
if testUrl('/catalog', "Homepage!"): print("Test 1 success!")
oneVar('/catalog/owner/{}', 'View items by owner {}.', testnum=2)
twoVar('/catalog/owner/{}/item/{}', 'This is item {} by owner {}.', testnum=3)
oneVar('/catalog/owner/{}/item/new', 'Make a new item by {}', testnum=4)
twoVar('/catalog/owner/{}/item/{}/edit', 'Edit item {} by owner {}', testnum=5)
twoVar('/catalog/owner/{}/item/{}/delete', 'Delete item {} by owner {}', testnum=6)
oneVar('/catalog/catagory/{}', 'View items in catagory {}', testnum=7)
twoVar('/catalog/catagory/{}/item/{}', 'This is item {} in catagory {}.', testnum=8)
oneVar('/catalog/catagory/{}/item/new', 'Make a new item in catagory {}.', testnum=9)
twoVar('/catalog/catagory/{}/item/{}/edit', 'Edit item {} in catagory {}.', testnum=10)
twoVar('/catalog/catagory/{}/item/{}/delete', 'Delete item {} in catagory {}.', testnum=11)