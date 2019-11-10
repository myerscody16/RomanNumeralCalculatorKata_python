# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 14:44:17 2019

@author: myers
"""
RomanNumeralsDictionary = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
        }

def convert(romanNumeral):
    listOfNumerals = split_str(romanNumeral)
    total = 0
    count = 0
    if(len(listOfNumerals) > 1):
        for numeral in listOfNumerals:
            isNumeralValid = determine_if_roman_numeral_is_a_valid_character(numeral)
            if(isNumeralValid == True):#addOrSubtract below needs to make sure the count stays in range of the list
                addOrSubtract = isCurrentNumberLowerOrEqualThanTheNextNumber(listOfNumerals[count], listOfNumerals[count+1])
                count += 1
                if(addOrSubtract == "smaller"):
                    total += (-1)*RomanNumeralsDictionary.get(numeral.upper())
                elif(addOrSubtract == "bigger" or "equal"):
                    total += RomanNumeralsDictionary.get(numeral.upper())
            elif(isNumeralValid == False):
                return "That is not a roman numeral"
    else:
        isNumeralValid = determine_if_roman_numeral_is_a_valid_character(romanNumeral.upper())
        if(isNumeralValid == "True"):
            total += RomanNumeralsDictionary.get(romanNumeral.upper())
        elif(isNumeralValid == "False"):
            return "That is not a roman numeral"
    return total
    
def determine_if_roman_numeral_is_a_valid_character(romanNumeral):
    return check_if_roman_numeral_in_the_dictionary(romanNumeral.upper())
            
def check_if_roman_numeral_in_the_dictionary(romanNumeral):
    if romanNumeral in RomanNumeralsDictionary:
        return True
    else:
        return False

def split_str(romanNumeral):
    return list(romanNumeral)

def isCurrentNumberLowerOrEqualThanTheNextNumber(firstNumber, secondNumber):
    valueOne = RomanNumeralsDictionary.get(firstNumber.upper())
    valueTwo = RomanNumeralsDictionary.get(secondNumber.upper())
    if(valueOne < valueTwo):
        return "smaller"
    elif(valueOne > valueTwo):
        return "bigger"
    elif(valueOne == valueTwo):
        return "equal"
    
def ifThereAreMultipleNumbers()