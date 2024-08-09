#!/usr/bin/python3

"""
    Given n characters, this function calculates the minimum operations
"""


def minOperations(n):
    """
    A function that calculates the fewest number of operations
    needed to give a result of exactly n H characters in a file
    args: n: Number of characters to be displayed
    return:
           number of min operations
    """

    current = 1
    begin = 0
    index = 0
    while current < n:
        remainder = n - current
        if remainder % current == 0:
            begin = current
            current += begin
            index += 2
        else:
            current += begin
            index += 1
    return index
