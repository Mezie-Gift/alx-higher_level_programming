#!/usr/bin/python3
# AUTHOR: Mezie Gift
"""Module defines a class 'Square' that inherits
 from Rectangle (9-rectangle.py)"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class represents a square based on Super.Rectangle"""
    def __init__(self, size):
        """initializing attributes of the square
        Args:
        size: size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__size) + "/" + str(self.__size)
        return string
