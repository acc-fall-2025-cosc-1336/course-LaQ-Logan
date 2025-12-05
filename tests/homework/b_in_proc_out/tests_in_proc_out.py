import unittest

from src.homework.b_in_proc_out.output import multiply_numbers, get_sales_tax_amount, get_tip_amount, get_total_cost

class Test_Config(unittest.TestCase):

    def test_multiply_numbers(self):
        self.assertEqual(multiply_numbers(5, 5), 25)
        self.assertEqual(multiply_numbers(7, 7), 49)

    def test_get_sales_tax_amount(self):
        self.assertAlmostEqual(get_sales_tax_amount(100), 6.5)
        self.assertAlmostEqual(get_sales_tax_amount(200), 13.0)

    def test_get_tip_amount(self):
        self.assertAlmostEqual(get_tip_amount(100, 0.15), 15.0)
        self.assertAlmostEqual(get_tip_amount(200, 0.20), 40.0)
    
    def test_get_total_cost(self):
        self.assertAlmostEqual(get_total_cost(100, 15, 6.5), 121.5)
        self.assertAlmostEqual(get_total_cost(200, 40, 13), 253.0)