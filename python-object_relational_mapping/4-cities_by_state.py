#!/usr/bin/python3

"""Script that lists all cities from the database hbtn_0e_4_usa"""

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
    cursor.execute(
        """SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states
        ON cities.state_id = states.id
        ORDER BY cities.id""")
    rows = cursor.fetchall()
    printed_states = set()
    for row in rows:
        city_id, city_name, state_name = row
        if state_name not in printed_states:
            print(row)
            printed_states.add(state_name)
    cursor.close()
    db.close()
