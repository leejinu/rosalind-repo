
def read_file(path):
    with open(path, 'r') as f:
        lines = f.read().split('\n')

    coding_dna= lines[0]
    amino_acids = lines[1]
    
    return coding_dna, amino_acids

def find_genetic_code_variant(dna_sequence, protein_sequence):
    # Try the standard genetic code variant (table=1) first
    translated_protein = translate(dna_sequence, to_stop=True)

    if translated_protein == protein_sequence:
        return 1  # Standard genetic code variant
    
    # Try other genetic code variants
    for table_id in [2,3,4,5,6,9,10,11,12,13,14,15]:
        translated_protein = translate(dna_sequence, table=table_id, to_stop=True)

        if translated_protein == protein_sequence:
            return table_id
    
    # If no match found
    return None

if __name__ == '__main__':
    from Bio.Seq import translate
    
    dna_sequence, protein_sequence = read_file('rosalind_rvco.txt')

    genetic_code_variant = find_genetic_code_variant(dna_sequence, protein_sequence)
    print("Genetic code variant:", genetic_code_variant)        
    

