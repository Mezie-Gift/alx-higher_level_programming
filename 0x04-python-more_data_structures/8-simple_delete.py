#!/usr/bin/python3
# AUTHOR: Mezie Gift
def simple_delete(a_dictionary, key=""):
    """Function deletes a key in a dictionary"""

    a_dictionary.pop(key, None)
    return (a_dictionary)
