import unittest

from src.homework.d_repetition.repetition import get_factorial, sum_odd_numbers

class Test_Config(unittest.TestCase):

    def test_get_factorial(self):
        self.assertEqual(get_factorial(1), 1)
        self.assertEqual(get_factorial(2), 2)
        self.assertEqual(get_factorial(3), 6)
        self.assertEqual(get_factorial(4), 24)
        self.assertEqual(get_factorial(5), 120)
        self.assertEqual(get_factorial(6), 720)
        self.assertEqual(get_factorial(7), 5040)
        self.assertEqual(get_factorial(8), 40320)
        self.assertEqual(get_factorial(9), 362880)

    def test_sum_odd_numbers(self):
        self.assertEqual(sum_odd_numbers(1), 1)
        self.assertEqual(sum_odd_numbers(2), 1)
        self.assertEqual(sum_odd_numbers(3), 4)   # 1 + 3
        self.assertEqual(sum_odd_numbers(4), 4)   # 1 + 3
        self.assertEqual(sum_odd_numbers(5), 9)   # 1 + 3 + 5
        self.assertEqual(sum_odd_numbers(10), 25) # 1 + 3 + 5 + 7 + 9
        self.assertEqual(sum_odd_numbers(99), 2500) # Sum of all odd numbers from 1 to 99