#!/usr/bin/python3
# AUTHOR: Mezie Gift
"""Defines a matrix division"""


def matrix_divided(matrix, div):
    """function divides a 'matrix' by div and returns the quotient.

    matrix must be a list of lists of integers or
    floats, otherwise a TypeError exception will be
    raised  with the message: matrix must be a matr
    x (list of lists) of integers/floats.

    Each row of the matrix must be of the same size
    otherwise a TypeError exception is raised with
    the message: Each row of the matrix must
    have the same size.

    div must be a number (integer or float),
    otherwise a TypeError exception with the
    message: div must be a number.

    if div == 0, a ZeroDivisionError is raised
    with exception message: division by zero.

    All elements of the matrix would be divided
    by div, and rounded to 2 decimal places.

    function returns a new matrix containing quotients of new matrix.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix
                        (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not type(div) is int:
        if not type(div) is float:
            raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        new_matrix = [list(map(lambda x:
                               round(x / div, 2), row)) for row in matrix]
    return new_matrix
