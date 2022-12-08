#!/usr/bin/python3

# AUTHOR: Mezie Gift
def only_diff_elements(set_1, set_2):
    """returns a set of all elements present in only one set"""

    list_1 = set(set_1)
    list_2 = set(set_2)
    compare = list_1 ^ list_2
    return (compare)
