"""
from itertools import combinations
import itertools

def read_file(filename):
    alphabet = []
    
    with open(filename, 'r') as f:
        lines = f.read().split('\n')
        alphabet = lines[0].split()

        n = int(lines[1])        

    return alphabet, n

def product(alphabet, n):
    
    result = []
    alphabet = alphabet * n
    result = list(combinations(alphabet, n))

    result = set(result)
    final = []
    for pair in result:
        final.append(''.join(pair))
    
    return final

def set_lexicographic_order(alphabet):
    order = dict()
    nums = list(range(len(alphabet), 0 , -1))
    order = dict(zip(alphabet, nums))
    print(order)
    return order
        
        


    
alphabet = []
alphabet, n = read_file('rosalind_lexf.txt')

order = dict()
order = set_lexicographic_order(alphabet)
temp_result = []
for i in range(0, n+1):
    temp_result.append(product(alphabet, i))

result = sum(temp_result, [])

result = result[1:]




result = []
for i in range(0, n+1):
    result.append(product(alphabet, i))

result = list(itertools.chain(*result))
result = sorted(result, reverse = True)
for pair in result:
    print(''.join(pair))

"""

from itertools import product

def parse_input(input_file):
    with open(input_file, 'r') as f:
        alphabet = f.readline().strip().split()
        n = int(f.readline())
    return alphabet, n

def generate_strings(alphabet, n):
    strings = []
    for length in range(1, n+1):
        for perm in product(alphabet, repeat=length):
            strings.append(''.join(perm))
    return strings

def lexicographic_order(strings, alphabet):
    return sorted(strings, key=lambda s: [alphabet.index(c) for c in s])

def write_output(output_file, ordered_strings):
    with open(output_file, 'w') as f:
        for s in ordered_strings:
            f.write(s + '\n')

def main(input_file, output_file):
    alphabet, n = parse_input(input_file)
    strings = generate_strings(alphabet, n)
    ordered_strings = lexicographic_order(strings, alphabet)
    write_output(output_file, ordered_strings)

if __name__ == "__main__":
    main("rosalind_lexv.txt", "output.txt")


