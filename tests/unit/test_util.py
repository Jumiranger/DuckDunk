import unittest
from unittest.mock import patch, Mock
import duckdunk.util

class TestUtilMethods(unittest.TestCase):
    def test_search_between_failure(self):
        with self.assertRaises(Exception):
            duckdunk.util.search_between_strict('aaa', 'b', 'c')


if __name__ == '__main__':
    unittest.main()