#!/usr/bin/python3
# AUTHOR: Mezie Gift
"""Module defines a read_file function"""


def read_file(filename=""):
    """function reads the contents of a file.
    Args:
    filename: the name of the file that is to be read.
    """
    with open("my_file_0.txt", encoding = "utf-8") as myfile:
        print(myfile.read())
