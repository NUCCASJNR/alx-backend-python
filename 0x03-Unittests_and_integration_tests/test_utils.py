#!/usr/bin/env python3

"""
This module tests the utils.access_nested_map function
"""

import unittest
from typing import Dict
from unittest.mock import Mock, patch

from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, output):
        """TestCase for AccessNestedMap method"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, output)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, output):
        """
        TestCase for AccessNestedMap keyError
        """
        with self.assertRaises(output) as err:
            result = access_nested_map(nested_map, path)
        # self.assertEqual(str(err.exception), output)


class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, url, payload, mock_get):
        """
        TestCase for get_json method
        """
        # Define a mock obj with json response
        mock_obj = Mock()
        mock_obj.json.return_value = payload
        # Confogure the mock_get function to return the mock_obj
        mock_get.return_value = mock_obj
        # Call the json function on the parametrized urls
        result = get_json(url)
        mock_get.assert_called_once_with(url)
        self.assertEqual(result, payload)


if __name__ == "__main__":
    unittest.main()
