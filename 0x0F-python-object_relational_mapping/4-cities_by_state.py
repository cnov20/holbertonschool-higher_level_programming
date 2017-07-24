#!/usr/bin/python3

''' Module that lists all fields from specific columns
    joined with newly created tabel - safe from MySQL injections '''

from sys import argv
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           password=argv[2], db=argv[3])
    cursor = conn.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
    INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC;")
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    conn.close()
