#!/usr/bin/python3

import json

''' Module that deserializes a str to JSON object '''


def from_json_string(my_str):

    ''' Converts str to JSON object and returns '''

    return(json.loads(my_str))
