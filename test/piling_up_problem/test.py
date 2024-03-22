import unittest
from src.piling_up_problem.util import piling_up

class TestCanStackCubes(unittest.TestCase):
    def test_can_stack_cubes(self):
        self.assertEqual(piling_up(6, [4, 3, 2, 1, 3, 4]), "Yes")
        self.assertEqual(piling_up(3, [1, 3, 2]), "No")

if __name__ == '__main__':
    unittest.main() 
