#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3],)
curs = db.cursor()
curs.execute("SELECT * FROM states ORDER BY states.id")
result = curs.fetchall()
for i in result:
    print(i)
curs.close()
db.close()
