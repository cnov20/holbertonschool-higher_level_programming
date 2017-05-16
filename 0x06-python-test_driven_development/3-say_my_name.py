#!/usr/bin/python3
'''
This is the 'say_my_name' module.

The say_my_name module supplies a single function
which takes two parameters - say_my_name(first_name, last_name="").

For example:
>>> say_my_name("Walter", "White")
My name is Walter White
'''


def say_my_name(first_name, last_name=""):
    '''
    Function prints the following:
    'My name is' combined with first_name and last_name

    Parameters:
    first_name -- first name to be printed
    last_name -- second (last) name to be printed

    Return: No return value, only prints
    '''

    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')

    print('My name is', first_name, last_name)
