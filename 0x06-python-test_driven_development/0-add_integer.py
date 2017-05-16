#!/usr/bin/python3
'''
This is the 'add_integer' module.

The add_integer module supplies a single function
which takes two parameters - add(a, b).

For example:
>>> add_integer(99, 1)
100
'''

def add_integer(a, b):
    '''
    Function adds two integers

    Parameters:
    a -- first integer to be added - typecast to int, if necessary
    b -- second integer to be added, typecast to int, if necessary

    Return: integer result of a and b
    '''

    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')

    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')

    return (int(a) + int(b))
