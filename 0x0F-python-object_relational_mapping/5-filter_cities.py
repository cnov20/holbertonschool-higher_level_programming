#!/usr/bin/python3

''' Module that lists all fields from specific columns based on user input
    joined with newly created tabel - safe from MySQL injections '''

from sys import argv
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           password=argv[2], db=argv[3])
    cursor = conn.cursor()
    cursor.execute("SELECT cities.name FROM cities\
    INNER JOIN states ON cities.state_id = states.id WHERE states.name='{}'\
    ORDER BY cities.id ASC".format(argv[4]))
    query_rows = cursor.fetchall()
    index = 0
    for row in query_rows:
        if index > 0:
            print(', ', end='')
        print('{}'.join(row), end='')
        index += 1
    print()
    cursor.close()
    conn.close()
