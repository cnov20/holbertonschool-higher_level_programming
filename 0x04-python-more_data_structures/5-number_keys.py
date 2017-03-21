#!/usr/bin/python3
def number_keys(my_dict):
    num_keys = 0
    for k, v in enumerate(range(len(my_dict))):
        num_keys += k
    return (num_keys)
