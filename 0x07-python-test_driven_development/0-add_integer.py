#!/usr/bin/python3
# AUTHOR: Mezie Gift
"""Define integer addition function"""

def add_integer(a, b=98):
    """add_integer adds number a and b, and returns the result.

    if a or b is neither an integer nor float, function raises a TypeError message: a must be an integer/ b must be an integer, respectively.

    if either a or b is a float, it will be first  casted to integer before the sum is returned.
    """
    if (not type(a) is int):
        if (not type(a) is float):
            raise TypeError("a must be an integer")
    if (not type(b) is int):
        if (not type(b) is float):
            raise TypeError("b must be an integer")
    result = int(a) + int(b)
    return (result)
