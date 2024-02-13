#!/bin/bash

# Path to your .m8 file
blast_output_file="/staging/leuven/stg_00106/PlasticDaphnia-Oomycytes/matches_oomycota.m8"

# Check if the file exists
if [ ! -f "$blast_output_file" ]; then
    echo "File not found: $blast_output_file"
    exit 1
fi

# Extract the second column (NCBI identifiers), count unique occurrences, sort numerically in descending order, and get the top 5
awk '{print $2}' "$blast_output_file" | sort | uniq -c | sort -nr | head -n 5

