#!/usr/bin/python3
# AUTHOR: Mezie Gift
"""Module defines a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """A sub-class of Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize attributes of a rectangle
        Args:
           width: width of of the rectangle
           height: the rectangle's height
           x=0: the x coordinate of the rectangle
           y=0: the y coordinate of the rectangle
           id: identity of the rectangle
        Raises:
           TypeError: if either width or height is not of type int
           TypeError: if either x or y is not an int
           ValueError: if either width or height is < 0
           ValueError: if either x or y is not an int"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """return/get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width of the rectangle
        Args:
            value (int): value of the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """return/get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height of the rectangle
        Args:
            value (int): value of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """return/get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x coordinate of a rectangle
        Args:
            value (int): the value of the x coordinate
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be greater >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """return/get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y coordinate of a rectangle
        Args:
            value (int): the value of y coordinate
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Method returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """Method that prints in stdout the
        Rectangle instance with the character #"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update the Rectangle.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
