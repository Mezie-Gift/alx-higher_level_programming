#!/usr/bin/python3
"""This script lists all the `states` from the database `hbtn_0e_0_usa`"""
import sys
import MySQLdb


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name
                         )
    cusor = db.cusor()
    cusor.execute("SELECT * FROM `states` ORDER BY id ASC")
    rows = cusor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
