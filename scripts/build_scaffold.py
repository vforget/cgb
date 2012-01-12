#!/usr/bin/python
# sort_agp.py

import sys
import agp

build_dir = sys.argv[2]
scaffold_file = sys.argv[1]
scaffolds = agp.load(open(scaffold_file))

offset = 0
chrom = 'chrI'
gap_count = 0

cf = open(build_dir + "/contigs.bed", 'w')
sf = open(build_dir + "/scaffolds.bed", 'w')
gf = open(build_dir + "/gaps.bed", 'w')

sc = 0

for length, object_id in sorted([(value,key) for (key,value) in scaffolds.lengths.items()], reverse=True):
    for x in scaffolds.objects[object_id]:
        name = None
        # CONTIG
        if x.component_type != 'N':
            name = x.component_id
            s = "\t".join([str(y) for y in [chrom,
                                            (x.object_beg + offset - 1),
                                            (x.object_end + offset),
                                            name,
                                            1000,
                                            x.orientation
                                            ]])
            print >> cf, s
        # GAP
        else:
            gap_count += 1
            name = 'gap' + str(gap_count)
            s = "\t".join([str(y) for y in [chrom,
                                           (x.object_beg + offset - 1),
                                           (x.object_end + offset),
                                           name
                                           ]])
            print >> gf, s
            
    rgb = None

    # SCAFFOLDS, alternate gray/black
    if (sc % 2) == 1: 
        rgb = '165,165,165'
    else:
        rgb = '0,0,0'
    print >> sf, "\t".join([str(y) for y in [chrom,
                                             offset,
                                             offset + length,
                                             x.object_id,
                                             1000,
                                             '.',
                                             offset,
                                             offset + length,
                                             rgb
                                             ]])
    sc += 1
    offset += length
cf.close
sf.close
gf.close
