#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    index = 0
    for row in matrix:
        for index in range(len(row)):
            if index == (len(row) - 1):
                print('{:d}'.format(row[index]), end='')
            else:
                print('{:d}'.format(row[index]), end=' ')
        print()
