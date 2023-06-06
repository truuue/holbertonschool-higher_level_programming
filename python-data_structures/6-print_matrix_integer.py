#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for i in range(len(line)):
            print("{:d}".format(line[i]), end="")
            if i != len(line) - 1:
                print(" ", end="")
        print()
