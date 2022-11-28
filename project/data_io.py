from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_data_types import Codon, DNA

db_engine = create_engine("sqlite:///data/connection_rules.db")
codon_csv = 'data/codon_table.csv'


def read_codon_table():
    with open(codon_csv, 'rt', encoding='utf8') as codon_table:
        contents = codon_table.readlines()
    codon_dict = {}
    for line in contents:
        codon = line.split(',')
        codon_dict[codon[0]] = codon[2].replace('Stop', '.')
    return codon_dict


def read_codon_db():
    Session = sessionmaker(bind=db_engine)
    with Session() as session:
        all_codons = session.query(Codon).all()
        codon_map = {}
        for item in all_codons:
            codon_map[item.codon] = item.amino_acid.amino_acid
    return codon_map


def read_dna_rna_db():
    Session = sessionmaker(bind=db_engine)
    with Session() as session:
        dna_rna_table = session.query(DNA).all()
        dna_rna_map = {}
        for item in dna_rna_table:
            dna_rna_map[item.dna_gene] = item.rna_gene.rna_gene
    return dna_rna_map


def read_genome(path_to_file):
    with open(path_to_file, 'rt', encoding='utf-8') as genome_file:
        contents = genome_file.readlines()
    return ''.join([row.strip() for row in contents[1:]])
        
    