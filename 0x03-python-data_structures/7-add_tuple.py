#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a is None or tuple_b is None:
        return

    #if len(tuple_a) < 2 or len(tuple_b) < 2:

    sums = []
    new_a = tuple_a + (0, 0)
    new_b = tuple_b + (0, 0)
    for i in range(len(tuple_a)):
        sums.append(new_a[i] + new_b[i])
    return(tuple(sums))
