#!/usr/bin/python3
"""Simple module that reads a text file and print it to stdout"""


def write_file(filename="", text=""):
    """Function that reads a text file"""
    with open(filename, "w",encoding="utf-8") as file:
        return file.write(text)
