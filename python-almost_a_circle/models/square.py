#!/usr/bin/python3
"""A simple module for a square that inherit from rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """The square class method"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """A simple function that use __str__ method"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
