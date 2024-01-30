#!/usr/bin/python3
def magic_string():
    """
    A function that generates a magic string containing repeated instances
    of "BestSchool."

    Returns:
    str: A string with "BestSchool" repeated a number of times based on the
    function's invocation count.

    Usage:
    Each time the function is called, it increments the count and generates a
    string with "BestSchool" repeated according to the current count.

    Example:
    >>> magic_string()
    'BestSchool'
    >>> magic_string()
    'BestSchool, BestSchool'
    >>> magic_string()
    'BestSchool, BestSchool, BestSchool'
    """
    magic_string.count = getattr(magic_string, 'count', 0) + 1
    return ", ".join(["BestSchool" for i in range(magic_string.count)])
