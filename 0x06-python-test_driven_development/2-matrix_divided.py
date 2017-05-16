#!/usr/bin/python3
def matrix_divided(matrix, div):

    new_matrix = []

    for i in range(len(matrix)):

        if type(matrix[i]) is not int and type(matrix[i]) is not float:
            raise TypeError('')

        elif type(matrix[i]) is not list:
            raise TypeError('')

        else:
            new_matrix += [list(map(lambda x: x / div, matrix[i]))]

    return (new_matrix)
