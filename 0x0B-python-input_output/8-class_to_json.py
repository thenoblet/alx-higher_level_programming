#!/usr/bin/python3

"""
A module with a function that returns the dictionary description with
simple data structure (list, dictionary, string, integer, and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """
    Convert an instance of a class to a dictionary for JSON serialization.

    Parameters:
    - obj: An instance of a class with serializable attributes.

    Returns:
    - dict: A dictionary representation of the object for JSON serialization.
    """
    if not hasattr(obj, '__dict__'):
        raise ValueError("Input is not an instance of a class")

    result_dict = {}

    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            result_dict[key] = value

    return result_dict
