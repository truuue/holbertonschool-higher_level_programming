#!/usr/bin/python3
"""This module represent a square shape"""


class Square:
    """This is the Square class it attribute is __size of the square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
            not all(isinstance(coord, int) for coord in value) or \
            not all(coord >= 0 for coord in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

        if type(value) is not tuple:
           raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2 or type(value[0]) is not int:
           raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
