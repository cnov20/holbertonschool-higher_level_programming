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
        ''' Instantiates width and height attributes - private '''
        super().__init__
        self.integer_validator('width', width)
        self.intger_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        ''' Returns area of rectangle - method override - now implemented '''
        return (self.__width * self.__height)

    def __str__(self):
        ''' Returns formatted string with subclass attribute values '''
        return ('{} {}/{}'.format(type(self).__name__, self.__width,
                                  self.__height))


class Square(Rectangle):

    def __init__(self, size):
        ''' Instatntiates size attribute of square sub class '''
        super().__init__
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        ''' Returns area of square - method override '''
        return (self.__size ** 2)

    def __str__(self):
        ''' Returns formatted string with subclass attributes - override '''
        return ('[Rectangle] {}/{}'.format(self.__size, self.__size))
