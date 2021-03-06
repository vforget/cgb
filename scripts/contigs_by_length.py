#!/usr/bin/python
# chrom.py

import fasta
import sys

assembly_file = "assembly.bed"

contigs_file = None
if not sys.argv[1]:
    contigs_file = "454AllContigs.fna"
else:
    contigs_file = sys.argv[1]

contigs = {}

for f in fasta.load(open(contigs_file)):
    contigs[f.name] = f
    
chrom = 'chrI'

print '>' + chrom
for line in open(assembly_file):
    fields = line.strip().split()
    s, e = int(fields[1]), int(fields[2])
    l = e - s
    if fields[3][0:3] == 'gap':
        sys.stdout.write('N' * l)
    else:
        strand = fields[5]
        if strand == '+':
            sys.stdout.write(contigs[fields[3]].seq)
        elif strand == '-':
            sys.stdout.write(contigs[fields[3]].reverse_complement().seq)
        elif strand == '.':
            sys.stdout.write(contigs[fields[3]].seq)
