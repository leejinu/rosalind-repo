"""
1.	Read sample name
2.	Read protein sequence in FASTA format
3.	Find location in the protein string where the N-glycosylation motif can be found(N{P}[ST]{P})
4.	Show a list of results about each uniport_id
"""
def findPM(protein_sequences):
    n = len(protein_sequences)

    result = []
    for i in range(0, n):
        location = ""
        for j, aa in enumerate(protein_sequences[i]):
            if j == len(protein_sequences[i])-3:
                break
            if aa == 'N':
                if protein_sequences[i][j+1] != 'P':
                    if protein_sequences[i][j+2] == 'S' or protein_sequences[i][j+2] == 'T':
                        if protein_sequences[i][j+3] != 'P':
                            location += (str(j+1)+" ")
        result.append(location)
    return result

def extract_id(arr):
    uniprot_id = []
    for sample in arr:
        words = sample.split('_')
        uniprot_id.append(words[0])
    return uniprot_id

# Extract uniprot_id
with open('rosalind_mprt.txt', 'r') as f:
    lines = f.read().split('\n')

uniprot_ids = extract_id(lines)
import requests as r
from Bio import SeqIO
from io import StringIO

print(uniprot_ids)

baseURL = "https://www.uniprot.org/uniprotkb/"
Seqs = []
for uni_id in uniprot_ids:
    currentURL = baseURL+uni_id+".fasta"
    response = r.post(currentURL)
    cData = ''.join(response.text)

    Seq = StringIO(cData)
    pSeq = list(SeqIO.parse(Seq, 'fasta'))
    Seqs.append(pSeq[0].seq)


# Find Protein Motif locations
locations = findPM(Seqs)

# Show result
for i, ids in enumerate(lines):
    if locations[i] != "":
        print(ids)
        print(locations[i])
    
