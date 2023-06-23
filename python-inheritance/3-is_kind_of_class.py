#!/usr/bin/python3
"""That's a module that check if the object is an instance"""


def is_kind_of_class(obj, a_class):
    """The checker function"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
