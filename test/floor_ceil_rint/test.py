import unittest

from src.floor_ceil_rint.util import new_array
class MyTestCase(unittest.TestCase):
    def test_something(self):
        input_str = "1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9"


        floor_arr, ceil_arr, rint_arr = new_array(input_str)

        self.assertEqual(new_array(input_str), ([1, 2, 3, 4, 5, 6, 7, 8, 9],
 [2.1, 3.2, 4.3, 5.4, 6.5, 7.6, 8.7, 9.8, 10.9],
 [1.1, 2.2, 3.3, 4.4, 5.5, 7.7, 8.8, 9.9]))


if __name__ == '__main__':
    unittest.main() 
  
 
