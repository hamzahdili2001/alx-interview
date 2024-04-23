#!/usr/bin/python3
"""
0-pascal_triangle.py
"""


def pascal_triangle(n):
    """
    function that returns a list of lists of integers representing
    the Pascal’s triangle of n

    Args:
        n (int): The number of rows to generate in the Pascal's triangle.

    Returns:
        list: A list of lists representing the Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    current_row = 1

    while current_row < n:
        row = [1]
        for i in range(1, current_row):
            row.append(
                triangle[current_row - 1][i - 1]
                + triangle[current_row - 1][i]
            )
        row.append(1)
        triangle.append(row)
        current_row += 1

    return triangle
