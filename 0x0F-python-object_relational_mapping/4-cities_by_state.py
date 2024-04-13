#!/usr/bin/python3 # W: Module name "1-filter_states" doesn't conform to snake_case naming style

"""
Script that lists all states with a name starting with N (upper N)
"""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    cur = db.cursor()

    cur.execute("""SELECT cities.id, cities.name,
                states.name FROM cities JOIN states ON
                cities.state_id = states.id ORDER BY cities.id ASC""")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
