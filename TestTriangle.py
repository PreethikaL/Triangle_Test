# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(2,3,4),'Scalene','2,3,4 should be scalene')

    def testIsocelesTriangles(self):
        self.assertEqual(classifyTriangle(5,5,4),'Isoceles','5,5,4 should be isoceles')

    def testZeroInputA(self):
        self.assertEqual(classifyTriangle(0,7,8),'InvalidInput','0,7,8 A is invalid')

    def testZeroInputB(self):
        self.assertEqual(classifyTriangle(6,0,8),'InvalidInput','6,0,8 B is invalid')

    def testZeroInputC(self):
        self.assertEqual(classifyTriangle(6,7,0),'InvalidInput','6,7,0 A is invalid')

    def testBadTypeA(self):
        self.assertEqual(classifyTriangle(6.23,7,8),'InvalidInput','6.23,7,0 A is invalid type')

    def testBadTypeB(self):
        self.assertEqual(classifyTriangle(6,7.50,8),'InvalidInput','6,7.50,8 B is invalid type')

    def testBadTypeC(self):
        self.assertEqual(classifyTriangle(6,7,9.5),'InvalidInput','6,7,9.5 C is invalid type')

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(3,4,9),'NotATriangle','3,4,9 is not a triangle')

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(3,4,9),'NotATriangle','3,4,9 is not a triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

