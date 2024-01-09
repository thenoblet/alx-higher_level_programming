#!/usr/bin/python3

"""
Description: Function to create a list indicating whether each element
in the input list is divisible by 2.

Args:
    my_list (list): The input list of integers.

Returns:
    list or None: A list of booleans indicating whether each element
    in the input list is divisible by 2.
    Returns None if the input list is empty.
"""


def divisible_by_2(my_list=[]):
    if not my_list:
        return None

    return [True if element % 2 == 0 else False for element in my_list]
