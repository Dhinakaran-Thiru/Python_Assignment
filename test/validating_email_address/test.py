import unittest
from src.validating_email_address.util import is_valid_email


class TestIsValidEmail(unittest.TestCase):
    def test_is_valid_email(self):
        # Valid email addresses
        self.assertTrue(is_valid_email("lara@hackerrank.com"))
        self.assertTrue(is_valid_email("brian-23@hackerrank.com"))
        self.assertTrue(is_valid_email("britts_54@hackerrank.com"))



if __name__ == '__main__':
    unittest.main()

