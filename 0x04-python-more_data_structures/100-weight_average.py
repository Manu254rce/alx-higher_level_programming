#!/usr/bin/python3
def weight_average(my_list=[]):
    return 0 if not my_list

    prod = 0 
    add = 0
    for i in range(len(my_list)):
        score, weight = my_list[i]
        add += weight
        prod += (score * weight)
        
    raise ValueError("Total weight can't be zero") if add == 0

    return prod / add
