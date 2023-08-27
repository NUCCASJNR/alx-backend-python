#!/usr/bin/env python3

"""
This module tests the utils.access_nested_map function
"""

import unittest
from typing import Any, Dict, Mapping, Sequence
from unittest.mock import Mock, patch

from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    def setUp(self) -> None:
        print(f"Testing the AccessNestedMap Method")

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               output: Any) -> None:
        """TestCase for AccessNestedMap method"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, output)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping, path:
                                         Sequence, output: Any) -> None:
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
    def test_get_json(self, url: str, payload: Dict) -> None:
        """
        TestCase for get_json method
        """
        with patch('utils.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = payload
            mock_get.return_value = mock_response
            result = get_json(url)
            mock_get.assert_called_once_with(url)
            self.assertEqual(result, payload)


class TestMemoize(unittest.TestCase):
    """
    Class contans functions for testing memoize method
    """
    def setUp(self) -> None:
        print(f"Testing the Memoize Method")

    def test_memoize(self):
        """
        TestCase for utils.memoize
        """
        class TestClass:
            """
            testclass class that contains a_method and a_property
            """
            def a_method(self):
                """
                Returns 42 when called
                """
                return 42

            @memoize
            def a_property(self):
                """
                invokes the a_method method
                """
                return self.a_method()
        test_obj = TestClass()
        with patch.object(test_obj, 'a_method', return_value=42) as mock:
            result1 = test_obj.a_property
            result2 = test_obj.a_property
            self.assertEqual(result1, mock.return_value)
            self.assertEqual(result2, mock.return_value)
            mock.assert_called_once()


if __name__ == "__main__":
    unittest.main()