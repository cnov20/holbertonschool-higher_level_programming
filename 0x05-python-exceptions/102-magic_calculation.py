#!/usr/bin/python3
import dis


def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too Far')
            else:
                result += (a ** b) / i
        finally:
            result = a + b
            break
            return
dis.dis(magic_calculation)
