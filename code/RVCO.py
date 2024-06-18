def match_reverse_complement(path):
    count = 0
    with open(path, 'r') as f:
        for i, record in enumerate(SeqIO.parse(f,"fasta")):
            if record.seq == record.seq.reverse_complement():
                count += 1
            else:
                continue

    return count

if __name__== "__main__":
    from Bio import SeqIO
    count = match_reverse_complement('rosalind_rvco.txt')

    print(count)


        
