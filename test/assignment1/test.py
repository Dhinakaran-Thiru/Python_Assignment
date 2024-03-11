import unittest
from src.assignment1.util import cal_avg


class TestCalAvg(unittest.TestCase):
    def test_cal_avg(self):
        n=3
        student_data=['harish 2.5 2.5 4','hari 2.5 3.5 3','lokesh 35 34 76']
        query_name='hari'
        self.assertEqual(cal_avg(n,student_data,query_name),'3.00')  # add assertion here


if __name__ == '__main__':
    unittest.main()
