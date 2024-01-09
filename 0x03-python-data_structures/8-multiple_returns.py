#!/usr/bin/python3

"""
Description: Function provides information about the input sentence.

Args:
    sentence (str): The input sentence.

Returns:
    tuple or None: A tuple containing information about the sentence,
    or None if the sentence is empty.
        Element 1 (int): Length of the sentence.
        Element 2 (str): First character of the sentence.
"""


def multiple_returns(sentence):
    if len(sentence) == 0:
        return None

    return len(sentence), sentence[0]
