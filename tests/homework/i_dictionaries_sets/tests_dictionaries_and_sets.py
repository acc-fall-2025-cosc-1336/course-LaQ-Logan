import unittest

from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget

class Test_Config(unittest.TestCase):

    def test_add_inventory(self):
        inventory = {}

       
        add_inventory(inventory, "Widget1", 10) # Add Widget1 with 10
        self.assertIn("Widget1", inventory)
        self.assertEqual(inventory["Widget1"], 10)

        
        add_inventory(inventory, "Widget1", 25) # Add Widget1 with 25 → 10 + 25 = 35
        self.assertEqual(inventory["Widget1"], 35)

        
        add_inventory(inventory, "Widget1", -10) # Add Widget1 with -10 → 35 - 10 = 25
        self.assertEqual(inventory["Widget1"], 25)

    def test_remove_inventory_widget(self):
        inventory = {}

        
        add_inventory(inventory, "Widget1", 10) # Add two widgets 1(10) and 2(20)
        add_inventory(inventory, "Widget2", 20)

      
        message  = remove_inventory_widget(inventory, "Widget1") # Remove existing widget 1
        self.assertEqual(message , "Record deleted") 
        self.assertEqual(len(inventory), 1)
        self.assertIn("Widget2", inventory)

        message2  = remove_inventory_widget(inventory, "Widget3") # Try removing non-existent widget
        self.assertEqual(message2, "Item not found") 
        self.assertEqual(len(inventory), 1)