#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""

if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine
    ('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for states in session.query(State):
        print("{}: {}".format(states.id, states.name))
    session.close()
