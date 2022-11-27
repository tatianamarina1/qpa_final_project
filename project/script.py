from data_io import read_codon_table, read_codon_db, read_dna_rna_db, read_genome
import matplotlib.pyplot as plt 

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


def plot_genome(string, step=100, output_file='image/gc_ratio.png'):
    x = []
    y = []
    for i in range(0, len(string), step):
        block = string[i:i + step]
        if len(block) != step:
            break
        g_count = block.count('G')
        c_count = block.count('C')
        gc_ratio = (g_count + c_count) * 100 / step
        x.append(i)
        y.append(gc_ratio)
        
    # plotting the points  
    plt.plot(x, y)
    # naming the x axis 
    plt.xlabel('genome position') 
    # naming the y axis 
    plt.ylabel('GC-ratio') 
    
    plt.savefig(output_file)
    # function to show the plot 
    plt.show()