#!/usr/bin/python3
# AUTHOR: Mezie Gift
"""Module defines a append_write function"""


def append_write(filename="", text=""):
    """function appends text to a file
    Args:
        filename: The file to write to
        text: The text to write into the file
    """
    with open(filename, mode="a", encoding="utf-8") as my_file:
        my_file.write(text)
        return len(text)
