# Quantori Python Academy Final Project - Genetic Code

## Description

This is the final project of **Quantory Academy Python School**. The main goal of the project is creating the application for genetic code analysis.

The project was build in **Python** with **SQLAlchemy**, **Matplotlib** and **Unittest** modules connecting with **PostgreSQL** database and packed via **Docker**.

The following tasks will be covered in this project:

1. Building the script for transcription DNA to RNA and for translation RNA to Protein.

2. Creating a database for data storage that includes four tables (dna_bases, rna_bases, codon_table, amino_acid_table) and relationship between them.

3. Plotting GC-content ratio in DNA strand with 100 bases as default size of a window. Saving the plot in .png or .jpeg file.

4. Packing the project into a Docker container. Creating a Postgres database in the second container. Adding a command-line arguments to the app.

5. Testing the functions for transcription, translation and GC-ratio calculation.

## Table of Contents

*project/script.py*

Consists of functions:

**mandatory**
- *convert_dna_to_rna* transcripts DNA strand to RNA strand. The input and output data set as strings.
- *convert_rna_to_protein* translates every codon of RNA strand to protein. The input and output data set as strings.
- *plot_genome* plots graph "GC-content ratio". The horizontal axis of this graph is the genome position. The vertical axis is the G-C ratio in the window. Default size of a window is 100 bases and called *step*.

**auxiliary**
- *gc_ratio_value* calculates GC-ratio for one interval
- *gc_ratio_coordinates* calculates two lists. The first list includes genome position like 0, step, 2*step, 3*step, and so on. The second one includes GC-ratio for this intervals in DNA strand.

*project/test.py*

Consists of three functions *test_dna_to_rna*, *test_rna_to_protein*, *test_gc_ratio* that tests *convert_dna_to_rna*, *convert_rna_to_protein*, and *gc_ratio_coordinates* respectively.

*project/data_io.py* implements functions for reading tables from file or from database and return dictionaries to use in script.py. Also it includes *read_genome* to read genome sequence from file.

*project/db_data_types.py* defines database structure

*project/fill_db.py* fills Database with tables

*project/sars_cov_2_plot_gc_ratio.py* plots GC-ratio for genome sequence as an example

*project/data* includes *codon_table.csv* that maps codon of RNA to protein, *connection_rules.db* that was created via sqlite-command, *sars_cov_2.fna* that was used as GC-ratio example

*project/image* includes output file for GC-ratio graph

## How to Install and Run the Project

1. Create *network* using command 'docker network create <name>'. Example: 'docker network create genome_net'

2. Set name and password for database and run command 'docker run -it --name genome_db -v <path>:/var/lib/postgresql/data -p 5432:5432 -e POSTGRES_PASSWORD=<psw> -e POSTGRES_DB=<name> --network <name> postgres'. 
    Example:
'docker run -it --name genome_db -v C:\Users\suri-\Python_scripts\Quantori\q_final_project\project\genome_db:/var/lib/postgresql/data -p 5432:5432 -e POSTGRES_PASSWORD=docker -e POSTGRES_DB=genome_db --network genome_net postgres'
    
3. To fill database use command 'docker run -v C:\Users\suri-\Python_scripts\Quantori\q_final_project\project\image:/image --network genome_net quantori_genome python fill_db.py'. Make sure that the correct URL is inside data_io.py.
    Example: 'db_engine = create_engine("postgresql+psycopg2://postgres:docker@genome_db:5432/genome_db")'

3. Build docker for the project via command 'docker build -t quantori_genome .' 

4. To work with Command Line Arguments set function from *script.py* and set input data (like *string* and *step*)
    Examples:
'docker run -v C:\Users\suri-\Python_scripts\Quantori\q_final_project\project\image:/image --network genome_net quantori_genome python script.py plot_genome AAAACCCTTTTGGGG 3'

'docker run -v C:\Users\suri-\Python_scripts\Quantori\q_final_project\project\image:/image --network genome_net quantori_genome python script.py convert_dna_to_rna AAAACCCTTTTGGGG'

'docker run -v C:\Users\suri-\Python_scripts\Quantori\q_final_project\project\image:/image --network genome_net quantori_genome python script.py convert_rna_to_protein AAAACCCUUUUGGGG'

5. Use the following command to run tests
'docker run -v C:\Users\suri-\Python_scripts\Quantori\q_final_project\project\image:/image --network genome_net quantori_genome python test.py'

