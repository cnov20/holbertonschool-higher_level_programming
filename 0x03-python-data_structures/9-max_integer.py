#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return

    answer = 0
    for i in my_list:
        if i > answer:
            answer = i
    return(answer)
