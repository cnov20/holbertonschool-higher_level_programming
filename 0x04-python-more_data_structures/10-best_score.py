#!/usr/bin/python3
def best_score(my_dict):
    if my_dict:
        maximum = max(my_dict, key=my_dict.get)
        return (maximum)
