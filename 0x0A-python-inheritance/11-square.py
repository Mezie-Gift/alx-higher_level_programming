#!/usr/bin/python3
# AUTHOR: Mezie Gift
"""Module defines a geometry class"""


class BaseGeometry(object):
    """class defines the method 'area'"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method validates value
        Args:
           name: argument passed
           value: the object to be validated
        Errors:
           TypeError: if value is not an integer
           ValueError: if value is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("{}  must be an integer".format(name))
        if value <= 0:
            raise ValueError("{}  must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string


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
