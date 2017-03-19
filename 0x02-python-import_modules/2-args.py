#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    length = len(argv)
    if length == 1:
        print ('{:d} argument.'.format(length - 1))
    elif length == 2:
        print('{:d} argument:'.format(length - 1))
    else:
        print('{:d} arguments:'.format(length - 1))
    for i in range(1, length):
        print('{:d}: {:s}'.format(i, argv[i]))
