#!/usr/bin/python3
"""This prints the `State` object with the name
passed as argument from the database `hbtn_0e_6_usa`
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
    item = session.query(State).filter(State.name == sys.argv[4])
    if item:
        print("{}".format(item[0].id))
    else:
        print("Not found")
