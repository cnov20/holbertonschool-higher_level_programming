#!/usr/bin/python3
def no_c(my_string):
    for char in range(len(my_string)):
        if 'C' in my_string or 'c' in my_string:
            return(my_string[1:])
        else:
            return (my_string)
