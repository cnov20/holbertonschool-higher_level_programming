#!/usr/bin/python3

import json
import pickle

''' Module that returns a dictionary - JSON serialization of an object '''


def class_to_json(obj):

    ''' Creates and returns a JSON dictionary object serialization '''

    data = json.dumps(obj.__dict__)
    return json.loads(data)
