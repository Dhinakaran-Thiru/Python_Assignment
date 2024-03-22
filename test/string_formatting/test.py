import unittest
from src.string_formatting.util import string_format


class MyTestCase(unittest.TestCase):
    def test_string_format(self):
        self.assertEqual(string_format(4), '  1   1   1   1\n  2   2   2  10\n  3   3   3  11\n  4   4   4 100')

if __name__ == '__main__':
    unittest.main()
  
