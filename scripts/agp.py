#!/usr/bin/python
############################################################
class Component:
    ''' class for component line '''
    def __init__(self, object_id,  object_beg, object_end, part_number, component_type, component_id, component_beg,  component_end, orientation):
        self.object_id = object_id
        self.object_beg = int(object_beg)
        self.object_end = int(object_end)
        self.part_number = int(part_number)
        self.component_type = component_type
        self.component_id = component_id
        self.component_beg = int(component_beg)
        self.component_end = int(component_end)
        self.orientation = orientation
    def __str__(self):
        return "\t".join([str(x) for x in [self.object_id,
                                    self.object_beg,
                                    self.object_end,
                                    self.part_number,
                                    self.component_type,
                                    self.component_id,
                                    self.component_beg,
                                    self.component_end,
                                    self.orientation]])
        
class Gap:
    ''' class for gap line '''
    def __init__(self, object_id,  object_beg, object_end, part_number, component_type, gap_length, gap_type, linkage):
        self.object_id = object_id
        self.object_beg = int(object_beg)
        self.object_end = int(object_end)
        self.part_number = int(part_number)
        self.component_type = component_type
        self.gap_length = int(gap_length)
        self.gap_type = gap_type
        self.linkage = linkage
        
    def __str__(self):
        return "\t".join([str(x) for x in [self.object_id,
                                           self.object_beg,
                                           self.object_end,
                                           self.part_number,
                                           self.component_type,
                                           self.gap_length,
                                           self.gap_type,
                                           self.linkage]])
    
        
        
class Scaffold:
    def __init__(self):
        self.objects = {}
        self.lengths = {}

    def __getitem__(self, i):
        self.objects[i]
    
    def __setitem__(self, i, j):
        if not self.objects.get(i): 
            self.objects[i] = []
            self.lengths[i] = 0
        self.objects[i].append(j)
        self.lengths[i] += (j.object_end - j.object_beg + 1)


def load(fh):
    ''' Parses AGP format.
    Returns hash key\'ed on scaffold name. '''

    scaffolds = Scaffold()
    lengths = {}
    
    for line in fh:
        columns = line.split()
        component_type = columns[4]
        object_id = columns[0]
        item = None
        if component_type != "N": # component
            item = Component(*columns)
        else: # gap
            item = Gap(*columns)
        
        scaffolds[object_id] = item
    
    return scaffolds

