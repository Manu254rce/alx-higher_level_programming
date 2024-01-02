#!/usr/bin/python3
output = ""
for i in range(0, 100):
    output += "{:02}, ".format(i)
output = output[:len(output)-2]
print(output)
