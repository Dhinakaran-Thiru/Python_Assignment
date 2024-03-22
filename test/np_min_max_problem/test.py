import unittest
from src.np_min_max_problem.util import minimum_maximum

class TestMinimumMaximum(unittest.TestCase):
    def test_minimum_maximum(self):
        arr = [[2, 5],
               [3, 7],
               [1, 3],
               [4, 0]]
        result = minimum_maximum(arr)
        self.assertEqual(result, 3)  # Correct the expected result to 3

if __name__ == '__main__':
    unittest.main()
