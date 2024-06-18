def read_file(path):
    with open(path,'r') as f:
        lines = f.read().split('\n')

    n = int(lines[0])
    
    lines[1] = lines[1][1:len(lines[1])-1]
    A = lines[1].split(', ')
    A = set([int(x) for x in A])
    lines[2] = lines[2][1:len(lines[2])-1]
    B = lines[2].split(', ')
    B = set([int(x) for x in B])
    return n, A, B

A = []
B = []
n, A, B = read_file('rosalind_seto.txt')

U = set(range(1,n+1))

print(A | B) # A U B: union
print(A & B) # A ∩ B: intersaction
print(A - B) # A - B: set difference
print(B - A) # B - A: set difference
print(U - A) # Ac: set complement of A w.r.t U
print(U - B) # Bc: set complement of B w.r.t U
