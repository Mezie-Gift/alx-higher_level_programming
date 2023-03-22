#!/usr/bin/python3
"""This script prints all `City` object from `hbtn_0e_14_usa` database
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for item in (session.query(State.name, City.id, City.name)
                 .filter(State.id == City.state_id)):
        print("{}: ({}) {}".format(item[0], str(item[1]), item[2]))
