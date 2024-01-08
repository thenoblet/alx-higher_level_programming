#!/usr/bin/python3

"""
Description: Function removes occurrences of the letter 'c'
(both uppercase and lowercase) from a given string using a
concise list comprehension.
"""


def no_c(my_string):
    return "".join(char for char in my_string if char.lower() != "c")
