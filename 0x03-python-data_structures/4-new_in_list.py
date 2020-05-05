#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = my_list[:]
    if idx >= len(my_list):
        return copy
    elif idx < 0:
        return copy
    else:
        copy[idx] = element
        return copy
