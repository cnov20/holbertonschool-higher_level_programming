#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
        while True:
                try:
                        print('{:d}'.format(value))
                        return (True)
                except (ValueError, TypeError) as error:
                        sys.stderr.write('Exception:' + str(error)+ '\n')
                        return (False)
