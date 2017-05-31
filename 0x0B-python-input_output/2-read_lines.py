#!/usr/bin/python3

''' Module that returns the number of lines of a text file '''

def read_lines(filename="", nb_lines=0):

    ''' Read file and return number of lines '''

    total_lines = 0
    with open('my_file_0.txt', encoding='utf-8') as a_file:
        for a_line in a_file:
            total_lines += 1
            if nb_lines <= 0 or nb_lines >= total_lines:
                print(a_line, end='')
