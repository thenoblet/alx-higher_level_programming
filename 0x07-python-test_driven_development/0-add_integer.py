#!/usr/bin/python3

"""
This module provides a function for calculating the sum
of two numbers. The function automatically casts input
operands to integers if they are floats.
The default value for the second operand is 98 if not provided.
"""


def add_integer(a, b=98):
    """ Calculates the sum of two numbers

    Parameters:
        - a (float | int ): first operand
        - b (float | int ): second operand

    Returns:
        int: The sum of the operands

    Raises:
        TypeError: If either operand is not an integer or float.

    Tests:
        >>> add_integer(3, 4)
        7
        >>> add_integer(3)
        101
        >>> add_integer(3, -10)
        -7
        >>> add_integer(0, 0)
        0
        >>> add_integer(-100, -3)
        -103
        >>> add_integer(9.8)
        107
        >>> add_integer(2**31 - 1, 1)
        Traceback (most recent call last):
            ...
        OverflowError: Number too large
        >>> add_integer(-(2**31), -1)
        Traceback (most recent call last):
            ...
        OverflowError: Number too large
        >>> add_integer("3", "2")
        Traceback (most recent call last):
        ...
        TypeError: a must be an integer
        >>> add_integer()
        Traceback (most recent call last):
        ...
        TypeError: add_integer() missing 1 required positional argument: 'a'
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    result = int(a) + int(b)
    if result > (2**31 - 1) or result < -(2**31):
        raise OverflowError("Number too large")

    return result
