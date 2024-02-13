#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 21:44:55 2024

@author: u0145079
"""

csv_data='/Users/u0145079/Library/CloudStorage/OneDrive-KULeuven/Desktop/PlasticDaphnia/Oomycytes/CAT/GC142490/GC142490_offical_contig_taxonomy.txt'
matching_orfs = []

with open(csv_data, 'r') as f1:
    next(f1)  # Skip header if there is one
    for line in f1:
        columns = line.strip().split('\t')
        # Assuming the taxonomy information starts from the 5th column onwards in your file
        taxonomy_info = columns[4:]  # Adjust index as necessary based on your file's structure

        # Check for "Oomycota" and "Sar" within the taxonomy columns
        if any("Oomycota" in info for info in taxonomy_info):
            orf_name = columns[0]  # Assuming the ORF name is in the first column
            matching_orfs.append(orf_name)

# Display or use the list of matching ORF names
print("Matching ORF names:", matching_orfs)

# Path to the .fasta file
fasta_data = '/Users/u0145079/Library/CloudStorage/OneDrive-KULeuven/Desktop/PlasticDaphnia/Oomycytes/Eukaryote-proteins/GC142490_CAT.predicted_proteins.faa'  # Update this path to your actual .fasta file location

# Output file where matched sequences will be saved
output_file = '/Users/u0145079/Library/CloudStorage/OneDrive-KULeuven/Desktop/PlasticDaphnia/Oomycytes/Eukaryote-proteins/Oomycota/GC142490_OOmycota+Sar_sequences.fa'  # Update this path to where you want to save the matched sequences

with open(fasta_data, 'r') as fasta, open(output_file, 'w') as out_fa:
    write_sequence = False
    for line in fasta:
        if line.startswith('>'):
            # Extract the ORF identifier from the header
            orf_identifier = line.split(' ')[0][1:]  # Removes '>' and splits by space, taking the first part as identifier
            if orf_identifier in matching_orfs:
                out_fa.write(line)  # Write the header line
                write_sequence = True  # Set flag to start writing sequence lines
            else:
                write_sequence = False  # Reset flag if ORF is not in the list
        elif write_sequence:
            out_fa.write(line)  # Write the sequence lines

print("Matching sequences have been written to", output_file)