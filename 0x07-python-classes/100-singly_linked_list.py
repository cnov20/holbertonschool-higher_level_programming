#!/usr/bin/python3

class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is None:
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')

class SinglyLinkedList:

    def __init__(self):
        self.__head = None


    def sorted_insert(self, value):
        next_node = Node(value)
        self.__next_node = value
        self.head = next_node
