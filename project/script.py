from data_io import read_codon_table, read_codon_db, read_dna_rna_db

#CODON_DICT = read_codon_table()
CODON_DICT = read_codon_db()
DNA_RNA_DICT = read_dna_rna_db()


def convert_dna_to_rna(string):
    string_rna = []
    for char_dna in string:
        char_rna = DNA_RNA_DICT[char_dna]
        string_rna.append(char_rna)
        
    return ''.join(string_rna)


def convert_rna_to_protein(string):
    protein = []
    for i in range(0, len(string), 3):
        if len(string[i:i + 3]) != 3:
            break
        triplet = string[i:i + 3]
        amino_acid = CODON_DICT[triplet]
        protein.append(amino_acid)
    return ''.join(protein)
