import unittest

from src.homework.c_decisions.decisions import letter_grade_if, letter_grade_switch

class Test_Config(unittest.TestCase):

    def test_letter_grade_if(self):
        self.assertEqual(letter_grade_if(95), 'A')
        self.assertEqual(letter_grade_if(85), 'B')
        self.assertEqual(letter_grade_if(75), 'C')
        self.assertEqual(letter_grade_if(65), 'D')
        self.assertEqual(letter_grade_if(55), 'F')
        self.assertEqual(letter_grade_if(-10), 'F')  # Edge case: negative grade
        self.assertEqual(letter_grade_if(110), 'A')  # Edge case: above 100

    
    def test_letter_grade_switch(self):
        self.assertEqual(letter_grade_switch(95), 'A')
        self.assertEqual(letter_grade_switch(85), 'B')
        self.assertEqual(letter_grade_switch(75), 'C')
        self.assertEqual(letter_grade_switch(65), 'D')
        self.assertEqual(letter_grade_switch(55), 'F')
        self.assertEqual(letter_grade_switch(-10), 'Invalid grade')  # Edge case: negative grade
        self.assertEqual(letter_grade_switch(110), 'Invalid grade')  # Edge case: above 100