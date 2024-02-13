import sys
import numpy as np

idxstats='/Users/u0145079/Library/CloudStorage/OneDrive-KULeuven/Desktop/PlasticDaphnia/Oomycytes/BAM.SAM.counts/GC142490/GC142490_contig_read_count.txt'
tax_class = '/Users/u0145079/Library/CloudStorage/OneDrive-KULeuven/Desktop/PlasticDaphnia/Oomycytes/CAT/GC142490/GC142490_offical_contig_taxonomy.txt'
output = '/Users/u0145079/Library/CloudStorage/OneDrive-KULeuven/Desktop/PlasticDaphnia/Oomycytes'

        
f1=open(idxstats)
info_d={}
for line in f1:
    a=line.strip().split('\t')
    info_d[a[0]]={'s':float(a[1]), 'mr':float(a[2]), 'um':float(a[3])}


f2 = open(tax_class)
f2.readline()
for i in f2:
    a=i.strip().split('\t')
    info_d[a[0].rsplit('_', 1)[0]]['taxonomy']= i.replace(a[0], '').strip() #taxonomy attribute = the rest of the information from CAT line after the contig name

for i in info_d:
    if 'taxonomy' not in info_d[i] or 'ORF has no hit to database' in info_d[i]['taxonomy']:
        info_d[i]['taxonomy']='null'

total_reads= 0

for i in info_d:
    total_reads+=info_d[i]['mr']
    total_reads+=info_d[i]['um']

for i in info_d:
    if info_d[i]['s']==0:
        info_d[i]['cov']=0
    else:
        info_d[i]['cov']=(info_d[i]['mr']+info_d[i]['um'])/info_d[i]['s']

oomycytes=0

for i in info_d:
    if 'Eukaryota' in info_d[i]['taxonomy']:
        oomycytes+=(info_d[i]['mr']+info_d[i]['um'])/float(total_reads)

print('Oomycota', "{:.10f}".format(oomycytes))


