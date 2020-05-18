#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    c = 0
    try:
        for c in range(x):
            x = my_list[c]
            c = c + 1
            print(x, end="")
    except IndexError:
        pass
    print()
    return c
