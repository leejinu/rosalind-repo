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
    T = [['-' for _ in range(0,m+1)] for _ in range(0, n+1)]
    
    for i in range(1, n+1):
        E[i][0] = i
        T[i][0] = 'U'
        
    for j in range(1, m+1):
        E[0][j] = j
        T[0][j] = 'L'
        
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i-1] == t[j-1]:
                E[i][j] = E[i-1][j-1]
                T[i][j] = 'D'
            else:
                E[i][j] = min(E[i-1][j]+1, E[i][j-1]+1, E[i-1][j-1]+1)
                if E[i][j] == E[i-1][j]+1:
                    T[i][j] = 'U'
                elif E[i][j] == E[i][j-1]+1:
                    T[i][j] = 'L'
                else:
                    T[i][j] = 'D'


    i = n
    j = m
    seq1 = ""
    seq2 = ""
    
    while i > 0 and j > 0:
        if T[i][j] == 'D':
            seq1 += s[i-1]
            seq2 += t[j-1]
            i -= 1
            j -= 1
        elif T[i][j] == 'L':
            seq1 += '-'
            seq2 += t[j-1]
            j -= 1
        elif T[i][j] == 'U':
            seq1 += s[i-1]
            seq2 += '-'
            i -= 1
        else:
            break
        
    seq1 = seq1[::-1]
    seq2 = seq2[::-1]

            
    return E[n][m], seq1, seq2   


if __name__ == "__main__":
    from Bio import SeqIO
    from Bio import Seq

    s, t = read_file('rosalind_edta.txt')

    ed, seq1, seq2 = edit_distance(s, t)

    print(ed)
    print(seq1)
    print(seq2)
    

    


