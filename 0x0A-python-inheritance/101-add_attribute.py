#!/usr/bin/python3
"""Module defines add_attribute method"""


def add_attribute(obj, arg, value):
    """Methods add new attribute to an object if possible.
    Args:
    obj: The object in question
    arg: (str) name of attribute to be added
    value: attribute value
    Errors:
    TypeError: if attribute cant be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, arg, value)
