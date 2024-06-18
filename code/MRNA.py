codon_dict = {'F': ('UUU', 'UUC'),
              'L': ('UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'),
              'S': ('UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'),
              'Y': ('UAU', 'UAC'),
              '_': ('UAA', 'UAG', 'UGA'),
              'C': ('UGU', 'UGC'),
              'W': ('UGG',),
              'P': ('CCU', 'CCC', 'CCA', 'CCG'),
              'H': ('CAU', 'CAC'),
              'Q': ('CAA', 'CAG'),
              'R': ('CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'),
              'I': ('AUU', 'AUC', 'AUA'),
              'M': ('AUG',),
              'T': ('ACU', 'ACC', 'ACA', 'ACG'),
              'N': ('AAU', 'AAC'),
              'K': ('AAA', 'AAG'),
              'V': ('GUU', 'GUC', 'GUA', 'GUG'),
              'A': ('GCU', 'GCC', 'GCA', 'GCG'),
              'D': ('GAU', 'GAC'),
              'E': ('GAA', 'GAG'),
              'G': ('GGU', 'GGC', 'GGA', 'GGG')
             }

def calculate_RNA_strings(seq, codon_table):
    n = 1
    for aa in seq:
        n *= len(codon_table[aa])
    # Consider stop codon
    n = n*len(codon_table['_'])
    return n
    
seq = input()

n = calculate_RNA_strings(seq, codon_dict)

result = n % 1000000

print(result)
