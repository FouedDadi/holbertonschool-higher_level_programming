#!/usr/bin/python3
def uppercase(str):
    st = ""
    for c in str:
        if 97 <= ord(c) <= 122:
            st += chr(ord(c) - 32)
        else:
            st += c
    print("{}".format(st))
