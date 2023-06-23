#!/usr/bin/python3
"""A simple module for a basegeaometry"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class heriting from BaseGeometry"""

    def __init__(self, width, height):
        """A constructor method that init a new rectangle object"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
