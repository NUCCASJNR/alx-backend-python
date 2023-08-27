#!/usr/bin/env python3

"""
This module tests the utils.access_nested_map function
"""

import unittest

from parameterized import parameterized
from utils import access_nested_map


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


if __name__ == "__main__":
    unittest.main()
