#!/bin/bash -l

#SBATCH --cluster=genius
#SBATCH --time=24:00:00
#SBATCH --nodes=3
#SBATCH --ntasks-per-node=36
#SBATCH --account=lkulak_daphnia_gp

cd /staging/leuven/stg_00106/PlasticDaphnia-Oomycytes/quality_filt

while IFS= read -r id; do
	/staging/leuven/stg_00106/tools/MEGAHIT-1.2.9-Linux-x86_64-static/bin/megahit -1 "${id}_qc.R1.fastq.gz" -2 "${id}_qc.R2.fastq.gz" -o /staging/leuven/stg_00106/PlasticDaphnia-Oomycytes/assembly/${id} --out-prefix $id -t 36
done < ./samples

cd /staging/leuven/stg_00106/PlasticDaphnia-Oomycytes/host-depleted

while IFS= read -r id; do
	/staging/leuven/stg_00106/tools/MEGAHIT-1.2.9-Linux-x86_64-static/bin/megahit -1 "${id}_noHost_R1.fastq.gz" -2 "${id}_noHost_R2.fastq.gz" -o /staging/leuven/stg_00106/PlasticDaphnia-Oomycytes/assembly/${id} --out-prefix $id -t 36
done < ./ID
