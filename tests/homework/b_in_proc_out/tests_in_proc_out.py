import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))


import unittest
from homework.b_in_proc_out.output import get_sales_tax_amount, get_tip_amount

class TestBillCalculations(unittest.TestCase):

    def test_get_sales_tax_amount(self):
        self.assertAlmostEqual(get_sales_tax_amount(100), 6.75)
        self.assertAlmostEqual(get_sales_tax_amount(50), 3.375)

    def test_get_tip_amount(self):
        self.assertAlmostEqual(get_tip_amount(100, 0.2), 20)
        self.assertAlmostEqual(get_tip_amount(50, 0.15), 7.5)

if __name__ == '__main__':
    unittest.main()

