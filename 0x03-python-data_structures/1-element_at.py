#!/usr/bin/python3

"""
Description: Function retrieves the element at the specified
index in `my_list`.
Checks if the index is within the valid range before
accessing the element.
If the index is out of bounds, returns None;
otherwise, returns the element at the index.
"""


def element_at(my_list, idx):
    if 0 < idx >= len(my_list):
        return None

    return my_list[idx]
