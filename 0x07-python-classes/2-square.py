#!/usr/bin/python3


class Square:
    def __init__(self, size=0):
        self.__size = size

        if type(size) is int and size >= 0:
            self.__size = size
        elif type(size) is int and size < 0:
            raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')
