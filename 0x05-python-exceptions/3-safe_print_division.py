#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    except TypeError:
        print("Must be int types")
    finally:
        if result is not None:
            print("Inside result: {}".format(result))
        else:
            print("Inside result: None")
    return result
