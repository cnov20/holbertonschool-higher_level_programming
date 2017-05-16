#!/usr/bin/python3
def matrix_divided(matrix, div):

    new_matrix = []

    for i in range(len(matrix)):

        if type(div) is not int and type(div) is not float:
            raise TypeError ('div must be a number')


        if type(matrix) is not int and type(matrix) is not float:
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

        if div == 0:
            raise ZeroDivisionError('division by zero')

        else:
            new_matrix += [list(map(lambda x: x / div, matrix[i]))]

    return (new_matrix)
