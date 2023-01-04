#!/usr/bin_python3
# AUTHOR: Mezie Gift
"""Define print_square"""


def print_square(size):
    """Function prints a square with the character '#'
    Args:
       size:is the size length of the square
    Errors:
       if size is not an integer:
           raise TypeError(size must be an integer)
       if size is less than 0:
           raise TypeError(size must be >= 0)
       if size is a float and is less than 0:
           raise TypeError(size must be an integer)
    """
    if not isinstance(size, int):
        #    if not isinstance(size, float):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
        #    if (isinstance(size, float)):
        #    if (size < 0):
        #    raise TypeError("size must be an integer")
        #    else:
        #    for i in range(0, int(size)):
        #    print("{}".format("#" * int(size)), end="")
        #    print("")
    else:
        for i in range(0, int(size)):
            print("{}".format("#" * size), end="")
            print("")
