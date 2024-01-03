#!/usr/bin/python3
def remove_char_at(str, n):
    str2 = ""
    for  i in range(len(str)):
        if (i == n):
           continue
        else:
            str2 += str[i]
    print("{}".format(str2))
