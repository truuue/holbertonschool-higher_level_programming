#!/usr/bin/python3
def uniq_add(my_list):
    unique_values = set(my_list)
    sum = 0
    for num in unique_values:
        sum += num
    return sum
