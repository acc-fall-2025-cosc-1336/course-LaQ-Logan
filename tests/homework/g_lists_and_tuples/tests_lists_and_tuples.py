import unittest
from src.homework.g_lists_and_tuples.lists import (get_p_distance, get_p_distance_matrix, get_lowest_list_value, get_highest_list_value)

class TestListsAndTuples(unittest.TestCase):

    def test_p_distance(self): # tests for the p-distance function
        list1 = ['T','T','T','C','C','A','T','T','T','A'] # sample list 1
        list2 = ['G','A','T','T','C','A','T','T','T','C'] # sample list 2
        self.assertAlmostEqual(get_p_distance(list1, list2), 0.4) # expected p-distance is 0.4




    def test_p_distance_matrix(self): # tests for the p-distance matrix function
        dna_lists = [ # nested lists representing DNA sequence samples
            ['T','T','T','C','C','A','T','T','T','A'],  # list1
            ['G','A','T','T','C','A','T','T','T','C'],  # list2
            ['T','T','T','C','C','A','T','T','T','T'],  # list3
            ['G','T','T','C','C','A','T','T','T','A']   # list4
        ]

        expected = [ # expected p-distance matrixes
            [0.0, 0.4, 0.1, 0.1],  # list1 vs list1, list2, list3, list4
            [0.4, 0.0, 0.4, 0.3],  # list2 vs list1, list2, list3, list4
            [0.1, 0.4, 0.0, 0.2],  # list3 vs list1, list2, list3, list4
            [0.1, 0.3, 0.2, 0.0]   # list4 vs list1, list2, list3, list4
        ]

        result = get_p_distance_matrix(dna_lists) # compute the p-distance matrix
      
        for i in range(len(expected)): # compare each value in the resulting matrix to the expected values
            for j in range(len(expected[i])): # iterate through each column of the row 
                self.assertAlmostEqual(result[i][j], expected[i][j], places=3) # assert values are approximately equal to 3 decimal places






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