#! /usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Base, Catagory, Item

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# make test users
users = {"Satetheus":'Satetheus@satetheus.com', "Vorian":'vorian@vorian.com', "Vanar":'vanar@vanar.com', "Primo":'primo@primo.com', "Lovely":'lovely@lovely.com'}
for username, email in users.items():
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
items = ['kdtl', 'gibm', 'jbmp', 'dopu', 'memb', 'fwcj', 'mhsd', 'yhge', 
         'mzze', 'uicj', 'nvwg', 'jypy', 'pdlp', 'oseg', 'gvku', 'alfk', 
         'npwe', 'ihtr', 'wwjr', 'ohas', 'wwkw', 'nnsq', 'hezz', 'tird', 
         'gbpb']

for i in range(len(items)):
    owner = session.query(User).filter_by(name=users[int(i/5)%5]).first().name
    catagory = session.query(Catagory).filter_by(name=catagories[i%5]).first().name
    game = Item(name=items[i], owner=owner, catagory=catagory)
    session.add(game)
session.commit()