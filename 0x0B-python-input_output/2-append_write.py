#!/usr/bin/python3
"""
This module contains the function read_lines.
"""


def append_write(filename="", text=""):
    """
    Appends text to the end of the specified file or creates the file 
    if it doesn't exist.

    Parameters:
    - filename (str): The name of the file to append to or create.
    - text (str): The text to be appended to the file.

    Returns:
    int: The number of characters appended to the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
