#!/usr/bin/python3

"""
Defines a blueprint for a Square
"""


class Square:
    """
    A blueprint for working with squares
    """

    def __init__(self, size=0):
        """
        Initializes the Square class

        Args:
            size (int, optional): the size of the square. Defaults to 0.

        Raises:
            TypeError: when the size received is not an integer
            ValueError: when the size if not a positive integer
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
