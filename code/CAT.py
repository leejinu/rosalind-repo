def readfile(path):
    seq = ""
    with open(path) as f:
        for s in SeqIO.parse(f, "fasta"):
            seq = str(s.seq)
    return seq

def mapping(seq):

    nt_map = {'A': 'U', 'C': 'G', 'G':'C', 'U':'A'}

    

if __name__ == "__main__":
    from Bio import SeqIO
    from Bio import Seq
    import math
    seq = readfile('rosalind_cat.txt')
    
   



    
