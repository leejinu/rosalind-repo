def read_file(path):
    with open(path, 'r') as f:
        lines = f.read().split('\n')

    N = int(lines[0])
    edges = []
    for line in lines[1:]:
        temp = line.split()
        item = (int(temp[0]), int(temp[1]))

        edges.append(item)
    
    return N, edges

if __name__ == "__main__":
    edges = []
    N, edges = read_file('rosalind_tree.txt')

    print(N)
    print(edges)
    print(len(edges))

    
    minimum_edges = N - 1 - len(edges)

    print(minimum_edges)
