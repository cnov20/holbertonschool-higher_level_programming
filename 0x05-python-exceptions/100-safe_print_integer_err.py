#!/usr/bin/python3
import sys
def safe_print_integer(value):
        while True:
                try:
                        print('{:d}'.format(value))
                        return (True)
                except:
                        sys.stderr.write('Eception: {:d}'.format(error))
                        return (False)
