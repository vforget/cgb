#!/usr/bin/python
################################################################################
#
# Vince Forgetta, 2010, McGill University
#
# Module with a Class to represent a Fasta sequence, 
# and methods to load Fasta-formatted sequences from a file.
#
################################################################################

import re
import string

# transliterate for reverse complement
trans = string.maketrans('ACGTacgt', 'TGCAtgca')
# re for fasta header
r = re.compile("^>(?P<name>\S+)(\s(?P<desc>.*))?")

class Fasta:
    ''' Simple class to store a fasta formatted sequence '''
    def __init__(self, name, desc, seq):
        self.name = name
        self.desc = desc
        self.seq = seq
        self.length = len(seq)
        
    def __str__(self):
        ''' Output FASTA format of sequence when 'print' method is called '''
        s = []
        for i in range(0, self.length, 80):
            s.append(self.seq[i:i+80])
        if self.desc:
            return ">%s %s\n%s" % (self.name, self.desc, "\n".join(s))
        else:
            return ">%s\n%s" % (self.name, "\n".join(s))
    
    def pretty_seq(self):
        s = []
        for i in range(0, self.length, 80):
            s.append(self.seq[i:i+80])
        return "\n".join(s)
    

    def reverse_complement(self):
        ''' Reverse complement sequence, return new Fasta object '''
        rcseq = self.seq[::-1].translate(trans)
        return Fasta(self.name, self.desc, rcseq)

def load(f):
    ''' Parameter: HANDLE to input in Fasta format 
        e.g. sys.stdin, or open(<file>)
        Returns array of Fasta objects.'''
    name, desc, seq = '', '', ''
    seqs = []
    while True:
        line = f.readline()
        if not line:
            break
            
        if line[0] == '>' and (line[1:].find(">") == -1):
            if seq != '':
                seqs.append(Fasta(name, desc, seq))

            seq = r""""""
            m = r.match(line)
            name = m.group("name")
            desc = m.group("desc")
        else:
            seq += line.strip()

    seqs.append(Fasta(name, None, seq))
    return seqs

def iter(f):
    ''' Parameter: HANDLE to input in Fasta format 
        e.g. sys.stdin, or open(<file>)
        Yields a Fasta object.'''
    name, desc, seq = '', '', ''
    while True:
        line = f.readline()
        if not line:
            break

        if line[0] == '>' and (line[1:].find(">") == -1):
            if seq != '':
                yield Fasta(name, desc, seq)
                
            seq = r""""""
            m = r.match(line)
            name = m.group("name")
            desc = m.group("desc")
        else:
            seq += line.strip()

    yield Fasta(name, desc, seq)
        
if __name__ == '__main__':
    ''' Example: print all sequences w/ length == 478 '''
    import sys
    for f in iter(sys.stdin):
        print f.length
#for f in iter(sys.stdin):
    #    if f.length == 478:
    #        print f
   # 

