import unittest
from src.calender_module.util import calendar_module

class MyTestCase(unittest.TestCase):
    def testcase1(self):
        self.assertEqual( calendar_module("08 05 2015"),"WEDNESDAY")

    def testcase2(self):
        self.assertEqual( calendar_module("06 09 2018"),"SATURDAY")

    def testcase3(self):
        self.assertEqual( calendar_module("11 02 2001"),"FRIDAY")


if __name__ == '__main__': 
    unittest.main()
 
