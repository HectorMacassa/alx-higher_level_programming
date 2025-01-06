#!/usr/bin/python3
"""
A script that deletes all State objects with a name containing the letter
a from the database
"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from model_state import State


if __name__ == "__main__":
    try:
        engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                               .format(sys.argv[1], sys.argv[2], sys.argv[3]))
        Session = sessionmaker(bind=engine)
        session = Session()

        del_states = session.query(State).filter(State.name.like('%a%')).all()
        for state in del_states:
            session.delete(state)
        session.commit()
    except SQLAlchemyError as e:
        print("Error:", e)
    finally:
        session.close()
