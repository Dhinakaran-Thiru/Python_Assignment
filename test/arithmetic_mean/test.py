import unittest
from src.arithmetic_mean.util import mean_variable


class MyTestCase(unittest.TestCase):
    def test_mean_variable(self):
        res=mean_variable()
        self.assertEqual(res, "[1.5 3.5]\n[1. 1.]\n1.11803398875")# add assertion here


if __name__ == '__main__':
    unittest.main() 
