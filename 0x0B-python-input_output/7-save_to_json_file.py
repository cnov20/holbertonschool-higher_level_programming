#!/usr/bin/python3

import json

''' Module that writes object to text file - JSON representation '''


def save_to_json_file(my_obj, filename):

    ''' Writes an object to text file - JSON representation '''
    with open(filename, 'w', encoding='utf-8') as a_file:

        return json.dump(my_obj, a_file)
