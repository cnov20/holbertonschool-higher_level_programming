#!/usr/bin/python3

import json

''' Module that creates a python object from a JSON file '''


def load_from_json_file(filename):

    ''' Creates and returns an object from JSON file '''

    with open(filename, 'r', encoding='utf-8') as a_file:

        return json.load(a_file)
