#!/usr/bin/python3

"""This module contains the function read_file."""


def read_file(filename=""):
    """
    Reads and prints the contents of the specified file.

    Parameters:
    - filename (str): The name of the file to read.

    Returns:
    None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
