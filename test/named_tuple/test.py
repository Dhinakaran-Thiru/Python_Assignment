from src.named_tuple.util import avg
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        res=avg()
        self.assertEqual(res, '78.00')  # add assertion here


if __name__ == '__main__':
    unittest.main()
 
