#!/usr/bin/python3
# AUTHOR: Mezie Gift
"""Module defines is_kind_of_class()"""


def is_kind_of_class(obj, a_class):
    """Functiin returns True if the object is an
    instance of, or if the object is an instance of
    a class that inherited from the specified class;    otherwise False.
    Args:
       obj: The object in question
       a_class: The class that obj is to be checked against.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
