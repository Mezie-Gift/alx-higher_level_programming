#!/usr/bin/python3
# AUTHOR: Mezie Gift
"""Module defines a is_same_class function"""


def is_same_class(obj, a_class):
    """function returns True if the object is exactly
    an instance of the specified class,
        otherwise returns False
    Args:
        obj: The object in question
        a_class: The class that obj is checked against
    """
    if type(obj) == a_class:
        return True
    else:
        return False
