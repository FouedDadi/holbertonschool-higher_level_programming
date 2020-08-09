#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
"""


if __name__ == "__main__":
    import sys
    import MySQLdb
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         password=sys.argv[2],
                         database=sys.argv[3],
                         port=3306)
cursor = db.cursor()
cursor.execute("SELECT * FROM states ORDER BY states.id")
result = cursor.fetchall()
for i in range(len(result)):
    print(result[i])
cursor.close()
db.close()
