#!/usr/bin/python3
"""
script that that prints all City objects from the database hbtn_0e_14_usa
"""


if __name__ == "__main__":
    import sys
    from model_city import City
    from model_state import Base
    from model_state import State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    session = sessionmaker(bind=engine)
    session = session()
    for state, city in session.query(State, City).filter(
                               State.id == City.state_id).order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
