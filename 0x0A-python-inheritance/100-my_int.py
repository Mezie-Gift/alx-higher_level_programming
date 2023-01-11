#!/usr/bin/python3
# AUTHOR: Mezie Gift
"""Module defines My_int class"""


class MyInt(int):
    """class defines a reverse operation for
    opertor'==' and '!='
    """

    def __eq__(self, value):
        """Method reverses the '==' with the '!=' operator"""
        result = self.real != value
        return (result)

    def __ne__(self, value):
        """Method reverses the '!=' operator"""
        result = self.real == value
        return (result)
