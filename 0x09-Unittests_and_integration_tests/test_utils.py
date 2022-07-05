#!/usr/bin/env python3
"""
Class to test the functions in the utils module
"""
import unittest
from utils import *
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    Class to test the functions in the utils module
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Method to test the output of the
        test_access_nested_map function
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)
