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
        self.name = name
        self.value = value
        if not isinstance(value, int):
            raise TypeError("{}  must be an integer".format(name))
        if value <= 0:
            raise ValueError("{}  must be greater than 0".format(name))
