#!/usr/bin/python3
# AUTHOR: Mezie Gift
def print_reversed_list_integer(my_list=[]):
    """Prints list of integers in reverse"""
    if my_list:
        my_list.reverse()
        for i in range(len(my_list)):
            print("{:d}".format(my_list[i]))
