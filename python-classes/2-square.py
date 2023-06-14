#!/usr/bin/python3
"""This module represent a square shape"""
class Square:
    """This is the Square class it attribute is __size of the square"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
