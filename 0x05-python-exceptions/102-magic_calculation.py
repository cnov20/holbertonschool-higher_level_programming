#!/usr/bin/python3
import dis

def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                return(result)
        except IndexError:
            raise IndexError('Too Far')

dis.dis(magic_calculation)
