#!/usr/bin/python3

''' Module that appends string to text file'''


def append_write(filename='', text=''):

    ''' Appends string to text file and returns num of chars added'''

    with open(filename, 'a', encoding='utf-8') as a_file:
        a_file = a_file.write(text)
        return (a_file)
