#!/usr/bin/python3
# AUTHOR: Mezie Gift
"""Module defines a BaseaGeometry class that
   is the parent of rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class defines a rectangle"""
    def __init__(self, width, height):
        """class defines attributes of a rectangle
        Args:
        (int)width: width of the rectangle
        (int)height: height of the rectangle
        """
        self.__width = width
        self.__height = height
