#!/usr/bin/python3

"""Script that lists all states with a name starting with N
from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    user_db = sys.argv[1]
    passwd_db = sys.argv[2]
    name_db = sys.argv[3]
    state_name = sys.argv[4]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user_db,
        passwd=passwd_db,
        db=name_db)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    printed_states = set()
    for row in rows:
        state_id, state_name = row
        if state_name not in printed_states:
            print(row)
            printed_states.add(state_name)
    db.close()
