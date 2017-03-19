#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    i = 1
    arg = 'argument'
    args = 'arguments'
    length = len(argv)

    if length == 1:
        print ('{:d} {:s}.'.format(length - 1, arg))

    elif length == 2:
        print('{:d} {:s}:'.format(length - 1, arg))
        print('{:d}: {:s}'.format(length - 1, argv[1]))

    elif length >= 3:
        print('{:d} {:s}:'.format(length - 1, args))

        for i in range(i, length, +1):
            print('{:d}: {:s}'.format(i, argv[i]))
