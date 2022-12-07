#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """This computes the square value of all integers of a matrix"""


    tmp = []
    for x in matrix:
        tmp.append(list(map(lambda x: x**2, x)))
    return (tmp)
