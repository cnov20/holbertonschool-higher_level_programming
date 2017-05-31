#!/usr/bin/python3

import json
''' Module that converts an object to it corresponding JSON str fromat'''

def to_json_string(my_obj):

    ''' Serializes Python object to JSON string and returns '''

    return(json.dumps(my_obj))
