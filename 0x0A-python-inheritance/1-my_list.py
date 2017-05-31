#!/usr/bin/python3

''' Module that creates a MyList class which inherits directly from
    built-in list() object '''


class MyList(list):

    ''' Prints a sorted version of a list instance '''

    def print_sorted(self):
        sorted_list = MyList()
        for i in self:
            sorted_list.append(i)
        print(sorted(sorted_list))
