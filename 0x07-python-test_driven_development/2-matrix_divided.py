#!/usr/bin/python3
"""
returning new matrix
"""


def matrix_divided(matrix, div):
    """
    handling errors
    """
    if type(matrix) is not list:
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')
    for x in matrix:
        for y in x:
            if type(y) not in (int, float):
                raise TypeError(
                    'matrix must be a matrix (list of lists) of integers/floats\
                        ')
        if len(x) != len(matrix[0]):
            raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats')
    if type(div) not in (int, float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    return [[round(y / div, 2) for y in x] for x in matrix]
