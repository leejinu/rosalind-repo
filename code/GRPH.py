def compare_sequences(a, b, k):
    if b[:k] == a[-k:]:
        return True
    else:
        return False

# Open file
filename = 'rosalind_grph.txt'
f = open(filename, 'r')

# Check the existence of file
if f is False:
    print("{Error} "+filename+" does not exist.")
    print("Terminate the program.")
    exit()
"""print(f)"""
# Read the file
text = f.read()

"""print(lines)"""

# Make array for the lines
lines = text.split()

samples = []
sequences = []

# Only save seqeunces
for i in range(0, len(lines),3):
    label = lines[i][1:]
    sequence = lines[i+1].replace('\n','')+lines[i+2].replace('\n','')
    samples.append(label)
    sequences.append(sequence)


"""
print("samples: ", end= '')
print(samples)
print("sequences: ", end = '')
print(sequences)
"""

N = len(samples)

rows = N
cols = N
k = 3

# Initialize the adjacency lits
adj_list = [[0]*cols for _ in range(rows)]
"""
print("length of list cols: "+str(len(adj_list)))
print("length of list rows: "+str(len(adj_list[0])))
"""
# Compare each sequence
result = []
for i, seq in enumerate(sequences):
    for j, seq2 in enumerate(sequences):
        if i == j:
            continue
        elif compare_sequences(seq, seq2,k) == True:
            adj_list[i][j] = 1
            output = samples[i]+" "+samples[j]
            result.append(output)
        else:
            continue
"""
print("Adjacency_list")
for i in range(len(adj_list)):
    for j in range(len(adj_list)):
        print(adj_list[i][j], end=' ')
    print()
"""

for line in result:
    print(line)


