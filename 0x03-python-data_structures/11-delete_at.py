#!/usr/bin/python3

"""
Description: Function to delete an element at a specified
index from a list.

Args:
    my_list (list): The input list.
    idx (int): The index of the element to be deleted.
Returns:
    list: The modified list after deleting the element.
          Returns the original list if the index is out of bounds.
"""


def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list

    del my_list[idx]
    return my_list
