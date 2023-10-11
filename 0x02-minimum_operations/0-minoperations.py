#!/usr/bin/python3
"""
This module contains the function minOperations(n)
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in
    exactly n 'H' characters in the file.
    """
    if n <= 1:
        return n

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            n //= divisor
            operations += divisor
        divisor += 1

    return operations