#!/usr/bin/python3
import sys


def infinite_args(*args):
    sum = 0
    args = args[1:]
    for arg in args:
        sum += int(arg)
    return sum


if __name__ == "__main__":
    print("{}".format(infinite_args(*sys.argv)))
