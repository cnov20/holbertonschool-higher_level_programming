#!/bin/usr/python3

''' Module that adds exception raising to previously BaseGeometry class '''


class BaseGeometry:
    ''' Class BaseGeometry '''

    def integer_validator(self, name, value):
        ''' Integer validation (as integer) method '''

        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))

    def area(self):
        ''' Area method '''

        def __str__(self):
            ''' Raises an exception for unimplemented methods '''
        raise Exception('area() is not implemented')
