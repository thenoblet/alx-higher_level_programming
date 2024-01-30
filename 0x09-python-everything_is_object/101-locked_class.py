#!/usr/bin/python3
class LockedClass:
    """
    A class demonstrating the use of __slots__ to restrict attribute creation.

    Attributes:
    - first_name (str): A slot for storing the first name of an instance.

    Note:
    The __slots__ attribute is used to explicitly declare a list of allowed
    ittribute names.
    Instances of this class will only be able to have attributes listed in __slots__.
    This can be useful for memory optimization and to prevent the creation of
    arbitrary attributes.
    """
    __slots__ = ["first_name"]
