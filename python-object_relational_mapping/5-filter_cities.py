#!/usr/bin/python3

"""Script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa"""

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
        """SELECT cities.name
        FROM cities JOIN states
        ON states.id = cities.state_id
        WHERE states.name LIKE BINARY %s
        ORDER BY cities.id""", (sys.argv[4],))
    rows = cursor.fetchall()
    city_names = []
    for row in rows:
        city_name = row[0]
        if city_name not in city_names:
            city_names.append(city_name)
    string = ", ".join(city_names)
    print(string)
    cursor.close()
    db.close()
