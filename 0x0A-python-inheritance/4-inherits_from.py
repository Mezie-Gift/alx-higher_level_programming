#!/usr/bin/python3
# AUTHOR: Mezie Gift
"""Module defines inherits_from()"""


def inherits_from(obj, a_class):
    """Function returns True if the object is an
    instance of a class that inherited (directly or
    indirectly) from the specified class ; otherwise False.
    Args:
       obj: The object in question
       a_class: The class that obj is to be checked against.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
