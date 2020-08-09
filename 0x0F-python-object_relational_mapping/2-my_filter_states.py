#!/usr/bin/python3
"""
lists all states that matches the argument from the database hbtn_0e_0_usa
"""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         password=sys.argv[2],
                         database=sys.argv[3],
                         port=3306)
    cu = db.cursor()
    cu.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id"
               .format(sys.argv[4]))
    result = cu.fetchall()
    for i in range(len(result)):
        print(result[i])
    cu.close()
    db.close()
