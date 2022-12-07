#!/usr/bin/python3
# Author: Mezie Gift

def uniq_add(my_list=[]):
    """adds all unique integers in a list (only once for each integer)"""

    single_elements = set(my_list)
    total = sum(single_elements)
    return total
