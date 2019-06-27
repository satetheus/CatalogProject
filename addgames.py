#! /usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Base, Catagory, Item
from gamefile import games

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# make test users
users = [["Satetheus", 'Satetheus@satetheus.com'],
         ["Vorian", 'vorian@vorian.com'],
         ["Vanar", 'vanar@vanar.com'],
         ["Primo", 'primo@primo.com'],
         ["Lovely", 'lovely@lovely.com']]
for username, email in users:
    person = User(name=username, email=email)
    session.add(person)
session.commit()

# make test catagories
catagories = ["rpg", "fps", "mmo", "platformer", "sidescroller"]
for types in catagories:
    gametype = Catagory(name=types)
    session.add(gametype)
session.commit()

# make test items
for game in games:
    name = game['name']
    owner = game['owner']
    catagory = game['catagory']
    newItem = Item(name=name, owner=owner, catagory=catagory)
    session.add(newItem)
session.commit()
