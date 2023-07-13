#!/usr/bin/python3
""" Module for fetching number of operations"""


def minOperations(n):
    """
    minOperations
    Fetches fewest number of operations needed to result in exactly n H characters
    """
    # all outputs should be at least two char:
if (n < 2):
    return 0
    x, y = 0, 2
while y <= n:
        # if n evenly divides by y
    if n % y == 0:
            # total even-divisions by y = total operations
        x += y
            # set n to the remainder
        n = n / y
            # reduce y to find remaining smaller vals that evenly-divide n
        y -= 1
        # increment y until it evenly-divides n
    y += 1
return x
