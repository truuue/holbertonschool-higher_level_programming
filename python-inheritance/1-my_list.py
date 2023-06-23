#!/usr/bin/python3
"""That's a module that ineriths from a list"""

class MyList(list):
    """A class that ineriths from a list"""
    def print_sorted(self):
        """This is a public instance method"""
        print(sorted(self))
