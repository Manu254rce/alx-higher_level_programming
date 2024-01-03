#!/usr/bin/python3
def isupper(str):
    new_str = ""
    for i in range(len(str)):
        number = ord(str[i])
        if (number < 97 or number > 122):
            continue
        number -= 32
        char = chr(number)
        new_str += char
    print("{}".format(new_str))
