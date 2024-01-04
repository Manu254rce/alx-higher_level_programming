#!/usr/bin/python3
import dis
import marshal
import py_compile
import dis
import sys

def print_names(filename):
    py_compile.compile(filename)
    with open(filename, 'rb') as file:
        code = marshal.load(file)
    names = code.co_names
    filtered_names = [name for name in names if not name.startswith('__')]
    sorted_names = sorted(filtered_names)
    for name in sorted_names:
        print(name)

if __name__ == "__main__":
    assert sys.version_info[:2] == (3, 8), "This script requires Python 3.8.x"
    filename = 'hidden_4.pyc'
    print_names(filename)

