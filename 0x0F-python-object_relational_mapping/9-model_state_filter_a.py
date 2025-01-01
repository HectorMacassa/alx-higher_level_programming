#!/usr/bin/python3
"""Lists all State objects that contain the letter a from the database"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

    db_url = (
            'mysql+mysqldb://{0}:{1}@localhost:3306/{2}'
            .format(username, password, database_name))
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    db_session = Session()
    class_a_states = (
            db_session.query(State)
            .filter(State.name.like('%a%')).order_by(State.id).all())
    for state in class_a_states:
        print("{}: {}".format(state.id, state.name))
