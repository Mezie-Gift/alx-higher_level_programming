#!/usr/bin/python3
# AUTHOR: Mezie Gift
def search_replace(my_list, search, replace):
    """This function replaces all occurrences
of an element by another in a new list"""

    new_list = my_list.copy()

    for i in range(len(my_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return (new_list)
