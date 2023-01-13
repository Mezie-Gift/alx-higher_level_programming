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

    def to_json(self, attrs=None):
        """Method retrieves a dictionary representation of a Student instance.
        """
        if (type(attrs) == list and all(type(item) == str for item in attrs)):
            return {name: getattr(self, name) for
                    name in attrs if hasattr(self, name)}
        return self.__dict__

    def reload_from_json(self, json):
        """Method replaces all attributes of the Student instance
        Args:
           json: A dictionary with keys and values
        """
        for k, v in json.items():
            setattr(self, k, v)
