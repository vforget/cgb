#!/usr/bin/python
################################################################################
# Usage: echo "variableStep  chrom=chrI" > depth.bed; python ~/ophiostoma/bin/python/454/coverage.py contigs.bed 454AlignmentInfo.tsv | sort -k 1 -n >> depth.bed


import sys

contig_f = sys.argv[1]
alinfo_f = sys.argv[2]

contigs = {}
for line in open(contig_f):
    fields = line.strip().split()
    
    contigs[fields[3]] = (int(fields[1]), \
                              (int(fields[2]) - int(fields[1])), \
                              fields[5])

fh = open(alinfo_f)
fh.readline()
contig_name = ''
# print 'variableStep  chrom=chrI'
for line in fh:
    if line[0] == '>':
        contig_name = line.strip().split()[0][1:]
    else:
        fields = line.strip().split()
        if contig_name in contigs:
            contig = contigs[contig_name]
            
            if contig[2] == '+' or contig[2] == '.':
                print (contig[0] + int(fields[0])), int(fields[3])
            elif contig[2] == '-':
                print (contig[0] + (contig[1] - int(fields[0])) + 1), \
                    int(fields[3])
            else:
                raise ValueError("Contig orientation must be one of "\
                                     "('+', '-', '.')")
            
