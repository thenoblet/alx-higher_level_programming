#!/usr/bin/python3

"""
Description: Function replaces an element at the specified
index in `my_list` with the given `element`.
Checks if the index is within the valid range before
performing the replacement.
If the index is out of bounds, returns the original list;
otherwise, returns the modified list.
"""


def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list

    my_list[idx] = element

    return my_list
