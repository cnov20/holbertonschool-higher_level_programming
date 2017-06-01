#!/usr/bin/python3

''' Module that creates a Student class and returns JSON dict rep '''


class Student:

    ''' Creates new dictionary and returns only existing attributes '''

    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        data = {}
        if attrs is None:
            data = self.__dict__
            return data
        for i in range(len(attrs)):
            if hasattr(self, attrs[i]):
                data[attrs[i]] = getattr(self, attrs[i])
        return (data)
