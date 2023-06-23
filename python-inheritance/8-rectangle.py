#!/usr/bin/python3
"""A simple module for a basegeaometry"""


class BaseGeometry:
    """A geometry module"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A rectangle class heriting from BaseGeometry"""

    def __init__(self, width, height):
        """A constructor method that init a new rectangle object"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
