#!/usr/bin/python3
for j in range(10):
    for i in range(10):
        if j < i and j < 8:
            print("{}{}, ".format(j,i), end = "")
        elif j == 8 and i == 9:
            print("{}{}".format(j,i))
