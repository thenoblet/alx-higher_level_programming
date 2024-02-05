#!/usr/bin/python3
"""
This module contains the class MyList.
"""


class MyList(list):
    """
    Class that inherits from list.
    """
    def print_sorted(self):
        """
        Function that prints a list sorted.
        """
        print(sorted(self))
