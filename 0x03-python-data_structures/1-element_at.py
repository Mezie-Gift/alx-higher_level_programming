#!/usr/bin/python3
# AUTHOR: Mezie Gift
def element_at(my_list, idx):
    """This function retrives an element at certain index"""
    i = len(my_list)
    if idx < 0 or idx > i - 1:
        return None
    else:
        return my_list[idx]
