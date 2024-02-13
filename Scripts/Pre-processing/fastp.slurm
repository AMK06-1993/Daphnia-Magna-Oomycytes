#!/bin/bash

#SBATCH --cluster=genius
#SBATCH --time=12:00:00
#SBATCH --nodes=3
#SBATCH --ntasks-per-node=36
#SBATCH --account=lkulak_daphnia_gp

output=""

while IFS= read -r id; do
	/staging/leuven/stg_00106/tools/fastp -i "${id}_R1.fastq.gz" -I "${id}_R2.fastq.gz" -o $output/"${id}_qc.R1.fastq.gz" -O $output/"${id}_qc.R2.fastq.gz"  -j $output/"${id}_qc_fastp.json" -h $output/"${id}_qc_fastp.html" -w 16
done < ./ID


