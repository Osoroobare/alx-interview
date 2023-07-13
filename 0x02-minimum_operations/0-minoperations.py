#!/usr/bin/python3


"""
Module for minimum operations
"""


def minOperations(n):
    """Gets fewest number of operations needed
    """
#All outputs should be atleast two chars
    ans = 0
    a = 2
    while n > 1:
        while n % a == 0:
            ans += a
            n /= a
        a += 1
    return ans
