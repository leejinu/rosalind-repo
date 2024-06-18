from Bio import SeqIO
from Bio import Seq

def read_file(path):
    seqs = []
    with open(path, 'r') as f:
        for s in SeqIO.parse(f, "fasta"):
            seqs.append(s.seq)

    s = seqs[0]
    t = seqs[1]
    return s,t

    
def edit_distance(s,t):
    n = len(s)
    m = len(t)
    E = [[0 for _ in range(0,m+1)] for _ in range(0,n+1)]

    for i in range(1, n+1):
        E[i][0] = i
    for j in range(1, m+1):
        E[0][j] = j
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i-1] == t[j-1]:
                E[i][j] = E[i-1][j-1]
            else:
                E[i][j] = min(E[i-1][j]+1, E[i][j-1]+1, E[i-1][j-1]+1)
    return E[n][m]     

s, t = read_file('rosalind_edit.txt')

print(edit_distance(s, t))


