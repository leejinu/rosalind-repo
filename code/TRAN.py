def extract_seqs(filename):
    with open(filename, 'r') as f:
        lines = f.read().split('\n')

    seqs = []
    seq = ""
    for line in lines:
        if line.startswith('>') is True:
            if len(seq) != 0:
                seqs.append(seq)
                seq = ""
        else:
            seq += line.strip()

    seqs.append(seq)
                
    return seqs
def type_mutation(nt1, nt2):

    transition = set([('A','G'), ('C','T'),('G','A'),('T','C')])

    if any((seq1, seq2) in transition or (seq2, seq1) in transition for seq1, seq2 in zip(nt1, nt2)):
        return 'transition'
    else:
        return 'transversion'


        
def calculate_ratio(seqs):
    transition = 0
    transversion = 0
    for i, nt in enumerate(seqs[0]):
        nt2 = seqs[1][i]
        if nt == nt2:
            continue
        elif type_mutation(nt, nt2) == 'transition':
            transition += 1
        elif type_mutation(nt, nt2) == 'transversion':
            transversion += 1
            
    ratio = transition/transversion

    return ratio


seqs = []

seqs = extract_seqs('rosalind_tran.txt')

result = calculate_ratio(seqs)

print(round(result,11))
