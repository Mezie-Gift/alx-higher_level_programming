#!/usr/bin/python3
"""This script takes in arguments and displays all values in the `states` \
table of `hbtn_0e_0_usa` where name matches the argument.
But this time, it is safe from MySQL injections!"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3]
                         )
    cursor = db.cursor()
    state_name = sys.argv[4]
    cursor.execute("SELECT * FROM states WHERE name LIKE %s \
        ORDER BY states.id ASC", (state_name, ))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
