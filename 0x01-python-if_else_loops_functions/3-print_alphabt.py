#!/usr/bin/python3
for x in range(97, 123):
    if x in [101, 113]:
        continue
    print("{}".format(chr(x)), end="")
