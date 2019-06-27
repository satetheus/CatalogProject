#! /usr/bin/env python3
from controls import sqlItemSearch, showAllItems
import sqlalchemy


def test_itemSearch():
    nameAssert = 'name didn\'t match or was absent.'
    assert sqlItemSearch('name', 'nier automata').name == 'nier automata', name
    ownerAssert = 'owner didn\'t match or was absent.'
    assert sqlItemSearch('owner', 'Vorian')[0].owner == 'Vorian', owner
    cataAssert = 'catagory didn\'t match or was absent.'
    assert sqlItemSearch('catagory', 'rpg')[0].catagory == 'rpg', cata


def test_showAllItems():
    test1 = showAllItems()
    test2 = showAllItems(True)

    showAllItemsAssert = 'showAllItems() is not returning a query.'
    assert type(test1) == sqlalchemy.orm.query.Query, showAllItemsAssert
    assert type(test2) == dict, 'showAllItems(True) is not returning a dict.'
