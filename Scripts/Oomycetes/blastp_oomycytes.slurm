#!/bin/bash -l

#SBATCH --cluster=genius
#SBATCH --time=3:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=36
#SBATCH --account=lkulak_daphnia_gp

cd /staging/leuven/stg_00106/PlasticDaphnia-Oomycytes

/staging/leuven/stg_00106/tools/diamond-linux64/diamond blastp -d /staging/leuven/stg_00106/databases/nr-database/nr.dmnd -q Oomycota_merged.fa -o matches_oomycota.m8 -b12 -c2 --max-target-seqs 5 --evalue 1e-3 --threads 36


