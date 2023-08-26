#!/usr/bin/pythn3
import unittest
from unittest.mock import Mock, patch
from make_request import fetch_data_from_url

class TestFetchFromUrl(unittest.TestCase):
    @patch('make_request.requests.get')
    def test_url(self, mock_get):
        res = Mock()
        res.status_code = 200
        res.json.return_value = {'key': 'value'}
        mock_get.return_value = res

        result = fetch_data_from_url("https://swapi-api.alx-tools.com/api/films/1")

        self.assertEqual(result, {'key': 'value'})
if __name__ == "__main__":
    unittest.main()