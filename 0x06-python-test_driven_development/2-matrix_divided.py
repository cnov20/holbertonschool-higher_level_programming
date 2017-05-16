#!/usr/bin/python3
'''
This is the 'matrix_divided' module.

The matrix_divided module supplies a single function
which takes two parameters - matrix_divided(matrix, div).

For example:
>>> matrix_divided(matrix, 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

'''


def matrix_divided(matrix, div):

    '''
    Function divides all elements of a matrix(list of lists)
    by second parameter passed (div)

    Parameters:
    matrix -- a list of lists to be divided
    div -- number to divide matrix by

    Return: new matrix containing the quotients of aforementioned division
    '''

    if div == 0:
        raise ZeroDivisionError('division by zero')

    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')

    new_matrix = []

    for i in range(len(matrix)):

        if type(i) is not int and type(i) is not float:
            raise TypeError('matrix must be a matrix'
                            '(list of lists) of integers/floats')

        if len(matrix[i]) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')

        new_matrix += [list(map(lambda x: round(x / div, 2), matrix[i]))]

    return (new_matrix)
