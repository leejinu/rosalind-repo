def read_file(filename):
    with open(filename) as f:
        lines = f.read().split('\n')
    sample_names = []
    seqs = []
    seq = ""
    for line in lines:
        if line.startswith('>') is True:
            if seq is not "":
                seqs.append(seq)
            sample_names.append(line[1:])
            seq = ""
        else:
            line = line.strip()
            seq += line
            if line == lines[len(lines)-1]:
                seqs.append(seq)

    return sample_names, seqs

def RNA_splicing(seqs):
    whole_seq = seqs[0]
    introns = []
    
    for i, seq in enumerate(seqs):
        if i == 0:
            continue
        introns.append(seq)
    for intron in introns:
        whole_seq = whole_seq.replace(intron, '')

    exon = whole_seq
    return exon
        

def translate_codon(codon):
    codon_table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    return codon_table.get(codon, 'X')

def translate_dna_sequence(dna_sequence):
    protein_sequence = ''
    for i in range(0, len(dna_sequence), 3):
        codon = dna_sequence[i:i+3]
        if translate_codon(codon) is not '_':
            protein_sequence += translate_codon(codon)
    return protein_sequence

sample_names = []
seqs = []

filename = 'rosalind_splc.txt'
sample_names, seqs = read_file(filename)

exon = RNA_splicing(seqs)

result = translate_dna_sequence(exon)
print(result)


    
