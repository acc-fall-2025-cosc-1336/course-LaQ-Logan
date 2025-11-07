import unittest
from src.homework.h_strings.strings import get_hamming_distance, get_dna_complement

class TestStrings(unittest.TestCase):

    def test_hamming(self):
        self.assertEqual(get_hamming_distance("GAGC", "GATC"), 1)
        self.assertEqual(get_hamming_distance("AAAA", "AAAA"), 0)
        self.assertEqual(get_hamming_distance("AAAA", "TTTT"), 4)


    def test_get_dna_complement(self):
        self.assertEqual(get_dna_complement("GTCA"), "TGAC")
        self.assertEqual(get_dna_complement("ATTA"), "TAAT")
        self.assertEqual(get_dna_complement("AAGTC"), "GACTT")
