
from incr_or_decr_all_list_element import incr_decr
import unittest

class TestClass(unittest.TestCase):
    def test_incr(self):
        result = incr_decr([1,2,3,-1,0],1)
        expected = [2,3,4,0,1]
        self.assertEqual(result, expected)
    def test_decr(self):
        result = incr_decr([1,2,3,-1,0],-2)
        expected = [-1,0,1,-3,-2]
        self.assertEqual(result, expected)
    def test_float(self):
        result = incr_decr([1,2,3,-1,0],1.3)
        expected = 'i must be an integer number . please try again ...'
        self.assertEqual(result, expected)

