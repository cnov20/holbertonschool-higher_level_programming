#!/usr/bin/python3


''' Module that returns a dictionary - JSON serialization of an object '''


def class_to_json(obj):

    ''' Creates and returns a JSON dictionary object serialization '''
    return (obj.__dict__)
