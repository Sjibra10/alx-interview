#!/usr/bin/python3
"""Module"""


def minOperations(n):
    """ calculates the fewest number of operations needed
        to result in exactly n H
        characters in the file."""
    if n <= 1:
        return 0

    operations = 0
    current_h = 1
    clipboard = current_h
    while current_h < n:
        if n % current_h == 0:
            clipboard = current_h
            operations += 1
        current_h += clipboard
        operations += 1
    return operations
