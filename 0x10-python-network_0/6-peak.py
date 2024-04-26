#!/usr/bin/python3

def find_peak(list_of_integers) -> "int | None":
    """Finds a peak in a list of unsorted integers using binary search.

    Args:
        list_of_integers (list): A list of unsorted integers.

    Returns:
        int | None: The peak of the list of integers, or None
        if the list is empty.

    Algorithm:
        This function finds a peak in a list of unsorted integers
        using binary search.
        A peak is defined as an element that is greater than or equal
        to its neighbors. The algorithm repeatedly divides the search
        space in half until it finds a peak.
        It checks the middle element of the current search space and
        compares it with its neighbors. If the middle element is greater
        than its right neighbor, the peak must be in the left half of the
        list. If the middle element is less than its right neighbor,
        the peak must be in the right half of the list.
        The algorithm updates the search space accordingly and continues
        the process until the search space is reduced to a single element,
        which is the peak.

    Complexity:
        Time Complexity: O(log n), where n is the number of elements in
        the list_of_integers. The binary search algorithm reduces the
        search space by half in each iteration, leading to a logarithmic
        time complexity.
        Space Complexity: O(1).
            The algorithm uses only a constant amount of additional space
            for variables, regardless of the size of the input list.
    """

    # Check if the list is empty
    if not list_of_integers:
        return None

    # Define the boundaries of the search space
    left = 0
    right = len(list_of_integers) - 1

    # Binary search to find the peak
    while left < right:
        mid = (left + right) // 2
        # Check if the midpoint is a peak
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid  # Peak found in the left half
        else:
            left = mid + 1  # Peak found in the right half

    # At this point, left and right will converge to the peak
    return list_of_integers[left]
