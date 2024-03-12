import unittest
from src.assignment2.util import second_largest


class MyTestCase(unittest.TestCase):
    def test_second_largest(self):
        answer=second_largest()
        self.assertEqual(answer, 41)

    def test_second_largest1(self):
            answer = second_largest()
            self.assertEqual(answer, 42)
    def test_second_largest2(self):
        answer=second_largest()
        self.assertEqual(answer, 43)

        # add assertion here


if __name__ == '__main__':
    unittest.main()

