#!/usr/bin/python3
# AUTHOR: Mezie Gift
def print_sorted_dictionary(a_dictionary):
    """function that prints a dictionary by ordered keys"""

    for i in sorted(a_dictionary):
        print("{}: {}".format(i, a_dictionary[i]))
