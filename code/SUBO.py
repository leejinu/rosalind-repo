def read_fasta(path):
    seqs = []
    for seq_record in SeqIO.parse(path, "fasta"):
        seqs.append(str(seq_record.seq))
    s= seqs[0]
    t=seqs[1]
    return s, t

def hamming_distance(seq1, seq2):
    """Calculate the Hamming distance between two sequences."""
    return sum(ch1 != ch2 for ch1, ch2 in zip(seq1, seq2))

def calculate_occurrence(seq, motif, max_modifications=3):
    """Count the occurrences of the motif in the sequence allowing up to max_modifications."""
    motif_len = len(motif)
    count = 0

    for i in range(len(seq) - motif_len + 1):
        window = seq[i:i + motif_len]
        if hamming_distance(window, motif) <= max_modifications:
            count += 1
    
    return count
            
        
if __name__ == "__main__":
    from Bio import SeqIO

    s, t = read_fasta('rosalind_subo.txt')

    r = input("Enter shared sequence r: ")

    occ_s = calculate_occurrence(s, r)
    occ_t = calculate_occurrence(t, r)

    print(occ_s,occ_t)



    

    
