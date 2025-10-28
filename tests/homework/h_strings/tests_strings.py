import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))

import unittest
from homework.h_strings.strings import get_hamming_distance, get_dna_complement

class Test_Config(unittest.TestCase):

    def test_get_hamming_distance(self):
        result = get_hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT")
        self.assertEqual(result, 7)

    def test_get_dna_complement(self):
        result = get_dna_complement("AAAACCCGGT")
        self.assertEqual(result, "ACCGGGTTTT")
 
if __name__ == "__main__":
    unittest.main()
    