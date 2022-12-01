import unittest

from script import convert_dna_to_rna, convert_rna_to_protein, gc_ratio_coordinates

class TestGenome(unittest.TestCase):

    def test_dna_to_rna(self):
        self.assertEqual(convert_dna_to_rna('ATTTGGCTACTAACAATCTA'), 'AUUUGGCUACUAACAAUCUA')
        self.assertEqual(convert_dna_to_rna('GTTGTAATGGCCTACATTA'), 'GUUGUAAUGGCCUACAUUA')
        self.assertEqual(convert_dna_to_rna('CAGGTGGTGTTGTTCAGTT'), 'CAGGUGGUGUUGUUCAGUU')
        self.assertEqual(convert_dna_to_rna('GCTAACTAAC'), 'GCUAACUAAC')
        self.assertEqual(convert_dna_to_rna('GCTAACTAACATCTTTGGCACTGTT'), 'GCUAACUAACAUCUUUGGCACUGUU')
        self.assertEqual(convert_dna_to_rna('TATGAAAAACTCAAA'), 'UAUGAAAAACUCAAA')
        self.assertEqual(convert_dna_to_rna('CCCGTCCTTGATTGGCTTGAAGAGAAGTTT'), 'CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU')
        
    def test_rna_to_protein(self):
        self.assertEqual(convert_rna_to_protein('AUUUGGCUACUAACAAUCUA'), 'IWLLTI')
        self.assertEqual(convert_rna_to_protein('GUUGUAAUGGCCUACAUUA'), 'VVMAYI')
        self.assertEqual(convert_rna_to_protein('CAGGUGGUGUUGUUCAGUU'), 'QVVLFS')
        self.assertEqual(convert_rna_to_protein('GCUAACUAAC'), 'AN.')
        self.assertEqual(convert_rna_to_protein('GCUAACUAACAUCUUUGGCACUGUU'), 'AN.HLWHC')
        self.assertEqual(convert_rna_to_protein('UAUGAAAAACUCAAA'), 'YEKLK')
        self.assertEqual(convert_rna_to_protein('CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU'), 'PVLDWLEEKF')
        
    def test_gc_ratio(self):
        string = 'AAAACCCTTTTGGGG'
        step = 3
        x, y = gc_ratio_coordinates(string, 3)
        x_expected, y_expected = [0, 3, 6, 9, 12], [0.0, 200/3, 100/3, 100/3, 100.0]
        self.assertEqual(x, x_expected)
        self.assertEqual(y, y_expected)
        
#    def test_dna_to_rna(self):
#        data = 'CAGGTGGTGTTGTTCAGTT'
#        expected = 'CAGGUGGUGUUGUUCAGUU'
#        actual = convert_dna_to_rna(data)
#        self.assertTrue(actual == expected, f'Should be {expected}')

#    def test_rna_to_protein_2(self):
#        data = 'AUUUGGCUACUAACAAUCUA'
#        expected = 'IWLLTI'
#        actual = convert_rna_to_protein(data)
#        self.assertTrue(actual == expected, f'Should be {expected}')
        
#    def test_rna_to_protein_stop(self):
#        data = 'GCUAACUAACAUCUUUGGCACUGUU'
#        expected = 'AN.HLWHC'
#        actual = convert_rna_to_protein(data)
#        self.assertTrue(actual == expected, f'Should be {expected}')
   

if __name__ == '__main__':
    unittest.main()