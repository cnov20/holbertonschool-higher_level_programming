#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return (0)
    elif my_list is None:
        return (None)
    else:
        for score in range(len(my_list)):
            weight = my_list[score][1]
            weight_avg = (score * weight / weight)
#           print (weight)
#           print (weight_avg)
        return (weight_avg)
