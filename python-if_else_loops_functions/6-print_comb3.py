#!/usr/bin/python3
for num in range(0, 100):
    if i % 10 > num / 10:
        if num == 89:
            print("{:02d}".format(num))
        else:
            print("{:02d}".format(num), end=", ")
