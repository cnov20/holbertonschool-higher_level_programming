#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = []
    for i in range(len(my_list)):
        del my_list[idx]
        return(new_list + my_list)
