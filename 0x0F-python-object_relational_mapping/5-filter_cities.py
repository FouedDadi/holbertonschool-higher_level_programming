#!/usr/bin/python3
"""
safe from injection script that lists all states
that matches the argument from the database hbtn_0e_0_usa
"""


import sys
import MySQLdb

if __name__ == "__main__":
    state = sys.argv[4]
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         password=sys.argv[2],
                         database=sys.argv[3],
                         port=3306)
    cu = db.cursor()
    cu.execute("SELECT cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s ORDER BY cities.id", (state,))
    result = cu.fetchall()
    print(", ".join([i[0] for i in result]))
    cu.close()
    db.close()
