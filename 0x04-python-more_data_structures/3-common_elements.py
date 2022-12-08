#!/usr/bin/python3
#AUTHOR: Mezie Gift
def common_elements(set_1, set_2):
    """returns a set of common elements in two sets"""

    list_set1 = set(set_1)
    list_set2 = set(set_2)
    common = list_set1 & list_set2
    return (common)
