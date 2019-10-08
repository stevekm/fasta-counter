#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Print number of characters in each fasta entry recursively

correct outut should be:

>chr1: 1261
>chr2: 1361
>chr3: 1311
>chr4: 1111
>chr5: 1161

"""
fasta = "hg19.snippet.fasta"

fin = open(fasta)

def count_nucleotides(fin, header, count = 0):
    """
    Count & print the number of nucleotides in each fasta entry recursively

    NOTE: Python recursive functions top out at ~3000 recursions, 
    so this will probably not support files larger than roughly 3000 lines
    """
    try:
        next_line = fin.next().strip()
        if not next_line.startswith('>'):
            count += len(next_line.strip())
            count_nucleotides(fin, header, count)
        else:
            print(header, count)
            count_nucleotides(fin, next_line, count = 0)
    except Exception as e:
        # need to catch the StopIteration error to print last entry
        print(header, count)

# find first header
for line in fin:
    if line.startswith('>'):
        first_header = line.strip()
        break
count_nucleotides(fin, first_header)


fin.close()
