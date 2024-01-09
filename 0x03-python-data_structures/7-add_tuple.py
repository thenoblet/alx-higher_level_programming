#!/usr/bin/python3

"""
Description: Function adds corresponding elements of two tuples
and returns a new tuple.

Args:
    tuple_a (tuple): First input tuple.
    tuple_b (tuple): Second input tuple.

Returns:
    tuple: A new tuple containing the sum of corresponding
    elements from tuple_a and tuple_b.
"""


def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least 2 elements by...
    # ...padding with zeros if needed
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    # Unpack elements from tuples
    x, y = tuple_a[:2]
    n, m = tuple_b[:2]

    # Calculate sums of corresponding elements
    first_elements_sum = x + n
    second_elements_sum = y + m

    # Create a new tuple with the sums
    new_tuple = first_elements_sum, second_elements_sum
    return new_tuple
