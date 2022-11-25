from sqlalchemy import create_engine

def read_codon_table():
    path_to_file = 'data/codon_table.csv'
    
    with open(path_to_file, 'rt', encoding='utf8') as codon_table:
        contents = codon_table.readlines()
        
    codon_dict = {}
    
    for line in contents:
        codon = line.split(',')
        codon_dict[codon[0]] = codon[2].replace('Stop', '.')
    
    return codon_dict

CODON_DICT = read_codon_table()

def convert_dna_to_rna(string):
    return str(string).replace("T", "U")

def convert_rna_to_protein(string):
    
    protein = []
    for i in range(0, len(string), 3):
        if len(string[i:i + 3]) != 3:
            break
        triplet = string[i:i + 3]
        amino_acid = CODON_DICT[triplet]
        protein.append(amino_acid)
    return ''.join(protein)

db_engine = create_engine("sqlite:///data/connection_rules.db", echo=True)

