#!/bin/usr/python3

''' Module that returns list of available attributes
    and methods of an object (directory) '''


def lookup(obj):
    ''' returns directory of attributes / methods of obj '''
    list = dir(obj)
    return list
