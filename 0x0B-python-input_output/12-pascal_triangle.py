#!/usr/bin/python3

"""
This module defines a function to generate Pascal's Triangle.

Functions:
- pascal_triangle(n): Generates Pascal's Triangle up to 'n' rows.
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the specified number of rows.

    Parameters:
    - n (int): The number of rows to generate in Pascal's Triangle.

    Returns:
    List[List[int]]: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    pascal_triangle = [[1]]
    row = []

    # Loop to generate the subsequent rows of Pascal's Triangle.
    for i in range(n - 1):
        for j in range(len(pascal_triangle[i]) + 1):
            if j == 0 or j == len(pascal_triangle[i]):
                row.append(1)
            else:
                row.append(pascal_triangle[i][j - 1] + pascal_triangle[i][j])
        pascal_triangle.append(row[:])
        row.clear()
    return pascal_triangle
