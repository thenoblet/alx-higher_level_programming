#!/usr/bin/python3

""" Module that defines a locked class"""


class LockedClass:
    """
    A class demonstrating the use of __slots__ to restrict attribute creation.

    Attributes:
    - first_name (str): A slot for storing the first name of an instance.
    """
    __slots__ = ["first_name"]
