#!/usr/bin/python3
"""This script creates the state "California" with the city "San Francisco"
from the database `hbtn_0e_100_usa`
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='California')
    session.add(new_state)
    new_city = City(name='San Francisco')
    new_state.cities.append(new_city)
    session.add(new_city)
    session.commit()
