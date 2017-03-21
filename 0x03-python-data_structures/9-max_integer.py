#!/usr/bin/python3
def max_integer(my_list=[]):
    answer = 0
    for i in my_list:
        if i > answer:
            answer = i
    return(answer)
