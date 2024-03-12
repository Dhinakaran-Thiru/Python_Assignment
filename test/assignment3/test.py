import unittest
from src.assignment3.util import given_string


class MyTestCase(unittest.TestCase):
    def test_given_string(self):
        self.assertEqual(given_string('abracadabra', 5, 'k'), 'abrackdabra')

    def test_given_string1(self):
        self.assertEqual(given_string("dhinakaran", 2, "y"), "dhynakaran")

    def test_given_string2(self):
        self.assertEqual(given_string("deepak", 3, "i"), "deeiak")

if __name__ == '__main__':
    unittest.main()
