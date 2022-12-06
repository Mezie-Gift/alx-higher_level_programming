#!/usr/bin/python3
# AUTHOR: Mezie Gift
def print_reversed_list_integer(my_list=[]):
    """Prints lisy of integers in reverse"""
    for num in reversed(my_list):
        print("{:d}".format(num))
