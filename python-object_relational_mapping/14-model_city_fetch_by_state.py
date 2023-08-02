#!/usr/bin/python3

"""Script 14-model_city_fetch_by_state.py
that prints all City objects from the database hbtn_0e_14_usa"""

import sys
from model_city import City
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

    c_data = session.query(State, City).filter(State.id == City.state_id).all()
    for state, city in c_data:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
