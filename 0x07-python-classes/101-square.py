#!/usr/bin/python3


class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.size == 0:
            print()
        else:
            print(self.position[1] * '\n', end='')
            for i in range(self.size):
                print(self.position[0] * ' ', end='')
                for j in range(self.size):
                    print('#', end='')
                print()
