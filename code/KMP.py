def readfile(path):
    seq = ""
    with open(path) as f:
        for s in SeqIO.parse(f, "fasta"):
            seq = str(s.seq)
    return seq

def makearray(pattern):
    P = [0 for _ in range(0, len(pattern))]
    n = len(pattern)
    j = 0
    for i in range(1, n):
        while j > 0 and pattern[i] != pattern[j]:
            j = P[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            P[i] = j
    return P

if __name__ == "__main__":
    from Bio import SeqIO
    from Bio import Seq
    seq = readfile('rosalind_kmp.txt')
    P = []
    P = makearray(seq)
    P = list(map(str,P))
    print(' '.join(P))
    
