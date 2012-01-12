#!/usr/bin/python
# sort_agp.py

import sys
import agp

assembly_dir = sys.argv[1]
scaffolds = agp.load(open(assembly_dir + '/454Scaffolds.txt'))

for length, object_id in sorted([(value,key) for (key,value) in scaffolds.lengths.items()], reverse=True):
    for x in scaffolds.objects[object_id]:
        print x

