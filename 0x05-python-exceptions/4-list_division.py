#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            if isinstance(my_list_1[i], (int, float)) and
            isinstance(my_list_2[i], (int, float)):
                division = my_list_1[i] / my_list_2[i]
                new_list.append(division)
            else:
                print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        finally:
            return new_list
