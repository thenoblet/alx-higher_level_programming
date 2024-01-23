#!/usr/bin/python3

"""
Defines a blueprint for a Square
"""


class Square:
    """
    A blueprint for working with squares
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the Square class

        Args:
            size (int, optional): the size of the square. Defaults to 0.
            position (tuple, optional): the coordinates of the square.
            Defaults to (0, 0)
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple or len(position) != 2 or\
           type(position[0]) is not int or type(position[1]) is not int or\
           position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    def area(self):
        """
        Computes and returns the area of the square

        Returns:
            int: the area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Retrieves the size of the square

        Returns:
            int: the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets or updates the size of the square

        Args:
            size (int): the size of the square

        Raises:
            TypeError: when the size received is not an integer
            ValueError: when the size if not a positive integer
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        Prints the representation of the square using hashes '#'
        """
        if (self.__size != 0):
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print("{}{}".format(" " * self.__position[0], "#" * self.__size
                                    ))
        if (not self.__size):
            print()

    @property
    def position(self):
        """
        Retrieves the 2-tuple containing the coordinates of the square

        Returns:
            tuple[int, int]: a 2-tuple containing the coordinates of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets or updates the coordinate of the square

        Args:
            position (tuple[int, int]): a 2-tuple containing the
            coordinates of the square

        Raise:
            TypeError: when the argument received is not a 2-tuple or if any of
            the values in the 2-tuple is not an integer
        """
        if type(value) is not tuple or len(value) != 2 or\
           type(value[0]) is not int or type(value[1]) is not int or\
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
