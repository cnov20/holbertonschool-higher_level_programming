#!/bin/usr/python3

''' Module that determines if an object is an instance of a specified class
    which inherited directly(or indirectly) from said class'''


def inherits_from(obj, a_class):

    ''' Returns true if an object is an instance of specified class
        that inherited directly or indirectly - otherwise, False'''

    if issubclass(a_class, type(obj)) or type(obj) is a_class:
        return True
    return False
