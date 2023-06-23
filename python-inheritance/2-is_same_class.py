#!/usr/bin/python3
"""That's a module that check if the object is an instance"""


def is_same_class(obj, a_class):
    """The checker function"""
    if type(obj) is a_class:
        return True
    else:
        return False
