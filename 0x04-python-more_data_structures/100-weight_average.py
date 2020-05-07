#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    S = 0
    n = 0
    for x in my_list:
        S = x[0] * x[1] + S
        n = n + x[1]
    return S / n
