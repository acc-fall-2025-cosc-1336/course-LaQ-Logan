import unittest

from tests.homework.d_repetition.tests_repetition import Test_Config as TestRepetition

suite = unittest.TestLoader().loadTestsFromTestCase(TestRepetition)
unittest.TextTestRunner(verbosity=2).run(suite)
