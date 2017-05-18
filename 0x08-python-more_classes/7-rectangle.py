#!/usr/bin/python3


class Rectangle:

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return (0)
        return (self.__width + self.__height) * 2

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ('')
        else:
            rectangle = '#'
            for i in range(self.height):
                for j in range(self.height - 1):
                    print(self.print_symbol * self.width)
                return(str(self.print_symbol * self.width))

    def __repr__(self):
        return('Rectangle({:d}, {:d})'.format(self.width, self.height))