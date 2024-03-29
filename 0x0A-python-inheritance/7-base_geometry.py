#!/usr/bin/python3


"""This module contains the class BaseGeometry."""


class BaseGeometry:
    """A base class for geometry shapes."""

    def area(self):
        """
        Area of a geometry, not implemented by default.
        Raises:
            Exception: When area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Function that validates that value is integer.
        Args:
            name (str): The name of the variable to be validated.
            value (int): The value to be validated.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
