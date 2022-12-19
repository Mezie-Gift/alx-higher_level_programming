#!/usr/bin/python3
# AUTHOR: Mezie Gift
def safe_print_integer(value):
    """This function prints an integer with "{:d}".format()"""
    try:
        print("{:d}".format(value))
        return(True)
    except (ValueError, TypeError):
        return(False)
