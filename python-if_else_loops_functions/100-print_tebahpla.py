#!/usr/bin/python3
for char in range(122, 96, -1):
    print("{:c}".format(char), end="")
    if char != 0:
        print("{:c}".format(char - 32), end="")
