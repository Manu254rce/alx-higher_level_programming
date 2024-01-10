#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [0 for _ in range(len(my_list))]
    for i in range(len(my_list)):
        if i == search:
            new_list[i] = replace
        else:
            new_list[i] = my_list[i]
    return(new_list)

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
    new_list = search_replace(my_list, 5, 100)

    print(new_list)
    print(my_list)
