#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = sum(map(lambda x: my_list[x], my_list[:]))
    return (result)
