#!/usr/bin/python3
def fizzBuzz():
    for i in range(1, 100):
        if (i % 3) and (i % 5) == 0:
            print('FizzBuzz')
        elif (i % 3 == 0):
            print('Fizz')
        elif (i % 5 == 0):
            print('Buzz')
        else:
            print("{}".format(i), end='')
