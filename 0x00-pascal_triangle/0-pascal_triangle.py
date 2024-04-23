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

    triangle = []

    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            prev_row = triangle[i - 1]

            current_row = [1]

            current_row.extend(
                [
                    prev_row[j] + prev_row[j + 1]
                    for j in range(len(prev_row) - 1)
                ]
            )

            current_row.append(1)

            triangle.append(current_row)

    return triangle
