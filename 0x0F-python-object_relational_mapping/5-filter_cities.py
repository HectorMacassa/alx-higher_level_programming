#!/usr/bin/python3
"""Lists all cities for each state from the database"""

import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3],
            port=3306
            )
    cursor = database.cursor()
    state = sys.argv[4]
    cursor.execute("SELECT cities.name FROM cities INNER JOIN " "states ON states.id=cities.state_id" " WHERE states.name=%s", (state, ))
    results = cursor.fetchall()
    cities = list(row[0] for row in results)
    print(*cities, sep=", ")
    cursor.close()
    database.close()
