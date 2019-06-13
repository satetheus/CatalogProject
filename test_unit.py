#! /usr/bin/env python3
from controls import sqlItemSearch, showAllItems
import sqlalchemy


def test_itemSearch():
   assert sqlItemSearch('name', 'dopu').name == 'dopu', 'name didn\'t match or was absent.'
   assert sqlItemSearch('owner', 'Vorian')[0].owner == 'Vorian', 'owner didn\'t match or was absent.'
   assert sqlItemSearch('catagory', 'rpg')[0].catagory == 'rpg', 'catagory didn\'t match or was absent.'


def test_showAllItems():
    test1 = showAllItems()
    test2 = showAllItems(True)

    assert type(test1) == sqlalchemy.orm.query.Query, 'showAllItems() is not returning a query.'
    assert type(test2) == dict, 'showAllItems(True) is not returning a dict.'