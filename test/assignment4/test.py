import unittest
from src.assignment4.util import merging


class MyTestCase(unittest.TestCase):
    def test_merging(self):

        self.assertEqual(merging(),'dhi\nnak\nar\nn')
    def test_merging1(self):

        self.assertEqual(merging(),'abc\ndef\nghi\njkl\nmno\npqr\nstu')
    def test_merging2(self):

        self.assertEqual(merging(),'de\npa')




if __name__ == '__main__':
    unittest.main()
