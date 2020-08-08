#!/usr/bin/python3
"""
safe from injection script that lists all states that matches the argument from the database hbtn_0e_0_usa
"""


import sys
import MySQLdb

if __name__ == "__main__":
    db= MySQLdb.connect(host="localhost", user=sys.argv[1], password=sys.argv[2], database=sys.argv[3], port=3306)
cursor= db.cursor()
cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY states.id",(sys.argv[4],))
result = cursor.fetchall()
for i in range(len(result)):
	print(result[i])
cursor.close()
db.close()