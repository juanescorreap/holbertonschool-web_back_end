#!/usr/bin/env python3
"""
Class to test the functions in the utils module
"""
import unittest
from utils import *
from parameterized import parameterized
from unittest.mock import patch, Mock
from unittest import TestCase, mock


class TestAccessNestedMap(unittest.TestCase):
    """
    Class to test the access_nested_map function
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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Method to test that test_access_nested_map
        is raising the correct error
        """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(error.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """
    Class to test the get_json function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Method to test the output of
        test_get_json
        """
        mock_instance = Mock()
        mock_instance.json.return_value = test_payload
        with patch('requests.get', return_value=mock_instance):
            response = get_json(test_url)
            self.assertEqual(response, test_payload)
            mock_instance.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """
    Class to test the memoized property
    """

    def test_memoize(self):
        """
        Method to test that memoized is working
        """
        class TestClass:
            """
            Class to test memoized
            """

            def a_method(self):
                """
                method to test memoized
                """
                return 42

            @memoize
            def a_property(self):
                """
                Method calling the previously
                defined method to test the
                @memoize decorator
                """
                return self.a_method()
        with patch.object(TestClass, 'a_method') as test_method:
            class_instance = TestClass()
            class_instance.a_property
            class_instance.a_property
            test_method.assert_called_once
