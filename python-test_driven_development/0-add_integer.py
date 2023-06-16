#!/usr/bin/python3
"""Function that add two integer"""


def add_integer(a, b=98):
    """here is the function that print the value or print the error"""
    if a is isinstance(a, int) or a is isinstance(a, float):
        return int(a) + int(b)
    else:
        raise TypeError("a must be an integer")

    if b is isinstance(b, int) or b is isinstance(b, float):
        return int(a) + int(b)
    else:
        raise TypeError("b must be an integer")
