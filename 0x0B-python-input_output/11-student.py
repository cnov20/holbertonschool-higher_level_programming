#!/usr/bin/python3

import json
''' Module that creates a Student class and returns JSON dict rep '''

class Student:

    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        data = json.dumps(self.__dict__)
        return json.loads(data)
