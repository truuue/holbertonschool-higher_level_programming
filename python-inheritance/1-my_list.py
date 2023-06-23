#!/usr/bin/python3
"""That's a module that ineriths from a list"""

class MyList(list):
    def print_sorted(self):
        """This is the function"""
        return sorted(self)
