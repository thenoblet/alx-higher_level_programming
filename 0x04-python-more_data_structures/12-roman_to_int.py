#!/usr/bin/python3

"""
Convert a Roman numeral to an integer.

Args:
    roman_string (str): The input Roman numeral.

Returns:
    int: The corresponding integer value.

    Returns 0 if the input is not a valid Roman numeral or an empty string.
"""


def roman_to_int(roman_string):
    # Check if the input is empty or not a string
    if not roman_string or type(roman_string) != str:
        return 0

    total = 0
    numeral_values = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
            }

    # Iterate through the reversed Roman numeral string
    for current_numeral in reversed(roman_string):
        current_value = numeral_values[current_numeral]
        total += current_value if total < current_value * 5 else -current_value
    return total
