import unittest
import sys
import os

from tests.homework.i_dictionaries_and_sets import test_dictionaries_and_set
suite = unittest.TestLoader().loadTestsFromModule(test_dictionaries_and_sets)
unittest.TextTestRunner(verbosity=2).run(suite)




