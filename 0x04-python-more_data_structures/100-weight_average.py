#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return (0)
    elif my_list is None:
        return (None)
    else:
        weight = 0
        score = 0
        for i in range(len(my_list)):
            score += (my_list[i][0] * my_list[i][1])
            weight += my_list[i][1]
        weight_avg = score / weight
        return (weight_avg)
