#!/bin/usr/python3

''' Module that adds exception raising to previously BaseGeometry class '''

class BaseGeometry:
    ''' Class BaseGeometry '''

    def integer_validator(self, name, value):
        ''' Integer validation (as integer) method '''

        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(value))

    def area(self):
        ''' Area method '''

        def __str__(self):
            ''' Raises an exception for unimplemented methods '''
        raise Exception('area() is not implemented')

class Rectangle(BaseGeometry):
    ''' Class that defines a rectangle - inherited from Class BaseGeometry '''

    def __init__(self, width, height):
        ''' Instantiates with width and height attributes '''
        super().__init__
        BaseGeometry.integer_validator = width
        BaseGeometry.integer_validator = height
