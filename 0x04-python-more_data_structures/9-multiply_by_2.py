#!/usr/bin/python3
# AUTHOR: Mezie Gift
def multiply_by_2(a_dictionary):
    """Function returns a new dictionary with all values multiplied by 2"""

    return {key: value * 2 for key, value in a_dictionary.items()}
