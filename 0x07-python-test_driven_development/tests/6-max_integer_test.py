#!/usr/bin/python3

"""Unittest for max_integer([..])"""
import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    def test_valid_result(self):
        """Tests for valid inputs and valid outputs (expected results)."""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([-45, 32, 2129, -34]), 2129)

    def test_empty_list(self):
        """Tests for empty lists"""
        self.assertIsNone(max_integer([]))

    def test_invalid_input(self) -> None:
        """Tests for invalid input given to the function."""
        # test for invalid input
        with self.assertRaises(TypeError):
            max_integer(56)
            max_integer(89.34)
            max_integer([[9, 3], 4])

            # '>' is not supported between two dictionaries
            max_integer([{"one": 1, "two": 2}, {"three": 3, "four": 4}])

        with self.assertRaises(KeyError):
            max_integer({"one": 1, "two": 2})

    def test_all_negatives(self):
        """Tests for the maximum number in an all-negative numbers list."""
        self.assertEqual(max_integer([-1, -45, -4, -2, -56, -90, -100]), -1)

    def test_repeating_numbers(self):
        """Tests repeating numbers that are not the maximum integer."""
        self.assertEqual(max_integer([4, -1, -4, 4, 9, 5, 4, 10]), 10)
        self.assertEqual(max_integer([2, 4, 6, 4, 8]), 8)

    def test_repeating_max_numbers(self):
        """Tests for a maximum number that repeats itself in the list."""
        self.assertEqual(max_integer([100, 4, -2, 100, 23, 99, 100, -32]), 100)
