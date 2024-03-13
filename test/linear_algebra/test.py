import unittest
from src.linear_algebra.util import find_the_determinant_value

class MyTestCase(unittest.TestCase):
    def test_find_the_determinant_value(self):
        N = 2
        matrix_value = [[1.1, 1.1], [1.1, 1.1]]
        result = find_the_determinant_value(N, matrix_value)
        self.assertEqual(result, 0.0)

    def test_find_the_determinant_value1(self):
        N = 2
        matrix_value = [[2.2, 2.2], [2.2, 2.2]]
        result = find_the_determinant_value(N, matrix_value)
        self.assertEqual(result, 0.0)



if __name__ == '__main__':
    unittest.main()
