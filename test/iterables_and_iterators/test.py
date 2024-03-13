import unittest
from src.iterables_and_iterators.util import calculate_probability

class TestProbability(unittest.TestCase):
    def test_case_1(self):
        result = calculate_probability(4, ['a', 'a', 'c', 'd'], 2)
        self.assertAlmostEqual(result, 0.8333, places=4)

if __name__ == "__main__":
    unittest.main()
