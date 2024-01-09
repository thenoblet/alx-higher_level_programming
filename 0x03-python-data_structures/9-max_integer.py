#!/usr/bin/python3

"""
Description: Function to find the maximum integer in a list.
Args:
    my_list (list): The input list of integers.
Returns:
    int or None: The maximum integer in the list,
    or None if the list is empty.
"""


def max_integer(my_list=[]):
    if not my_list:
        return None

    return sorted(my_list)[-1]
