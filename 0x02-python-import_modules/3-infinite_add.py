#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg = 'argument'
    args = 'arguments'
    length = len(argv)
    result = 0

    for i in range(1, length):
        result += int(argv[i])

    print('{:d}'.format(result))
