import unittest
from src.homework.g_lists_and_tuples.lists import ( get_lowest_list_value, get_highest_list_value )

class TestListsAndTuples(unittest.TestCase):

    def test_get_lowest_list_value(self): # tests for the lowest value function
        test_list = [8, 10, 1, 50, 20] 
        expected_lowest = 1
        self.assertEqual(get_lowest_list_value(test_list), expected_lowest)

    def test_get_highest_list_value(self): # tests for the highest value function
        test_list = [8, 10, 1, 50, 20]
        expected_highest = 50
        self.assertEqual(get_highest_list_value(test_list), expected_highest)

    def test_get_lowest_list_value_empty(self): # tests for empty list
        test_list = []
        expected_lowest = None
        self.assertEqual(get_lowest_list_value(test_list), expected_lowest)

    def test_get_highest_list_value_empty(self): # tests for empty list
        test_list = []
        expected_highest = None
        self.assertEqual(get_highest_list_value(test_list), expected_highest)