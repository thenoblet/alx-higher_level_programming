#!/usr/bin/python3

"""
A module with a function that divides all elements of a matrix by a given
divisor
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor

    Parameters:
    - matrix (list of lists): The matrix to be divided, containing integers or floats.
    - div (int or float): The divisor.

    Returns:
    A new matrix with elements rounded to 2 decimal places after division.

    Raises:
    - TypeError: If div is not a number, matrix is not a list of lists, matrix rows have
      inconsistent lengths, or matrix elements are not integers or floats.
    - ZeroDivisionError: If div is zero.
    """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for index, row in enumerate(matrix):
        if type(row) is not list or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        if index > 0 and len(matrix[index]) != len(matrix[index - 1]):
                raise TypeError("Each row of the matrix must have the same size")

        for element in row:
            if type(element) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    return list(map(lambda row: list(map(lambda x: round(x / div, 2), row)), matrix))
