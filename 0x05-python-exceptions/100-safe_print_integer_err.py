#!/usr/bin/python3
import sys
def safe_print_integer(value):
        while True:
                try:
                        print('{:d}'.format(value))
                        return (True)
                except (ValueError, TypeError):
                        sys.stderr.write('Exception:', file=sys.stderr)
                        return (False)
