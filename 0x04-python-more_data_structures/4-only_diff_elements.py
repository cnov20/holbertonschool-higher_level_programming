#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    list_1 = list(set_1)
    list_2 = list(set_2)
    full_list = list_1 + list_2
    return (common for common in full_list if common
            not in list_1 or common not in list_2)
