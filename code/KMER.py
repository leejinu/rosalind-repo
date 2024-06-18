from itertools import combinations

def read_file(filename):
    alphabet = []
    
    with open(filename, 'r') as f:
        lines = f.read().split('\n')
        alphabet = lines[0].split()

        n = int(lines[1])        

    return alphabet, n

def permutation(alphabet, n):
    
    result = []
    alphabet = alphabet * n
    result = list(combinations(alphabet, n))

    result = set(result)
    result = sorted(result)
    return result

# Make 4-mer list
alphabet = []
alphabet, n = read_file('rosalind_lexf.txt') # alphabet  -> A,G,C,T , n -> 4

result = []
result = permutation(alphabet, n)

kmer_list = []

for pair in result:
    kmer_list.append(''.join(pair))

numbers= [0 for _ in kmer_list]
count_list = dict(zip(kmer_list,numbers))

    
# read sequence
def read_seq(filename):
    seq = ""
    with open(filename, 'r') as f:
        lines = f.read().split('\n')

    for line in lines:
        if line.startswith('>') is False:
            seq += line.strip()

    return seq
# split 4mer
def split_4mer(seq):
    the4merlist = []

    for i in range(0, len(seq)):
        if i == len(seq)-3:
            break
        if len(seq[i:i+4]) == 4:
            the4merlist.append(seq[i:i+4])

    return the4merlist

# main code
seq = read_seq('rosalind_kmer.txt')

the4merlist = []
the4merlist = split_4mer(seq)

for the4mer in the4merlist:
    count_list[the4mer] += 1

# display result
for value in count_list.values():
    print(value, end = ' ')

    


