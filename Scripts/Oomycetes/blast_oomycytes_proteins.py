#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 11:18:23 2024

@author: u0145079
"""

from Bio import Entrez
from collections import Counter
import time

# Set your email here; NCBI requests you provide it
Entrez.email = ""

def get_organism(protein_id):
    try:
        handle = Entrez.efetch(db="protein", id=protein_id, rettype="gb", retmode="text")
        record = handle.read()
        organism_start = record.find("ORGANISM") + 9
        organism_end = record.find("\n", organism_start)
        organism = record[organism_start:organism_end].strip()
        return organism
    except Exception as e:
        print(f"Error fetching organism for {protein_id}: {e}")
        return None

def main():
    protein_ids = []
    with open('/Users/u0145079/Library/CloudStorage/OneDrive-KULeuven/Desktop/PlasticDaphnia/Oomycytes/Eukaryote-proteins/Oomycota/matches_oomycota.m8', 'r') as file:
        for line in file:
            parts = line.split('\t')
            if len(parts) > 1:
                protein_ids.append(parts[1])

    organism_counts = Counter()
    for protein_id in set(protein_ids):  # Use set to avoid duplicate queries
        organism = get_organism(protein_id)
        if organism:
            organism_counts[organism] += 1
        time.sleep(0.1)  # Sleep to avoid overwhelming NCBI servers

    top_organisms = organism_counts.most_common(3)
    for organism, count in top_organisms:
        print(f"{organism}: {count}")
        
"""
Aphanomyces astaci: 58
Aphanomyces euteiches: 53
Aphanomyces stellatus: 27

"""

if __name__ == "__main__":
    main()
