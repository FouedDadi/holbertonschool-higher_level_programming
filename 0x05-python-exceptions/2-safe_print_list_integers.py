#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    c = 0
    for y in range(x):
        try:
            x = my_list[y]
            print("{:d}".format(x), end="")
            c = c + 1
        except (TypeError, ValueError):
            pass
    print()
    return c
