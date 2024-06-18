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

alphabet = []
alphabet, n = read_file('rosalind_lexf.txt')

result = []
result = permutation(alphabet, n)

for pair in result:
    print(''.join(pair))
