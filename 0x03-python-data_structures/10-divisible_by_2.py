#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mul2 = []
    for x in my_list:
        if x % 2 == 0:
            mul2.append(True)
        elif my_list[x] % 2 != 0:
            mul2.append(False)
    return mul2
