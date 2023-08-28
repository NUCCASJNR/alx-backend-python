#!/usr/bin/env python3
"""
This module tests client.py
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([
        ("google", {"key": "value"}),
        ("abc", {"key": "value"})
    ])
    def test_org(self, org_name, output):
        """Test the GithubOrgClient.org method"""
        expected_url = f"{GithubOrgClient.ORG_URL.format(org=org_name)}"
        with patch('client.get_json', return_value=output) as mock_get_json:
            client = GithubOrgClient(org_name)
            result = client.org
            # print(result)
            mock_get_json.assert_called_once_with(expected_url)
            self.assertEqual(result, output)

    @parameterized.expand([
        ("google", ("https://api.github.com/orgs/adobe/repos")),
        ("abc", ("https://api.github.com/orgs/abc/repos")),
        ('Netflix', ("https://api.github.com/orgs/Netflix/repos"))
    ])
    def test_public_repos_url(self, org_name, output):
        """Test the GithubOrgClient.public-repos_url method"""
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock)as mock_public_repos_url:
            mock_public_repos_url.return_value = output
            client = GithubOrgClient(org_name)
            result = client._public_repos_url
            self.assertEqual(result, output)


if __name__ == "__main__":
    unittest.main()
