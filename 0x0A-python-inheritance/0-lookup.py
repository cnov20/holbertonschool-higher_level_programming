#!/bin/usr/python3

''' Module that returns list of available attributes\ '''
''' and methods of an object (dictionary) '''

def lookup(obj):
    ''' returns dictionary of attributes / methods of obj '''

    list = dir(obj)
    return list
