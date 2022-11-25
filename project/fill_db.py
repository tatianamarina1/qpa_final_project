from sqlalchemy.orm import sessionmaker

from db_data_types import DNA, RNA, Codon, Polypeptide, Base
from script import read_codon_table, db_engine

Base.metadata.create_all(db_engine)

rna_a = RNA(rna_gene="A")
rna_c = RNA(rna_gene="C")
rna_g = RNA(rna_gene="G")
rna_u = RNA(rna_gene="U")

dna_a = DNA(dna_gene="A", rna_gene=rna_a)
dna_c = DNA(dna_gene="C", rna_gene=rna_c)
dna_g = DNA(dna_gene="G", rna_gene=rna_g)
dna_t = DNA(dna_gene="T", rna_gene=rna_u)

dna_bases = [dna_a, dna_c, dna_g, dna_t]

codon_dict = read_codon_table()

aminoacid_dict = {}
for key, value in codon_dict.items():
    if value not in aminoacid_dict:
        aminoacid_dict[value] = []
    aminoacid_dict[value].append(key)

codon_bases = []
for aminoacid_letter, codons in aminoacid_dict.items():
    aminoacid = Polypeptide(amino_acid=aminoacid_letter)
    for triplet in codons:
        codon = Codon(codon = triplet, amino_acid = aminoacid)
        codon_bases.append(codon)

Session = sessionmaker(bind=db_engine)
with Session() as session:
    session.add_all(dna_bases)
    session.add_all(codon_bases)
    session.commit()
    session.close()