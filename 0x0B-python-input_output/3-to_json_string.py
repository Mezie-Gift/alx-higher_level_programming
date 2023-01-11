#!/usr/bin/python3
# AUTHOR: Mezie Gift
"""Mode defines to_json_string function"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)
    Args:
        my_obj: the object to return in jason format
    """
    js = my_obj
    return json.dumps(js)
