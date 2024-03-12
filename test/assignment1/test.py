import unittest
from src.assignment1.util import cal_avg


class TestCalAvg(unittest.TestCase):
    def test_cal_avg(self):
        n=3
        student_data=['dhina 1 2 3','deepak 1 4 7','deepa 5 7 2']
        query_name='dhina'
        self.assertEqual(cal_avg(n,student_data,query_name),'2.00')

    def test1_cal_avg(self):
        n=3
        student_data=['a 4 6 8 ','b 4 4 4','c 5 5 5']
        query_name='c'
        self.assertEqual(cal_avg(n,student_data,query_name), '5.00')

    def test2_cal_avg(self):
        n=3
        student_data=['e 1 1 1 ','f 10 10 10','g 20 20 20']
        query_name='g'
        self.assertEqual(cal_avg(n,student_data,query_name), '20.00')



if __name__ == '__main__':
    unittest.main()
