import unittest
from src.homework.e_functions.value_return_functions import (
    get_gross_pay,
    get_fica_tax,
    get_federal_tax,
)

class TestPayrollFunctions(unittest.TestCase):

    def test_case1(self):
        hours = 40
        rate = 10
        gross = get_gross_pay(hours, rate)
        self.assertAlmostEqual(gross, 400)
        self.assertAlmostEqual(get_fica_tax(gross), 30.6, places=2)
        self.assertAlmostEqual(get_federal_tax(gross), 32.0, places=2)

    def test_case2(self):
        hours = 45
        rate = 10
        gross = get_gross_pay(hours, rate)
        self.assertAlmostEqual(gross, 475)
        self.assertAlmostEqual(get_fica_tax(gross), 36.34, places=2)
        self.assertAlmostEqual(get_federal_tax(gross), 38.0, places=2)

    def test_case3(self):
        hours = 30
        rate = 10
        gross = get_gross_pay(hours, rate)
        self.assertAlmostEqual(gross, 300)
        self.assertAlmostEqual(get_fica_tax(gross), 22.95, places=2)
        self.assertAlmostEqual(get_federal_tax(gross), 24.0, places=2)

if __name__ == "__main__":
    unittest.main()
