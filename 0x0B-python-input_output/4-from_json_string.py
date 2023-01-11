#!/usr/bin/python3
# AUTHOR: Mezie Gift
"""Mode defines from_json_string function"""
import json


def from_json_string(my_str):
    """Returns Python data structure) represented by a JSON string:
    Args:
        my_obj: the object to return in jason format
    """
    js = my_str
    return json.loads(js)
