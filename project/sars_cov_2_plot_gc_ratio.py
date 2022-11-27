from script import plot_genome
from data_io import read_genome


string_genome = read_genome('data/sars_cov_2.fna')
#step = 100

plot_genome(string_genome)
