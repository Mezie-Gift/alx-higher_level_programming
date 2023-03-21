#!/usr/bin/python3
"""This script lists all objects from database `hbtn_0e_6_usa`
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for item in session.query(State).order_by(State.id).all():
        print("{}: {}".format(item.id, item.name))
session.close()
