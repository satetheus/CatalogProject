#! /usr/bin/env python3
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), index=True)


class Catagory(Base):
    __tablename__ = 'catagory'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), index=True)


class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), index=True)
    owner = Column(String(32), ForeignKey(User.name), nullable=False)
    catagory = Column(String(32), ForeignKey(Catagory.name), nullable=False)


engine = create_engine('sqlite:///catalog.db')

Base.metadata.create_all(engine)
