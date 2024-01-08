#!/usr/bin/python3

"""
Description: Function prints elements in `my_list`
in reverse order.
Uses list slicing to reverse the list and then
iterates through each element.
"""


def print_reversed_list_integer(my_list=[]):
    # Check if the list is empty
    if not my_list:
        return None

    """
    Could use listcomps:
    `[print("{:d}".format(x)) for x in my_list[::-1]]`
    but there no need to create another list so for loop it is
    """
    for x in my_list[::-1]:
        print("{:d}".format(x))
