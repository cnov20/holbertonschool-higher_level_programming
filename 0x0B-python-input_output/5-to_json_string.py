#!/usr/bin/python3

import json
''' Module that converts a string to it corresponding JSON representation '''

def to_json_string(my_obj):

    ''' Convert str to JSON representation and returns '''

    return(json.dumps(my_obj))
