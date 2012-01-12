#!/usr/bin/python
# Usage: chromByLen.py 454LargeContigs.fna chrI

import fasta
import sys

gap = "N" * 100

contig_file, cn, outdir = sys.argv[1], sys.argv[2], sys.argv[3]


# Load fasta file w/ contigs sequences. Typically, 454LargeContigs.fna
contigs = dict([(x.name, x) for x in fasta.load(open(sys.argv[1]))])

# get sorted list of contigs by length
lengths = [(contigs[x].length, x) for x in contigs]
lengths.sort(reverse=True)

cn = sys.argv[2]

# output BED tracks
cf = open(outdir + '/contigs.bed', 'w')
gf = open(outdir + '/gaps.bed', 'w')

cstart = 0
gn = 1
for length, name in lengths:
    print >> cf, cn, cstart, cstart+length, name, 1000, '+'
    cstart = cstart + length
    print >> gf, cn, cstart, cstart+100, 'gap%s' % gn
    cstart = cstart + len(gap)
    gn += 1

cf.close()
gf.close()

chromseq = gap.join([contigs[name].seq for length, name in lengths])
build = fasta.Fasta(cn, None, chromseq)

print build
