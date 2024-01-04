#!/usr/bin/python3
import sys


def print_args():
    args = sys.argv[1:]
    if len(args) == 1:
        print("{} argument:".format(len(args)))
    else:
        print("{} arguments:".format(len(args)))
    for i, arg in enumerate(args, start=1):
        print("{} : {}".format(i, arg))


if __name__ == "__main__":
    print_args()
