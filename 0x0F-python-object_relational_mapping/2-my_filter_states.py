#!/usr/bin/python3

''' Module that lists all fields in a given column with a specific name'''

from sys import argv
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           password=argv[2], db=argv[3])
    cursor = conn.cursor()
    cursor.execute("SELECT states.id, states.name FROM states WHERE BINARY\
    states.name='{}'".format(argv[4]))
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    conn.close()
