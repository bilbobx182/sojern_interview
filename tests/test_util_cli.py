"""
Unit tests for the UTIL CLI
"""
import unittest
from util_cli import app


class TestUtilCLI(unittest.TestCase):
    """
    Test Case for CLI
    """
    def test_happy_path_validate_versions_single(self):
        """
        Test normal path of versions being passed in.
        """
        self.assertEqual(app.validate_versions("1.0", "1.1"), -1)

    def test_happy_path_validate_versions_double(self):
        """
        Test that longer version comparisons don't trip it up.
        """

        self.assertEqual(app.validate_versions("1.3.10", "1.10"), -1)

    def test_happy_path_returns_1(self):
        """
        Test happy path returns 1
        """
        self.assertEqual(app.validate_versions("1.0.0", "0.0.1"), 1)

    def test_edge_case_versions_same(self):
        """
        Test same version returns 0
        :return:
        """
        self.assertEqual(app.validate_versions("1", "1"), 0)

    def test_basic_bad_path(self):
        """
        Test alphanumeric edge cases
        :return:
        """
        self.assertEqual(app.validate_versions("abc", "def"), 0)
        self.assertEqual(app.validate_versions("1.2.3", "def"), 0)
        self.assertEqual(app.validate_versions("abc", "1.2.3"), 0)

