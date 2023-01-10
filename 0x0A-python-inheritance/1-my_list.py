#!/usr/bin/python3
# AUTHOR: Mezie Gift
"""module prints sorted lists"""


class MyList(list):
    """MyList inherits from lists"""
    def print_sorted(self):
        """prints a sorted list of integers"""
        lst = sorted(self)
        print(lst)
