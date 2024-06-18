def readfile(path):
    seqs = []
    with open(path) as f:
        for s in SeqIO.parse(f, "fasta"):
            seqs.append(str(s.seq))
    return seqs

def find_shared_spliced_motif(s,t):
    m = len(s)
    n = len(t)

    # Initialize matrix
    mat = [[0 for x in range(0, n+1)] for y in range(0, m+1)]
    tracking = [[0 for x in range(0, n+1)] for y in range(0, m+1)]
    cs = ""
    # Filling Matrix
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                mat[i][j] = 0
                tracking[i][j] = "E" # empty
            elif s[i-1] == t[j-1]:
                mat[i][j] = mat[i-1][j-1] + 1
                tracking[i][j] = "D"
            else:
                if mat[i-1][j] >= mat[i][j-1]:
                    mat[i][j]= mat[i-1][j]
                    tracking[i][j] = "U"
                else:
                    mat[i][j] = mat[i][j-1]
                    tracking[i][j] = "L"
    return mat, tracking

def backtracking(seq1, seq2, tracking):
    m = len(tracking)-1
    n = len(tracking[0])-1
    lcs = ""
    
    while 1:
        if m <= 0 or n <= 0:
            break
        if tracking[m][n] == "D":
            lcs += seq1[m-1]
            m -= 1
            n -= 1
        elif tracking[m][n] == "U":
            m-=1
            seq1 = seq1[:m]
        elif tracking[m][n] == "L":
            n-=1
            seq2 = seq2[:n]
        elif tracking[m][n] == "E":
            break
            
    return lcs[::-1]
    
    
if __name__ == "__main__":
    from Bio import SeqIO
    from Bio import Seq
    
    seqs = []
    seqs = readfile('rosalind_lcsq.txt')
    s,t = seqs[0], seqs[1]

    mat, tracking = find_shared_spliced_motif(s, t)

    print(backtracking(s,t, tracking))
    
               
    
   



    
