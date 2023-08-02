#!/usr/bin/python3

"""Script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}"
        )

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).filter(State.name == sys.argv[4]).first()
    print(f"Not found" if result is None else f"{result.id}")

    session.close()
