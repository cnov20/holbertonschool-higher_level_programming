#!/usr/bin/python3

''' Module that writes string to a text file and returns num of chars'''


def write_file(filename='', text=''):

    ''' Writes string to text file and returns num of chars written'''

    with open(filename, 'w', encoding='utf-8') as a_file:
        a_file = a_file.write(text)
        return (a_file)
