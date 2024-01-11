#!/usr/bin/python3


def weight_average(my_list=[]):
    """
    Calculate the weighted average of a list of score and weight pairs.

    Args:
        my_list (list): List of tuples, each containing a score and its weight.

    Returns:
        float: Weighted average or 0 if the input is invalid.
    """

    if my_list is None or len(my_list) < 1:
        return 0

    # Unpack the list of tuples into two lists (scores and weights)
    scores, weights = zip(*my_list)

    # Calculate the weighted average
    weighted_sum = sum(score * weight for score, weight in my_list)
    total_weight = sum(weights)

    return weighted_sum / total_weight if total_weight != 0 else 0
