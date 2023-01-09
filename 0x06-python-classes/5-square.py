#!/usr/bin/python3
# AUTHOR: Mezie Gift
"""Defines a square class"""


class Square:
    """Square defines a square based on 4-square.py"""
    def __init__(self, size=0):
        """initializing size"""
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """A TypeError is raised if size is not of type int.
        A ValueError is raised if size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """method returns the area of a square"""
        return self.__size ** 2

    def my_print(self):
        """Method prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__size):
                [print("{}".format("#"), end="") for j in range(self.__size)]
                print("")
