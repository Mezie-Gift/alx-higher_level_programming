#!/usr/bin/python3
# AUTHOR: Mezie Gift
"""Defines a square class"""


class Square:
    """Square defines a square based on 1-square.py"""
    def __init__(self, size=0):
        self.__size = size
        """A TypeError is raised if size is not of type int.
        A ValueError is raised if size is less than 0.
        """
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):

        """method returns the area of a square"""

        return self.__size ** 2


sqr = Square()
sqr.area()
