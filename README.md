# Quantori Python Academy Final Project - Genetic Code

This is the final project of Quantory Academy Python School. The main goal of the project is creating the application for genetic code analysis.

The application was build in #Python with #SQLAlchemy, #Matplotlib and #Unittest modules connecting with #PostgreSQL database and packed via #Docker.

The following tasks will be covered in this app:

1. Building the script for transcription DNA to RNA and for translation RNA to Protein.

2. Creating a database for data storage that includes four tables (dna_bases, rna_bases, codon_table, amino_acid_table) and relationship between them.

3. Plotting GC-content ratio in DNA strand with 100 bases as default size of a window. The horizontal axis of this graph is the genome position. The vertical axis is the G-C ratio in the window. Saving the plot in .png or .jpeg file.

GC-content is calculated as
(G + C) / (A + T + G + C) * 100%
where
G is the number of G-bases in the selected region (it may be the whole molecule or it's part)
C is the number of C-bases
and so on.

4. Packing the application into a Docker container. Creating a Postgres database in the second container. Adding a command-line arguments to the app.

5. Testing the functions for transcription, translation and GC-ratio calculation.