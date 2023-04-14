
from nesting_structure_comparison import same_structure_as
import unittest

class TestClass(unittest.TestCase):
    def test_same_structure_as1(self):
        actual = same_structure_as(original=[ 1, 1, 1 ], other=[ 2, 2, 2 ])
        expected = True
        self.assertEqual(actual, expected)   
    def test_same_structure_as2(self):
        actual = same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )
        expected = True
        self.assertEqual(actual, expected)   
    def test_same_structure_as3(self):
        actual = same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
        expected = False
        self.assertEqual(actual, expected)   
    def test_same_structure_as4(self):
        actual = same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )
        expected = False
        self.assertEqual(actual, expected)   
    def test_same_structure_as5(self):
        actual = same_structure_as([1,'[',']'], ['[',']',1])
        expected = True
        self.assertEqual(actual, expected)  
    