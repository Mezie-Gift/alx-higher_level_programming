#!/usr/bin/python3
# AUTHOR: Mezie Gift
"""Module defines a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializing attributes of the new square
        Args:
            size(int): size of the square
            x(int): the x coordinate
            y(int): the y cordinate
            id(int): the square's identity
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get/return size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """set size of square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Method updates the class Square
    args:
         (*args):is the list of arguments - no-keyworded arguments
                 - first argument = id
                 - second argument = size
                 - third argument = x
                 - fourth argument = y
         (**kwargs): a pointer to dictionary: key/value
                 - **kwargs must be skipped if *args exists and is not empty.
        """
        if args and len(args) != 0:
            chk = 0
            for arg in args:
                if chk == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif chk == 1:
                    self.size = arg
                elif chk == 2:
                    self.x = arg
                elif chk == 3:
                    self.y = arg
                chk = chk + 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
