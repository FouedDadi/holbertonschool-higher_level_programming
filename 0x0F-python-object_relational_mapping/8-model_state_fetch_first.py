#!/usr/bin/python3
"""
script that prints the first State object from the database hbtn_0e_6_usa
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
    i = session.query(State).order_by(State.id).first()
    if i is None:
        print("Nothing")
    else:
        print("{}: {}".format(i.id, i.name))
    session.close()
