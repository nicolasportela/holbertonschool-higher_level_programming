#!/usr/bin/python3
"""script that prints all City objects
from the database hbtn_0e_14_usa"""

if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for cities in session.query(City):
        for states in session.query(State).filter(State.id == cities.state_id):
            print("{}: ({}) {}".format(states.name, cities.id, cities.name))
    session.close()
