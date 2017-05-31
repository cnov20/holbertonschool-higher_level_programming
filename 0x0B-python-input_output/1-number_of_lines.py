#!/usr/bin/python3

''' Module that returns the number of lines of a text file '''


def number_of_lines(filename=""):

    ''' Read file and return number of lines '''

    with open('my_file_0.txt', encoding='utf-8') as a_file:
        a_file = a_file.readlines()
    return(len(a_file))
