#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
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
        for i in range(1, length):
            print('{:d}: {:s}'.format(i, argv[i]))
