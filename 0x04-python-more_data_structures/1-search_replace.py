#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for x in my_list:
        new_list.append(x)
        if x == search:
            new_list.remove(search)
            new_list.append(replace)
    return new_list
