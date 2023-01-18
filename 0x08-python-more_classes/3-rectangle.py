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
        self.width = width
        self.height = height

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

    def area(self):
        """Returns the area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0 * 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Prints rectangle with the character '#'"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rect = []
            for i in range(self.__height):
                [rect.append('#') for j in range(self.__width)]
                if i != self.__height - 1:
                    rect.append("\n")
            return ("".join(rect))
