#!/usr/bin/python3
"""
script that adds the state object Louisiana to the database hbtn_0e_6_usa
"""


if __name__ == "__main__":
    import sys
    from model_city import Base, City
    from model_state import State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    session = sessionmaker(bind=engine)
    session = session()
    state = State(name="California")
    city = City(name="San Francisco")
    session.add(state)
    session.add(city)
    session.commit()
    session.close()
