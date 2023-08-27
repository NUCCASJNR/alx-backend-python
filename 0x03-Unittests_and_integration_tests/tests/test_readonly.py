#!/usr/bin/env python3

import unittest
from unittest.mock import Mock, patch
from read_only import add, ReadOnly, square
from parameterized import parameterized

class TestReadOnly(unittest.TestCase):
    def test_read_only(self):
        mock_class = Mock(spec=ReadOnly)
        mock_class.read_only = 100
        result = mock_class.read_only
        self.assertEqual(result, 100)

class TestAdd(unittest.TestCase):
    @patch("read_only.add")
    def test_add(self, mock_add):
        mock_add.return_value = 5
        result = add(2, 3)
        self.assertEqual(result, 5)

class TestSquare(unittest.TestCase):
    @parameterized.expand([
        (2, 4),
        (3, 9),
        (0, 0),
        (-2, 4)
    ])
    def test_square(self, input_value, expected_result):
        result = square(input_value)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()