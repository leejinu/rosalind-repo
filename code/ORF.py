codontab = {
    'TCA': 'S',    # Serina
    'TCC': 'S',    # Serina
    'TCG': 'S',    # Serina
    'TCT': 'S',    # Serina
    'TTC': 'F',    # Fenilalanina
    'TTT': 'F',    # Fenilalanina
    'TTA': 'L',    # Leucina
    'TTG': 'L',    # Leucina
    'TAC': 'Y',    # Tirosina
    'TAT': 'Y',    # Tirosina
    'TAA': '*',    # Stop
    'TAG': '*',    # Stop
    'TGC': 'C',    # Cisteina
    'TGT': 'C',    # Cisteina
    'TGA': '*',    # Stop
    'TGG': 'W',    # Triptofano
    'CTA': 'L',    # Leucina
    'CTC': 'L',    # Leucina
    'CTG': 'L',    # Leucina
    'CTT': 'L',    # Leucina
    'CCA': 'P',    # Prolina
    'CCC': 'P',    # Prolina
    'CCG': 'P',    # Prolina
    'CCT': 'P',    # Prolina
    'CAC': 'H',    # Histidina
    'CAT': 'H',    # Histidina
    'CAA': 'Q',    # Glutamina
    'CAG': 'Q',    # Glutamina
    'CGA': 'R',    # Arginina
    'CGC': 'R',    # Arginina
    'CGG': 'R',    # Arginina
    'CGT': 'R',    # Arginina
    'ATA': 'I',    # Isoleucina
    'ATC': 'I',    # Isoleucina
    'ATT': 'I',    # Isoleucina
    'ATG': 'M',    # Methionina
    'ACA': 'T',    # Treonina
    'ACC': 'T',    # Treonina
    'ACG': 'T',    # Treonina
    'ACT': 'T',    # Treonina
    'AAC': 'N',    # Asparagina
    'AAT': 'N',    # Asparagina
    'AAA': 'K',    # Lisina
    'AAG': 'K',    # Lisina
    'AGC': 'S',    # Serina
    'AGT': 'S',    # Serina
    'AGA': 'R',    # Arginina
    'AGG': 'R',    # Arginina
    'GTA': 'V',    # Valina
    'GTC': 'V',    # Valina
    'GTG': 'V',    # Valina
    'GTT': 'V',    # Valina
    'GCA': 'A',    # Alanina
    'GCC': 'A',    # Alanina
    'GCG': 'A',    # Alanina
    'GCT': 'A',    # Alanina
    'GAC': 'D',    # Acido Aspartico
    'GAT': 'D',    # Acido Aspartico
    'GAA': 'E',    # Acido Glutamico
    'GAG': 'E',    # Acido Glutamico
    'GGA': 'G',    # Glicina
    'GGC': 'G',    # Glicina
    'GGG': 'G',    # Glicina
    'GGT': 'G'     # Glicina
}

def read_file(filename):
    with open(filename, 'r') as f:
        lines = f.read().split('\n')

    sample_id = []
    seqs = []
    seq = ""
    
    for line in lines:
        if line.startswith('>') == True:
            sample_id.append(line[1:])
        else:
            seq +=line.strip()

    seqs.append(seq)
    return sample_id, seqs

def find_orf(seq, codontab):
    candidates = []
    candidate = "M"
    count = 0
    indexes = []
    
    for i, aa in enumerate(seq):
        if i == len(seq)-2:
            break
        start_codon = aa + seq[i+1]+ seq[i+2]
        if start_codon == 'ATG':
            count += 1
            indexes.append(i)
    print(indexes)
    for index in indexes:
        new_seq = seq[index:]
        
        for i in range(0,len(new_seq)-2,3):
            codon = new_seq[i] + new_seq[i+1]+new_seq[i+2]
            if codontab[codon] == '*':
                candidates.append(candidate)
                candidate = "M"
                break
            else:
                candidate += codontab[codon]
                
        
    return candidates
        
        
            
                
samples = []
seqs = []

filename = 'rosalind_orf.txt'
samples, seqs = read_file(filename)

candidate_proteins = []

reverse_seq= ""
for seq in seqs:
    for aa in seq:
        if aa == 'A':
            reverse_seq += 'T'
        elif aa == 'T':
            reverse_seq += 'A'
        elif aa == 'C':
            reverse_seq += 'G'
        elif aa == 'G':
            reverse_seq += 'C'

reverse_seq = reverse_seq[::-1]

print('reverse_seq')
print(reverse_seq)

candidate_proteins.append(find_orf(reverse_seq, codontab))

for seq in seqs:
    candidate_proteins.append(find_orf(seq, codontab))

printed_list = []
for candidate in candidate_proteins:
    for sequence in candidate:
        if sequence not in printed_list:
            print(sequence[1:])
            printed_list.append(sequence)
    

