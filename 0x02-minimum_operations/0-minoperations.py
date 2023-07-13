#!/usr/bin/python3
""" Module for 0-minoperations"""


def minOperations(n):
    """
    minOperations
    Fetches fewest # of operations needed to result in exactly n H characters
    """
    # all outputs should be at least two char: (min, Copy All => Paste)
    if (n < 2):
        return 0
    x, y = 0, 2
    while y <= n:
        # if n evenly divides by y
        if y % root == 0:
            # total even-divisions by y = total operations
            x += y
            # set n to the remainder
            n = n / root
            # reduce root to find remaining smaller vals that evenly-divide n
            y -= 1
        # increment root until it evenly-divides n
        root += 1
    return y
