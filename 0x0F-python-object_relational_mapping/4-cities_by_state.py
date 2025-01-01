#!/usr/bin/python3
"""Lists all cities by states from the database"""

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
    cursor.execute("SELECT cities.id, cities.name, "
                   "states.name FROM cities INNER JOIN "
                   "states ON states.id=cities.state_id")
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    database.close()
