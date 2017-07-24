#!/usr/bin/python3

''' Module that changes name of  an object in a given table,
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
    new_state = session.query(State).
    filter_by(id=2).update({'name': 'New Mexico'})
    session.commit()
    try:
        print("{}".format(new_state))
    except:
        print("Not found")
    session.close()
