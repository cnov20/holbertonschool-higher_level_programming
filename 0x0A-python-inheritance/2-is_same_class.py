#!/bin/usr/python3

''' Module that compares an object to a specified class to determine type '''


def is_same_class(obj, a_class):

    ''' Returns true if an object is an instance of specified class
        otherwise, False'''

    if isinstance(obj, a_class) and type(obj) is a_class:
        return True
    return False
