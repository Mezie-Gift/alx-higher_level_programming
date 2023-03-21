#!/usr/bin/python3
"""Thisscript lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa:
"""
import sys
import MySQLdb
import re

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    pattern = r'\bN\w*'

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name
                         )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE states.name REGEXP % s"
                   "ORDER BY id ASC", (pattern,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
