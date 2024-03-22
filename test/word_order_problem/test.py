import unittest
from src.word_order_problem.util import word_counting


class TestCountWordOccurrences(unittest.TestCase):
    def test_word_counting(self):
        n = 4
        words = ['bcdef', 'abcdefg', 'bcde', 'bcdef']
        expected_result = {'bcdef': 2, 'abcdefg': 1, 'bcde': 1}
        self.assertEqual(word_counting(n, words), expected_result)

if __name__ == '__main__': 
    unittest.main()
