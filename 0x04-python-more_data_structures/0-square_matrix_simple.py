#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """This computes the square value of all integers of a matrix"""

    new = []
    for i in matrix:
        new.append([j ** 2 for j in i])
    return new
