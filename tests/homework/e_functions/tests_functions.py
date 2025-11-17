import unittest
from src.homework.e_functions.void_func import display_payroll_check
from src.homework.e_functions.value_return import get_gross_pay, get_fica_tax, get_federal_tax

class TestPayrollFunctions(unittest.TestCase):

    def test_case1(self):
        gross = get_gross_pay(40, 10) # 40*10 + 5*15 = 475
        self.assertAlmostEqual(gross, 400.0)
        fica = get_fica_tax(gross) # 475 * 0.0765
        self.assertAlmostEqual(fica, 30.60, places=2)
        federal = get_federal_tax(gross) # 475 * 0.08
        self.assertAlmostEqual(federal, 32.00)
        net = gross - fica - federal # 475 - 36.34 - 38
        self.assertAlmostEqual(net, 337.40 , places=2)


    def test_case2(self):
        gross = get_gross_pay(45, 10) # 40*10 + 5*15 = 475
        self.assertAlmostEqual(gross, 475.0)
        fica = get_fica_tax(gross) # 475 * 0.0765
        self.assertAlmostEqual(fica, 36.34, places=2)
        federal = get_federal_tax(gross) # 475 * 0.08
        self.assertAlmostEqual(federal, 38.00)
        net = gross - fica - federal # 475 - 36.34 - 38
        self.assertAlmostEqual(net, 400.66, places=2)

    def test_case3(self):
        gross = get_gross_pay(30, 10) # 30*15 = 450
        self.assertAlmostEqual(gross, 300.0)
        fica = get_fica_tax(gross) # 450 * 0.0765
        self.assertAlmostEqual(fica, 22.95 , places=2)
        federal = get_federal_tax(gross) # 450 * 0.08
        self.assertAlmostEqual(federal, 24.00)
        net = gross - fica - federal # 450 - 34.43 - 36
        self.assertAlmostEqual(net, 253.05 , places=2)
