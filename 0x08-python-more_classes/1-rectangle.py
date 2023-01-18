#!/usr/bin/python3
# AUTHOR: Mezie Gift
"""Module defines a rectangle class"""


class Rectangle:
    """A rectangle class"""
    def __init__(self, width=0, height=0):
        """Initializing a rectangle
        Args:
          width: width of the rectangle
          height: height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrives/returns width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """retrieves/returns height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height of a rectangle"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
