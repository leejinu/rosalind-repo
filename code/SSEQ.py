"""
Problem
A subsequence of a string is a collection of symbols contained in order
(though not necessarily contiguously) in the string
(e.g., ACG is a subsequence of TATGCTAAGATC).
The indices of a subsequence are the positions in the string at which the symbols of the subsequence appear;
thus, the indices of ACG in TATGCTAAGATC can be represented by (2, 5, 9).

As a substring can have multiple locations, a subsequence can have multiple collections of indices,
and the same index can be reused in more than one appearance of the subsequence;
for example, ACG is a subsequence of AACCGGTT in 8 different ways.

Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.

Return: One collection of indices of s in which the symbols of t appear as a subsequence of s.
If multiple solutions exist, you may return any one.
"""

def read_file(path):
    with open(path, 'r') as f:
        lines = f.read().split('\n')
    seqs = []
    seq = ""
    for line in lines:
        if line.startswith('>') is True:
            if seq != "":
                seqs.append(seq)
                seq = ""
                continue
        else:
            seq += line.strip()
    seqs.append(seq)
    
    s = seqs[0]
    t = seqs[1]
    
    return s, t

def find_spliced_motif(seq,t):
    indices = []
    j=0
    for i, nt in enumerate(seq):
        if len(indices) == len(t):
            break
        if nt == t[j]:
            j += 1
            indices.append(i+1)
    return indices

s, t = read_file('rosalind_fms.txt')
indices = []
indices = find_spliced_motif(s,t)
for idx in indices:
    print(idx, end = ' ')
        
            
        
            
