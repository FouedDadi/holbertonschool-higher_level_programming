#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = {}
    for k in list(a_dictionary):
        if a_dictionary[k] != value:
            new_dict.update(a_dictionary)
        else:
            a_dictionary.pop(k)
    return new_dict
