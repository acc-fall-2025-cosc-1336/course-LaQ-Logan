import unittest

from src.homework.c_decisions.decisions import get_faculty_rating, get_options_ratio

class Test_Config(unittest.TestCase):

    def test_get_options_ratio(self):
        self.assertAlmostEqual(get_options_ratio(3, 10), 0.3)
        self.assertAlmostEqual(get_options_ratio(7, 10), 0.7)
        self.assertAlmostEqual(get_options_ratio(9, 10), 0.9)
        self.assertAlmostEqual(get_options_ratio(0, 10), 0.0)
        self.assertAlmostEqual(get_options_ratio(10, 10), 1.0)
        self.assertRaises(ZeroDivisionError, get_options_ratio, 5, 0)  # Edge case: division by zero

    def test_get_faculty_rating(self):
        self.assertEqual(get_faculty_rating(0.5), "Unacceptable")
        self.assertEqual(get_faculty_rating(0.6), "Needs Improvement")
        self.assertEqual(get_faculty_rating(0.75), "Good")
        self.assertEqual(get_faculty_rating(0.85), "Very Good")
        self.assertEqual(get_faculty_rating(0.95), "Excellent")
        self.assertEqual(get_faculty_rating(-0.1), "Invalid Ratio, Please enter a valid ratio between 0 and 1")  # Edge case: negative ratio
        self.assertEqual(get_faculty_rating(1.1), "Invalid Ratio, Please enter a valid ratio between 0 and 1")  # Edge case: ratio above 1

    