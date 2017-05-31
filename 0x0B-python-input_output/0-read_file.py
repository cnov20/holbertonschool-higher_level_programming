#!/usr/bin/python3

''' Module that reads a text file and prints to std out '''


def read_file(filename=""):

    ''' Read file and print to std out '''

with open('my_file_0.txt', encoding='utf-8') as a_file:
    a_file = a_file.read()
    print (a_file)
