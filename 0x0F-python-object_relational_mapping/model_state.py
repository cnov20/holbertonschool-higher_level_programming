#!/usr/bin/python3

''' Module defines a class and contains an instance of said class,
    this is linked to a MySQL table via SQLAlchemy'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
