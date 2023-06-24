#!/usr/bin/python3
"""This is the "Print Square" module"""


def print_square(size):
    """Print a perfect square given a valid int or float argument"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
