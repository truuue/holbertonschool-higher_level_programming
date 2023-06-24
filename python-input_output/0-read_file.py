#!/usr/bin/python3
"""Simple module that reads a text file and print it to stdout"""


def read_file(filename=""):
    """Function that reads a text file"""
    with open(filename, encoding="utf-8") as file:
            print(file.read(), end="")
