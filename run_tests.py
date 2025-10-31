import unittest

from tests.homework.h_strings.tests_strings import TestStrings

suite = unittest.TestLoader().loadTestsFromTestCase(TestStrings)
unittest.TextTestRunner(verbosity=2).run(suite)
