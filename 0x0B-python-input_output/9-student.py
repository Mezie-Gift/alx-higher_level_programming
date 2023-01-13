#!/usr/bin/python3
# AUTHOR: Mezie Gift
"""Module defines a Student class"""


class Student(object):
    """class defines a student"""
    def __init__(self, first_name, last_name, age):
        """initializing a student attributes:
        Args:
            first_name: A student's first name
            last_name: A student's last name
            age: The student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Method retrieves a dictionary representation of a Student instance.
        """
        return self.__dict__
