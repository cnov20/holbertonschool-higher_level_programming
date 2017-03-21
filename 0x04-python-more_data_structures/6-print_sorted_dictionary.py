#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    key_list = list(my_dict)
    key_list.sort()
    for key in key_list:
        print('{:s}: {}'.format(key, my_dict[key]))
