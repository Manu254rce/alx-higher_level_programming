#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list = set(my_list)
    return sum(i + 1 for i in range(len(my_list)))
