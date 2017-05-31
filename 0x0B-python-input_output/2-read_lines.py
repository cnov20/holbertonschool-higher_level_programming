#!/usr/bin/python3

''' Module that reads (n) lines of a text file and prints to stdout'''


def read_lines(filename="", nb_lines=0):

    ''' Read (n) lines of file and print to stdout'''

    total_lines = 0
    with open('my_file_0.txt', encoding='utf-8') as a_file:
        for a_line in a_file:
            total_lines += 1
            if nb_lines <= 0 or nb_lines >= total_lines:
                print(a_line, end='')
