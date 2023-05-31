#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            num = 32
        else:
            num = 0
        print("{:c}".format(ord(str[i]) - num), end="")
    print()
