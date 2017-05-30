#!/bin/usr/python3

''' Module that determines if an object is an instance of a specified class or
    instance of a derived class '''


def is_kind_of_class(obj, a_class):

    ''' Returns true if an object is an instance of specified class
        or derived class - otherwise, False'''

    if isinstance(obj, a_class):
        return True
    return False
