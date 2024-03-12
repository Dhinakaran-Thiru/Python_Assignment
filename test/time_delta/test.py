import unittest
from src.time_delta.util import time_delta


class MyTestCase(unittest.TestCase):
    def test_time_delta(self):
        self.assertEqual( time_delta("2\nSun 10 May 2015 13:54:36 -0700\nSun 10 May 2015 13:54:36 -0000\nSat 02 May 2015 19:54:36 +0530\nFri 01 May 2015 13:54:36 -0000"),'25200\n88200')  # add assertion here

 # add assertion here


if __name__ == '__main__':
    unittest.main()
