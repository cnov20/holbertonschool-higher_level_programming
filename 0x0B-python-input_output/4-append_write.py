#!/usr/bin/python3

''' Module that writes string to a text file and returns num of chars'''


def append_write(filename='', text=''):

    ''' Writes string to text file and returns num of chars written'''

    with open('file_append.txt', 'a', encoding='utf-8') as a_file:
        a_file = a_file.write("Holberton School is so cool!\n")
        return (a_file)
