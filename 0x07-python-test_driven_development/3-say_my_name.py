#!/usr/bin/python3
# AUTHOR: Mezie Gift
"""Define say_my_name function"""

def say_my_name(first_name, last_name=""):
    """function prints a persons name.
    args:
        first_name: The person's first name
        last_name: The person's last name
    raises:
        TypeError: first_name must be a string (if first_name is not a string)
        TypeError: last_name must be a string (if last_name is not a string)
   prints: My name is <first name> <last name>
   """
    if (not isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if (not isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
