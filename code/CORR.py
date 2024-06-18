def correct_incorrect(counts, orig_seqs):
    correct = []
    incorrect = []
    for s in counts:
        if counts[s] >= 2:
            correct.append(s)
        elif s in orig_seqs:
            incorrect.append(s)
    return correct, incorrect


def hamming(seq1, seq2):
    mutations = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            mutations += 1
    return mutations


def corrections(correct, incorrect):
    corrected = []
    for seq1 in incorrect:
        for seq2 in correct:
            if hamming(seq1, seq2) == 1:
                corrected.append([seq1, seq2])
    return corrected

if __name__ == "__main__":
    from Bio import SeqIO
    from Bio import Seq
    from collections import Counter

    f = open("rosalind_corr.txt", 'r')
    seqs = []
    orig_seqs = [] # kept for later comparisons
    for s in SeqIO.parse(f, "fasta"):
        orig_seqs.append(str(s.seq))
        seqs.append(str(s.seq))
        seqs.append(str(s.seq.reverse_complement()))
    f.close()

    counts = Counter(seqs)
    correct, incorrect = correct_incorrect(counts, orig_seqs)
    corrs = corrections(correct, incorrect)
    print(len(corrs))

    for i in corrs:
        print("->".join(i))

