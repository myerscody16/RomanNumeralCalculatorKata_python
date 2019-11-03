# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 14:44:17 2019

@author: myers
"""
RomanNumeralsDictionary = {
        "I": 1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
        }

def convert(romanNumeral):
    isNumeralValid = determine_if_roman_numeral_is_a_valid_character(romanNumeral)
    if(isNumeralValid == True):
        return RomanNumeralsDictionary.get(romanNumeral.upper())
    elif(isNumeralValid == False):
        return "That is not a roman numeral"
    
def determine_if_roman_numeral_is_a_valid_character(romanNumeral):
    return check_if_roman_numeral_in_the_dictionary(romanNumeral.upper())
            
def check_if_roman_numeral_in_the_dictionary(romanNumeral):
    if romanNumeral in RomanNumeralsDictionary:
        return True
    else:
        return False