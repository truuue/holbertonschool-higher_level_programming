#!/usr/bin/python3

"""Script that takes in an argument and
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument"""

import MySQLdb
import sys

if __name__ == "__main__":
    user_db = sys.argv[1]
    passwd_db = sys.argv[2]
    name_db = sys.argv[3]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user_db,
        passwd=passwd_db,
        db=name_db)
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states WHERE name LIKE BINARY
    %s ORDER BY id ASC""", (sys.argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
