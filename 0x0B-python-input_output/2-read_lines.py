#!/usr/bin/python3
"""
function that read defined lines
"""


def read_lines(filename="", nb_lines=0):
    """
    handle conditions of reading lines
    """

    number = 0
    with open(filename, encoding="UTF8") as myfile:
        for line in myfile:
            number = number + 1
            if nb_lines <= 0 or nb_lines >= number:
                print(line, end="")
