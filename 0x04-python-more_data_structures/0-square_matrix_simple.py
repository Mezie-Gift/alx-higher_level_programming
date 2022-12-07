#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """This computes the square value of all integers of a matrix"""


    matrix_sqr = matrix.copy()

    for i in range(len(matrix)):
        matrix_sqr[i] = list(map(lambda x: x**2, matrix[i]))
    return (matrix_sqr)
