#!/usr/bin/python3

''' Module that lists all objects with a given attribute in a given table,
using SQLAlchemy, this is linked to a MySQL table via SQLAlchemy '''

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).filter(State.name.contains('a')):
        try:
            session.delete(state)
        except:
            print("Nothing")
    session.commit()
    session.close()
