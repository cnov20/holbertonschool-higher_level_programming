#!/usr/bin/python3

for char in range(97, 123):
    if char != 101 and char != 114:
        print('{:s}'.format(chr(char)), end="")