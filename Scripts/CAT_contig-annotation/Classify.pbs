#!/bin/bash -l
#SBATCH --cluster=genius
#SBATCH --time=24:00:00
#SBATCH --nodes=3
#SBATCH --ntasks-per-node=36
#SBATCH --account=lkulak_daphnia_gp

cd /staging/leuven/stg_00106/PlasticDaphnia-Oomycytes/assembly

while IFS= read -r id; do	
	/staging/leuven/stg_00106/PlasticDaphnia-Field-Shotgun/scripts/CAT/CAT-5.2.3/CAT_pack/CAT contigs -c ${id}/${id}.contigs.fa -d /staging/leuven/stg_00088/Tinh/Software/cat/CAT_prepare_20210107/2021-01-07_CAT_database -t /staging/leuven/stg_00088/Tinh/Software/cat/CAT_prepare_20210107/2021-01-07_taxonomy --path_to_diamond /staging/leuven/stg_00088/Tinh/Software/cat/CAT_prepare_20210107/Diamond_2.0.6/diamond --nproc 36 --out_prefix "${id}_CAT" --path_to_prodigal /staging/leuven/stg_00106/tools/Prodigal-2.6.3/prodigal
done < ./ID

	
