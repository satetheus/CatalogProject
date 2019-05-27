#! /usr/bin/env python3
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), index=True)
    

class catagory(Base):
    __tablename__ = 'catagory'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), index=True)
    
class item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), index=True)
    owner_id = Column(Integer, ForeignKey(user.id), nullable=False)
    