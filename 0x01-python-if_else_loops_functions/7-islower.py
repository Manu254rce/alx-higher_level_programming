#!/usr/bin/python3
def islower(c):
    flag = True
    c = ord(c)
    for i in range(97, 123):
        if c == i:
            return flag
    return not flag
