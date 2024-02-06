#!/usr/bin/python3

"""Model that contains a function that writes or overwrites to a file."""


def write_file(filename="", text=""):
    """
    Writes or overwrites text to a specified file.

    Parameters:
    - filename (str): The name of the file to write to.
    - text (str): The text to be written to the file.

    Returns:
    int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
