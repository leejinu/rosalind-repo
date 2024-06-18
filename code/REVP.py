def read_file(filename):
    with open(filename) as f:
        lines = f.read().split('\n')
    sample_name = ""
    seq = ""
    for line in lines:
        if line.startswith('>') is True:
           sample_name = line[1:]
        else:
            line = line.strip()
            seq += line
    print(seq)
    return sample_name, seq

def reverse(seq):
    reverse_seq = ""
    for nt in seq:
        if nt == 'A':
            reverse_seq += 'T'
        elif nt == 'T':
            reverse_seq += 'A'
        elif nt == 'C':
            reverse_seq += 'G'
        elif nt == 'G':
            reverse_seq += 'C'
    reverse_seq = reverse_seq[::-1]
    return reverse_seq
def palindrome(seq):
    locations = []
    lengths = []
    for length in range(4, 13, 2):
        for i, nt in enumerate(seq):
            left = seq[i:(i+int(length/2))]
            right = reverse(seq[i+int(length/2):i+length])
            if  left == right:
                locations.append(i+1)
                lengths.append(length)
    
    return locations, lengths
                
samples, seq = read_file('rosalind_revp.txt')

locations = []
lengths = []


locations, lengths = palindrome(seq)

result = list(zip(locations, lengths))
print(result)

result.sort(key = lambda x:x[0])

print(result)

for item in result:
    print(item[0],item[1],sep= ' ')
        
    
