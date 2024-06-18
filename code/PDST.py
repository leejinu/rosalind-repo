def readfile(path):
    seqs = []
    with open(path) as f:
        for s in SeqIO.parse(f, "fasta"):
            seqs.append(str(s.seq))
    return seqs

def p_distance(s1,s2):
    return round(1-sum(a==b for a, b in zip(s1, s2))/len(s1), 5)

if __name__ == "__main__":
    from Bio import SeqIO
    from Bio import Seq
    
    seqs = []
    seqs = readfile('rosalind_pdst.txt')

    for i, seq1 in enumerate(seqs):
        for j, seq2 in enumerate(seqs):
            if i == j:
                print("0.00000", end = ' ')
            else:
                print(format(p_distance(seq1, seq2),"0.5f"), end = ' ')
        print()
        
               
    
   



    
