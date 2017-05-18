#!/usr/bin/python3


class Square:
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):

        if type(value) is int and value >= 0:
            self.__size = value
        elif type(value) is int and value < 0:
            raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(self.__size):
                print(self.size * '#')