#!/usr/bin/python3

''' Module that creates a Student class and returns JSON dict rep '''


class Student:

    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        data = self.__dict__
        return (data)
