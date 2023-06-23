#!/usr/bin/python3
"""A module that check if the object is an instance"""


def inherits_from(obj, a_class):
    """Function that returns check if obj is a type of a_class"""
    if type(obj) is not a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
