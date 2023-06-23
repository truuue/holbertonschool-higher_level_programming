#!/usr/bin/python3
"""A simple module for a basegeaometry"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))
