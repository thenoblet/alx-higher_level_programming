#!/usr/bin/python3

"""Multiply each element of a list by a given number using map.

Args:
    my_list (list): List of integers.
    number (int): The number to multiply each element by.

Returns:
    list: A new list with each element multiplied by the given number.
"""


def multiply_list_map(my_list=[], number=0):
        list(map(lambda x: x * number, my_list))
