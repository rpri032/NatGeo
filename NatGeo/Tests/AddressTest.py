'''
Created on Sep 19, 2016

@author: RICH
'''
import unittest
from Models.Address import Address
class Test(unittest.TestCase):
    def testName(self):
        address = Address("1150 K Street NW", "Washington", "20005", "DC", "United States")
        self.assertEqual(str(address), "1150 K Street NW, Washington DC 20005, UNITED STATES", "Incorrect Address Formatting")
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()