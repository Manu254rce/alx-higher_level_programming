#!/usr/bin/python3
str = ""
for i in range(122, 96, -1):
    if (i % 2 == 1):
        i -= 32
        str += chr(i)
    else:
        str += chr(i)

print("{}".format(str))
