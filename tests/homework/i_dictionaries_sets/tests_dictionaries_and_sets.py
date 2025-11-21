import unittest
from src.homework.i_dictionaries_and_sets.dictionary import add_inventory, remove_inventory_widget

class Test_Config(unittest.TestCase):

    def test_add_inventory(self):
        inventory_dictionary = {}

        # Add widget1 with quantity 10
        add_inventory(inventory_dictionary, "Widget1", 10)
        self.assertEqual(inventory_dictionary["Widget1"], 10)

        # Update widget1 by adding 25
        add_inventory(inventory_dictionary, "Widget1", 25)
        self.assertEqual(inventory_dictionary["Widget1"], 35)

        # Update widget1 by adding -10
        add_inventory(inventory_dictionary, "Widget1", -10)
        self.assertEqual(inventory_dictionary["Widget1"], 25)

    def test_remove_inventory_widget(self):
        inventory_dictionary = {}

        # Add two widgets
        add_inventory(inventory_dictionary, "Widget1", 10)
        add_inventory(inventory_dictionary, "Widget2", 20)

        # Remove widget1
        response = remove_inventory_widget(inventory_dictionary, "Widget1")
        self.assertEqual(response, 'Record deleted')

        # Dictionary should have only 1 entry left
        self.assertEqual(len(inventory_dictionary), 1)
        self.assertTrue("Widget2" in inventory_dictionary)