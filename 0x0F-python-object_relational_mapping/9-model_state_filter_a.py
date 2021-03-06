#!/usr/bin/python3
"""
script that lists all State objects that contains a from the database
hbtn_0e_6_usa
"""


if __name__ == "__main__":
    import sys
    from model_state import Base
    from model_state import State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    session = sessionmaker(bind=engine)
    session = session()
    for i in session.query(State).order_by(State.id).filter(
             State.name.contains('%a')):
        print("{}: {}".format(i.id, i.name))
    session.close()
