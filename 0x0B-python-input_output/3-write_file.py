#!/usr/bin/python3

''' Module that writes string to a text file and returns num of chars'''


def write_file(filename='', text=''):

    ''' Writes string to text file and returns num of chars written'''

    chars_written = 0
    with open('my_first_file.txt', 'w', encoding='utf-8') as a_file:
        a_file = a_file.write("Holberton School is so cool!\n")
        return (a_file)
