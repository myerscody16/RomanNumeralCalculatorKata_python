# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 14:43:32 2019

@author: myers
"""


import unittest
import RomanNumberToIntegerConverter as RNIC

class RomanNumberToIntegerConverterTests(unittest.TestCase):
          
    def setUp(self): 
        pass
    
        
    def test_convert_when_passed_a_single_valid_roman_numeral_returns_the_equivalent_value(self):
        self.assertEqual(RNIC.convert("I"),1)
        self.assertEqual(RNIC.convert("l"),50)
        self.assertEqual(RNIC.convert("M"),1000)
        
    def test_when_passed_a_single_invalid_roman_numeral_returns_an_error_message(self):
        self.assertEqual(RNIC.convert("j"),"That is not a roman numeral")
        
    def test_convert_when_passed_two_valid_roman_numerals_with_higher_value_in_the_front_return_equivalent_value(self):
        self.assertEqual(RNIC.convert("vi"),6)
        self.assertEqual(RNIC.convert("Xii"),12)
        
    def test_convert_when_passed_two_valid_roman_numerals_with_lower_value_in_the_front_return_equivalent_value(self):
        self.assertEqual(RNIC.convert("iv"),4)
        self.assertEqual(RNIC.convert("dM"),950)
    


if __name__ == '__main__':
    unittest.main()