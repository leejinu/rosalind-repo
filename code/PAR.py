# 2-way partition
def read_file(path):
    with open(path, 'r') as f:
        lines = f.read().split('\n')
    size = int(lines[0])
    A = [int(n) for n in lines[1].split()]

    return A, size

def two_way_partition(A, size):
    B = []
    p = A[0]
    
    for i, n in enumerate(A):
        if i == 0:
            B.append(n)
            continue
        if n > p:
            B.append(n)
        else:
            B.insert(0,n)
    return B
        
    
if __name__ == "__main__":
    A = []
    A, size = read_file('rosalind_par.txt')

    B = two_way_partition(A, size)
    
    

    with open('output_par.txt', 'w') as f:
        line = ""
        for n in B:
            line += str(n)+" "
        f.write(line)
    f.close()
    
    
