#!/usr/bin/python3
""" Module that calculates the fewest number of operations needed"""


def minOperations(n):
    """
    minOperations
    fetches fewest number of operations needed to result in exactly n H characters in the file
    """
    if (n < 2):
        return 0
    x, y = 0, 2
    while y <= n:
        if n % y == 0:
            x += y
            n = n / y
            y -= 1
        y += 1
    return x
