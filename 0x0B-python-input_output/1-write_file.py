#!/usr/bin/python3
# AUTHOR: Mezie Gift
"""Module defines a write_file function"""


def write_file(filename="", text=""):
    """function writes text to a file
    Args:
        filename: The file to write to
        text: The text to write into the file
    """
    with open(filename, mode="w", encoding="utf-8") as my_file:
        my_file.write(text)
        return len(text)
