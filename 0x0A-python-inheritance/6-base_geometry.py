#!/bin/usr/python3

''' Module that adds exception raising to previously BaseGeometry class '''


class BaseGeometry:
    ''' Class BaseGeometry '''

    pass

    def area(self):
        ''' Area method '''


        def __str__(self):
            ''' Raises an exception for unimplemented methods '''
        raise Exception('area() is not implemented')
