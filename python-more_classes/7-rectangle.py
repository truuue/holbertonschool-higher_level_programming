#!/usr/bin/python3
"""This is a project on a rectangle object"""


class Rectangle:
    """This is a rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        rectangle_str = ""
        if self.width == 0 or self.height == 0:
            return rectangle_str
        for i in range(self.height):
            rectangle_str += str(self.print_symbol) * self.width + "\n"
        return rectangle_str[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
