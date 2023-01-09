#!/usr/bin/python3
# AUTHOR: Mezie Gift
"""Defines a square class"""


class Square:
    """Defines a square based on 5-square.py"""
    def __init__(self, size=0, position=(0, 0)):
        """initializing square attributes"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """set size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """A TypeError is raised if size value is not of type int.
        A ValueError is raised if size value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """set position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """A TypeError is raised if the value of
               position is not a tuple of two
                   positive integers
        """
        if not isinstance(value, tuple):
            if not len(value) == 2:
                if not all(isinstance(number, int) for number in value):
                    if not all((number >= 0) for number in value):
                        raise TypeError("""position
must be a tuple of 2 positive integers""")
        else:
            self.__position = value

    def area(self):
        """Method returns area of a square"""
        return self.__size ** 2

    def my_print(self):
        """Method prints in stdout the square with the character '#'"""
        if self.__size == 0:
            print("")
        else:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
