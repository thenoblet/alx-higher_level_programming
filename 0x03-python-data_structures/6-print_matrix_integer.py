#!/usr/bin/python3

"""
Description: Function prints each row of a matrix
of integers in a formatted way.
"""


def print_matrix_integer(matrix=[[]]):
    """
    Could do:
    for row in matrix:
        print(*row)

    But Guillaume & Julien said to use str.format so,
    here you go...
    """
    for row in matrix:
        print(" ".join("{:d}".format(element) for element in row))
