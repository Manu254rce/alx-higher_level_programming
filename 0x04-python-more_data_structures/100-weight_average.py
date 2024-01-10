#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    prod = 0
    add = 0
    for score, weight in my_list:
        add += weight
        prod += (score * weight)
    if add == 0:
        raise ValueError("Total weight can't be zero")

    return prod / add
