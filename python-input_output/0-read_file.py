#!/usr/bin/python3
"""Simple function that reads a text file and print it to stdout"""

def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end="")
