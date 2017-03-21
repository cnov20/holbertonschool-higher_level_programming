#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a is None or tuple_b is None:
        return
    sums = []
    new_a = tuple_a + (0, 0)
    new_b = tuple_b + (0, 0)
    for i in range(2):
        sums.append(new_a[] + new_b[i])
    return(tuple(sums))
