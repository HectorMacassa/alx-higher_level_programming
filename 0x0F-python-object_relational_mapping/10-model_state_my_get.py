#!/usr/bin/python3
"""Prints the State object with the name passed as argument fromthedatabase"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    state_name = sys.argv[4]

    db_url = (
            'mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(username, password, database_name))
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    db_session = Session()

    matching_state = (
            db_session.query(State)
            .filter(State.name.like(state_name)).first()
            )

    if not matching_state:
        print("Not found")
    else:
        print(matching_state.id)
