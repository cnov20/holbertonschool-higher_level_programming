#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sums = []
    new_tuple_a = tuple_a + (0, 0)
    new_tuple_b = tuple_b + (0, 0)
    for i in range(len(tuple_a)):
        sums.append(new_tuple_a[i] + new_tuple_b[i])
    return(sums)
