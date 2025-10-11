import unittest

from tests.homework.e_functions.tests_functions import TestPayrollFunctions

suite = unittest.TestLoader().loadTestsFromTestCase(TestPayrollFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)
