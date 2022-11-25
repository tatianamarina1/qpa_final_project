'''
This module defines database structure
'''
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class DNA(Base):
    __tablename__ = "dna_bases"
    __table_args__ = {"extend_existing": True}
    
    id = Column(Integer, primary_key=True)
    dna_gene = Column(String(1))
    rna_gene = relationship("RNA", back_populates="dna_gene", uselist=False)
    rna_gene_id = Column(Integer, ForeignKey("rna_bases.id"), nullable=False)
    
    def __repr__(self):
        return f"DNA(dna_gene={self.dna_gene}, rna_gene={self.rna_gene})"

class RNA(Base):
    __tablename__ = "rna_bases"
    __table_args__ = {"extend_existing": True}
    
    id = Column(Integer, primary_key=True)
    rna_gene = Column(String(1))
    dna_gene = relationship("DNA", back_populates="rna_gene", uselist=False)

    def __repr__(self):
        return f"RNA(rna_gene={self.rna_gene})"

class Codon(Base):
    __tablename__ = "codon_table"
    __table_args__ = {"extend_existing": True}
    
    id = Column(Integer, primary_key=True)
    codon = Column(String(3))
    amino_acid_id = Column(Integer, ForeignKey("amino_acid_table.id"))
    amino_acid = relationship("Polypeptide", back_populates="codons")
    
    def __repr__(self):
        return f"Codon(codon={self.codon}, amino_acid={self.amino_acid})"

class Polypeptide(Base):
    __tablename__ = "amino_acid_table"
    __table_args__ = {"extend_existing": True}
    
    id = Column(Integer, primary_key=True)
    amino_acid = Column(String(1))
    codons = relationship("Codon", back_populates="amino_acid")
    
    def __repr__(self):
        return f"Polypeptide(amino_acid={self.amino_acid})"
