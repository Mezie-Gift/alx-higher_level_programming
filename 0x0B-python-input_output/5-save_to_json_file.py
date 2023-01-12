#!/usr/bin/python3
# AUTHOR: Mezie Gift
"""Module defines save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """function writes an Object to a text file, using a JSON representation
    Args:
        my_obj: The objet that is to be written
        filename: The file to write objects to
    """
    f = json.dumps(my_obj)
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(f)
