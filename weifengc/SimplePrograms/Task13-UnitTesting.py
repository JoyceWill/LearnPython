# Run this test. python weifengc/Task13-UnitTesting.py

import unittest

def median(pool):
    copy = sorted(pool)
    size = len(pool)
    if size % 2 == 1:
        return copy[(size - 1) / 2]
    else:
        return (copy[size / 2 - 1] + copy[size/2]) / 2

class TestMedian(unittest.TestCase):
    def testMedian(self):
        self.failUnlessEqual(median([2, 9, 9, 7, 9, 2, 4, 5, 8]), 7)

if __name__ == '__main__' :
    unittest.main()

