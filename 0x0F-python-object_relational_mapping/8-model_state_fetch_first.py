#!/usr/bin/python3
"""This prints the first State object from the database `hbtn_0e_6_usa`.
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
    for item in session.query(State).order_by(State.id):
        if not bool(State):
            print("Nothing")
        elif item.id == 1:
            print("{}: {}".format(item.id, item.name))
