import unittest
from src.no_idea_problem.util import calculate_happiness

class TestCalculateHappiness(unittest.TestCase):
    def test_calculate_happiness(self):
        n, m = 3, 2
        arr = [1, 5, 3]
        a = {3, 1}
        b = {5, 7}
        self.assertEqual(calculate_happiness(n, m, arr, a, b), 1)

if __name__ == '__main__':
    unittest.main()
