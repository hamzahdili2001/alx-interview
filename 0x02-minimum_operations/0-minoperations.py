#!/usr/bin/python3
"""0-minoperations"""


def minOperations(n):
    """method to find the minimum operations to reach n characters"""

    if n <= 1:
        return 0
    for i in range(2, n + 1):
        if n % i == 0:
            return minOperations(n // i) + i
    return 0
