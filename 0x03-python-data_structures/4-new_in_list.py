#!/usr/bin/python3

"""
Description: Function replaces an element at the specified
index in `my_list` with the given `element`.
Checks if the index is within the valid range before
performing the replacement.
If the index is out of bounds, returns the original list;
otherwise, returns the modified list.
"""


def new_in_list(my_list, idx, element):
    # Check if the index is within the valid range
    if 0 <= idx < len(my_list):
        modified_list = my_list.copy()
        modified_list[idx] = element

        return modified_list

    # If the index is out of bounds, return the original list
    return my_list
